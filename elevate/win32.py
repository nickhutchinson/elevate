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
     ('param', LPVOID)])

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
                         lambda h, *_: h and h != INVALID_HANDLE_VALUE)

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
     ('inherit_handles', BOOL),
     ('creation_flags', DWORD, 0),
     ('environment', LPVOID, None),
     ('current_directory', LPCWSTR, None),
     ('startup_info', POINTER(STARTUPINFO)),
     ('process_information', POINTER(PROCESS_INFORMATION), OUTPUT_PARAM)])

ShellExecuteEx = Win32Func('ShellExecuteExW', 'shell32', BOOL,
                           [POINTER(SHELLEXECUTEINFO)])

GetCurrentProcess = Win32Func('GetCurrentProcess', 'kernel32', HANDLE, [])

GetModuleHandleEx = Win32Func(
    'GetModuleHandleExW', 'kernel32', BOOL,
    [('flags', DWORD),
     ('module_name', c_wchar_p),
     ('module', POINTER(HMODULE), OUTPUT_PARAM)])

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

MessageBox = Win32Func(
    'MessageBoxW', 'user32', c_int,
    [('wnd', HWND, None),
     ('text', LPCWSTR),
     ('caption', LPCWSTR, None),
     ('type', UINT, 0)])
