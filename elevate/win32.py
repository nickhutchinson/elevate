import ctypes
from ctypes import POINTER, c_int, c_wchar_p
from ctypes.wintypes import *
from .ctypes_utils import OUTPUT_PARAM, Win32Func
from .libc import c_intptr
from ._constants import *

HCURSOR = HICON
LRESULT = c_intptr
LONG_PTR = c_intptr

###############################################################################
# Window functions

WNDPROC = ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)


class WNDCLASSEX(ctypes.Structure):
    _fields_ = (
        ('cbSize', UINT),
        ('style', UINT),
        ('lpfnWndProc', WNDPROC),
        ('cbClsExtra', c_int),
        ('cbWndExtra', c_int),
        ('hInstance', HINSTANCE),
        ('hIcon', HICON),
        ('hCursor', HCURSOR),
        ('hbrBackground', HBRUSH),
        ('lpszMenuName', LPCWSTR),
        ('lpszClassName', LPCWSTR),
        ('hIconSm', HICON),
    )

RegisterClassEx = Win32Func('RegisterClassExW', 'user32', ATOM,
                            [POINTER(WNDCLASSEX)], lambda atom, *_: atom)

GetWindowLongPtr = Win32Func(
    'GetWindowLongPtrW', 'user32', LONG_PTR,
    [('hWnd', HWND),
     ('nIndex', c_int)])

SetWindowLongPtr = Win32Func(
    'SetWindowLongPtrW', 'user32', LONG_PTR,
    [('hWnd', HWND),
     ('nIndex', c_int),
     ('dwNewLong', LONG_PTR)])


class CREATESTRUCT(ctypes.Structure):
    _fields_ = (
        ('lpCreateParams', LPVOID),
        ('hInstance', HINSTANCE),
        ('hMenu', HMENU),
        ('hwndParent', HWND),
        ('cy', c_int),
        ('cx', c_int),
        ('y', c_int),
        ('x', c_int),
        ('style', LONG),
        ('lpszName', LPCWSTR),
        ('lpszClass', LPCWSTR),
        ('dwExStyle', DWORD))

CreateWindowEx = Win32Func(
    'CreateWindowExW', 'user32', HWND,
    [('dwExStyle', DWORD),
     ('lpClassName', LPCWSTR),
     ('lpWindowName', LPCWSTR, None),
     ('dwStyle', DWORD),
     ('x', c_int, 0),
     ('y', c_int, 0),
     ('nWidth', c_int, 0),
     ('nHeight', c_int, 0),
     ('hWndParent', HWND, None),
     ('hMenu', HMENU, None),
     ('hInstance', HINSTANCE),
     ('lpParam', LPVOID)])

DefWindowProc = Win32Func(
    'DefWindowProcW', 'user32', LRESULT,
    [('hWnd', HWND),
     ('Msg', UINT),
     ('wParam', WPARAM),
     ('lParam', LPARAM)])

PeekMessage = Win32Func(
    'PeekMessageW', 'user32', BOOL,
    [('lpMsg', POINTER(MSG)),
     ('hWnd', HWND, None),
     ('wMsgFilterMin', UINT, 0),
     ('wMsgFilterMax', UINT, 0),
     ('wRemoveMsg', UINT, PM_REMOVE)],
    success_predicate=None)

TranslateMessage = Win32Func('TranslateMessage', 'user32',
                             BOOL, [POINTER(MSG)], success_predicate=None)

DispatchMessage = Win32Func('DispatchMessageW', 'user32',
                            LRESULT, [POINTER(MSG)], success_predicate=None)

###############################################################################

DuplicateHandle = Win32Func(
    'DuplicateHandle', 'kernel32', BOOL,
    [('hSourceProcessHandle', HANDLE),
     ('hSourceHandle', HANDLE),
     ('hTargetProcessHandle', HANDLE),
     ('lpTargetHandle', POINTER(HANDLE), OUTPUT_PARAM),
     ('dwDesiredAccess', DWORD, 0),
     ('bInheritHandle', BOOL, False),
     ('dwOptions', DWORD, DUPLICATE_SAME_ACCESS)])

CloseHandle = Win32Func('CloseHandle', 'kernel32', BOOL, [HANDLE])

###############################################################################


class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = (
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL)
    )


class SID(ctypes.Structure):
    pass

AllocateAndInitializeSid = Win32Func(
    'AllocateAndInitializeSid', 'advapi32', BOOL,
    [('pIdentifierAuthority', POINTER(SID_IDENTIFIER_AUTHORITY)),
     ('nSubAuthorityCount', BYTE, 0),
     ('dwSubAuthority0', DWORD, 0),
     ('dwSubAuthority1', DWORD, 0),
     ('dwSubAuthority2', DWORD, 0),
     ('dwSubAuthority3', DWORD, 0),
     ('dwSubAuthority4', DWORD, 0),
     ('dwSubAuthority5', DWORD, 0),
     ('dwSubAuthority6', DWORD, 0),
     ('dwSubAuthority7', DWORD, 0),
     ('pSid', POINTER(POINTER(SID)), OUTPUT_PARAM)])

FreeSid = Win32Func('FreeSid', 'advapi32', POINTER(SID), [POINTER(SID)])

CheckTokenMembership = Win32Func(
    'CheckTokenMembership', 'advapi32', BOOL,
    [('TokenHandle', HANDLE, None),
     ('SidToCheck', POINTER(SID)),
     ('IsMember', POINTER(BOOL), OUTPUT_PARAM)])

###############################################################################

SetStdHandle = Win32Func('SetStdHandle', 'kernel32', BOOL, [DWORD, HANDLE])

GetStdHandle = Win32Func('GetStdHandle', 'kernel32', HANDLE, [DWORD],
                         lambda h, *_: h and h != INVALID_HANDLE_VALUE)

AttachConsole = Win32Func('AttachConsole', 'kernel32', BOOL,
                          [('dwProcessId', DWORD)])

WriteConsole = Win32Func(
    'WriteConsoleW', 'kernel32', BOOL,
    [('hConsoleOutput', HANDLE),
     ('lpBuffer', LPCWSTR),
     ('nNumberOfCharsToWrite', DWORD),
     ('lpNumberOfCharsWritten', POINTER(DWORD), OUTPUT_PARAM),
     ('lpReserved', LPVOID, None)])

###############################################################################
# Process management


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

CreateProcess = Win32Func(
    'CreateProcessW', 'kernel32', BOOL,
    [('lpApplicationName', LPCWSTR),
     ('lpCommandLine', LPWSTR),
     ('lpProcessAttributes', POINTER(SECURITY_ATTRIBUTES), None),
     ('lpThreadAttributes', POINTER(SECURITY_ATTRIBUTES), None),
     ('bInheritHandles', BOOL),
     ('dwCreationFlags', DWORD, 0),
     ('lpEnvironment', LPVOID, None),
     ('lpCurrentDirectory', LPCWSTR, None),
     ('lpStartupInfo', POINTER(STARTUPINFO)),
     ('lpProcessInformation', POINTER(PROCESS_INFORMATION), OUTPUT_PARAM)])

ShellExecuteEx = Win32Func('ShellExecuteExW', 'shell32', BOOL,
                           [POINTER(SHELLEXECUTEINFO)])

GetCurrentProcess = Win32Func('GetCurrentProcess', 'kernel32', HANDLE, [])

GetModuleHandleEx = Win32Func(
    'GetModuleHandleExW', 'kernel32', BOOL,
    [('dwFlags', DWORD),
     ('lpModuleName', c_wchar_p),
     ('phModule', POINTER(HMODULE), OUTPUT_PARAM)])

###############################################################################


MsgWaitForMultipleObjectsEx = Win32Func(
    'MsgWaitForMultipleObjectsEx', 'user32', DWORD,
    [('nCount', DWORD),
     ('pHandles', POINTER(HANDLE)),
     ('dwMilliseconds', DWORD),
     ('dwWakeMask', DWORD),
     ('dwFlags', DWORD)])

WaitForSingleObject = Win32Func(
    'WaitForSingleObject', 'kernel32', DWORD, [HANDLE, DWORD],
    lambda result, *_: result != WAIT_FAILED)

MessageBox = Win32Func(
    'MessageBoxW', 'user32', c_int,
    [('hWnd', HWND, None),
     ('lpText', LPCWSTR),
     ('lpCaption', LPCWSTR, None),
     ('uType', UINT, 0)])
