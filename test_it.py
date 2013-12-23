import time
import ctypes
import traceback
from collections import namedtuple
import os
import re
import sys

import elevate.win32 as win32
import elevate.libc as libc


def is_elevated():
    admin_sid = None
    try:
        admin_sid = win32.AllocateAndInitializeSid(
            ctypes.byref(win32.SECURITY_NT_AUTHORITY),
            2, win32.SECURITY_BUILTIN_DOMAIN_RID,
            win32.DOMAIN_ALIAS_RID_ADMINS)

        return bool(win32.CheckTokenMembership(SidToCheck=admin_sid))
    finally:
        if admin_sid:
            win32.FreeSid(admin_sid)


def argv_to_command_line(args):
    def escape_arg(arg):
        arg = re.sub(r'(\\*)"', r'\1\1\"', arg)
        arg = re.sub(r'(\\+)$', r'\1\1', arg)
        return "".join(('"', arg, '"'))

    return " ".join(escape_arg(arg) for arg in args)


def python_interpreter():
    import sys
    return sys.executable


def pythonw_interpreter():
    head, tail = os.path.split(python_interpreter())
    base, ext = os.path.splitext(tail)
    return os.path.join(head, 'pythonw' + ext)


def whereami():
    return os.path.abspath(sys.argv[0])


def duplicate_handle(h):
    return win32.DuplicateHandle(
        win32.GetCurrentProcess(), h, win32.GetCurrentProcess(), 0,
        False, win32.DUPLICATE_SAME_ACCESS)


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

    std_streams = libc.get_std_streams()

    for handle_info in standard_handles:
        stream = getattr(sys, handle_info.name)
        if stream:
            stream.flush()

        handle = duplicate_handle(
            win32.GetStdHandle(handle_info.win32_constant))
        fd = libc.open_osfhandle(handle, libc.O_TEXT)
        libc.dup2(fd, handle_info.fd)
        libc.close(fd)

        setattr(sys, handle_info.name,
                libc.fdopen(handle_info.fd, handle_info.mode))

        # associate C stdout/stdin/stderr with the console
        libc.freopen(handle_info.filename, handle_info.mode,
                     std_streams[handle_info.fd])


def main():
    print("before")
    if is_elevated():
        # windowed subsystem
        connect_to_parent_console()
        print("printafter\n")
        write_console("writeconsoleafer\n")

        libc.printf("printf after\n")

        time.sleep(5)
    else:
        # console subsystem
        exec_info = win32.SHELLEXECUTEINFO()
        exec_info.cbSize = ctypes.sizeof(exec_info)
        exec_info.lpFile = pythonw_interpreter()
        exec_info.lpParameters = argv_to_command_line([whereami()])
        exec_info.lpVerb = "runas"
        exec_info.fMask = (SEE_MASK_FLAG_NO_UI | SEE_MASK_NOASYNC
                           | SEE_MASK_NOCLOSEPROCESS | SEE_MASK_UNICODE)
        exec_info.nShow = SW_SHOWNORMAL

        result = win32.ShellExecuteEx(ctypes.byref(exec_info))

        # win32.WaitForSingleObject(exec_info.hProcess, INFINITE)
        time.sleep(10)

        win32.CloseHandle(exec_info.hProcess)


        # STARTUPINFOW startup_info{ sizeof(startup_info) };
        # PROCESS_INFORMATION process_info;
        # BOOL result = CreateProcessW(L"C:/cygwin64/bin/dir.exe", L"dir.exe --size",
        #  nullptr /*process attrs*/, nullptr /*thread attrs*/, TRUE,
        #  CREATE_UNICODE_ENVIRONMENT, nullptr /*env*/, nullptr /*cwd*/,
        #  &startup_info, &process_info);
        # Sleep(4000);
if __name__ == '__main__':
    from ctypes import c_int, WINFUNCTYPE, windll
    from ctypes.wintypes import HWND, LPCWSTR, UINT
    prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
    paramflags = ((1, "hwnd", 0), (1, "text"), (1, "caption", "Message"),
                  (1, "flags", 0))
    MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)

    try:
        main()
    except Exception as e:
        MessageBox(text="{}".format(traceback.format_exc()))
