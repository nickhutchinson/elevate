import ctypes
from ctypes.wintypes import BYTE, LPCWSTR
from ._winerror import *

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

# CreateProcess
CREATE_UNICODE_ENVIRONMENT = 0x400


# GetStdHandle()
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

# AttachConsole()
ATTACH_PARENT_PROCESS = -1

# Timeouts
INFINITE = 0xFFFFFFFF

# DuplicateHandle()
DUPLICATE_CLOSE_SOURCE = 0x00000001
DUPLICATE_SAME_ACCESS = 0x00000002

# Sids, impersonation tokens, yadda yadda yadda
SECURITY_BUILTIN_DOMAIN_RID = 0x00000020


class SID_IDENTIFIER_AUTHORITY(ctypes.Structure):
    _fields_ = (('Value', BYTE * 6), )

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

# GetModuleHandleEx
GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS = 0x00000004
GET_MODULE_HANDLE_EX_FLAG_PIN = 0x00000001
GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT = 0x00000002

# Get/SetWindowLongPtr
GWLP_USERDATA = -21

# PeekMessage
PM_NOREMOVE = 0x0000
PM_REMOVE = 0x0001
PM_NOYIELD = 0x0002

"""
Sent prior to the WM_CREATE message when a window is first created.
l_param: A pointer to the CREATESTRUCT
"""
WM_NCCREATE = 0x0081

WM_QUIT = 0x0012

###############################################################################
#CreateWindowEx
###############################################################################

CW_USEDEFAULT = 0x80000000

WS_EX_ACCEPTFILES = 0x00000010
WS_EX_APPWINDOW = 0x00040000
WS_EX_CLIENTEDGE = 0x00000200
WS_EX_COMPOSITED = 0x02000000
WS_EX_CONTEXTHELP = 0x00000400
WS_EX_CONTROLPARENT = 0x00010000
WS_EX_DLGMODALFRAME = 0x00000001
WS_EX_LAYERED = 0x00080000
WS_EX_LAYOUTRTL = 0x00400000
WS_EX_LEFT = 0x00000000
WS_EX_LEFTSCROLLBAR = 0x00004000
WS_EX_LTRREADING = 0x00000000
WS_EX_MDICHILD = 0x00000040
WS_EX_NOACTIVATE = 0x08000000
WS_EX_NOINHERITLAYOUT = 0x00100000
WS_EX_NOPARENTNOTIFY = 0x00000004
WS_EX_NOREDIRECTIONBITMAP = 0x00200000
WS_EX_RIGHT = 0x00001000
WS_EX_RIGHTSCROLLBAR = 0x00000000
WS_EX_RTLREADING = 0x00002000
WS_EX_STATICEDGE = 0x00020000
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_TOPMOST = 0x00000008
WS_EX_TRANSPARENT = 0x00000020
WS_EX_WINDOWEDGE = 0x00000100
WS_EX_OVERLAPPEDWINDOW = WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE
WS_EX_PALETTEWINDOW = WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST

WS_BORDER = 0x00800000
WS_CAPTION = 0x00C00000
WS_CHILD = 0x40000000
WS_CLIPCHILDREN = 0x02000000
WS_CLIPSIBLINGS = 0x04000000
WS_DISABLED = 0x08000000
WS_DLGFRAME = 0x00400000
WS_GROUP = 0x00020000
WS_HSCROLL = 0x00100000
WS_MAXIMIZE = 0x01000000
WS_MAXIMIZEBOX = 0x00010000
WS_MINIMIZE = 0x20000000
WS_MINIMIZEBOX = 0x00020000
WS_OVERLAPPED = 0x00000000
WS_POPUP = 0x80000000
WS_SYSMENU = 0x00080000
WS_TABSTOP = 0x00010000
WS_THICKFRAME = 0x00040000
WS_TILED = 0x00000000
WS_VISIBLE = 0x10000000
WS_VSCROLL = 0x00200000

WS_CHILDWINDOW = WS_CHILD
WS_ICONIC = WS_MINIMIZE
WS_SIZEBOX = WS_THICKFRAME

WS_OVERLAPPEDWINDOW = (WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME
                       | WS_MINIMIZEBOX | WS_MAXIMIZEBOX)
WS_POPUPWINDOW = WS_POPUP | WS_BORDER | WS_SYSMENU
WS_TILEDWINDOW = WS_OVERLAPPEDWINDOW

def MAKEINTRESOURCE(i):
   return LPCWSTR(ctypes.c_uint16(i).value)

# LoadCursor()
IDC_APPSTARTING = MAKEINTRESOURCE(32650)
IDC_ARROW = MAKEINTRESOURCE(32512)
IDC_CROSS = MAKEINTRESOURCE(32515)
IDC_HAND = MAKEINTRESOURCE(32649)
IDC_HELP = MAKEINTRESOURCE(32651)
IDC_IBEAM = MAKEINTRESOURCE(32513)
IDC_ICON = MAKEINTRESOURCE(32641)
IDC_NO = MAKEINTRESOURCE(32648)
IDC_SIZE = MAKEINTRESOURCE(32640)
IDC_SIZEALL = MAKEINTRESOURCE(32646)
IDC_SIZENESW = MAKEINTRESOURCE(32643)
IDC_SIZENS = MAKEINTRESOURCE(32645)
IDC_SIZENWSE = MAKEINTRESOURCE(32642)
IDC_SIZEWE = MAKEINTRESOURCE(32644)
IDC_UPARROW = MAKEINTRESOURCE(32516)
IDC_WAIT = MAKEINTRESOURCE(32514)


# System Colours
COLOR_SCROLLBAR = 0
COLOR_BACKGROUND = 1
COLOR_ACTIVECAPTION = 2
COLOR_INACTIVECAPTION = 3
COLOR_MENU = 4
COLOR_WINDOW = 5
COLOR_WINDOWFRAME = 6
COLOR_MENUTEXT = 7
COLOR_WINDOWTEXT = 8
COLOR_CAPTIONTEXT = 9
COLOR_ACTIVEBORDER = 0
COLOR_INACTIVEBORDER = 1
COLOR_APPWORKSPACE = 2
COLOR_HIGHLIGHT = 3
COLOR_HIGHLIGHTTEXT = 4
COLOR_BTNFACE = 5
COLOR_BTNSHADOW = 6
COLOR_GRAYTEXT = 7
COLOR_BTNTEXT = 8
COLOR_INACTIVECAPTIONTEXT = 9
COLOR_BTNHIGHLIGHT = 0

COLOR_3DDKSHADOW = 1
COLOR_3DLIGHT = 2
COLOR_INFOTEXT = 3
COLOR_INFOBK = 4
COLOR_HOTLIGHT = 6
COLOR_GRADIENTACTIVECAPTION = 7
COLOR_GRADIENTINACTIVECAPTION = 8
COLOR_MENUHILIGHT = 9
COLOR_MENUBAR = 0

####

