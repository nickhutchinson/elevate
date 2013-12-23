import ctypes
from ctypes import get_last_error, get_errno, WinError
import os
from collections import Sequence
from functools import partial

INPUT_PARAM = 1
OUTPUT_PARAM = 2

def DEFAULT_WIN32_SUCCESS(result, *args):
    return result != 0

def DEFAULT_C_SUCCESS(result, *args):
    return result >= 0

class FuncType:
    Win32 = ctypes.windll, partial(ctypes.WINFUNCTYPE, use_last_error=True)
    C = ctypes.cdll, partial(ctypes.CFUNCTYPE, use_errno=True)

def NativeFunc(kind, function_name, module_name, result_type, 
               argument_descriptors):
    def head(x):
        return x[0] if isinstance(x, Sequence) else x

    def tail(x):
        return x[1:] if isinstance(x, Sequence) else tuple()

    def get_param_flags(obj):
        param_flags = tail(obj)
        return param_flags if param_flags else (INPUT_PARAM, )

    module_type, function_type = kind
    module = getattr(module_type, module_name)
    arg_types = (head(tup) for tup in argument_descriptors)
    param_flags = tuple(get_param_flags(tup) for tup in argument_descriptors)

    prototype = function_type(result_type, *arg_types)
    return prototype((function_name, module), param_flags)

def Win32Func(function_name, module_name, result_type, argument_descriptors,
              success_predicate=DEFAULT_WIN32_SUCCESS):
    function = NativeFunc(FuncType.Win32, function_name, module_name,
                          result_type, argument_descriptors)
    if success_predicate:
        def errcheck(result, func, args):
            is_unknown_restype = (success_predicate is DEFAULT_WIN32_SUCCESS
                and result_type != ctypes.wintypes.BOOL)
            if (not is_unknown_restype 
                and not success_predicate(result, func, args)):
                raise WinError(get_last_error())
            return args

        function.errcheck = errcheck

    return function


def CFunc(function_name, module_name, result_type, argument_descriptors,
          success_predicate=DEFAULT_C_SUCCESS):
    function = NativeFunc(FuncType.C, function_name, module_name,
                          result_type, argument_descriptors)
    if success_predicate:
        def is_integral(type):
            try:
                type() < int()
                return True
            except TypeError:
                return False

        is_unknown_restype = (success_predicate is DEFAULT_C_SUCCESS
                and not is_integral(result_type))
        def errcheck(result, func, args):
            if (not is_unknown_restype
                and not success_predicate(result, func, args)):
                raise OSError(get_errno(), os.strerror(get_errno()))
            return args

        function.errcheck = errcheck

    return function
