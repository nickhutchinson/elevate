"""A few useful functions from MSVCRT."""
import ctypes
from ctypes import POINTER, c_int, c_wchar_p, c_char_p, c_size_t
from .ctypes_utils import CFunc

if ctypes.sizeof(ctypes.c_voidp) == 8:
    c_uintptr, c_intptr = ctypes.c_uint64, ctypes.c_int64
else:
    c_uintptr, c_intptr = ctypes.c_uint32, ctypes.c_int32

class FILE(ctypes.Structure):
    _fields_ = (
        ('_ptr', c_char_p),
        ('_cnt', c_int),
        ('_base', c_char_p),
        ('_flag', c_int),
        ('_file', c_int),
        ('_charbuf', c_int),
        ('_bufsiz', c_int),
        ('_tmpfname', c_char_p))

freopen = CFunc('_wfreopen', 'msvcrt',
                POINTER(FILE), (c_wchar_p, c_wchar_p, POINTER(FILE)))
fileno = CFunc('_fileno', 'msvcrt', POINTER(FILE), (c_int,))
printf = CFunc('wprintf', 'msvcrt', c_int, (c_wchar_p,))

get_std_streams = CFunc('__iob_func', 'msvcrt', POINTER(FILE), [])
wcslen = CFunc('wcslen', 'msvcrt', c_size_t, [c_wchar_p])

from msvcrt import open_osfhandle, get_osfhandle
from os import dup2, close, fdopen, O_TEXT, O_BINARY
