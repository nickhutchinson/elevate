from collections import Sequence

import ctypes
from ctypes import (POINTER, Structure, Union, WinError, c_int, WINFUNCTYPE,
                    get_last_error)
from ctypes.wintypes import (DWORD, LPVOID, LPWSTR, BOOL, WORD, LPBYTE, HANDLE,
                             ULONG, HWND, LPCWSTR, HINSTANCE, HKEY, BYTE)
from . import win32_constants as constants

class SECURITY_ATTRIBUTES(Structure):
    _fields_ = (
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL)
    )

class STARTUPINFO(Structure):
    _fields_ = (
        ('cb', DWORD),
        ('lpReserved', LPWSTR),
        ('lpDesktop', LPWSTR),
        ('lpTitle', LPWSTR),
        ('dwX', DWORD),
        ('dwY', DWORD),
        ('dwXSize', DWORD),
        ('dwYSize', DWORD),
        ('dwXCountChars', DWORD),
        ('dwYCountChars', DWORD),
        ('dwFillAttribute', DWORD),
        ('dwFlags', DWORD),
        ('wShowWindow', WORD),
        ('cbReserved2', WORD),
        ('lpReserved2', LPBYTE),
        ('hStdInput', HANDLE),
        ('hStdOutput', HANDLE),
        ('hStdError', HANDLE)
    )

class PROCESS_INFORMATION(Structure):
    _fields_ = (
        ('hProcess', HANDLE),
        ('hThread', HANDLE),
        ('dwProcessId', DWORD),
        ('dwThreadId', DWORD)
    )

class SHELLEXECUTEINFO(Structure):
    class _IconOrMonitor(Union):
        _fields_ = (
            ('hIcon', HANDLE),
            ('hMonitor', HANDLE)
        )

    _anonymous_ = ('iconOrMonitor',)
    _fields_ = (
        ('cbSize', DWORD),
        ('fMask', ULONG),
        ('hwnd', HWND),
        ('lpVerb', LPCWSTR),
        ('lpFile', LPCWSTR),
        ('lpParameters', LPCWSTR),
        ('lpDirectory', LPCWSTR),
        ('nShow', c_int),
        ('hInstApp', HINSTANCE),
        ('lpIDList', LPVOID),
        ('lpClass', LPCWSTR),
        ('hkeyClass', HKEY),
        ('dwHotKey', DWORD),
        ('iconOrMonitor', _IconOrMonitor),
        ('hProcess', HANDLE)
    )

class SID_IDENTIFIER_AUTHORITY(Structure):
    _fields_ = (('Value', BYTE * 6), )

SECURITY_NT_AUTHORITY = (SID_IDENTIFIER_AUTHORITY)((0, 0, 0, 0, 0, 5))

class SID(Structure):
    pass

INPUT_PARAM = 1
OUTPUT_PARAM = 2

def DEFAULT_SUCCESS(result, *args):
    return result != 0

def Win32Func(function_name, module_name, result_type, argument_descriptors,
              success_predicate=DEFAULT_SUCCESS):
    def head(x):
        return x[0] if isinstance(x, Sequence) else x

    def tail(x):
        return x[1:] if isinstance(x, Sequence) else tuple()

    def get_param_flags(obj):
        param_flags = tail(obj)
        return param_flags if param_flags else (INPUT_PARAM, )

    module = getattr(ctypes.windll, module_name)
    arg_types = (head(tup) for tup in argument_descriptors)
    param_flags = tuple(get_param_flags(tup) for tup in argument_descriptors)

    prototype = WINFUNCTYPE(
        result_type, *arg_types, use_last_error=True)
    function = prototype((function_name, module), param_flags)

    if success_predicate:
        def errcheck(result, func, args):
            is_unknown_restype = (success_predicate is DEFAULT_SUCCESS
                and result_type != BOOL)
            if (not is_unknown_restype 
                and not success_predicate(result, func, args)):
                raise WinError(get_last_error())
            return args

        function.errcheck = errcheck

    return function

ShellExecuteEx = Win32Func('ShellExecuteExW', 'shell32', BOOL,
                           [POINTER(SHELLEXECUTEINFO)])

CloseHandle = Win32Func('CloseHandle', 'kernel32', BOOL, [HANDLE])

WaitForSingleObject = Win32Func('WaitForSingleObject', 'kernel32', DWORD,
    [HANDLE, DWORD], lambda result, *_: result != constants.WAIT_FAILED)

AllocateAndInitializeSid = Win32Func(
    'AllocateAndInitializeSid', 'advapi32', BOOL, 
    [(POINTER(SID_IDENTIFIER_AUTHORITY), INPUT_PARAM, 'pIdentifierAuthority'),
    (BYTE, INPUT_PARAM, 'nSubAuthorityCount', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority0', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority1', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority2', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority3', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority4', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority5', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority6', 0),
    (DWORD, INPUT_PARAM, 'dwSubAuthority7', 0),
    (POINTER(POINTER(SID)), OUTPUT_PARAM, 'pSid')])

FreeSid = Win32Func('FreeSid', 'advapi32', POINTER(SID), [POINTER(SID)])

CheckTokenMembership = Win32Func('CheckTokenMembership', 'advapi32', BOOL, 
    [(HANDLE, INPUT_PARAM, 'TokenHandle', None),
    (POINTER(SID), INPUT_PARAM, 'SidToCheck'),
    (POINTER(BOOL), OUTPUT_PARAM, 'IsMember')])

SetStdHandle = Win32Func('SetStdHandle', 'kernel32', BOOL, [DWORD, HANDLE])


def is_handle_valid(h, *_):
    return h != 0 and h != constants.INVALID_HANDLE_VALUE

GetStdHandle = Win32Func('GetStdHandle', 'kernel32', HANDLE, [DWORD],
                         is_handle_valid)

AttachConsole = Win32Func('AttachConsole', 'kernel32', BOOL,
                          [(DWORD, INPUT_PARAM, 'dwProcessId')])

CreateProcess = Win32Func(
    'CreateProcessW', 'kernel32', BOOL,
    [(LPCWSTR, INPUT_PARAM, 'lpApplicationName'),
    (LPWSTR, INPUT_PARAM, 'lpCommandLine'),
    (POINTER(SECURITY_ATTRIBUTES), INPUT_PARAM, 'lpProcessAttributes', None),
    (POINTER(SECURITY_ATTRIBUTES), INPUT_PARAM, 'lpThreadAttributes', None),
    (BOOL, INPUT_PARAM, 'bInheritHandles', None),
    (DWORD, INPUT_PARAM, 'dwCreationFlags', 0),
    (LPVOID, INPUT_PARAM, 'lpEnvironment', None),
    (LPCWSTR, INPUT_PARAM, 'lpCurrentDirectory', None),
    (POINTER(STARTUPINFO), INPUT_PARAM, 'lpStartupInfo'),
    (POINTER(PROCESS_INFORMATION), OUTPUT_PARAM, 'lpProcessInformation')])

DuplicateHandle = Win32Func(
    'DuplicateHandle', 'kernel32', BOOL, 
    [(HANDLE, INPUT_PARAM, 'hSourceProcessHandle'),
     (HANDLE, INPUT_PARAM, 'hSourceHandle'),
     (HANDLE, INPUT_PARAM, 'hTargetProcessHandle'),
     (POINTER(HANDLE), OUTPUT_PARAM, 'lpTargetHandle'),
     (DWORD, INPUT_PARAM, 'dwDesiredAccess'),
     (BOOL, INPUT_PARAM, 'bInheritHandle'),
     (DWORD, INPUT_PARAM, 'dwOptions')])

GetCurrentProcess = Win32Func('GetCurrentProcess', 'kernel32', HANDLE, [])

WriteConsole = Win32Func('WriteConsoleW', 'kernel32', BOOL,
    [(HANDLE, INPUT_PARAM, 'hConsoleOutput'),
    (LPCWSTR, INPUT_PARAM, 'lpBuffer'),
    (DWORD, INPUT_PARAM, 'nNumberOfCharsToWrite'),
    (POINTER(DWORD), OUTPUT_PARAM, 'lpNumberOfCharsWritten'),
    (LPVOID, INPUT_PARAM, 'lpReserved', None)])

MsgWaitForMultipleObjectsEx = Win32Func(
    'MsgWaitForMultipleObjectsEx', 'user32', DWORD,
    [(DWORD, INPUT_PARAM, 'nCount'),
    (POINTER(HANDLE), INPUT_PARAM, 'pHandles'),
    (DWORD, INPUT_PARAM, 'dwMilliseconds'),
    (DWORD, INPUT_PARAM, 'dwWakeMask'),
    (DWORD, INPUT_PARAM, 'dwFlags')])
