import time
import ctypes
import traceback
import elevate 
import msvcrt
import os
import re
import sys
from elevate import (SECURITY_NT_AUTHORITY, SECURITY_BUILTIN_DOMAIN_RID,
                     DOMAIN_ALIAS_RID_ADMINS, SEE_MASK_FLAG_NO_UI,
                     SEE_MASK_NOASYNC, SEE_MASK_NOCLOSEPROCESS,
                     SEE_MASK_UNICODE, SW_SHOWNORMAL, INFINITE, WAIT_FAILED)
def is_elevated():
    admin_sid = None
    try:
        admin_sid = elevate.AllocateAndInitializeSid(
            ctypes.byref(SECURITY_NT_AUTHORITY),
            2, SECURITY_BUILTIN_DOMAIN_RID, DOMAIN_ALIAS_RID_ADMINS)

        return bool(elevate.CheckTokenMembership(SidToCheck=admin_sid))
    finally:
        if admin_sid: elevate.FreeSid(admin_sid)


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
    return elevate.DuplicateHandle(
        elevate.GetCurrentProcess(), h, elevate.GetCurrentProcess(), 0,
        False, elevate.DUPLICATE_SAME_ACCESS)

def write_console(s, console=elevate.STD_OUTPUT_HANDLE):
    wcslen = ctypes.cdll.msvcrt.wcslen
    wcslen.argtypes = [ctypes.c_wchar_p]
    wcslen.restype = ctypes.c_size_t

    wide_string = ctypes.c_wchar_p(s)
    elevate.WriteConsole(elevate.GetStdHandle(console),
                         wide_string, cslen(wide_string))

def connect_to_parent_console():
    try:
        elevate.AttachConsole(elevate.ATTACH_PARENT_PROCESS)
    except OSError as e:
        if e.winerror != elevate.ERROR_ACCESS_DENIED:
            raise
    standard_handles = ((elevate.STD_INPUT_HANDLE, 0, 'stdin', 'r'),
                        (elevate.STD_OUTPUT_HANDLE, 1, 'stdout', 'w'),
                        (elevate.STD_ERROR_HANDLE, 2, 'stderr', 'w'))

    for handle_constant, target_fd, stream_name, mode in standard_handles:
        stream = getattr(sys, stream_name)
        if stream: stream.flush()
        handle = duplicate_handle(elevate.GetStdHandle(handle_constant))
        fd = msvcrt.open_osfhandle(handle, os.O_TEXT)
        os.dup2(fd, target_fd)
        os.close(fd)
        stream = os.fdopen(target_fd, mode)
        setattr(sys, stream_name, stream)


def main():
    if is_elevated():
        # windowed subsystem
        connect_to_parent_console()
        print("Hi!")
        time.sleep(5)
    else:
        # console subsystem
        exec_info = elevate.SHELLEXECUTEINFO()
        exec_info.cbSize = ctypes.sizeof(exec_info)
        exec_info.lpFile = pythonw_interpreter()
        exec_info.lpParameters = argv_to_command_line([ whereami() ])
        exec_info.lpVerb = "runas"
        exec_info.fMask = (SEE_MASK_FLAG_NO_UI | SEE_MASK_NOASYNC 
                        | SEE_MASK_NOCLOSEPROCESS | SEE_MASK_UNICODE)
        exec_info.nShow = SW_SHOWNORMAL

        result = elevate.ShellExecuteEx(ctypes.byref(exec_info))

        # elevate.WaitForSingleObject(exec_info.hProcess, INFINITE)
        time.sleep(10)

        elevate.CloseHandle(exec_info.hProcess)


        # printf("hi");
        # //printf("hello from privileged child1!\n");

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
    paramflags = (1, "hwnd", 0), (1, "text"), (1, "caption", "Message"), (1, "flags", 0)
    MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)
    
    try:
        main()
    except Exception as e:
        MessageBox(text="{}".format(traceback.format_exc()))
