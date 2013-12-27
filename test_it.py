import ctypes
import traceback
from collections import namedtuple
import os
import sys

from elevate import win32, libc, utilities


def python_interpreter():
    return sys.executable


def pythonw_interpreter():
    head, tail = os.path.split(python_interpreter())
    base, ext = os.path.splitext(tail)
    return os.path.join(head, 'pythonw' + ext)


def whereami():
    return os.path.abspath(sys.argv[0])


def write_console(s, console=win32.STD_OUTPUT_HANDLE):
    wide_string = ctypes.c_wchar_p(s)
    win32.WriteConsole(win32.GetStdHandle(console),
                       wide_string, libc.wcslen(wide_string))


def print_console(*args):
    write_console("%s\n" % args)


def connect_to_parent_console():
    try:
        win32.AttachConsole(win32.ATTACH_PARENT_PROCESS)
    except OSError as e:
        if e.winerror != win32.ERROR_ACCESS_DENIED:
            raise

    StandardHandleInfo = namedtuple('StandardHandleInfo',
                                    'name filename win32_constant fd mode')
    standard_handles = (
        StandardHandleInfo(
            'stdin', 'CONIN$', win32.STD_INPUT_HANDLE, 0, 'r'),
        StandardHandleInfo(
            'stdout', 'CONOUT$', win32.STD_OUTPUT_HANDLE, 1, 'w'),
        StandardHandleInfo(
            'stderr', 'CONOUT$', win32.STD_ERROR_HANDLE, 2, 'w'))

    c_standard_streams = libc.get_std_streams()

    for handle_info in standard_handles:
        stream = getattr(sys, handle_info.name)
        if stream:
            stream.flush()

        handle = win32.DuplicateHandle(
            win32.GetCurrentProcess(),
            win32.GetStdHandle(handle_info.win32_constant),
            win32.GetCurrentProcess())
        fd = libc.open_osfhandle(handle, libc.O_TEXT)
        libc.dup2(fd, handle_info.fd)
        libc.close(fd)

        # associate Python's sys.(stdin|stdout|stderr) with the console
        setattr(sys, handle_info.name,
                libc.fdopen(handle_info.fd, handle_info.mode))

        # associate C's (stdin|stdout|stderr) with the console
        libc.freopen(handle_info.filename, handle_info.mode,
                     c_standard_streams[handle_info.fd])


def main():
    # class Wproc(utilities.WndProc):
    #     def wnd_proc(self, window_handle, message_id, wParam, lParam):
    #         print(window_handle, message_id, wParam, lParam)
    #         return super().wnd_proc(window_handle, message_id, wParam, lParam)

    # window = utilities.create_window(Wproc(), 0x00040000, 0x10000000,
    #                                  b"Foobar")
    # assert window

    if utilities.is_elevated():
        print("before")
        # windowed subsystem
        connect_to_parent_console()
        print("printafter\n")
        write_console("writeconsoleafer\n")


        
        libc.printf("printf after\n")
        utilities.RunLoop().run()

    else:
        # console subsystem
        exec_info = win32.SHELLEXECUTEINFO()
        exec_info.cbSize = ctypes.sizeof(exec_info)
        exec_info.lpFile = pythonw_interpreter()
        exec_info.lpParameters = utilities.argv_to_command_line([whereami()])
        exec_info.lpVerb = "runas"
        exec_info.fMask = (win32.SEE_MASK_FLAG_NO_UI
                           | win32.SEE_MASK_NOASYNC
                           | win32.SEE_MASK_NOCLOSEPROCESS
                           | win32.SEE_MASK_UNICODE)
        exec_info.nShow = win32.SW_SHOWNORMAL

        win32.ShellExecuteEx(ctypes.byref(exec_info))
        win32.WaitForSingleObject(exec_info.hProcess, win32.INFINITE)
        win32.CloseHandle(exec_info.hProcess)

if __name__ == '__main__':
    # try:
    main()
    # except Exception as e:
        # win32.MessageBox(lpText="{}".format(traceback.format_exc()))
