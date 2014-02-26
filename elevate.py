from elevate import win32, libc, utilities

from collections import namedtuple
import argparse
import ctypes
import os
import shutil
import sys
import traceback
import logging
from multiprocessing.connection import Listener, Client

logging.basicConfig(filename='elevate.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:%(message)s')

def python_interpreter_path():
    return sys.executable


def pythonw_interpreter_path():
    head, tail = os.path.split(python_interpreter_path())
    base, ext = os.path.splitext(tail)
    return os.path.join(head, 'pythonw' + ext)


def path_to_current_script():
    absolute_script_path = os.path.abspath(sys.argv[0])

    # Handle case where we're on a mapped network drive. When we're relaunched
    # as admin, drive mappings seem to be no longer there.
    try:
        return utilities.unc_name_for_path(absolute_script_path)
    except OSError as e:
        if e.winerror in (win32.ERROR_NOT_CONNECTED, win32.ERROR_BAD_DEVICE):
            return absolute_script_path
        else:
            raise


def write_console(s, console=win32.STD_OUTPUT_HANDLE):
    wide_string = ctypes.c_wchar_p(s)
    win32.WriteConsole(win32.GetStdHandle(console),
                       wide_string, libc.wcslen(wide_string))


def print_console(*args):
    write_console('{}\n'.format(args))


def attach_to_parent_console():
    # FIXME:
    # Currently, redirection of the std streams doesn't work. We need to do
    # more than just attach to our parent's console, as that process' std
    # handles might be pipes and not be console handles at all. e.g. MinTTY.

    try:
        win32.AttachConsole(win32.ATTACH_PARENT_PROCESS)
    except OSError as e:
        logging.debug("couldn't attach to parent {}".format(e))
        if e.winerror != win32.ERROR_ACCESS_DENIED:
            raise

    StandardHandleInfo = namedtuple('StandardHandleInfo',
                                    'name filename win32_constant fd mode')
    standard_handles = (
        StandardHandleInfo('stdin', 'CONIN$', win32.STD_INPUT_HANDLE, 
                           libc.STDIN_FILENO, 'r'),
        StandardHandleInfo('stdout', 'CONOUT$', win32.STD_OUTPUT_HANDLE,
                           libc.STDOUT_FILENO, 'w'),
        StandardHandleInfo('stderr', 'CONOUT$', win32.STD_ERROR_HANDLE,
                           libc.STDERR_FILENO, 'w'))

    for handle_info in standard_handles:
        stream = getattr(sys, handle_info.name)
        if stream:
            stream.flush()

        handle = win32.DuplicateHandle(
            win32.GetCurrentProcess(),
            win32.GetStdHandle(handle_info.win32_constant),
            win32.GetCurrentProcess())
        fd = libc.open_osfhandle(handle, libc.O_TEXT)
        libc.dup2(fd, handle_info.fd)
        libc.close(fd)

        # associate Python's sys.(stdin|stdout|stderr) with the console
        setattr(sys, handle_info.name,
                libc.fdopen(handle_info.fd, handle_info.mode))

        # associate C's (stdin|stdout|stderr) with the console
        libc.freopen(handle_info.filename, handle_info.mode,
                     getattr(libc, handle_info.name))


def spawn_user_process_sync(argv, environment):
    # FIXME: we need a win32 message pump to avoid the caller getting the 
    #        wait cursor.

    command_line = utilities.argv_to_command_line(argv)
    # MSDN says CreateProcess needs a mutable string, for whatever reason.
    command_line_mutable = ctypes.create_unicode_buffer(command_line)

    startup_info = win32.STARTUPINFO()
    startup_info.cb = ctypes.sizeof(win32.STARTUPINFO)

    proc_info = win32.CreateProcess(argv[0],
        command_line_mutable,
        startup_info=startup_info,
        environment=environment,
        creation_flags=win32.CREATE_UNICODE_ENVIRONMENT)
    
    win32.WaitForSingleObject(proc_info.process, win32.INFINITE)
    # FIXME exit code
    win32.CloseHandle(proc_info.process)


def launch_privileged_helper_sync(argv):
    resolved_path = shutil.which(argv[0])
    if not resolved_path:
        print("File '{}' was not found.".format(argv[0]), file=sys.stderr)
        sys.exit(1)
    

    with Listener() as server:
        exec_info = win32.SHELLEXECUTEINFO()
        exec_info.size = ctypes.sizeof(exec_info)
        exec_info.verb = 'runas'
        exec_info.mask = (win32.SEE_MASK_FLAG_NO_UI
                          | win32.SEE_MASK_NOASYNC
                          | win32.SEE_MASK_NOCLOSEPROCESS
                          | win32.SEE_MASK_UNICODE)
        exec_info.show = win32.SW_SHOWNORMAL
        exec_info.file = pythonw_interpreter_path()
        exec_info.parameters = utilities.argv_to_command_line([
            path_to_current_script(),
            '--named_pipe', server.address, '--',
            resolved_path] + argv[1:])

        try:
            win32.ShellExecuteEx(ctypes.byref(exec_info))
        except OSError as e:
            if e.winerror == win32.ERROR_CANCELLED:
                # User declined
                sys.exit(1)
            else:
                raise
                
        with server.accept() as conn:
            message = {
                'environment_block': utilities.environment_block_snapshot()
                # FIXME
                # stdout, stderr, stdin handles
                # pid
            }
            logging.debug("Sending message {}".format(message))
            conn.send(message)
            
            win32.WaitForSingleObject(exec_info.process, win32.INFINITE)
            # FIXME exit code
            win32.CloseHandle(exec_info.process)


def main():
    parser = argparse.ArgumentParser(prog='elevate.py')
    parser.add_argument('--named_pipe', help=argparse.SUPPRESS)
    parser.add_argument('--passkey', help=argparse.SUPPRESS)    
    parser.add_argument('command', help='the command to run')
    parser.add_argument('args', nargs=argparse.REMAINDER,
                        help=argparse.SUPPRESS)
    
    args = parser.parse_args()

    if utilities.is_elevated():
        attach_to_parent_console()
        env = None

        if args.named_pipe:
            with Client(args.named_pipe) as conn:
                message = conn.recv()
                env = message['environment_block']

        logging.debug("Received message {}".format(message))
        spawn_user_process_sync([args.command] + args.args, env)

    else:
        launch_privileged_helper_sync([args.command] + args.args)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        win32.MessageBox(text='{}'.format(traceback.format_exc()))
