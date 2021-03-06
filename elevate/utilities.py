import abc
import ctypes
import weakref
from ctypes import byref, cast, sizeof, POINTER
from . import win32
from . import libc
from . import pyapi

def is_elevated():
    """Return True if the current user has superuser privileges, False
    otherwise"""
    admin_sid = None
    try:
        admin_sid = win32.AllocateAndInitializeSid(
            byref(win32.SECURITY_NT_AUTHORITY),
            2, win32.SECURITY_BUILTIN_DOMAIN_RID,
            win32.DOMAIN_ALIAS_RID_ADMINS)

        return bool(win32.CheckTokenMembership(sid_to_check=admin_sid))
    finally:
        if admin_sid:
            win32.FreeSid(admin_sid)


def argv_to_command_line(args):
    def escape_arg(arg):
        import re
        arg = re.sub(r'(\\*)"', r'\1\1\"', arg)
        arg = re.sub(r'(\\+)$', r'\1\1', arg)
        return "".join(('"', arg, '"'))

    return ' '.join(escape_arg(arg) for arg in args)


def module_from_address(address):
    return win32.GetModuleHandleEx(
        win32.GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS
        | win32.GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT,
        cast(address, ctypes.c_wchar_p))


def current_process_module():
    return win32.GetModuleHandleEx(
        win32.GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT, None)


def unc_name_for_path(path):
    buf = None
    buffer_size = win32.DWORD()

    MAX_ATTEMPTS=5
    for _ in range(MAX_ATTEMPTS):
        try:
            buf_ptr = byref(buf) if buf else None
            win32.WNetGetUniversalName(path, win32.UNIVERSAL_NAME_INFO_LEVEL, 
                                       buf_ptr, byref(buffer_size))
            return win32.UNIVERSAL_NAME_INFO.from_buffer(buf).universal_name
        except OSError as e:
            if e.winerror == win32.ERROR_MORE_DATA:
                buf = ctypes.c_buffer(buffer_size.value)
            else:
                raise

    raise ctypes.WinError(win32.ERROR_MORE_DATA)


def _length_of_environment_block(env_block):
    """ Length of the environment block, in bytes """
    # the envblock is terminated by a zero-length string
    n = 0
    while True:
        current_length = libc.wcslen(byref(env_block.contents, n))
        n += (current_length + 1) * sizeof(ctypes.c_wchar);

        if current_length == 0:
            break

    return n


def environment_block_snapshot():
    env_block = win32.GetEnvironmentStrings()
    try:
        view = pyapi.PyMemoryView_FromMemory(
            env_block,
            _length_of_environment_block(env_block),
            pyapi.PyBUF_READ)
        return bytes(view)

    finally:
        win32.FreeEnvironmentStrings(env_block)


class WndProc(metaclass=abc.ABCMeta):

    """Implement this interface to to customise window behaviour."""

    @abc.abstractmethod
    def wnd_proc(self, window_handle, message_id, w_param, l_param):
        """Process Window messages; return type depends on the message kind.

        Default implementation calls DefWindowProc()
        """
        return win32.DefWindowProc(window_handle, message_id, w_param, l_param)


def _add_refdata_for_item(item, data):
    """Weakly associates some data with |item|."""
    _add_refdata_for_item.s_refdata.setdefault(item, []).append(data)
_add_refdata_for_item.s_refdata = weakref.WeakKeyDictionary()


class WindowClass(WndProc):
    @classmethod
    def shared_instance(klass):
        """Return the default window class."""
        try:
            return klass._shared_instance
        except AttributeError:
            klass._shared_instance = klass(
                'me.nickhutchinson.elevate.wnd_class')
            return klass._shared_instance

    def __init__(self, name):
        self.name = name
        self.wnd_proc_closure = win32.WNDPROC(self.wnd_proc)

        class_info = win32.WNDCLASSEX()
        class_info.size = sizeof(class_info)
        class_info.class_name = name
        class_info.cursor = win32.LoadCursor(None, win32.IDC_ARROW)
        class_info.background  = win32.COLOR_WINDOW + 1
        class_info.wnd_proc = self.wnd_proc_closure
        class_info.instance = current_process_module()
        win32.RegisterClassEx(byref(class_info))

    def wnd_proc(self, window_handle, message_id, w_param, l_param):
        if message_id == win32.WM_NCCREATE and l_param:
            creation_struct = cast(l_param, POINTER(win32.CREATESTRUCT))[0]
            actual_wnd_proc = cast(
                creation_struct.create_params, win32.WNDPROC)
            win32.SetWindowLongPtr(
                window_handle,
                win32.GWLP_USERDATA,
                cast(actual_wnd_proc, ctypes.c_void_p).value)
        else:
            actual_wnd_proc = cast(win32.GetWindowLongPtr(
                window_handle, win32.GWLP_USERDATA), win32.WNDPROC)

        if not actual_wnd_proc:
            actual_wnd_proc = super().wnd_proc

        return actual_wnd_proc(window_handle, message_id, w_param, l_param)


def create_window(wnd_proc, ex_style, style, window_name="Untitled window",
                  x=win32.CW_USEDEFAULT, y=win32.CW_USEDEFAULT,
                  width=win32.CW_USEDEFAULT, height=win32.CW_USEDEFAULT,
                  parent=None, menu=None):
    wnd_proc_closure = win32.WNDPROC(wnd_proc.wnd_proc)

    class HashableRestype(win32.CreateWindowEx.restype):
        def __hash__(self):
            return id(self)

    wnd = HashableRestype(win32.CreateWindowEx(ex_style,
                          WindowClass.shared_instance().name,
                          window_name, style, x, y, width, height, parent,
                          menu, current_process_module(), wnd_proc_closure))
    _add_refdata_for_item(wnd, wnd_proc_closure)
    return wnd


class RunLoop:

    def run(self):
        message = win32.MSG()
        handle_count = 0

        while True:
            result = win32.MsgWaitForMultipleObjectsEx(
                0, None, win32.INFINITE, win32.QS_ALLINPUT,
                win32.MWMO_INPUTAVAILABLE)

            if (win32.WAIT_OBJECT_0
                    <= result < win32.WAIT_OBJECT_0 + handle_count):
                # signaled handle
                pass

            elif (win32.WAIT_ABANDONED_0
                    <= result < win32.WAIT_ABANDONED_0 + handle_count):
                # abandoned handle
                pass

            elif result == win32.WAIT_OBJECT_0 + handle_count:
                # windows message
                if not win32.PeekMessage(byref(message)):
                    continue

                if message.message == win32.WM_QUIT:
                    return message.w_param
                else:
                    win32.TranslateMessage(byref(message))
                    win32.DispatchMessage(byref(message))

            elif result == win32.WAIT_IO_COMPLETION:
                # APC
                pass

            elif result == win32.WAIT_TIMEOUT:
                # timeout
                pass

            else:
                raise ctypes.WinError(ctypes.get_last_error())
