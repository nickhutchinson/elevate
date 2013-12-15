from elevate import _native as Win32
import ctypes

def is_elevated():
    admin_sid = None
    try:
        admin_sid = Win32.AllocateAndInitializeSid(
                ctypes.byref(Win32.SECURITY_NT_AUTHORITY),
                2, Win32.SECURITY_BUILTIN_DOMAIN_RID,
                Win32.DOMAIN_ALIAS_RID_ADMINS)

        return bool(Win32.CheckTokenMembership(SidToCheck=admin_sid))
    finally:
        Win32.FreeSid(admin_sid)


def main():
    print(is_elevated())

    exec_info = Win32.SHELLEXECUTEINFO()
    exec_info.cbSize = ctypes.sizeof(exec_info)
    exec_info.lpFile = "cmd"
    exec_info.lpParameters = "/C dir && pause"
    exec_info.lpVerb = "runas"
    exec_info.fMask = Win32.SEE_MASK_FLAG_NO_UI | Win32.SEE_MASK_NOASYNC \
                    | Win32.SEE_MASK_NOCLOSEPROCESS | Win32.SEE_MASK_UNICODE
    exec_info.nShow = Win32.SW_SHOWNORMAL

    result = Win32.ShellExecuteEx(ctypes.byref(exec_info))

    Win32.WaitForSingleObject(exec_info.hProcess, Win32.INFINITE)

    Win32.CloseHandle(exec_info.hProcess)


if __name__ == '__main__':
    main()