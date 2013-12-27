import ctypes
from ctypes import POINTER, c_int
from ctypes.wintypes import *
from .ctypes_utils import Win32Func, INPUT_PARAM, OUTPUT_PARAM
from .libc import c_intptr
from ._constants import *

HCURSOR = HICON
LRESULT = c_intptr
LONG_PTR = c_intptr

###############################################################################
# Window functions
###############################################################################

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

GetWindowLongPtr = Win32Func('GetWindowLongPtrW', 'user32', LONG_PTR,
    [(HWND, INPUT_PARAM, 'hWnd'),
     (c_int, INPUT_PARAM, 'nIndex')])

SetWindowLongPtr = Win32Func('SetWindowLongPtrW', 'user32', LONG_PTR,
    [(HWND, INPUT_PARAM, 'hWnd'),
     (c_int, INPUT_PARAM, 'nIndex'),
     (LONG_PTR, INPUT_PARAM, 'dwNewLong')])

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
    [(DWORD, INPUT_PARAM, 'dwExStyle'),
     (LPCWSTR, INPUT_PARAM, 'lpClassName'),
     (LPCWSTR, INPUT_PARAM, 'lpWindowName', None),
     (DWORD, INPUT_PARAM, 'dwStyle'),
     (c_int, INPUT_PARAM, 'x', 0),
     (c_int, INPUT_PARAM, 'y', 0),
     (c_int, INPUT_PARAM, 'nWidth', 0),
     (c_int, INPUT_PARAM, 'nHeight', 0),
     (HWND, INPUT_PARAM, 'hWndParent', None),
     (HMENU, INPUT_PARAM, 'hMenu', None),
     (HINSTANCE, INPUT_PARAM, 'hInstance'),
     (LPVOID, INPUT_PARAM, 'lpParam')])

DefWindowProc = Win32Func('DefWindowProcW', 'user32', LRESULT,
  [(HWND, INPUT_PARAM, 'hWnd'),
   (UINT, INPUT_PARAM, 'Msg'),
   (WPARAM, INPUT_PARAM, 'wParam'),
   (LPARAM, INPUT_PARAM, 'lParam')])

PeekMessage = Win32Func('PeekMessageW', 'user32', BOOL,
  [(POINTER(MSG), INPUT_PARAM, 'lpMsg'),
   (HWND, INPUT_PARAM, 'hWnd', None),
   (UINT, INPUT_PARAM, 'wMsgFilterMin', 0),
   (UINT, INPUT_PARAM, 'wMsgFilterMax', 0),
   (UINT, INPUT_PARAM, 'wRemoveMsg', PM_REMOVE)],
   success_predicate=None)

TranslateMessage = Win32Func('TranslateMessage', 'user32',
                             BOOL, [POINTER(MSG)], success_predicate=None)

DispatchMessage = Win32Func('DispatchMessageW', 'user32',
                            LRESULT, [POINTER(MSG)], success_predicate=None)

###############################################################################

DuplicateHandle = Win32Func(
    'DuplicateHandle', 'kernel32', BOOL,
    [(HANDLE, INPUT_PARAM, 'hSourceProcessHandle'),
     (HANDLE, INPUT_PARAM, 'hSourceHandle'),
     (HANDLE, INPUT_PARAM, 'hTargetProcessHandle'),
     (POINTER(HANDLE), OUTPUT_PARAM, 'lpTargetHandle'),
     (DWORD, INPUT_PARAM, 'dwDesiredAccess', 0),
     (BOOL, INPUT_PARAM, 'bInheritHandle', False),
     (DWORD, INPUT_PARAM, 'dwOptions', DUPLICATE_SAME_ACCESS)])

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

###############################################################################

SetStdHandle = Win32Func('SetStdHandle', 'kernel32', BOOL, [DWORD, HANDLE])

GetStdHandle = Win32Func('GetStdHandle', 'kernel32', HANDLE, [DWORD],
                         lambda h, *_: h and h != INVALID_HANDLE_VALUE)

AttachConsole = Win32Func('AttachConsole', 'kernel32', BOOL,
                          [(DWORD, INPUT_PARAM, 'dwProcessId')])

WriteConsole = Win32Func(
    'WriteConsoleW', 'kernel32', BOOL,
    [(HANDLE, INPUT_PARAM, 'hConsoleOutput'),
     (LPCWSTR, INPUT_PARAM, 'lpBuffer'),
     (DWORD, INPUT_PARAM, 'nNumberOfCharsToWrite'),
     (POINTER(DWORD), OUTPUT_PARAM, 'lpNumberOfCharsWritten'),
     (LPVOID, INPUT_PARAM, 'lpReserved', None)])

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

ShellExecuteEx = Win32Func('ShellExecuteExW', 'shell32', BOOL,
                           [POINTER(SHELLEXECUTEINFO)])

GetCurrentProcess = Win32Func('GetCurrentProcess', 'kernel32', HANDLE, [])

GetModuleHandleEx = Win32Func(
    'GetModuleHandleExW', 'kernel32', BOOL,
    [(DWORD, INPUT_PARAM, 'dwFlags'),
     (ctypes.c_wchar_p, INPUT_PARAM, 'lpModuleName'),
     (POINTER(HMODULE), OUTPUT_PARAM, 'phModule')])

###############################################################################


MsgWaitForMultipleObjectsEx = Win32Func(
    'MsgWaitForMultipleObjectsEx', 'user32', DWORD,
    [(DWORD, INPUT_PARAM, 'nCount'),
     (POINTER(HANDLE), INPUT_PARAM, 'pHandles'),
     (DWORD, INPUT_PARAM, 'dwMilliseconds'),
     (DWORD, INPUT_PARAM, 'dwWakeMask'),
     (DWORD, INPUT_PARAM, 'dwFlags')])

WaitForSingleObject = Win32Func(
    'WaitForSingleObject', 'kernel32', DWORD, [HANDLE, DWORD],
    lambda result, *_: result != WAIT_FAILED)

MessageBox = Win32Func(
    'MessageBoxW', 'user32', c_int,
    [(HWND, INPUT_PARAM,  'hWnd', None),
     (LPCWSTR, INPUT_PARAM, 'lpText'),
     (LPCWSTR, INPUT_PARAM, 'lpCaption', None),
     (UINT, INPUT_PARAM, 'uType', 0)])
