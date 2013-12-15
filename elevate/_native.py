import ctypes
from ctypes import POINTER, Structure, Union, WinError, c_int, WINFUNCTYPE
from ctypes.wintypes import DWORD, LPVOID, LPWSTR, BOOL, WORD, LPBYTE, \
    HANDLE, ULONG, HWND, LPCWSTR, HINSTANCE, HKEY, BYTE
from collections import Sequence

INPUT_PARAM = 1
OUTPUT_PARAM = 2

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

SECURITY_NT_AUTHORITY = SID_IDENTIFIER_AUTHORITY((0, 0, 0, 0, 0, 5))


class SID(Structure):
    pass

SEE_MASK_DEFAULT = 0x00000000
SEE_MASK_CLASSNAME = 0x00000001
SEE_MASK_CLASSKEY = 0x00000003
SEE_MASK_IDLIST = 0x00000004
SEE_MASK_INVOKEIDLIST = 0x0000000C
SEE_MASK_ICON = 0x00000010
SEE_MASK_HOTKEY = 0x00000020
SEE_MASK_NOCLOSEPROCESS = 0x00000040
SEE_MASK_CONNECTNETDRV = 0x00000080
SEE_MASK_NOASYNC = 0x00000100
SEE_MASK_FLAG_DDEWAIT = 0x00000100
SEE_MASK_DOENVSUBST = 0x00000200
SEE_MASK_FLAG_NO_UI = 0x00000400
SEE_MASK_UNICODE = 0x00004000
SEE_MASK_NO_CONSOLE = 0x00008000
SEE_MASK_ASYNCOK = 0x00100000
SEE_MASK_NOQUERYCLASSSTORE = 0x01000000
SEE_MASK_HMONITOR = 0x00200000
SEE_MASK_NOZONECHECKS = 0x00800000
SEE_MASK_WAITFORINPUTIDLE = 0x02000000

SW_HIDE = 0
SW_MAXIMIZE = 3
SW_MINIMIZE = 6
SW_RESTORE = 9
SW_SHOW = 5
SW_SHOWDEFAULT = 10
SW_SHOWMAXIMIZED = 3
SW_SHOWMINIMIZED = 2
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA = 8
SW_SHOWNOACTIVATE = 4
SW_SHOWNORMAL = 1

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

ATTACH_PARENT_PROCESS = -1

WAIT_ABANDONED = 0x00000080
WAIT_OBJECT_0 = 0x00000000
WAIT_TIMEOUT = 0x00000102
WAIT_FAILED = 0xFFFFFFFF

INFINITE = 0xFFFFFFFF

SECURITY_BUILTIN_DOMAIN_RID = 0x00000020

DOMAIN_ALIAS_RID_ADMINS = 0x00000220

class DomainAliasRID:
    ADMINS = 0x00000220
    USERS = 0x00000221
    GUESTS = 0x00000222
    POWER_USERS = 0x00000223


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
        return param_flags if len(param_flags) != 0 else (INPUT_PARAM, )

    module = getattr(ctypes.windll, module_name)
    arg_types = (head(tup) for tup in argument_descriptors)
    param_flags = tuple(get_param_flags(tup) for tup in argument_descriptors)

    prototype = WINFUNCTYPE(
        result_type, *arg_types, use_last_error=True)
    function = prototype((function_name, module), param_flags)

    if success_predicate:
        def errcheck(result, func, args):
            is_unknown_restype = success_predicate is DEFAULT_SUCCESS \
                and result_type != BOOL
            if not is_unknown_restype \
                and not success_predicate(result, func, args):
                raise WinError(get_last_error())
            return args

        function.errcheck = errcheck

    return function

ShellExecuteEx = Win32Func('ShellExecuteExW', 'shell32', BOOL,
                           [POINTER(SHELLEXECUTEINFO)])

CloseHandle = Win32Func('CloseHandle', 'kernel32', BOOL, [HANDLE])

WaitForSingleObject = Win32Func('WaitForSingleObject', 'kernel32', DWORD,
    [HANDLE, DWORD], lambda result, *_: result != WAIT_FAILED)

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

AttachConsole = Win32Func('AttachConsole', 'kernel32', BOOL,
                          [(DWORD, INPUT_PARAM, 'dwProcessId')])
