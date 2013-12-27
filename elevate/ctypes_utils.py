import ctypes
from ctypes import get_last_error, get_errno, WinError
import os
from collections import Sequence
from functools import partial

# sentinel values
def INPUT_PARAM(): return 1
def OUTPUT_PARAM(): return 2

def DEFAULT_WIN32_SUCCESS(result, *args): return result != 0
def DEFAULT_C_SUCCESS(result, *args): return result >= 0


class FuncType:
    Win32 = ctypes.windll, partial(ctypes.WINFUNCTYPE, use_last_error=True)
    C = ctypes.cdll, partial(ctypes.CFUNCTYPE, use_errno=True)


def _flattened(sequence):
    result = []

    def impl(sequence, result):
        for elem in sequence:
            if isinstance(elem, Sequence) and not isinstance(elem, str):
                impl(elem, result)
            else:
                result.append(elem)
    impl(sequence, result)
    return result


def _NativeFunc(kind, function_name, module_name, result_type,
                argument_descriptors):
    """Return a ctypes function prototype.

    :param kind: FuncType.Win32 or FuncType.C
    :type function_name: string
    :type module_name: string
    :type result_type: ctypes type
    :param argument_descriptors:
        either:
          - a sequence of ctypes types (DWORD, c_int, etc...)
          - a sequence of tuples of the form
              (param_name, param_type, [value_kind]|[default_value])
            where value_kind is either of INPUT_PARAM or OUTPUT_PARAM

    """
    def function_argtype(descriptor):
        assert descriptor
        if not isinstance(descriptor, Sequence):
            return descriptor
        return descriptor[0] if len(descriptor) == 1 else descriptor[1]

    def function_argdesc(descriptor):
        assert descriptor
        if not isinstance(descriptor, Sequence) or len(descriptor) == 1:
            return (INPUT_PARAM(), )

        arg_desc = [[INPUT_PARAM()], [descriptor[0]], []]

        for param in descriptor[2:]:
            if param in (INPUT_PARAM, OUTPUT_PARAM):
                arg_desc[0] = param()
            else:
                arg_desc[-1] = param

        return tuple(_flattened(arg_desc))

    module_type, function_type = kind
    module = getattr(module_type, module_name)

    arg_types = (function_argtype(elem) for elem in argument_descriptors)
    prototype = function_type(result_type, *arg_types)

    param_flags = tuple(
        function_argdesc(elem) for elem in argument_descriptors)

    return prototype((function_name, module), param_flags)


def Win32Func(function_name, module_name, result_type, argument_descriptors,
              success_predicate=DEFAULT_WIN32_SUCCESS):
    function = _NativeFunc(FuncType.Win32, function_name, module_name,
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
    function = _NativeFunc(FuncType.C, function_name, module_name,
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
