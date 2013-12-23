import ctypes
from ctypes import POINTER, c_int
from ctypes.wintypes import (DWORD, LPVOID, LPWSTR, BOOL, WORD, LPBYTE, HANDLE,
                             ULONG, HWND, LPCWSTR, HINSTANCE, HKEY, BYTE)
from .ctypes_utils import Win32Func, INPUT_PARAM, OUTPUT_PARAM


class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = (
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL)
    )


class STARTUPINFO(ctypes.Structure):
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


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = (
        ('hProcess', HANDLE),
        ('hThread', HANDLE),
        ('dwProcessId', DWORD),
        ('dwThreadId', DWORD)
    )


class SHELLEXECUTEINFO(ctypes.Structure):

    class _IconOrMonitor(ctypes.Union):
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


class SID_IDENTIFIER_AUTHORITY(ctypes.Structure):
    _fields_ = (('Value', BYTE * 6), )


class SID(ctypes.Structure):
    pass

ShellExecuteEx = Win32Func('ShellExecuteExW', 'shell32', BOOL,
                           [POINTER(SHELLEXECUTEINFO)])

CloseHandle = Win32Func('CloseHandle', 'kernel32', BOOL, [HANDLE])

WaitForSingleObject = Win32Func(
    'WaitForSingleObject', 'kernel32', DWORD, [HANDLE, DWORD],
    lambda result, *_: result != WAIT_FAILED)

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

CheckTokenMembership = Win32Func(
    'CheckTokenMembership', 'advapi32', BOOL,
    [(HANDLE, INPUT_PARAM, 'TokenHandle', None),
     (POINTER(SID), INPUT_PARAM, 'SidToCheck'),
     (POINTER(BOOL), OUTPUT_PARAM, 'IsMember')])

SetStdHandle = Win32Func('SetStdHandle', 'kernel32', BOOL, [DWORD, HANDLE])

GetStdHandle = Win32Func('GetStdHandle', 'kernel32', HANDLE, [DWORD],
                         lambda h, *_: h and h != INVALID_HANDLE_VALUE)

AttachConsole = Win32Func('AttachConsole', 'kernel32', BOOL,
                          [(DWORD, INPUT_PARAM, 'dwProcessId')])

CreateProcess = Win32Func(
    'CreateProcessW', 'kernel32', BOOL,
    [(LPCWSTR, INPUT_PARAM, 'lpApplicationName'),
     (LPWSTR, INPUT_PARAM, 'lpCommandLine'),
     (POINTER(SECURITY_ATTRIBUTES), INPUT_PARAM, 'lpProcessAttributes', None),
     (POINTER(SECURITY_ATTRIBUTES), INPUT_PARAM, 'lpThreadAttributes', None),
     (BOOL, INPUT_PARAM, 'bInheritHandles'),
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

WriteConsole = Win32Func(
    'WriteConsoleW', 'kernel32', BOOL,
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

#
# ShellExecuteEx()
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
#
# GetStdHandle()
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

INVALID_HANDLE_VALUE = -1

# AttachConsole()
ATTACH_PARENT_PROCESS = -1
ERROR_ACCESS_DENIED = 5

# Timeouts
INFINITE = 0xFFFFFFFF

# DuplicateHandle()
DUPLICATE_CLOSE_SOURCE = 0x00000001
DUPLICATE_SAME_ACCESS = 0x00000002

# Sids, impersonation tokens, yadda yadda yadda
SECURITY_BUILTIN_DOMAIN_RID = 0x00000020
SECURITY_NT_AUTHORITY = SID_IDENTIFIER_AUTHORITY((0, 0, 0, 0, 0, 5))

DOMAIN_ALIAS_RID_ADMINS = 0x00000220
DOMAIN_ALIAS_RID_USERS = 0x00000221
DOMAIN_ALIAS_RID_GUESTS = 0x00000222
DOMAIN_ALIAS_RID_POWER_USERS = 0x00000223


#
# WaitForMultipleObjectsEx() and friends

QS_ALLEVENTS = 0x04BF
QS_ALLINPUT = 0x04FF
QS_ALLPOSTMESSAGE = 0x0100
QS_HOTKEY = 0x0080
QS_INPUT = 0x407
QS_KEY = 0x0001
QS_MOUSE = 0x0006
QS_MOUSEBUTTON = 0x0004
QS_MOUSEMOVE = 0x0002
QS_PAINT = 0x0020
QS_POSTMESSAGE = 0x0008
QS_RAWINPUT = 0x0400
QS_SENDMESSAGE = 0x0040
QS_TIMER = 0x0010

MWMO_ALERTABLE = 0x0002
MWMO_INPUTAVAILABLE = 0x0004
MWMO_WAITALL = 0x0001

WAIT_ABANDONED = 0x00000080
WAIT_ABANDONED_0 = 0x00000080
WAIT_FAILED = 0xFFFFFFFF
WAIT_IO_COMPLETION = 0x000000C0
WAIT_OBJECT_0 = 0x00000000
WAIT_TIMEOUT = 0x00000102
