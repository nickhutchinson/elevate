import ctypes
from . import libc

PyBUF_READ = 0x100
PyBUF_WRITE = 0x200

PyMemoryView_FromMemory = ctypes.pythonapi.PyMemoryView_FromMemory
PyMemoryView_FromMemory.restype = ctypes.py_object
PyMemoryView_FromMemory.argtypes = (
    ctypes.c_void_p, libc.c_intptr, ctypes.c_int)

