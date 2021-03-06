import ctypes
from ctypes import POINTER, c_int, c_wchar_p, c_wchar, c_void_p, HRESULT
from ctypes.wintypes import *
from .ctypes_utils import OUTPUT_PARAM, Win32Func, Win32OLEFunc
from .libc import c_intptr
from ._constants import *
import sys
from uuid import UUID

HCURSOR = HICON
LRESULT = c_intptr
LONG_PTR = c_intptr

def _is_valid_handle(h, *args):
    return h and h != INVALID_HANDLE_VALUE

# Fundamental Types

class FILETIME(ctypes.Structure):
    _fields_ = [('low_date_time', DWORD), ('high_date_time', DWORD)]

    def __int__(self):
        return (self.high_date_time << 32) | self.low_date_time


class GUID(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], str):
            super().__init__(**kwargs)
            if sys.byteorder == 'big':
                self.data[:] = UUID(args[0]).bytes
            else:
                self.data[:] = UUID(args[0]).bytes_le
        else:
            super().__init__(*args, **kwargs)


    _fields_ = [('data', ctypes.c_ubyte * 16)]

###############################################################################
# Window functions

WNDPROC = ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)


class WNDCLASSEX(ctypes.Structure):
    _fields_ = (
        ('size', UINT),
        ('style', UINT),
        ('wnd_proc', WNDPROC),
        ('cls_extra', c_int),
        ('wnd_extra', c_int),
        ('instance', HINSTANCE),
        ('icon', HICON),
        ('cursor', HCURSOR),
        ('background', HBRUSH),
        ('menu_name', LPCWSTR),
        ('class_name', LPCWSTR),
        ('small_icon', HICON),
    )

RegisterClassEx = Win32Func('RegisterClassExW', 'user32', ATOM,
                            [POINTER(WNDCLASSEX)], lambda atom, *_: atom)

GetWindowLongPtr = Win32Func(
    'GetWindowLongPtrW', 'user32', LONG_PTR,
    [('wnd', HWND),
     ('index', c_int)])

SetWindowLongPtr = Win32Func(
    'SetWindowLongPtrW', 'user32', LONG_PTR,
    [('wnd', HWND),
     ('index', c_int),
     ('new_long', LONG_PTR)])


class CREATESTRUCT(ctypes.Structure):
    _fields_ = (
        ('create_params', LPVOID),
        ('instance', HINSTANCE),
        ('menu', HMENU),
        ('parent', HWND),
        ('cy', c_int),
        ('cx', c_int),
        ('y', c_int),
        ('x', c_int),
        ('style', LONG),
        ('name', LPCWSTR),
        ('class', LPCWSTR),
        ('ex_style', DWORD))

CreateWindowEx = Win32Func(
    'CreateWindowExW', 'user32', HWND,
    [('ex_style', DWORD),
     ('class_name', LPCWSTR),
     ('window_name', LPCWSTR, None),
     ('style', DWORD),
     ('x', c_int, 0),
     ('y', c_int, 0),
     ('width', c_int, 0),
     ('height', c_int, 0),
     ('wnd_parent', HWND, None),
     ('menu', HMENU, None),
     ('instance', HINSTANCE),
     ('param', LPVOID)],
    success_predicate=_is_valid_handle)

DefWindowProc = Win32Func(
    'DefWindowProcW', 'user32', LRESULT,
    [('wnd', HWND),
     ('Msg', UINT),
     ('param', WPARAM),
     ('param', LPARAM)])

PeekMessage = Win32Func(
    'PeekMessageW', 'user32', BOOL,
    [('msg', POINTER(MSG)),
     ('wnd', HWND, None),
     ('msg_filter_min', UINT, 0),
     ('msg_filter_max', UINT, 0),
     ('remove_msg', UINT, PM_REMOVE)],
    success_predicate=None)

TranslateMessage = Win32Func('TranslateMessage', 'user32',
                             BOOL, [POINTER(MSG)], success_predicate=None)

DispatchMessage = Win32Func('DispatchMessageW', 'user32',
                            LRESULT, [POINTER(MSG)], success_predicate=None)

###############################################################################

DuplicateHandle = Win32Func(
    'DuplicateHandle', 'kernel32', BOOL,
    [('source_process_handle', HANDLE),
     ('source_handle', HANDLE),
     ('target_process_handle', HANDLE),
     ('target_handle', POINTER(HANDLE), OUTPUT_PARAM),
     ('desired_access', DWORD, 0),
     ('inherit_handle', BOOL, False),
     ('options', DWORD, DUPLICATE_SAME_ACCESS)])

CloseHandle = Win32Func('CloseHandle', 'kernel32', BOOL, [HANDLE])

###############################################################################


class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = (
        ('length', DWORD),
        ('security_descriptor', LPVOID),
        ('inherit_handle', BOOL)
    )


class SID(ctypes.Structure):
    pass

AllocateAndInitializeSid = Win32Func(
    'AllocateAndInitializeSid', 'advapi32', BOOL,
    [('identifier_authority', POINTER(SID_IDENTIFIER_AUTHORITY)),
     ('sub_authority_count', BYTE, 0),
     ('sub_authority0', DWORD, 0),
     ('sub_authority1', DWORD, 0),
     ('sub_authority2', DWORD, 0),
     ('sub_authority3', DWORD, 0),
     ('sub_authority4', DWORD, 0),
     ('sub_authority5', DWORD, 0),
     ('sub_authority6', DWORD, 0),
     ('sub_authority7', DWORD, 0),
     ('sid', POINTER(POINTER(SID)), OUTPUT_PARAM)])

FreeSid = Win32Func('FreeSid', 'advapi32', POINTER(SID), [POINTER(SID)])

CheckTokenMembership = Win32Func(
    'CheckTokenMembership', 'advapi32', BOOL,
    [('token_handle', HANDLE, None),
     ('sid_to_check', POINTER(SID)),
     ('is_member', POINTER(BOOL), OUTPUT_PARAM)])

###############################################################################

SetStdHandle = Win32Func('SetStdHandle', 'kernel32', BOOL, [DWORD, HANDLE])

GetStdHandle = Win32Func('GetStdHandle', 'kernel32', HANDLE, [DWORD],
                         _is_valid_handle)

AttachConsole = Win32Func('AttachConsole', 'kernel32', BOOL,
                          [('process_id', DWORD)])

WriteConsole = Win32Func(
    'WriteConsoleW', 'kernel32', BOOL,
    [('console_output', HANDLE),
     ('buffer', LPCWSTR),
     ('number_of_chars_to_write', DWORD),
     ('number_of_chars_written', POINTER(DWORD), OUTPUT_PARAM),
     ('reserved', LPVOID, None)])

###############################################################################
# Process management


class STARTUPINFO(ctypes.Structure):
    _fields_ = (
        ('cb', DWORD),
        ('reserved', LPWSTR),
        ('desktop', LPWSTR),
        ('title', LPWSTR),
        ('x', DWORD),
        ('y', DWORD),
        ('x_size', DWORD),
        ('y_size', DWORD),
        ('x_count_chars', DWORD),
        ('y_count_chars', DWORD),
        ('fill_attribute', DWORD),
        ('flags', DWORD),
        ('show_window', WORD),
        ('reserved2', WORD),
        ('reserved3', LPBYTE),
        ('std_input', HANDLE),
        ('std_output', HANDLE),
        ('std_error', HANDLE)
    )


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = (
        ('process', HANDLE),
        ('thread', HANDLE),
        ('process_id', DWORD),
        ('thread_id', DWORD)
    )


class SHELLEXECUTEINFO(ctypes.Structure):

    class _IconOrMonitor(ctypes.Union):
        _fields_ = (
            ('icon', HANDLE),
            ('monitor', HANDLE)
        )

    _anonymous_ = ('icon_or_monitor',)

    _fields_ = (
        ('size', DWORD),
        ('mask', ULONG),
        ('hwnd', HWND),
        ('verb', LPCWSTR),
        ('file', LPCWSTR),
        ('parameters', LPCWSTR),
        ('directory', LPCWSTR),
        ('show', c_int),
        ('inst_app', HINSTANCE),
        ('id_list', LPVOID),
        ('class_name', LPCWSTR),
        ('reg_key_class', HKEY),
        ('hot_key', DWORD),
        ('icon_or_monitor', _IconOrMonitor),
        ('process', HANDLE)
    )

CreateProcess = Win32Func(
    'CreateProcessW', 'kernel32', BOOL,
    [('application_name', LPCWSTR),
     ('command_line', LPWSTR),
     ('process_attributes', POINTER(SECURITY_ATTRIBUTES), None),
     ('thread_attributes', POINTER(SECURITY_ATTRIBUTES), None),
     ('inherit_handles', BOOL, False),
     ('creation_flags', DWORD, 0),
     ('environment', LPVOID, None),
     ('current_directory', LPCWSTR, None),
     ('startup_info', POINTER(STARTUPINFO)),
     ('process_information', POINTER(PROCESS_INFORMATION), OUTPUT_PARAM)])

ShellExecuteEx = Win32Func('ShellExecuteExW', 'shell32', BOOL,
                           [POINTER(SHELLEXECUTEINFO)])

GetModuleHandleEx = Win32Func(
    'GetModuleHandleExW', 'kernel32', BOOL,
    [('flags', DWORD),
     ('module_name', c_wchar_p),
     ('module', POINTER(HMODULE), OUTPUT_PARAM)])


GetEnvironmentStrings = Win32Func(
    'GetEnvironmentStringsW', 'kernel32', POINTER(c_wchar), [])
FreeEnvironmentStrings = Win32Func(
    'FreeEnvironmentStringsW', 'kernel32', BOOL, [POINTER(c_wchar)])


GetProcessTimes = Win32Func(
    'GetProcessTimes', 'kernel32', BOOL,
    [('process', HANDLE),
     ('creation_time', POINTER(FILETIME), OUTPUT_PARAM),
     ('exit_time', POINTER(FILETIME), OUTPUT_PARAM),
     ('kernel_time', POINTER(FILETIME), OUTPUT_PARAM),
     ('user_time', POINTER(FILETIME), OUTPUT_PARAM)])


GetCurrentProcessId = Win32Func('GetCurrentProcessId', 'kernel32', DWORD, [])
GetCurrentProcess = Win32Func('GetCurrentProcess', 'kernel32', HANDLE, [])

OpenProcess = Win32Func(
    'OpenProcess', 'kernel32', HANDLE,
    [('desired_access', DWORD),
     ('inherit_handle', BOOL),
     ('process_id', DWORD)])

###############################################################################


MsgWaitForMultipleObjectsEx = Win32Func(
    'MsgWaitForMultipleObjectsEx', 'user32', DWORD,
    [('count', DWORD),
     ('handles', POINTER(HANDLE)),
     ('milliseconds', DWORD),
     ('wake_mask', DWORD),
     ('flags', DWORD)])

WaitForSingleObject = Win32Func(
    'WaitForSingleObject', 'kernel32', DWORD, [HANDLE, DWORD],
    lambda result, *_: result != WAIT_FAILED)

PostMessage = Win32Func(
    'PostMessageW', 'user32', BOOL,
    [('hwnd', HWND),
     ('msg', UINT),
     ('w_param', WPARAM),
     ('l_param', LPARAM)])

MessageBox = Win32Func(
    'MessageBoxW', 'user32', c_int,
    [('wnd', HWND, None),
     ('text', LPCWSTR),
     ('caption', LPCWSTR, None),
     ('type', UINT, 0)])

LoadCursor = Win32Func(
    'LoadCursorW', 'user32', HCURSOR,
    [('instance', HINSTANCE),
     ('cursor_name', LPCWSTR)])


class UNIVERSAL_NAME_INFO(ctypes.Structure):
    _fields_ = (('universal_name', LPCWSTR),)


UNIVERSAL_NAME_INFO_LEVEL = 0x00000001
REMOTE_NAME_INFO_LEVEL = 0x00000002

WNetGetUniversalName = Win32Func(
   'WNetGetUniversalNameW', 'mpr', DWORD,
   [('local_path', LPCWSTR),
    ('info_level', DWORD),
    ('buffer', LPVOID),
    ('buffer_size', LPDWORD)])

def _wnet_get_universal_name_errcheck(result, func, args):
    if result == NO_ERROR:
        return args

    raise ctypes.WinError(result)

WNetGetUniversalName.errcheck = _wnet_get_universal_name_errcheck

# ---

CoTaskMemFree = Win32Func('CoTaskMemFree', 'ole32', None, [('ptr', c_void_p)])

SHGetKnownFolderPath = Win32OLEFunc(
    'SHGetKnownFolderPath', 'shell32', HRESULT,
    [('rfid', POINTER(GUID)),
     ('flags', DWORD, 0),
     ('token', HANDLE, None),
     ('path', POINTER(POINTER(c_wchar)), OUTPUT_PARAM)])

def _sh_get_known_folder_path_result_handler(result, func, args):
    if result == S_OK:
        try:
            path_ptr = args[3]
            return ctypes.wstring_at(path_ptr)
        finally:
            CoTaskMemFree(path_ptr)
    else:
        return args

SHGetKnownFolderPath.errcheck = _sh_get_known_folder_path_result_handler


