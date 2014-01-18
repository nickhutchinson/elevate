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
    absolute_script_path = os.path.abspath(sys.argv[0])
    try:
        return utilities.get_unc_name_for_path(absolute_script_path)
    except OSError as e:
        if e.winerror in (win32.ERROR_NOT_CONNECTED, win32.ERROR_BAD_DEVICE):
            return absolute_script_path
        else:
            raise


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
        StandardHandleInfo('stdin', 'CONIN$', win32.STD_INPUT_HANDLE, 
                           libc.STDIN_FILENO, 'r'),
        StandardHandleInfo('stdout', 'CONOUT$', win32.STD_OUTPUT_HANDLE,
                           libc.STDOUT_FILENO, 'w'),
        StandardHandleInfo('stderr', 'CONOUT$', win32.STD_ERROR_HANDLE,
                           libc.STDERR_FILENO, 'w'))

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
                     getattr(libc, handle_info.name))


def main():

    if utilities.is_elevated():
        class WndProc(utilities.WndProc):
            def wnd_proc(self, window_handle, message_id, w_param, l_param):
                return super().wnd_proc(window_handle, message_id, w_param,
                                        l_param)

        window = utilities.create_window(WndProc(), win32.WS_EX_OVERLAPPEDWINDOW,
                                         win32.WS_OVERLAPPEDWINDOW|win32.WS_VISIBLE, "Foobar")
        print("before")
        # windowed subsystem
        connect_to_parent_console()
        print("printafter\n")
        write_console("writeconsoleafer\n")
        libc.printf("printf after\n")
        utilities.RunLoop().run()
        assert window

    else:
        # console subsystem
        exec_info = win32.SHELLEXECUTEINFO()
        exec_info.size = ctypes.sizeof(exec_info)
        exec_info.file = pythonw_interpreter()
        exec_info.parameters = utilities.argv_to_command_line([whereami()])
        exec_info.verb = "runas"
        exec_info.mask = (win32.SEE_MASK_FLAG_NO_UI
                          | win32.SEE_MASK_NOASYNC
                          | win32.SEE_MASK_NOCLOSEPROCESS
                          | win32.SEE_MASK_UNICODE)
        exec_info.show = win32.SW_SHOWNORMAL

        win32.ShellExecuteEx(ctypes.byref(exec_info))
        win32.WaitForSingleObject(exec_info.process, win32.INFINITE)
        win32.CloseHandle(exec_info.process)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        win32.MessageBox(text="{}".format(traceback.format_exc()))
