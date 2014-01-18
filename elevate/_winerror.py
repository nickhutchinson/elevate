#
# Note: There is a slightly modified layout for HRESULT values below,
#        after the heading "COM Error Codes".
#
# Search for "**** Available SYSTEM error codes ****" to find where to
# insert new error codes
#
#  Values are 32 bit values laid out as follows:
#
#   3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
#   1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
#  +-+-+-+-+-+---------------------+-------------------------------+
#  |S|R|C|N|r|    Facility         |               Code            |
#  +-+-+-+-+-+---------------------+-------------------------------+
#
#  where
#
#      S - Severity - indicates success/fail
#
#          0 - Success
#          1 - Fail (COERROR)
#
#      R - reserved portion of the facility code, corresponds to NT's
#              second severity bit.
#
#      C - reserved portion of the facility code, corresponds to NT's
#              C field.
#
#      N - reserved portion of the facility code. Used to indicate a
#              mapped NT status value.
#
#      r - reserved portion of the facility code. Reserved for internal
#              use. Used to indicate HRESULT values that are not status
#              values, but are instead message ids for display strings.
#
#      Facility - is the facility code
#
#      Code - is the facility's status code
#
#
# Define the facility codes
#
FACILITY_XPS = 82
FACILITY_XAML = 43
FACILITY_USN = 129
FACILITY_BLBUI = 128
FACILITY_SPP = 256
FACILITY_WSB_ONLINE = 133
FACILITY_DLS = 153
FACILITY_BLB_CLI = 121
FACILITY_BLB = 120
FACILITY_WSBAPP = 122
FACILITY_WPN = 62
FACILITY_WMAAECMA = 1996
FACILITY_WINRM = 51
FACILITY_WINPE = 61
FACILITY_WINDOWSUPDATE = 36
FACILITY_WINDOWS_STORE = 63
FACILITY_WINDOWS_SETUP = 48
FACILITY_WINDOWS_DEFENDER = 80
FACILITY_WINDOWS_CE = 24
FACILITY_WINDOWS = 8
FACILITY_WINCODEC_DWRITE_DWM = 2200
FACILITY_WIA = 33
FACILITY_WER = 27
FACILITY_WEP = 2049
FACILITY_WEB_SOCKET = 886
FACILITY_WEB = 885
FACILITY_USERMODE_VOLSNAP = 130
FACILITY_USERMODE_VOLMGR = 56
FACILITY_VISUALCPP = 109
FACILITY_USERMODE_VIRTUALIZATION = 55
FACILITY_USERMODE_VHD = 58
FACILITY_URT = 19
FACILITY_UMI = 22
FACILITY_UI = 42
FACILITY_TPM_SOFTWARE = 41
FACILITY_TPM_SERVICES = 40
FACILITY_TIERING = 131
FACILITY_SYNCENGINE = 2050
FACILITY_SXS = 23
FACILITY_STORAGE = 3
FACILITY_STATE_MANAGEMENT = 34
FACILITY_SSPI = 9
FACILITY_USERMODE_SPACES = 231
FACILITY_SOS = 160
FACILITY_SCARD = 16
FACILITY_SHELL = 39
FACILITY_SETUPAPI = 15
FACILITY_SECURITY = 9
FACILITY_SDIAG = 60
FACILITY_USERMODE_SDBUS = 2305
FACILITY_RPC = 1
FACILITY_RESTORE = 256
FACILITY_SCRIPT = 112
FACILITY_PARSE = 113
FACILITY_RAS = 83
FACILITY_POWERSHELL = 84
FACILITY_PLA = 48
FACILITY_PIDGENX = 2561
FACILITY_P2P_INT = 98
FACILITY_P2P = 99
FACILITY_OPC = 81
FACILITY_ONLINE_ID = 134
FACILITY_WIN32 = 7
FACILITY_CONTROL = 10
FACILITY_WEBSERVICES = 61
FACILITY_NULL = 0
FACILITY_NDIS = 52
FACILITY_NAP = 39
FACILITY_MOBILE = 1793
FACILITY_METADIRECTORY = 35
FACILITY_MSMQ = 14
FACILITY_MEDIASERVER = 13
FACILITY_MBN = 84
FACILITY_LINGUISTIC_SERVICES = 305
FACILITY_LEAP = 2184
FACILITY_JSCRIPT = 2306
FACILITY_INTERNET = 12
FACILITY_ITF = 4
FACILITY_INPUT = 64
FACILITY_USERMODE_HYPERVISOR = 53
FACILITY_ACCELERATOR = 1536
FACILITY_HTTP = 25
FACILITY_GRAPHICS = 38
FACILITY_FWP = 50
FACILITY_FVE = 49
FACILITY_USERMODE_FILTER_MANAGER = 31
FACILITY_EAS = 85
FACILITY_EAP = 66
FACILITY_DXGI_DDI = 2171
FACILITY_DXGI = 2170
FACILITY_DPLAY = 21
FACILITY_DMSERVER = 256
FACILITY_DISPATCH = 2
FACILITY_DIRECTORYSERVICE = 37
FACILITY_DIRECTMUSIC = 2168
FACILITY_DIRECT3D11 = 2172
FACILITY_DIRECT3D10 = 2169
FACILITY_DIRECT2D = 2201
FACILITY_DAF = 100
FACILITY_DEPLOYMENT_SERVICES_UTIL = 260
FACILITY_DEPLOYMENT_SERVICES_TRANSPORT_MANAGEMENT = 272
FACILITY_DEPLOYMENT_SERVICES_TFTP = 264
FACILITY_DEPLOYMENT_SERVICES_PXE = 263
FACILITY_DEPLOYMENT_SERVICES_MULTICAST_SERVER = 289
FACILITY_DEPLOYMENT_SERVICES_MULTICAST_CLIENT = 290
FACILITY_DEPLOYMENT_SERVICES_MANAGEMENT = 259
FACILITY_DEPLOYMENT_SERVICES_IMAGING = 258
FACILITY_DEPLOYMENT_SERVICES_DRIVER_PROVISIONING = 278
FACILITY_DEPLOYMENT_SERVICES_SERVER = 257
FACILITY_DEPLOYMENT_SERVICES_CONTENT_PROVIDER = 293
FACILITY_DEPLOYMENT_SERVICES_BINLSVC = 261
FACILITY_DEFRAG = 2304
FACILITY_DEBUGGERS = 176
FACILITY_CONFIGURATION = 33
FACILITY_COMPLUS = 17
FACILITY_USERMODE_COMMONLOG = 26
FACILITY_CMI = 54
FACILITY_CERT = 11
FACILITY_BLUETOOTH_ATT = 101
FACILITY_BCD = 57
FACILITY_BACKGROUNDCOPY = 32
FACILITY_AUDIOSTREAMING = 1094
FACILITY_AUDCLNT = 2185
FACILITY_AUDIO = 102
FACILITY_ACTION_QUEUE = 44
FACILITY_ACS = 20
FACILITY_AAF = 18


#
# Define the severity codes
#


#
# MessageId: ERROR_SUCCESS
#
# MessageText:
#
# The operation completed successfully.
#
ERROR_SUCCESS = 0

NO_ERROR = 0
SEC_E_OK = 0x00000000

#
# MessageId: ERROR_INVALID_FUNCTION
#
# MessageText:
#
# Incorrect function.
#
ERROR_INVALID_FUNCTION = 1

#
# MessageId: ERROR_FILE_NOT_FOUND
#
# MessageText:
#
# The system cannot find the file specified.
#
ERROR_FILE_NOT_FOUND = 2

#
# MessageId: ERROR_PATH_NOT_FOUND
#
# MessageText:
#
# The system cannot find the path specified.
#
ERROR_PATH_NOT_FOUND = 3

#
# MessageId: ERROR_TOO_MANY_OPEN_FILES
#
# MessageText:
#
# The system cannot open the file.
#
ERROR_TOO_MANY_OPEN_FILES = 4

#
# MessageId: ERROR_ACCESS_DENIED
#
# MessageText:
#
# Access is denied.
#
ERROR_ACCESS_DENIED = 5

#
# MessageId: ERROR_INVALID_HANDLE
#
# MessageText:
#
# The handle is invalid.
#
ERROR_INVALID_HANDLE = 6

#
# MessageId: ERROR_ARENA_TRASHED
#
# MessageText:
#
# The storage control blocks were destroyed.
#
ERROR_ARENA_TRASHED = 7

#
# MessageId: ERROR_NOT_ENOUGH_MEMORY
#
# MessageText:
#
# Not enough storage is available to process this command.
#
ERROR_NOT_ENOUGH_MEMORY = 8

#
# MessageId: ERROR_INVALID_BLOCK
#
# MessageText:
#
# The storage control block address is invalid.
#
ERROR_INVALID_BLOCK = 9

#
# MessageId: ERROR_BAD_ENVIRONMENT
#
# MessageText:
#
# The environment is incorrect.
#
ERROR_BAD_ENVIRONMENT = 10

#
# MessageId: ERROR_BAD_FORMAT
#
# MessageText:
#
# An attempt was made to load a program with an incorrect format.
#
ERROR_BAD_FORMAT = 11

#
# MessageId: ERROR_INVALID_ACCESS
#
# MessageText:
#
# The access code is invalid.
#
ERROR_INVALID_ACCESS = 12

#
# MessageId: ERROR_INVALID_DATA
#
# MessageText:
#
# The data is invalid.
#
ERROR_INVALID_DATA = 13

#
# MessageId: ERROR_OUTOFMEMORY
#
# MessageText:
#
# Not enough storage is available to complete this operation.
#
ERROR_OUTOFMEMORY = 14

#
# MessageId: ERROR_INVALID_DRIVE
#
# MessageText:
#
# The system cannot find the drive specified.
#
ERROR_INVALID_DRIVE = 15

#
# MessageId: ERROR_CURRENT_DIRECTORY
#
# MessageText:
#
# The directory cannot be removed.
#
ERROR_CURRENT_DIRECTORY = 16

#
# MessageId: ERROR_NOT_SAME_DEVICE
#
# MessageText:
#
# The system cannot move the file to a different disk drive.
#
ERROR_NOT_SAME_DEVICE = 17

#
# MessageId: ERROR_NO_MORE_FILES
#
# MessageText:
#
# There are no more files.
#
ERROR_NO_MORE_FILES = 18

#
# MessageId: ERROR_WRITE_PROTECT
#
# MessageText:
#
# The media is write protected.
#
ERROR_WRITE_PROTECT = 19

#
# MessageId: ERROR_BAD_UNIT
#
# MessageText:
#
# The system cannot find the device specified.
#
ERROR_BAD_UNIT = 20

#
# MessageId: ERROR_NOT_READY
#
# MessageText:
#
# The device is not ready.
#
ERROR_NOT_READY = 21

#
# MessageId: ERROR_BAD_COMMAND
#
# MessageText:
#
# The device does not recognize the command.
#
ERROR_BAD_COMMAND = 22

#
# MessageId: ERROR_CRC
#
# MessageText:
#
# Data error (cyclic redundancy check).
#
ERROR_CRC = 23

#
# MessageId: ERROR_BAD_LENGTH
#
# MessageText:
#
# The program issued a command but the command length is incorrect.
#
ERROR_BAD_LENGTH = 24

#
# MessageId: ERROR_SEEK
#
# MessageText:
#
# The drive cannot locate a specific area or track on the disk.
#
ERROR_SEEK = 25

#
# MessageId: ERROR_NOT_DOS_DISK
#
# MessageText:
#
# The specified disk or diskette cannot be accessed.
#
ERROR_NOT_DOS_DISK = 26

#
# MessageId: ERROR_SECTOR_NOT_FOUND
#
# MessageText:
#
# The drive cannot find the sector requested.
#
ERROR_SECTOR_NOT_FOUND = 27

#
# MessageId: ERROR_OUT_OF_PAPER
#
# MessageText:
#
# The printer is out of paper.
#
ERROR_OUT_OF_PAPER = 28

#
# MessageId: ERROR_WRITE_FAULT
#
# MessageText:
#
# The system cannot write to the specified device.
#
ERROR_WRITE_FAULT = 29

#
# MessageId: ERROR_READ_FAULT
#
# MessageText:
#
# The system cannot read from the specified device.
#
ERROR_READ_FAULT = 30

#
# MessageId: ERROR_GEN_FAILURE
#
# MessageText:
#
# A device attached to the system is not functioning.
#
ERROR_GEN_FAILURE = 31

#
# MessageId: ERROR_SHARING_VIOLATION
#
# MessageText:
#
# The process cannot access the file because it is being used by another process.
#
ERROR_SHARING_VIOLATION = 32

#
# MessageId: ERROR_LOCK_VIOLATION
#
# MessageText:
#
# The process cannot access the file because another process has locked a portion of the file.
#
ERROR_LOCK_VIOLATION = 33

#
# MessageId: ERROR_WRONG_DISK
#
# MessageText:
#
# The wrong diskette is in the drive.
# Insert %2 (Volume Serial Number: %3) into drive %1.
#
ERROR_WRONG_DISK = 34

#
# MessageId: ERROR_SHARING_BUFFER_EXCEEDED
#
# MessageText:
#
# Too many files opened for sharing.
#
ERROR_SHARING_BUFFER_EXCEEDED = 36

#
# MessageId: ERROR_HANDLE_EOF
#
# MessageText:
#
# Reached the end of the file.
#
ERROR_HANDLE_EOF = 38

#
# MessageId: ERROR_HANDLE_DISK_FULL
#
# MessageText:
#
# The disk is full.
#
ERROR_HANDLE_DISK_FULL = 39

#
# MessageId: ERROR_NOT_SUPPORTED
#
# MessageText:
#
# The request is not supported.
#
ERROR_NOT_SUPPORTED = 50

#
# MessageId: ERROR_REM_NOT_LIST
#
# MessageText:
#
# Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator.
#
ERROR_REM_NOT_LIST = 51

#
# MessageId: ERROR_DUP_NAME
#
# MessageText:
#
# You were not connected because a duplicate name exists on the network. If joining a domain, go to System in Control Panel to change the computer name and try again. If joining a workgroup, choose another workgroup name.
#
ERROR_DUP_NAME = 52

#
# MessageId: ERROR_BAD_NETPATH
#
# MessageText:
#
# The network path was not found.
#
ERROR_BAD_NETPATH = 53

#
# MessageId: ERROR_NETWORK_BUSY
#
# MessageText:
#
# The network is busy.
#
ERROR_NETWORK_BUSY = 54

#
# MessageId: ERROR_DEV_NOT_EXIST
#
# MessageText:
#
# The specified network resource or device is no longer available.
#
ERROR_DEV_NOT_EXIST = 55

#
# MessageId: ERROR_TOO_MANY_CMDS
#
# MessageText:
#
# The network BIOS command limit has been reached.
#
ERROR_TOO_MANY_CMDS = 56

#
# MessageId: ERROR_ADAP_HDW_ERR
#
# MessageText:
#
# A network adapter hardware error occurred.
#
ERROR_ADAP_HDW_ERR = 57

#
# MessageId: ERROR_BAD_NET_RESP
#
# MessageText:
#
# The specified server cannot perform the requested operation.
#
ERROR_BAD_NET_RESP = 58

#
# MessageId: ERROR_UNEXP_NET_ERR
#
# MessageText:
#
# An unexpected network error occurred.
#
ERROR_UNEXP_NET_ERR = 59

#
# MessageId: ERROR_BAD_REM_ADAP
#
# MessageText:
#
# The remote adapter is not compatible.
#
ERROR_BAD_REM_ADAP = 60

#
# MessageId: ERROR_PRINTQ_FULL
#
# MessageText:
#
# The printer queue is full.
#
ERROR_PRINTQ_FULL = 61

#
# MessageId: ERROR_NO_SPOOL_SPACE
#
# MessageText:
#
# Space to store the file waiting to be printed is not available on the server.
#
ERROR_NO_SPOOL_SPACE = 62

#
# MessageId: ERROR_PRINT_CANCELLED
#
# MessageText:
#
# Your file waiting to be printed was deleted.
#
ERROR_PRINT_CANCELLED = 63

#
# MessageId: ERROR_NETNAME_DELETED
#
# MessageText:
#
# The specified network name is no longer available.
#
ERROR_NETNAME_DELETED = 64

#
# MessageId: ERROR_NETWORK_ACCESS_DENIED
#
# MessageText:
#
# Network access is denied.
#
ERROR_NETWORK_ACCESS_DENIED = 65

#
# MessageId: ERROR_BAD_DEV_TYPE
#
# MessageText:
#
# The network resource type is not correct.
#
ERROR_BAD_DEV_TYPE = 66

#
# MessageId: ERROR_BAD_NET_NAME
#
# MessageText:
#
# The network name cannot be found.
#
ERROR_BAD_NET_NAME = 67

#
# MessageId: ERROR_TOO_MANY_NAMES
#
# MessageText:
#
# The name limit for the local computer network adapter card was exceeded.
#
ERROR_TOO_MANY_NAMES = 68

#
# MessageId: ERROR_TOO_MANY_SESS
#
# MessageText:
#
# The network BIOS session limit was exceeded.
#
ERROR_TOO_MANY_SESS = 69

#
# MessageId: ERROR_SHARING_PAUSED
#
# MessageText:
#
# The remote server has been paused or is in the process of being started.
#
ERROR_SHARING_PAUSED = 70

#
# MessageId: ERROR_REQ_NOT_ACCEP
#
# MessageText:
#
# No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.
#
ERROR_REQ_NOT_ACCEP = 71

#
# MessageId: ERROR_REDIR_PAUSED
#
# MessageText:
#
# The specified printer or disk device has been paused.
#
ERROR_REDIR_PAUSED = 72

#
# MessageId: ERROR_FILE_EXISTS
#
# MessageText:
#
# The file exists.
#
ERROR_FILE_EXISTS = 80

#
# MessageId: ERROR_CANNOT_MAKE
#
# MessageText:
#
# The directory or file cannot be created.
#
ERROR_CANNOT_MAKE = 82

#
# MessageId: ERROR_FAIL_I24
#
# MessageText:
#
# Fail on INT 24.
#
ERROR_FAIL_I24 = 83

#
# MessageId: ERROR_OUT_OF_STRUCTURES
#
# MessageText:
#
# Storage to process this request is not available.
#
ERROR_OUT_OF_STRUCTURES = 84

#
# MessageId: ERROR_ALREADY_ASSIGNED
#
# MessageText:
#
# The local device name is already in use.
#
ERROR_ALREADY_ASSIGNED = 85

#
# MessageId: ERROR_INVALID_PASSWORD
#
# MessageText:
#
# The specified network password is not correct.
#
ERROR_INVALID_PASSWORD = 86

#
# MessageId: ERROR_INVALID_PARAMETER
#
# MessageText:
#
# The parameter is incorrect.
#
ERROR_INVALID_PARAMETER = 87

#
# MessageId: ERROR_NET_WRITE_FAULT
#
# MessageText:
#
# A write fault occurred on the network.
#
ERROR_NET_WRITE_FAULT = 88

#
# MessageId: ERROR_NO_PROC_SLOTS
#
# MessageText:
#
# The system cannot start another process at this time.
#
ERROR_NO_PROC_SLOTS = 89

#
# MessageId: ERROR_TOO_MANY_SEMAPHORES
#
# MessageText:
#
# Cannot create another system semaphore.
#
ERROR_TOO_MANY_SEMAPHORES = 100

#
# MessageId: ERROR_EXCL_SEM_ALREADY_OWNED
#
# MessageText:
#
# The exclusive semaphore is owned by another process.
#
ERROR_EXCL_SEM_ALREADY_OWNED = 101

#
# MessageId: ERROR_SEM_IS_SET
#
# MessageText:
#
# The semaphore is set and cannot be closed.
#
ERROR_SEM_IS_SET = 102

#
# MessageId: ERROR_TOO_MANY_SEM_REQUESTS
#
# MessageText:
#
# The semaphore cannot be set again.
#
ERROR_TOO_MANY_SEM_REQUESTS = 103

#
# MessageId: ERROR_INVALID_AT_INTERRUPT_TIME
#
# MessageText:
#
# Cannot request exclusive semaphores at interrupt time.
#
ERROR_INVALID_AT_INTERRUPT_TIME = 104

#
# MessageId: ERROR_SEM_OWNER_DIED
#
# MessageText:
#
# The previous ownership of this semaphore has ended.
#
ERROR_SEM_OWNER_DIED = 105

#
# MessageId: ERROR_SEM_USER_LIMIT
#
# MessageText:
#
# Insert the diskette for drive %1.
#
ERROR_SEM_USER_LIMIT = 106

#
# MessageId: ERROR_DISK_CHANGE
#
# MessageText:
#
# The program stopped because an alternate diskette was not inserted.
#
ERROR_DISK_CHANGE = 107

#
# MessageId: ERROR_DRIVE_LOCKED
#
# MessageText:
#
# The disk is in use or locked by another process.
#
ERROR_DRIVE_LOCKED = 108

#
# MessageId: ERROR_BROKEN_PIPE
#
# MessageText:
#
# The pipe has been ended.
#
ERROR_BROKEN_PIPE = 109

#
# MessageId: ERROR_OPEN_FAILED
#
# MessageText:
#
# The system cannot open the device or file specified.
#
ERROR_OPEN_FAILED = 110

#
# MessageId: ERROR_BUFFER_OVERFLOW
#
# MessageText:
#
# The file name is too long.
#
ERROR_BUFFER_OVERFLOW = 111

#
# MessageId: ERROR_DISK_FULL
#
# MessageText:
#
# There is not enough space on the disk.
#
ERROR_DISK_FULL = 112

#
# MessageId: ERROR_NO_MORE_SEARCH_HANDLES
#
# MessageText:
#
# No more internal file identifiers available.
#
ERROR_NO_MORE_SEARCH_HANDLES = 113

#
# MessageId: ERROR_INVALID_TARGET_HANDLE
#
# MessageText:
#
# The target internal file identifier is incorrect.
#
ERROR_INVALID_TARGET_HANDLE = 114

#
# MessageId: ERROR_INVALID_CATEGORY
#
# MessageText:
#
# The IOCTL call made by the application program is not correct.
#
ERROR_INVALID_CATEGORY = 117

#
# MessageId: ERROR_INVALID_VERIFY_SWITCH
#
# MessageText:
#
# The verify-on-write switch parameter value is not correct.
#
ERROR_INVALID_VERIFY_SWITCH = 118

#
# MessageId: ERROR_BAD_DRIVER_LEVEL
#
# MessageText:
#
# The system does not support the command requested.
#
ERROR_BAD_DRIVER_LEVEL = 119

#
# MessageId: ERROR_CALL_NOT_IMPLEMENTED
#
# MessageText:
#
# This function is not supported on this system.
#
ERROR_CALL_NOT_IMPLEMENTED = 120

#
# MessageId: ERROR_SEM_TIMEOUT
#
# MessageText:
#
# The semaphore timeout period has expired.
#
ERROR_SEM_TIMEOUT = 121

#
# MessageId: ERROR_INSUFFICIENT_BUFFER
#
# MessageText:
#
# The data area passed to a system call is too small.
#
ERROR_INSUFFICIENT_BUFFER = 122

#
# MessageId: ERROR_INVALID_NAME
#
# MessageText:
#
# The filename, directory name, or volume label syntax is incorrect.
#
ERROR_INVALID_NAME = 123

#
# MessageId: ERROR_INVALID_LEVEL
#
# MessageText:
#
# The system call level is not correct.
#
ERROR_INVALID_LEVEL = 124

#
# MessageId: ERROR_NO_VOLUME_LABEL
#
# MessageText:
#
# The disk has no volume label.
#
ERROR_NO_VOLUME_LABEL = 125

#
# MessageId: ERROR_MOD_NOT_FOUND
#
# MessageText:
#
# The specified module could not be found.
#
ERROR_MOD_NOT_FOUND = 126

#
# MessageId: ERROR_PROC_NOT_FOUND
#
# MessageText:
#
# The specified procedure could not be found.
#
ERROR_PROC_NOT_FOUND = 127

#
# MessageId: ERROR_WAIT_NO_CHILDREN
#
# MessageText:
#
# There are no child processes to wait for.
#
ERROR_WAIT_NO_CHILDREN = 128

#
# MessageId: ERROR_CHILD_NOT_COMPLETE
#
# MessageText:
#
# The %1 application cannot be run in Win32 mode.
#
ERROR_CHILD_NOT_COMPLETE = 129

#
# MessageId: ERROR_DIRECT_ACCESS_HANDLE
#
# MessageText:
#
# Attempt to use a file handle to an open disk partition for an operation other than raw disk I/O.
#
ERROR_DIRECT_ACCESS_HANDLE = 130

#
# MessageId: ERROR_NEGATIVE_SEEK
#
# MessageText:
#
# An attempt was made to move the file pointer before the beginning of the file.
#
ERROR_NEGATIVE_SEEK = 131

#
# MessageId: ERROR_SEEK_ON_DEVICE
#
# MessageText:
#
# The file pointer cannot be set on the specified device or file.
#
ERROR_SEEK_ON_DEVICE = 132

#
# MessageId: ERROR_IS_JOIN_TARGET
#
# MessageText:
#
# A JOIN or SUBST command cannot be used for a drive that contains previously joined drives.
#
ERROR_IS_JOIN_TARGET = 133

#
# MessageId: ERROR_IS_JOINED
#
# MessageText:
#
# An attempt was made to use a JOIN or SUBST command on a drive that has already been joined.
#
ERROR_IS_JOINED = 134

#
# MessageId: ERROR_IS_SUBSTED
#
# MessageText:
#
# An attempt was made to use a JOIN or SUBST command on a drive that has already been substituted.
#
ERROR_IS_SUBSTED = 135

#
# MessageId: ERROR_NOT_JOINED
#
# MessageText:
#
# The system tried to delete the JOIN of a drive that is not joined.
#
ERROR_NOT_JOINED = 136

#
# MessageId: ERROR_NOT_SUBSTED
#
# MessageText:
#
# The system tried to delete the substitution of a drive that is not substituted.
#
ERROR_NOT_SUBSTED = 137

#
# MessageId: ERROR_JOIN_TO_JOIN
#
# MessageText:
#
# The system tried to join a drive to a directory on a joined drive.
#
ERROR_JOIN_TO_JOIN = 138

#
# MessageId: ERROR_SUBST_TO_SUBST
#
# MessageText:
#
# The system tried to substitute a drive to a directory on a substituted drive.
#
ERROR_SUBST_TO_SUBST = 139

#
# MessageId: ERROR_JOIN_TO_SUBST
#
# MessageText:
#
# The system tried to join a drive to a directory on a substituted drive.
#
ERROR_JOIN_TO_SUBST = 140

#
# MessageId: ERROR_SUBST_TO_JOIN
#
# MessageText:
#
# The system tried to SUBST a drive to a directory on a joined drive.
#
ERROR_SUBST_TO_JOIN = 141

#
# MessageId: ERROR_BUSY_DRIVE
#
# MessageText:
#
# The system cannot perform a JOIN or SUBST at this time.
#
ERROR_BUSY_DRIVE = 142

#
# MessageId: ERROR_SAME_DRIVE
#
# MessageText:
#
# The system cannot join or substitute a drive to or for a directory on the same drive.
#
ERROR_SAME_DRIVE = 143

#
# MessageId: ERROR_DIR_NOT_ROOT
#
# MessageText:
#
# The directory is not a subdirectory of the root directory.
#
ERROR_DIR_NOT_ROOT = 144

#
# MessageId: ERROR_DIR_NOT_EMPTY
#
# MessageText:
#
# The directory is not empty.
#
ERROR_DIR_NOT_EMPTY = 145

#
# MessageId: ERROR_IS_SUBST_PATH
#
# MessageText:
#
# The path specified is being used in a substitute.
#
ERROR_IS_SUBST_PATH = 146

#
# MessageId: ERROR_IS_JOIN_PATH
#
# MessageText:
#
# Not enough resources are available to process this command.
#
ERROR_IS_JOIN_PATH = 147

#
# MessageId: ERROR_PATH_BUSY
#
# MessageText:
#
# The path specified cannot be used at this time.
#
ERROR_PATH_BUSY = 148

#
# MessageId: ERROR_IS_SUBST_TARGET
#
# MessageText:
#
# An attempt was made to join or substitute a drive for which a directory on the drive is the target of a previous substitute.
#
ERROR_IS_SUBST_TARGET = 149

#
# MessageId: ERROR_SYSTEM_TRACE
#
# MessageText:
#
# System trace information was not specified in your CONFIG.SYS file, or tracing is disallowed.
#
ERROR_SYSTEM_TRACE = 150

#
# MessageId: ERROR_INVALID_EVENT_COUNT
#
# MessageText:
#
# The number of specified semaphore events for DosMuxSemWait is not correct.
#
ERROR_INVALID_EVENT_COUNT = 151

#
# MessageId: ERROR_TOO_MANY_MUXWAITERS
#
# MessageText:
#
# DosMuxSemWait did not execute; too many semaphores are already set.
#
ERROR_TOO_MANY_MUXWAITERS = 152

#
# MessageId: ERROR_INVALID_LIST_FORMAT
#
# MessageText:
#
# The DosMuxSemWait list is not correct.
#
ERROR_INVALID_LIST_FORMAT = 153

#
# MessageId: ERROR_LABEL_TOO_LONG
#
# MessageText:
#
# The volume label you entered exceeds the label character limit of the target file system.
#
ERROR_LABEL_TOO_LONG = 154

#
# MessageId: ERROR_TOO_MANY_TCBS
#
# MessageText:
#
# Cannot create another thread.
#
ERROR_TOO_MANY_TCBS = 155

#
# MessageId: ERROR_SIGNAL_REFUSED
#
# MessageText:
#
# The recipient process has refused the signal.
#
ERROR_SIGNAL_REFUSED = 156

#
# MessageId: ERROR_DISCARDED
#
# MessageText:
#
# The segment is already discarded and cannot be locked.
#
ERROR_DISCARDED = 157

#
# MessageId: ERROR_NOT_LOCKED
#
# MessageText:
#
# The segment is already unlocked.
#
ERROR_NOT_LOCKED = 158

#
# MessageId: ERROR_BAD_THREADID_ADDR
#
# MessageText:
#
# The address for the thread ID is not correct.
#
ERROR_BAD_THREADID_ADDR = 159

#
# MessageId: ERROR_BAD_ARGUMENTS
#
# MessageText:
#
# One or more arguments are not correct.
#
ERROR_BAD_ARGUMENTS = 160

#
# MessageId: ERROR_BAD_PATHNAME
#
# MessageText:
#
# The specified path is invalid.
#
ERROR_BAD_PATHNAME = 161

#
# MessageId: ERROR_SIGNAL_PENDING
#
# MessageText:
#
# A signal is already pending.
#
ERROR_SIGNAL_PENDING = 162

#
# MessageId: ERROR_MAX_THRDS_REACHED
#
# MessageText:
#
# No more threads can be created in the system.
#
ERROR_MAX_THRDS_REACHED = 164

#
# MessageId: ERROR_LOCK_FAILED
#
# MessageText:
#
# Unable to lock a region of a file.
#
ERROR_LOCK_FAILED = 167

#
# MessageId: ERROR_BUSY
#
# MessageText:
#
# The requested resource is in use.
#
ERROR_BUSY = 170

#
# MessageId: ERROR_DEVICE_SUPPORT_IN_PROGRESS
#
# MessageText:
#
# Device's command support detection is in progress.
#
ERROR_DEVICE_SUPPORT_IN_PROGRESS = 171

#
# MessageId: ERROR_CANCEL_VIOLATION
#
# MessageText:
#
# A lock request was not outstanding for the supplied cancel region.
#
ERROR_CANCEL_VIOLATION = 173

#
# MessageId: ERROR_ATOMIC_LOCKS_NOT_SUPPORTED
#
# MessageText:
#
# The file system does not support atomic changes to the lock type.
#
ERROR_ATOMIC_LOCKS_NOT_SUPPORTED = 174

#
# MessageId: ERROR_INVALID_SEGMENT_NUMBER
#
# MessageText:
#
# The system detected a segment number that was not correct.
#
ERROR_INVALID_SEGMENT_NUMBER = 180

#
# MessageId: ERROR_INVALID_ORDINAL
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_INVALID_ORDINAL = 182

#
# MessageId: ERROR_ALREADY_EXISTS
#
# MessageText:
#
# Cannot create a file when that file already exists.
#
ERROR_ALREADY_EXISTS = 183

#
# MessageId: ERROR_INVALID_FLAG_NUMBER
#
# MessageText:
#
# The flag passed is not correct.
#
ERROR_INVALID_FLAG_NUMBER = 186

#
# MessageId: ERROR_SEM_NOT_FOUND
#
# MessageText:
#
# The specified system semaphore name was not found.
#
ERROR_SEM_NOT_FOUND = 187

#
# MessageId: ERROR_INVALID_STARTING_CODESEG
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_INVALID_STARTING_CODESEG = 188

#
# MessageId: ERROR_INVALID_STACKSEG
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_INVALID_STACKSEG = 189

#
# MessageId: ERROR_INVALID_MODULETYPE
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_INVALID_MODULETYPE = 190

#
# MessageId: ERROR_INVALID_EXE_SIGNATURE
#
# MessageText:
#
# Cannot run %1 in Win32 mode.
#
ERROR_INVALID_EXE_SIGNATURE = 191

#
# MessageId: ERROR_EXE_MARKED_INVALID
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_EXE_MARKED_INVALID = 192

#
# MessageId: ERROR_BAD_EXE_FORMAT
#
# MessageText:
#
# %1 is not a valid Win32 application.
#
ERROR_BAD_EXE_FORMAT = 193

#
# MessageId: ERROR_ITERATED_DATA_EXCEEDS_64k
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_ITERATED_DATA_EXCEEDS_64k = 194

#
# MessageId: ERROR_INVALID_MINALLOCSIZE
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_INVALID_MINALLOCSIZE = 195

#
# MessageId: ERROR_DYNLINK_FROM_INVALID_RING
#
# MessageText:
#
# The operating system cannot run this application program.
#
ERROR_DYNLINK_FROM_INVALID_RING = 196

#
# MessageId: ERROR_IOPL_NOT_ENABLED
#
# MessageText:
#
# The operating system is not presently configured to run this application.
#
ERROR_IOPL_NOT_ENABLED = 197

#
# MessageId: ERROR_INVALID_SEGDPL
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_INVALID_SEGDPL = 198

#
# MessageId: ERROR_AUTODATASEG_EXCEEDS_64k
#
# MessageText:
#
# The operating system cannot run this application program.
#
ERROR_AUTODATASEG_EXCEEDS_64k = 199

#
# MessageId: ERROR_RING2SEG_MUST_BE_MOVABLE
#
# MessageText:
#
# The code segment cannot be greater than or equal to 64K.
#
ERROR_RING2SEG_MUST_BE_MOVABLE = 200

#
# MessageId: ERROR_RELOC_CHAIN_XEEDS_SEGLIM
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_RELOC_CHAIN_XEEDS_SEGLIM = 201

#
# MessageId: ERROR_INFLOOP_IN_RELOC_CHAIN
#
# MessageText:
#
# The operating system cannot run %1.
#
ERROR_INFLOOP_IN_RELOC_CHAIN = 202

#
# MessageId: ERROR_ENVVAR_NOT_FOUND
#
# MessageText:
#
# The system could not find the environment option that was entered.
#
ERROR_ENVVAR_NOT_FOUND = 203

#
# MessageId: ERROR_NO_SIGNAL_SENT
#
# MessageText:
#
# No process in the command subtree has a signal handler.
#
ERROR_NO_SIGNAL_SENT = 205

#
# MessageId: ERROR_FILENAME_EXCED_RANGE
#
# MessageText:
#
# The filename or extension is too long.
#
ERROR_FILENAME_EXCED_RANGE = 206

#
# MessageId: ERROR_RING2_STACK_IN_USE
#
# MessageText:
#
# The ring 2 stack is in use.
#
ERROR_RING2_STACK_IN_USE = 207

#
# MessageId: ERROR_META_EXPANSION_TOO_LONG
#
# MessageText:
#
# The global filename characters, * or ?, are entered incorrectly or too many global filename characters are specified.
#
ERROR_META_EXPANSION_TOO_LONG = 208

#
# MessageId: ERROR_INVALID_SIGNAL_NUMBER
#
# MessageText:
#
# The signal being posted is not correct.
#
ERROR_INVALID_SIGNAL_NUMBER = 209

#
# MessageId: ERROR_THREAD_1_INACTIVE
#
# MessageText:
#
# The signal handler cannot be set.
#
ERROR_THREAD_1_INACTIVE = 210

#
# MessageId: ERROR_LOCKED
#
# MessageText:
#
# The segment is locked and cannot be reallocated.
#
ERROR_LOCKED = 212

#
# MessageId: ERROR_TOO_MANY_MODULES
#
# MessageText:
#
# Too many dynamic-link modules are attached to this program or dynamic-link module.
#
ERROR_TOO_MANY_MODULES = 214

#
# MessageId: ERROR_NESTING_NOT_ALLOWED
#
# MessageText:
#
# Cannot nest calls to LoadModule.
#
ERROR_NESTING_NOT_ALLOWED = 215

#
# MessageId: ERROR_EXE_MACHINE_TYPE_MISMATCH
#
# MessageText:
#
# This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher.
#
ERROR_EXE_MACHINE_TYPE_MISMATCH = 216

#
# MessageId: ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY
#
# MessageText:
#
# The image file %1 is signed, unable to modify.
#
ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY = 217

#
# MessageId: ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY
#
# MessageText:
#
# The image file %1 is strong signed, unable to modify.
#
ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY = 218

#
# MessageId: ERROR_FILE_CHECKED_OUT
#
# MessageText:
#
# This file is checked out or locked for editing by another user.
#
ERROR_FILE_CHECKED_OUT = 220

#
# MessageId: ERROR_CHECKOUT_REQUIRED
#
# MessageText:
#
# The file must be checked out before saving changes.
#
ERROR_CHECKOUT_REQUIRED = 221

#
# MessageId: ERROR_BAD_FILE_TYPE
#
# MessageText:
#
# The file type being saved or retrieved has been blocked.
#
ERROR_BAD_FILE_TYPE = 222

#
# MessageId: ERROR_FILE_TOO_LARGE
#
# MessageText:
#
# The file size exceeds the limit allowed and cannot be saved.
#
ERROR_FILE_TOO_LARGE = 223

#
# MessageId: ERROR_FORMS_AUTH_REQUIRED
#
# MessageText:
#
# Access Denied. Before opening files in this location, you must first add the web site to your trusted sites list, browse to the web site, and select the option to login automatically.
#
ERROR_FORMS_AUTH_REQUIRED = 224

#
# MessageId: ERROR_VIRUS_INFECTED
#
# MessageText:
#
# Operation did not complete successfully because the file contains a virus or potentially unwanted software.
#
ERROR_VIRUS_INFECTED = 225

#
# MessageId: ERROR_VIRUS_DELETED
#
# MessageText:
#
# This file contains a virus or potentially unwanted software and cannot be opened. Due to the nature of this virus or potentially unwanted software, the file has been removed from this location.
#
ERROR_VIRUS_DELETED = 226

#
# MessageId: ERROR_PIPE_LOCAL
#
# MessageText:
#
# The pipe is local.
#
ERROR_PIPE_LOCAL = 229

#
# MessageId: ERROR_BAD_PIPE
#
# MessageText:
#
# The pipe state is invalid.
#
ERROR_BAD_PIPE = 230

#
# MessageId: ERROR_PIPE_BUSY
#
# MessageText:
#
# All pipe instances are busy.
#
ERROR_PIPE_BUSY = 231

#
# MessageId: ERROR_NO_DATA
#
# MessageText:
#
# The pipe is being closed.
#
ERROR_NO_DATA = 232

#
# MessageId: ERROR_PIPE_NOT_CONNECTED
#
# MessageText:
#
# No process is on the other end of the pipe.
#
ERROR_PIPE_NOT_CONNECTED = 233

#
# MessageId: ERROR_MORE_DATA
#
# MessageText:
#
# More data is available.
#
ERROR_MORE_DATA = 234

#
# MessageId: ERROR_VC_DISCONNECTED
#
# MessageText:
#
# The session was canceled.
#
ERROR_VC_DISCONNECTED = 240

#
# MessageId: ERROR_INVALID_EA_NAME
#
# MessageText:
#
# The specified extended attribute name was invalid.
#
ERROR_INVALID_EA_NAME = 254

#
# MessageId: ERROR_EA_LIST_INCONSISTENT
#
# MessageText:
#
# The extended attributes are inconsistent.
#
ERROR_EA_LIST_INCONSISTENT = 255

#
# MessageId: WAIT_TIMEOUT
#
# MessageText:
#
# The wait operation timed out.
#
WAIT_TIMEOUT = 258

#
# MessageId: ERROR_NO_MORE_ITEMS
#
# MessageText:
#
# No more data is available.
#
ERROR_NO_MORE_ITEMS = 259

#
# MessageId: ERROR_CANNOT_COPY
#
# MessageText:
#
# The copy functions cannot be used.
#
ERROR_CANNOT_COPY = 266

#
# MessageId: ERROR_DIRECTORY
#
# MessageText:
#
# The directory name is invalid.
#
ERROR_DIRECTORY = 267

#
# MessageId: ERROR_EAS_DIDNT_FIT
#
# MessageText:
#
# The extended attributes did not fit in the buffer.
#
ERROR_EAS_DIDNT_FIT = 275

#
# MessageId: ERROR_EA_FILE_CORRUPT
#
# MessageText:
#
# The extended attribute file on the mounted file system is corrupt.
#
ERROR_EA_FILE_CORRUPT = 276

#
# MessageId: ERROR_EA_TABLE_FULL
#
# MessageText:
#
# The extended attribute table file is full.
#
ERROR_EA_TABLE_FULL = 277

#
# MessageId: ERROR_INVALID_EA_HANDLE
#
# MessageText:
#
# The specified extended attribute handle is invalid.
#
ERROR_INVALID_EA_HANDLE = 278

#
# MessageId: ERROR_EAS_NOT_SUPPORTED
#
# MessageText:
#
# The mounted file system does not support extended attributes.
#
ERROR_EAS_NOT_SUPPORTED = 282

#
# MessageId: ERROR_NOT_OWNER
#
# MessageText:
#
# Attempt to release mutex not owned by caller.
#
ERROR_NOT_OWNER = 288

#
# MessageId: ERROR_TOO_MANY_POSTS
#
# MessageText:
#
# Too many posts were made to a semaphore.
#
ERROR_TOO_MANY_POSTS = 298

#
# MessageId: ERROR_PARTIAL_COPY
#
# MessageText:
#
# Only part of a ReadProcessMemory or WriteProcessMemory request was completed.
#
ERROR_PARTIAL_COPY = 299

#
# MessageId: ERROR_OPLOCK_NOT_GRANTED
#
# MessageText:
#
# The oplock request is denied.
#
ERROR_OPLOCK_NOT_GRANTED = 300

#
# MessageId: ERROR_INVALID_OPLOCK_PROTOCOL
#
# MessageText:
#
# An invalid oplock acknowledgment was received by the system.
#
ERROR_INVALID_OPLOCK_PROTOCOL = 301

#
# MessageId: ERROR_DISK_TOO_FRAGMENTED
#
# MessageText:
#
# The volume is too fragmented to complete this operation.
#
ERROR_DISK_TOO_FRAGMENTED = 302

#
# MessageId: ERROR_DELETE_PENDING
#
# MessageText:
#
# The file cannot be opened because it is in the process of being deleted.
#
ERROR_DELETE_PENDING = 303

#
# MessageId: ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING
#
# MessageText:
#
# Short name settings may not be changed on this volume due to the global registry setting.
#
ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING = 304

#
# MessageId: ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME
#
# MessageText:
#
# Short names are not enabled on this volume.
#
ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME = 305

#
# MessageId: ERROR_SECURITY_STREAM_IS_INCONSISTENT
#
# MessageText:
#
# The security stream for the given volume is in an inconsistent state.
# Please run CHKDSK on the volume.
#
ERROR_SECURITY_STREAM_IS_INCONSISTENT = 306

#
# MessageId: ERROR_INVALID_LOCK_RANGE
#
# MessageText:
#
# A requested file lock operation cannot be processed due to an invalid byte range.
#
ERROR_INVALID_LOCK_RANGE = 307

#
# MessageId: ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT
#
# MessageText:
#
# The subsystem needed to support the image type is not present.
#
ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT = 308

#
# MessageId: ERROR_NOTIFICATION_GUID_ALREADY_DEFINED
#
# MessageText:
#
# The specified file already has a notification GUID associated with it.
#
ERROR_NOTIFICATION_GUID_ALREADY_DEFINED = 309

#
# MessageId: ERROR_INVALID_EXCEPTION_HANDLER
#
# MessageText:
#
# An invalid exception handler routine has been detected.
#
ERROR_INVALID_EXCEPTION_HANDLER = 310

#
# MessageId: ERROR_DUPLICATE_PRIVILEGES
#
# MessageText:
#
# Duplicate privileges were specified for the token.
#
ERROR_DUPLICATE_PRIVILEGES = 311

#
# MessageId: ERROR_NO_RANGES_PROCESSED
#
# MessageText:
#
# No ranges for the specified operation were able to be processed.
#
ERROR_NO_RANGES_PROCESSED = 312

#
# MessageId: ERROR_NOT_ALLOWED_ON_SYSTEM_FILE
#
# MessageText:
#
# Operation is not allowed on a file system internal file.
#
ERROR_NOT_ALLOWED_ON_SYSTEM_FILE = 313

#
# MessageId: ERROR_DISK_RESOURCES_EXHAUSTED
#
# MessageText:
#
# The physical resources of this disk have been exhausted.
#
ERROR_DISK_RESOURCES_EXHAUSTED = 314

#
# MessageId: ERROR_INVALID_TOKEN
#
# MessageText:
#
# The token representing the data is invalid.
#
ERROR_INVALID_TOKEN = 315

#
# MessageId: ERROR_DEVICE_FEATURE_NOT_SUPPORTED
#
# MessageText:
#
# The device does not support the command feature.
#
ERROR_DEVICE_FEATURE_NOT_SUPPORTED = 316

#
# MessageId: ERROR_MR_MID_NOT_FOUND
#
# MessageText:
#
# The system cannot find message text for message number 0x%1 in the message file for %2.
#
ERROR_MR_MID_NOT_FOUND = 317

#
# MessageId: ERROR_SCOPE_NOT_FOUND
#
# MessageText:
#
# The scope specified was not found.
#
ERROR_SCOPE_NOT_FOUND = 318

#
# MessageId: ERROR_UNDEFINED_SCOPE
#
# MessageText:
#
# The Central Access Policy specified is not defined on the target machine.
#
ERROR_UNDEFINED_SCOPE = 319

#
# MessageId: ERROR_INVALID_CAP
#
# MessageText:
#
# The Central Access Policy obtained from Active Directory is invalid.
#
ERROR_INVALID_CAP = 320

#
# MessageId: ERROR_DEVICE_UNREACHABLE
#
# MessageText:
#
# The device is unreachable.
#
ERROR_DEVICE_UNREACHABLE = 321

#
# MessageId: ERROR_DEVICE_NO_RESOURCES
#
# MessageText:
#
# The target device has insufficient resources to complete the operation.
#
ERROR_DEVICE_NO_RESOURCES = 322

#
# MessageId: ERROR_DATA_CHECKSUM_ERROR
#
# MessageText:
#
# A data integrity checksum error occurred. Data in the file stream is corrupt.
#
ERROR_DATA_CHECKSUM_ERROR = 323

#
# MessageId: ERROR_INTERMIXED_KERNEL_EA_OPERATION
#
# MessageText:
#
# An attempt was made to modify both a KERNEL and normal Extended Attribute (EA) in the same operation.
#
ERROR_INTERMIXED_KERNEL_EA_OPERATION = 324

#
# MessageId: ERROR_FILE_LEVEL_TRIM_NOT_SUPPORTED
#
# MessageText:
#
# Device does not support file-level TRIM.
#
ERROR_FILE_LEVEL_TRIM_NOT_SUPPORTED = 326

#
# MessageId: ERROR_OFFSET_ALIGNMENT_VIOLATION
#
# MessageText:
#
# The command specified a data offset that does not align to the device's granularity/alignment.
#
ERROR_OFFSET_ALIGNMENT_VIOLATION = 327

#
# MessageId: ERROR_INVALID_FIELD_IN_PARAMETER_LIST
#
# MessageText:
#
# The command specified an invalid field in its parameter list.
#
ERROR_INVALID_FIELD_IN_PARAMETER_LIST = 328

#
# MessageId: ERROR_OPERATION_IN_PROGRESS
#
# MessageText:
#
# An operation is currently in progress with the device.
#
ERROR_OPERATION_IN_PROGRESS = 329

#
# MessageId: ERROR_BAD_DEVICE_PATH
#
# MessageText:
#
# An attempt was made to send down the command via an invalid path to the target device.
#
ERROR_BAD_DEVICE_PATH = 330

#
# MessageId: ERROR_TOO_MANY_DESCRIPTORS
#
# MessageText:
#
# The command specified a number of descriptors that exceeded the maximum supported by the device.
#
ERROR_TOO_MANY_DESCRIPTORS = 331

#
# MessageId: ERROR_SCRUB_DATA_DISABLED
#
# MessageText:
#
# Scrub is disabled on the specified file.
#
ERROR_SCRUB_DATA_DISABLED = 332

#
# MessageId: ERROR_NOT_REDUNDANT_STORAGE
#
# MessageText:
#
# The storage device does not provide redundancy.
#
ERROR_NOT_REDUNDANT_STORAGE = 333

#
# MessageId: ERROR_RESIDENT_FILE_NOT_SUPPORTED
#
# MessageText:
#
# An operation is not supported on a resident file.
#
ERROR_RESIDENT_FILE_NOT_SUPPORTED = 334

#
# MessageId: ERROR_COMPRESSED_FILE_NOT_SUPPORTED
#
# MessageText:
#
# An operation is not supported on a compressed file.
#
ERROR_COMPRESSED_FILE_NOT_SUPPORTED = 335

#
# MessageId: ERROR_DIRECTORY_NOT_SUPPORTED
#
# MessageText:
#
# An operation is not supported on a directory.
#
ERROR_DIRECTORY_NOT_SUPPORTED = 336

#
# MessageId: ERROR_NOT_READ_FROM_COPY
#
# MessageText:
#
# The specified copy of the requested data could not be read.
#
ERROR_NOT_READ_FROM_COPY = 337

#
# MessageId: ERROR_FT_WRITE_FAILURE
#
# MessageText:
#
# The specified data could not be written to any of the copies.
#
ERROR_FT_WRITE_FAILURE = 338

#
# MessageId: ERROR_FT_DI_SCAN_REQUIRED
#
# MessageText:
#
# One or more copies of data on this device may be out of sync. No writes may be performed until a data integrity scan is completed.
#
ERROR_FT_DI_SCAN_REQUIRED = 339

#
# MessageId: ERROR_INVALID_KERNEL_INFO_VERSION
#
# MessageText:
#
# The supplied kernel information version is invalid.
#
ERROR_INVALID_KERNEL_INFO_VERSION = 340

#
# MessageId: ERROR_INVALID_PEP_INFO_VERSION
#
# MessageText:
#
# The supplied PEP information version is invalid.
#
ERROR_INVALID_PEP_INFO_VERSION = 341

#
# **** Available SYSTEM error codes ****
#
#
# MessageId: ERROR_FAIL_NOACTION_REBOOT
#
# MessageText:
#
# No action was taken as a system reboot is required.
#
ERROR_FAIL_NOACTION_REBOOT = 350

#
# MessageId: ERROR_FAIL_SHUTDOWN
#
# MessageText:
#
# The shutdown operation failed.
#
ERROR_FAIL_SHUTDOWN = 351

#
# MessageId: ERROR_FAIL_RESTART
#
# MessageText:
#
# The restart operation failed.
#
ERROR_FAIL_RESTART = 352

#
# MessageId: ERROR_MAX_SESSIONS_REACHED
#
# MessageText:
#
# The maximum number of sessions has been reached.
#
ERROR_MAX_SESSIONS_REACHED = 353

#
# **** Available SYSTEM error codes ****
#
#
# MessageId: ERROR_THREAD_MODE_ALREADY_BACKGROUND
#
# MessageText:
#
# The thread is already in background processing mode.
#
ERROR_THREAD_MODE_ALREADY_BACKGROUND = 400

#
# MessageId: ERROR_THREAD_MODE_NOT_BACKGROUND
#
# MessageText:
#
# The thread is not in background processing mode.
#
ERROR_THREAD_MODE_NOT_BACKGROUND = 401

#
# MessageId: ERROR_PROCESS_MODE_ALREADY_BACKGROUND
#
# MessageText:
#
# The process is already in background processing mode.
#
ERROR_PROCESS_MODE_ALREADY_BACKGROUND = 402

#
# MessageId: ERROR_PROCESS_MODE_NOT_BACKGROUND
#
# MessageText:
#
# The process is not in background processing mode.
#
ERROR_PROCESS_MODE_NOT_BACKGROUND = 403

#
# **** Available SYSTEM error codes ****
#
#
# MessageId: ERROR_DEVICE_HARDWARE_ERROR
#
# MessageText:
#
# The request failed due to a fatal device hardware error.
#
ERROR_DEVICE_HARDWARE_ERROR = 483

#
# MessageId: ERROR_INVALID_ADDRESS
#
# MessageText:
#
# Attempt to access invalid address.
#
ERROR_INVALID_ADDRESS = 487

#
# **** Available SYSTEM error codes ****
#
#
# MessageId: ERROR_USER_PROFILE_LOAD
#
# MessageText:
#
# User profile cannot be loaded.
#
ERROR_USER_PROFILE_LOAD = 500

#
# **** Available SYSTEM error codes ****
#
#
# MessageId: ERROR_ARITHMETIC_OVERFLOW
#
# MessageText:
#
# Arithmetic result exceeded 32 bits.
#
ERROR_ARITHMETIC_OVERFLOW = 534

#
# MessageId: ERROR_PIPE_CONNECTED
#
# MessageText:
#
# There is a process on other end of the pipe.
#
ERROR_PIPE_CONNECTED = 535

#
# MessageId: ERROR_PIPE_LISTENING
#
# MessageText:
#
# Waiting for a process to open the other end of the pipe.
#
ERROR_PIPE_LISTENING = 536

#
# MessageId: ERROR_VERIFIER_STOP
#
# MessageText:
#
# Application verifier has found an error in the current process.
#
ERROR_VERIFIER_STOP = 537

#
# MessageId: ERROR_ABIOS_ERROR
#
# MessageText:
#
# An error occurred in the ABIOS subsystem.
#
ERROR_ABIOS_ERROR = 538

#
# MessageId: ERROR_WX86_WARNING
#
# MessageText:
#
# A warning occurred in the WX86 subsystem.
#
ERROR_WX86_WARNING = 539

#
# MessageId: ERROR_WX86_ERROR
#
# MessageText:
#
# An error occurred in the WX86 subsystem.
#
ERROR_WX86_ERROR = 540

#
# MessageId: ERROR_TIMER_NOT_CANCELED
#
# MessageText:
#
# An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.
#
ERROR_TIMER_NOT_CANCELED = 541

#
# MessageId: ERROR_UNWIND
#
# MessageText:
#
# Unwind exception code.
#
ERROR_UNWIND = 542

#
# MessageId: ERROR_BAD_STACK
#
# MessageText:
#
# An invalid or unaligned stack was encountered during an unwind operation.
#
ERROR_BAD_STACK = 543

#
# MessageId: ERROR_INVALID_UNWIND_TARGET
#
# MessageText:
#
# An invalid unwind target was encountered during an unwind operation.
#
ERROR_INVALID_UNWIND_TARGET = 544

#
# MessageId: ERROR_INVALID_PORT_ATTRIBUTES
#
# MessageText:
#
# Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort
#
ERROR_INVALID_PORT_ATTRIBUTES = 545

#
# MessageId: ERROR_PORT_MESSAGE_TOO_LONG
#
# MessageText:
#
# Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.
#
ERROR_PORT_MESSAGE_TOO_LONG = 546

#
# MessageId: ERROR_INVALID_QUOTA_LOWER
#
# MessageText:
#
# An attempt was made to lower a quota limit below the current usage.
#
ERROR_INVALID_QUOTA_LOWER = 547

#
# MessageId: ERROR_DEVICE_ALREADY_ATTACHED
#
# MessageText:
#
# An attempt was made to attach to a device that was already attached to another device.
#
ERROR_DEVICE_ALREADY_ATTACHED = 548

#
# MessageId: ERROR_INSTRUCTION_MISALIGNMENT
#
# MessageText:
#
# An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.
#
ERROR_INSTRUCTION_MISALIGNMENT = 549

#
# MessageId: ERROR_PROFILING_NOT_STARTED
#
# MessageText:
#
# Profiling not started.
#
ERROR_PROFILING_NOT_STARTED = 550

#
# MessageId: ERROR_PROFILING_NOT_STOPPED
#
# MessageText:
#
# Profiling not stopped.
#
ERROR_PROFILING_NOT_STOPPED = 551

#
# MessageId: ERROR_COULD_NOT_INTERPRET
#
# MessageText:
#
# The passed ACL did not contain the minimum required information.
#
ERROR_COULD_NOT_INTERPRET = 552

#
# MessageId: ERROR_PROFILING_AT_LIMIT
#
# MessageText:
#
# The number of active profiling objects is at the maximum and no more may be started.
#
ERROR_PROFILING_AT_LIMIT = 553

#
# MessageId: ERROR_CANT_WAIT
#
# MessageText:
#
# Used to indicate that an operation cannot continue without blocking for I/O.
#
ERROR_CANT_WAIT = 554

#
# MessageId: ERROR_CANT_TERMINATE_SELF
#
# MessageText:
#
# Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.
#
ERROR_CANT_TERMINATE_SELF = 555

#
# MessageId: ERROR_UNEXPECTED_MM_CREATE_ERR
#
# MessageText:
#
# If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.
# In this case information is lost, however, the filter correctly handles the exception.
#
ERROR_UNEXPECTED_MM_CREATE_ERR = 556

#
# MessageId: ERROR_UNEXPECTED_MM_MAP_ERROR
#
# MessageText:
#
# If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.
# In this case information is lost, however, the filter correctly handles the exception.
#
ERROR_UNEXPECTED_MM_MAP_ERROR = 557

#
# MessageId: ERROR_UNEXPECTED_MM_EXTEND_ERR
#
# MessageText:
#
# If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.
# In this case information is lost, however, the filter correctly handles the exception.
#
ERROR_UNEXPECTED_MM_EXTEND_ERR = 558

#
# MessageId: ERROR_BAD_FUNCTION_TABLE
#
# MessageText:
#
# A malformed function table was encountered during an unwind operation.
#
ERROR_BAD_FUNCTION_TABLE = 559

#
# MessageId: ERROR_NO_GUID_TRANSLATION
#
# MessageText:
#
# Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system.
# This causes the protection attempt to fail, which may cause a file creation attempt to fail.
#
ERROR_NO_GUID_TRANSLATION = 560

#
# MessageId: ERROR_INVALID_LDT_SIZE
#
# MessageText:
#
# Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.
#
ERROR_INVALID_LDT_SIZE = 561

#
# MessageId: ERROR_INVALID_LDT_OFFSET
#
# MessageText:
#
# Indicates that the starting value for the LDT information was not an integral multiple of the selector size.
#
ERROR_INVALID_LDT_OFFSET = 563

#
# MessageId: ERROR_INVALID_LDT_DESCRIPTOR
#
# MessageText:
#
# Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.
#
ERROR_INVALID_LDT_DESCRIPTOR = 564

#
# MessageId: ERROR_TOO_MANY_THREADS
#
# MessageText:
#
# Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.
#
ERROR_TOO_MANY_THREADS = 565

#
# MessageId: ERROR_THREAD_NOT_IN_PROCESS
#
# MessageText:
#
# An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.
#
ERROR_THREAD_NOT_IN_PROCESS = 566

#
# MessageId: ERROR_PAGEFILE_QUOTA_EXCEEDED
#
# MessageText:
#
# Page file quota was exceeded.
#
ERROR_PAGEFILE_QUOTA_EXCEEDED = 567

#
# MessageId: ERROR_LOGON_SERVER_CONFLICT
#
# MessageText:
#
# The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.
#
ERROR_LOGON_SERVER_CONFLICT = 568

#
# MessageId: ERROR_SYNCHRONIZATION_REQUIRED
#
# MessageText:
#
# The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.
#
ERROR_SYNCHRONIZATION_REQUIRED = 569

#
# MessageId: ERROR_NET_OPEN_FAILED
#
# MessageText:
#
# The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.
#
ERROR_NET_OPEN_FAILED = 570

#
# MessageId: ERROR_IO_PRIVILEGE_FAILED
#
# MessageText:
#
# {Privilege Failed}
# The I/O permissions for the process could not be changed.
#
ERROR_IO_PRIVILEGE_FAILED = 571

#
# MessageId: ERROR_CONTROL_C_EXIT
#
# MessageText:
#
# {Application Exit by CTRL+C}
# The application terminated as a result of a CTRL+C.
#
ERROR_CONTROL_C_EXIT = 572

#
# MessageId: ERROR_MISSING_SYSTEMFILE
#
# MessageText:
#
# {Missing System File}
# The required system file %hs is bad or missing.
#
ERROR_MISSING_SYSTEMFILE = 573

#
# MessageId: ERROR_UNHANDLED_EXCEPTION
#
# MessageText:
#
# {Application Error}
# The exception %s (0x%08lx) occurred in the application at location 0x%08lx.
#
ERROR_UNHANDLED_EXCEPTION = 574

#
# MessageId: ERROR_APP_INIT_FAILURE
#
# MessageText:
#
# {Application Error}
# The application was unable to start correctly (0x%lx). Click OK to close the application.
#
ERROR_APP_INIT_FAILURE = 575

#
# MessageId: ERROR_PAGEFILE_CREATE_FAILED
#
# MessageText:
#
# {Unable to Create Paging File}
# The creation of the paging file %hs failed (%lx). The requested size was %ld.
#
ERROR_PAGEFILE_CREATE_FAILED = 576

#
# MessageId: ERROR_INVALID_IMAGE_HASH
#
# MessageText:
#
# Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.
#
ERROR_INVALID_IMAGE_HASH = 577

#
# MessageId: ERROR_NO_PAGEFILE
#
# MessageText:
#
# {No Paging File Specified}
# No paging file was specified in the system configuration.
#
ERROR_NO_PAGEFILE = 578

#
# MessageId: ERROR_ILLEGAL_FLOAT_CONTEXT
#
# MessageText:
#
# {EXCEPTION}
# A real-mode application issued a floating-point instruction and floating-point hardware is not present.
#
ERROR_ILLEGAL_FLOAT_CONTEXT = 579

#
# MessageId: ERROR_NO_EVENT_PAIR
#
# MessageText:
#
# An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.
#
ERROR_NO_EVENT_PAIR = 580

#
# MessageId: ERROR_DOMAIN_CTRLR_CONFIG_ERROR
#
# MessageText:
#
# A Windows Server has an incorrect configuration.
#
ERROR_DOMAIN_CTRLR_CONFIG_ERROR = 581

#
# MessageId: ERROR_ILLEGAL_CHARACTER
#
# MessageText:
#
# An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.
#
ERROR_ILLEGAL_CHARACTER = 582

#
# MessageId: ERROR_UNDEFINED_CHARACTER
#
# MessageText:
#
# The Unicode character is not defined in the Unicode character set installed on the system.
#
ERROR_UNDEFINED_CHARACTER = 583

#
# MessageId: ERROR_FLOPPY_VOLUME
#
# MessageText:
#
# The paging file cannot be created on a floppy diskette.
#
ERROR_FLOPPY_VOLUME = 584

#
# MessageId: ERROR_BIOS_FAILED_TO_CONNECT_INTERRUPT
#
# MessageText:
#
# The system BIOS failed to connect a system interrupt to the device or bus for which the device is connected.
#
ERROR_BIOS_FAILED_TO_CONNECT_INTERRUPT = 585

#
# MessageId: ERROR_BACKUP_CONTROLLER
#
# MessageText:
#
# This operation is only allowed for the Primary Domain Controller of the domain.
#
ERROR_BACKUP_CONTROLLER = 586

#
# MessageId: ERROR_MUTANT_LIMIT_EXCEEDED
#
# MessageText:
#
# An attempt was made to acquire a mutant such that its maximum count would have been exceeded.
#
ERROR_MUTANT_LIMIT_EXCEEDED = 587

#
# MessageId: ERROR_FS_DRIVER_REQUIRED
#
# MessageText:
#
# A volume has been accessed for which a file system driver is required that has not yet been loaded.
#
ERROR_FS_DRIVER_REQUIRED = 588

#
# MessageId: ERROR_CANNOT_LOAD_REGISTRY_FILE
#
# MessageText:
#
# {Registry File Failure}
# The registry cannot load the hive (file):
# %hs
# or its log or alternate.
# It is corrupt, absent, or not writable.
#
ERROR_CANNOT_LOAD_REGISTRY_FILE = 589

#
# MessageId: ERROR_DEBUG_ATTACH_FAILED
#
# MessageText:
#
# {Unexpected Failure in DebugActiveProcess}
# An unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.
#
ERROR_DEBUG_ATTACH_FAILED = 590

#
# MessageId: ERROR_SYSTEM_PROCESS_TERMINATED
#
# MessageText:
#
# {Fatal System Error}
# The %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x).
# The system has been shut down.
#
ERROR_SYSTEM_PROCESS_TERMINATED = 591

#
# MessageId: ERROR_DATA_NOT_ACCEPTED
#
# MessageText:
#
# {Data Not Accepted}
# The TDI client could not handle the data received during an indication.
#
ERROR_DATA_NOT_ACCEPTED = 592

#
# MessageId: ERROR_VDM_HARD_ERROR
#
# MessageText:
#
# NTVDM encountered a hard error.
#
ERROR_VDM_HARD_ERROR = 593

#
# MessageId: ERROR_DRIVER_CANCEL_TIMEOUT
#
# MessageText:
#
# {Cancel Timeout}
# The driver %hs failed to complete a cancelled I/O request in the allotted time.
#
ERROR_DRIVER_CANCEL_TIMEOUT = 594

#
# MessageId: ERROR_REPLY_MESSAGE_MISMATCH
#
# MessageText:
#
# {Reply Message Mismatch}
# An attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.
#
ERROR_REPLY_MESSAGE_MISMATCH = 595

#
# MessageId: ERROR_LOST_WRITEBEHIND_DATA
#
# MessageText:
#
# {Delayed Write Failed}
# Windows was unable to save all the data for the file %hs. The data has been lost.
# This error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.
#
ERROR_LOST_WRITEBEHIND_DATA = 596

#
# MessageId: ERROR_CLIENT_SERVER_PARAMETERS_INVALID
#
# MessageText:
#
# The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.
#
ERROR_CLIENT_SERVER_PARAMETERS_INVALID = 597

#
# MessageId: ERROR_NOT_TINY_STREAM
#
# MessageText:
#
# The stream is not a tiny stream.
#
ERROR_NOT_TINY_STREAM = 598

#
# MessageId: ERROR_STACK_OVERFLOW_READ
#
# MessageText:
#
# The request must be handled by the stack overflow code.
#
ERROR_STACK_OVERFLOW_READ = 599

#
# MessageId: ERROR_CONVERT_TO_LARGE
#
# MessageText:
#
# Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.
#
ERROR_CONVERT_TO_LARGE = 600

#
# MessageId: ERROR_FOUND_OUT_OF_SCOPE
#
# MessageText:
#
# The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.
#
ERROR_FOUND_OUT_OF_SCOPE = 601

#
# MessageId: ERROR_ALLOCATE_BUCKET
#
# MessageText:
#
# The bucket array must be grown. Retry transaction after doing so.
#
ERROR_ALLOCATE_BUCKET = 602

#
# MessageId: ERROR_MARSHALL_OVERFLOW
#
# MessageText:
#
# The user/kernel marshalling buffer has overflowed.
#
ERROR_MARSHALL_OVERFLOW = 603

#
# MessageId: ERROR_INVALID_VARIANT
#
# MessageText:
#
# The supplied variant structure contains invalid data.
#
ERROR_INVALID_VARIANT = 604

#
# MessageId: ERROR_BAD_COMPRESSION_BUFFER
#
# MessageText:
#
# The specified buffer contains ill-formed data.
#
ERROR_BAD_COMPRESSION_BUFFER = 605

#
# MessageId: ERROR_AUDIT_FAILED
#
# MessageText:
#
# {Audit Failed}
# An attempt to generate a security audit failed.
#
ERROR_AUDIT_FAILED = 606

#
# MessageId: ERROR_TIMER_RESOLUTION_NOT_SET
#
# MessageText:
#
# The timer resolution was not previously set by the current process.
#
ERROR_TIMER_RESOLUTION_NOT_SET = 607

#
# MessageId: ERROR_INSUFFICIENT_LOGON_INFO
#
# MessageText:
#
# There is insufficient account information to log you on.
#
ERROR_INSUFFICIENT_LOGON_INFO = 608

#
# MessageId: ERROR_BAD_DLL_ENTRYPOINT
#
# MessageText:
#
# {Invalid DLL Entrypoint}
# The dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state.
# The entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.
#
ERROR_BAD_DLL_ENTRYPOINT = 609

#
# MessageId: ERROR_BAD_SERVICE_ENTRYPOINT
#
# MessageText:
#
# {Invalid Service Callback Entrypoint}
# The %hs service is not written correctly. The stack pointer has been left in an inconsistent state.
# The callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.
#
ERROR_BAD_SERVICE_ENTRYPOINT = 610

#
# MessageId: ERROR_IP_ADDRESS_CONFLICT1
#
# MessageText:
#
# There is an IP address conflict with another system on the network
#
ERROR_IP_ADDRESS_CONFLICT1 = 611

#
# MessageId: ERROR_IP_ADDRESS_CONFLICT2
#
# MessageText:
#
# There is an IP address conflict with another system on the network
#
ERROR_IP_ADDRESS_CONFLICT2 = 612

#
# MessageId: ERROR_REGISTRY_QUOTA_LIMIT
#
# MessageText:
#
# {Low On Registry Space}
# The system has reached the maximum size allowed for the system part of the registry. Additional storage requests will be ignored.
#
ERROR_REGISTRY_QUOTA_LIMIT = 613

#
# MessageId: ERROR_NO_CALLBACK_ACTIVE
#
# MessageText:
#
# A callback return system service cannot be executed when no callback is active.
#
ERROR_NO_CALLBACK_ACTIVE = 614

#
# MessageId: ERROR_PWD_TOO_SHORT
#
# MessageText:
#
# The password provided is too short to meet the policy of your user account.
# Please choose a longer password.
#
ERROR_PWD_TOO_SHORT = 615

#
# MessageId: ERROR_PWD_TOO_RECENT
#
# MessageText:
#
# The policy of your user account does not allow you to change passwords too frequently.
# This is done to prevent users from changing back to a familiar, but potentially discovered, password.
# If you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.
#
ERROR_PWD_TOO_RECENT = 616

#
# MessageId: ERROR_PWD_HISTORY_CONFLICT
#
# MessageText:
#
# You have attempted to change your password to one that you have used in the past.
# The policy of your user account does not allow this. Please select a password that you have not previously used.
#
ERROR_PWD_HISTORY_CONFLICT = 617

#
# MessageId: ERROR_UNSUPPORTED_COMPRESSION
#
# MessageText:
#
# The specified compression format is unsupported.
#
ERROR_UNSUPPORTED_COMPRESSION = 618

#
# MessageId: ERROR_INVALID_HW_PROFILE
#
# MessageText:
#
# The specified hardware profile configuration is invalid.
#
ERROR_INVALID_HW_PROFILE = 619

#
# MessageId: ERROR_INVALID_PLUGPLAY_DEVICE_PATH
#
# MessageText:
#
# The specified Plug and Play registry device path is invalid.
#
ERROR_INVALID_PLUGPLAY_DEVICE_PATH = 620

#
# MessageId: ERROR_QUOTA_LIST_INCONSISTENT
#
# MessageText:
#
# The specified quota list is internally inconsistent with its descriptor.
#
ERROR_QUOTA_LIST_INCONSISTENT = 621

#
# MessageId: ERROR_EVALUATION_EXPIRATION
#
# MessageText:
#
# {Windows Evaluation Notification}
# The evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.
#
ERROR_EVALUATION_EXPIRATION = 622

#
# MessageId: ERROR_ILLEGAL_DLL_RELOCATION
#
# MessageText:
#
# {Illegal System DLL Relocation}
# The system DLL %hs was relocated in memory. The application will not run properly.
# The relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.
#
ERROR_ILLEGAL_DLL_RELOCATION = 623

#
# MessageId: ERROR_DLL_INIT_FAILED_LOGOFF
#
# MessageText:
#
# {DLL Initialization Failed}
# The application failed to initialize because the window station is shutting down.
#
ERROR_DLL_INIT_FAILED_LOGOFF = 624

#
# MessageId: ERROR_VALIDATE_CONTINUE
#
# MessageText:
#
# The validation process needs to continue on to the next step.
#
ERROR_VALIDATE_CONTINUE = 625

#
# MessageId: ERROR_NO_MORE_MATCHES
#
# MessageText:
#
# There are no more matches for the current index enumeration.
#
ERROR_NO_MORE_MATCHES = 626

#
# MessageId: ERROR_RANGE_LIST_CONFLICT
#
# MessageText:
#
# The range could not be added to the range list because of a conflict.
#
ERROR_RANGE_LIST_CONFLICT = 627

#
# MessageId: ERROR_SERVER_SID_MISMATCH
#
# MessageText:
#
# The server process is running under a SID different than that required by client.
#
ERROR_SERVER_SID_MISMATCH = 628

#
# MessageId: ERROR_CANT_ENABLE_DENY_ONLY
#
# MessageText:
#
# A group marked use for deny only cannot be enabled.
#
ERROR_CANT_ENABLE_DENY_ONLY = 629

#
# MessageId: ERROR_FLOAT_MULTIPLE_FAULTS
#
# MessageText:
#
# {EXCEPTION}
# Multiple floating point faults.
#
ERROR_FLOAT_MULTIPLE_FAULTS = 630

#
# MessageId: ERROR_FLOAT_MULTIPLE_TRAPS
#
# MessageText:
#
# {EXCEPTION}
# Multiple floating point traps.
#
ERROR_FLOAT_MULTIPLE_TRAPS = 631

#
# MessageId: ERROR_NOINTERFACE
#
# MessageText:
#
# The requested interface is not supported.
#
ERROR_NOINTERFACE = 632

#
# MessageId: ERROR_DRIVER_FAILED_SLEEP
#
# MessageText:
#
# {System Standby Failed}
# The driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.
#
ERROR_DRIVER_FAILED_SLEEP = 633

#
# MessageId: ERROR_CORRUPT_SYSTEM_FILE
#
# MessageText:
#
# The system file %1 has become corrupt and has been replaced.
#
ERROR_CORRUPT_SYSTEM_FILE = 634

#
# MessageId: ERROR_COMMITMENT_MINIMUM
#
# MessageText:
#
# {Virtual Memory Minimum Too Low}
# Your system is low on virtual memory. Windows is increasing the size of your virtual memory paging file.
# During this process, memory requests for some applications may be denied. For more information, see Help.
#
ERROR_COMMITMENT_MINIMUM = 635

#
# MessageId: ERROR_PNP_RESTART_ENUMERATION
#
# MessageText:
#
# A device was removed so enumeration must be restarted.
#
ERROR_PNP_RESTART_ENUMERATION = 636

#
# MessageId: ERROR_SYSTEM_IMAGE_BAD_SIGNATURE
#
# MessageText:
#
# {Fatal System Error}
# The system image %s is not properly signed.
# The file has been replaced with the signed file.
# The system has been shut down.
#
ERROR_SYSTEM_IMAGE_BAD_SIGNATURE = 637

#
# MessageId: ERROR_PNP_REBOOT_REQUIRED
#
# MessageText:
#
# Device will not start without a reboot.
#
ERROR_PNP_REBOOT_REQUIRED = 638

#
# MessageId: ERROR_INSUFFICIENT_POWER
#
# MessageText:
#
# There is not enough power to complete the requested operation.
#
ERROR_INSUFFICIENT_POWER = 639

#
# MessageId: ERROR_MULTIPLE_FAULT_VIOLATION
#
# MessageText:
#
#  ERROR_MULTIPLE_FAULT_VIOLATION
#
ERROR_MULTIPLE_FAULT_VIOLATION = 640

#
# MessageId: ERROR_SYSTEM_SHUTDOWN
#
# MessageText:
#
# The system is in the process of shutting down.
#
ERROR_SYSTEM_SHUTDOWN = 641

#
# MessageId: ERROR_PORT_NOT_SET
#
# MessageText:
#
# An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.
#
ERROR_PORT_NOT_SET = 642

#
# MessageId: ERROR_DS_VERSION_CHECK_FAILURE
#
# MessageText:
#
# This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.
#
ERROR_DS_VERSION_CHECK_FAILURE = 643

#
# MessageId: ERROR_RANGE_NOT_FOUND
#
# MessageText:
#
# The specified range could not be found in the range list.
#
ERROR_RANGE_NOT_FOUND = 644

#
# MessageId: ERROR_NOT_SAFE_MODE_DRIVER
#
# MessageText:
#
# The driver was not loaded because the system is booting into safe mode.
#
ERROR_NOT_SAFE_MODE_DRIVER = 646

#
# MessageId: ERROR_FAILED_DRIVER_ENTRY
#
# MessageText:
#
# The driver was not loaded because it failed its initialization call.
#
ERROR_FAILED_DRIVER_ENTRY = 647

#
# MessageId: ERROR_DEVICE_ENUMERATION_ERROR
#
# MessageText:
#
# The "%hs" encountered an error while applying power or reading the device configuration.
# This may be caused by a failure of your hardware or by a poor connection.
#
ERROR_DEVICE_ENUMERATION_ERROR = 648

#
# MessageId: ERROR_MOUNT_POINT_NOT_RESOLVED
#
# MessageText:
#
# The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.
#
ERROR_MOUNT_POINT_NOT_RESOLVED = 649

#
# MessageId: ERROR_INVALID_DEVICE_OBJECT_PARAMETER
#
# MessageText:
#
# The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.
#
ERROR_INVALID_DEVICE_OBJECT_PARAMETER = 650

#
# MessageId: ERROR_MCA_OCCURED
#
# MessageText:
#
# A Machine Check Error has occurred. Please check the system eventlog for additional information.
#
ERROR_MCA_OCCURED = 651

#
# MessageId: ERROR_DRIVER_DATABASE_ERROR
#
# MessageText:
#
# There was error [%2] processing the driver database.
#
ERROR_DRIVER_DATABASE_ERROR = 652

#
# MessageId: ERROR_SYSTEM_HIVE_TOO_LARGE
#
# MessageText:
#
# System hive size has exceeded its limit.
#
ERROR_SYSTEM_HIVE_TOO_LARGE = 653

#
# MessageId: ERROR_DRIVER_FAILED_PRIOR_UNLOAD
#
# MessageText:
#
# The driver could not be loaded because a previous version of the driver is still in memory.
#
ERROR_DRIVER_FAILED_PRIOR_UNLOAD = 654

#
# MessageId: ERROR_VOLSNAP_PREPARE_HIBERNATE
#
# MessageText:
#
# {Volume Shadow Copy Service}
# Please wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.
#
ERROR_VOLSNAP_PREPARE_HIBERNATE = 655

#
# MessageId: ERROR_HIBERNATION_FAILURE
#
# MessageText:
#
# The system has failed to hibernate (The error code is %hs). Hibernation will be disabled until the system is restarted.
#
ERROR_HIBERNATION_FAILURE = 656

#
# MessageId: ERROR_PWD_TOO_LONG
#
# MessageText:
#
# The password provided is too long to meet the policy of your user account.
# Please choose a shorter password.
#
ERROR_PWD_TOO_LONG = 657

#
# MessageId: ERROR_FILE_SYSTEM_LIMITATION
#
# MessageText:
#
# The requested operation could not be completed due to a file system limitation
#
ERROR_FILE_SYSTEM_LIMITATION = 665

#
# MessageId: ERROR_ASSERTION_FAILURE
#
# MessageText:
#
# An assertion failure has occurred.
#
ERROR_ASSERTION_FAILURE = 668

#
# MessageId: ERROR_ACPI_ERROR
#
# MessageText:
#
# An error occurred in the ACPI subsystem.
#
ERROR_ACPI_ERROR = 669

#
# MessageId: ERROR_WOW_ASSERTION
#
# MessageText:
#
# WOW Assertion Error.
#
ERROR_WOW_ASSERTION = 670

#
# MessageId: ERROR_PNP_BAD_MPS_TABLE
#
# MessageText:
#
# A device is missing in the system BIOS MPS table. This device will not be used.
# Please contact your system vendor for system BIOS update.
#
ERROR_PNP_BAD_MPS_TABLE = 671

#
# MessageId: ERROR_PNP_TRANSLATION_FAILED
#
# MessageText:
#
# A translator failed to translate resources.
#
ERROR_PNP_TRANSLATION_FAILED = 672

#
# MessageId: ERROR_PNP_IRQ_TRANSLATION_FAILED
#
# MessageText:
#
# A IRQ translator failed to translate resources.
#
ERROR_PNP_IRQ_TRANSLATION_FAILED = 673

#
# MessageId: ERROR_PNP_INVALID_ID
#
# MessageText:
#
# Driver %2 returned invalid ID for a child device (%3).
#
ERROR_PNP_INVALID_ID = 674

#
# MessageId: ERROR_WAKE_SYSTEM_DEBUGGER
#
# MessageText:
#
# {Kernel Debugger Awakened}
# the system debugger was awakened by an interrupt.
#
ERROR_WAKE_SYSTEM_DEBUGGER = 675

#
# MessageId: ERROR_HANDLES_CLOSED
#
# MessageText:
#
# {Handles Closed}
# Handles to objects have been automatically closed as a result of the requested operation.
#
ERROR_HANDLES_CLOSED = 676

#
# MessageId: ERROR_EXTRANEOUS_INFORMATION
#
# MessageText:
#
# {Too Much Information}
# The specified access control list (ACL) contained more information than was expected.
#
ERROR_EXTRANEOUS_INFORMATION = 677

#
# MessageId: ERROR_RXACT_COMMIT_NECESSARY
#
# MessageText:
#
# This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.
# The commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).
#
ERROR_RXACT_COMMIT_NECESSARY = 678

#
# MessageId: ERROR_MEDIA_CHECK
#
# MessageText:
#
# {Media Changed}
# The media may have changed.
#
ERROR_MEDIA_CHECK = 679

#
# MessageId: ERROR_GUID_SUBSTITUTION_MADE
#
# MessageText:
#
# {GUID Substitution}
# During the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found.
# A substitute prefix was used, which will not compromise system security. However, this may provide a more restrictive access than intended.
#
ERROR_GUID_SUBSTITUTION_MADE = 680

#
# MessageId: ERROR_STOPPED_ON_SYMLINK
#
# MessageText:
#
# The create operation stopped after reaching a symbolic link
#
ERROR_STOPPED_ON_SYMLINK = 681

#
# MessageId: ERROR_LONGJUMP
#
# MessageText:
#
# A long jump has been executed.
#
ERROR_LONGJUMP = 682

#
# MessageId: ERROR_PLUGPLAY_QUERY_VETOED
#
# MessageText:
#
# The Plug and Play query operation was not successful.
#
ERROR_PLUGPLAY_QUERY_VETOED = 683

#
# MessageId: ERROR_UNWIND_CONSOLIDATE
#
# MessageText:
#
# A frame consolidation has been executed.
#
ERROR_UNWIND_CONSOLIDATE = 684

#
# MessageId: ERROR_REGISTRY_HIVE_RECOVERED
#
# MessageText:
#
# {Registry Hive Recovered}
# Registry hive (file):
# %hs
# was corrupted and it has been recovered. Some data might have been lost.
#
ERROR_REGISTRY_HIVE_RECOVERED = 685

#
# MessageId: ERROR_DLL_MIGHT_BE_INSECURE
#
# MessageText:
#
# The application is attempting to run executable code from the module %hs. This may be insecure. An alternative, %hs, is available. Should the application use the secure module %hs?
#
ERROR_DLL_MIGHT_BE_INSECURE = 686

#
# MessageId: ERROR_DLL_MIGHT_BE_INCOMPATIBLE
#
# MessageText:
#
# The application is loading executable code from the module %hs. This is secure, but may be incompatible with previous releases of the operating system. An alternative, %hs, is available. Should the application use the secure module %hs?
#
ERROR_DLL_MIGHT_BE_INCOMPATIBLE = 687

#
# MessageId: ERROR_DBG_EXCEPTION_NOT_HANDLED
#
# MessageText:
#
# Debugger did not handle the exception.
#
ERROR_DBG_EXCEPTION_NOT_HANDLED = 688

#
# MessageId: ERROR_DBG_REPLY_LATER
#
# MessageText:
#
# Debugger will reply later.
#
ERROR_DBG_REPLY_LATER = 689

#
# MessageId: ERROR_DBG_UNABLE_TO_PROVIDE_HANDLE
#
# MessageText:
#
# Debugger cannot provide handle.
#
ERROR_DBG_UNABLE_TO_PROVIDE_HANDLE = 690

#
# MessageId: ERROR_DBG_TERMINATE_THREAD
#
# MessageText:
#
# Debugger terminated thread.
#
ERROR_DBG_TERMINATE_THREAD = 691

#
# MessageId: ERROR_DBG_TERMINATE_PROCESS
#
# MessageText:
#
# Debugger terminated process.
#
ERROR_DBG_TERMINATE_PROCESS = 692

#
# MessageId: ERROR_DBG_CONTROL_C
#
# MessageText:
#
# Debugger got control C.
#
ERROR_DBG_CONTROL_C = 693

#
# MessageId: ERROR_DBG_PRINTEXCEPTION_C
#
# MessageText:
#
# Debugger printed exception on control C.
#
ERROR_DBG_PRINTEXCEPTION_C = 694

#
# MessageId: ERROR_DBG_RIPEXCEPTION
#
# MessageText:
#
# Debugger received RIP exception.
#
ERROR_DBG_RIPEXCEPTION = 695

#
# MessageId: ERROR_DBG_CONTROL_BREAK
#
# MessageText:
#
# Debugger received control break.
#
ERROR_DBG_CONTROL_BREAK = 696

#
# MessageId: ERROR_DBG_COMMAND_EXCEPTION
#
# MessageText:
#
# Debugger command communication exception.
#
ERROR_DBG_COMMAND_EXCEPTION = 697

#
# MessageId: ERROR_OBJECT_NAME_EXISTS
#
# MessageText:
#
# {Object Exists}
# An attempt was made to create an object and the object name already existed.
#
ERROR_OBJECT_NAME_EXISTS = 698

#
# MessageId: ERROR_THREAD_WAS_SUSPENDED
#
# MessageText:
#
# {Thread Suspended}
# A thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.
#
ERROR_THREAD_WAS_SUSPENDED = 699

#
# MessageId: ERROR_IMAGE_NOT_AT_BASE
#
# MessageText:
#
# {Image Relocated}
# An image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.
#
ERROR_IMAGE_NOT_AT_BASE = 700

#
# MessageId: ERROR_RXACT_STATE_CREATED
#
# MessageText:
#
# This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.
#
ERROR_RXACT_STATE_CREATED = 701

#
# MessageId: ERROR_SEGMENT_NOTIFICATION
#
# MessageText:
#
# {Segment Load}
# A virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image.
# An exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.
#
ERROR_SEGMENT_NOTIFICATION = 702

#
# MessageId: ERROR_BAD_CURRENT_DIRECTORY
#
# MessageText:
#
# {Invalid Current Directory}
# The process cannot switch to the startup current directory %hs.
# Select OK to set current directory to %hs, or select CANCEL to exit.
#
ERROR_BAD_CURRENT_DIRECTORY = 703

#
# MessageId: ERROR_FT_READ_RECOVERY_FROM_BACKUP
#
# MessageText:
#
# {Redundant Read}
# To satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy.
# This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.
#
ERROR_FT_READ_RECOVERY_FROM_BACKUP = 704

#
# MessageId: ERROR_FT_WRITE_RECOVERY
#
# MessageText:
#
# {Redundant Write}
# To satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information.
# This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.
#
ERROR_FT_WRITE_RECOVERY = 705

#
# MessageId: ERROR_IMAGE_MACHINE_TYPE_MISMATCH
#
# MessageText:
#
# {Machine Type Mismatch}
# The image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.
#
ERROR_IMAGE_MACHINE_TYPE_MISMATCH = 706

#
# MessageId: ERROR_RECEIVE_PARTIAL
#
# MessageText:
#
# {Partial Data Received}
# The network transport returned partial data to its client. The remaining data will be sent later.
#
ERROR_RECEIVE_PARTIAL = 707

#
# MessageId: ERROR_RECEIVE_EXPEDITED
#
# MessageText:
#
# {Expedited Data Received}
# The network transport returned data to its client that was marked as expedited by the remote system.
#
ERROR_RECEIVE_EXPEDITED = 708

#
# MessageId: ERROR_RECEIVE_PARTIAL_EXPEDITED
#
# MessageText:
#
# {Partial Expedited Data Received}
# The network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.
#
ERROR_RECEIVE_PARTIAL_EXPEDITED = 709

#
# MessageId: ERROR_EVENT_DONE
#
# MessageText:
#
# {TDI Event Done}
# The TDI indication has completed successfully.
#
ERROR_EVENT_DONE = 710

#
# MessageId: ERROR_EVENT_PENDING
#
# MessageText:
#
# {TDI Event Pending}
# The TDI indication has entered the pending state.
#
ERROR_EVENT_PENDING = 711

#
# MessageId: ERROR_CHECKING_FILE_SYSTEM
#
# MessageText:
#
# Checking file system on %wZ
#
ERROR_CHECKING_FILE_SYSTEM = 712

#
# MessageId: ERROR_FATAL_APP_EXIT
#
# MessageText:
#
# {Fatal Application Exit}
# %hs
#
ERROR_FATAL_APP_EXIT = 713

#
# MessageId: ERROR_PREDEFINED_HANDLE
#
# MessageText:
#
# The specified registry key is referenced by a predefined handle.
#
ERROR_PREDEFINED_HANDLE = 714

#
# MessageId: ERROR_WAS_UNLOCKED
#
# MessageText:
#
# {Page Unlocked}
# The page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.
#
ERROR_WAS_UNLOCKED = 715

#
# MessageId: ERROR_SERVICE_NOTIFICATION
#
# MessageText:
#
# %hs
#
ERROR_SERVICE_NOTIFICATION = 716

#
# MessageId: ERROR_WAS_LOCKED
#
# MessageText:
#
# {Page Locked}
# One of the pages to lock was already locked.
#
ERROR_WAS_LOCKED = 717

#
# MessageId: ERROR_LOG_HARD_ERROR
#
# MessageText:
#
# Application popup: %1 : %2
#
ERROR_LOG_HARD_ERROR = 718

#
# MessageId: ERROR_ALREADY_WIN32
#
# MessageText:
#
#  ERROR_ALREADY_WIN32
#
ERROR_ALREADY_WIN32 = 719

#
# MessageId: ERROR_IMAGE_MACHINE_TYPE_MISMATCH_EXE
#
# MessageText:
#
# {Machine Type Mismatch}
# The image file %hs is valid, but is for a machine type other than the current machine.
#
ERROR_IMAGE_MACHINE_TYPE_MISMATCH_EXE = 720

#
# MessageId: ERROR_NO_YIELD_PERFORMED
#
# MessageText:
#
# A yield execution was performed and no thread was available to run.
#
ERROR_NO_YIELD_PERFORMED = 721

#
# MessageId: ERROR_TIMER_RESUME_IGNORED
#
# MessageText:
#
# The resumable flag to a timer API was ignored.
#
ERROR_TIMER_RESUME_IGNORED = 722

#
# MessageId: ERROR_ARBITRATION_UNHANDLED
#
# MessageText:
#
# The arbiter has deferred arbitration of these resources to its parent
#
ERROR_ARBITRATION_UNHANDLED = 723

#
# MessageId: ERROR_CARDBUS_NOT_SUPPORTED
#
# MessageText:
#
# The inserted CardBus device cannot be started because of a configuration error on "%hs".
#
ERROR_CARDBUS_NOT_SUPPORTED = 724

#
# MessageId: ERROR_MP_PROCESSOR_MISMATCH
#
# MessageText:
#
# The CPUs in this multiprocessor system are not all the same revision level. To use all processors the operating system restricts itself to the features of the least capable processor in the system. Should problems occur with this system, contact the CPU manufacturer to see if this mix of processors is supported.
#
ERROR_MP_PROCESSOR_MISMATCH = 725

#
# MessageId: ERROR_HIBERNATED
#
# MessageText:
#
# The system was put into hibernation.
#
ERROR_HIBERNATED = 726

#
# MessageId: ERROR_RESUME_HIBERNATION
#
# MessageText:
#
# The system was resumed from hibernation.
#
ERROR_RESUME_HIBERNATION = 727

#
# MessageId: ERROR_FIRMWARE_UPDATED
#
# MessageText:
#
# Windows has detected that the system firmware (BIOS) was updated [previous firmware date = %2, current firmware date %3].
#
ERROR_FIRMWARE_UPDATED = 728

#
# MessageId: ERROR_DRIVERS_LEAKING_LOCKED_PAGES
#
# MessageText:
#
# A device driver is leaking locked I/O pages causing system degradation. The system has automatically enabled tracking code in order to try and catch the culprit.
#
ERROR_DRIVERS_LEAKING_LOCKED_PAGES = 729

#
# MessageId: ERROR_WAKE_SYSTEM
#
# MessageText:
#
# The system has awoken
#
ERROR_WAKE_SYSTEM = 730

#
# MessageId: ERROR_WAIT_1
#
# MessageText:
#
#  ERROR_WAIT_1
#
ERROR_WAIT_1 = 731

#
# MessageId: ERROR_WAIT_2
#
# MessageText:
#
#  ERROR_WAIT_2
#
ERROR_WAIT_2 = 732

#
# MessageId: ERROR_WAIT_3
#
# MessageText:
#
#  ERROR_WAIT_3
#
ERROR_WAIT_3 = 733

#
# MessageId: ERROR_WAIT_63
#
# MessageText:
#
#  ERROR_WAIT_63
#
ERROR_WAIT_63 = 734

#
# MessageId: ERROR_ABANDONED_WAIT_0
#
# MessageText:
#
#  ERROR_ABANDONED_WAIT_0
#
ERROR_ABANDONED_WAIT_0 = 735

#
# MessageId: ERROR_ABANDONED_WAIT_63
#
# MessageText:
#
#  ERROR_ABANDONED_WAIT_63
#
ERROR_ABANDONED_WAIT_63 = 736

#
# MessageId: ERROR_USER_APC
#
# MessageText:
#
#  ERROR_USER_APC
#
ERROR_USER_APC = 737

#
# MessageId: ERROR_KERNEL_APC
#
# MessageText:
#
#  ERROR_KERNEL_APC
#
ERROR_KERNEL_APC = 738

#
# MessageId: ERROR_ALERTED
#
# MessageText:
#
#  ERROR_ALERTED
#
ERROR_ALERTED = 739

#
# MessageId: ERROR_ELEVATION_REQUIRED
#
# MessageText:
#
# The requested operation requires elevation.
#
ERROR_ELEVATION_REQUIRED = 740

#
# MessageId: ERROR_REPARSE
#
# MessageText:
#
# A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.
#
ERROR_REPARSE = 741

#
# MessageId: ERROR_OPLOCK_BREAK_IN_PROGRESS
#
# MessageText:
#
# An open/create operation completed while an oplock break is underway.
#
ERROR_OPLOCK_BREAK_IN_PROGRESS = 742

#
# MessageId: ERROR_VOLUME_MOUNTED
#
# MessageText:
#
# A new volume has been mounted by a file system.
#
ERROR_VOLUME_MOUNTED = 743

#
# MessageId: ERROR_RXACT_COMMITTED
#
# MessageText:
#
# This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.
# The commit has now been completed.
#
ERROR_RXACT_COMMITTED = 744

#
# MessageId: ERROR_NOTIFY_CLEANUP
#
# MessageText:
#
# This indicates that a notify change request has been completed due to closing the handle which made the notify change request.
#
ERROR_NOTIFY_CLEANUP = 745

#
# MessageId: ERROR_PRIMARY_TRANSPORT_CONNECT_FAILED
#
# MessageText:
#
# {Connect Failure on Primary Transport}
# An attempt was made to connect to the remote server %hs on the primary transport, but the connection failed.
# The computer WAS able to connect on a secondary transport.
#
ERROR_PRIMARY_TRANSPORT_CONNECT_FAILED = 746

#
# MessageId: ERROR_PAGE_FAULT_TRANSITION
#
# MessageText:
#
# Page fault was a transition fault.
#
ERROR_PAGE_FAULT_TRANSITION = 747

#
# MessageId: ERROR_PAGE_FAULT_DEMAND_ZERO
#
# MessageText:
#
# Page fault was a demand zero fault.
#
ERROR_PAGE_FAULT_DEMAND_ZERO = 748

#
# MessageId: ERROR_PAGE_FAULT_COPY_ON_WRITE
#
# MessageText:
#
# Page fault was a demand zero fault.
#
ERROR_PAGE_FAULT_COPY_ON_WRITE = 749

#
# MessageId: ERROR_PAGE_FAULT_GUARD_PAGE
#
# MessageText:
#
# Page fault was a demand zero fault.
#
ERROR_PAGE_FAULT_GUARD_PAGE = 750

#
# MessageId: ERROR_PAGE_FAULT_PAGING_FILE
#
# MessageText:
#
# Page fault was satisfied by reading from a secondary storage device.
#
ERROR_PAGE_FAULT_PAGING_FILE = 751

#
# MessageId: ERROR_CACHE_PAGE_LOCKED
#
# MessageText:
#
# Cached page was locked during operation.
#
ERROR_CACHE_PAGE_LOCKED = 752

#
# MessageId: ERROR_CRASH_DUMP
#
# MessageText:
#
# Crash dump exists in paging file.
#
ERROR_CRASH_DUMP = 753

#
# MessageId: ERROR_BUFFER_ALL_ZEROS
#
# MessageText:
#
# Specified buffer contains all zeros.
#
ERROR_BUFFER_ALL_ZEROS = 754

#
# MessageId: ERROR_REPARSE_OBJECT
#
# MessageText:
#
# A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.
#
ERROR_REPARSE_OBJECT = 755

#
# MessageId: ERROR_RESOURCE_REQUIREMENTS_CHANGED
#
# MessageText:
#
# The device has succeeded a query-stop and its resource requirements have changed.
#
ERROR_RESOURCE_REQUIREMENTS_CHANGED = 756

#
# MessageId: ERROR_TRANSLATION_COMPLETE
#
# MessageText:
#
# The translator has translated these resources into the global space and no further translations should be performed.
#
ERROR_TRANSLATION_COMPLETE = 757

#
# MessageId: ERROR_NOTHING_TO_TERMINATE
#
# MessageText:
#
# A process being terminated has no threads to terminate.
#
ERROR_NOTHING_TO_TERMINATE = 758

#
# MessageId: ERROR_PROCESS_NOT_IN_JOB
#
# MessageText:
#
# The specified process is not part of a job.
#
ERROR_PROCESS_NOT_IN_JOB = 759

#
# MessageId: ERROR_PROCESS_IN_JOB
#
# MessageText:
#
# The specified process is part of a job.
#
ERROR_PROCESS_IN_JOB = 760

#
# MessageId: ERROR_VOLSNAP_HIBERNATE_READY
#
# MessageText:
#
# {Volume Shadow Copy Service}
# The system is now ready for hibernation.
#
ERROR_VOLSNAP_HIBERNATE_READY = 761

#
# MessageId: ERROR_FSFILTER_OP_COMPLETED_SUCCESSFULLY
#
# MessageText:
#
# A file system or file system filter driver has successfully completed an FsFilter operation.
#
ERROR_FSFILTER_OP_COMPLETED_SUCCESSFULLY = 762

#
# MessageId: ERROR_INTERRUPT_VECTOR_ALREADY_CONNECTED
#
# MessageText:
#
# The specified interrupt vector was already connected.
#
ERROR_INTERRUPT_VECTOR_ALREADY_CONNECTED = 763

#
# MessageId: ERROR_INTERRUPT_STILL_CONNECTED
#
# MessageText:
#
# The specified interrupt vector is still connected.
#
ERROR_INTERRUPT_STILL_CONNECTED = 764

#
# MessageId: ERROR_WAIT_FOR_OPLOCK
#
# MessageText:
#
# An operation is blocked waiting for an oplock.
#
ERROR_WAIT_FOR_OPLOCK = 765

#
# MessageId: ERROR_DBG_EXCEPTION_HANDLED
#
# MessageText:
#
# Debugger handled exception
#
ERROR_DBG_EXCEPTION_HANDLED = 766

#
# MessageId: ERROR_DBG_CONTINUE
#
# MessageText:
#
# Debugger continued
#
ERROR_DBG_CONTINUE = 767

#
# MessageId: ERROR_CALLBACK_POP_STACK
#
# MessageText:
#
# An exception occurred in a user mode callback and the kernel callback frame should be removed.
#
ERROR_CALLBACK_POP_STACK = 768

#
# MessageId: ERROR_COMPRESSION_DISABLED
#
# MessageText:
#
# Compression is disabled for this volume.
#
ERROR_COMPRESSION_DISABLED = 769

#
# MessageId: ERROR_CANTFETCHBACKWARDS
#
# MessageText:
#
# The data provider cannot fetch backwards through a result set.
#
ERROR_CANTFETCHBACKWARDS = 770

#
# MessageId: ERROR_CANTSCROLLBACKWARDS
#
# MessageText:
#
# The data provider cannot scroll backwards through a result set.
#
ERROR_CANTSCROLLBACKWARDS = 771

#
# MessageId: ERROR_ROWSNOTRELEASED
#
# MessageText:
#
# The data provider requires that previously fetched data is released before asking for more data.
#
ERROR_ROWSNOTRELEASED = 772

#
# MessageId: ERROR_BAD_ACCESSOR_FLAGS
#
# MessageText:
#
# The data provider was not able to interpret the flags set for a column binding in an accessor.
#
ERROR_BAD_ACCESSOR_FLAGS = 773

#
# MessageId: ERROR_ERRORS_ENCOUNTERED
#
# MessageText:
#
# One or more errors occurred while processing the request.
#
ERROR_ERRORS_ENCOUNTERED = 774

#
# MessageId: ERROR_NOT_CAPABLE
#
# MessageText:
#
# The implementation is not capable of performing the request.
#
ERROR_NOT_CAPABLE = 775

#
# MessageId: ERROR_REQUEST_OUT_OF_SEQUENCE
#
# MessageText:
#
# The client of a component requested an operation which is not valid given the state of the component instance.
#
ERROR_REQUEST_OUT_OF_SEQUENCE = 776

#
# MessageId: ERROR_VERSION_PARSE_ERROR
#
# MessageText:
#
# A version number could not be parsed.
#
ERROR_VERSION_PARSE_ERROR = 777

#
# MessageId: ERROR_BADSTARTPOSITION
#
# MessageText:
#
# The iterator's start position is invalid.
#
ERROR_BADSTARTPOSITION = 778

#
# MessageId: ERROR_MEMORY_HARDWARE
#
# MessageText:
#
# The hardware has reported an uncorrectable memory error.
#
ERROR_MEMORY_HARDWARE = 779

#
# MessageId: ERROR_DISK_REPAIR_DISABLED
#
# MessageText:
#
# The attempted operation required self healing to be enabled.
#
ERROR_DISK_REPAIR_DISABLED = 780

#
# MessageId: ERROR_INSUFFICIENT_RESOURCE_FOR_SPECIFIED_SHARED_SECTION_SIZE
#
# MessageText:
#
# The Desktop heap encountered an error while allocating session memory. There is more information in the system event log.
#
ERROR_INSUFFICIENT_RESOURCE_FOR_SPECIFIED_SHARED_SECTION_SIZE = 781

#
# MessageId: ERROR_SYSTEM_POWERSTATE_TRANSITION
#
# MessageText:
#
# The system power state is transitioning from %2 to %3.
#
ERROR_SYSTEM_POWERSTATE_TRANSITION = 782

#
# MessageId: ERROR_SYSTEM_POWERSTATE_COMPLEX_TRANSITION
#
# MessageText:
#
# The system power state is transitioning from %2 to %3 but could enter %4.
#
ERROR_SYSTEM_POWERSTATE_COMPLEX_TRANSITION = 783

#
# MessageId: ERROR_MCA_EXCEPTION
#
# MessageText:
#
# A thread is getting dispatched with MCA EXCEPTION because of MCA.
#
ERROR_MCA_EXCEPTION = 784

#
# MessageId: ERROR_ACCESS_AUDIT_BY_POLICY
#
# MessageText:
#
# Access to %1 is monitored by policy rule %2.
#
ERROR_ACCESS_AUDIT_BY_POLICY = 785

#
# MessageId: ERROR_ACCESS_DISABLED_NO_SAFER_UI_BY_POLICY
#
# MessageText:
#
# Access to %1 has been restricted by your Administrator by policy rule %2.
#
ERROR_ACCESS_DISABLED_NO_SAFER_UI_BY_POLICY = 786

#
# MessageId: ERROR_ABANDON_HIBERFILE
#
# MessageText:
#
# A valid hibernation file has been invalidated and should be abandoned.
#
ERROR_ABANDON_HIBERFILE = 787

#
# MessageId: ERROR_LOST_WRITEBEHIND_DATA_NETWORK_DISCONNECTED
#
# MessageText:
#
# {Delayed Write Failed}
# Windows was unable to save all the data for the file %hs; the data has been lost.
# This error may be caused by network connectivity issues. Please try to save this file elsewhere.
#
ERROR_LOST_WRITEBEHIND_DATA_NETWORK_DISCONNECTED = 788

#
# MessageId: ERROR_LOST_WRITEBEHIND_DATA_NETWORK_SERVER_ERROR
#
# MessageText:
#
# {Delayed Write Failed}
# Windows was unable to save all the data for the file %hs; the data has been lost.
# This error was returned by the server on which the file exists. Please try to save this file elsewhere.
#
ERROR_LOST_WRITEBEHIND_DATA_NETWORK_SERVER_ERROR = 789

#
# MessageId: ERROR_LOST_WRITEBEHIND_DATA_LOCAL_DISK_ERROR
#
# MessageText:
#
# {Delayed Write Failed}
# Windows was unable to save all the data for the file %hs; the data has been lost.
# This error may be caused if the device has been removed or the media is write-protected.
#
ERROR_LOST_WRITEBEHIND_DATA_LOCAL_DISK_ERROR = 790

#
# MessageId: ERROR_BAD_MCFG_TABLE
#
# MessageText:
#
# The resources required for this device conflict with the MCFG table.
#
ERROR_BAD_MCFG_TABLE = 791

#
# MessageId: ERROR_DISK_REPAIR_REDIRECTED
#
# MessageText:
#
# The volume repair could not be performed while it is online.
# Please schedule to take the volume offline so that it can be repaired.
#
ERROR_DISK_REPAIR_REDIRECTED = 792

#
# MessageId: ERROR_DISK_REPAIR_UNSUCCESSFUL
#
# MessageText:
#
# The volume repair was not successful.
#
ERROR_DISK_REPAIR_UNSUCCESSFUL = 793

#
# MessageId: ERROR_CORRUPT_LOG_OVERFULL
#
# MessageText:
#
# One of the volume corruption logs is full. Further corruptions that may be detected won't be logged.
#
ERROR_CORRUPT_LOG_OVERFULL = 794

#
# MessageId: ERROR_CORRUPT_LOG_CORRUPTED
#
# MessageText:
#
# One of the volume corruption logs is internally corrupted and needs to be recreated. The volume may contain undetected corruptions and must be scanned.
#
ERROR_CORRUPT_LOG_CORRUPTED = 795

#
# MessageId: ERROR_CORRUPT_LOG_UNAVAILABLE
#
# MessageText:
#
# One of the volume corruption logs is unavailable for being operated on.
#
ERROR_CORRUPT_LOG_UNAVAILABLE = 796

#
# MessageId: ERROR_CORRUPT_LOG_DELETED_FULL
#
# MessageText:
#
# One of the volume corruption logs was deleted while still having corruption records in them. The volume contains detected corruptions and must be scanned.
#
ERROR_CORRUPT_LOG_DELETED_FULL = 797

#
# MessageId: ERROR_CORRUPT_LOG_CLEARED
#
# MessageText:
#
# One of the volume corruption logs was cleared by chkdsk and no longer contains real corruptions.
#
ERROR_CORRUPT_LOG_CLEARED = 798

#
# MessageId: ERROR_ORPHAN_NAME_EXHAUSTED
#
# MessageText:
#
# Orphaned files exist on the volume but could not be recovered because no more new names could be created in the recovery directory. Files must be moved from the recovery directory.
#
ERROR_ORPHAN_NAME_EXHAUSTED = 799

#
# MessageId: ERROR_OPLOCK_SWITCHED_TO_NEW_HANDLE
#
# MessageText:
#
# The oplock that was associated with this handle is now associated with a different handle.
#
ERROR_OPLOCK_SWITCHED_TO_NEW_HANDLE = 800

#
# MessageId: ERROR_CANNOT_GRANT_REQUESTED_OPLOCK
#
# MessageText:
#
# An oplock of the requested level cannot be granted.  An oplock of a lower level may be available.
#
ERROR_CANNOT_GRANT_REQUESTED_OPLOCK = 801

#
# MessageId: ERROR_CANNOT_BREAK_OPLOCK
#
# MessageText:
#
# The operation did not complete successfully because it would cause an oplock to be broken. The caller has requested that existing oplocks not be broken.
#
ERROR_CANNOT_BREAK_OPLOCK = 802

#
# MessageId: ERROR_OPLOCK_HANDLE_CLOSED
#
# MessageText:
#
# The handle with which this oplock was associated has been closed.  The oplock is now broken.
#
ERROR_OPLOCK_HANDLE_CLOSED = 803

#
# MessageId: ERROR_NO_ACE_CONDITION
#
# MessageText:
#
# The specified access control entry (ACE) does not contain a condition.
#
ERROR_NO_ACE_CONDITION = 804

#
# MessageId: ERROR_INVALID_ACE_CONDITION
#
# MessageText:
#
# The specified access control entry (ACE) contains an invalid condition.
#
ERROR_INVALID_ACE_CONDITION = 805

#
# MessageId: ERROR_FILE_HANDLE_REVOKED
#
# MessageText:
#
# Access to the specified file handle has been revoked.
#
ERROR_FILE_HANDLE_REVOKED = 806

#
# MessageId: ERROR_IMAGE_AT_DIFFERENT_BASE
#
# MessageText:
#
# {Image Relocated}
# An image file was mapped at a different address from the one specified in the image file but fixups will still be automatically performed on the image.
#
ERROR_IMAGE_AT_DIFFERENT_BASE = 807

#
# MessageId: ERROR_ENCRYPTED_IO_NOT_POSSIBLE
#
# MessageText:
#
# The read or write operation to an encrypted file could not be completed because the file has not been opened for data access.
#
ERROR_ENCRYPTED_IO_NOT_POSSIBLE = 808

#
# **** Available SYSTEM error codes ****
#
#
# MessageId: ERROR_EA_ACCESS_DENIED
#
# MessageText:
#
# Access to the extended attribute was denied.
#
ERROR_EA_ACCESS_DENIED = 994

#
# MessageId: ERROR_OPERATION_ABORTED
#
# MessageText:
#
# The I/O operation has been aborted because of either a thread exit or an application request.
#
ERROR_OPERATION_ABORTED = 995

#
# MessageId: ERROR_IO_INCOMPLETE
#
# MessageText:
#
# Overlapped I/O event is not in a signaled state.
#
ERROR_IO_INCOMPLETE = 996

#
# MessageId: ERROR_IO_PENDING
#
# MessageText:
#
# Overlapped I/O operation is in progress.
#
ERROR_IO_PENDING = 997

#
# MessageId: ERROR_NOACCESS
#
# MessageText:
#
# Invalid access to memory location.
#
ERROR_NOACCESS = 998

#
# MessageId: ERROR_SWAPERROR
#
# MessageText:
#
# Error performing inpage operation.
#
ERROR_SWAPERROR = 999

#
# MessageId: ERROR_STACK_OVERFLOW
#
# MessageText:
#
# Recursion too deep; the stack overflowed.
#
ERROR_STACK_OVERFLOW = 1001

#
# MessageId: ERROR_INVALID_MESSAGE
#
# MessageText:
#
# The window cannot act on the sent message.
#
ERROR_INVALID_MESSAGE = 1002

#
# MessageId: ERROR_CAN_NOT_COMPLETE
#
# MessageText:
#
# Cannot complete this function.
#
ERROR_CAN_NOT_COMPLETE = 1003

#
# MessageId: ERROR_INVALID_FLAGS
#
# MessageText:
#
# Invalid flags.
#
ERROR_INVALID_FLAGS = 1004

#
# MessageId: ERROR_UNRECOGNIZED_VOLUME
#
# MessageText:
#
# The volume does not contain a recognized file system.
# Please make sure that all required file system drivers are loaded and that the volume is not corrupted.
#
ERROR_UNRECOGNIZED_VOLUME = 1005

#
# MessageId: ERROR_FILE_INVALID
#
# MessageText:
#
# The volume for a file has been externally altered so that the opened file is no longer valid.
#
ERROR_FILE_INVALID = 1006

#
# MessageId: ERROR_FULLSCREEN_MODE
#
# MessageText:
#
# The requested operation cannot be performed in full-screen mode.
#
ERROR_FULLSCREEN_MODE = 1007

#
# MessageId: ERROR_NO_TOKEN
#
# MessageText:
#
# An attempt was made to reference a token that does not exist.
#
ERROR_NO_TOKEN = 1008

#
# MessageId: ERROR_BADDB
#
# MessageText:
#
# The configuration registry database is corrupt.
#
ERROR_BADDB = 1009

#
# MessageId: ERROR_BADKEY
#
# MessageText:
#
# The configuration registry key is invalid.
#
ERROR_BADKEY = 1010

#
# MessageId: ERROR_CANTOPEN
#
# MessageText:
#
# The configuration registry key could not be opened.
#
ERROR_CANTOPEN = 1011

#
# MessageId: ERROR_CANTREAD
#
# MessageText:
#
# The configuration registry key could not be read.
#
ERROR_CANTREAD = 1012

#
# MessageId: ERROR_CANTWRITE
#
# MessageText:
#
# The configuration registry key could not be written.
#
ERROR_CANTWRITE = 1013

#
# MessageId: ERROR_REGISTRY_RECOVERED
#
# MessageText:
#
# One of the files in the registry database had to be recovered by use of a log or alternate copy. The recovery was successful.
#
ERROR_REGISTRY_RECOVERED = 1014

#
# MessageId: ERROR_REGISTRY_CORRUPT
#
# MessageText:
#
# The registry is corrupted. The structure of one of the files containing registry data is corrupted, or the system's memory image of the file is corrupted, or the file could not be recovered because the alternate copy or log was absent or corrupted.
#
ERROR_REGISTRY_CORRUPT = 1015

#
# MessageId: ERROR_REGISTRY_IO_FAILED
#
# MessageText:
#
# An I/O operation initiated by the registry failed unrecoverably. The registry could not read in, or write out, or flush, one of the files that contain the system's image of the registry.
#
ERROR_REGISTRY_IO_FAILED = 1016

#
# MessageId: ERROR_NOT_REGISTRY_FILE
#
# MessageText:
#
# The system has attempted to load or restore a file into the registry, but the specified file is not in a registry file format.
#
ERROR_NOT_REGISTRY_FILE = 1017

#
# MessageId: ERROR_KEY_DELETED
#
# MessageText:
#
# Illegal operation attempted on a registry key that has been marked for deletion.
#
ERROR_KEY_DELETED = 1018

#
# MessageId: ERROR_NO_LOG_SPACE
#
# MessageText:
#
# System could not allocate the required space in a registry log.
#
ERROR_NO_LOG_SPACE = 1019

#
# MessageId: ERROR_KEY_HAS_CHILDREN
#
# MessageText:
#
# Cannot create a symbolic link in a registry key that already has subkeys or values.
#
ERROR_KEY_HAS_CHILDREN = 1020

#
# MessageId: ERROR_CHILD_MUST_BE_VOLATILE
#
# MessageText:
#
# Cannot create a stable subkey under a volatile parent key.
#
ERROR_CHILD_MUST_BE_VOLATILE = 1021

#
# MessageId: ERROR_NOTIFY_ENUM_DIR
#
# MessageText:
#
# A notify change request is being completed and the information is not being returned in the caller's buffer. The caller now needs to enumerate the files to find the changes.
#
ERROR_NOTIFY_ENUM_DIR = 1022

#
# MessageId: ERROR_DEPENDENT_SERVICES_RUNNING
#
# MessageText:
#
# A stop control has been sent to a service that other running services are dependent on.
#
ERROR_DEPENDENT_SERVICES_RUNNING = 1051

#
# MessageId: ERROR_INVALID_SERVICE_CONTROL
#
# MessageText:
#
# The requested control is not valid for this service.
#
ERROR_INVALID_SERVICE_CONTROL = 1052

#
# MessageId: ERROR_SERVICE_REQUEST_TIMEOUT
#
# MessageText:
#
# The service did not respond to the start or control request in a timely fashion.
#
ERROR_SERVICE_REQUEST_TIMEOUT = 1053

#
# MessageId: ERROR_SERVICE_NO_THREAD
#
# MessageText:
#
# A thread could not be created for the service.
#
ERROR_SERVICE_NO_THREAD = 1054

#
# MessageId: ERROR_SERVICE_DATABASE_LOCKED
#
# MessageText:
#
# The service database is locked.
#
ERROR_SERVICE_DATABASE_LOCKED = 1055

#
# MessageId: ERROR_SERVICE_ALREADY_RUNNING
#
# MessageText:
#
# An instance of the service is already running.
#
ERROR_SERVICE_ALREADY_RUNNING = 1056

#
# MessageId: ERROR_INVALID_SERVICE_ACCOUNT
#
# MessageText:
#
# The account name is invalid or does not exist, or the password is invalid for the account name specified.
#
ERROR_INVALID_SERVICE_ACCOUNT = 1057

#
# MessageId: ERROR_SERVICE_DISABLED
#
# MessageText:
#
# The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.
#
ERROR_SERVICE_DISABLED = 1058

#
# MessageId: ERROR_CIRCULAR_DEPENDENCY
#
# MessageText:
#
# Circular service dependency was specified.
#
ERROR_CIRCULAR_DEPENDENCY = 1059

#
# MessageId: ERROR_SERVICE_DOES_NOT_EXIST
#
# MessageText:
#
# The specified service does not exist as an installed service.
#
ERROR_SERVICE_DOES_NOT_EXIST = 1060

#
# MessageId: ERROR_SERVICE_CANNOT_ACCEPT_CTRL
#
# MessageText:
#
# The service cannot accept control messages at this time.
#
ERROR_SERVICE_CANNOT_ACCEPT_CTRL = 1061

#
# MessageId: ERROR_SERVICE_NOT_ACTIVE
#
# MessageText:
#
# The service has not been started.
#
ERROR_SERVICE_NOT_ACTIVE = 1062

#
# MessageId: ERROR_FAILED_SERVICE_CONTROLLER_CONNECT
#
# MessageText:
#
# The service process could not connect to the service controller.
#
ERROR_FAILED_SERVICE_CONTROLLER_CONNECT = 1063

#
# MessageId: ERROR_EXCEPTION_IN_SERVICE
#
# MessageText:
#
# An exception occurred in the service when handling the control request.
#
ERROR_EXCEPTION_IN_SERVICE = 1064

#
# MessageId: ERROR_DATABASE_DOES_NOT_EXIST
#
# MessageText:
#
# The database specified does not exist.
#
ERROR_DATABASE_DOES_NOT_EXIST = 1065

#
# MessageId: ERROR_SERVICE_SPECIFIC_ERROR
#
# MessageText:
#
# The service has returned a service-specific error code.
#
ERROR_SERVICE_SPECIFIC_ERROR = 1066

#
# MessageId: ERROR_PROCESS_ABORTED
#
# MessageText:
#
# The process terminated unexpectedly.
#
ERROR_PROCESS_ABORTED = 1067

#
# MessageId: ERROR_SERVICE_DEPENDENCY_FAIL
#
# MessageText:
#
# The dependency service or group failed to start.
#
ERROR_SERVICE_DEPENDENCY_FAIL = 1068

#
# MessageId: ERROR_SERVICE_LOGON_FAILED
#
# MessageText:
#
# The service did not start due to a logon failure.
#
ERROR_SERVICE_LOGON_FAILED = 1069

#
# MessageId: ERROR_SERVICE_START_HANG
#
# MessageText:
#
# After starting, the service hung in a start-pending state.
#
ERROR_SERVICE_START_HANG = 1070

#
# MessageId: ERROR_INVALID_SERVICE_LOCK
#
# MessageText:
#
# The specified service database lock is invalid.
#
ERROR_INVALID_SERVICE_LOCK = 1071

#
# MessageId: ERROR_SERVICE_MARKED_FOR_DELETE
#
# MessageText:
#
# The specified service has been marked for deletion.
#
ERROR_SERVICE_MARKED_FOR_DELETE = 1072

#
# MessageId: ERROR_SERVICE_EXISTS
#
# MessageText:
#
# The specified service already exists.
#
ERROR_SERVICE_EXISTS = 1073

#
# MessageId: ERROR_ALREADY_RUNNING_LKG
#
# MessageText:
#
# The system is currently running with the last-known-good configuration.
#
ERROR_ALREADY_RUNNING_LKG = 1074

#
# MessageId: ERROR_SERVICE_DEPENDENCY_DELETED
#
# MessageText:
#
# The dependency service does not exist or has been marked for deletion.
#
ERROR_SERVICE_DEPENDENCY_DELETED = 1075

#
# MessageId: ERROR_BOOT_ALREADY_ACCEPTED
#
# MessageText:
#
# The current boot has already been accepted for use as the last-known-good control set.
#
ERROR_BOOT_ALREADY_ACCEPTED = 1076

#
# MessageId: ERROR_SERVICE_NEVER_STARTED
#
# MessageText:
#
# No attempts to start the service have been made since the last boot.
#
ERROR_SERVICE_NEVER_STARTED = 1077

#
# MessageId: ERROR_DUPLICATE_SERVICE_NAME
#
# MessageText:
#
# The name is already in use as either a service name or a service display name.
#
ERROR_DUPLICATE_SERVICE_NAME = 1078

#
# MessageId: ERROR_DIFFERENT_SERVICE_ACCOUNT
#
# MessageText:
#
# The account specified for this service is different from the account specified for other services running in the same process.
#
ERROR_DIFFERENT_SERVICE_ACCOUNT = 1079

#
# MessageId: ERROR_CANNOT_DETECT_DRIVER_FAILURE
#
# MessageText:
#
# Failure actions can only be set for Win32 services, not for drivers.
#
ERROR_CANNOT_DETECT_DRIVER_FAILURE = 1080

#
# MessageId: ERROR_CANNOT_DETECT_PROCESS_ABORT
#
# MessageText:
#
# This service runs in the same process as the service control manager.
# Therefore, the service control manager cannot take action if this service's process terminates unexpectedly.
#
ERROR_CANNOT_DETECT_PROCESS_ABORT = 1081

#
# MessageId: ERROR_NO_RECOVERY_PROGRAM
#
# MessageText:
#
# No recovery program has been configured for this service.
#
ERROR_NO_RECOVERY_PROGRAM = 1082

#
# MessageId: ERROR_SERVICE_NOT_IN_EXE
#
# MessageText:
#
# The executable program that this service is configured to run in does not implement the service.
#
ERROR_SERVICE_NOT_IN_EXE = 1083

#
# MessageId: ERROR_NOT_SAFEBOOT_SERVICE
#
# MessageText:
#
# This service cannot be started in Safe Mode
#
ERROR_NOT_SAFEBOOT_SERVICE = 1084

#
# MessageId: ERROR_END_OF_MEDIA
#
# MessageText:
#
# The physical end of the tape has been reached.
#
ERROR_END_OF_MEDIA = 1100

#
# MessageId: ERROR_FILEMARK_DETECTED
#
# MessageText:
#
# A tape access reached a filemark.
#
ERROR_FILEMARK_DETECTED = 1101

#
# MessageId: ERROR_BEGINNING_OF_MEDIA
#
# MessageText:
#
# The beginning of the tape or a partition was encountered.
#
ERROR_BEGINNING_OF_MEDIA = 1102

#
# MessageId: ERROR_SETMARK_DETECTED
#
# MessageText:
#
# A tape access reached the end of a set of files.
#
ERROR_SETMARK_DETECTED = 1103

#
# MessageId: ERROR_NO_DATA_DETECTED
#
# MessageText:
#
# No more data is on the tape.
#
ERROR_NO_DATA_DETECTED = 1104

#
# MessageId: ERROR_PARTITION_FAILURE
#
# MessageText:
#
# Tape could not be partitioned.
#
ERROR_PARTITION_FAILURE = 1105

#
# MessageId: ERROR_INVALID_BLOCK_LENGTH
#
# MessageText:
#
# When accessing a new tape of a multivolume partition, the current block size is incorrect.
#
ERROR_INVALID_BLOCK_LENGTH = 1106

#
# MessageId: ERROR_DEVICE_NOT_PARTITIONED
#
# MessageText:
#
# Tape partition information could not be found when loading a tape.
#
ERROR_DEVICE_NOT_PARTITIONED = 1107

#
# MessageId: ERROR_UNABLE_TO_LOCK_MEDIA
#
# MessageText:
#
# Unable to lock the media eject mechanism.
#
ERROR_UNABLE_TO_LOCK_MEDIA = 1108

#
# MessageId: ERROR_UNABLE_TO_UNLOAD_MEDIA
#
# MessageText:
#
# Unable to unload the media.
#
ERROR_UNABLE_TO_UNLOAD_MEDIA = 1109

#
# MessageId: ERROR_MEDIA_CHANGED
#
# MessageText:
#
# The media in the drive may have changed.
#
ERROR_MEDIA_CHANGED = 1110

#
# MessageId: ERROR_BUS_RESET
#
# MessageText:
#
# The I/O bus was reset.
#
ERROR_BUS_RESET = 1111

#
# MessageId: ERROR_NO_MEDIA_IN_DRIVE
#
# MessageText:
#
# No media in drive.
#
ERROR_NO_MEDIA_IN_DRIVE = 1112

#
# MessageId: ERROR_NO_UNICODE_TRANSLATION
#
# MessageText:
#
# No mapping for the Unicode character exists in the target multi-byte code page.
#
ERROR_NO_UNICODE_TRANSLATION = 1113

#
# MessageId: ERROR_DLL_INIT_FAILED
#
# MessageText:
#
# A dynamic link library (DLL) initialization routine failed.
#
ERROR_DLL_INIT_FAILED = 1114

#
# MessageId: ERROR_SHUTDOWN_IN_PROGRESS
#
# MessageText:
#
# A system shutdown is in progress.
#
ERROR_SHUTDOWN_IN_PROGRESS = 1115

#
# MessageId: ERROR_NO_SHUTDOWN_IN_PROGRESS
#
# MessageText:
#
# Unable to abort the system shutdown because no shutdown was in progress.
#
ERROR_NO_SHUTDOWN_IN_PROGRESS = 1116

#
# MessageId: ERROR_IO_DEVICE
#
# MessageText:
#
# The request could not be performed because of an I/O device error.
#
ERROR_IO_DEVICE = 1117

#
# MessageId: ERROR_SERIAL_NO_DEVICE
#
# MessageText:
#
# No serial device was successfully initialized. The serial driver will unload.
#
ERROR_SERIAL_NO_DEVICE = 1118

#
# MessageId: ERROR_IRQ_BUSY
#
# MessageText:
#
# Unable to open a device that was sharing an interrupt request (IRQ) with other devices. At least one other device that uses that IRQ was already opened.
#
ERROR_IRQ_BUSY = 1119

#
# MessageId: ERROR_MORE_WRITES
#
# MessageText:
#
# A serial I/O operation was completed by another write to the serial port.
# (The IOCTL_SERIAL_XOFF_COUNTER reached zero.)
#
ERROR_MORE_WRITES = 1120

#
# MessageId: ERROR_COUNTER_TIMEOUT
#
# MessageText:
#
# A serial I/O operation completed because the timeout period expired.
# (The IOCTL_SERIAL_XOFF_COUNTER did not reach zero.)
#
ERROR_COUNTER_TIMEOUT = 1121

#
# MessageId: ERROR_FLOPPY_ID_MARK_NOT_FOUND
#
# MessageText:
#
# No ID address mark was found on the floppy disk.
#
ERROR_FLOPPY_ID_MARK_NOT_FOUND = 1122

#
# MessageId: ERROR_FLOPPY_WRONG_CYLINDER
#
# MessageText:
#
# Mismatch between the floppy disk sector ID field and the floppy disk controller track address.
#
ERROR_FLOPPY_WRONG_CYLINDER = 1123

#
# MessageId: ERROR_FLOPPY_UNKNOWN_ERROR
#
# MessageText:
#
# The floppy disk controller reported an error that is not recognized by the floppy disk driver.
#
ERROR_FLOPPY_UNKNOWN_ERROR = 1124

#
# MessageId: ERROR_FLOPPY_BAD_REGISTERS
#
# MessageText:
#
# The floppy disk controller returned inconsistent results in its registers.
#
ERROR_FLOPPY_BAD_REGISTERS = 1125

#
# MessageId: ERROR_DISK_RECALIBRATE_FAILED
#
# MessageText:
#
# While accessing the hard disk, a recalibrate operation failed, even after retries.
#
ERROR_DISK_RECALIBRATE_FAILED = 1126

#
# MessageId: ERROR_DISK_OPERATION_FAILED
#
# MessageText:
#
# While accessing the hard disk, a disk operation failed even after retries.
#
ERROR_DISK_OPERATION_FAILED = 1127

#
# MessageId: ERROR_DISK_RESET_FAILED
#
# MessageText:
#
# While accessing the hard disk, a disk controller reset was needed, but even that failed.
#
ERROR_DISK_RESET_FAILED = 1128

#
# MessageId: ERROR_EOM_OVERFLOW
#
# MessageText:
#
# Physical end of tape encountered.
#
ERROR_EOM_OVERFLOW = 1129

#
# MessageId: ERROR_NOT_ENOUGH_SERVER_MEMORY
#
# MessageText:
#
# Not enough server storage is available to process this command.
#
ERROR_NOT_ENOUGH_SERVER_MEMORY = 1130

#
# MessageId: ERROR_POSSIBLE_DEADLOCK
#
# MessageText:
#
# A potential deadlock condition has been detected.
#
ERROR_POSSIBLE_DEADLOCK = 1131

#
# MessageId: ERROR_MAPPED_ALIGNMENT
#
# MessageText:
#
# The base address or the file offset specified does not have the proper alignment.
#
ERROR_MAPPED_ALIGNMENT = 1132

#
# MessageId: ERROR_SET_POWER_STATE_VETOED
#
# MessageText:
#
# An attempt to change the system power state was vetoed by another application or driver.
#
ERROR_SET_POWER_STATE_VETOED = 1140

#
# MessageId: ERROR_SET_POWER_STATE_FAILED
#
# MessageText:
#
# The system BIOS failed an attempt to change the system power state.
#
ERROR_SET_POWER_STATE_FAILED = 1141

#
# MessageId: ERROR_TOO_MANY_LINKS
#
# MessageText:
#
# An attempt was made to create more links on a file than the file system supports.
#
ERROR_TOO_MANY_LINKS = 1142

#
# MessageId: ERROR_OLD_WIN_VERSION
#
# MessageText:
#
# The specified program requires a newer version of Windows.
#
ERROR_OLD_WIN_VERSION = 1150

#
# MessageId: ERROR_APP_WRONG_OS
#
# MessageText:
#
# The specified program is not a Windows or MS-DOS program.
#
ERROR_APP_WRONG_OS = 1151

#
# MessageId: ERROR_SINGLE_INSTANCE_APP
#
# MessageText:
#
# Cannot start more than one instance of the specified program.
#
ERROR_SINGLE_INSTANCE_APP = 1152

#
# MessageId: ERROR_RMODE_APP
#
# MessageText:
#
# The specified program was written for an earlier version of Windows.
#
ERROR_RMODE_APP = 1153

#
# MessageId: ERROR_INVALID_DLL
#
# MessageText:
#
# One of the library files needed to run this application is damaged.
#
ERROR_INVALID_DLL = 1154

#
# MessageId: ERROR_NO_ASSOCIATION
#
# MessageText:
#
# No application is associated with the specified file for this operation.
#
ERROR_NO_ASSOCIATION = 1155

#
# MessageId: ERROR_DDE_FAIL
#
# MessageText:
#
# An error occurred in sending the command to the application.
#
ERROR_DDE_FAIL = 1156

#
# MessageId: ERROR_DLL_NOT_FOUND
#
# MessageText:
#
# One of the library files needed to run this application cannot be found.
#
ERROR_DLL_NOT_FOUND = 1157

#
# MessageId: ERROR_NO_MORE_USER_HANDLES
#
# MessageText:
#
# The current process has used all of its system allowance of handles for Window Manager objects.
#
ERROR_NO_MORE_USER_HANDLES = 1158

#
# MessageId: ERROR_MESSAGE_SYNC_ONLY
#
# MessageText:
#
# The message can be used only with synchronous operations.
#
ERROR_MESSAGE_SYNC_ONLY = 1159

#
# MessageId: ERROR_SOURCE_ELEMENT_EMPTY
#
# MessageText:
#
# The indicated source element has no media.
#
ERROR_SOURCE_ELEMENT_EMPTY = 1160

#
# MessageId: ERROR_DESTINATION_ELEMENT_FULL
#
# MessageText:
#
# The indicated destination element already contains media.
#
ERROR_DESTINATION_ELEMENT_FULL = 1161

#
# MessageId: ERROR_ILLEGAL_ELEMENT_ADDRESS
#
# MessageText:
#
# The indicated element does not exist.
#
ERROR_ILLEGAL_ELEMENT_ADDRESS = 1162

#
# MessageId: ERROR_MAGAZINE_NOT_PRESENT
#
# MessageText:
#
# The indicated element is part of a magazine that is not present.
#
ERROR_MAGAZINE_NOT_PRESENT = 1163

#
# MessageId: ERROR_DEVICE_REINITIALIZATION_NEEDED
#
# MessageText:
#
# The indicated device requires reinitialization due to hardware errors.
#
ERROR_DEVICE_REINITIALIZATION_NEEDED = 1164

#
# MessageId: ERROR_DEVICE_REQUIRES_CLEANING
#
# MessageText:
#
# The device has indicated that cleaning is required before further operations are attempted.
#
ERROR_DEVICE_REQUIRES_CLEANING = 1165

#
# MessageId: ERROR_DEVICE_DOOR_OPEN
#
# MessageText:
#
# The device has indicated that its door is open.
#
ERROR_DEVICE_DOOR_OPEN = 1166

#
# MessageId: ERROR_DEVICE_NOT_CONNECTED
#
# MessageText:
#
# The device is not connected.
#
ERROR_DEVICE_NOT_CONNECTED = 1167

#
# MessageId: ERROR_NOT_FOUND
#
# MessageText:
#
# Element not found.
#
ERROR_NOT_FOUND = 1168

#
# MessageId: ERROR_NO_MATCH
#
# MessageText:
#
# There was no match for the specified key in the index.
#
ERROR_NO_MATCH = 1169

#
# MessageId: ERROR_SET_NOT_FOUND
#
# MessageText:
#
# The property set specified does not exist on the object.
#
ERROR_SET_NOT_FOUND = 1170

#
# MessageId: ERROR_POINT_NOT_FOUND
#
# MessageText:
#
# The point passed to GetMouseMovePoints is not in the buffer.
#
ERROR_POINT_NOT_FOUND = 1171

#
# MessageId: ERROR_NO_TRACKING_SERVICE
#
# MessageText:
#
# The tracking (workstation) service is not running.
#
ERROR_NO_TRACKING_SERVICE = 1172

#
# MessageId: ERROR_NO_VOLUME_ID
#
# MessageText:
#
# The Volume ID could not be found.
#
ERROR_NO_VOLUME_ID = 1173

#
# MessageId: ERROR_UNABLE_TO_REMOVE_REPLACED
#
# MessageText:
#
# Unable to remove the file to be replaced.
#
ERROR_UNABLE_TO_REMOVE_REPLACED = 1175

#
# MessageId: ERROR_UNABLE_TO_MOVE_REPLACEMENT
#
# MessageText:
#
# Unable to move the replacement file to the file to be replaced. The file to be replaced has retained its original name.
#
ERROR_UNABLE_TO_MOVE_REPLACEMENT = 1176

#
# MessageId: ERROR_UNABLE_TO_MOVE_REPLACEMENT_2
#
# MessageText:
#
# Unable to move the replacement file to the file to be replaced. The file to be replaced has been renamed using the backup name.
#
ERROR_UNABLE_TO_MOVE_REPLACEMENT_2 = 1177

#
# MessageId: ERROR_JOURNAL_DELETE_IN_PROGRESS
#
# MessageText:
#
# The volume change journal is being deleted.
#
ERROR_JOURNAL_DELETE_IN_PROGRESS = 1178

#
# MessageId: ERROR_JOURNAL_NOT_ACTIVE
#
# MessageText:
#
# The volume change journal is not active.
#
ERROR_JOURNAL_NOT_ACTIVE = 1179

#
# MessageId: ERROR_POTENTIAL_FILE_FOUND
#
# MessageText:
#
# A file was found, but it may not be the correct file.
#
ERROR_POTENTIAL_FILE_FOUND = 1180

#
# MessageId: ERROR_JOURNAL_ENTRY_DELETED
#
# MessageText:
#
# The journal entry has been deleted from the journal.
#
ERROR_JOURNAL_ENTRY_DELETED = 1181

#
# MessageId: ERROR_SHUTDOWN_IS_SCHEDULED
#
# MessageText:
#
# A system shutdown has already been scheduled.
#
ERROR_SHUTDOWN_IS_SCHEDULED = 1190

#
# MessageId: ERROR_SHUTDOWN_USERS_LOGGED_ON
#
# MessageText:
#
# The system shutdown cannot be initiated because there are other users logged on to the computer.
#
ERROR_SHUTDOWN_USERS_LOGGED_ON = 1191

#
# MessageId: ERROR_BAD_DEVICE
#
# MessageText:
#
# The specified device name is invalid.
#
ERROR_BAD_DEVICE = 1200

#
# MessageId: ERROR_CONNECTION_UNAVAIL
#
# MessageText:
#
# The device is not currently connected but it is a remembered connection.
#
ERROR_CONNECTION_UNAVAIL = 1201

#
# MessageId: ERROR_DEVICE_ALREADY_REMEMBERED
#
# MessageText:
#
# The local device name has a remembered connection to another network resource.
#
ERROR_DEVICE_ALREADY_REMEMBERED = 1202

#
# MessageId: ERROR_NO_NET_OR_BAD_PATH
#
# MessageText:
#
# The network path was either typed incorrectly, does not exist, or the network provider is not currently available. Please try retyping the path or contact your network administrator.
#
ERROR_NO_NET_OR_BAD_PATH = 1203

#
# MessageId: ERROR_BAD_PROVIDER
#
# MessageText:
#
# The specified network provider name is invalid.
#
ERROR_BAD_PROVIDER = 1204

#
# MessageId: ERROR_CANNOT_OPEN_PROFILE
#
# MessageText:
#
# Unable to open the network connection profile.
#
ERROR_CANNOT_OPEN_PROFILE = 1205

#
# MessageId: ERROR_BAD_PROFILE
#
# MessageText:
#
# The network connection profile is corrupted.
#
ERROR_BAD_PROFILE = 1206

#
# MessageId: ERROR_NOT_CONTAINER
#
# MessageText:
#
# Cannot enumerate a noncontainer.
#
ERROR_NOT_CONTAINER = 1207

#
# MessageId: ERROR_EXTENDED_ERROR
#
# MessageText:
#
# An extended error has occurred.
#
ERROR_EXTENDED_ERROR = 1208

#
# MessageId: ERROR_INVALID_GROUPNAME
#
# MessageText:
#
# The format of the specified group name is invalid.
#
ERROR_INVALID_GROUPNAME = 1209

#
# MessageId: ERROR_INVALID_COMPUTERNAME
#
# MessageText:
#
# The format of the specified computer name is invalid.
#
ERROR_INVALID_COMPUTERNAME = 1210

#
# MessageId: ERROR_INVALID_EVENTNAME
#
# MessageText:
#
# The format of the specified event name is invalid.
#
ERROR_INVALID_EVENTNAME = 1211

#
# MessageId: ERROR_INVALID_DOMAINNAME
#
# MessageText:
#
# The format of the specified domain name is invalid.
#
ERROR_INVALID_DOMAINNAME = 1212

#
# MessageId: ERROR_INVALID_SERVICENAME
#
# MessageText:
#
# The format of the specified service name is invalid.
#
ERROR_INVALID_SERVICENAME = 1213

#
# MessageId: ERROR_INVALID_NETNAME
#
# MessageText:
#
# The format of the specified network name is invalid.
#
ERROR_INVALID_NETNAME = 1214

#
# MessageId: ERROR_INVALID_SHARENAME
#
# MessageText:
#
# The format of the specified share name is invalid.
#
ERROR_INVALID_SHARENAME = 1215

#
# MessageId: ERROR_INVALID_PASSWORDNAME
#
# MessageText:
#
# The format of the specified password is invalid.
#
ERROR_INVALID_PASSWORDNAME = 1216

#
# MessageId: ERROR_INVALID_MESSAGENAME
#
# MessageText:
#
# The format of the specified message name is invalid.
#
ERROR_INVALID_MESSAGENAME = 1217

#
# MessageId: ERROR_INVALID_MESSAGEDEST
#
# MessageText:
#
# The format of the specified message destination is invalid.
#
ERROR_INVALID_MESSAGEDEST = 1218

#
# MessageId: ERROR_SESSION_CREDENTIAL_CONFLICT
#
# MessageText:
#
# Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.
#
ERROR_SESSION_CREDENTIAL_CONFLICT = 1219

#
# MessageId: ERROR_REMOTE_SESSION_LIMIT_EXCEEDED
#
# MessageText:
#
# An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.
#
ERROR_REMOTE_SESSION_LIMIT_EXCEEDED = 1220

#
# MessageId: ERROR_DUP_DOMAINNAME
#
# MessageText:
#
# The workgroup or domain name is already in use by another computer on the network.
#
ERROR_DUP_DOMAINNAME = 1221

#
# MessageId: ERROR_NO_NETWORK
#
# MessageText:
#
# The network is not present or not started.
#
ERROR_NO_NETWORK = 1222

#
# MessageId: ERROR_CANCELLED
#
# MessageText:
#
# The operation was canceled by the user.
#
ERROR_CANCELLED = 1223

#
# MessageId: ERROR_USER_MAPPED_FILE
#
# MessageText:
#
# The requested operation cannot be performed on a file with a user-mapped section open.
#
ERROR_USER_MAPPED_FILE = 1224

#
# MessageId: ERROR_CONNECTION_REFUSED
#
# MessageText:
#
# The remote computer refused the network connection.
#
ERROR_CONNECTION_REFUSED = 1225

#
# MessageId: ERROR_GRACEFUL_DISCONNECT
#
# MessageText:
#
# The network connection was gracefully closed.
#
ERROR_GRACEFUL_DISCONNECT = 1226

#
# MessageId: ERROR_ADDRESS_ALREADY_ASSOCIATED
#
# MessageText:
#
# The network transport endpoint already has an address associated with it.
#
ERROR_ADDRESS_ALREADY_ASSOCIATED = 1227

#
# MessageId: ERROR_ADDRESS_NOT_ASSOCIATED
#
# MessageText:
#
# An address has not yet been associated with the network endpoint.
#
ERROR_ADDRESS_NOT_ASSOCIATED = 1228

#
# MessageId: ERROR_CONNECTION_INVALID
#
# MessageText:
#
# An operation was attempted on a nonexistent network connection.
#
ERROR_CONNECTION_INVALID = 1229

#
# MessageId: ERROR_CONNECTION_ACTIVE
#
# MessageText:
#
# An invalid operation was attempted on an active network connection.
#
ERROR_CONNECTION_ACTIVE = 1230

#
# MessageId: ERROR_NETWORK_UNREACHABLE
#
# MessageText:
#
# The network location cannot be reached. For information about network troubleshooting, see Windows Help.
#
ERROR_NETWORK_UNREACHABLE = 1231

#
# MessageId: ERROR_HOST_UNREACHABLE
#
# MessageText:
#
# The network location cannot be reached. For information about network troubleshooting, see Windows Help.
#
ERROR_HOST_UNREACHABLE = 1232

#
# MessageId: ERROR_PROTOCOL_UNREACHABLE
#
# MessageText:
#
# The network location cannot be reached. For information about network troubleshooting, see Windows Help.
#
ERROR_PROTOCOL_UNREACHABLE = 1233

#
# MessageId: ERROR_PORT_UNREACHABLE
#
# MessageText:
#
# No service is operating at the destination network endpoint on the remote system.
#
ERROR_PORT_UNREACHABLE = 1234

#
# MessageId: ERROR_REQUEST_ABORTED
#
# MessageText:
#
# The request was aborted.
#
ERROR_REQUEST_ABORTED = 1235

#
# MessageId: ERROR_CONNECTION_ABORTED
#
# MessageText:
#
# The network connection was aborted by the local system.
#
ERROR_CONNECTION_ABORTED = 1236

#
# MessageId: ERROR_RETRY
#
# MessageText:
#
# The operation could not be completed. A retry should be performed.
#
ERROR_RETRY = 1237

#
# MessageId: ERROR_CONNECTION_COUNT_LIMIT
#
# MessageText:
#
# A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.
#
ERROR_CONNECTION_COUNT_LIMIT = 1238

#
# MessageId: ERROR_LOGIN_TIME_RESTRICTION
#
# MessageText:
#
# Attempting to log in during an unauthorized time of day for this account.
#
ERROR_LOGIN_TIME_RESTRICTION = 1239

#
# MessageId: ERROR_LOGIN_WKSTA_RESTRICTION
#
# MessageText:
#
# The account is not authorized to log in from this station.
#
ERROR_LOGIN_WKSTA_RESTRICTION = 1240

#
# MessageId: ERROR_INCORRECT_ADDRESS
#
# MessageText:
#
# The network address could not be used for the operation requested.
#
ERROR_INCORRECT_ADDRESS = 1241

#
# MessageId: ERROR_ALREADY_REGISTERED
#
# MessageText:
#
# The service is already registered.
#
ERROR_ALREADY_REGISTERED = 1242

#
# MessageId: ERROR_SERVICE_NOT_FOUND
#
# MessageText:
#
# The specified service does not exist.
#
ERROR_SERVICE_NOT_FOUND = 1243

#
# MessageId: ERROR_NOT_AUTHENTICATED
#
# MessageText:
#
# The operation being requested was not performed because the user has not been authenticated.
#
ERROR_NOT_AUTHENTICATED = 1244

#
# MessageId: ERROR_NOT_LOGGED_ON
#
# MessageText:
#
# The operation being requested was not performed because the user has not logged on to the network. The specified service does not exist.
#
ERROR_NOT_LOGGED_ON = 1245

#
# MessageId: ERROR_CONTINUE
#
# MessageText:
#
# Continue with work in progress.
#
ERROR_CONTINUE = 1246

#
# MessageId: ERROR_ALREADY_INITIALIZED
#
# MessageText:
#
# An attempt was made to perform an initialization operation when initialization has already been completed.
#
ERROR_ALREADY_INITIALIZED = 1247

#
# MessageId: ERROR_NO_MORE_DEVICES
#
# MessageText:
#
# No more local devices.
#
ERROR_NO_MORE_DEVICES = 1248

#
# MessageId: ERROR_NO_SUCH_SITE
#
# MessageText:
#
# The specified site does not exist.
#
ERROR_NO_SUCH_SITE = 1249

#
# MessageId: ERROR_DOMAIN_CONTROLLER_EXISTS
#
# MessageText:
#
# A domain controller with the specified name already exists.
#
ERROR_DOMAIN_CONTROLLER_EXISTS = 1250

#
# MessageId: ERROR_ONLY_IF_CONNECTED
#
# MessageText:
#
# This operation is supported only when you are connected to the server.
#
ERROR_ONLY_IF_CONNECTED = 1251

#
# MessageId: ERROR_OVERRIDE_NOCHANGES
#
# MessageText:
#
# The group policy framework should call the extension even if there are no changes.
#
ERROR_OVERRIDE_NOCHANGES = 1252

#
# MessageId: ERROR_BAD_USER_PROFILE
#
# MessageText:
#
# The specified user does not have a valid profile.
#
ERROR_BAD_USER_PROFILE = 1253

#
# MessageId: ERROR_NOT_SUPPORTED_ON_SBS
#
# MessageText:
#
# This operation is not supported on a computer running Windows Server 2003 for Small Business Server
#
ERROR_NOT_SUPPORTED_ON_SBS = 1254

#
# MessageId: ERROR_SERVER_SHUTDOWN_IN_PROGRESS
#
# MessageText:
#
# The server machine is shutting down.
#
ERROR_SERVER_SHUTDOWN_IN_PROGRESS = 1255

#
# MessageId: ERROR_HOST_DOWN
#
# MessageText:
#
# The remote system is not available. For information about network troubleshooting, see Windows Help.
#
ERROR_HOST_DOWN = 1256

#
# MessageId: ERROR_NON_ACCOUNT_SID
#
# MessageText:
#
# The security identifier provided is not from an account domain.
#
ERROR_NON_ACCOUNT_SID = 1257

#
# MessageId: ERROR_NON_DOMAIN_SID
#
# MessageText:
#
# The security identifier provided does not have a domain component.
#
ERROR_NON_DOMAIN_SID = 1258

#
# MessageId: ERROR_APPHELP_BLOCK
#
# MessageText:
#
# AppHelp dialog canceled thus preventing the application from starting.
#
ERROR_APPHELP_BLOCK = 1259

#
# MessageId: ERROR_ACCESS_DISABLED_BY_POLICY
#
# MessageText:
#
# This program is blocked by group policy. For more information, contact your system administrator.
#
ERROR_ACCESS_DISABLED_BY_POLICY = 1260

#
# MessageId: ERROR_REG_NAT_CONSUMPTION
#
# MessageText:
#
# A program attempt to use an invalid register value. Normally caused by an uninitialized register. This error is Itanium specific.
#
ERROR_REG_NAT_CONSUMPTION = 1261

#
# MessageId: ERROR_CSCSHARE_OFFLINE
#
# MessageText:
#
# The share is currently offline or does not exist.
#
ERROR_CSCSHARE_OFFLINE = 1262

#
# MessageId: ERROR_PKINIT_FAILURE
#
# MessageText:
#
# The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon. There is more information in the system event log.
#
ERROR_PKINIT_FAILURE = 1263

#
# MessageId: ERROR_SMARTCARD_SUBSYSTEM_FAILURE
#
# MessageText:
#
# The Kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.
#
ERROR_SMARTCARD_SUBSYSTEM_FAILURE = 1264

#
# MessageId: ERROR_DOWNGRADE_DETECTED
#
# MessageText:
#
# The system cannot contact a domain controller to service the authentication request. Please try again later.
#
ERROR_DOWNGRADE_DETECTED = 1265

#
# Do not use ID's 1266 - 1270 as the symbolicNames have been moved to SEC_E_*
#
#
# MessageId: ERROR_MACHINE_LOCKED
#
# MessageText:
#
# The machine is locked and cannot be shut down without the force option.
#
ERROR_MACHINE_LOCKED = 1271

#
# MessageId: ERROR_CALLBACK_SUPPLIED_INVALID_DATA
#
# MessageText:
#
# An application-defined callback gave invalid data when called.
#
ERROR_CALLBACK_SUPPLIED_INVALID_DATA = 1273

#
# MessageId: ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED
#
# MessageText:
#
# The group policy framework should call the extension in the synchronous foreground policy refresh.
#
ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED = 1274

#
# MessageId: ERROR_DRIVER_BLOCKED
#
# MessageText:
#
# This driver has been blocked from loading
#
ERROR_DRIVER_BLOCKED = 1275

#
# MessageId: ERROR_INVALID_IMPORT_OF_NON_DLL
#
# MessageText:
#
# A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.
#
ERROR_INVALID_IMPORT_OF_NON_DLL = 1276

#
# MessageId: ERROR_ACCESS_DISABLED_WEBBLADE
#
# MessageText:
#
# Windows cannot open this program since it has been disabled.
#
ERROR_ACCESS_DISABLED_WEBBLADE = 1277

#
# MessageId: ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER
#
# MessageText:
#
# Windows cannot open this program because the license enforcement system has been tampered with or become corrupted.
#
ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER = 1278

#
# MessageId: ERROR_RECOVERY_FAILURE
#
# MessageText:
#
# A transaction recover failed.
#
ERROR_RECOVERY_FAILURE = 1279

#
# MessageId: ERROR_ALREADY_FIBER
#
# MessageText:
#
# The current thread has already been converted to a fiber.
#
ERROR_ALREADY_FIBER = 1280

#
# MessageId: ERROR_ALREADY_THREAD
#
# MessageText:
#
# The current thread has already been converted from a fiber.
#
ERROR_ALREADY_THREAD = 1281

#
# MessageId: ERROR_STACK_BUFFER_OVERRUN
#
# MessageText:
#
# The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.
#
ERROR_STACK_BUFFER_OVERRUN = 1282

#
# MessageId: ERROR_PARAMETER_QUOTA_EXCEEDED
#
# MessageText:
#
# Data present in one of the parameters is more than the function can operate on.
#
ERROR_PARAMETER_QUOTA_EXCEEDED = 1283

#
# MessageId: ERROR_DEBUGGER_INACTIVE
#
# MessageText:
#
# An attempt to do an operation on a debug object failed because the object is in the process of being deleted.
#
ERROR_DEBUGGER_INACTIVE = 1284

#
# MessageId: ERROR_DELAY_LOAD_FAILED
#
# MessageText:
#
# An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.
#
ERROR_DELAY_LOAD_FAILED = 1285

#
# MessageId: ERROR_VDM_DISALLOWED
#
# MessageText:
#
# %1 is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.
#
ERROR_VDM_DISALLOWED = 1286

#
# MessageId: ERROR_UNIDENTIFIED_ERROR
#
# MessageText:
#
# Insufficient information exists to identify the cause of failure.
#
ERROR_UNIDENTIFIED_ERROR = 1287

#
# MessageId: ERROR_INVALID_CRUNTIME_PARAMETER
#
# MessageText:
#
# The parameter passed to a C runtime function is incorrect.
#
ERROR_INVALID_CRUNTIME_PARAMETER = 1288

#
# MessageId: ERROR_BEYOND_VDL
#
# MessageText:
#
# The operation occurred beyond the valid data length of the file.
#
ERROR_BEYOND_VDL = 1289

#
# MessageId: ERROR_INCOMPATIBLE_SERVICE_SID_TYPE
#
# MessageText:
#
# The service start failed since one or more services in the same process have an incompatible service SID type setting. A service with restricted service SID type can only coexist in the same process with other services with a restricted SID type. If the service SID type for this service was just configured, the hosting process must be restarted in order to start this service.
#
ERROR_INCOMPATIBLE_SERVICE_SID_TYPE = 1290

#
# MessageId: ERROR_DRIVER_PROCESS_TERMINATED
#
# MessageText:
#
# The process hosting the driver for this device has been terminated.
#
ERROR_DRIVER_PROCESS_TERMINATED = 1291

#
# MessageId: ERROR_IMPLEMENTATION_LIMIT
#
# MessageText:
#
# An operation attempted to exceed an implementation-defined limit.
#
ERROR_IMPLEMENTATION_LIMIT = 1292

#
# MessageId: ERROR_PROCESS_IS_PROTECTED
#
# MessageText:
#
# Either the target process, or the target thread's containing process, is a protected process.
#
ERROR_PROCESS_IS_PROTECTED = 1293

#
# MessageId: ERROR_SERVICE_NOTIFY_CLIENT_LAGGING
#
# MessageText:
#
# The service notification client is lagging too far behind the current state of services in the machine.
#
ERROR_SERVICE_NOTIFY_CLIENT_LAGGING = 1294

#
# MessageId: ERROR_DISK_QUOTA_EXCEEDED
#
# MessageText:
#
# The requested file operation failed because the storage quota was exceeded.
# To free up disk space, move files to a different location or delete unnecessary files. For more information, contact your system administrator.
#
ERROR_DISK_QUOTA_EXCEEDED = 1295

#
# MessageId: ERROR_CONTENT_BLOCKED
#
# MessageText:
#
# The requested file operation failed because the storage policy blocks that type of file. For more information, contact your system administrator.
#
ERROR_CONTENT_BLOCKED = 1296

#
# MessageId: ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE
#
# MessageText:
#
# A privilege that the service requires to function properly does not exist in the service account configuration.
# You may use the Services Microsoft Management Console (MMC) snap-in (services.msc) and the Local Security Settings MMC snap-in (secpol.msc) to view the service configuration and the account configuration.
#
ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE = 1297

#
# MessageId: ERROR_APP_HANG
#
# MessageText:
#
# A thread involved in this operation appears to be unresponsive.
#
ERROR_APP_HANG = 1298


#/////////////////////////////////////////////////
#                                               //
#             SECURITY Error codes              //
#                                               //
#                 1299 to 1399                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INVALID_LABEL
#
# MessageText:
#
# Indicates a particular Security ID may not be assigned as the label of an object.
#
ERROR_INVALID_LABEL = 1299

#
# MessageId: ERROR_NOT_ALL_ASSIGNED
#
# MessageText:
#
# Not all privileges or groups referenced are assigned to the caller.
#
ERROR_NOT_ALL_ASSIGNED = 1300

#
# MessageId: ERROR_SOME_NOT_MAPPED
#
# MessageText:
#
# Some mapping between account names and security IDs was not done.
#
ERROR_SOME_NOT_MAPPED = 1301

#
# MessageId: ERROR_NO_QUOTAS_FOR_ACCOUNT
#
# MessageText:
#
# No system quota limits are specifically set for this account.
#
ERROR_NO_QUOTAS_FOR_ACCOUNT = 1302

#
# MessageId: ERROR_LOCAL_USER_SESSION_KEY
#
# MessageText:
#
# No encryption key is available. A well-known encryption key was returned.
#
ERROR_LOCAL_USER_SESSION_KEY = 1303

#
# MessageId: ERROR_NULL_LM_PASSWORD
#
# MessageText:
#
# The password is too complex to be converted to a LAN Manager password. The LAN Manager password returned is a NULL string.
#
ERROR_NULL_LM_PASSWORD = 1304

#
# MessageId: ERROR_UNKNOWN_REVISION
#
# MessageText:
#
# The revision level is unknown.
#
ERROR_UNKNOWN_REVISION = 1305

#
# MessageId: ERROR_REVISION_MISMATCH
#
# MessageText:
#
# Indicates two revision levels are incompatible.
#
ERROR_REVISION_MISMATCH = 1306

#
# MessageId: ERROR_INVALID_OWNER
#
# MessageText:
#
# This security ID may not be assigned as the owner of this object.
#
ERROR_INVALID_OWNER = 1307

#
# MessageId: ERROR_INVALID_PRIMARY_GROUP
#
# MessageText:
#
# This security ID may not be assigned as the primary group of an object.
#
ERROR_INVALID_PRIMARY_GROUP = 1308

#
# MessageId: ERROR_NO_IMPERSONATION_TOKEN
#
# MessageText:
#
# An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.
#
ERROR_NO_IMPERSONATION_TOKEN = 1309

#
# MessageId: ERROR_CANT_DISABLE_MANDATORY
#
# MessageText:
#
# The group may not be disabled.
#
ERROR_CANT_DISABLE_MANDATORY = 1310

#
# MessageId: ERROR_NO_LOGON_SERVERS
#
# MessageText:
#
# There are currently no logon servers available to service the logon request.
#
ERROR_NO_LOGON_SERVERS = 1311

#
# MessageId: ERROR_NO_SUCH_LOGON_SESSION
#
# MessageText:
#
# A specified logon session does not exist. It may already have been terminated.
#
ERROR_NO_SUCH_LOGON_SESSION = 1312

#
# MessageId: ERROR_NO_SUCH_PRIVILEGE
#
# MessageText:
#
# A specified privilege does not exist.
#
ERROR_NO_SUCH_PRIVILEGE = 1313

#
# MessageId: ERROR_PRIVILEGE_NOT_HELD
#
# MessageText:
#
# A required privilege is not held by the client.
#
ERROR_PRIVILEGE_NOT_HELD = 1314

#
# MessageId: ERROR_INVALID_ACCOUNT_NAME
#
# MessageText:
#
# The name provided is not a properly formed account name.
#
ERROR_INVALID_ACCOUNT_NAME = 1315

#
# MessageId: ERROR_USER_EXISTS
#
# MessageText:
#
# The specified account already exists.
#
ERROR_USER_EXISTS = 1316

#
# MessageId: ERROR_NO_SUCH_USER
#
# MessageText:
#
# The specified account does not exist.
#
ERROR_NO_SUCH_USER = 1317

#
# MessageId: ERROR_GROUP_EXISTS
#
# MessageText:
#
# The specified group already exists.
#
ERROR_GROUP_EXISTS = 1318

#
# MessageId: ERROR_NO_SUCH_GROUP
#
# MessageText:
#
# The specified group does not exist.
#
ERROR_NO_SUCH_GROUP = 1319

#
# MessageId: ERROR_MEMBER_IN_GROUP
#
# MessageText:
#
# Either the specified user account is already a member of the specified group, or the specified group cannot be deleted because it contains a member.
#
ERROR_MEMBER_IN_GROUP = 1320

#
# MessageId: ERROR_MEMBER_NOT_IN_GROUP
#
# MessageText:
#
# The specified user account is not a member of the specified group account.
#
ERROR_MEMBER_NOT_IN_GROUP = 1321

#
# MessageId: ERROR_LAST_ADMIN
#
# MessageText:
#
# This operation is disallowed as it could result in an administration account being disabled, deleted or unable to logon.
#
ERROR_LAST_ADMIN = 1322

#
# MessageId: ERROR_WRONG_PASSWORD
#
# MessageText:
#
# Unable to update the password. The value provided as the current password is incorrect.
#
ERROR_WRONG_PASSWORD = 1323

#
# MessageId: ERROR_ILL_FORMED_PASSWORD
#
# MessageText:
#
# Unable to update the password. The value provided for the new password contains values that are not allowed in passwords.
#
ERROR_ILL_FORMED_PASSWORD = 1324

#
# MessageId: ERROR_PASSWORD_RESTRICTION
#
# MessageText:
#
# Unable to update the password. The value provided for the new password does not meet the length, complexity, or history requirements of the domain.
#
ERROR_PASSWORD_RESTRICTION = 1325

#
# MessageId: ERROR_LOGON_FAILURE
#
# MessageText:
#
# The user name or password is incorrect.
#
ERROR_LOGON_FAILURE = 1326

#
# MessageId: ERROR_ACCOUNT_RESTRICTION
#
# MessageText:
#
# Account restrictions are preventing this user from signing in. For example: blank passwords aren't allowed, sign-in times are limited, or a policy restriction has been enforced.
#
ERROR_ACCOUNT_RESTRICTION = 1327

#
# MessageId: ERROR_INVALID_LOGON_HOURS
#
# MessageText:
#
# Your account has time restrictions that keep you from signing in right now.
#
ERROR_INVALID_LOGON_HOURS = 1328

#
# MessageId: ERROR_INVALID_WORKSTATION
#
# MessageText:
#
# This user isn't allowed to sign in to this computer.
#
ERROR_INVALID_WORKSTATION = 1329

#
# MessageId: ERROR_PASSWORD_EXPIRED
#
# MessageText:
#
# The password for this account has expired.
#
ERROR_PASSWORD_EXPIRED = 1330

#
# MessageId: ERROR_ACCOUNT_DISABLED
#
# MessageText:
#
# This user can't sign in because this account is currently disabled.
#
ERROR_ACCOUNT_DISABLED = 1331

#
# MessageId: ERROR_NONE_MAPPED
#
# MessageText:
#
# No mapping between account names and security IDs was done.
#
ERROR_NONE_MAPPED = 1332

#
# MessageId: ERROR_TOO_MANY_LUIDS_REQUESTED
#
# MessageText:
#
# Too many local user identifiers (LUIDs) were requested at one time.
#
ERROR_TOO_MANY_LUIDS_REQUESTED = 1333

#
# MessageId: ERROR_LUIDS_EXHAUSTED
#
# MessageText:
#
# No more local user identifiers (LUIDs) are available.
#
ERROR_LUIDS_EXHAUSTED = 1334

#
# MessageId: ERROR_INVALID_SUB_AUTHORITY
#
# MessageText:
#
# The subauthority part of a security ID is invalid for this particular use.
#
ERROR_INVALID_SUB_AUTHORITY = 1335

#
# MessageId: ERROR_INVALID_ACL
#
# MessageText:
#
# The access control list (ACL) structure is invalid.
#
ERROR_INVALID_ACL = 1336

#
# MessageId: ERROR_INVALID_SID
#
# MessageText:
#
# The security ID structure is invalid.
#
ERROR_INVALID_SID = 1337

#
# MessageId: ERROR_INVALID_SECURITY_DESCR
#
# MessageText:
#
# The security descriptor structure is invalid.
#
ERROR_INVALID_SECURITY_DESCR = 1338

#
# MessageId: ERROR_BAD_INHERITANCE_ACL
#
# MessageText:
#
# The inherited access control list (ACL) or access control entry (ACE) could not be built.
#
ERROR_BAD_INHERITANCE_ACL = 1340

#
# MessageId: ERROR_SERVER_DISABLED
#
# MessageText:
#
# The server is currently disabled.
#
ERROR_SERVER_DISABLED = 1341

#
# MessageId: ERROR_SERVER_NOT_DISABLED
#
# MessageText:
#
# The server is currently enabled.
#
ERROR_SERVER_NOT_DISABLED = 1342

#
# MessageId: ERROR_INVALID_ID_AUTHORITY
#
# MessageText:
#
# The value provided was an invalid value for an identifier authority.
#
ERROR_INVALID_ID_AUTHORITY = 1343

#
# MessageId: ERROR_ALLOTTED_SPACE_EXCEEDED
#
# MessageText:
#
# No more memory is available for security information updates.
#
ERROR_ALLOTTED_SPACE_EXCEEDED = 1344

#
# MessageId: ERROR_INVALID_GROUP_ATTRIBUTES
#
# MessageText:
#
# The specified attributes are invalid, or incompatible with the attributes for the group as a whole.
#
ERROR_INVALID_GROUP_ATTRIBUTES = 1345

#
# MessageId: ERROR_BAD_IMPERSONATION_LEVEL
#
# MessageText:
#
# Either a required impersonation level was not provided, or the provided impersonation level is invalid.
#
ERROR_BAD_IMPERSONATION_LEVEL = 1346

#
# MessageId: ERROR_CANT_OPEN_ANONYMOUS
#
# MessageText:
#
# Cannot open an anonymous level security token.
#
ERROR_CANT_OPEN_ANONYMOUS = 1347

#
# MessageId: ERROR_BAD_VALIDATION_CLASS
#
# MessageText:
#
# The validation information class requested was invalid.
#
ERROR_BAD_VALIDATION_CLASS = 1348

#
# MessageId: ERROR_BAD_TOKEN_TYPE
#
# MessageText:
#
# The type of the token is inappropriate for its attempted use.
#
ERROR_BAD_TOKEN_TYPE = 1349

#
# MessageId: ERROR_NO_SECURITY_ON_OBJECT
#
# MessageText:
#
# Unable to perform a security operation on an object that has no associated security.
#
ERROR_NO_SECURITY_ON_OBJECT = 1350

#
# MessageId: ERROR_CANT_ACCESS_DOMAIN_INFO
#
# MessageText:
#
# Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.
#
ERROR_CANT_ACCESS_DOMAIN_INFO = 1351

#
# MessageId: ERROR_INVALID_SERVER_STATE
#
# MessageText:
#
# The security account manager (SAM) or local security authority (LSA) server was in the wrong state to perform the security operation.
#
ERROR_INVALID_SERVER_STATE = 1352

#
# MessageId: ERROR_INVALID_DOMAIN_STATE
#
# MessageText:
#
# The domain was in the wrong state to perform the security operation.
#
ERROR_INVALID_DOMAIN_STATE = 1353

#
# MessageId: ERROR_INVALID_DOMAIN_ROLE
#
# MessageText:
#
# This operation is only allowed for the Primary Domain Controller of the domain.
#
ERROR_INVALID_DOMAIN_ROLE = 1354

#
# MessageId: ERROR_NO_SUCH_DOMAIN
#
# MessageText:
#
# The specified domain either does not exist or could not be contacted.
#
ERROR_NO_SUCH_DOMAIN = 1355

#
# MessageId: ERROR_DOMAIN_EXISTS
#
# MessageText:
#
# The specified domain already exists.
#
ERROR_DOMAIN_EXISTS = 1356

#
# MessageId: ERROR_DOMAIN_LIMIT_EXCEEDED
#
# MessageText:
#
# An attempt was made to exceed the limit on the number of domains per server.
#
ERROR_DOMAIN_LIMIT_EXCEEDED = 1357

#
# MessageId: ERROR_INTERNAL_DB_CORRUPTION
#
# MessageText:
#
# Unable to complete the requested operation because of either a catastrophic media failure or a data structure corruption on the disk.
#
ERROR_INTERNAL_DB_CORRUPTION = 1358

#
# MessageId: ERROR_INTERNAL_ERROR
#
# MessageText:
#
# An internal error occurred.
#
ERROR_INTERNAL_ERROR = 1359

#
# MessageId: ERROR_GENERIC_NOT_MAPPED
#
# MessageText:
#
# Generic access types were contained in an access mask which should already be mapped to nongeneric types.
#
ERROR_GENERIC_NOT_MAPPED = 1360

#
# MessageId: ERROR_BAD_DESCRIPTOR_FORMAT
#
# MessageText:
#
# A security descriptor is not in the right format (absolute or self-relative).
#
ERROR_BAD_DESCRIPTOR_FORMAT = 1361

#
# MessageId: ERROR_NOT_LOGON_PROCESS
#
# MessageText:
#
# The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.
#
ERROR_NOT_LOGON_PROCESS = 1362

#
# MessageId: ERROR_LOGON_SESSION_EXISTS
#
# MessageText:
#
# Cannot start a new logon session with an ID that is already in use.
#
ERROR_LOGON_SESSION_EXISTS = 1363

#
# MessageId: ERROR_NO_SUCH_PACKAGE
#
# MessageText:
#
# A specified authentication package is unknown.
#
ERROR_NO_SUCH_PACKAGE = 1364

#
# MessageId: ERROR_BAD_LOGON_SESSION_STATE
#
# MessageText:
#
# The logon session is not in a state that is consistent with the requested operation.
#
ERROR_BAD_LOGON_SESSION_STATE = 1365

#
# MessageId: ERROR_LOGON_SESSION_COLLISION
#
# MessageText:
#
# The logon session ID is already in use.
#
ERROR_LOGON_SESSION_COLLISION = 1366

#
# MessageId: ERROR_INVALID_LOGON_TYPE
#
# MessageText:
#
# A logon request contained an invalid logon type value.
#
ERROR_INVALID_LOGON_TYPE = 1367

#
# MessageId: ERROR_CANNOT_IMPERSONATE
#
# MessageText:
#
# Unable to impersonate using a named pipe until data has been read from that pipe.
#
ERROR_CANNOT_IMPERSONATE = 1368

#
# MessageId: ERROR_RXACT_INVALID_STATE
#
# MessageText:
#
# The transaction state of a registry subtree is incompatible with the requested operation.
#
ERROR_RXACT_INVALID_STATE = 1369

#
# MessageId: ERROR_RXACT_COMMIT_FAILURE
#
# MessageText:
#
# An internal security database corruption has been encountered.
#
ERROR_RXACT_COMMIT_FAILURE = 1370

#
# MessageId: ERROR_SPECIAL_ACCOUNT
#
# MessageText:
#
# Cannot perform this operation on built-in accounts.
#
ERROR_SPECIAL_ACCOUNT = 1371

#
# MessageId: ERROR_SPECIAL_GROUP
#
# MessageText:
#
# Cannot perform this operation on this built-in special group.
#
ERROR_SPECIAL_GROUP = 1372

#
# MessageId: ERROR_SPECIAL_USER
#
# MessageText:
#
# Cannot perform this operation on this built-in special user.
#
ERROR_SPECIAL_USER = 1373

#
# MessageId: ERROR_MEMBERS_PRIMARY_GROUP
#
# MessageText:
#
# The user cannot be removed from a group because the group is currently the user's primary group.
#
ERROR_MEMBERS_PRIMARY_GROUP = 1374

#
# MessageId: ERROR_TOKEN_ALREADY_IN_USE
#
# MessageText:
#
# The token is already in use as a primary token.
#
ERROR_TOKEN_ALREADY_IN_USE = 1375

#
# MessageId: ERROR_NO_SUCH_ALIAS
#
# MessageText:
#
# The specified local group does not exist.
#
ERROR_NO_SUCH_ALIAS = 1376

#
# MessageId: ERROR_MEMBER_NOT_IN_ALIAS
#
# MessageText:
#
# The specified account name is not a member of the group.
#
ERROR_MEMBER_NOT_IN_ALIAS = 1377

#
# MessageId: ERROR_MEMBER_IN_ALIAS
#
# MessageText:
#
# The specified account name is already a member of the group.
#
ERROR_MEMBER_IN_ALIAS = 1378

#
# MessageId: ERROR_ALIAS_EXISTS
#
# MessageText:
#
# The specified local group already exists.
#
ERROR_ALIAS_EXISTS = 1379

#
# MessageId: ERROR_LOGON_NOT_GRANTED
#
# MessageText:
#
# Logon failure: the user has not been granted the requested logon type at this computer.
#
ERROR_LOGON_NOT_GRANTED = 1380

#
# MessageId: ERROR_TOO_MANY_SECRETS
#
# MessageText:
#
# The maximum number of secrets that may be stored in a single system has been exceeded.
#
ERROR_TOO_MANY_SECRETS = 1381

#
# MessageId: ERROR_SECRET_TOO_LONG
#
# MessageText:
#
# The length of a secret exceeds the maximum length allowed.
#
ERROR_SECRET_TOO_LONG = 1382

#
# MessageId: ERROR_INTERNAL_DB_ERROR
#
# MessageText:
#
# The local security authority database contains an internal inconsistency.
#
ERROR_INTERNAL_DB_ERROR = 1383

#
# MessageId: ERROR_TOO_MANY_CONTEXT_IDS
#
# MessageText:
#
# During a logon attempt, the user's security context accumulated too many security IDs.
#
ERROR_TOO_MANY_CONTEXT_IDS = 1384

#
# MessageId: ERROR_LOGON_TYPE_NOT_GRANTED
#
# MessageText:
#
# Logon failure: the user has not been granted the requested logon type at this computer.
#
ERROR_LOGON_TYPE_NOT_GRANTED = 1385

#
# MessageId: ERROR_NT_CROSS_ENCRYPTION_REQUIRED
#
# MessageText:
#
# A cross-encrypted password is necessary to change a user password.
#
ERROR_NT_CROSS_ENCRYPTION_REQUIRED = 1386

#
# MessageId: ERROR_NO_SUCH_MEMBER
#
# MessageText:
#
# A member could not be added to or removed from the local group because the member does not exist.
#
ERROR_NO_SUCH_MEMBER = 1387

#
# MessageId: ERROR_INVALID_MEMBER
#
# MessageText:
#
# A new member could not be added to a local group because the member has the wrong account type.
#
ERROR_INVALID_MEMBER = 1388

#
# MessageId: ERROR_TOO_MANY_SIDS
#
# MessageText:
#
# Too many security IDs have been specified.
#
ERROR_TOO_MANY_SIDS = 1389

#
# MessageId: ERROR_LM_CROSS_ENCRYPTION_REQUIRED
#
# MessageText:
#
# A cross-encrypted password is necessary to change this user password.
#
ERROR_LM_CROSS_ENCRYPTION_REQUIRED = 1390

#
# MessageId: ERROR_NO_INHERITANCE
#
# MessageText:
#
# Indicates an ACL contains no inheritable components.
#
ERROR_NO_INHERITANCE = 1391

#
# MessageId: ERROR_FILE_CORRUPT
#
# MessageText:
#
# The file or directory is corrupted and unreadable.
#
ERROR_FILE_CORRUPT = 1392

#
# MessageId: ERROR_DISK_CORRUPT
#
# MessageText:
#
# The disk structure is corrupted and unreadable.
#
ERROR_DISK_CORRUPT = 1393

#
# MessageId: ERROR_NO_USER_SESSION_KEY
#
# MessageText:
#
# There is no user session key for the specified logon session.
#
ERROR_NO_USER_SESSION_KEY = 1394

#
# MessageId: ERROR_LICENSE_QUOTA_EXCEEDED
#
# MessageText:
#
# The service being accessed is licensed for a particular number of connections. No more connections can be made to the service at this time because there are already as many connections as the service can accept.
#
ERROR_LICENSE_QUOTA_EXCEEDED = 1395

#
# MessageId: ERROR_WRONG_TARGET_NAME
#
# MessageText:
#
# The target account name is incorrect.
#
ERROR_WRONG_TARGET_NAME = 1396

#
# MessageId: ERROR_MUTUAL_AUTH_FAILED
#
# MessageText:
#
# Mutual Authentication failed. The server's password is out of date at the domain controller.
#
ERROR_MUTUAL_AUTH_FAILED = 1397

#
# MessageId: ERROR_TIME_SKEW
#
# MessageText:
#
# There is a time and/or date difference between the client and server.
#
ERROR_TIME_SKEW = 1398

#
# MessageId: ERROR_CURRENT_DOMAIN_NOT_ALLOWED
#
# MessageText:
#
# This operation cannot be performed on the current domain.
#
ERROR_CURRENT_DOMAIN_NOT_ALLOWED = 1399


#/////////////////////////////////////////////////
#                                               //
#              WinUser Error codes              //
#                                               //
#                 1400 to 1499                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INVALID_WINDOW_HANDLE
#
# MessageText:
#
# Invalid window handle.
#
ERROR_INVALID_WINDOW_HANDLE = 1400

#
# MessageId: ERROR_INVALID_MENU_HANDLE
#
# MessageText:
#
# Invalid menu handle.
#
ERROR_INVALID_MENU_HANDLE = 1401

#
# MessageId: ERROR_INVALID_CURSOR_HANDLE
#
# MessageText:
#
# Invalid cursor handle.
#
ERROR_INVALID_CURSOR_HANDLE = 1402

#
# MessageId: ERROR_INVALID_ACCEL_HANDLE
#
# MessageText:
#
# Invalid accelerator table handle.
#
ERROR_INVALID_ACCEL_HANDLE = 1403

#
# MessageId: ERROR_INVALID_HOOK_HANDLE
#
# MessageText:
#
# Invalid hook handle.
#
ERROR_INVALID_HOOK_HANDLE = 1404

#
# MessageId: ERROR_INVALID_DWP_HANDLE
#
# MessageText:
#
# Invalid handle to a multiple-window position structure.
#
ERROR_INVALID_DWP_HANDLE = 1405

#
# MessageId: ERROR_TLW_WITH_WSCHILD
#
# MessageText:
#
# Cannot create a top-level child window.
#
ERROR_TLW_WITH_WSCHILD = 1406

#
# MessageId: ERROR_CANNOT_FIND_WND_CLASS
#
# MessageText:
#
# Cannot find window class.
#
ERROR_CANNOT_FIND_WND_CLASS = 1407

#
# MessageId: ERROR_WINDOW_OF_OTHER_THREAD
#
# MessageText:
#
# Invalid window; it belongs to other thread.
#
ERROR_WINDOW_OF_OTHER_THREAD = 1408

#
# MessageId: ERROR_HOTKEY_ALREADY_REGISTERED
#
# MessageText:
#
# Hot key is already registered.
#
ERROR_HOTKEY_ALREADY_REGISTERED = 1409

#
# MessageId: ERROR_CLASS_ALREADY_EXISTS
#
# MessageText:
#
# Class already exists.
#
ERROR_CLASS_ALREADY_EXISTS = 1410

#
# MessageId: ERROR_CLASS_DOES_NOT_EXIST
#
# MessageText:
#
# Class does not exist.
#
ERROR_CLASS_DOES_NOT_EXIST = 1411

#
# MessageId: ERROR_CLASS_HAS_WINDOWS
#
# MessageText:
#
# Class still has open windows.
#
ERROR_CLASS_HAS_WINDOWS = 1412

#
# MessageId: ERROR_INVALID_INDEX
#
# MessageText:
#
# Invalid index.
#
ERROR_INVALID_INDEX = 1413

#
# MessageId: ERROR_INVALID_ICON_HANDLE
#
# MessageText:
#
# Invalid icon handle.
#
ERROR_INVALID_ICON_HANDLE = 1414

#
# MessageId: ERROR_PRIVATE_DIALOG_INDEX
#
# MessageText:
#
# Using private DIALOG window words.
#
ERROR_PRIVATE_DIALOG_INDEX = 1415

#
# MessageId: ERROR_LISTBOX_ID_NOT_FOUND
#
# MessageText:
#
# The list box identifier was not found.
#
ERROR_LISTBOX_ID_NOT_FOUND = 1416

#
# MessageId: ERROR_NO_WILDCARD_CHARACTERS
#
# MessageText:
#
# No wildcards were found.
#
ERROR_NO_WILDCARD_CHARACTERS = 1417

#
# MessageId: ERROR_CLIPBOARD_NOT_OPEN
#
# MessageText:
#
# Thread does not have a clipboard open.
#
ERROR_CLIPBOARD_NOT_OPEN = 1418

#
# MessageId: ERROR_HOTKEY_NOT_REGISTERED
#
# MessageText:
#
# Hot key is not registered.
#
ERROR_HOTKEY_NOT_REGISTERED = 1419

#
# MessageId: ERROR_WINDOW_NOT_DIALOG
#
# MessageText:
#
# The window is not a valid dialog window.
#
ERROR_WINDOW_NOT_DIALOG = 1420

#
# MessageId: ERROR_CONTROL_ID_NOT_FOUND
#
# MessageText:
#
# Control ID not found.
#
ERROR_CONTROL_ID_NOT_FOUND = 1421

#
# MessageId: ERROR_INVALID_COMBOBOX_MESSAGE
#
# MessageText:
#
# Invalid message for a combo box because it does not have an edit control.
#
ERROR_INVALID_COMBOBOX_MESSAGE = 1422

#
# MessageId: ERROR_WINDOW_NOT_COMBOBOX
#
# MessageText:
#
# The window is not a combo box.
#
ERROR_WINDOW_NOT_COMBOBOX = 1423

#
# MessageId: ERROR_INVALID_EDIT_HEIGHT
#
# MessageText:
#
# Height must be less than 256.
#
ERROR_INVALID_EDIT_HEIGHT = 1424

#
# MessageId: ERROR_DC_NOT_FOUND
#
# MessageText:
#
# Invalid device context (DC) handle.
#
ERROR_DC_NOT_FOUND = 1425

#
# MessageId: ERROR_INVALID_HOOK_FILTER
#
# MessageText:
#
# Invalid hook procedure type.
#
ERROR_INVALID_HOOK_FILTER = 1426

#
# MessageId: ERROR_INVALID_FILTER_PROC
#
# MessageText:
#
# Invalid hook procedure.
#
ERROR_INVALID_FILTER_PROC = 1427

#
# MessageId: ERROR_HOOK_NEEDS_HMOD
#
# MessageText:
#
# Cannot set nonlocal hook without a module handle.
#
ERROR_HOOK_NEEDS_HMOD = 1428

#
# MessageId: ERROR_GLOBAL_ONLY_HOOK
#
# MessageText:
#
# This hook procedure can only be set globally.
#
ERROR_GLOBAL_ONLY_HOOK = 1429

#
# MessageId: ERROR_JOURNAL_HOOK_SET
#
# MessageText:
#
# The journal hook procedure is already installed.
#
ERROR_JOURNAL_HOOK_SET = 1430

#
# MessageId: ERROR_HOOK_NOT_INSTALLED
#
# MessageText:
#
# The hook procedure is not installed.
#
ERROR_HOOK_NOT_INSTALLED = 1431

#
# MessageId: ERROR_INVALID_LB_MESSAGE
#
# MessageText:
#
# Invalid message for single-selection list box.
#
ERROR_INVALID_LB_MESSAGE = 1432

#
# MessageId: ERROR_SETCOUNT_ON_BAD_LB
#
# MessageText:
#
# LB_SETCOUNT sent to non-lazy list box.
#
ERROR_SETCOUNT_ON_BAD_LB = 1433

#
# MessageId: ERROR_LB_WITHOUT_TABSTOPS
#
# MessageText:
#
# This list box does not support tab stops.
#
ERROR_LB_WITHOUT_TABSTOPS = 1434

#
# MessageId: ERROR_DESTROY_OBJECT_OF_OTHER_THREAD
#
# MessageText:
#
# Cannot destroy object created by another thread.
#
ERROR_DESTROY_OBJECT_OF_OTHER_THREAD = 1435

#
# MessageId: ERROR_CHILD_WINDOW_MENU
#
# MessageText:
#
# Child windows cannot have menus.
#
ERROR_CHILD_WINDOW_MENU = 1436

#
# MessageId: ERROR_NO_SYSTEM_MENU
#
# MessageText:
#
# The window does not have a system menu.
#
ERROR_NO_SYSTEM_MENU = 1437

#
# MessageId: ERROR_INVALID_MSGBOX_STYLE
#
# MessageText:
#
# Invalid message box style.
#
ERROR_INVALID_MSGBOX_STYLE = 1438

#
# MessageId: ERROR_INVALID_SPI_VALUE
#
# MessageText:
#
# Invalid system-wide (SPI_*) parameter.
#
ERROR_INVALID_SPI_VALUE = 1439

#
# MessageId: ERROR_SCREEN_ALREADY_LOCKED
#
# MessageText:
#
# Screen already locked.
#
ERROR_SCREEN_ALREADY_LOCKED = 1440

#
# MessageId: ERROR_HWNDS_HAVE_DIFF_PARENT
#
# MessageText:
#
# All handles to windows in a multiple-window position structure must have the same parent.
#
ERROR_HWNDS_HAVE_DIFF_PARENT = 1441

#
# MessageId: ERROR_NOT_CHILD_WINDOW
#
# MessageText:
#
# The window is not a child window.
#
ERROR_NOT_CHILD_WINDOW = 1442

#
# MessageId: ERROR_INVALID_GW_COMMAND
#
# MessageText:
#
# Invalid GW_* command.
#
ERROR_INVALID_GW_COMMAND = 1443

#
# MessageId: ERROR_INVALID_THREAD_ID
#
# MessageText:
#
# Invalid thread identifier.
#
ERROR_INVALID_THREAD_ID = 1444

#
# MessageId: ERROR_NON_MDICHILD_WINDOW
#
# MessageText:
#
# Cannot process a message from a window that is not a multiple document interface (MDI) window.
#
ERROR_NON_MDICHILD_WINDOW = 1445

#
# MessageId: ERROR_POPUP_ALREADY_ACTIVE
#
# MessageText:
#
# Popup menu already active.
#
ERROR_POPUP_ALREADY_ACTIVE = 1446

#
# MessageId: ERROR_NO_SCROLLBARS
#
# MessageText:
#
# The window does not have scroll bars.
#
ERROR_NO_SCROLLBARS = 1447

#
# MessageId: ERROR_INVALID_SCROLLBAR_RANGE
#
# MessageText:
#
# Scroll bar range cannot be greater than MAXLONG.
#
ERROR_INVALID_SCROLLBAR_RANGE = 1448

#
# MessageId: ERROR_INVALID_SHOWWIN_COMMAND
#
# MessageText:
#
# Cannot show or remove the window in the way specified.
#
ERROR_INVALID_SHOWWIN_COMMAND = 1449

#
# MessageId: ERROR_NO_SYSTEM_RESOURCES
#
# MessageText:
#
# Insufficient system resources exist to complete the requested service.
#
ERROR_NO_SYSTEM_RESOURCES = 1450

#
# MessageId: ERROR_NONPAGED_SYSTEM_RESOURCES
#
# MessageText:
#
# Insufficient system resources exist to complete the requested service.
#
ERROR_NONPAGED_SYSTEM_RESOURCES = 1451

#
# MessageId: ERROR_PAGED_SYSTEM_RESOURCES
#
# MessageText:
#
# Insufficient system resources exist to complete the requested service.
#
ERROR_PAGED_SYSTEM_RESOURCES = 1452

#
# MessageId: ERROR_WORKING_SET_QUOTA
#
# MessageText:
#
# Insufficient quota to complete the requested service.
#
ERROR_WORKING_SET_QUOTA = 1453

#
# MessageId: ERROR_PAGEFILE_QUOTA
#
# MessageText:
#
# Insufficient quota to complete the requested service.
#
ERROR_PAGEFILE_QUOTA = 1454

#
# MessageId: ERROR_COMMITMENT_LIMIT
#
# MessageText:
#
# The paging file is too small for this operation to complete.
#
ERROR_COMMITMENT_LIMIT = 1455

#
# MessageId: ERROR_MENU_ITEM_NOT_FOUND
#
# MessageText:
#
# A menu item was not found.
#
ERROR_MENU_ITEM_NOT_FOUND = 1456

#
# MessageId: ERROR_INVALID_KEYBOARD_HANDLE
#
# MessageText:
#
# Invalid keyboard layout handle.
#
ERROR_INVALID_KEYBOARD_HANDLE = 1457

#
# MessageId: ERROR_HOOK_TYPE_NOT_ALLOWED
#
# MessageText:
#
# Hook type not allowed.
#
ERROR_HOOK_TYPE_NOT_ALLOWED = 1458

#
# MessageId: ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION
#
# MessageText:
#
# This operation requires an interactive window station.
#
ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION = 1459

#
# MessageId: ERROR_TIMEOUT
#
# MessageText:
#
# This operation returned because the timeout period expired.
#
ERROR_TIMEOUT = 1460

#
# MessageId: ERROR_INVALID_MONITOR_HANDLE
#
# MessageText:
#
# Invalid monitor handle.
#
ERROR_INVALID_MONITOR_HANDLE = 1461

#
# MessageId: ERROR_INCORRECT_SIZE
#
# MessageText:
#
# Incorrect size argument.
#
ERROR_INCORRECT_SIZE = 1462

#
# MessageId: ERROR_SYMLINK_CLASS_DISABLED
#
# MessageText:
#
# The symbolic link cannot be followed because its type is disabled.
#
ERROR_SYMLINK_CLASS_DISABLED = 1463

#
# MessageId: ERROR_SYMLINK_NOT_SUPPORTED
#
# MessageText:
#
# This application does not support the current operation on symbolic links.
#
ERROR_SYMLINK_NOT_SUPPORTED = 1464

#
# MessageId: ERROR_XML_PARSE_ERROR
#
# MessageText:
#
# Windows was unable to parse the requested XML data.
#
ERROR_XML_PARSE_ERROR = 1465

#
# MessageId: ERROR_XMLDSIG_ERROR
#
# MessageText:
#
# An error was encountered while processing an XML digital signature.
#
ERROR_XMLDSIG_ERROR = 1466

#
# MessageId: ERROR_RESTART_APPLICATION
#
# MessageText:
#
# This application must be restarted.
#
ERROR_RESTART_APPLICATION = 1467

#
# MessageId: ERROR_WRONG_COMPARTMENT
#
# MessageText:
#
# The caller made the connection request in the wrong routing compartment.
#
ERROR_WRONG_COMPARTMENT = 1468

#
# MessageId: ERROR_AUTHIP_FAILURE
#
# MessageText:
#
# There was an AuthIP failure when attempting to connect to the remote host.
#
ERROR_AUTHIP_FAILURE = 1469

#
# MessageId: ERROR_NO_NVRAM_RESOURCES
#
# MessageText:
#
# Insufficient NVRAM resources exist to complete the requested service. A reboot might be required.
#
ERROR_NO_NVRAM_RESOURCES = 1470

#
# MessageId: ERROR_NOT_GUI_PROCESS
#
# MessageText:
#
# Unable to finish the requested operation because the specified process is not a GUI process.
#
ERROR_NOT_GUI_PROCESS = 1471


#/////////////////////////////////////////////////
#                                               //
#             EventLog Error codes              //
#                                               //
#                 1500 to 1549                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_EVENTLOG_FILE_CORRUPT
#
# MessageText:
#
# The event log file is corrupted.
#
ERROR_EVENTLOG_FILE_CORRUPT = 1500

#
# MessageId: ERROR_EVENTLOG_CANT_START
#
# MessageText:
#
# No event log file could be opened, so the event logging service did not start.
#
ERROR_EVENTLOG_CANT_START = 1501

#
# MessageId: ERROR_LOG_FILE_FULL
#
# MessageText:
#
# The event log file is full.
#
ERROR_LOG_FILE_FULL = 1502

#
# MessageId: ERROR_EVENTLOG_FILE_CHANGED
#
# MessageText:
#
# The event log file has changed between read operations.
#
ERROR_EVENTLOG_FILE_CHANGED = 1503


#/////////////////////////////////////////////////
#                                               //
#            Class Scheduler Error codes        //
#                                               //
#                 1550 to 1599                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INVALID_TASK_NAME
#
# MessageText:
#
# The specified task name is invalid.
#
ERROR_INVALID_TASK_NAME = 1550

#
# MessageId: ERROR_INVALID_TASK_INDEX
#
# MessageText:
#
# The specified task index is invalid.
#
ERROR_INVALID_TASK_INDEX = 1551

#
# MessageId: ERROR_THREAD_ALREADY_IN_TASK
#
# MessageText:
#
# The specified thread is already joining a task.
#
ERROR_THREAD_ALREADY_IN_TASK = 1552


#/////////////////////////////////////////////////
#                                               //
#                MSI Error codes                //
#                                               //
#                 1600 to 1699                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INSTALL_SERVICE_FAILURE
#
# MessageText:
#
# The Windows Installer Service could not be accessed. This can occur if the Windows Installer is not correctly installed. Contact your support personnel for assistance.
#
ERROR_INSTALL_SERVICE_FAILURE = 1601

#
# MessageId: ERROR_INSTALL_USEREXIT
#
# MessageText:
#
# User cancelled installation.
#
ERROR_INSTALL_USEREXIT = 1602

#
# MessageId: ERROR_INSTALL_FAILURE
#
# MessageText:
#
# Fatal error during installation.
#
ERROR_INSTALL_FAILURE = 1603

#
# MessageId: ERROR_INSTALL_SUSPEND
#
# MessageText:
#
# Installation suspended, incomplete.
#
ERROR_INSTALL_SUSPEND = 1604

#
# MessageId: ERROR_UNKNOWN_PRODUCT
#
# MessageText:
#
# This action is only valid for products that are currently installed.
#
ERROR_UNKNOWN_PRODUCT = 1605

#
# MessageId: ERROR_UNKNOWN_FEATURE
#
# MessageText:
#
# Feature ID not registered.
#
ERROR_UNKNOWN_FEATURE = 1606

#
# MessageId: ERROR_UNKNOWN_COMPONENT
#
# MessageText:
#
# Component ID not registered.
#
ERROR_UNKNOWN_COMPONENT = 1607

#
# MessageId: ERROR_UNKNOWN_PROPERTY
#
# MessageText:
#
# Unknown property.
#
ERROR_UNKNOWN_PROPERTY = 1608

#
# MessageId: ERROR_INVALID_HANDLE_STATE
#
# MessageText:
#
# Handle is in an invalid state.
#
ERROR_INVALID_HANDLE_STATE = 1609

#
# MessageId: ERROR_BAD_CONFIGURATION
#
# MessageText:
#
# The configuration data for this product is corrupt. Contact your support personnel.
#
ERROR_BAD_CONFIGURATION = 1610

#
# MessageId: ERROR_INDEX_ABSENT
#
# MessageText:
#
# Component qualifier not present.
#
ERROR_INDEX_ABSENT = 1611

#
# MessageId: ERROR_INSTALL_SOURCE_ABSENT
#
# MessageText:
#
# The installation source for this product is not available. Verify that the source exists and that you can access it.
#
ERROR_INSTALL_SOURCE_ABSENT = 1612

#
# MessageId: ERROR_INSTALL_PACKAGE_VERSION
#
# MessageText:
#
# This installation package cannot be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.
#
ERROR_INSTALL_PACKAGE_VERSION = 1613

#
# MessageId: ERROR_PRODUCT_UNINSTALLED
#
# MessageText:
#
# Product is uninstalled.
#
ERROR_PRODUCT_UNINSTALLED = 1614

#
# MessageId: ERROR_BAD_QUERY_SYNTAX
#
# MessageText:
#
# SQL query syntax invalid or unsupported.
#
ERROR_BAD_QUERY_SYNTAX = 1615

#
# MessageId: ERROR_INVALID_FIELD
#
# MessageText:
#
# Record field does not exist.
#
ERROR_INVALID_FIELD = 1616

#
# MessageId: ERROR_DEVICE_REMOVED
#
# MessageText:
#
# The device has been removed.
#
ERROR_DEVICE_REMOVED = 1617

#
# MessageId: ERROR_INSTALL_ALREADY_RUNNING
#
# MessageText:
#
# Another installation is already in progress. Complete that installation before proceeding with this install.
#
ERROR_INSTALL_ALREADY_RUNNING = 1618

#
# MessageId: ERROR_INSTALL_PACKAGE_OPEN_FAILED
#
# MessageText:
#
# This installation package could not be opened. Verify that the package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer package.
#
ERROR_INSTALL_PACKAGE_OPEN_FAILED = 1619

#
# MessageId: ERROR_INSTALL_PACKAGE_INVALID
#
# MessageText:
#
# This installation package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer package.
#
ERROR_INSTALL_PACKAGE_INVALID = 1620

#
# MessageId: ERROR_INSTALL_UI_FAILURE
#
# MessageText:
#
# There was an error starting the Windows Installer service user interface. Contact your support personnel.
#
ERROR_INSTALL_UI_FAILURE = 1621

#
# MessageId: ERROR_INSTALL_LOG_FAILURE
#
# MessageText:
#
# Error opening installation log file. Verify that the specified log file location exists and that you can write to it.
#
ERROR_INSTALL_LOG_FAILURE = 1622

#
# MessageId: ERROR_INSTALL_LANGUAGE_UNSUPPORTED
#
# MessageText:
#
# The language of this installation package is not supported by your system.
#
ERROR_INSTALL_LANGUAGE_UNSUPPORTED = 1623

#
# MessageId: ERROR_INSTALL_TRANSFORM_FAILURE
#
# MessageText:
#
# Error applying transforms. Verify that the specified transform paths are valid.
#
ERROR_INSTALL_TRANSFORM_FAILURE = 1624

#
# MessageId: ERROR_INSTALL_PACKAGE_REJECTED
#
# MessageText:
#
# This installation is forbidden by system policy. Contact your system administrator.
#
ERROR_INSTALL_PACKAGE_REJECTED = 1625

#
# MessageId: ERROR_FUNCTION_NOT_CALLED
#
# MessageText:
#
# Function could not be executed.
#
ERROR_FUNCTION_NOT_CALLED = 1626

#
# MessageId: ERROR_FUNCTION_FAILED
#
# MessageText:
#
# Function failed during execution.
#
ERROR_FUNCTION_FAILED = 1627

#
# MessageId: ERROR_INVALID_TABLE
#
# MessageText:
#
# Invalid or unknown table specified.
#
ERROR_INVALID_TABLE = 1628

#
# MessageId: ERROR_DATATYPE_MISMATCH
#
# MessageText:
#
# Data supplied is of wrong type.
#
ERROR_DATATYPE_MISMATCH = 1629

#
# MessageId: ERROR_UNSUPPORTED_TYPE
#
# MessageText:
#
# Data of this type is not supported.
#
ERROR_UNSUPPORTED_TYPE = 1630

#
# MessageId: ERROR_CREATE_FAILED
#
# MessageText:
#
# The Windows Installer service failed to start. Contact your support personnel.
#
ERROR_CREATE_FAILED = 1631

#
# MessageId: ERROR_INSTALL_TEMP_UNWRITABLE
#
# MessageText:
#
# The Temp folder is on a drive that is full or is inaccessible. Free up space on the drive or verify that you have write permission on the Temp folder.
#
ERROR_INSTALL_TEMP_UNWRITABLE = 1632

#
# MessageId: ERROR_INSTALL_PLATFORM_UNSUPPORTED
#
# MessageText:
#
# This installation package is not supported by this processor type. Contact your product vendor.
#
ERROR_INSTALL_PLATFORM_UNSUPPORTED = 1633

#
# MessageId: ERROR_INSTALL_NOTUSED
#
# MessageText:
#
# Component not used on this computer.
#
ERROR_INSTALL_NOTUSED = 1634

#
# MessageId: ERROR_PATCH_PACKAGE_OPEN_FAILED
#
# MessageText:
#
# This update package could not be opened. Verify that the update package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer update package.
#
ERROR_PATCH_PACKAGE_OPEN_FAILED = 1635

#
# MessageId: ERROR_PATCH_PACKAGE_INVALID
#
# MessageText:
#
# This update package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer update package.
#
ERROR_PATCH_PACKAGE_INVALID = 1636

#
# MessageId: ERROR_PATCH_PACKAGE_UNSUPPORTED
#
# MessageText:
#
# This update package cannot be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.
#
ERROR_PATCH_PACKAGE_UNSUPPORTED = 1637

#
# MessageId: ERROR_PRODUCT_VERSION
#
# MessageText:
#
# Another version of this product is already installed. Installation of this version cannot continue. To configure or remove the existing version of this product, use Add/Remove Programs on the Control Panel.
#
ERROR_PRODUCT_VERSION = 1638

#
# MessageId: ERROR_INVALID_COMMAND_LINE
#
# MessageText:
#
# Invalid command line argument. Consult the Windows Installer SDK for detailed command line help.
#
ERROR_INVALID_COMMAND_LINE = 1639

#
# MessageId: ERROR_INSTALL_REMOTE_DISALLOWED
#
# MessageText:
#
# Only administrators have permission to add, remove, or configure server software during a Terminal services remote session. If you want to install or configure software on the server, contact your network administrator.
#
ERROR_INSTALL_REMOTE_DISALLOWED = 1640

#
# MessageId: ERROR_SUCCESS_REBOOT_INITIATED
#
# MessageText:
#
# The requested operation completed successfully. The system will be restarted so the changes can take effect.
#
ERROR_SUCCESS_REBOOT_INITIATED = 1641

#
# MessageId: ERROR_PATCH_TARGET_NOT_FOUND
#
# MessageText:
#
# The upgrade cannot be installed by the Windows Installer service because the program to be upgraded may be missing, or the upgrade may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade.
#
ERROR_PATCH_TARGET_NOT_FOUND = 1642

#
# MessageId: ERROR_PATCH_PACKAGE_REJECTED
#
# MessageText:
#
# The update package is not permitted by software restriction policy.
#
ERROR_PATCH_PACKAGE_REJECTED = 1643

#
# MessageId: ERROR_INSTALL_TRANSFORM_REJECTED
#
# MessageText:
#
# One or more customizations are not permitted by software restriction policy.
#
ERROR_INSTALL_TRANSFORM_REJECTED = 1644

#
# MessageId: ERROR_INSTALL_REMOTE_PROHIBITED
#
# MessageText:
#
# The Windows Installer does not permit installation from a Remote Desktop Connection.
#
ERROR_INSTALL_REMOTE_PROHIBITED = 1645

#
# MessageId: ERROR_PATCH_REMOVAL_UNSUPPORTED
#
# MessageText:
#
# Uninstallation of the update package is not supported.
#
ERROR_PATCH_REMOVAL_UNSUPPORTED = 1646

#
# MessageId: ERROR_UNKNOWN_PATCH
#
# MessageText:
#
# The update is not applied to this product.
#
ERROR_UNKNOWN_PATCH = 1647

#
# MessageId: ERROR_PATCH_NO_SEQUENCE
#
# MessageText:
#
# No valid sequence could be found for the set of updates.
#
ERROR_PATCH_NO_SEQUENCE = 1648

#
# MessageId: ERROR_PATCH_REMOVAL_DISALLOWED
#
# MessageText:
#
# Update removal was disallowed by policy.
#
ERROR_PATCH_REMOVAL_DISALLOWED = 1649

#
# MessageId: ERROR_INVALID_PATCH_XML
#
# MessageText:
#
# The XML update data is invalid.
#
ERROR_INVALID_PATCH_XML = 1650

#
# MessageId: ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT
#
# MessageText:
#
# Windows Installer does not permit updating of managed advertised products. At least one feature of the product must be installed before applying the update.
#
ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT = 1651

#
# MessageId: ERROR_INSTALL_SERVICE_SAFEBOOT
#
# MessageText:
#
# The Windows Installer service is not accessible in Safe Mode. Please try again when your computer is not in Safe Mode or you can use System Restore to return your machine to a previous good state.
#
ERROR_INSTALL_SERVICE_SAFEBOOT = 1652

#
# MessageId: ERROR_FAIL_FAST_EXCEPTION
#
# MessageText:
#
# A fail fast exception occurred. Exception handlers will not be invoked and the process will be terminated immediately.
#
ERROR_FAIL_FAST_EXCEPTION = 1653

#
# MessageId: ERROR_INSTALL_REJECTED
#
# MessageText:
#
# The app that you are trying to run is not supported on this version of Windows.
#
ERROR_INSTALL_REJECTED = 1654

#
# MessageId: ERROR_DYNAMIC_CODE_BLOCKED
#
# MessageText:
#
# The operation was blocked as the process prohibits dynamic code generation.
#
ERROR_DYNAMIC_CODE_BLOCKED = 1655


#/////////////////////////////////////////////////
#                                               //
#               RPC Error codes                 //
#                                               //
#                 1700 to 1999                  //
#/////////////////////////////////////////////////

#
# MessageId: RPC_S_INVALID_STRING_BINDING
#
# MessageText:
#
# The string binding is invalid.
#
RPC_S_INVALID_STRING_BINDING = 1700

#
# MessageId: RPC_S_WRONG_KIND_OF_BINDING
#
# MessageText:
#
# The binding handle is not the correct type.
#
RPC_S_WRONG_KIND_OF_BINDING = 1701

#
# MessageId: RPC_S_INVALID_BINDING
#
# MessageText:
#
# The binding handle is invalid.
#
RPC_S_INVALID_BINDING = 1702

#
# MessageId: RPC_S_PROTSEQ_NOT_SUPPORTED
#
# MessageText:
#
# The RPC protocol sequence is not supported.
#
RPC_S_PROTSEQ_NOT_SUPPORTED = 1703

#
# MessageId: RPC_S_INVALID_RPC_PROTSEQ
#
# MessageText:
#
# The RPC protocol sequence is invalid.
#
RPC_S_INVALID_RPC_PROTSEQ = 1704

#
# MessageId: RPC_S_INVALID_STRING_UUID
#
# MessageText:
#
# The string universal unique identifier (UUID) is invalid.
#
RPC_S_INVALID_STRING_UUID = 1705

#
# MessageId: RPC_S_INVALID_ENDPOINT_FORMAT
#
# MessageText:
#
# The endpoint format is invalid.
#
RPC_S_INVALID_ENDPOINT_FORMAT = 1706

#
# MessageId: RPC_S_INVALID_NET_ADDR
#
# MessageText:
#
# The network address is invalid.
#
RPC_S_INVALID_NET_ADDR = 1707

#
# MessageId: RPC_S_NO_ENDPOINT_FOUND
#
# MessageText:
#
# No endpoint was found.
#
RPC_S_NO_ENDPOINT_FOUND = 1708

#
# MessageId: RPC_S_INVALID_TIMEOUT
#
# MessageText:
#
# The timeout value is invalid.
#
RPC_S_INVALID_TIMEOUT = 1709

#
# MessageId: RPC_S_OBJECT_NOT_FOUND
#
# MessageText:
#
# The object universal unique identifier (UUID) was not found.
#
RPC_S_OBJECT_NOT_FOUND = 1710

#
# MessageId: RPC_S_ALREADY_REGISTERED
#
# MessageText:
#
# The object universal unique identifier (UUID) has already been registered.
#
RPC_S_ALREADY_REGISTERED = 1711

#
# MessageId: RPC_S_TYPE_ALREADY_REGISTERED
#
# MessageText:
#
# The type universal unique identifier (UUID) has already been registered.
#
RPC_S_TYPE_ALREADY_REGISTERED = 1712

#
# MessageId: RPC_S_ALREADY_LISTENING
#
# MessageText:
#
# The RPC server is already listening.
#
RPC_S_ALREADY_LISTENING = 1713

#
# MessageId: RPC_S_NO_PROTSEQS_REGISTERED
#
# MessageText:
#
# No protocol sequences have been registered.
#
RPC_S_NO_PROTSEQS_REGISTERED = 1714

#
# MessageId: RPC_S_NOT_LISTENING
#
# MessageText:
#
# The RPC server is not listening.
#
RPC_S_NOT_LISTENING = 1715

#
# MessageId: RPC_S_UNKNOWN_MGR_TYPE
#
# MessageText:
#
# The manager type is unknown.
#
RPC_S_UNKNOWN_MGR_TYPE = 1716

#
# MessageId: RPC_S_UNKNOWN_IF
#
# MessageText:
#
# The interface is unknown.
#
RPC_S_UNKNOWN_IF = 1717

#
# MessageId: RPC_S_NO_BINDINGS
#
# MessageText:
#
# There are no bindings.
#
RPC_S_NO_BINDINGS = 1718

#
# MessageId: RPC_S_NO_PROTSEQS
#
# MessageText:
#
# There are no protocol sequences.
#
RPC_S_NO_PROTSEQS = 1719

#
# MessageId: RPC_S_CANT_CREATE_ENDPOINT
#
# MessageText:
#
# The endpoint cannot be created.
#
RPC_S_CANT_CREATE_ENDPOINT = 1720

#
# MessageId: RPC_S_OUT_OF_RESOURCES
#
# MessageText:
#
# Not enough resources are available to complete this operation.
#
RPC_S_OUT_OF_RESOURCES = 1721

#
# MessageId: RPC_S_SERVER_UNAVAILABLE
#
# MessageText:
#
# The RPC server is unavailable.
#
RPC_S_SERVER_UNAVAILABLE = 1722

#
# MessageId: RPC_S_SERVER_TOO_BUSY
#
# MessageText:
#
# The RPC server is too busy to complete this operation.
#
RPC_S_SERVER_TOO_BUSY = 1723

#
# MessageId: RPC_S_INVALID_NETWORK_OPTIONS
#
# MessageText:
#
# The network options are invalid.
#
RPC_S_INVALID_NETWORK_OPTIONS = 1724

#
# MessageId: RPC_S_NO_CALL_ACTIVE
#
# MessageText:
#
# There are no remote procedure calls active on this thread.
#
RPC_S_NO_CALL_ACTIVE = 1725

#
# MessageId: RPC_S_CALL_FAILED
#
# MessageText:
#
# The remote procedure call failed.
#
RPC_S_CALL_FAILED = 1726

#
# MessageId: RPC_S_CALL_FAILED_DNE
#
# MessageText:
#
# The remote procedure call failed and did not execute.
#
RPC_S_CALL_FAILED_DNE = 1727

#
# MessageId: RPC_S_PROTOCOL_ERROR
#
# MessageText:
#
# A remote procedure call (RPC) protocol error occurred.
#
RPC_S_PROTOCOL_ERROR = 1728

#
# MessageId: RPC_S_PROXY_ACCESS_DENIED
#
# MessageText:
#
# Access to the HTTP proxy is denied.
#
RPC_S_PROXY_ACCESS_DENIED = 1729

#
# MessageId: RPC_S_UNSUPPORTED_TRANS_SYN
#
# MessageText:
#
# The transfer syntax is not supported by the RPC server.
#
RPC_S_UNSUPPORTED_TRANS_SYN = 1730

#
# MessageId: RPC_S_UNSUPPORTED_TYPE
#
# MessageText:
#
# The universal unique identifier (UUID) type is not supported.
#
RPC_S_UNSUPPORTED_TYPE = 1732

#
# MessageId: RPC_S_INVALID_TAG
#
# MessageText:
#
# The tag is invalid.
#
RPC_S_INVALID_TAG = 1733

#
# MessageId: RPC_S_INVALID_BOUND
#
# MessageText:
#
# The array bounds are invalid.
#
RPC_S_INVALID_BOUND = 1734

#
# MessageId: RPC_S_NO_ENTRY_NAME
#
# MessageText:
#
# The binding does not contain an entry name.
#
RPC_S_NO_ENTRY_NAME = 1735

#
# MessageId: RPC_S_INVALID_NAME_SYNTAX
#
# MessageText:
#
# The name syntax is invalid.
#
RPC_S_INVALID_NAME_SYNTAX = 1736

#
# MessageId: RPC_S_UNSUPPORTED_NAME_SYNTAX
#
# MessageText:
#
# The name syntax is not supported.
#
RPC_S_UNSUPPORTED_NAME_SYNTAX = 1737

#
# MessageId: RPC_S_UUID_NO_ADDRESS
#
# MessageText:
#
# No network address is available to use to construct a universal unique identifier (UUID).
#
RPC_S_UUID_NO_ADDRESS = 1739

#
# MessageId: RPC_S_DUPLICATE_ENDPOINT
#
# MessageText:
#
# The endpoint is a duplicate.
#
RPC_S_DUPLICATE_ENDPOINT = 1740

#
# MessageId: RPC_S_UNKNOWN_AUTHN_TYPE
#
# MessageText:
#
# The authentication type is unknown.
#
RPC_S_UNKNOWN_AUTHN_TYPE = 1741

#
# MessageId: RPC_S_MAX_CALLS_TOO_SMALL
#
# MessageText:
#
# The maximum number of calls is too small.
#
RPC_S_MAX_CALLS_TOO_SMALL = 1742

#
# MessageId: RPC_S_STRING_TOO_LONG
#
# MessageText:
#
# The string is too long.
#
RPC_S_STRING_TOO_LONG = 1743

#
# MessageId: RPC_S_PROTSEQ_NOT_FOUND
#
# MessageText:
#
# The RPC protocol sequence was not found.
#
RPC_S_PROTSEQ_NOT_FOUND = 1744

#
# MessageId: RPC_S_PROCNUM_OUT_OF_RANGE
#
# MessageText:
#
# The procedure number is out of range.
#
RPC_S_PROCNUM_OUT_OF_RANGE = 1745

#
# MessageId: RPC_S_BINDING_HAS_NO_AUTH
#
# MessageText:
#
# The binding does not contain any authentication information.
#
RPC_S_BINDING_HAS_NO_AUTH = 1746

#
# MessageId: RPC_S_UNKNOWN_AUTHN_SERVICE
#
# MessageText:
#
# The authentication service is unknown.
#
RPC_S_UNKNOWN_AUTHN_SERVICE = 1747

#
# MessageId: RPC_S_UNKNOWN_AUTHN_LEVEL
#
# MessageText:
#
# The authentication level is unknown.
#
RPC_S_UNKNOWN_AUTHN_LEVEL = 1748

#
# MessageId: RPC_S_INVALID_AUTH_IDENTITY
#
# MessageText:
#
# The security context is invalid.
#
RPC_S_INVALID_AUTH_IDENTITY = 1749

#
# MessageId: RPC_S_UNKNOWN_AUTHZ_SERVICE
#
# MessageText:
#
# The authorization service is unknown.
#
RPC_S_UNKNOWN_AUTHZ_SERVICE = 1750

#
# MessageId: EPT_S_INVALID_ENTRY
#
# MessageText:
#
# The entry is invalid.
#
EPT_S_INVALID_ENTRY = 1751

#
# MessageId: EPT_S_CANT_PERFORM_OP
#
# MessageText:
#
# The server endpoint cannot perform the operation.
#
EPT_S_CANT_PERFORM_OP = 1752

#
# MessageId: EPT_S_NOT_REGISTERED
#
# MessageText:
#
# There are no more endpoints available from the endpoint mapper.
#
EPT_S_NOT_REGISTERED = 1753

#
# MessageId: RPC_S_NOTHING_TO_EXPORT
#
# MessageText:
#
# No interfaces have been exported.
#
RPC_S_NOTHING_TO_EXPORT = 1754

#
# MessageId: RPC_S_INCOMPLETE_NAME
#
# MessageText:
#
# The entry name is incomplete.
#
RPC_S_INCOMPLETE_NAME = 1755

#
# MessageId: RPC_S_INVALID_VERS_OPTION
#
# MessageText:
#
# The version option is invalid.
#
RPC_S_INVALID_VERS_OPTION = 1756

#
# MessageId: RPC_S_NO_MORE_MEMBERS
#
# MessageText:
#
# There are no more members.
#
RPC_S_NO_MORE_MEMBERS = 1757

#
# MessageId: RPC_S_NOT_ALL_OBJS_UNEXPORTED
#
# MessageText:
#
# There is nothing to unexport.
#
RPC_S_NOT_ALL_OBJS_UNEXPORTED = 1758

#
# MessageId: RPC_S_INTERFACE_NOT_FOUND
#
# MessageText:
#
# The interface was not found.
#
RPC_S_INTERFACE_NOT_FOUND = 1759

#
# MessageId: RPC_S_ENTRY_ALREADY_EXISTS
#
# MessageText:
#
# The entry already exists.
#
RPC_S_ENTRY_ALREADY_EXISTS = 1760

#
# MessageId: RPC_S_ENTRY_NOT_FOUND
#
# MessageText:
#
# The entry is not found.
#
RPC_S_ENTRY_NOT_FOUND = 1761

#
# MessageId: RPC_S_NAME_SERVICE_UNAVAILABLE
#
# MessageText:
#
# The name service is unavailable.
#
RPC_S_NAME_SERVICE_UNAVAILABLE = 1762

#
# MessageId: RPC_S_INVALID_NAF_ID
#
# MessageText:
#
# The network address family is invalid.
#
RPC_S_INVALID_NAF_ID = 1763

#
# MessageId: RPC_S_CANNOT_SUPPORT
#
# MessageText:
#
# The requested operation is not supported.
#
RPC_S_CANNOT_SUPPORT = 1764

#
# MessageId: RPC_S_NO_CONTEXT_AVAILABLE
#
# MessageText:
#
# No security context is available to allow impersonation.
#
RPC_S_NO_CONTEXT_AVAILABLE = 1765

#
# MessageId: RPC_S_INTERNAL_ERROR
#
# MessageText:
#
# An internal error occurred in a remote procedure call (RPC).
#
RPC_S_INTERNAL_ERROR = 1766

#
# MessageId: RPC_S_ZERO_DIVIDE
#
# MessageText:
#
# The RPC server attempted an integer division by zero.
#
RPC_S_ZERO_DIVIDE = 1767

#
# MessageId: RPC_S_ADDRESS_ERROR
#
# MessageText:
#
# An addressing error occurred in the RPC server.
#
RPC_S_ADDRESS_ERROR = 1768

#
# MessageId: RPC_S_FP_DIV_ZERO
#
# MessageText:
#
# A floating-point operation at the RPC server caused a division by zero.
#
RPC_S_FP_DIV_ZERO = 1769

#
# MessageId: RPC_S_FP_UNDERFLOW
#
# MessageText:
#
# A floating-point underflow occurred at the RPC server.
#
RPC_S_FP_UNDERFLOW = 1770

#
# MessageId: RPC_S_FP_OVERFLOW
#
# MessageText:
#
# A floating-point overflow occurred at the RPC server.
#
RPC_S_FP_OVERFLOW = 1771

#
# MessageId: RPC_X_NO_MORE_ENTRIES
#
# MessageText:
#
# The list of RPC servers available for the binding of auto handles has been exhausted.
#
RPC_X_NO_MORE_ENTRIES = 1772

#
# MessageId: RPC_X_SS_CHAR_TRANS_OPEN_FAIL
#
# MessageText:
#
# Unable to open the character translation table file.
#
RPC_X_SS_CHAR_TRANS_OPEN_FAIL = 1773

#
# MessageId: RPC_X_SS_CHAR_TRANS_SHORT_FILE
#
# MessageText:
#
# The file containing the character translation table has fewer than 512 bytes.
#
RPC_X_SS_CHAR_TRANS_SHORT_FILE = 1774

#
# MessageId: RPC_X_SS_IN_NULL_CONTEXT
#
# MessageText:
#
# A null context handle was passed from the client to the host during a remote procedure call.
#
RPC_X_SS_IN_NULL_CONTEXT = 1775

#
# MessageId: RPC_X_SS_CONTEXT_DAMAGED
#
# MessageText:
#
# The context handle changed during a remote procedure call.
#
RPC_X_SS_CONTEXT_DAMAGED = 1777

#
# MessageId: RPC_X_SS_HANDLES_MISMATCH
#
# MessageText:
#
# The binding handles passed to a remote procedure call do not match.
#
RPC_X_SS_HANDLES_MISMATCH = 1778

#
# MessageId: RPC_X_SS_CANNOT_GET_CALL_HANDLE
#
# MessageText:
#
# The stub is unable to get the remote procedure call handle.
#
RPC_X_SS_CANNOT_GET_CALL_HANDLE = 1779

#
# MessageId: RPC_X_NULL_REF_POINTER
#
# MessageText:
#
# A null reference pointer was passed to the stub.
#
RPC_X_NULL_REF_POINTER = 1780

#
# MessageId: RPC_X_ENUM_VALUE_OUT_OF_RANGE
#
# MessageText:
#
# The enumeration value is out of range.
#
RPC_X_ENUM_VALUE_OUT_OF_RANGE = 1781

#
# MessageId: RPC_X_BYTE_COUNT_TOO_SMALL
#
# MessageText:
#
# The byte count is too small.
#
RPC_X_BYTE_COUNT_TOO_SMALL = 1782

#
# MessageId: RPC_X_BAD_STUB_DATA
#
# MessageText:
#
# The stub received bad data.
#
RPC_X_BAD_STUB_DATA = 1783

#
# MessageId: ERROR_INVALID_USER_BUFFER
#
# MessageText:
#
# The supplied user buffer is not valid for the requested operation.
#
ERROR_INVALID_USER_BUFFER = 1784

#
# MessageId: ERROR_UNRECOGNIZED_MEDIA
#
# MessageText:
#
# The disk media is not recognized. It may not be formatted.
#
ERROR_UNRECOGNIZED_MEDIA = 1785

#
# MessageId: ERROR_NO_TRUST_LSA_SECRET
#
# MessageText:
#
# The workstation does not have a trust secret.
#
ERROR_NO_TRUST_LSA_SECRET = 1786

#
# MessageId: ERROR_NO_TRUST_SAM_ACCOUNT
#
# MessageText:
#
# The security database on the server does not have a computer account for this workstation trust relationship.
#
ERROR_NO_TRUST_SAM_ACCOUNT = 1787

#
# MessageId: ERROR_TRUSTED_DOMAIN_FAILURE
#
# MessageText:
#
# The trust relationship between the primary domain and the trusted domain failed.
#
ERROR_TRUSTED_DOMAIN_FAILURE = 1788

#
# MessageId: ERROR_TRUSTED_RELATIONSHIP_FAILURE
#
# MessageText:
#
# The trust relationship between this workstation and the primary domain failed.
#
ERROR_TRUSTED_RELATIONSHIP_FAILURE = 1789

#
# MessageId: ERROR_TRUST_FAILURE
#
# MessageText:
#
# The network logon failed.
#
ERROR_TRUST_FAILURE = 1790

#
# MessageId: RPC_S_CALL_IN_PROGRESS
#
# MessageText:
#
# A remote procedure call is already in progress for this thread.
#
RPC_S_CALL_IN_PROGRESS = 1791

#
# MessageId: ERROR_NETLOGON_NOT_STARTED
#
# MessageText:
#
# An attempt was made to logon, but the network logon service was not started.
#
ERROR_NETLOGON_NOT_STARTED = 1792

#
# MessageId: ERROR_ACCOUNT_EXPIRED
#
# MessageText:
#
# The user's account has expired.
#
ERROR_ACCOUNT_EXPIRED = 1793

#
# MessageId: ERROR_REDIRECTOR_HAS_OPEN_HANDLES
#
# MessageText:
#
# The redirector is in use and cannot be unloaded.
#
ERROR_REDIRECTOR_HAS_OPEN_HANDLES = 1794

#
# MessageId: ERROR_PRINTER_DRIVER_ALREADY_INSTALLED
#
# MessageText:
#
# The specified printer driver is already installed.
#
ERROR_PRINTER_DRIVER_ALREADY_INSTALLED = 1795

#
# MessageId: ERROR_UNKNOWN_PORT
#
# MessageText:
#
# The specified port is unknown.
#
ERROR_UNKNOWN_PORT = 1796

#
# MessageId: ERROR_UNKNOWN_PRINTER_DRIVER
#
# MessageText:
#
# The printer driver is unknown.
#
ERROR_UNKNOWN_PRINTER_DRIVER = 1797

#
# MessageId: ERROR_UNKNOWN_PRINTPROCESSOR
#
# MessageText:
#
# The print processor is unknown.
#
ERROR_UNKNOWN_PRINTPROCESSOR = 1798

#
# MessageId: ERROR_INVALID_SEPARATOR_FILE
#
# MessageText:
#
# The specified separator file is invalid.
#
ERROR_INVALID_SEPARATOR_FILE = 1799

#
# MessageId: ERROR_INVALID_PRIORITY
#
# MessageText:
#
# The specified priority is invalid.
#
ERROR_INVALID_PRIORITY = 1800

#
# MessageId: ERROR_INVALID_PRINTER_NAME
#
# MessageText:
#
# The printer name is invalid.
#
ERROR_INVALID_PRINTER_NAME = 1801

#
# MessageId: ERROR_PRINTER_ALREADY_EXISTS
#
# MessageText:
#
# The printer already exists.
#
ERROR_PRINTER_ALREADY_EXISTS = 1802

#
# MessageId: ERROR_INVALID_PRINTER_COMMAND
#
# MessageText:
#
# The printer command is invalid.
#
ERROR_INVALID_PRINTER_COMMAND = 1803

#
# MessageId: ERROR_INVALID_DATATYPE
#
# MessageText:
#
# The specified datatype is invalid.
#
ERROR_INVALID_DATATYPE = 1804

#
# MessageId: ERROR_INVALID_ENVIRONMENT
#
# MessageText:
#
# The environment specified is invalid.
#
ERROR_INVALID_ENVIRONMENT = 1805

#
# MessageId: RPC_S_NO_MORE_BINDINGS
#
# MessageText:
#
# There are no more bindings.
#
RPC_S_NO_MORE_BINDINGS = 1806

#
# MessageId: ERROR_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT
#
# MessageText:
#
# The account used is an interdomain trust account. Use your global user account or local user account to access this server.
#
ERROR_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT = 1807

#
# MessageId: ERROR_NOLOGON_WORKSTATION_TRUST_ACCOUNT
#
# MessageText:
#
# The account used is a computer account. Use your global user account or local user account to access this server.
#
ERROR_NOLOGON_WORKSTATION_TRUST_ACCOUNT = 1808

#
# MessageId: ERROR_NOLOGON_SERVER_TRUST_ACCOUNT
#
# MessageText:
#
# The account used is a server trust account. Use your global user account or local user account to access this server.
#
ERROR_NOLOGON_SERVER_TRUST_ACCOUNT = 1809

#
# MessageId: ERROR_DOMAIN_TRUST_INCONSISTENT
#
# MessageText:
#
# The name or security ID (SID) of the domain specified is inconsistent with the trust information for that domain.
#
ERROR_DOMAIN_TRUST_INCONSISTENT = 1810

#
# MessageId: ERROR_SERVER_HAS_OPEN_HANDLES
#
# MessageText:
#
# The server is in use and cannot be unloaded.
#
ERROR_SERVER_HAS_OPEN_HANDLES = 1811

#
# MessageId: ERROR_RESOURCE_DATA_NOT_FOUND
#
# MessageText:
#
# The specified image file did not contain a resource section.
#
ERROR_RESOURCE_DATA_NOT_FOUND = 1812

#
# MessageId: ERROR_RESOURCE_TYPE_NOT_FOUND
#
# MessageText:
#
# The specified resource type cannot be found in the image file.
#
ERROR_RESOURCE_TYPE_NOT_FOUND = 1813

#
# MessageId: ERROR_RESOURCE_NAME_NOT_FOUND
#
# MessageText:
#
# The specified resource name cannot be found in the image file.
#
ERROR_RESOURCE_NAME_NOT_FOUND = 1814

#
# MessageId: ERROR_RESOURCE_LANG_NOT_FOUND
#
# MessageText:
#
# The specified resource language ID cannot be found in the image file.
#
ERROR_RESOURCE_LANG_NOT_FOUND = 1815

#
# MessageId: ERROR_NOT_ENOUGH_QUOTA
#
# MessageText:
#
# Not enough quota is available to process this command.
#
ERROR_NOT_ENOUGH_QUOTA = 1816

#
# MessageId: RPC_S_NO_INTERFACES
#
# MessageText:
#
# No interfaces have been registered.
#
RPC_S_NO_INTERFACES = 1817

#
# MessageId: RPC_S_CALL_CANCELLED
#
# MessageText:
#
# The remote procedure call was cancelled.
#
RPC_S_CALL_CANCELLED = 1818

#
# MessageId: RPC_S_BINDING_INCOMPLETE
#
# MessageText:
#
# The binding handle does not contain all required information.
#
RPC_S_BINDING_INCOMPLETE = 1819

#
# MessageId: RPC_S_COMM_FAILURE
#
# MessageText:
#
# A communications failure occurred during a remote procedure call.
#
RPC_S_COMM_FAILURE = 1820

#
# MessageId: RPC_S_UNSUPPORTED_AUTHN_LEVEL
#
# MessageText:
#
# The requested authentication level is not supported.
#
RPC_S_UNSUPPORTED_AUTHN_LEVEL = 1821

#
# MessageId: RPC_S_NO_PRINC_NAME
#
# MessageText:
#
# No principal name registered.
#
RPC_S_NO_PRINC_NAME = 1822

#
# MessageId: RPC_S_NOT_RPC_ERROR
#
# MessageText:
#
# The error specified is not a valid Windows RPC error code.
#
RPC_S_NOT_RPC_ERROR = 1823

#
# MessageId: RPC_S_UUID_LOCAL_ONLY
#
# MessageText:
#
# A UUID that is valid only on this computer has been allocated.
#
RPC_S_UUID_LOCAL_ONLY = 1824

#
# MessageId: RPC_S_SEC_PKG_ERROR
#
# MessageText:
#
# A security package specific error occurred.
#
RPC_S_SEC_PKG_ERROR = 1825

#
# MessageId: RPC_S_NOT_CANCELLED
#
# MessageText:
#
# Thread is not canceled.
#
RPC_S_NOT_CANCELLED = 1826

#
# MessageId: RPC_X_INVALID_ES_ACTION
#
# MessageText:
#
# Invalid operation on the encoding/decoding handle.
#
RPC_X_INVALID_ES_ACTION = 1827

#
# MessageId: RPC_X_WRONG_ES_VERSION
#
# MessageText:
#
# Incompatible version of the serializing package.
#
RPC_X_WRONG_ES_VERSION = 1828

#
# MessageId: RPC_X_WRONG_STUB_VERSION
#
# MessageText:
#
# Incompatible version of the RPC stub.
#
RPC_X_WRONG_STUB_VERSION = 1829

#
# MessageId: RPC_X_INVALID_PIPE_OBJECT
#
# MessageText:
#
# The RPC pipe object is invalid or corrupted.
#
RPC_X_INVALID_PIPE_OBJECT = 1830

#
# MessageId: RPC_X_WRONG_PIPE_ORDER
#
# MessageText:
#
# An invalid operation was attempted on an RPC pipe object.
#
RPC_X_WRONG_PIPE_ORDER = 1831

#
# MessageId: RPC_X_WRONG_PIPE_VERSION
#
# MessageText:
#
# Unsupported RPC pipe version.
#
RPC_X_WRONG_PIPE_VERSION = 1832

#
# MessageId: RPC_S_COOKIE_AUTH_FAILED
#
# MessageText:
#
# HTTP proxy server rejected the connection because the cookie authentication failed.
#
RPC_S_COOKIE_AUTH_FAILED = 1833

#
# MessageId: RPC_S_GROUP_MEMBER_NOT_FOUND
#
# MessageText:
#
# The group member was not found.
#
RPC_S_GROUP_MEMBER_NOT_FOUND = 1898

#
# MessageId: EPT_S_CANT_CREATE
#
# MessageText:
#
# The endpoint mapper database entry could not be created.
#
EPT_S_CANT_CREATE = 1899

#
# MessageId: RPC_S_INVALID_OBJECT
#
# MessageText:
#
# The object universal unique identifier (UUID) is the nil UUID.
#
RPC_S_INVALID_OBJECT = 1900

#
# MessageId: ERROR_INVALID_TIME
#
# MessageText:
#
# The specified time is invalid.
#
ERROR_INVALID_TIME = 1901

#
# MessageId: ERROR_INVALID_FORM_NAME
#
# MessageText:
#
# The specified form name is invalid.
#
ERROR_INVALID_FORM_NAME = 1902

#
# MessageId: ERROR_INVALID_FORM_SIZE
#
# MessageText:
#
# The specified form size is invalid.
#
ERROR_INVALID_FORM_SIZE = 1903

#
# MessageId: ERROR_ALREADY_WAITING
#
# MessageText:
#
# The specified printer handle is already being waited on
#
ERROR_ALREADY_WAITING = 1904

#
# MessageId: ERROR_PRINTER_DELETED
#
# MessageText:
#
# The specified printer has been deleted.
#
ERROR_PRINTER_DELETED = 1905

#
# MessageId: ERROR_INVALID_PRINTER_STATE
#
# MessageText:
#
# The state of the printer is invalid.
#
ERROR_INVALID_PRINTER_STATE = 1906

#
# MessageId: ERROR_PASSWORD_MUST_CHANGE
#
# MessageText:
#
# The user's password must be changed before signing in.
#
ERROR_PASSWORD_MUST_CHANGE = 1907

#
# MessageId: ERROR_DOMAIN_CONTROLLER_NOT_FOUND
#
# MessageText:
#
# Could not find the domain controller for this domain.
#
ERROR_DOMAIN_CONTROLLER_NOT_FOUND = 1908

#
# MessageId: ERROR_ACCOUNT_LOCKED_OUT
#
# MessageText:
#
# The referenced account is currently locked out and may not be logged on to.
#
ERROR_ACCOUNT_LOCKED_OUT = 1909

#
# MessageId: OR_INVALID_OXID
#
# MessageText:
#
# The object exporter specified was not found.
#
OR_INVALID_OXID = 1910

#
# MessageId: OR_INVALID_OID
#
# MessageText:
#
# The object specified was not found.
#
OR_INVALID_OID = 1911

#
# MessageId: OR_INVALID_SET
#
# MessageText:
#
# The object resolver set specified was not found.
#
OR_INVALID_SET = 1912

#
# MessageId: RPC_S_SEND_INCOMPLETE
#
# MessageText:
#
# Some data remains to be sent in the request buffer.
#
RPC_S_SEND_INCOMPLETE = 1913

#
# MessageId: RPC_S_INVALID_ASYNC_HANDLE
#
# MessageText:
#
# Invalid asynchronous remote procedure call handle.
#
RPC_S_INVALID_ASYNC_HANDLE = 1914

#
# MessageId: RPC_S_INVALID_ASYNC_CALL
#
# MessageText:
#
# Invalid asynchronous RPC call handle for this operation.
#
RPC_S_INVALID_ASYNC_CALL = 1915

#
# MessageId: RPC_X_PIPE_CLOSED
#
# MessageText:
#
# The RPC pipe object has already been closed.
#
RPC_X_PIPE_CLOSED = 1916

#
# MessageId: RPC_X_PIPE_DISCIPLINE_ERROR
#
# MessageText:
#
# The RPC call completed before all pipes were processed.
#
RPC_X_PIPE_DISCIPLINE_ERROR = 1917

#
# MessageId: RPC_X_PIPE_EMPTY
#
# MessageText:
#
# No more data is available from the RPC pipe.
#
RPC_X_PIPE_EMPTY = 1918

#
# MessageId: ERROR_NO_SITENAME
#
# MessageText:
#
# No site name is available for this machine.
#
ERROR_NO_SITENAME = 1919

#
# MessageId: ERROR_CANT_ACCESS_FILE
#
# MessageText:
#
# The file cannot be accessed by the system.
#
ERROR_CANT_ACCESS_FILE = 1920

#
# MessageId: ERROR_CANT_RESOLVE_FILENAME
#
# MessageText:
#
# The name of the file cannot be resolved by the system.
#
ERROR_CANT_RESOLVE_FILENAME = 1921

#
# MessageId: RPC_S_ENTRY_TYPE_MISMATCH
#
# MessageText:
#
# The entry is not of the expected type.
#
RPC_S_ENTRY_TYPE_MISMATCH = 1922

#
# MessageId: RPC_S_NOT_ALL_OBJS_EXPORTED
#
# MessageText:
#
# Not all object UUIDs could be exported to the specified entry.
#
RPC_S_NOT_ALL_OBJS_EXPORTED = 1923

#
# MessageId: RPC_S_INTERFACE_NOT_EXPORTED
#
# MessageText:
#
# Interface could not be exported to the specified entry.
#
RPC_S_INTERFACE_NOT_EXPORTED = 1924

#
# MessageId: RPC_S_PROFILE_NOT_ADDED
#
# MessageText:
#
# The specified profile entry could not be added.
#
RPC_S_PROFILE_NOT_ADDED = 1925

#
# MessageId: RPC_S_PRF_ELT_NOT_ADDED
#
# MessageText:
#
# The specified profile element could not be added.
#
RPC_S_PRF_ELT_NOT_ADDED = 1926

#
# MessageId: RPC_S_PRF_ELT_NOT_REMOVED
#
# MessageText:
#
# The specified profile element could not be removed.
#
RPC_S_PRF_ELT_NOT_REMOVED = 1927

#
# MessageId: RPC_S_GRP_ELT_NOT_ADDED
#
# MessageText:
#
# The group element could not be added.
#
RPC_S_GRP_ELT_NOT_ADDED = 1928

#
# MessageId: RPC_S_GRP_ELT_NOT_REMOVED
#
# MessageText:
#
# The group element could not be removed.
#
RPC_S_GRP_ELT_NOT_REMOVED = 1929

#
# MessageId: ERROR_KM_DRIVER_BLOCKED
#
# MessageText:
#
# The printer driver is not compatible with a policy enabled on your computer that blocks NT 4.0 drivers.
#
ERROR_KM_DRIVER_BLOCKED = 1930

#
# MessageId: ERROR_CONTEXT_EXPIRED
#
# MessageText:
#
# The context has expired and can no longer be used.
#
ERROR_CONTEXT_EXPIRED = 1931

#
# MessageId: ERROR_PER_USER_TRUST_QUOTA_EXCEEDED
#
# MessageText:
#
# The current user's delegated trust creation quota has been exceeded.
#
ERROR_PER_USER_TRUST_QUOTA_EXCEEDED = 1932

#
# MessageId: ERROR_ALL_USER_TRUST_QUOTA_EXCEEDED
#
# MessageText:
#
# The total delegated trust creation quota has been exceeded.
#
ERROR_ALL_USER_TRUST_QUOTA_EXCEEDED = 1933

#
# MessageId: ERROR_USER_DELETE_TRUST_QUOTA_EXCEEDED
#
# MessageText:
#
# The current user's delegated trust deletion quota has been exceeded.
#
ERROR_USER_DELETE_TRUST_QUOTA_EXCEEDED = 1934

#
# MessageId: ERROR_AUTHENTICATION_FIREWALL_FAILED
#
# MessageText:
#
# The computer you are signing into is protected by an authentication firewall. The specified account is not allowed to authenticate to the computer.
#
ERROR_AUTHENTICATION_FIREWALL_FAILED = 1935

#
# MessageId: ERROR_REMOTE_PRINT_CONNECTIONS_BLOCKED
#
# MessageText:
#
# Remote connections to the Print Spooler are blocked by a policy set on your machine.
#
ERROR_REMOTE_PRINT_CONNECTIONS_BLOCKED = 1936

#
# MessageId: ERROR_NTLM_BLOCKED
#
# MessageText:
#
# Authentication failed because NTLM authentication has been disabled.
#
ERROR_NTLM_BLOCKED = 1937

#
# MessageId: ERROR_PASSWORD_CHANGE_REQUIRED
#
# MessageText:
#
# Logon Failure: EAS policy requires that the user change their password before this operation can be performed.
#
ERROR_PASSWORD_CHANGE_REQUIRED = 1938


#/////////////////////////////////////////////////
#                                               //
#              OpenGL Error codes               //
#                                               //
#                 2000 to 2009                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INVALID_PIXEL_FORMAT
#
# MessageText:
#
# The pixel format is invalid.
#
ERROR_INVALID_PIXEL_FORMAT = 2000

#
# MessageId: ERROR_BAD_DRIVER
#
# MessageText:
#
# The specified driver is invalid.
#
ERROR_BAD_DRIVER = 2001

#
# MessageId: ERROR_INVALID_WINDOW_STYLE
#
# MessageText:
#
# The window style or class attribute is invalid for this operation.
#
ERROR_INVALID_WINDOW_STYLE = 2002

#
# MessageId: ERROR_METAFILE_NOT_SUPPORTED
#
# MessageText:
#
# The requested metafile operation is not supported.
#
ERROR_METAFILE_NOT_SUPPORTED = 2003

#
# MessageId: ERROR_TRANSFORM_NOT_SUPPORTED
#
# MessageText:
#
# The requested transformation operation is not supported.
#
ERROR_TRANSFORM_NOT_SUPPORTED = 2004

#
# MessageId: ERROR_CLIPPING_NOT_SUPPORTED
#
# MessageText:
#
# The requested clipping operation is not supported.
#
ERROR_CLIPPING_NOT_SUPPORTED = 2005


#/////////////////////////////////////////////////
#                                               //
#       Image Color Management Error codes      //
#                                               //
#                 2010 to 2049                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INVALID_CMM
#
# MessageText:
#
# The specified color management module is invalid.
#
ERROR_INVALID_CMM = 2010

#
# MessageId: ERROR_INVALID_PROFILE
#
# MessageText:
#
# The specified color profile is invalid.
#
ERROR_INVALID_PROFILE = 2011

#
# MessageId: ERROR_TAG_NOT_FOUND
#
# MessageText:
#
# The specified tag was not found.
#
ERROR_TAG_NOT_FOUND = 2012

#
# MessageId: ERROR_TAG_NOT_PRESENT
#
# MessageText:
#
# A required tag is not present.
#
ERROR_TAG_NOT_PRESENT = 2013

#
# MessageId: ERROR_DUPLICATE_TAG
#
# MessageText:
#
# The specified tag is already present.
#
ERROR_DUPLICATE_TAG = 2014

#
# MessageId: ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE
#
# MessageText:
#
# The specified color profile is not associated with the specified device.
#
ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE = 2015

#
# MessageId: ERROR_PROFILE_NOT_FOUND
#
# MessageText:
#
# The specified color profile was not found.
#
ERROR_PROFILE_NOT_FOUND = 2016

#
# MessageId: ERROR_INVALID_COLORSPACE
#
# MessageText:
#
# The specified color space is invalid.
#
ERROR_INVALID_COLORSPACE = 2017

#
# MessageId: ERROR_ICM_NOT_ENABLED
#
# MessageText:
#
# Image Color Management is not enabled.
#
ERROR_ICM_NOT_ENABLED = 2018

#
# MessageId: ERROR_DELETING_ICM_XFORM
#
# MessageText:
#
# There was an error while deleting the color transform.
#
ERROR_DELETING_ICM_XFORM = 2019

#
# MessageId: ERROR_INVALID_TRANSFORM
#
# MessageText:
#
# The specified color transform is invalid.
#
ERROR_INVALID_TRANSFORM = 2020

#
# MessageId: ERROR_COLORSPACE_MISMATCH
#
# MessageText:
#
# The specified transform does not match the bitmap's color space.
#
ERROR_COLORSPACE_MISMATCH = 2021

#
# MessageId: ERROR_INVALID_COLORINDEX
#
# MessageText:
#
# The specified named color index is not present in the profile.
#
ERROR_INVALID_COLORINDEX = 2022

#
# MessageId: ERROR_PROFILE_DOES_NOT_MATCH_DEVICE
#
# MessageText:
#
# The specified profile is intended for a device of a different type than the specified device.
#
ERROR_PROFILE_DOES_NOT_MATCH_DEVICE = 2023


#/////////////////////////////////////////////////
#                                               //
#             Winnet32 Error codes              //
#                                               //
#                 2100 to 2999                  //
#                                               //
# The range 2100 through 2999 is reserved for   //
# network status codes. See lmerr.h for a       //
# complete listing                              //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_CONNECTED_OTHER_PASSWORD
#
# MessageText:
#
# The network connection was made successfully, but the user had to be prompted for a password other than the one originally specified.
#
ERROR_CONNECTED_OTHER_PASSWORD = 2108

#
# MessageId: ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT
#
# MessageText:
#
# The network connection was made successfully using default credentials.
#
ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT = 2109

#
# MessageId: ERROR_BAD_USERNAME
#
# MessageText:
#
# The specified username is invalid.
#
ERROR_BAD_USERNAME = 2202

#
# MessageId: ERROR_NOT_CONNECTED
#
# MessageText:
#
# This network connection does not exist.
#
ERROR_NOT_CONNECTED = 2250

#
# MessageId: ERROR_OPEN_FILES
#
# MessageText:
#
# This network connection has files open or requests pending.
#
ERROR_OPEN_FILES = 2401

#
# MessageId: ERROR_ACTIVE_CONNECTIONS
#
# MessageText:
#
# Active connections still exist.
#
ERROR_ACTIVE_CONNECTIONS = 2402

#
# MessageId: ERROR_DEVICE_IN_USE
#
# MessageText:
#
# The device is in use by an active process and cannot be disconnected.
#
ERROR_DEVICE_IN_USE = 2404


#/////////////////////////////////////////////////
#                                               //
#           Win32 Spooler Error codes           //
#                                               //
#                 3000 to 3049                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_UNKNOWN_PRINT_MONITOR
#
# MessageText:
#
# The specified print monitor is unknown.
#
ERROR_UNKNOWN_PRINT_MONITOR = 3000

#
# MessageId: ERROR_PRINTER_DRIVER_IN_USE
#
# MessageText:
#
# The specified printer driver is currently in use.
#
ERROR_PRINTER_DRIVER_IN_USE = 3001

#
# MessageId: ERROR_SPOOL_FILE_NOT_FOUND
#
# MessageText:
#
# The spool file was not found.
#
ERROR_SPOOL_FILE_NOT_FOUND = 3002

#
# MessageId: ERROR_SPL_NO_STARTDOC
#
# MessageText:
#
# A StartDocPrinter call was not issued.
#
ERROR_SPL_NO_STARTDOC = 3003

#
# MessageId: ERROR_SPL_NO_ADDJOB
#
# MessageText:
#
# An AddJob call was not issued.
#
ERROR_SPL_NO_ADDJOB = 3004

#
# MessageId: ERROR_PRINT_PROCESSOR_ALREADY_INSTALLED
#
# MessageText:
#
# The specified print processor has already been installed.
#
ERROR_PRINT_PROCESSOR_ALREADY_INSTALLED = 3005

#
# MessageId: ERROR_PRINT_MONITOR_ALREADY_INSTALLED
#
# MessageText:
#
# The specified print monitor has already been installed.
#
ERROR_PRINT_MONITOR_ALREADY_INSTALLED = 3006

#
# MessageId: ERROR_INVALID_PRINT_MONITOR
#
# MessageText:
#
# The specified print monitor does not have the required functions.
#
ERROR_INVALID_PRINT_MONITOR = 3007

#
# MessageId: ERROR_PRINT_MONITOR_IN_USE
#
# MessageText:
#
# The specified print monitor is currently in use.
#
ERROR_PRINT_MONITOR_IN_USE = 3008

#
# MessageId: ERROR_PRINTER_HAS_JOBS_QUEUED
#
# MessageText:
#
# The requested operation is not allowed when there are jobs queued to the printer.
#
ERROR_PRINTER_HAS_JOBS_QUEUED = 3009

#
# MessageId: ERROR_SUCCESS_REBOOT_REQUIRED
#
# MessageText:
#
# The requested operation is successful. Changes will not be effective until the system is rebooted.
#
ERROR_SUCCESS_REBOOT_REQUIRED = 3010

#
# MessageId: ERROR_SUCCESS_RESTART_REQUIRED
#
# MessageText:
#
# The requested operation is successful. Changes will not be effective until the service is restarted.
#
ERROR_SUCCESS_RESTART_REQUIRED = 3011

#
# MessageId: ERROR_PRINTER_NOT_FOUND
#
# MessageText:
#
# No printers were found.
#
ERROR_PRINTER_NOT_FOUND = 3012

#
# MessageId: ERROR_PRINTER_DRIVER_WARNED
#
# MessageText:
#
# The printer driver is known to be unreliable.
#
ERROR_PRINTER_DRIVER_WARNED = 3013

#
# MessageId: ERROR_PRINTER_DRIVER_BLOCKED
#
# MessageText:
#
# The printer driver is known to harm the system.
#
ERROR_PRINTER_DRIVER_BLOCKED = 3014

#
# MessageId: ERROR_PRINTER_DRIVER_PACKAGE_IN_USE
#
# MessageText:
#
# The specified printer driver package is currently in use.
#
ERROR_PRINTER_DRIVER_PACKAGE_IN_USE = 3015

#
# MessageId: ERROR_CORE_DRIVER_PACKAGE_NOT_FOUND
#
# MessageText:
#
# Unable to find a core driver package that is required by the printer driver package.
#
ERROR_CORE_DRIVER_PACKAGE_NOT_FOUND = 3016

#
# MessageId: ERROR_FAIL_REBOOT_REQUIRED
#
# MessageText:
#
# The requested operation failed. A system reboot is required to roll back changes made.
#
ERROR_FAIL_REBOOT_REQUIRED = 3017

#
# MessageId: ERROR_FAIL_REBOOT_INITIATED
#
# MessageText:
#
# The requested operation failed. A system reboot has been initiated to roll back changes made.
#
ERROR_FAIL_REBOOT_INITIATED = 3018

#
# MessageId: ERROR_PRINTER_DRIVER_DOWNLOAD_NEEDED
#
# MessageText:
#
# The specified printer driver was not found on the system and needs to be downloaded.
#
ERROR_PRINTER_DRIVER_DOWNLOAD_NEEDED = 3019

#
# MessageId: ERROR_PRINT_JOB_RESTART_REQUIRED
#
# MessageText:
#
# The requested print job has failed to print. A print system update requires the job to be resubmitted.
#
ERROR_PRINT_JOB_RESTART_REQUIRED = 3020

#
# MessageId: ERROR_INVALID_PRINTER_DRIVER_MANIFEST
#
# MessageText:
#
# The printer driver does not contain a valid manifest, or contains too many manifests.
#
ERROR_INVALID_PRINTER_DRIVER_MANIFEST = 3021

#
# MessageId: ERROR_PRINTER_NOT_SHAREABLE
#
# MessageText:
#
# The specified printer cannot be shared.
#
ERROR_PRINTER_NOT_SHAREABLE = 3022


#/////////////////////////////////////////////////
#                                               //
#           CopyFile ext. Error codes           //
#                                               //
#                 3050 to 3059                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_REQUEST_PAUSED
#
# MessageText:
#
# The operation was paused.
#
ERROR_REQUEST_PAUSED = 3050


#/////////////////////////////////////////////////
#                                               //
#                  Available                    //
#                                               //
#                 3060 to 3199                  //
#/////////////////////////////////////////////////


#
#               the message range
#                 3200 to 3299
#      is reserved and used in isolation lib
#

#/////////////////////////////////////////////////
#                                               //
#                  Available                    //
#                                               //
#                 3300 to 3899                  //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#                IO Error Codes                 //
#                                               //
#                 3900 to 3999                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_IO_REISSUE_AS_CACHED
#
# MessageText:
#
# Reissue the given operation as a cached IO operation
#
ERROR_IO_REISSUE_AS_CACHED = 3950



#/////////////////////////////////////////////////
#                                               //
#                Wins Error codes               //
#                                               //
#                 4000 to 4049                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_WINS_INTERNAL
#
# MessageText:
#
# WINS encountered an error while processing the command.
#
ERROR_WINS_INTERNAL = 4000

#
# MessageId: ERROR_CAN_NOT_DEL_LOCAL_WINS
#
# MessageText:
#
# The local WINS cannot be deleted.
#
ERROR_CAN_NOT_DEL_LOCAL_WINS = 4001

#
# MessageId: ERROR_STATIC_INIT
#
# MessageText:
#
# The importation from the file failed.
#
ERROR_STATIC_INIT = 4002

#
# MessageId: ERROR_INC_BACKUP
#
# MessageText:
#
# The backup failed. Was a full backup done before?
#
ERROR_INC_BACKUP = 4003

#
# MessageId: ERROR_FULL_BACKUP
#
# MessageText:
#
# The backup failed. Check the directory to which you are backing the database.
#
ERROR_FULL_BACKUP = 4004

#
# MessageId: ERROR_REC_NON_EXISTENT
#
# MessageText:
#
# The name does not exist in the WINS database.
#
ERROR_REC_NON_EXISTENT = 4005

#
# MessageId: ERROR_RPL_NOT_ALLOWED
#
# MessageText:
#
# Replication with a nonconfigured partner is not allowed.
#
ERROR_RPL_NOT_ALLOWED = 4006


#/////////////////////////////////////////////////
#                                               //
#              PeerDist Error codes             //
#                                               //
#                 4050 to 4099                  //
#/////////////////////////////////////////////////

#
# MessageId: PEERDIST_ERROR_CONTENTINFO_VERSION_UNSUPPORTED
#
# MessageText:
#
# The version of the supplied content information is not supported.
#
PEERDIST_ERROR_CONTENTINFO_VERSION_UNSUPPORTED = 4050

#
# MessageId: PEERDIST_ERROR_CANNOT_PARSE_CONTENTINFO
#
# MessageText:
#
# The supplied content information is malformed.
#
PEERDIST_ERROR_CANNOT_PARSE_CONTENTINFO = 4051

#
# MessageId: PEERDIST_ERROR_MISSING_DATA
#
# MessageText:
#
# The requested data cannot be found in local or peer caches.
#
PEERDIST_ERROR_MISSING_DATA = 4052

#
# MessageId: PEERDIST_ERROR_NO_MORE
#
# MessageText:
#
# No more data is available or required.
#
PEERDIST_ERROR_NO_MORE = 4053

#
# MessageId: PEERDIST_ERROR_NOT_INITIALIZED
#
# MessageText:
#
# The supplied object has not been initialized.
#
PEERDIST_ERROR_NOT_INITIALIZED = 4054

#
# MessageId: PEERDIST_ERROR_ALREADY_INITIALIZED
#
# MessageText:
#
# The supplied object has already been initialized.
#
PEERDIST_ERROR_ALREADY_INITIALIZED = 4055

#
# MessageId: PEERDIST_ERROR_SHUTDOWN_IN_PROGRESS
#
# MessageText:
#
# A shutdown operation is already in progress.
#
PEERDIST_ERROR_SHUTDOWN_IN_PROGRESS = 4056

#
# MessageId: PEERDIST_ERROR_INVALIDATED
#
# MessageText:
#
# The supplied object has already been invalidated.
#
PEERDIST_ERROR_INVALIDATED = 4057

#
# MessageId: PEERDIST_ERROR_ALREADY_EXISTS
#
# MessageText:
#
# An element already exists and was not replaced.
#
PEERDIST_ERROR_ALREADY_EXISTS = 4058

#
# MessageId: PEERDIST_ERROR_OPERATION_NOTFOUND
#
# MessageText:
#
# Can not cancel the requested operation as it has already been completed.
#
PEERDIST_ERROR_OPERATION_NOTFOUND = 4059

#
# MessageId: PEERDIST_ERROR_ALREADY_COMPLETED
#
# MessageText:
#
# Can not perform the reqested operation because it has already been carried out.
#
PEERDIST_ERROR_ALREADY_COMPLETED = 4060

#
# MessageId: PEERDIST_ERROR_OUT_OF_BOUNDS
#
# MessageText:
#
# An operation accessed data beyond the bounds of valid data.
#
PEERDIST_ERROR_OUT_OF_BOUNDS = 4061

#
# MessageId: PEERDIST_ERROR_VERSION_UNSUPPORTED
#
# MessageText:
#
# The requested version is not supported.
#
PEERDIST_ERROR_VERSION_UNSUPPORTED = 4062

#
# MessageId: PEERDIST_ERROR_INVALID_CONFIGURATION
#
# MessageText:
#
# A configuration value is invalid.
#
PEERDIST_ERROR_INVALID_CONFIGURATION = 4063

#
# MessageId: PEERDIST_ERROR_NOT_LICENSED
#
# MessageText:
#
# The SKU is not licensed.
#
PEERDIST_ERROR_NOT_LICENSED = 4064

#
# MessageId: PEERDIST_ERROR_SERVICE_UNAVAILABLE
#
# MessageText:
#
# PeerDist Service is still initializing and will be available shortly.
#
PEERDIST_ERROR_SERVICE_UNAVAILABLE = 4065

#
# MessageId: PEERDIST_ERROR_TRUST_FAILURE
#
# MessageText:
#
# Communication with one or more computers will be temporarily blocked due to recent errors.
#
PEERDIST_ERROR_TRUST_FAILURE = 4066


#/////////////////////////////////////////////////
#                                               //
#               DHCP Error codes                //
#                                               //
#                 4100 to 4149                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_DHCP_ADDRESS_CONFLICT
#
# MessageText:
#
# The DHCP client has obtained an IP address that is already in use on the network. The local interface will be disabled until the DHCP client can obtain a new address.
#
ERROR_DHCP_ADDRESS_CONFLICT = 4100


#/////////////////////////////////////////////////
#                                               //
#                  Available                    //
#                                               //
#                 4150 to 4199                  //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#               WMI Error codes                 //
#                                               //
#                 4200 to 4249                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_WMI_GUID_NOT_FOUND
#
# MessageText:
#
# The GUID passed was not recognized as valid by a WMI data provider.
#
ERROR_WMI_GUID_NOT_FOUND = 4200

#
# MessageId: ERROR_WMI_INSTANCE_NOT_FOUND
#
# MessageText:
#
# The instance name passed was not recognized as valid by a WMI data provider.
#
ERROR_WMI_INSTANCE_NOT_FOUND = 4201

#
# MessageId: ERROR_WMI_ITEMID_NOT_FOUND
#
# MessageText:
#
# The data item ID passed was not recognized as valid by a WMI data provider.
#
ERROR_WMI_ITEMID_NOT_FOUND = 4202

#
# MessageId: ERROR_WMI_TRY_AGAIN
#
# MessageText:
#
# The WMI request could not be completed and should be retried.
#
ERROR_WMI_TRY_AGAIN = 4203

#
# MessageId: ERROR_WMI_DP_NOT_FOUND
#
# MessageText:
#
# The WMI data provider could not be located.
#
ERROR_WMI_DP_NOT_FOUND = 4204

#
# MessageId: ERROR_WMI_UNRESOLVED_INSTANCE_REF
#
# MessageText:
#
# The WMI data provider references an instance set that has not been registered.
#
ERROR_WMI_UNRESOLVED_INSTANCE_REF = 4205

#
# MessageId: ERROR_WMI_ALREADY_ENABLED
#
# MessageText:
#
# The WMI data block or event notification has already been enabled.
#
ERROR_WMI_ALREADY_ENABLED = 4206

#
# MessageId: ERROR_WMI_GUID_DISCONNECTED
#
# MessageText:
#
# The WMI data block is no longer available.
#
ERROR_WMI_GUID_DISCONNECTED = 4207

#
# MessageId: ERROR_WMI_SERVER_UNAVAILABLE
#
# MessageText:
#
# The WMI data service is not available.
#
ERROR_WMI_SERVER_UNAVAILABLE = 4208

#
# MessageId: ERROR_WMI_DP_FAILED
#
# MessageText:
#
# The WMI data provider failed to carry out the request.
#
ERROR_WMI_DP_FAILED = 4209

#
# MessageId: ERROR_WMI_INVALID_MOF
#
# MessageText:
#
# The WMI MOF information is not valid.
#
ERROR_WMI_INVALID_MOF = 4210

#
# MessageId: ERROR_WMI_INVALID_REGINFO
#
# MessageText:
#
# The WMI registration information is not valid.
#
ERROR_WMI_INVALID_REGINFO = 4211

#
# MessageId: ERROR_WMI_ALREADY_DISABLED
#
# MessageText:
#
# The WMI data block or event notification has already been disabled.
#
ERROR_WMI_ALREADY_DISABLED = 4212

#
# MessageId: ERROR_WMI_READ_ONLY
#
# MessageText:
#
# The WMI data item or data block is read only.
#
ERROR_WMI_READ_ONLY = 4213

#
# MessageId: ERROR_WMI_SET_FAILURE
#
# MessageText:
#
# The WMI data item or data block could not be changed.
#
ERROR_WMI_SET_FAILURE = 4214


#/////////////////////////////////////////////////
#                                               //
#      app container Specific Error Codes        //
#                                               //
#                 4250 to 4299                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_NOT_APPCONTAINER
#
# MessageText:
#
# This operation is only valid in the context of an app container.
#
ERROR_NOT_APPCONTAINER = 4250

#
# MessageId: ERROR_APPCONTAINER_REQUIRED
#
# MessageText:
#
# This application can only run in the context of an app container.
#
ERROR_APPCONTAINER_REQUIRED = 4251

#
# MessageId: ERROR_NOT_SUPPORTED_IN_APPCONTAINER
#
# MessageText:
#
# This functionality is not supported in the context of an app container.
#
ERROR_NOT_SUPPORTED_IN_APPCONTAINER = 4252

#
# MessageId: ERROR_INVALID_PACKAGE_SID_LENGTH
#
# MessageText:
#
# The length of the SID supplied is not a valid length for app container SIDs.
#
ERROR_INVALID_PACKAGE_SID_LENGTH = 4253

#/////////////////////////////////////////////////
#                                               //
#        RSM (Media Services) Error codes       //
#                                               //
#                 4300 to 4349                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INVALID_MEDIA
#
# MessageText:
#
# The media identifier does not represent a valid medium.
#
ERROR_INVALID_MEDIA = 4300

#
# MessageId: ERROR_INVALID_LIBRARY
#
# MessageText:
#
# The library identifier does not represent a valid library.
#
ERROR_INVALID_LIBRARY = 4301

#
# MessageId: ERROR_INVALID_MEDIA_POOL
#
# MessageText:
#
# The media pool identifier does not represent a valid media pool.
#
ERROR_INVALID_MEDIA_POOL = 4302

#
# MessageId: ERROR_DRIVE_MEDIA_MISMATCH
#
# MessageText:
#
# The drive and medium are not compatible or exist in different libraries.
#
ERROR_DRIVE_MEDIA_MISMATCH = 4303

#
# MessageId: ERROR_MEDIA_OFFLINE
#
# MessageText:
#
# The medium currently exists in an offline library and must be online to perform this operation.
#
ERROR_MEDIA_OFFLINE = 4304

#
# MessageId: ERROR_LIBRARY_OFFLINE
#
# MessageText:
#
# The operation cannot be performed on an offline library.
#
ERROR_LIBRARY_OFFLINE = 4305

#
# MessageId: ERROR_EMPTY
#
# MessageText:
#
# The library, drive, or media pool is empty.
#
ERROR_EMPTY = 4306

#
# MessageId: ERROR_NOT_EMPTY
#
# MessageText:
#
# The library, drive, or media pool must be empty to perform this operation.
#
ERROR_NOT_EMPTY = 4307

#
# MessageId: ERROR_MEDIA_UNAVAILABLE
#
# MessageText:
#
# No media is currently available in this media pool or library.
#
ERROR_MEDIA_UNAVAILABLE = 4308

#
# MessageId: ERROR_RESOURCE_DISABLED
#
# MessageText:
#
# A resource required for this operation is disabled.
#
ERROR_RESOURCE_DISABLED = 4309

#
# MessageId: ERROR_INVALID_CLEANER
#
# MessageText:
#
# The media identifier does not represent a valid cleaner.
#
ERROR_INVALID_CLEANER = 4310

#
# MessageId: ERROR_UNABLE_TO_CLEAN
#
# MessageText:
#
# The drive cannot be cleaned or does not support cleaning.
#
ERROR_UNABLE_TO_CLEAN = 4311

#
# MessageId: ERROR_OBJECT_NOT_FOUND
#
# MessageText:
#
# The object identifier does not represent a valid object.
#
ERROR_OBJECT_NOT_FOUND = 4312

#
# MessageId: ERROR_DATABASE_FAILURE
#
# MessageText:
#
# Unable to read from or write to the database.
#
ERROR_DATABASE_FAILURE = 4313

#
# MessageId: ERROR_DATABASE_FULL
#
# MessageText:
#
# The database is full.
#
ERROR_DATABASE_FULL = 4314

#
# MessageId: ERROR_MEDIA_INCOMPATIBLE
#
# MessageText:
#
# The medium is not compatible with the device or media pool.
#
ERROR_MEDIA_INCOMPATIBLE = 4315

#
# MessageId: ERROR_RESOURCE_NOT_PRESENT
#
# MessageText:
#
# The resource required for this operation does not exist.
#
ERROR_RESOURCE_NOT_PRESENT = 4316

#
# MessageId: ERROR_INVALID_OPERATION
#
# MessageText:
#
# The operation identifier is not valid.
#
ERROR_INVALID_OPERATION = 4317

#
# MessageId: ERROR_MEDIA_NOT_AVAILABLE
#
# MessageText:
#
# The media is not mounted or ready for use.
#
ERROR_MEDIA_NOT_AVAILABLE = 4318

#
# MessageId: ERROR_DEVICE_NOT_AVAILABLE
#
# MessageText:
#
# The device is not ready for use.
#
ERROR_DEVICE_NOT_AVAILABLE = 4319

#
# MessageId: ERROR_REQUEST_REFUSED
#
# MessageText:
#
# The operator or administrator has refused the request.
#
ERROR_REQUEST_REFUSED = 4320

#
# MessageId: ERROR_INVALID_DRIVE_OBJECT
#
# MessageText:
#
# The drive identifier does not represent a valid drive.
#
ERROR_INVALID_DRIVE_OBJECT = 4321

#
# MessageId: ERROR_LIBRARY_FULL
#
# MessageText:
#
# Library is full. No slot is available for use.
#
ERROR_LIBRARY_FULL = 4322

#
# MessageId: ERROR_MEDIUM_NOT_ACCESSIBLE
#
# MessageText:
#
# The transport cannot access the medium.
#
ERROR_MEDIUM_NOT_ACCESSIBLE = 4323

#
# MessageId: ERROR_UNABLE_TO_LOAD_MEDIUM
#
# MessageText:
#
# Unable to load the medium into the drive.
#
ERROR_UNABLE_TO_LOAD_MEDIUM = 4324

#
# MessageId: ERROR_UNABLE_TO_INVENTORY_DRIVE
#
# MessageText:
#
# Unable to retrieve the drive status.
#
ERROR_UNABLE_TO_INVENTORY_DRIVE = 4325

#
# MessageId: ERROR_UNABLE_TO_INVENTORY_SLOT
#
# MessageText:
#
# Unable to retrieve the slot status.
#
ERROR_UNABLE_TO_INVENTORY_SLOT = 4326

#
# MessageId: ERROR_UNABLE_TO_INVENTORY_TRANSPORT
#
# MessageText:
#
# Unable to retrieve status about the transport.
#
ERROR_UNABLE_TO_INVENTORY_TRANSPORT = 4327

#
# MessageId: ERROR_TRANSPORT_FULL
#
# MessageText:
#
# Cannot use the transport because it is already in use.
#
ERROR_TRANSPORT_FULL = 4328

#
# MessageId: ERROR_CONTROLLING_IEPORT
#
# MessageText:
#
# Unable to open or close the inject/eject port.
#
ERROR_CONTROLLING_IEPORT = 4329

#
# MessageId: ERROR_UNABLE_TO_EJECT_MOUNTED_MEDIA
#
# MessageText:
#
# Unable to eject the medium because it is in a drive.
#
ERROR_UNABLE_TO_EJECT_MOUNTED_MEDIA = 4330

#
# MessageId: ERROR_CLEANER_SLOT_SET
#
# MessageText:
#
# A cleaner slot is already reserved.
#
ERROR_CLEANER_SLOT_SET = 4331

#
# MessageId: ERROR_CLEANER_SLOT_NOT_SET
#
# MessageText:
#
# A cleaner slot is not reserved.
#
ERROR_CLEANER_SLOT_NOT_SET = 4332

#
# MessageId: ERROR_CLEANER_CARTRIDGE_SPENT
#
# MessageText:
#
# The cleaner cartridge has performed the maximum number of drive cleanings.
#
ERROR_CLEANER_CARTRIDGE_SPENT = 4333

#
# MessageId: ERROR_UNEXPECTED_OMID
#
# MessageText:
#
# Unexpected on-medium identifier.
#
ERROR_UNEXPECTED_OMID = 4334

#
# MessageId: ERROR_CANT_DELETE_LAST_ITEM
#
# MessageText:
#
# The last remaining item in this group or resource cannot be deleted.
#
ERROR_CANT_DELETE_LAST_ITEM = 4335

#
# MessageId: ERROR_MESSAGE_EXCEEDS_MAX_SIZE
#
# MessageText:
#
# The message provided exceeds the maximum size allowed for this parameter.
#
ERROR_MESSAGE_EXCEEDS_MAX_SIZE = 4336

#
# MessageId: ERROR_VOLUME_CONTAINS_SYS_FILES
#
# MessageText:
#
# The volume contains system or paging files.
#
ERROR_VOLUME_CONTAINS_SYS_FILES = 4337

#
# MessageId: ERROR_INDIGENOUS_TYPE
#
# MessageText:
#
# The media type cannot be removed from this library since at least one drive in the library reports it can support this media type.
#
ERROR_INDIGENOUS_TYPE = 4338

#
# MessageId: ERROR_NO_SUPPORTING_DRIVES
#
# MessageText:
#
# This offline media cannot be mounted on this system since no enabled drives are present which can be used.
#
ERROR_NO_SUPPORTING_DRIVES = 4339

#
# MessageId: ERROR_CLEANER_CARTRIDGE_INSTALLED
#
# MessageText:
#
# A cleaner cartridge is present in the tape library.
#
ERROR_CLEANER_CARTRIDGE_INSTALLED = 4340

#
# MessageId: ERROR_IEPORT_FULL
#
# MessageText:
#
# Cannot use the inject/eject port because it is not empty.
#
ERROR_IEPORT_FULL = 4341


#/////////////////////////////////////////////////
#                                               //
#       Remote Storage Service Error codes      //
#                                               //
#                 4350 to 4389                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_FILE_OFFLINE
#
# MessageText:
#
# This file is currently not available for use on this computer.
#
ERROR_FILE_OFFLINE = 4350

#
# MessageId: ERROR_REMOTE_STORAGE_NOT_ACTIVE
#
# MessageText:
#
# The remote storage service is not operational at this time.
#
ERROR_REMOTE_STORAGE_NOT_ACTIVE = 4351

#
# MessageId: ERROR_REMOTE_STORAGE_MEDIA_ERROR
#
# MessageText:
#
# The remote storage service encountered a media error.
#
ERROR_REMOTE_STORAGE_MEDIA_ERROR = 4352


#/////////////////////////////////////////////////
#                                               //
#           Reparse Point Error codes           //
#                                               //
#                 4390 to 4399                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_NOT_A_REPARSE_POINT
#
# MessageText:
#
# The file or directory is not a reparse point.
#
ERROR_NOT_A_REPARSE_POINT = 4390

#
# MessageId: ERROR_REPARSE_ATTRIBUTE_CONFLICT
#
# MessageText:
#
# The reparse point attribute cannot be set because it conflicts with an existing attribute.
#
ERROR_REPARSE_ATTRIBUTE_CONFLICT = 4391

#
# MessageId: ERROR_INVALID_REPARSE_DATA
#
# MessageText:
#
# The data present in the reparse point buffer is invalid.
#
ERROR_INVALID_REPARSE_DATA = 4392

#
# MessageId: ERROR_REPARSE_TAG_INVALID
#
# MessageText:
#
# The tag present in the reparse point buffer is invalid.
#
ERROR_REPARSE_TAG_INVALID = 4393

#
# MessageId: ERROR_REPARSE_TAG_MISMATCH
#
# MessageText:
#
# There is a mismatch between the tag specified in the request and the tag present in the reparse point.
# 
#
ERROR_REPARSE_TAG_MISMATCH = 4394


#/////////////////////////////////////////////////
#                                               //
#         Fast Cache Specific Error Codes       //
#                                               //
#                 4400 to 4419                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_APP_DATA_NOT_FOUND
#
# MessageText:
#
# Fast Cache data not found.
#
ERROR_APP_DATA_NOT_FOUND = 4400

#
# MessageId: ERROR_APP_DATA_EXPIRED
#
# MessageText:
#
# Fast Cache data expired.
#
ERROR_APP_DATA_EXPIRED = 4401

#
# MessageId: ERROR_APP_DATA_CORRUPT
#
# MessageText:
#
# Fast Cache data corrupt.
#
ERROR_APP_DATA_CORRUPT = 4402

#
# MessageId: ERROR_APP_DATA_LIMIT_EXCEEDED
#
# MessageText:
#
# Fast Cache data has exceeded its max size and cannot be updated.
#
ERROR_APP_DATA_LIMIT_EXCEEDED = 4403

#
# MessageId: ERROR_APP_DATA_REBOOT_REQUIRED
#
# MessageText:
#
# Fast Cache has been ReArmed and requires a reboot until it can be updated.
#
ERROR_APP_DATA_REBOOT_REQUIRED = 4404


#/////////////////////////////////////////////////
#                                               //
#             SecureBoot Error codes            //
#                                               //
#                 4420 to 4439                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_SECUREBOOT_ROLLBACK_DETECTED
#
# MessageText:
#
# Secure Boot detected that rollback of protected data has been attempted.
#
ERROR_SECUREBOOT_ROLLBACK_DETECTED = 4420

#
# MessageId: ERROR_SECUREBOOT_POLICY_VIOLATION
#
# MessageText:
#
# The value is protected by Secure Boot policy and cannot be modified or deleted.
#
ERROR_SECUREBOOT_POLICY_VIOLATION = 4421

#
# MessageId: ERROR_SECUREBOOT_INVALID_POLICY
#
# MessageText:
#
# The Secure Boot policy is invalid.
#
ERROR_SECUREBOOT_INVALID_POLICY = 4422

#
# MessageId: ERROR_SECUREBOOT_POLICY_PUBLISHER_NOT_FOUND
#
# MessageText:
#
# A new Secure Boot policy did not contain the current publisher on its update list.
#
ERROR_SECUREBOOT_POLICY_PUBLISHER_NOT_FOUND = 4423

#
# MessageId: ERROR_SECUREBOOT_POLICY_NOT_SIGNED
#
# MessageText:
#
# The Secure Boot policy is either not signed or is signed by a non-trusted signer.
#
ERROR_SECUREBOOT_POLICY_NOT_SIGNED = 4424

#
# MessageId: ERROR_SECUREBOOT_NOT_ENABLED
#
# MessageText:
#
# Secure Boot is not enabled on this machine.
#
ERROR_SECUREBOOT_NOT_ENABLED = 4425

#
# MessageId: ERROR_SECUREBOOT_FILE_REPLACED
#
# MessageText:
#
# Secure Boot requires that certain files and drivers are not replaced by other files or drivers.
#
ERROR_SECUREBOOT_FILE_REPLACED = 4426


#/////////////////////////////////////////////////
#                                               //
#   File System Supported Features Error Codes  //
#                                               //
#                 4440 to 4499                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_OFFLOAD_READ_FLT_NOT_SUPPORTED
#
# MessageText:
#
# The copy offload read operation is not supported by a filter.
#
ERROR_OFFLOAD_READ_FLT_NOT_SUPPORTED = 4440

#
# MessageId: ERROR_OFFLOAD_WRITE_FLT_NOT_SUPPORTED
#
# MessageText:
#
# The copy offload write operation is not supported by a filter.
#
ERROR_OFFLOAD_WRITE_FLT_NOT_SUPPORTED = 4441

#
# MessageId: ERROR_OFFLOAD_READ_FILE_NOT_SUPPORTED
#
# MessageText:
#
# The copy offload read operation is not supported for the file.
#
ERROR_OFFLOAD_READ_FILE_NOT_SUPPORTED = 4442

#
# MessageId: ERROR_OFFLOAD_WRITE_FILE_NOT_SUPPORTED
#
# MessageText:
#
# The copy offload write operation is not supported for the file.
#
ERROR_OFFLOAD_WRITE_FILE_NOT_SUPPORTED = 4443


#/////////////////////////////////////////////////
#                                               //
#    Single Instance Store (SIS) Error codes    //
#                                               //
#                 4500 to 4549                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_VOLUME_NOT_SIS_ENABLED
#
# MessageText:
#
# Single Instance Storage is not available on this volume.
#
ERROR_VOLUME_NOT_SIS_ENABLED = 4500

#/////////////////////////////////////////////////
#                                               //
#                  Available                    //
#                                               //
#                 4550 to 4599                  //
#/////////////////////////////////////////////////

#/////////////////////////////////////////////////
#                                               //
#             Cluster Error codes               //
#                                               //
#                 5000 to 5999                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_DEPENDENT_RESOURCE_EXISTS
#
# MessageText:
#
# The operation cannot be completed because other resources are dependent on this resource.
#
ERROR_DEPENDENT_RESOURCE_EXISTS = 5001

#
# MessageId: ERROR_DEPENDENCY_NOT_FOUND
#
# MessageText:
#
# The cluster resource dependency cannot be found.
#
ERROR_DEPENDENCY_NOT_FOUND = 5002

#
# MessageId: ERROR_DEPENDENCY_ALREADY_EXISTS
#
# MessageText:
#
# The cluster resource cannot be made dependent on the specified resource because it is already dependent.
#
ERROR_DEPENDENCY_ALREADY_EXISTS = 5003

#
# MessageId: ERROR_RESOURCE_NOT_ONLINE
#
# MessageText:
#
# The cluster resource is not online.
#
ERROR_RESOURCE_NOT_ONLINE = 5004

#
# MessageId: ERROR_HOST_NODE_NOT_AVAILABLE
#
# MessageText:
#
# A cluster node is not available for this operation.
#
ERROR_HOST_NODE_NOT_AVAILABLE = 5005

#
# MessageId: ERROR_RESOURCE_NOT_AVAILABLE
#
# MessageText:
#
# The cluster resource is not available.
#
ERROR_RESOURCE_NOT_AVAILABLE = 5006

#
# MessageId: ERROR_RESOURCE_NOT_FOUND
#
# MessageText:
#
# The cluster resource could not be found.
#
ERROR_RESOURCE_NOT_FOUND = 5007

#
# MessageId: ERROR_SHUTDOWN_CLUSTER
#
# MessageText:
#
# The cluster is being shut down.
#
ERROR_SHUTDOWN_CLUSTER = 5008

#
# MessageId: ERROR_CANT_EVICT_ACTIVE_NODE
#
# MessageText:
#
# A cluster node cannot be evicted from the cluster unless the node is down or it is the last node.
#
ERROR_CANT_EVICT_ACTIVE_NODE = 5009

#
# MessageId: ERROR_OBJECT_ALREADY_EXISTS
#
# MessageText:
#
# The object already exists.
#
ERROR_OBJECT_ALREADY_EXISTS = 5010

#
# MessageId: ERROR_OBJECT_IN_LIST
#
# MessageText:
#
# The object is already in the list.
#
ERROR_OBJECT_IN_LIST = 5011

#
# MessageId: ERROR_GROUP_NOT_AVAILABLE
#
# MessageText:
#
# The cluster group is not available for any new requests.
#
ERROR_GROUP_NOT_AVAILABLE = 5012

#
# MessageId: ERROR_GROUP_NOT_FOUND
#
# MessageText:
#
# The cluster group could not be found.
#
ERROR_GROUP_NOT_FOUND = 5013

#
# MessageId: ERROR_GROUP_NOT_ONLINE
#
# MessageText:
#
# The operation could not be completed because the cluster group is not online.
#
ERROR_GROUP_NOT_ONLINE = 5014

#
# MessageId: ERROR_HOST_NODE_NOT_RESOURCE_OWNER
#
# MessageText:
#
# The operation failed because either the specified cluster node is not the owner of the resource, or the node is not a possible owner of the resource.
#
ERROR_HOST_NODE_NOT_RESOURCE_OWNER = 5015

#
# MessageId: ERROR_HOST_NODE_NOT_GROUP_OWNER
#
# MessageText:
#
# The operation failed because either the specified cluster node is not the owner of the group, or the node is not a possible owner of the group.
#
ERROR_HOST_NODE_NOT_GROUP_OWNER = 5016

#
# MessageId: ERROR_RESMON_CREATE_FAILED
#
# MessageText:
#
# The cluster resource could not be created in the specified resource monitor.
#
ERROR_RESMON_CREATE_FAILED = 5017

#
# MessageId: ERROR_RESMON_ONLINE_FAILED
#
# MessageText:
#
# The cluster resource could not be brought online by the resource monitor.
#
ERROR_RESMON_ONLINE_FAILED = 5018

#
# MessageId: ERROR_RESOURCE_ONLINE
#
# MessageText:
#
# The operation could not be completed because the cluster resource is online.
#
ERROR_RESOURCE_ONLINE = 5019

#
# MessageId: ERROR_QUORUM_RESOURCE
#
# MessageText:
#
# The cluster resource could not be deleted or brought offline because it is the quorum resource.
#
ERROR_QUORUM_RESOURCE = 5020

#
# MessageId: ERROR_NOT_QUORUM_CAPABLE
#
# MessageText:
#
# The cluster could not make the specified resource a quorum resource because it is not capable of being a quorum resource.
#
ERROR_NOT_QUORUM_CAPABLE = 5021

#
# MessageId: ERROR_CLUSTER_SHUTTING_DOWN
#
# MessageText:
#
# The cluster software is shutting down.
#
ERROR_CLUSTER_SHUTTING_DOWN = 5022

#
# MessageId: ERROR_INVALID_STATE
#
# MessageText:
#
# The group or resource is not in the correct state to perform the requested operation.
#
ERROR_INVALID_STATE = 5023

#
# MessageId: ERROR_RESOURCE_PROPERTIES_STORED
#
# MessageText:
#
# The properties were stored but not all changes will take effect until the next time the resource is brought online.
#
ERROR_RESOURCE_PROPERTIES_STORED = 5024

#
# MessageId: ERROR_NOT_QUORUM_CLASS
#
# MessageText:
#
# The cluster could not make the specified resource a quorum resource because it does not belong to a shared storage class.
#
ERROR_NOT_QUORUM_CLASS = 5025

#
# MessageId: ERROR_CORE_RESOURCE
#
# MessageText:
#
# The cluster resource could not be deleted since it is a core resource.
#
ERROR_CORE_RESOURCE = 5026

#
# MessageId: ERROR_QUORUM_RESOURCE_ONLINE_FAILED
#
# MessageText:
#
# The quorum resource failed to come online.
#
ERROR_QUORUM_RESOURCE_ONLINE_FAILED = 5027

#
# MessageId: ERROR_QUORUMLOG_OPEN_FAILED
#
# MessageText:
#
# The quorum log could not be created or mounted successfully.
#
ERROR_QUORUMLOG_OPEN_FAILED = 5028

#
# MessageId: ERROR_CLUSTERLOG_CORRUPT
#
# MessageText:
#
# The cluster log is corrupt.
#
ERROR_CLUSTERLOG_CORRUPT = 5029

#
# MessageId: ERROR_CLUSTERLOG_RECORD_EXCEEDS_MAXSIZE
#
# MessageText:
#
# The record could not be written to the cluster log since it exceeds the maximum size.
#
ERROR_CLUSTERLOG_RECORD_EXCEEDS_MAXSIZE = 5030

#
# MessageId: ERROR_CLUSTERLOG_EXCEEDS_MAXSIZE
#
# MessageText:
#
# The cluster log exceeds its maximum size.
#
ERROR_CLUSTERLOG_EXCEEDS_MAXSIZE = 5031

#
# MessageId: ERROR_CLUSTERLOG_CHKPOINT_NOT_FOUND
#
# MessageText:
#
# No checkpoint record was found in the cluster log.
#
ERROR_CLUSTERLOG_CHKPOINT_NOT_FOUND = 5032

#
# MessageId: ERROR_CLUSTERLOG_NOT_ENOUGH_SPACE
#
# MessageText:
#
# The minimum required disk space needed for logging is not available.
#
ERROR_CLUSTERLOG_NOT_ENOUGH_SPACE = 5033

#
# MessageId: ERROR_QUORUM_OWNER_ALIVE
#
# MessageText:
#
# The cluster node failed to take control of the quorum resource because the resource is owned by another active node.
#
ERROR_QUORUM_OWNER_ALIVE = 5034

#
# MessageId: ERROR_NETWORK_NOT_AVAILABLE
#
# MessageText:
#
# A cluster network is not available for this operation.
#
ERROR_NETWORK_NOT_AVAILABLE = 5035

#
# MessageId: ERROR_NODE_NOT_AVAILABLE
#
# MessageText:
#
# A cluster node is not available for this operation.
#
ERROR_NODE_NOT_AVAILABLE = 5036

#
# MessageId: ERROR_ALL_NODES_NOT_AVAILABLE
#
# MessageText:
#
# All cluster nodes must be running to perform this operation.
#
ERROR_ALL_NODES_NOT_AVAILABLE = 5037

#
# MessageId: ERROR_RESOURCE_FAILED
#
# MessageText:
#
# A cluster resource failed.
#
ERROR_RESOURCE_FAILED = 5038

#
# MessageId: ERROR_CLUSTER_INVALID_NODE
#
# MessageText:
#
# The cluster node is not valid.
#
ERROR_CLUSTER_INVALID_NODE = 5039

#
# MessageId: ERROR_CLUSTER_NODE_EXISTS
#
# MessageText:
#
# The cluster node already exists.
#
ERROR_CLUSTER_NODE_EXISTS = 5040

#
# MessageId: ERROR_CLUSTER_JOIN_IN_PROGRESS
#
# MessageText:
#
# A node is in the process of joining the cluster.
#
ERROR_CLUSTER_JOIN_IN_PROGRESS = 5041

#
# MessageId: ERROR_CLUSTER_NODE_NOT_FOUND
#
# MessageText:
#
# The cluster node was not found.
#
ERROR_CLUSTER_NODE_NOT_FOUND = 5042

#
# MessageId: ERROR_CLUSTER_LOCAL_NODE_NOT_FOUND
#
# MessageText:
#
# The cluster local node information was not found.
#
ERROR_CLUSTER_LOCAL_NODE_NOT_FOUND = 5043

#
# MessageId: ERROR_CLUSTER_NETWORK_EXISTS
#
# MessageText:
#
# The cluster network already exists.
#
ERROR_CLUSTER_NETWORK_EXISTS = 5044

#
# MessageId: ERROR_CLUSTER_NETWORK_NOT_FOUND
#
# MessageText:
#
# The cluster network was not found.
#
ERROR_CLUSTER_NETWORK_NOT_FOUND = 5045

#
# MessageId: ERROR_CLUSTER_NETINTERFACE_EXISTS
#
# MessageText:
#
# The cluster network interface already exists.
#
ERROR_CLUSTER_NETINTERFACE_EXISTS = 5046

#
# MessageId: ERROR_CLUSTER_NETINTERFACE_NOT_FOUND
#
# MessageText:
#
# The cluster network interface was not found.
#
ERROR_CLUSTER_NETINTERFACE_NOT_FOUND = 5047

#
# MessageId: ERROR_CLUSTER_INVALID_REQUEST
#
# MessageText:
#
# The cluster request is not valid for this object.
#
ERROR_CLUSTER_INVALID_REQUEST = 5048

#
# MessageId: ERROR_CLUSTER_INVALID_NETWORK_PROVIDER
#
# MessageText:
#
# The cluster network provider is not valid.
#
ERROR_CLUSTER_INVALID_NETWORK_PROVIDER = 5049

#
# MessageId: ERROR_CLUSTER_NODE_DOWN
#
# MessageText:
#
# The cluster node is down.
#
ERROR_CLUSTER_NODE_DOWN = 5050

#
# MessageId: ERROR_CLUSTER_NODE_UNREACHABLE
#
# MessageText:
#
# The cluster node is not reachable.
#
ERROR_CLUSTER_NODE_UNREACHABLE = 5051

#
# MessageId: ERROR_CLUSTER_NODE_NOT_MEMBER
#
# MessageText:
#
# The cluster node is not a member of the cluster.
#
ERROR_CLUSTER_NODE_NOT_MEMBER = 5052

#
# MessageId: ERROR_CLUSTER_JOIN_NOT_IN_PROGRESS
#
# MessageText:
#
# A cluster join operation is not in progress.
#
ERROR_CLUSTER_JOIN_NOT_IN_PROGRESS = 5053

#
# MessageId: ERROR_CLUSTER_INVALID_NETWORK
#
# MessageText:
#
# The cluster network is not valid.
#
ERROR_CLUSTER_INVALID_NETWORK = 5054

#
# MessageId: ERROR_CLUSTER_NODE_UP
#
# MessageText:
#
# The cluster node is up.
#
ERROR_CLUSTER_NODE_UP = 5056

#
# MessageId: ERROR_CLUSTER_IPADDR_IN_USE
#
# MessageText:
#
# The cluster IP address is already in use.
#
ERROR_CLUSTER_IPADDR_IN_USE = 5057

#
# MessageId: ERROR_CLUSTER_NODE_NOT_PAUSED
#
# MessageText:
#
# The cluster node is not paused.
#
ERROR_CLUSTER_NODE_NOT_PAUSED = 5058

#
# MessageId: ERROR_CLUSTER_NO_SECURITY_CONTEXT
#
# MessageText:
#
# No cluster security context is available.
#
ERROR_CLUSTER_NO_SECURITY_CONTEXT = 5059

#
# MessageId: ERROR_CLUSTER_NETWORK_NOT_INTERNAL
#
# MessageText:
#
# The cluster network is not configured for internal cluster communication.
#
ERROR_CLUSTER_NETWORK_NOT_INTERNAL = 5060

#
# MessageId: ERROR_CLUSTER_NODE_ALREADY_UP
#
# MessageText:
#
# The cluster node is already up.
#
ERROR_CLUSTER_NODE_ALREADY_UP = 5061

#
# MessageId: ERROR_CLUSTER_NODE_ALREADY_DOWN
#
# MessageText:
#
# The cluster node is already down.
#
ERROR_CLUSTER_NODE_ALREADY_DOWN = 5062

#
# MessageId: ERROR_CLUSTER_NETWORK_ALREADY_ONLINE
#
# MessageText:
#
# The cluster network is already online.
#
ERROR_CLUSTER_NETWORK_ALREADY_ONLINE = 5063

#
# MessageId: ERROR_CLUSTER_NETWORK_ALREADY_OFFLINE
#
# MessageText:
#
# The cluster network is already offline.
#
ERROR_CLUSTER_NETWORK_ALREADY_OFFLINE = 5064

#
# MessageId: ERROR_CLUSTER_NODE_ALREADY_MEMBER
#
# MessageText:
#
# The cluster node is already a member of the cluster.
#
ERROR_CLUSTER_NODE_ALREADY_MEMBER = 5065

#
# MessageId: ERROR_CLUSTER_LAST_INTERNAL_NETWORK
#
# MessageText:
#
# The cluster network is the only one configured for internal cluster communication between two or more active cluster nodes. The internal communication capability cannot be removed from the network.
#
ERROR_CLUSTER_LAST_INTERNAL_NETWORK = 5066

#
# MessageId: ERROR_CLUSTER_NETWORK_HAS_DEPENDENTS
#
# MessageText:
#
# One or more cluster resources depend on the network to provide service to clients. The client access capability cannot be removed from the network.
#
ERROR_CLUSTER_NETWORK_HAS_DEPENDENTS = 5067

#
# MessageId: ERROR_INVALID_OPERATION_ON_QUORUM
#
# MessageText:
#
# This operation cannot currently be performed on the cluster group containing the quorum resource.
#
ERROR_INVALID_OPERATION_ON_QUORUM = 5068

#
# MessageId: ERROR_DEPENDENCY_NOT_ALLOWED
#
# MessageText:
#
# The cluster quorum resource is not allowed to have any dependencies.
#
ERROR_DEPENDENCY_NOT_ALLOWED = 5069

#
# MessageId: ERROR_CLUSTER_NODE_PAUSED
#
# MessageText:
#
# The cluster node is paused.
#
ERROR_CLUSTER_NODE_PAUSED = 5070

#
# MessageId: ERROR_NODE_CANT_HOST_RESOURCE
#
# MessageText:
#
# The cluster resource cannot be brought online. The owner node cannot run this resource.
#
ERROR_NODE_CANT_HOST_RESOURCE = 5071

#
# MessageId: ERROR_CLUSTER_NODE_NOT_READY
#
# MessageText:
#
# The cluster node is not ready to perform the requested operation.
#
ERROR_CLUSTER_NODE_NOT_READY = 5072

#
# MessageId: ERROR_CLUSTER_NODE_SHUTTING_DOWN
#
# MessageText:
#
# The cluster node is shutting down.
#
ERROR_CLUSTER_NODE_SHUTTING_DOWN = 5073

#
# MessageId: ERROR_CLUSTER_JOIN_ABORTED
#
# MessageText:
#
# The cluster join operation was aborted.
#
ERROR_CLUSTER_JOIN_ABORTED = 5074

#
# MessageId: ERROR_CLUSTER_INCOMPATIBLE_VERSIONS
#
# MessageText:
#
# The cluster join operation failed due to incompatible software versions between the joining node and its sponsor.
#
ERROR_CLUSTER_INCOMPATIBLE_VERSIONS = 5075

#
# MessageId: ERROR_CLUSTER_MAXNUM_OF_RESOURCES_EXCEEDED
#
# MessageText:
#
# This resource cannot be created because the cluster has reached the limit on the number of resources it can monitor.
#
ERROR_CLUSTER_MAXNUM_OF_RESOURCES_EXCEEDED = 5076

#
# MessageId: ERROR_CLUSTER_SYSTEM_CONFIG_CHANGED
#
# MessageText:
#
# The system configuration changed during the cluster join or form operation. The join or form operation was aborted.
#
ERROR_CLUSTER_SYSTEM_CONFIG_CHANGED = 5077

#
# MessageId: ERROR_CLUSTER_RESOURCE_TYPE_NOT_FOUND
#
# MessageText:
#
# The specified resource type was not found.
#
ERROR_CLUSTER_RESOURCE_TYPE_NOT_FOUND = 5078

#
# MessageId: ERROR_CLUSTER_RESTYPE_NOT_SUPPORTED
#
# MessageText:
#
# The specified node does not support a resource of this type. This may be due to version inconsistencies or due to the absence of the resource DLL on this node.
#
ERROR_CLUSTER_RESTYPE_NOT_SUPPORTED = 5079

#
# MessageId: ERROR_CLUSTER_RESNAME_NOT_FOUND
#
# MessageText:
#
# The specified resource name is not supported by this resource DLL. This may be due to a bad (or changed) name supplied to the resource DLL.
#
ERROR_CLUSTER_RESNAME_NOT_FOUND = 5080

#
# MessageId: ERROR_CLUSTER_NO_RPC_PACKAGES_REGISTERED
#
# MessageText:
#
# No authentication package could be registered with the RPC server.
#
ERROR_CLUSTER_NO_RPC_PACKAGES_REGISTERED = 5081

#
# MessageId: ERROR_CLUSTER_OWNER_NOT_IN_PREFLIST
#
# MessageText:
#
# You cannot bring the group online because the owner of the group is not in the preferred list for the group. To change the owner node for the group, move the group.
#
ERROR_CLUSTER_OWNER_NOT_IN_PREFLIST = 5082

#
# MessageId: ERROR_CLUSTER_DATABASE_SEQMISMATCH
#
# MessageText:
#
# The join operation failed because the cluster database sequence number has changed or is incompatible with the locker node. This may happen during a join operation if the cluster database was changing during the join.
#
ERROR_CLUSTER_DATABASE_SEQMISMATCH = 5083

#
# MessageId: ERROR_RESMON_INVALID_STATE
#
# MessageText:
#
# The resource monitor will not allow the fail operation to be performed while the resource is in its current state. This may happen if the resource is in a pending state.
#
ERROR_RESMON_INVALID_STATE = 5084

#
# MessageId: ERROR_CLUSTER_GUM_NOT_LOCKER
#
# MessageText:
#
# A non locker code got a request to reserve the lock for making global updates.
#
ERROR_CLUSTER_GUM_NOT_LOCKER = 5085

#
# MessageId: ERROR_QUORUM_DISK_NOT_FOUND
#
# MessageText:
#
# The quorum disk could not be located by the cluster service.
#
ERROR_QUORUM_DISK_NOT_FOUND = 5086

#
# MessageId: ERROR_DATABASE_BACKUP_CORRUPT
#
# MessageText:
#
# The backed up cluster database is possibly corrupt.
#
ERROR_DATABASE_BACKUP_CORRUPT = 5087

#
# MessageId: ERROR_CLUSTER_NODE_ALREADY_HAS_DFS_ROOT
#
# MessageText:
#
# A DFS root already exists in this cluster node.
#
ERROR_CLUSTER_NODE_ALREADY_HAS_DFS_ROOT = 5088

#
# MessageId: ERROR_RESOURCE_PROPERTY_UNCHANGEABLE
#
# MessageText:
#
# An attempt to modify a resource property failed because it conflicts with another existing property.
#
ERROR_RESOURCE_PROPERTY_UNCHANGEABLE = 5089

#
# MessageId: ERROR_NO_ADMIN_ACCESS_POINT
#
# MessageText:
#
# This operation is not supported on a cluster without an Administrator Access Point.
#
ERROR_NO_ADMIN_ACCESS_POINT = 5090

# /*
#  Codes from 4300 through 5889 overlap with codes in ds\published\inc\apperr2.w.
#  Do not add any more error codes in that range.
# */
#
# MessageId: ERROR_CLUSTER_MEMBERSHIP_INVALID_STATE
#
# MessageText:
#
# An operation was attempted that is incompatible with the current membership state of the node.
#
ERROR_CLUSTER_MEMBERSHIP_INVALID_STATE = 5890

#
# MessageId: ERROR_CLUSTER_QUORUMLOG_NOT_FOUND
#
# MessageText:
#
# The quorum resource does not contain the quorum log.
#
ERROR_CLUSTER_QUORUMLOG_NOT_FOUND = 5891

#
# MessageId: ERROR_CLUSTER_MEMBERSHIP_HALT
#
# MessageText:
#
# The membership engine requested shutdown of the cluster service on this node.
#
ERROR_CLUSTER_MEMBERSHIP_HALT = 5892

#
# MessageId: ERROR_CLUSTER_INSTANCE_ID_MISMATCH
#
# MessageText:
#
# The join operation failed because the cluster instance ID of the joining node does not match the cluster instance ID of the sponsor node.
#
ERROR_CLUSTER_INSTANCE_ID_MISMATCH = 5893

#
# MessageId: ERROR_CLUSTER_NETWORK_NOT_FOUND_FOR_IP
#
# MessageText:
#
# A matching cluster network for the specified IP address could not be found.
#
ERROR_CLUSTER_NETWORK_NOT_FOUND_FOR_IP = 5894

#
# MessageId: ERROR_CLUSTER_PROPERTY_DATA_TYPE_MISMATCH
#
# MessageText:
#
# The actual data type of the property did not match the expected data type of the property.
#
ERROR_CLUSTER_PROPERTY_DATA_TYPE_MISMATCH = 5895

#
# MessageId: ERROR_CLUSTER_EVICT_WITHOUT_CLEANUP
#
# MessageText:
#
# The cluster node was evicted from the cluster successfully, but the node was not cleaned up. To determine what cleanup steps failed and how to recover, see the Failover Clustering application event log using Event Viewer.
#
ERROR_CLUSTER_EVICT_WITHOUT_CLEANUP = 5896

#
# MessageId: ERROR_CLUSTER_PARAMETER_MISMATCH
#
# MessageText:
#
# Two or more parameter values specified for a resource's properties are in conflict.
#
ERROR_CLUSTER_PARAMETER_MISMATCH = 5897

#
# MessageId: ERROR_NODE_CANNOT_BE_CLUSTERED
#
# MessageText:
#
# This computer cannot be made a member of a cluster.
#
ERROR_NODE_CANNOT_BE_CLUSTERED = 5898

#
# MessageId: ERROR_CLUSTER_WRONG_OS_VERSION
#
# MessageText:
#
# This computer cannot be made a member of a cluster because it does not have the correct version of Windows installed.
#
ERROR_CLUSTER_WRONG_OS_VERSION = 5899

#
# MessageId: ERROR_CLUSTER_CANT_CREATE_DUP_CLUSTER_NAME
#
# MessageText:
#
# A cluster cannot be created with the specified cluster name because that cluster name is already in use. Specify a different name for the cluster.
#
ERROR_CLUSTER_CANT_CREATE_DUP_CLUSTER_NAME = 5900

#
# MessageId: ERROR_CLUSCFG_ALREADY_COMMITTED
#
# MessageText:
#
# The cluster configuration action has already been committed.
#
ERROR_CLUSCFG_ALREADY_COMMITTED = 5901

#
# MessageId: ERROR_CLUSCFG_ROLLBACK_FAILED
#
# MessageText:
#
# The cluster configuration action could not be rolled back.
#
ERROR_CLUSCFG_ROLLBACK_FAILED = 5902

#
# MessageId: ERROR_CLUSCFG_SYSTEM_DISK_DRIVE_LETTER_CONFLICT
#
# MessageText:
#
# The drive letter assigned to a system disk on one node conflicted with the drive letter assigned to a disk on another node.
#
ERROR_CLUSCFG_SYSTEM_DISK_DRIVE_LETTER_CONFLICT = 5903

#
# MessageId: ERROR_CLUSTER_OLD_VERSION
#
# MessageText:
#
# One or more nodes in the cluster are running a version of Windows that does not support this operation.
#
ERROR_CLUSTER_OLD_VERSION = 5904

#
# MessageId: ERROR_CLUSTER_MISMATCHED_COMPUTER_ACCT_NAME
#
# MessageText:
#
# The name of the corresponding computer account doesn't match the Network Name for this resource.
#
ERROR_CLUSTER_MISMATCHED_COMPUTER_ACCT_NAME = 5905

#
# MessageId: ERROR_CLUSTER_NO_NET_ADAPTERS
#
# MessageText:
#
# No network adapters are available.
#
ERROR_CLUSTER_NO_NET_ADAPTERS = 5906

#
# MessageId: ERROR_CLUSTER_POISONED
#
# MessageText:
#
# The cluster node has been poisoned.
#
ERROR_CLUSTER_POISONED = 5907

#
# MessageId: ERROR_CLUSTER_GROUP_MOVING
#
# MessageText:
#
# The group is unable to accept the request since it is moving to another node.
#
ERROR_CLUSTER_GROUP_MOVING = 5908

#
# MessageId: ERROR_CLUSTER_RESOURCE_TYPE_BUSY
#
# MessageText:
#
# The resource type cannot accept the request since is too busy performing another operation.
#
ERROR_CLUSTER_RESOURCE_TYPE_BUSY = 5909

#
# MessageId: ERROR_RESOURCE_CALL_TIMED_OUT
#
# MessageText:
#
# The call to the cluster resource DLL timed out.
#
ERROR_RESOURCE_CALL_TIMED_OUT = 5910

#
# MessageId: ERROR_INVALID_CLUSTER_IPV6_ADDRESS
#
# MessageText:
#
# The address is not valid for an IPv6 Address resource. A global IPv6 address is required, and it must match a cluster network. Compatibility addresses are not permitted.
#
ERROR_INVALID_CLUSTER_IPV6_ADDRESS = 5911

#
# MessageId: ERROR_CLUSTER_INTERNAL_INVALID_FUNCTION
#
# MessageText:
#
# An internal cluster error occurred. A call to an invalid function was attempted.
#
ERROR_CLUSTER_INTERNAL_INVALID_FUNCTION = 5912

#
# MessageId: ERROR_CLUSTER_PARAMETER_OUT_OF_BOUNDS
#
# MessageText:
#
# A parameter value is out of acceptable range.
#
ERROR_CLUSTER_PARAMETER_OUT_OF_BOUNDS = 5913

#
# MessageId: ERROR_CLUSTER_PARTIAL_SEND
#
# MessageText:
#
# A network error occurred while sending data to another node in the cluster. The number of bytes transmitted was less than required.
#
ERROR_CLUSTER_PARTIAL_SEND = 5914

#
# MessageId: ERROR_CLUSTER_REGISTRY_INVALID_FUNCTION
#
# MessageText:
#
# An invalid cluster registry operation was attempted.
#
ERROR_CLUSTER_REGISTRY_INVALID_FUNCTION = 5915

#
# MessageId: ERROR_CLUSTER_INVALID_STRING_TERMINATION
#
# MessageText:
#
# An input string of characters is not properly terminated.
#
ERROR_CLUSTER_INVALID_STRING_TERMINATION = 5916

#
# MessageId: ERROR_CLUSTER_INVALID_STRING_FORMAT
#
# MessageText:
#
# An input string of characters is not in a valid format for the data it represents.
#
ERROR_CLUSTER_INVALID_STRING_FORMAT = 5917

#
# MessageId: ERROR_CLUSTER_DATABASE_TRANSACTION_IN_PROGRESS
#
# MessageText:
#
# An internal cluster error occurred. A cluster database transaction was attempted while a transaction was already in progress.
#
ERROR_CLUSTER_DATABASE_TRANSACTION_IN_PROGRESS = 5918

#
# MessageId: ERROR_CLUSTER_DATABASE_TRANSACTION_NOT_IN_PROGRESS
#
# MessageText:
#
# An internal cluster error occurred. There was an attempt to commit a cluster database transaction while no transaction was in progress.
#
ERROR_CLUSTER_DATABASE_TRANSACTION_NOT_IN_PROGRESS = 5919

#
# MessageId: ERROR_CLUSTER_NULL_DATA
#
# MessageText:
#
# An internal cluster error occurred. Data was not properly initialized.
#
ERROR_CLUSTER_NULL_DATA = 5920

#
# MessageId: ERROR_CLUSTER_PARTIAL_READ
#
# MessageText:
#
# An error occurred while reading from a stream of data. An unexpected number of bytes was returned.
#
ERROR_CLUSTER_PARTIAL_READ = 5921

#
# MessageId: ERROR_CLUSTER_PARTIAL_WRITE
#
# MessageText:
#
# An error occurred while writing to a stream of data. The required number of bytes could not be written.
#
ERROR_CLUSTER_PARTIAL_WRITE = 5922

#
# MessageId: ERROR_CLUSTER_CANT_DESERIALIZE_DATA
#
# MessageText:
#
# An error occurred while deserializing a stream of cluster data.
#
ERROR_CLUSTER_CANT_DESERIALIZE_DATA = 5923

#
# MessageId: ERROR_DEPENDENT_RESOURCE_PROPERTY_CONFLICT
#
# MessageText:
#
# One or more property values for this resource are in conflict with one or more property values associated with its dependent resource(s).
#
ERROR_DEPENDENT_RESOURCE_PROPERTY_CONFLICT = 5924

#
# MessageId: ERROR_CLUSTER_NO_QUORUM
#
# MessageText:
#
# A quorum of cluster nodes was not present to form a cluster.
#
ERROR_CLUSTER_NO_QUORUM = 5925

#
# MessageId: ERROR_CLUSTER_INVALID_IPV6_NETWORK
#
# MessageText:
#
# The cluster network is not valid for an IPv6 Address resource, or it does not match the configured address.
#
ERROR_CLUSTER_INVALID_IPV6_NETWORK = 5926

#
# MessageId: ERROR_CLUSTER_INVALID_IPV6_TUNNEL_NETWORK
#
# MessageText:
#
# The cluster network is not valid for an IPv6 Tunnel resource. Check the configuration of the IP Address resource on which the IPv6 Tunnel resource depends.
#
ERROR_CLUSTER_INVALID_IPV6_TUNNEL_NETWORK = 5927

#
# MessageId: ERROR_QUORUM_NOT_ALLOWED_IN_THIS_GROUP
#
# MessageText:
#
# Quorum resource cannot reside in the Available Storage group.
#
ERROR_QUORUM_NOT_ALLOWED_IN_THIS_GROUP = 5928

#
# MessageId: ERROR_DEPENDENCY_TREE_TOO_COMPLEX
#
# MessageText:
#
# The dependencies for this resource are nested too deeply.
#
ERROR_DEPENDENCY_TREE_TOO_COMPLEX = 5929

#
# MessageId: ERROR_EXCEPTION_IN_RESOURCE_CALL
#
# MessageText:
#
# The call into the resource DLL raised an unhandled exception.
#
ERROR_EXCEPTION_IN_RESOURCE_CALL = 5930

#
# MessageId: ERROR_CLUSTER_RHS_FAILED_INITIALIZATION
#
# MessageText:
#
# The RHS process failed to initialize.
#
ERROR_CLUSTER_RHS_FAILED_INITIALIZATION = 5931

#
# MessageId: ERROR_CLUSTER_NOT_INSTALLED
#
# MessageText:
#
# The Failover Clustering feature is not installed on this node.
#
ERROR_CLUSTER_NOT_INSTALLED = 5932

#
# MessageId: ERROR_CLUSTER_RESOURCES_MUST_BE_ONLINE_ON_THE_SAME_NODE
#
# MessageText:
#
# The resources must be online on the same node for this operation
#
ERROR_CLUSTER_RESOURCES_MUST_BE_ONLINE_ON_THE_SAME_NODE = 5933

#
# MessageId: ERROR_CLUSTER_MAX_NODES_IN_CLUSTER
#
# MessageText:
#
# A new node can not be added since this cluster is already at its maximum number of nodes.
#
ERROR_CLUSTER_MAX_NODES_IN_CLUSTER = 5934

#
# MessageId: ERROR_CLUSTER_TOO_MANY_NODES
#
# MessageText:
#
# This cluster can not be created since the specified number of nodes exceeds the maximum allowed limit.
#
ERROR_CLUSTER_TOO_MANY_NODES = 5935

#
# MessageId: ERROR_CLUSTER_OBJECT_ALREADY_USED
#
# MessageText:
#
# An attempt to use the specified cluster name failed because an enabled computer object with the given name already exists in the domain.
#
ERROR_CLUSTER_OBJECT_ALREADY_USED = 5936

#
# MessageId: ERROR_NONCORE_GROUPS_FOUND
#
# MessageText:
#
# This cluster cannot be destroyed. It has non-core application groups which must be deleted before the cluster can be destroyed.
#
ERROR_NONCORE_GROUPS_FOUND = 5937

#
# MessageId: ERROR_FILE_SHARE_RESOURCE_CONFLICT
#
# MessageText:
#
# File share associated with file share witness resource cannot be hosted by this cluster or any of its nodes.
#
ERROR_FILE_SHARE_RESOURCE_CONFLICT = 5938

#
# MessageId: ERROR_CLUSTER_EVICT_INVALID_REQUEST
#
# MessageText:
#
# Eviction of this node is invalid at this time. Due to quorum requirements node eviction will result in cluster shutdown.
# If it is the last node in the cluster, destroy cluster command should be used.
#
ERROR_CLUSTER_EVICT_INVALID_REQUEST = 5939

#
# MessageId: ERROR_CLUSTER_SINGLETON_RESOURCE
#
# MessageText:
#
# Only one instance of this resource type is allowed in the cluster.
#
ERROR_CLUSTER_SINGLETON_RESOURCE = 5940

#
# MessageId: ERROR_CLUSTER_GROUP_SINGLETON_RESOURCE
#
# MessageText:
#
# Only one instance of this resource type is allowed per resource group.
#
ERROR_CLUSTER_GROUP_SINGLETON_RESOURCE = 5941

#
# MessageId: ERROR_CLUSTER_RESOURCE_PROVIDER_FAILED
#
# MessageText:
#
# The resource failed to come online due to the failure of one or more provider resources.
#
ERROR_CLUSTER_RESOURCE_PROVIDER_FAILED = 5942

#
# MessageId: ERROR_CLUSTER_RESOURCE_CONFIGURATION_ERROR
#
# MessageText:
#
# The resource has indicated that it cannot come online on any node.
#
ERROR_CLUSTER_RESOURCE_CONFIGURATION_ERROR = 5943

#
# MessageId: ERROR_CLUSTER_GROUP_BUSY
#
# MessageText:
#
# The current operation cannot be performed on this group at this time.
#
ERROR_CLUSTER_GROUP_BUSY = 5944

#
# MessageId: ERROR_CLUSTER_NOT_SHARED_VOLUME
#
# MessageText:
#
# The directory or file is not located on a cluster shared volume.
#
ERROR_CLUSTER_NOT_SHARED_VOLUME = 5945

#
# MessageId: ERROR_CLUSTER_INVALID_SECURITY_DESCRIPTOR
#
# MessageText:
#
# The Security Descriptor does not meet the requirements for a cluster.
#
ERROR_CLUSTER_INVALID_SECURITY_DESCRIPTOR = 5946

#
# MessageId: ERROR_CLUSTER_SHARED_VOLUMES_IN_USE
#
# MessageText:
#
# There is one or more shared volumes resources configured in the cluster.
# Those resources must be moved to available storage in order for operation to succeed.
#
ERROR_CLUSTER_SHARED_VOLUMES_IN_USE = 5947

#
# MessageId: ERROR_CLUSTER_USE_SHARED_VOLUMES_API
#
# MessageText:
#
# This group or resource cannot be directly manipulated.
# Use shared volume APIs to perform desired operation.
#
ERROR_CLUSTER_USE_SHARED_VOLUMES_API = 5948

#
# MessageId: ERROR_CLUSTER_BACKUP_IN_PROGRESS
#
# MessageText:
#
# Back up is in progress. Please wait for backup completion before trying this operation again.
#
ERROR_CLUSTER_BACKUP_IN_PROGRESS = 5949

#
# MessageId: ERROR_NON_CSV_PATH
#
# MessageText:
#
# The path does not belong to a cluster shared volume.
#
ERROR_NON_CSV_PATH = 5950

#
# MessageId: ERROR_CSV_VOLUME_NOT_LOCAL
#
# MessageText:
#
# The cluster shared volume is not locally mounted on this node.
#
ERROR_CSV_VOLUME_NOT_LOCAL = 5951

#
# MessageId: ERROR_CLUSTER_WATCHDOG_TERMINATING
#
# MessageText:
#
# The cluster watchdog is terminating.
#
ERROR_CLUSTER_WATCHDOG_TERMINATING = 5952

#
# MessageId: ERROR_CLUSTER_RESOURCE_VETOED_MOVE_INCOMPATIBLE_NODES
#
# MessageText:
#
# A resource vetoed a move between two nodes because they are incompatible.
#
ERROR_CLUSTER_RESOURCE_VETOED_MOVE_INCOMPATIBLE_NODES = 5953

#
# MessageId: ERROR_CLUSTER_INVALID_NODE_WEIGHT
#
# MessageText:
#
# The request is invalid either because node weight cannot be changed while the cluster is in disk-only quorum mode, or because changing the node weight would violate the minimum cluster quorum requirements.
#
ERROR_CLUSTER_INVALID_NODE_WEIGHT = 5954

#
# MessageId: ERROR_CLUSTER_RESOURCE_VETOED_CALL
#
# MessageText:
#
# The resource vetoed the call.
#
ERROR_CLUSTER_RESOURCE_VETOED_CALL = 5955

#
# MessageId: ERROR_RESMON_SYSTEM_RESOURCES_LACKING
#
# MessageText:
#
# Resource could not start or run because it could not reserve sufficient system resources.
#
ERROR_RESMON_SYSTEM_RESOURCES_LACKING = 5956

#
# MessageId: ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_DESTINATION
#
# MessageText:
#
# A resource vetoed a move between two nodes because the destination currently does not have enough resources to complete the operation.
#
ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_DESTINATION = 5957

#
# MessageId: ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_SOURCE
#
# MessageText:
#
# 
# A resource vetoed a move between two nodes because the source currently does not have enough resources to complete the operation.
#
ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_SOURCE = 5958

#
# MessageId: ERROR_CLUSTER_GROUP_QUEUED
#
# MessageText:
#
# 
# The requested operation can not be completed because the group is queued for an operation.
#
ERROR_CLUSTER_GROUP_QUEUED = 5959

#
# MessageId: ERROR_CLUSTER_RESOURCE_LOCKED_STATUS
#
# MessageText:
#
# 
# The requested operation can not be completed because a resource has locked status.
#
ERROR_CLUSTER_RESOURCE_LOCKED_STATUS = 5960

#
# MessageId: ERROR_CLUSTER_SHARED_VOLUME_FAILOVER_NOT_ALLOWED
#
# MessageText:
#
# 
# The resource cannot move to another node because a cluster shared volume vetoed the operation.
#
ERROR_CLUSTER_SHARED_VOLUME_FAILOVER_NOT_ALLOWED = 5961

#
# MessageId: ERROR_CLUSTER_NODE_DRAIN_IN_PROGRESS
#
# MessageText:
#
# 
# A node drain is already in progress.
#
ERROR_CLUSTER_NODE_DRAIN_IN_PROGRESS = 5962

#
# MessageId: ERROR_CLUSTER_DISK_NOT_CONNECTED
#
# MessageText:
#
# 
# Clustered storage is not connected to the node.
#
ERROR_CLUSTER_DISK_NOT_CONNECTED = 5963

#
# MessageId: ERROR_DISK_NOT_CSV_CAPABLE
#
# MessageText:
#
# 
# The disk is not configured in a way to be used with CSV. CSV disks must have at least one partition that is formatted with NTFS or REFS.
#
ERROR_DISK_NOT_CSV_CAPABLE = 5964

#
# MessageId: ERROR_RESOURCE_NOT_IN_AVAILABLE_STORAGE
#
# MessageText:
#
# 
# The resource must be part of the Available Storage group to complete this action.
#
ERROR_RESOURCE_NOT_IN_AVAILABLE_STORAGE = 5965

#
# MessageId: ERROR_CLUSTER_SHARED_VOLUME_REDIRECTED
#
# MessageText:
#
# 
# CSVFS failed operation as volume is in redirected mode.
#
ERROR_CLUSTER_SHARED_VOLUME_REDIRECTED = 5966

#
# MessageId: ERROR_CLUSTER_SHARED_VOLUME_NOT_REDIRECTED
#
# MessageText:
#
# 
# CSVFS failed operation as volume is not in redirected mode.
#
ERROR_CLUSTER_SHARED_VOLUME_NOT_REDIRECTED = 5967

#
# MessageId: ERROR_CLUSTER_CANNOT_RETURN_PROPERTIES
#
# MessageText:
#
# 
# Cluster properties cannot be returned at this time.
#
ERROR_CLUSTER_CANNOT_RETURN_PROPERTIES = 5968

#
# MessageId: ERROR_CLUSTER_RESOURCE_CONTAINS_UNSUPPORTED_DIFF_AREA_FOR_SHARED_VOLUMES
#
# MessageText:
#
# 
# The clustered disk resource contains software snapshot diff area that are not supported for Cluster Shared Volumes.
#
ERROR_CLUSTER_RESOURCE_CONTAINS_UNSUPPORTED_DIFF_AREA_FOR_SHARED_VOLUMES = 5969

#
# MessageId: ERROR_CLUSTER_RESOURCE_IS_IN_MAINTENANCE_MODE
#
# MessageText:
#
# 
# The operation cannot be completed because the resource is in maintenance mode.
#
ERROR_CLUSTER_RESOURCE_IS_IN_MAINTENANCE_MODE = 5970

#
# MessageId: ERROR_CLUSTER_AFFINITY_CONFLICT
#
# MessageText:
#
# 
# The operation cannot be completed because of cluster affinity conflicts
#
ERROR_CLUSTER_AFFINITY_CONFLICT = 5971

#
# MessageId: ERROR_CLUSTER_RESOURCE_IS_REPLICA_VIRTUAL_MACHINE
#
# MessageText:
#
# 
# The operation cannot be completed because the resource is a replica virtual machine.
#
ERROR_CLUSTER_RESOURCE_IS_REPLICA_VIRTUAL_MACHINE = 5972


#/////////////////////////////////////////////////
#                                               //
#               EFS Error codes                 //
#                                               //
#                 6000 to 6099                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_ENCRYPTION_FAILED
#
# MessageText:
#
# The specified file could not be encrypted.
#
ERROR_ENCRYPTION_FAILED = 6000

#
# MessageId: ERROR_DECRYPTION_FAILED
#
# MessageText:
#
# The specified file could not be decrypted.
#
ERROR_DECRYPTION_FAILED = 6001

#
# MessageId: ERROR_FILE_ENCRYPTED
#
# MessageText:
#
# The specified file is encrypted and the user does not have the ability to decrypt it.
#
ERROR_FILE_ENCRYPTED = 6002

#
# MessageId: ERROR_NO_RECOVERY_POLICY
#
# MessageText:
#
# There is no valid encryption recovery policy configured for this system.
#
ERROR_NO_RECOVERY_POLICY = 6003

#
# MessageId: ERROR_NO_EFS
#
# MessageText:
#
# The required encryption driver is not loaded for this system.
#
ERROR_NO_EFS = 6004

#
# MessageId: ERROR_WRONG_EFS
#
# MessageText:
#
# The file was encrypted with a different encryption driver than is currently loaded.
#
ERROR_WRONG_EFS = 6005

#
# MessageId: ERROR_NO_USER_KEYS
#
# MessageText:
#
# There are no EFS keys defined for the user.
#
ERROR_NO_USER_KEYS = 6006

#
# MessageId: ERROR_FILE_NOT_ENCRYPTED
#
# MessageText:
#
# The specified file is not encrypted.
#
ERROR_FILE_NOT_ENCRYPTED = 6007

#
# MessageId: ERROR_NOT_EXPORT_FORMAT
#
# MessageText:
#
# The specified file is not in the defined EFS export format.
#
ERROR_NOT_EXPORT_FORMAT = 6008

#
# MessageId: ERROR_FILE_READ_ONLY
#
# MessageText:
#
# The specified file is read only.
#
ERROR_FILE_READ_ONLY = 6009

#
# MessageId: ERROR_DIR_EFS_DISALLOWED
#
# MessageText:
#
# The directory has been disabled for encryption.
#
ERROR_DIR_EFS_DISALLOWED = 6010

#
# MessageId: ERROR_EFS_SERVER_NOT_TRUSTED
#
# MessageText:
#
# The server is not trusted for remote encryption operation.
#
ERROR_EFS_SERVER_NOT_TRUSTED = 6011

#
# MessageId: ERROR_BAD_RECOVERY_POLICY
#
# MessageText:
#
# Recovery policy configured for this system contains invalid recovery certificate.
#
ERROR_BAD_RECOVERY_POLICY = 6012

#
# MessageId: ERROR_EFS_ALG_BLOB_TOO_BIG
#
# MessageText:
#
# The encryption algorithm used on the source file needs a bigger key buffer than the one on the destination file.
#
ERROR_EFS_ALG_BLOB_TOO_BIG = 6013

#
# MessageId: ERROR_VOLUME_NOT_SUPPORT_EFS
#
# MessageText:
#
# The disk partition does not support file encryption.
#
ERROR_VOLUME_NOT_SUPPORT_EFS = 6014

#
# MessageId: ERROR_EFS_DISABLED
#
# MessageText:
#
# This machine is disabled for file encryption.
#
ERROR_EFS_DISABLED = 6015

#
# MessageId: ERROR_EFS_VERSION_NOT_SUPPORT
#
# MessageText:
#
# A newer system is required to decrypt this encrypted file.
#
ERROR_EFS_VERSION_NOT_SUPPORT = 6016

#
# MessageId: ERROR_CS_ENCRYPTION_INVALID_SERVER_RESPONSE
#
# MessageText:
#
# The remote server sent an invalid response for a file being opened with Client Side Encryption.
#
ERROR_CS_ENCRYPTION_INVALID_SERVER_RESPONSE = 6017

#
# MessageId: ERROR_CS_ENCRYPTION_UNSUPPORTED_SERVER
#
# MessageText:
#
# Client Side Encryption is not supported by the remote server even though it claims to support it.
#
ERROR_CS_ENCRYPTION_UNSUPPORTED_SERVER = 6018

#
# MessageId: ERROR_CS_ENCRYPTION_EXISTING_ENCRYPTED_FILE
#
# MessageText:
#
# File is encrypted and should be opened in Client Side Encryption mode.
#
ERROR_CS_ENCRYPTION_EXISTING_ENCRYPTED_FILE = 6019

#
# MessageId: ERROR_CS_ENCRYPTION_NEW_ENCRYPTED_FILE
#
# MessageText:
#
# A new encrypted file is being created and a $EFS needs to be provided.
#
ERROR_CS_ENCRYPTION_NEW_ENCRYPTED_FILE = 6020

#
# MessageId: ERROR_CS_ENCRYPTION_FILE_NOT_CSE
#
# MessageText:
#
# The SMB client requested a CSE FSCTL on a non-CSE file.
#
ERROR_CS_ENCRYPTION_FILE_NOT_CSE = 6021

#
# MessageId: ERROR_ENCRYPTION_POLICY_DENIES_OPERATION
#
# MessageText:
#
# The requested operation was blocked by policy. For more information, contact your system administrator.
#
ERROR_ENCRYPTION_POLICY_DENIES_OPERATION = 6022


#/////////////////////////////////////////////////
#                                               //
#              BROWSER Error codes              //
#                                               //
#                 6100 to 6199                  //
#/////////////////////////////////////////////////

# This message number is for historical purposes and cannot be changed or re-used.
#
# MessageId: ERROR_NO_BROWSER_SERVERS_FOUND
#
# MessageText:
#
# The list of servers for this workgroup is not currently available
#
ERROR_NO_BROWSER_SERVERS_FOUND = 6118


#/////////////////////////////////////////////////
#                                               //
#            Task Scheduler Error codes         //
#            NET START must understand          //
#                                               //
#                 6200 to 6249                  //
#/////////////////////////////////////////////////

#
# MessageId: SCHED_E_SERVICE_NOT_LOCALSYSTEM
#
# MessageText:
#
# The Task Scheduler service must be configured to run in the System account to function properly. Individual tasks may be configured to run in other accounts.
#
SCHED_E_SERVICE_NOT_LOCALSYSTEM = 6200


#/////////////////////////////////////////////////
#                                               //
#                  Available                    //
#                                               //
#                 6250 to 6599                  //
#/////////////////////////////////////////////////

#/////////////////////////////////////////////////
#                                               //
#         Common Log (CLFS) Error codes         //
#                                               //
#                 6600 to 6699                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_LOG_SECTOR_INVALID
#
# MessageText:
#
# Log service encountered an invalid log sector.
#
ERROR_LOG_SECTOR_INVALID = 6600

#
# MessageId: ERROR_LOG_SECTOR_PARITY_INVALID
#
# MessageText:
#
# Log service encountered a log sector with invalid block parity.
#
ERROR_LOG_SECTOR_PARITY_INVALID = 6601

#
# MessageId: ERROR_LOG_SECTOR_REMAPPED
#
# MessageText:
#
# Log service encountered a remapped log sector.
#
ERROR_LOG_SECTOR_REMAPPED = 6602

#
# MessageId: ERROR_LOG_BLOCK_INCOMPLETE
#
# MessageText:
#
# Log service encountered a partial or incomplete log block.
#
ERROR_LOG_BLOCK_INCOMPLETE = 6603

#
# MessageId: ERROR_LOG_INVALID_RANGE
#
# MessageText:
#
# Log service encountered an attempt access data outside the active log range.
#
ERROR_LOG_INVALID_RANGE = 6604

#
# MessageId: ERROR_LOG_BLOCKS_EXHAUSTED
#
# MessageText:
#
# Log service user marshalling buffers are exhausted.
#
ERROR_LOG_BLOCKS_EXHAUSTED = 6605

#
# MessageId: ERROR_LOG_READ_CONTEXT_INVALID
#
# MessageText:
#
# Log service encountered an attempt read from a marshalling area with an invalid read context.
#
ERROR_LOG_READ_CONTEXT_INVALID = 6606

#
# MessageId: ERROR_LOG_RESTART_INVALID
#
# MessageText:
#
# Log service encountered an invalid log restart area.
#
ERROR_LOG_RESTART_INVALID = 6607

#
# MessageId: ERROR_LOG_BLOCK_VERSION
#
# MessageText:
#
# Log service encountered an invalid log block version.
#
ERROR_LOG_BLOCK_VERSION = 6608

#
# MessageId: ERROR_LOG_BLOCK_INVALID
#
# MessageText:
#
# Log service encountered an invalid log block.
#
ERROR_LOG_BLOCK_INVALID = 6609

#
# MessageId: ERROR_LOG_READ_MODE_INVALID
#
# MessageText:
#
# Log service encountered an attempt to read the log with an invalid read mode.
#
ERROR_LOG_READ_MODE_INVALID = 6610

#
# MessageId: ERROR_LOG_NO_RESTART
#
# MessageText:
#
# Log service encountered a log stream with no restart area.
#
ERROR_LOG_NO_RESTART = 6611

#
# MessageId: ERROR_LOG_METADATA_CORRUPT
#
# MessageText:
#
# Log service encountered a corrupted metadata file.
#
ERROR_LOG_METADATA_CORRUPT = 6612

#
# MessageId: ERROR_LOG_METADATA_INVALID
#
# MessageText:
#
# Log service encountered a metadata file that could not be created by the log file system.
#
ERROR_LOG_METADATA_INVALID = 6613

#
# MessageId: ERROR_LOG_METADATA_INCONSISTENT
#
# MessageText:
#
# Log service encountered a metadata file with inconsistent data.
#
ERROR_LOG_METADATA_INCONSISTENT = 6614

#
# MessageId: ERROR_LOG_RESERVATION_INVALID
#
# MessageText:
#
# Log service encountered an attempt to erroneous allocate or dispose reservation space.
#
ERROR_LOG_RESERVATION_INVALID = 6615

#
# MessageId: ERROR_LOG_CANT_DELETE
#
# MessageText:
#
# Log service cannot delete log file or file system container.
#
ERROR_LOG_CANT_DELETE = 6616

#
# MessageId: ERROR_LOG_CONTAINER_LIMIT_EXCEEDED
#
# MessageText:
#
# Log service has reached the maximum allowable containers allocated to a log file.
#
ERROR_LOG_CONTAINER_LIMIT_EXCEEDED = 6617

#
# MessageId: ERROR_LOG_START_OF_LOG
#
# MessageText:
#
# Log service has attempted to read or write backward past the start of the log.
#
ERROR_LOG_START_OF_LOG = 6618

#
# MessageId: ERROR_LOG_POLICY_ALREADY_INSTALLED
#
# MessageText:
#
# Log policy could not be installed because a policy of the same type is already present.
#
ERROR_LOG_POLICY_ALREADY_INSTALLED = 6619

#
# MessageId: ERROR_LOG_POLICY_NOT_INSTALLED
#
# MessageText:
#
# Log policy in question was not installed at the time of the request.
#
ERROR_LOG_POLICY_NOT_INSTALLED = 6620

#
# MessageId: ERROR_LOG_POLICY_INVALID
#
# MessageText:
#
# The installed set of policies on the log is invalid.
#
ERROR_LOG_POLICY_INVALID = 6621

#
# MessageId: ERROR_LOG_POLICY_CONFLICT
#
# MessageText:
#
# A policy on the log in question prevented the operation from completing.
#
ERROR_LOG_POLICY_CONFLICT = 6622

#
# MessageId: ERROR_LOG_PINNED_ARCHIVE_TAIL
#
# MessageText:
#
# Log space cannot be reclaimed because the log is pinned by the archive tail.
#
ERROR_LOG_PINNED_ARCHIVE_TAIL = 6623

#
# MessageId: ERROR_LOG_RECORD_NONEXISTENT
#
# MessageText:
#
# Log record is not a record in the log file.
#
ERROR_LOG_RECORD_NONEXISTENT = 6624

#
# MessageId: ERROR_LOG_RECORDS_RESERVED_INVALID
#
# MessageText:
#
# Number of reserved log records or the adjustment of the number of reserved log records is invalid.
#
ERROR_LOG_RECORDS_RESERVED_INVALID = 6625

#
# MessageId: ERROR_LOG_SPACE_RESERVED_INVALID
#
# MessageText:
#
# Reserved log space or the adjustment of the log space is invalid.
#
ERROR_LOG_SPACE_RESERVED_INVALID = 6626

#
# MessageId: ERROR_LOG_TAIL_INVALID
#
# MessageText:
#
# An new or existing archive tail or base of the active log is invalid.
#
ERROR_LOG_TAIL_INVALID = 6627

#
# MessageId: ERROR_LOG_FULL
#
# MessageText:
#
# Log space is exhausted.
#
ERROR_LOG_FULL = 6628

#
# MessageId: ERROR_COULD_NOT_RESIZE_LOG
#
# MessageText:
#
# The log could not be set to the requested size.
#
ERROR_COULD_NOT_RESIZE_LOG = 6629

#
# MessageId: ERROR_LOG_MULTIPLEXED
#
# MessageText:
#
# Log is multiplexed, no direct writes to the physical log is allowed.
#
ERROR_LOG_MULTIPLEXED = 6630

#
# MessageId: ERROR_LOG_DEDICATED
#
# MessageText:
#
# The operation failed because the log is a dedicated log.
#
ERROR_LOG_DEDICATED = 6631

#
# MessageId: ERROR_LOG_ARCHIVE_NOT_IN_PROGRESS
#
# MessageText:
#
# The operation requires an archive context.
#
ERROR_LOG_ARCHIVE_NOT_IN_PROGRESS = 6632

#
# MessageId: ERROR_LOG_ARCHIVE_IN_PROGRESS
#
# MessageText:
#
# Log archival is in progress.
#
ERROR_LOG_ARCHIVE_IN_PROGRESS = 6633

#
# MessageId: ERROR_LOG_EPHEMERAL
#
# MessageText:
#
# The operation requires a non-ephemeral log, but the log is ephemeral.
#
ERROR_LOG_EPHEMERAL = 6634

#
# MessageId: ERROR_LOG_NOT_ENOUGH_CONTAINERS
#
# MessageText:
#
# The log must have at least two containers before it can be read from or written to.
#
ERROR_LOG_NOT_ENOUGH_CONTAINERS = 6635

#
# MessageId: ERROR_LOG_CLIENT_ALREADY_REGISTERED
#
# MessageText:
#
# A log client has already registered on the stream.
#
ERROR_LOG_CLIENT_ALREADY_REGISTERED = 6636

#
# MessageId: ERROR_LOG_CLIENT_NOT_REGISTERED
#
# MessageText:
#
# A log client has not been registered on the stream.
#
ERROR_LOG_CLIENT_NOT_REGISTERED = 6637

#
# MessageId: ERROR_LOG_FULL_HANDLER_IN_PROGRESS
#
# MessageText:
#
# A request has already been made to handle the log full condition.
#
ERROR_LOG_FULL_HANDLER_IN_PROGRESS = 6638

#
# MessageId: ERROR_LOG_CONTAINER_READ_FAILED
#
# MessageText:
#
# Log service encountered an error when attempting to read from a log container.
#
ERROR_LOG_CONTAINER_READ_FAILED = 6639

#
# MessageId: ERROR_LOG_CONTAINER_WRITE_FAILED
#
# MessageText:
#
# Log service encountered an error when attempting to write to a log container.
#
ERROR_LOG_CONTAINER_WRITE_FAILED = 6640

#
# MessageId: ERROR_LOG_CONTAINER_OPEN_FAILED
#
# MessageText:
#
# Log service encountered an error when attempting open a log container.
#
ERROR_LOG_CONTAINER_OPEN_FAILED = 6641

#
# MessageId: ERROR_LOG_CONTAINER_STATE_INVALID
#
# MessageText:
#
# Log service encountered an invalid container state when attempting a requested action.
#
ERROR_LOG_CONTAINER_STATE_INVALID = 6642

#
# MessageId: ERROR_LOG_STATE_INVALID
#
# MessageText:
#
# Log service is not in the correct state to perform a requested action.
#
ERROR_LOG_STATE_INVALID = 6643

#
# MessageId: ERROR_LOG_PINNED
#
# MessageText:
#
# Log space cannot be reclaimed because the log is pinned.
#
ERROR_LOG_PINNED = 6644

#
# MessageId: ERROR_LOG_METADATA_FLUSH_FAILED
#
# MessageText:
#
# Log metadata flush failed.
#
ERROR_LOG_METADATA_FLUSH_FAILED = 6645

#
# MessageId: ERROR_LOG_INCONSISTENT_SECURITY
#
# MessageText:
#
# Security on the log and its containers is inconsistent.
#
ERROR_LOG_INCONSISTENT_SECURITY = 6646

#
# MessageId: ERROR_LOG_APPENDED_FLUSH_FAILED
#
# MessageText:
#
# Records were appended to the log or reservation changes were made, but the log could not be flushed.
#
ERROR_LOG_APPENDED_FLUSH_FAILED = 6647

#
# MessageId: ERROR_LOG_PINNED_RESERVATION
#
# MessageText:
#
# The log is pinned due to reservation consuming most of the log space. Free some reserved records to make space available.
#
ERROR_LOG_PINNED_RESERVATION = 6648


#/////////////////////////////////////////////////
#                                               //
#           Transaction (KTM) Error codes       //
#                                               //
#                 6700 to 6799                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_INVALID_TRANSACTION
#
# MessageText:
#
# The transaction handle associated with this operation is not valid.
#
ERROR_INVALID_TRANSACTION = 6700

#
# MessageId: ERROR_TRANSACTION_NOT_ACTIVE
#
# MessageText:
#
# The requested operation was made in the context of a transaction that is no longer active.
#
ERROR_TRANSACTION_NOT_ACTIVE = 6701

#
# MessageId: ERROR_TRANSACTION_REQUEST_NOT_VALID
#
# MessageText:
#
# The requested operation is not valid on the Transaction object in its current state.
#
ERROR_TRANSACTION_REQUEST_NOT_VALID = 6702

#
# MessageId: ERROR_TRANSACTION_NOT_REQUESTED
#
# MessageText:
#
# The caller has called a response API, but the response is not expected because the TM did not issue the corresponding request to the caller.
#
ERROR_TRANSACTION_NOT_REQUESTED = 6703

#
# MessageId: ERROR_TRANSACTION_ALREADY_ABORTED
#
# MessageText:
#
# It is too late to perform the requested operation, since the Transaction has already been aborted.
#
ERROR_TRANSACTION_ALREADY_ABORTED = 6704

#
# MessageId: ERROR_TRANSACTION_ALREADY_COMMITTED
#
# MessageText:
#
# It is too late to perform the requested operation, since the Transaction has already been committed.
#
ERROR_TRANSACTION_ALREADY_COMMITTED = 6705

#
# MessageId: ERROR_TM_INITIALIZATION_FAILED
#
# MessageText:
#
# The Transaction Manager was unable to be successfully initialized. Transacted operations are not supported.
#
ERROR_TM_INITIALIZATION_FAILED = 6706

#
# MessageId: ERROR_RESOURCEMANAGER_READ_ONLY
#
# MessageText:
#
# The specified ResourceManager made no changes or updates to the resource under this transaction.
#
ERROR_RESOURCEMANAGER_READ_ONLY = 6707

#
# MessageId: ERROR_TRANSACTION_NOT_JOINED
#
# MessageText:
#
# The resource manager has attempted to prepare a transaction that it has not successfully joined.
#
ERROR_TRANSACTION_NOT_JOINED = 6708

#
# MessageId: ERROR_TRANSACTION_SUPERIOR_EXISTS
#
# MessageText:
#
# The Transaction object already has a superior enlistment, and the caller attempted an operation that would have created a new superior. Only a single superior enlistment is allow.
#
ERROR_TRANSACTION_SUPERIOR_EXISTS = 6709

#
# MessageId: ERROR_CRM_PROTOCOL_ALREADY_EXISTS
#
# MessageText:
#
# The RM tried to register a protocol that already exists.
#
ERROR_CRM_PROTOCOL_ALREADY_EXISTS = 6710

#
# MessageId: ERROR_TRANSACTION_PROPAGATION_FAILED
#
# MessageText:
#
# The attempt to propagate the Transaction failed.
#
ERROR_TRANSACTION_PROPAGATION_FAILED = 6711

#
# MessageId: ERROR_CRM_PROTOCOL_NOT_FOUND
#
# MessageText:
#
# The requested propagation protocol was not registered as a CRM.
#
ERROR_CRM_PROTOCOL_NOT_FOUND = 6712

#
# MessageId: ERROR_TRANSACTION_INVALID_MARSHALL_BUFFER
#
# MessageText:
#
# The buffer passed in to PushTransaction or PullTransaction is not in a valid format.
#
ERROR_TRANSACTION_INVALID_MARSHALL_BUFFER = 6713

#
# MessageId: ERROR_CURRENT_TRANSACTION_NOT_VALID
#
# MessageText:
#
# The current transaction context associated with the thread is not a valid handle to a transaction object.
#
ERROR_CURRENT_TRANSACTION_NOT_VALID = 6714

#
# MessageId: ERROR_TRANSACTION_NOT_FOUND
#
# MessageText:
#
# The specified Transaction object could not be opened, because it was not found.
#
ERROR_TRANSACTION_NOT_FOUND = 6715

#
# MessageId: ERROR_RESOURCEMANAGER_NOT_FOUND
#
# MessageText:
#
# The specified ResourceManager object could not be opened, because it was not found.
#
ERROR_RESOURCEMANAGER_NOT_FOUND = 6716

#
# MessageId: ERROR_ENLISTMENT_NOT_FOUND
#
# MessageText:
#
# The specified Enlistment object could not be opened, because it was not found.
#
ERROR_ENLISTMENT_NOT_FOUND = 6717

#
# MessageId: ERROR_TRANSACTIONMANAGER_NOT_FOUND
#
# MessageText:
#
# The specified TransactionManager object could not be opened, because it was not found.
#
ERROR_TRANSACTIONMANAGER_NOT_FOUND = 6718

#
# MessageId: ERROR_TRANSACTIONMANAGER_NOT_ONLINE
#
# MessageText:
#
# The object specified could not be created or opened, because its associated TransactionManager is not online.  The TransactionManager must be brought fully Online by calling RecoverTransactionManager to recover to the end of its LogFile before objects in its Transaction or ResourceManager namespaces can be opened.  In addition, errors in writing records to its LogFile can cause a TransactionManager to go offline.
#
ERROR_TRANSACTIONMANAGER_NOT_ONLINE = 6719

#
# MessageId: ERROR_TRANSACTIONMANAGER_RECOVERY_NAME_COLLISION
#
# MessageText:
#
# The specified TransactionManager was unable to create the objects contained in its logfile in the Ob namespace. Therefore, the TransactionManager was unable to recover.
#
ERROR_TRANSACTIONMANAGER_RECOVERY_NAME_COLLISION = 6720

#
# MessageId: ERROR_TRANSACTION_NOT_ROOT
#
# MessageText:
#
# The call to create a superior Enlistment on this Transaction object could not be completed, because the Transaction object specified for the enlistment is a subordinate branch of the Transaction. Only the root of the Transaction can be enlisted on as a superior.
#
ERROR_TRANSACTION_NOT_ROOT = 6721

#
# MessageId: ERROR_TRANSACTION_OBJECT_EXPIRED
#
# MessageText:
#
# Because the associated transaction manager or resource manager has been closed, the handle is no longer valid.
#
ERROR_TRANSACTION_OBJECT_EXPIRED = 6722

#
# MessageId: ERROR_TRANSACTION_RESPONSE_NOT_ENLISTED
#
# MessageText:
#
# The specified operation could not be performed on this Superior enlistment, because the enlistment was not created with the corresponding completion response in the NotificationMask.
#
ERROR_TRANSACTION_RESPONSE_NOT_ENLISTED = 6723

#
# MessageId: ERROR_TRANSACTION_RECORD_TOO_LONG
#
# MessageText:
#
# The specified operation could not be performed, because the record that would be logged was too long. This can occur because of two conditions: either there are too many Enlistments on this Transaction, or the combined RecoveryInformation being logged on behalf of those Enlistments is too long.
#
ERROR_TRANSACTION_RECORD_TOO_LONG = 6724

#
# MessageId: ERROR_IMPLICIT_TRANSACTION_NOT_SUPPORTED
#
# MessageText:
#
# Implicit transaction are not supported.
#
ERROR_IMPLICIT_TRANSACTION_NOT_SUPPORTED = 6725

#
# MessageId: ERROR_TRANSACTION_INTEGRITY_VIOLATED
#
# MessageText:
#
# The kernel transaction manager had to abort or forget the transaction because it blocked forward progress.
#
ERROR_TRANSACTION_INTEGRITY_VIOLATED = 6726

#
# MessageId: ERROR_TRANSACTIONMANAGER_IDENTITY_MISMATCH
#
# MessageText:
#
# The TransactionManager identity that was supplied did not match the one recorded in the TransactionManager's log file.
#
ERROR_TRANSACTIONMANAGER_IDENTITY_MISMATCH = 6727

#
# MessageId: ERROR_RM_CANNOT_BE_FROZEN_FOR_SNAPSHOT
#
# MessageText:
#
# This snapshot operation cannot continue because a transactional resource manager cannot be frozen in its current state.  Please try again.
#
ERROR_RM_CANNOT_BE_FROZEN_FOR_SNAPSHOT = 6728

#
# MessageId: ERROR_TRANSACTION_MUST_WRITETHROUGH
#
# MessageText:
#
# The transaction cannot be enlisted on with the specified EnlistmentMask, because the transaction has already completed the PrePrepare phase.  In order to ensure correctness, the ResourceManager must switch to a write-through mode and cease caching data within this transaction.  Enlisting for only subsequent transaction phases may still succeed.
#
ERROR_TRANSACTION_MUST_WRITETHROUGH = 6729

#
# MessageId: ERROR_TRANSACTION_NO_SUPERIOR
#
# MessageText:
#
# The transaction does not have a superior enlistment.
#
ERROR_TRANSACTION_NO_SUPERIOR = 6730

#
# MessageId: ERROR_HEURISTIC_DAMAGE_POSSIBLE
#
# MessageText:
#
# The attempt to commit the Transaction completed, but it is possible that some portion of the transaction tree did not commit successfully due to heuristics.  Therefore it is possible that some data modified in the transaction may not have committed, resulting in transactional inconsistency.  If possible, check the consistency of the associated data.
#
ERROR_HEURISTIC_DAMAGE_POSSIBLE = 6731


#/////////////////////////////////////////////////
#                                               //
#        Transactional File Services (TxF)      //
#                  Error codes                  //
#                                               //
#                 6800 to 6899                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_TRANSACTIONAL_CONFLICT
#
# MessageText:
#
# The function attempted to use a name that is reserved for use by another transaction.
#
ERROR_TRANSACTIONAL_CONFLICT = 6800

#
# MessageId: ERROR_RM_NOT_ACTIVE
#
# MessageText:
#
# Transaction support within the specified resource manager is not started or was shut down due to an error.
#
ERROR_RM_NOT_ACTIVE = 6801

#
# MessageId: ERROR_RM_METADATA_CORRUPT
#
# MessageText:
#
# The metadata of the RM has been corrupted. The RM will not function.
#
ERROR_RM_METADATA_CORRUPT = 6802

#
# MessageId: ERROR_DIRECTORY_NOT_RM
#
# MessageText:
#
# The specified directory does not contain a resource manager.
#
ERROR_DIRECTORY_NOT_RM = 6803

#
# MessageId: ERROR_TRANSACTIONS_UNSUPPORTED_REMOTE
#
# MessageText:
#
# The remote server or share does not support transacted file operations.
#
ERROR_TRANSACTIONS_UNSUPPORTED_REMOTE = 6805

#
# MessageId: ERROR_LOG_RESIZE_INVALID_SIZE
#
# MessageText:
#
# The requested log size is invalid.
#
ERROR_LOG_RESIZE_INVALID_SIZE = 6806

#
# MessageId: ERROR_OBJECT_NO_LONGER_EXISTS
#
# MessageText:
#
# The object (file, stream, link) corresponding to the handle has been deleted by a Transaction Savepoint Rollback.
#
ERROR_OBJECT_NO_LONGER_EXISTS = 6807

#
# MessageId: ERROR_STREAM_MINIVERSION_NOT_FOUND
#
# MessageText:
#
# The specified file miniversion was not found for this transacted file open.
#
ERROR_STREAM_MINIVERSION_NOT_FOUND = 6808

#
# MessageId: ERROR_STREAM_MINIVERSION_NOT_VALID
#
# MessageText:
#
# The specified file miniversion was found but has been invalidated. Most likely cause is a transaction savepoint rollback.
#
ERROR_STREAM_MINIVERSION_NOT_VALID = 6809

#
# MessageId: ERROR_MINIVERSION_INACCESSIBLE_FROM_SPECIFIED_TRANSACTION
#
# MessageText:
#
# A miniversion may only be opened in the context of the transaction that created it.
#
ERROR_MINIVERSION_INACCESSIBLE_FROM_SPECIFIED_TRANSACTION = 6810

#
# MessageId: ERROR_CANT_OPEN_MINIVERSION_WITH_MODIFY_INTENT
#
# MessageText:
#
# It is not possible to open a miniversion with modify access.
#
ERROR_CANT_OPEN_MINIVERSION_WITH_MODIFY_INTENT = 6811

#
# MessageId: ERROR_CANT_CREATE_MORE_STREAM_MINIVERSIONS
#
# MessageText:
#
# It is not possible to create any more miniversions for this stream.
#
ERROR_CANT_CREATE_MORE_STREAM_MINIVERSIONS = 6812

#
# MessageId: ERROR_REMOTE_FILE_VERSION_MISMATCH
#
# MessageText:
#
# The remote server sent mismatching version number or Fid for a file opened with transactions.
#
ERROR_REMOTE_FILE_VERSION_MISMATCH = 6814

#
# MessageId: ERROR_HANDLE_NO_LONGER_VALID
#
# MessageText:
#
# The handle has been invalidated by a transaction. The most likely cause is the presence of memory mapping on a file or an open handle when the transaction ended or rolled back to savepoint.
#
ERROR_HANDLE_NO_LONGER_VALID = 6815

#
# MessageId: ERROR_NO_TXF_METADATA
#
# MessageText:
#
# There is no transaction metadata on the file.
#
ERROR_NO_TXF_METADATA = 6816

#
# MessageId: ERROR_LOG_CORRUPTION_DETECTED
#
# MessageText:
#
# The log data is corrupt.
#
ERROR_LOG_CORRUPTION_DETECTED = 6817

#
# MessageId: ERROR_CANT_RECOVER_WITH_HANDLE_OPEN
#
# MessageText:
#
# The file can't be recovered because there is a handle still open on it.
#
ERROR_CANT_RECOVER_WITH_HANDLE_OPEN = 6818

#
# MessageId: ERROR_RM_DISCONNECTED
#
# MessageText:
#
# The transaction outcome is unavailable because the resource manager responsible for it has disconnected.
#
ERROR_RM_DISCONNECTED = 6819

#
# MessageId: ERROR_ENLISTMENT_NOT_SUPERIOR
#
# MessageText:
#
# The request was rejected because the enlistment in question is not a superior enlistment.
#
ERROR_ENLISTMENT_NOT_SUPERIOR = 6820

#
# MessageId: ERROR_RECOVERY_NOT_NEEDED
#
# MessageText:
#
# The transactional resource manager is already consistent. Recovery is not needed.
#
ERROR_RECOVERY_NOT_NEEDED = 6821

#
# MessageId: ERROR_RM_ALREADY_STARTED
#
# MessageText:
#
# The transactional resource manager has already been started.
#
ERROR_RM_ALREADY_STARTED = 6822

#
# MessageId: ERROR_FILE_IDENTITY_NOT_PERSISTENT
#
# MessageText:
#
# The file cannot be opened transactionally, because its identity depends on the outcome of an unresolved transaction.
#
ERROR_FILE_IDENTITY_NOT_PERSISTENT = 6823

#
# MessageId: ERROR_CANT_BREAK_TRANSACTIONAL_DEPENDENCY
#
# MessageText:
#
# The operation cannot be performed because another transaction is depending on the fact that this property will not change.
#
ERROR_CANT_BREAK_TRANSACTIONAL_DEPENDENCY = 6824

#
# MessageId: ERROR_CANT_CROSS_RM_BOUNDARY
#
# MessageText:
#
# The operation would involve a single file with two transactional resource managers and is therefore not allowed.
#
ERROR_CANT_CROSS_RM_BOUNDARY = 6825

#
# MessageId: ERROR_TXF_DIR_NOT_EMPTY
#
# MessageText:
#
# The $Txf directory must be empty for this operation to succeed.
#
ERROR_TXF_DIR_NOT_EMPTY = 6826

#
# MessageId: ERROR_INDOUBT_TRANSACTIONS_EXIST
#
# MessageText:
#
# The operation would leave a transactional resource manager in an inconsistent state and is therefore not allowed.
#
ERROR_INDOUBT_TRANSACTIONS_EXIST = 6827

#
# MessageId: ERROR_TM_VOLATILE
#
# MessageText:
#
# The operation could not be completed because the transaction manager does not have a log.
#
ERROR_TM_VOLATILE = 6828

#
# MessageId: ERROR_ROLLBACK_TIMER_EXPIRED
#
# MessageText:
#
# A rollback could not be scheduled because a previously scheduled rollback has already executed or been queued for execution.
#
ERROR_ROLLBACK_TIMER_EXPIRED = 6829

#
# MessageId: ERROR_TXF_ATTRIBUTE_CORRUPT
#
# MessageText:
#
# The transactional metadata attribute on the file or directory is corrupt and unreadable.
#
ERROR_TXF_ATTRIBUTE_CORRUPT = 6830

#
# MessageId: ERROR_EFS_NOT_ALLOWED_IN_TRANSACTION
#
# MessageText:
#
# The encryption operation could not be completed because a transaction is active.
#
ERROR_EFS_NOT_ALLOWED_IN_TRANSACTION = 6831

#
# MessageId: ERROR_TRANSACTIONAL_OPEN_NOT_ALLOWED
#
# MessageText:
#
# This object is not allowed to be opened in a transaction.
#
ERROR_TRANSACTIONAL_OPEN_NOT_ALLOWED = 6832

#
# MessageId: ERROR_LOG_GROWTH_FAILED
#
# MessageText:
#
# An attempt to create space in the transactional resource manager's log failed. The failure status has been recorded in the event log.
#
ERROR_LOG_GROWTH_FAILED = 6833

#
# MessageId: ERROR_TRANSACTED_MAPPING_UNSUPPORTED_REMOTE
#
# MessageText:
#
# Memory mapping (creating a mapped section) a remote file under a transaction is not supported.
#
ERROR_TRANSACTED_MAPPING_UNSUPPORTED_REMOTE = 6834

#
# MessageId: ERROR_TXF_METADATA_ALREADY_PRESENT
#
# MessageText:
#
# Transaction metadata is already present on this file and cannot be superseded.
#
ERROR_TXF_METADATA_ALREADY_PRESENT = 6835

#
# MessageId: ERROR_TRANSACTION_SCOPE_CALLBACKS_NOT_SET
#
# MessageText:
#
# A transaction scope could not be entered because the scope handler has not been initialized.
#
ERROR_TRANSACTION_SCOPE_CALLBACKS_NOT_SET = 6836

#
# MessageId: ERROR_TRANSACTION_REQUIRED_PROMOTION
#
# MessageText:
#
# Promotion was required in order to allow the resource manager to enlist, but the transaction was set to disallow it.
#
ERROR_TRANSACTION_REQUIRED_PROMOTION = 6837

#
# MessageId: ERROR_CANNOT_EXECUTE_FILE_IN_TRANSACTION
#
# MessageText:
#
# This file is open for modification in an unresolved transaction and may be opened for execute only by a transacted reader.
#
ERROR_CANNOT_EXECUTE_FILE_IN_TRANSACTION = 6838

#
# MessageId: ERROR_TRANSACTIONS_NOT_FROZEN
#
# MessageText:
#
# The request to thaw frozen transactions was ignored because transactions had not previously been frozen.
#
ERROR_TRANSACTIONS_NOT_FROZEN = 6839

#
# MessageId: ERROR_TRANSACTION_FREEZE_IN_PROGRESS
#
# MessageText:
#
# Transactions cannot be frozen because a freeze is already in progress.
#
ERROR_TRANSACTION_FREEZE_IN_PROGRESS = 6840

#
# MessageId: ERROR_NOT_SNAPSHOT_VOLUME
#
# MessageText:
#
# The target volume is not a snapshot volume. This operation is only valid on a volume mounted as a snapshot.
#
ERROR_NOT_SNAPSHOT_VOLUME = 6841

#
# MessageId: ERROR_NO_SAVEPOINT_WITH_OPEN_FILES
#
# MessageText:
#
# The savepoint operation failed because files are open on the transaction. This is not permitted.
#
ERROR_NO_SAVEPOINT_WITH_OPEN_FILES = 6842

#
# MessageId: ERROR_DATA_LOST_REPAIR
#
# MessageText:
#
# Windows has discovered corruption in a file, and that file has since been repaired. Data loss may have occurred.
#
ERROR_DATA_LOST_REPAIR = 6843

#
# MessageId: ERROR_SPARSE_NOT_ALLOWED_IN_TRANSACTION
#
# MessageText:
#
# The sparse operation could not be completed because a transaction is active on the file.
#
ERROR_SPARSE_NOT_ALLOWED_IN_TRANSACTION = 6844

#
# MessageId: ERROR_TM_IDENTITY_MISMATCH
#
# MessageText:
#
# The call to create a TransactionManager object failed because the Tm Identity stored in the logfile does not match the Tm Identity that was passed in as an argument.
#
ERROR_TM_IDENTITY_MISMATCH = 6845

#
# MessageId: ERROR_FLOATED_SECTION
#
# MessageText:
#
# I/O was attempted on a section object that has been floated as a result of a transaction ending. There is no valid data.
#
ERROR_FLOATED_SECTION = 6846

#
# MessageId: ERROR_CANNOT_ACCEPT_TRANSACTED_WORK
#
# MessageText:
#
# The transactional resource manager cannot currently accept transacted work due to a transient condition such as low resources.
#
ERROR_CANNOT_ACCEPT_TRANSACTED_WORK = 6847

#
# MessageId: ERROR_CANNOT_ABORT_TRANSACTIONS
#
# MessageText:
#
# The transactional resource manager had too many tranactions outstanding that could not be aborted. The transactional resource manger has been shut down.
#
ERROR_CANNOT_ABORT_TRANSACTIONS = 6848

#
# MessageId: ERROR_BAD_CLUSTERS
#
# MessageText:
#
# The operation could not be completed due to bad clusters on disk.
#
ERROR_BAD_CLUSTERS = 6849

#
# MessageId: ERROR_COMPRESSION_NOT_ALLOWED_IN_TRANSACTION
#
# MessageText:
#
# The compression operation could not be completed because a transaction is active on the file.
#
ERROR_COMPRESSION_NOT_ALLOWED_IN_TRANSACTION = 6850

#
# MessageId: ERROR_VOLUME_DIRTY
#
# MessageText:
#
# The operation could not be completed because the volume is dirty. Please run chkdsk and try again.
#
ERROR_VOLUME_DIRTY = 6851

#
# MessageId: ERROR_NO_LINK_TRACKING_IN_TRANSACTION
#
# MessageText:
#
# The link tracking operation could not be completed because a transaction is active.
#
ERROR_NO_LINK_TRACKING_IN_TRANSACTION = 6852

#
# MessageId: ERROR_OPERATION_NOT_SUPPORTED_IN_TRANSACTION
#
# MessageText:
#
# This operation cannot be performed in a transaction.
#
ERROR_OPERATION_NOT_SUPPORTED_IN_TRANSACTION = 6853

#
# MessageId: ERROR_EXPIRED_HANDLE
#
# MessageText:
#
# The handle is no longer properly associated with its transaction.  It may have been opened in a transactional resource manager that was subsequently forced to restart.  Please close the handle and open a new one.
#
ERROR_EXPIRED_HANDLE = 6854

#
# MessageId: ERROR_TRANSACTION_NOT_ENLISTED
#
# MessageText:
#
# The specified operation could not be performed because the resource manager is not enlisted in the transaction.
#
ERROR_TRANSACTION_NOT_ENLISTED = 6855


#/////////////////////////////////////////////////
#                                               //
#                  Available                    //
#                                               //
#                 6900 to 6999                  //
#/////////////////////////////////////////////////

#/////////////////////////////////////////////////
#                                               //
#          Terminal Server Error codes          //
#                                               //
#                 7000 to 7099                  //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_CTX_WINSTATION_NAME_INVALID
#
# MessageText:
#
# The specified session name is invalid.
#
ERROR_CTX_WINSTATION_NAME_INVALID = 7001

#
# MessageId: ERROR_CTX_INVALID_PD
#
# MessageText:
#
# The specified protocol driver is invalid.
#
ERROR_CTX_INVALID_PD = 7002

#
# MessageId: ERROR_CTX_PD_NOT_FOUND
#
# MessageText:
#
# The specified protocol driver was not found in the system path.
#
ERROR_CTX_PD_NOT_FOUND = 7003

#
# MessageId: ERROR_CTX_WD_NOT_FOUND
#
# MessageText:
#
# The specified terminal connection driver was not found in the system path.
#
ERROR_CTX_WD_NOT_FOUND = 7004

#
# MessageId: ERROR_CTX_CANNOT_MAKE_EVENTLOG_ENTRY
#
# MessageText:
#
# A registry key for event logging could not be created for this session.
#
ERROR_CTX_CANNOT_MAKE_EVENTLOG_ENTRY = 7005

#
# MessageId: ERROR_CTX_SERVICE_NAME_COLLISION
#
# MessageText:
#
# A service with the same name already exists on the system.
#
ERROR_CTX_SERVICE_NAME_COLLISION = 7006

#
# MessageId: ERROR_CTX_CLOSE_PENDING
#
# MessageText:
#
# A close operation is pending on the session.
#
ERROR_CTX_CLOSE_PENDING = 7007

#
# MessageId: ERROR_CTX_NO_OUTBUF
#
# MessageText:
#
# There are no free output buffers available.
#
ERROR_CTX_NO_OUTBUF = 7008

#
# MessageId: ERROR_CTX_MODEM_INF_NOT_FOUND
#
# MessageText:
#
# The MODEM.INF file was not found.
#
ERROR_CTX_MODEM_INF_NOT_FOUND = 7009

#
# MessageId: ERROR_CTX_INVALID_MODEMNAME
#
# MessageText:
#
# The modem name was not found in MODEM.INF.
#
ERROR_CTX_INVALID_MODEMNAME = 7010

#
# MessageId: ERROR_CTX_MODEM_RESPONSE_ERROR
#
# MessageText:
#
# The modem did not accept the command sent to it. Verify that the configured modem name matches the attached modem.
#
ERROR_CTX_MODEM_RESPONSE_ERROR = 7011

#
# MessageId: ERROR_CTX_MODEM_RESPONSE_TIMEOUT
#
# MessageText:
#
# The modem did not respond to the command sent to it. Verify that the modem is properly cabled and powered on.
#
ERROR_CTX_MODEM_RESPONSE_TIMEOUT = 7012

#
# MessageId: ERROR_CTX_MODEM_RESPONSE_NO_CARRIER
#
# MessageText:
#
# Carrier detect has failed or carrier has been dropped due to disconnect.
#
ERROR_CTX_MODEM_RESPONSE_NO_CARRIER = 7013

#
# MessageId: ERROR_CTX_MODEM_RESPONSE_NO_DIALTONE
#
# MessageText:
#
# Dial tone not detected within the required time. Verify that the phone cable is properly attached and functional.
#
ERROR_CTX_MODEM_RESPONSE_NO_DIALTONE = 7014

#
# MessageId: ERROR_CTX_MODEM_RESPONSE_BUSY
#
# MessageText:
#
# Busy signal detected at remote site on callback.
#
ERROR_CTX_MODEM_RESPONSE_BUSY = 7015

#
# MessageId: ERROR_CTX_MODEM_RESPONSE_VOICE
#
# MessageText:
#
# Voice detected at remote site on callback.
#
ERROR_CTX_MODEM_RESPONSE_VOICE = 7016

#
# MessageId: ERROR_CTX_TD_ERROR
#
# MessageText:
#
# Transport driver error
#
ERROR_CTX_TD_ERROR = 7017

#
# MessageId: ERROR_CTX_WINSTATION_NOT_FOUND
#
# MessageText:
#
# The specified session cannot be found.
#
ERROR_CTX_WINSTATION_NOT_FOUND = 7022

#
# MessageId: ERROR_CTX_WINSTATION_ALREADY_EXISTS
#
# MessageText:
#
# The specified session name is already in use.
#
ERROR_CTX_WINSTATION_ALREADY_EXISTS = 7023

#
# MessageId: ERROR_CTX_WINSTATION_BUSY
#
# MessageText:
#
# The task you are trying to do can't be completed because Remote Desktop Services is currently busy. Please try again in a few minutes. Other users should still be able to log on.
#
ERROR_CTX_WINSTATION_BUSY = 7024

#
# MessageId: ERROR_CTX_BAD_VIDEO_MODE
#
# MessageText:
#
# An attempt has been made to connect to a session whose video mode is not supported by the current client.
#
ERROR_CTX_BAD_VIDEO_MODE = 7025

#
# MessageId: ERROR_CTX_GRAPHICS_INVALID
#
# MessageText:
#
# The application attempted to enable DOS graphics mode. DOS graphics mode is not supported.
#
ERROR_CTX_GRAPHICS_INVALID = 7035

#
# MessageId: ERROR_CTX_LOGON_DISABLED
#
# MessageText:
#
# Your interactive logon privilege has been disabled. Please contact your administrator.
#
ERROR_CTX_LOGON_DISABLED = 7037

#
# MessageId: ERROR_CTX_NOT_CONSOLE
#
# MessageText:
#
# The requested operation can be performed only on the system console. This is most often the result of a driver or system DLL requiring direct console access.
#
ERROR_CTX_NOT_CONSOLE = 7038

#
# MessageId: ERROR_CTX_CLIENT_QUERY_TIMEOUT
#
# MessageText:
#
# The client failed to respond to the server connect message.
#
ERROR_CTX_CLIENT_QUERY_TIMEOUT = 7040

#
# MessageId: ERROR_CTX_CONSOLE_DISCONNECT
#
# MessageText:
#
# Disconnecting the console session is not supported.
#
ERROR_CTX_CONSOLE_DISCONNECT = 7041

#
# MessageId: ERROR_CTX_CONSOLE_CONNECT
#
# MessageText:
#
# Reconnecting a disconnected session to the console is not supported.
#
ERROR_CTX_CONSOLE_CONNECT = 7042

#
# MessageId: ERROR_CTX_SHADOW_DENIED
#
# MessageText:
#
# The request to control another session remotely was denied.
#
ERROR_CTX_SHADOW_DENIED = 7044

#
# MessageId: ERROR_CTX_WINSTATION_ACCESS_DENIED
#
# MessageText:
#
# The requested session access is denied.
#
ERROR_CTX_WINSTATION_ACCESS_DENIED = 7045

#
# MessageId: ERROR_CTX_INVALID_WD
#
# MessageText:
#
# The specified terminal connection driver is invalid.
#
ERROR_CTX_INVALID_WD = 7049

#
# MessageId: ERROR_CTX_SHADOW_INVALID
#
# MessageText:
#
# The requested session cannot be controlled remotely.
# This may be because the session is disconnected or does not currently have a user logged on.
#
ERROR_CTX_SHADOW_INVALID = 7050

#
# MessageId: ERROR_CTX_SHADOW_DISABLED
#
# MessageText:
#
# The requested session is not configured to allow remote control.
#
ERROR_CTX_SHADOW_DISABLED = 7051

#
# MessageId: ERROR_CTX_CLIENT_LICENSE_IN_USE
#
# MessageText:
#
# Your request to connect to this Terminal Server has been rejected. Your Terminal Server client license number is currently being used by another user. Please call your system administrator to obtain a unique license number.
#
ERROR_CTX_CLIENT_LICENSE_IN_USE = 7052

#
# MessageId: ERROR_CTX_CLIENT_LICENSE_NOT_SET
#
# MessageText:
#
# Your request to connect to this Terminal Server has been rejected. Your Terminal Server client license number has not been entered for this copy of the Terminal Server client. Please contact your system administrator.
#
ERROR_CTX_CLIENT_LICENSE_NOT_SET = 7053

#
# MessageId: ERROR_CTX_LICENSE_NOT_AVAILABLE
#
# MessageText:
#
# The number of connections to this computer is limited and all connections are in use right now. Try connecting later or contact your system administrator.
#
ERROR_CTX_LICENSE_NOT_AVAILABLE = 7054

#
# MessageId: ERROR_CTX_LICENSE_CLIENT_INVALID
#
# MessageText:
#
# The client you are using is not licensed to use this system. Your logon request is denied.
#
ERROR_CTX_LICENSE_CLIENT_INVALID = 7055

#
# MessageId: ERROR_CTX_LICENSE_EXPIRED
#
# MessageText:
#
# The system license has expired. Your logon request is denied.
#
ERROR_CTX_LICENSE_EXPIRED = 7056

#
# MessageId: ERROR_CTX_SHADOW_NOT_RUNNING
#
# MessageText:
#
# Remote control could not be terminated because the specified session is not currently being remotely controlled.
#
ERROR_CTX_SHADOW_NOT_RUNNING = 7057

#
# MessageId: ERROR_CTX_SHADOW_ENDED_BY_MODE_CHANGE
#
# MessageText:
#
# The remote control of the console was terminated because the display mode was changed. Changing the display mode in a remote control session is not supported.
#
ERROR_CTX_SHADOW_ENDED_BY_MODE_CHANGE = 7058

#
# MessageId: ERROR_ACTIVATION_COUNT_EXCEEDED
#
# MessageText:
#
# Activation has already been reset the maximum number of times for this installation. Your activation timer will not be cleared.
#
ERROR_ACTIVATION_COUNT_EXCEEDED = 7059

#
# MessageId: ERROR_CTX_WINSTATIONS_DISABLED
#
# MessageText:
#
# Remote logins are currently disabled.
#
ERROR_CTX_WINSTATIONS_DISABLED = 7060

#
# MessageId: ERROR_CTX_ENCRYPTION_LEVEL_REQUIRED
#
# MessageText:
#
# You do not have the proper encryption level to access this Session.
#
ERROR_CTX_ENCRYPTION_LEVEL_REQUIRED = 7061

#
# MessageId: ERROR_CTX_SESSION_IN_USE
#
# MessageText:
#
# The user %s\\%s is currently logged on to this computer. Only the current user or an administrator can log on to this computer.
#
ERROR_CTX_SESSION_IN_USE = 7062

#
# MessageId: ERROR_CTX_NO_FORCE_LOGOFF
#
# MessageText:
#
# The user %s\\%s is already logged on to the console of this computer. You do not have permission to log in at this time. To resolve this issue, contact %s\\%s and have them log off.
#
ERROR_CTX_NO_FORCE_LOGOFF = 7063

#
# MessageId: ERROR_CTX_ACCOUNT_RESTRICTION
#
# MessageText:
#
# Unable to log you on because of an account restriction.
#
ERROR_CTX_ACCOUNT_RESTRICTION = 7064

#
# MessageId: ERROR_RDP_PROTOCOL_ERROR
#
# MessageText:
#
# The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.
#
ERROR_RDP_PROTOCOL_ERROR = 7065

#
# MessageId: ERROR_CTX_CDM_CONNECT
#
# MessageText:
#
# The Client Drive Mapping Service Has Connected on Terminal Connection.
#
ERROR_CTX_CDM_CONNECT = 7066

#
# MessageId: ERROR_CTX_CDM_DISCONNECT
#
# MessageText:
#
# The Client Drive Mapping Service Has Disconnected on Terminal Connection.
#
ERROR_CTX_CDM_DISCONNECT = 7067

#
# MessageId: ERROR_CTX_SECURITY_LAYER_ERROR
#
# MessageText:
#
# The Terminal Server security layer detected an error in the protocol stream and has disconnected the client.
#
ERROR_CTX_SECURITY_LAYER_ERROR = 7068

#
# MessageId: ERROR_TS_INCOMPATIBLE_SESSIONS
#
# MessageText:
#
# The target session is incompatible with the current session.
#
ERROR_TS_INCOMPATIBLE_SESSIONS = 7069

#
# MessageId: ERROR_TS_VIDEO_SUBSYSTEM_ERROR
#
# MessageText:
#
# Windows can't connect to your session because a problem occurred in the Windows video subsystem. Try connecting again later, or contact the server administrator for assistance.
#
ERROR_TS_VIDEO_SUBSYSTEM_ERROR = 7070

#/////////////////////////////////////////////////
#                                               //
#          Windows Fabric Error Codes           //
#                                               //
#                 7100 to 7499                  //
#                                               //
#          defined in FabricCommon.idl          //
#                                               //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                                /
#           Traffic Control Error Codes          /
#                                                /
#                  7500 to 7999                  /
#                                                /
#            defined in: tcerror.h               /
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#           Active Directory Error codes        //
#                                               //
#                 8000 to 8999                  //
#/////////////////////////////////////////////////

# *****************
# FACILITY_FILE_REPLICATION_SERVICE
# *****************
#
# MessageId: FRS_ERR_INVALID_API_SEQUENCE
#
# MessageText:
#
# The file replication service API was called incorrectly.
#
FRS_ERR_INVALID_API_SEQUENCE = 8001

#
# MessageId: FRS_ERR_STARTING_SERVICE
#
# MessageText:
#
# The file replication service cannot be started.
#
FRS_ERR_STARTING_SERVICE = 8002

#
# MessageId: FRS_ERR_STOPPING_SERVICE
#
# MessageText:
#
# The file replication service cannot be stopped.
#
FRS_ERR_STOPPING_SERVICE = 8003

#
# MessageId: FRS_ERR_INTERNAL_API
#
# MessageText:
#
# The file replication service API terminated the request. The event log may have more information.
#
FRS_ERR_INTERNAL_API = 8004

#
# MessageId: FRS_ERR_INTERNAL
#
# MessageText:
#
# The file replication service terminated the request. The event log may have more information.
#
FRS_ERR_INTERNAL = 8005

#
# MessageId: FRS_ERR_SERVICE_COMM
#
# MessageText:
#
# The file replication service cannot be contacted. The event log may have more information.
#
FRS_ERR_SERVICE_COMM = 8006

#
# MessageId: FRS_ERR_INSUFFICIENT_PRIV
#
# MessageText:
#
# The file replication service cannot satisfy the request because the user has insufficient privileges. The event log may have more information.
#
FRS_ERR_INSUFFICIENT_PRIV = 8007

#
# MessageId: FRS_ERR_AUTHENTICATION
#
# MessageText:
#
# The file replication service cannot satisfy the request because authenticated RPC is not available. The event log may have more information.
#
FRS_ERR_AUTHENTICATION = 8008

#
# MessageId: FRS_ERR_PARENT_INSUFFICIENT_PRIV
#
# MessageText:
#
# The file replication service cannot satisfy the request because the user has insufficient privileges on the domain controller. The event log may have more information.
#
FRS_ERR_PARENT_INSUFFICIENT_PRIV = 8009

#
# MessageId: FRS_ERR_PARENT_AUTHENTICATION
#
# MessageText:
#
# The file replication service cannot satisfy the request because authenticated RPC is not available on the domain controller. The event log may have more information.
#
FRS_ERR_PARENT_AUTHENTICATION = 8010

#
# MessageId: FRS_ERR_CHILD_TO_PARENT_COMM
#
# MessageText:
#
# The file replication service cannot communicate with the file replication service on the domain controller. The event log may have more information.
#
FRS_ERR_CHILD_TO_PARENT_COMM = 8011

#
# MessageId: FRS_ERR_PARENT_TO_CHILD_COMM
#
# MessageText:
#
# The file replication service on the domain controller cannot communicate with the file replication service on this computer. The event log may have more information.
#
FRS_ERR_PARENT_TO_CHILD_COMM = 8012

#
# MessageId: FRS_ERR_SYSVOL_POPULATE
#
# MessageText:
#
# The file replication service cannot populate the system volume because of an internal error. The event log may have more information.
#
FRS_ERR_SYSVOL_POPULATE = 8013

#
# MessageId: FRS_ERR_SYSVOL_POPULATE_TIMEOUT
#
# MessageText:
#
# The file replication service cannot populate the system volume because of an internal timeout. The event log may have more information.
#
FRS_ERR_SYSVOL_POPULATE_TIMEOUT = 8014

#
# MessageId: FRS_ERR_SYSVOL_IS_BUSY
#
# MessageText:
#
# The file replication service cannot process the request. The system volume is busy with a previous request.
#
FRS_ERR_SYSVOL_IS_BUSY = 8015

#
# MessageId: FRS_ERR_SYSVOL_DEMOTE
#
# MessageText:
#
# The file replication service cannot stop replicating the system volume because of an internal error. The event log may have more information.
#
FRS_ERR_SYSVOL_DEMOTE = 8016

#
# MessageId: FRS_ERR_INVALID_SERVICE_PARAMETER
#
# MessageText:
#
# The file replication service detected an invalid parameter.
#
FRS_ERR_INVALID_SERVICE_PARAMETER = 8017

# *****************
# FACILITY DIRECTORY SERVICE
# *****************
DS_S_SUCCESS = NO_ERROR
#
# MessageId: ERROR_DS_NOT_INSTALLED
#
# MessageText:
#
# An error occurred while installing the directory service. For more information, see the event log.
#
ERROR_DS_NOT_INSTALLED = 8200

#
# MessageId: ERROR_DS_MEMBERSHIP_EVALUATED_LOCALLY
#
# MessageText:
#
# The directory service evaluated group memberships locally.
#
ERROR_DS_MEMBERSHIP_EVALUATED_LOCALLY = 8201

#
# MessageId: ERROR_DS_NO_ATTRIBUTE_OR_VALUE
#
# MessageText:
#
# The specified directory service attribute or value does not exist.
#
ERROR_DS_NO_ATTRIBUTE_OR_VALUE = 8202

#
# MessageId: ERROR_DS_INVALID_ATTRIBUTE_SYNTAX
#
# MessageText:
#
# The attribute syntax specified to the directory service is invalid.
#
ERROR_DS_INVALID_ATTRIBUTE_SYNTAX = 8203

#
# MessageId: ERROR_DS_ATTRIBUTE_TYPE_UNDEFINED
#
# MessageText:
#
# The attribute type specified to the directory service is not defined.
#
ERROR_DS_ATTRIBUTE_TYPE_UNDEFINED = 8204

#
# MessageId: ERROR_DS_ATTRIBUTE_OR_VALUE_EXISTS
#
# MessageText:
#
# The specified directory service attribute or value already exists.
#
ERROR_DS_ATTRIBUTE_OR_VALUE_EXISTS = 8205

#
# MessageId: ERROR_DS_BUSY
#
# MessageText:
#
# The directory service is busy.
#
ERROR_DS_BUSY = 8206

#
# MessageId: ERROR_DS_UNAVAILABLE
#
# MessageText:
#
# The directory service is unavailable.
#
ERROR_DS_UNAVAILABLE = 8207

#
# MessageId: ERROR_DS_NO_RIDS_ALLOCATED
#
# MessageText:
#
# The directory service was unable to allocate a relative identifier.
#
ERROR_DS_NO_RIDS_ALLOCATED = 8208

#
# MessageId: ERROR_DS_NO_MORE_RIDS
#
# MessageText:
#
# The directory service has exhausted the pool of relative identifiers.
#
ERROR_DS_NO_MORE_RIDS = 8209

#
# MessageId: ERROR_DS_INCORRECT_ROLE_OWNER
#
# MessageText:
#
# The requested operation could not be performed because the directory service is not the master for that type of operation.
#
ERROR_DS_INCORRECT_ROLE_OWNER = 8210

#
# MessageId: ERROR_DS_RIDMGR_INIT_ERROR
#
# MessageText:
#
# The directory service was unable to initialize the subsystem that allocates relative identifiers.
#
ERROR_DS_RIDMGR_INIT_ERROR = 8211

#
# MessageId: ERROR_DS_OBJ_CLASS_VIOLATION
#
# MessageText:
#
# The requested operation did not satisfy one or more constraints associated with the class of the object.
#
ERROR_DS_OBJ_CLASS_VIOLATION = 8212

#
# MessageId: ERROR_DS_CANT_ON_NON_LEAF
#
# MessageText:
#
# The directory service can perform the requested operation only on a leaf object.
#
ERROR_DS_CANT_ON_NON_LEAF = 8213

#
# MessageId: ERROR_DS_CANT_ON_RDN
#
# MessageText:
#
# The directory service cannot perform the requested operation on the RDN attribute of an object.
#
ERROR_DS_CANT_ON_RDN = 8214

#
# MessageId: ERROR_DS_CANT_MOD_OBJ_CLASS
#
# MessageText:
#
# The directory service detected an attempt to modify the object class of an object.
#
ERROR_DS_CANT_MOD_OBJ_CLASS = 8215

#
# MessageId: ERROR_DS_CROSS_DOM_MOVE_ERROR
#
# MessageText:
#
# The requested cross-domain move operation could not be performed.
#
ERROR_DS_CROSS_DOM_MOVE_ERROR = 8216

#
# MessageId: ERROR_DS_GC_NOT_AVAILABLE
#
# MessageText:
#
# Unable to contact the global catalog server.
#
ERROR_DS_GC_NOT_AVAILABLE = 8217

#
# MessageId: ERROR_SHARED_POLICY
#
# MessageText:
#
# The policy object is shared and can only be modified at the root.
#
ERROR_SHARED_POLICY = 8218

#
# MessageId: ERROR_POLICY_OBJECT_NOT_FOUND
#
# MessageText:
#
# The policy object does not exist.
#
ERROR_POLICY_OBJECT_NOT_FOUND = 8219

#
# MessageId: ERROR_POLICY_ONLY_IN_DS
#
# MessageText:
#
# The requested policy information is only in the directory service.
#
ERROR_POLICY_ONLY_IN_DS = 8220

#
# MessageId: ERROR_PROMOTION_ACTIVE
#
# MessageText:
#
# A domain controller promotion is currently active.
#
ERROR_PROMOTION_ACTIVE = 8221

#
# MessageId: ERROR_NO_PROMOTION_ACTIVE
#
# MessageText:
#
# A domain controller promotion is not currently active
#
ERROR_NO_PROMOTION_ACTIVE = 8222

# 8223 unused
#
# MessageId: ERROR_DS_OPERATIONS_ERROR
#
# MessageText:
#
# An operations error occurred.
#
ERROR_DS_OPERATIONS_ERROR = 8224

#
# MessageId: ERROR_DS_PROTOCOL_ERROR
#
# MessageText:
#
# A protocol error occurred.
#
ERROR_DS_PROTOCOL_ERROR = 8225

#
# MessageId: ERROR_DS_TIMELIMIT_EXCEEDED
#
# MessageText:
#
# The time limit for this request was exceeded.
#
ERROR_DS_TIMELIMIT_EXCEEDED = 8226

#
# MessageId: ERROR_DS_SIZELIMIT_EXCEEDED
#
# MessageText:
#
# The size limit for this request was exceeded.
#
ERROR_DS_SIZELIMIT_EXCEEDED = 8227

#
# MessageId: ERROR_DS_ADMIN_LIMIT_EXCEEDED
#
# MessageText:
#
# The administrative limit for this request was exceeded.
#
ERROR_DS_ADMIN_LIMIT_EXCEEDED = 8228

#
# MessageId: ERROR_DS_COMPARE_FALSE
#
# MessageText:
#
# The compare response was false.
#
ERROR_DS_COMPARE_FALSE = 8229

#
# MessageId: ERROR_DS_COMPARE_TRUE
#
# MessageText:
#
# The compare response was true.
#
ERROR_DS_COMPARE_TRUE = 8230

#
# MessageId: ERROR_DS_AUTH_METHOD_NOT_SUPPORTED
#
# MessageText:
#
# The requested authentication method is not supported by the server.
#
ERROR_DS_AUTH_METHOD_NOT_SUPPORTED = 8231

#
# MessageId: ERROR_DS_STRONG_AUTH_REQUIRED
#
# MessageText:
#
# A more secure authentication method is required for this server.
#
ERROR_DS_STRONG_AUTH_REQUIRED = 8232

#
# MessageId: ERROR_DS_INAPPROPRIATE_AUTH
#
# MessageText:
#
# Inappropriate authentication.
#
ERROR_DS_INAPPROPRIATE_AUTH = 8233

#
# MessageId: ERROR_DS_AUTH_UNKNOWN
#
# MessageText:
#
# The authentication mechanism is unknown.
#
ERROR_DS_AUTH_UNKNOWN = 8234

#
# MessageId: ERROR_DS_REFERRAL
#
# MessageText:
#
# A referral was returned from the server.
#
ERROR_DS_REFERRAL = 8235

#
# MessageId: ERROR_DS_UNAVAILABLE_CRIT_EXTENSION
#
# MessageText:
#
# The server does not support the requested critical extension.
#
ERROR_DS_UNAVAILABLE_CRIT_EXTENSION = 8236

#
# MessageId: ERROR_DS_CONFIDENTIALITY_REQUIRED
#
# MessageText:
#
# This request requires a secure connection.
#
ERROR_DS_CONFIDENTIALITY_REQUIRED = 8237

#
# MessageId: ERROR_DS_INAPPROPRIATE_MATCHING
#
# MessageText:
#
# Inappropriate matching.
#
ERROR_DS_INAPPROPRIATE_MATCHING = 8238

#
# MessageId: ERROR_DS_CONSTRAINT_VIOLATION
#
# MessageText:
#
# A constraint violation occurred.
#
ERROR_DS_CONSTRAINT_VIOLATION = 8239

#
# MessageId: ERROR_DS_NO_SUCH_OBJECT
#
# MessageText:
#
# There is no such object on the server.
#
ERROR_DS_NO_SUCH_OBJECT = 8240

#
# MessageId: ERROR_DS_ALIAS_PROBLEM
#
# MessageText:
#
# There is an alias problem.
#
ERROR_DS_ALIAS_PROBLEM = 8241

#
# MessageId: ERROR_DS_INVALID_DN_SYNTAX
#
# MessageText:
#
# An invalid dn syntax has been specified.
#
ERROR_DS_INVALID_DN_SYNTAX = 8242

#
# MessageId: ERROR_DS_IS_LEAF
#
# MessageText:
#
# The object is a leaf object.
#
ERROR_DS_IS_LEAF = 8243

#
# MessageId: ERROR_DS_ALIAS_DEREF_PROBLEM
#
# MessageText:
#
# There is an alias dereferencing problem.
#
ERROR_DS_ALIAS_DEREF_PROBLEM = 8244

#
# MessageId: ERROR_DS_UNWILLING_TO_PERFORM
#
# MessageText:
#
# The server is unwilling to process the request.
#
ERROR_DS_UNWILLING_TO_PERFORM = 8245

#
# MessageId: ERROR_DS_LOOP_DETECT
#
# MessageText:
#
# A loop has been detected.
#
ERROR_DS_LOOP_DETECT = 8246

#
# MessageId: ERROR_DS_NAMING_VIOLATION
#
# MessageText:
#
# There is a naming violation.
#
ERROR_DS_NAMING_VIOLATION = 8247

#
# MessageId: ERROR_DS_OBJECT_RESULTS_TOO_LARGE
#
# MessageText:
#
# The result set is too large.
#
ERROR_DS_OBJECT_RESULTS_TOO_LARGE = 8248

#
# MessageId: ERROR_DS_AFFECTS_MULTIPLE_DSAS
#
# MessageText:
#
# The operation affects multiple DSAs
#
ERROR_DS_AFFECTS_MULTIPLE_DSAS = 8249

#
# MessageId: ERROR_DS_SERVER_DOWN
#
# MessageText:
#
# The server is not operational.
#
ERROR_DS_SERVER_DOWN = 8250

#
# MessageId: ERROR_DS_LOCAL_ERROR
#
# MessageText:
#
# A local error has occurred.
#
ERROR_DS_LOCAL_ERROR = 8251

#
# MessageId: ERROR_DS_ENCODING_ERROR
#
# MessageText:
#
# An encoding error has occurred.
#
ERROR_DS_ENCODING_ERROR = 8252

#
# MessageId: ERROR_DS_DECODING_ERROR
#
# MessageText:
#
# A decoding error has occurred.
#
ERROR_DS_DECODING_ERROR = 8253

#
# MessageId: ERROR_DS_FILTER_UNKNOWN
#
# MessageText:
#
# The search filter cannot be recognized.
#
ERROR_DS_FILTER_UNKNOWN = 8254

#
# MessageId: ERROR_DS_PARAM_ERROR
#
# MessageText:
#
# One or more parameters are illegal.
#
ERROR_DS_PARAM_ERROR = 8255

#
# MessageId: ERROR_DS_NOT_SUPPORTED
#
# MessageText:
#
# The specified method is not supported.
#
ERROR_DS_NOT_SUPPORTED = 8256

#
# MessageId: ERROR_DS_NO_RESULTS_RETURNED
#
# MessageText:
#
# No results were returned.
#
ERROR_DS_NO_RESULTS_RETURNED = 8257

#
# MessageId: ERROR_DS_CONTROL_NOT_FOUND
#
# MessageText:
#
# The specified control is not supported by the server.
#
ERROR_DS_CONTROL_NOT_FOUND = 8258

#
# MessageId: ERROR_DS_CLIENT_LOOP
#
# MessageText:
#
# A referral loop was detected by the client.
#
ERROR_DS_CLIENT_LOOP = 8259

#
# MessageId: ERROR_DS_REFERRAL_LIMIT_EXCEEDED
#
# MessageText:
#
# The preset referral limit was exceeded.
#
ERROR_DS_REFERRAL_LIMIT_EXCEEDED = 8260

#
# MessageId: ERROR_DS_SORT_CONTROL_MISSING
#
# MessageText:
#
# The search requires a SORT control.
#
ERROR_DS_SORT_CONTROL_MISSING = 8261

#
# MessageId: ERROR_DS_OFFSET_RANGE_ERROR
#
# MessageText:
#
# The search results exceed the offset range specified.
#
ERROR_DS_OFFSET_RANGE_ERROR = 8262

#
# MessageId: ERROR_DS_RIDMGR_DISABLED
#
# MessageText:
#
# The directory service detected the subsystem that allocates relative identifiers is disabled. This can occur as a protective mechanism when the system determines a significant portion of relative identifiers (RIDs) have been exhausted. Please see http://go.microsoft.com/fwlink/?LinkId=228610 for recommended diagnostic steps and the procedure to re-enable account creation.
#
ERROR_DS_RIDMGR_DISABLED = 8263

#
# MessageId: ERROR_DS_ROOT_MUST_BE_NC
#
# MessageText:
#
# The root object must be the head of a naming context. The root object cannot have an instantiated parent.
#
ERROR_DS_ROOT_MUST_BE_NC = 8301

#
# MessageId: ERROR_DS_ADD_REPLICA_INHIBITED
#
# MessageText:
#
# The add replica operation cannot be performed. The naming context must be writeable in order to create the replica.
#
ERROR_DS_ADD_REPLICA_INHIBITED = 8302

#
# MessageId: ERROR_DS_ATT_NOT_DEF_IN_SCHEMA
#
# MessageText:
#
# A reference to an attribute that is not defined in the schema occurred.
#
ERROR_DS_ATT_NOT_DEF_IN_SCHEMA = 8303

#
# MessageId: ERROR_DS_MAX_OBJ_SIZE_EXCEEDED
#
# MessageText:
#
# The maximum size of an object has been exceeded.
#
ERROR_DS_MAX_OBJ_SIZE_EXCEEDED = 8304

#
# MessageId: ERROR_DS_OBJ_STRING_NAME_EXISTS
#
# MessageText:
#
# An attempt was made to add an object to the directory with a name that is already in use.
#
ERROR_DS_OBJ_STRING_NAME_EXISTS = 8305

#
# MessageId: ERROR_DS_NO_RDN_DEFINED_IN_SCHEMA
#
# MessageText:
#
# An attempt was made to add an object of a class that does not have an RDN defined in the schema.
#
ERROR_DS_NO_RDN_DEFINED_IN_SCHEMA = 8306

#
# MessageId: ERROR_DS_RDN_DOESNT_MATCH_SCHEMA
#
# MessageText:
#
# An attempt was made to add an object using an RDN that is not the RDN defined in the schema.
#
ERROR_DS_RDN_DOESNT_MATCH_SCHEMA = 8307

#
# MessageId: ERROR_DS_NO_REQUESTED_ATTS_FOUND
#
# MessageText:
#
# None of the requested attributes were found on the objects.
#
ERROR_DS_NO_REQUESTED_ATTS_FOUND = 8308

#
# MessageId: ERROR_DS_USER_BUFFER_TO_SMALL
#
# MessageText:
#
# The user buffer is too small.
#
ERROR_DS_USER_BUFFER_TO_SMALL = 8309

#
# MessageId: ERROR_DS_ATT_IS_NOT_ON_OBJ
#
# MessageText:
#
# The attribute specified in the operation is not present on the object.
#
ERROR_DS_ATT_IS_NOT_ON_OBJ = 8310

#
# MessageId: ERROR_DS_ILLEGAL_MOD_OPERATION
#
# MessageText:
#
# Illegal modify operation. Some aspect of the modification is not permitted.
#
ERROR_DS_ILLEGAL_MOD_OPERATION = 8311

#
# MessageId: ERROR_DS_OBJ_TOO_LARGE
#
# MessageText:
#
# The specified object is too large.
#
ERROR_DS_OBJ_TOO_LARGE = 8312

#
# MessageId: ERROR_DS_BAD_INSTANCE_TYPE
#
# MessageText:
#
# The specified instance type is not valid.
#
ERROR_DS_BAD_INSTANCE_TYPE = 8313

#
# MessageId: ERROR_DS_MASTERDSA_REQUIRED
#
# MessageText:
#
# The operation must be performed at a master DSA.
#
ERROR_DS_MASTERDSA_REQUIRED = 8314

#
# MessageId: ERROR_DS_OBJECT_CLASS_REQUIRED
#
# MessageText:
#
# The object class attribute must be specified.
#
ERROR_DS_OBJECT_CLASS_REQUIRED = 8315

#
# MessageId: ERROR_DS_MISSING_REQUIRED_ATT
#
# MessageText:
#
# A required attribute is missing.
#
ERROR_DS_MISSING_REQUIRED_ATT = 8316

#
# MessageId: ERROR_DS_ATT_NOT_DEF_FOR_CLASS
#
# MessageText:
#
# An attempt was made to modify an object to include an attribute that is not legal for its class.
#
ERROR_DS_ATT_NOT_DEF_FOR_CLASS = 8317

#
# MessageId: ERROR_DS_ATT_ALREADY_EXISTS
#
# MessageText:
#
# The specified attribute is already present on the object.
#
ERROR_DS_ATT_ALREADY_EXISTS = 8318

# 8319 unused
#
# MessageId: ERROR_DS_CANT_ADD_ATT_VALUES
#
# MessageText:
#
# The specified attribute is not present, or has no values.
#
ERROR_DS_CANT_ADD_ATT_VALUES = 8320

#
# MessageId: ERROR_DS_SINGLE_VALUE_CONSTRAINT
#
# MessageText:
#
# Multiple values were specified for an attribute that can have only one value.
#
ERROR_DS_SINGLE_VALUE_CONSTRAINT = 8321

#
# MessageId: ERROR_DS_RANGE_CONSTRAINT
#
# MessageText:
#
# A value for the attribute was not in the acceptable range of values.
#
ERROR_DS_RANGE_CONSTRAINT = 8322

#
# MessageId: ERROR_DS_ATT_VAL_ALREADY_EXISTS
#
# MessageText:
#
# The specified value already exists.
#
ERROR_DS_ATT_VAL_ALREADY_EXISTS = 8323

#
# MessageId: ERROR_DS_CANT_REM_MISSING_ATT
#
# MessageText:
#
# The attribute cannot be removed because it is not present on the object.
#
ERROR_DS_CANT_REM_MISSING_ATT = 8324

#
# MessageId: ERROR_DS_CANT_REM_MISSING_ATT_VAL
#
# MessageText:
#
# The attribute value cannot be removed because it is not present on the object.
#
ERROR_DS_CANT_REM_MISSING_ATT_VAL = 8325

#
# MessageId: ERROR_DS_ROOT_CANT_BE_SUBREF
#
# MessageText:
#
# The specified root object cannot be a subref.
#
ERROR_DS_ROOT_CANT_BE_SUBREF = 8326

#
# MessageId: ERROR_DS_NO_CHAINING
#
# MessageText:
#
# Chaining is not permitted.
#
ERROR_DS_NO_CHAINING = 8327

#
# MessageId: ERROR_DS_NO_CHAINED_EVAL
#
# MessageText:
#
# Chained evaluation is not permitted.
#
ERROR_DS_NO_CHAINED_EVAL = 8328

#
# MessageId: ERROR_DS_NO_PARENT_OBJECT
#
# MessageText:
#
# The operation could not be performed because the object's parent is either uninstantiated or deleted.
#
ERROR_DS_NO_PARENT_OBJECT = 8329

#
# MessageId: ERROR_DS_PARENT_IS_AN_ALIAS
#
# MessageText:
#
# Having a parent that is an alias is not permitted. Aliases are leaf objects.
#
ERROR_DS_PARENT_IS_AN_ALIAS = 8330

#
# MessageId: ERROR_DS_CANT_MIX_MASTER_AND_REPS
#
# MessageText:
#
# The object and parent must be of the same type, either both masters or both replicas.
#
ERROR_DS_CANT_MIX_MASTER_AND_REPS = 8331

#
# MessageId: ERROR_DS_CHILDREN_EXIST
#
# MessageText:
#
# The operation cannot be performed because child objects exist. This operation can only be performed on a leaf object.
#
ERROR_DS_CHILDREN_EXIST = 8332

#
# MessageId: ERROR_DS_OBJ_NOT_FOUND
#
# MessageText:
#
# Directory object not found.
#
ERROR_DS_OBJ_NOT_FOUND = 8333

#
# MessageId: ERROR_DS_ALIASED_OBJ_MISSING
#
# MessageText:
#
# The aliased object is missing.
#
ERROR_DS_ALIASED_OBJ_MISSING = 8334

#
# MessageId: ERROR_DS_BAD_NAME_SYNTAX
#
# MessageText:
#
# The object name has bad syntax.
#
ERROR_DS_BAD_NAME_SYNTAX = 8335

#
# MessageId: ERROR_DS_ALIAS_POINTS_TO_ALIAS
#
# MessageText:
#
# It is not permitted for an alias to refer to another alias.
#
ERROR_DS_ALIAS_POINTS_TO_ALIAS = 8336

#
# MessageId: ERROR_DS_CANT_DEREF_ALIAS
#
# MessageText:
#
# The alias cannot be dereferenced.
#
ERROR_DS_CANT_DEREF_ALIAS = 8337

#
# MessageId: ERROR_DS_OUT_OF_SCOPE
#
# MessageText:
#
# The operation is out of scope.
#
ERROR_DS_OUT_OF_SCOPE = 8338

#
# MessageId: ERROR_DS_OBJECT_BEING_REMOVED
#
# MessageText:
#
# The operation cannot continue because the object is in the process of being removed.
#
ERROR_DS_OBJECT_BEING_REMOVED = 8339

#
# MessageId: ERROR_DS_CANT_DELETE_DSA_OBJ
#
# MessageText:
#
# The DSA object cannot be deleted.
#
ERROR_DS_CANT_DELETE_DSA_OBJ = 8340

#
# MessageId: ERROR_DS_GENERIC_ERROR
#
# MessageText:
#
# A directory service error has occurred.
#
ERROR_DS_GENERIC_ERROR = 8341

#
# MessageId: ERROR_DS_DSA_MUST_BE_INT_MASTER
#
# MessageText:
#
# The operation can only be performed on an internal master DSA object.
#
ERROR_DS_DSA_MUST_BE_INT_MASTER = 8342

#
# MessageId: ERROR_DS_CLASS_NOT_DSA
#
# MessageText:
#
# The object must be of class DSA.
#
ERROR_DS_CLASS_NOT_DSA = 8343

#
# MessageId: ERROR_DS_INSUFF_ACCESS_RIGHTS
#
# MessageText:
#
# Insufficient access rights to perform the operation.
#
ERROR_DS_INSUFF_ACCESS_RIGHTS = 8344

#
# MessageId: ERROR_DS_ILLEGAL_SUPERIOR
#
# MessageText:
#
# The object cannot be added because the parent is not on the list of possible superiors.
#
ERROR_DS_ILLEGAL_SUPERIOR = 8345

#
# MessageId: ERROR_DS_ATTRIBUTE_OWNED_BY_SAM
#
# MessageText:
#
# Access to the attribute is not permitted because the attribute is owned by the Security Accounts Manager (SAM).
#
ERROR_DS_ATTRIBUTE_OWNED_BY_SAM = 8346

#
# MessageId: ERROR_DS_NAME_TOO_MANY_PARTS
#
# MessageText:
#
# The name has too many parts.
#
ERROR_DS_NAME_TOO_MANY_PARTS = 8347

#
# MessageId: ERROR_DS_NAME_TOO_LONG
#
# MessageText:
#
# The name is too long.
#
ERROR_DS_NAME_TOO_LONG = 8348

#
# MessageId: ERROR_DS_NAME_VALUE_TOO_LONG
#
# MessageText:
#
# The name value is too long.
#
ERROR_DS_NAME_VALUE_TOO_LONG = 8349

#
# MessageId: ERROR_DS_NAME_UNPARSEABLE
#
# MessageText:
#
# The directory service encountered an error parsing a name.
#
ERROR_DS_NAME_UNPARSEABLE = 8350

#
# MessageId: ERROR_DS_NAME_TYPE_UNKNOWN
#
# MessageText:
#
# The directory service cannot get the attribute type for a name.
#
ERROR_DS_NAME_TYPE_UNKNOWN = 8351

#
# MessageId: ERROR_DS_NOT_AN_OBJECT
#
# MessageText:
#
# The name does not identify an object; the name identifies a phantom.
#
ERROR_DS_NOT_AN_OBJECT = 8352

#
# MessageId: ERROR_DS_SEC_DESC_TOO_SHORT
#
# MessageText:
#
# The security descriptor is too short.
#
ERROR_DS_SEC_DESC_TOO_SHORT = 8353

#
# MessageId: ERROR_DS_SEC_DESC_INVALID
#
# MessageText:
#
# The security descriptor is invalid.
#
ERROR_DS_SEC_DESC_INVALID = 8354

#
# MessageId: ERROR_DS_NO_DELETED_NAME
#
# MessageText:
#
# Failed to create name for deleted object.
#
ERROR_DS_NO_DELETED_NAME = 8355

#
# MessageId: ERROR_DS_SUBREF_MUST_HAVE_PARENT
#
# MessageText:
#
# The parent of a new subref must exist.
#
ERROR_DS_SUBREF_MUST_HAVE_PARENT = 8356

#
# MessageId: ERROR_DS_NCNAME_MUST_BE_NC
#
# MessageText:
#
# The object must be a naming context.
#
ERROR_DS_NCNAME_MUST_BE_NC = 8357

#
# MessageId: ERROR_DS_CANT_ADD_SYSTEM_ONLY
#
# MessageText:
#
# It is not permitted to add an attribute which is owned by the system.
#
ERROR_DS_CANT_ADD_SYSTEM_ONLY = 8358

#
# MessageId: ERROR_DS_CLASS_MUST_BE_CONCRETE
#
# MessageText:
#
# The class of the object must be structural; you cannot instantiate an abstract class.
#
ERROR_DS_CLASS_MUST_BE_CONCRETE = 8359

#
# MessageId: ERROR_DS_INVALID_DMD
#
# MessageText:
#
# The schema object could not be found.
#
ERROR_DS_INVALID_DMD = 8360

#
# MessageId: ERROR_DS_OBJ_GUID_EXISTS
#
# MessageText:
#
# A local object with this GUID (dead or alive) already exists.
#
ERROR_DS_OBJ_GUID_EXISTS = 8361

#
# MessageId: ERROR_DS_NOT_ON_BACKLINK
#
# MessageText:
#
# The operation cannot be performed on a back link.
#
ERROR_DS_NOT_ON_BACKLINK = 8362

#
# MessageId: ERROR_DS_NO_CROSSREF_FOR_NC
#
# MessageText:
#
# The cross reference for the specified naming context could not be found.
#
ERROR_DS_NO_CROSSREF_FOR_NC = 8363

#
# MessageId: ERROR_DS_SHUTTING_DOWN
#
# MessageText:
#
# The operation could not be performed because the directory service is shutting down.
#
ERROR_DS_SHUTTING_DOWN = 8364

#
# MessageId: ERROR_DS_UNKNOWN_OPERATION
#
# MessageText:
#
# The directory service request is invalid.
#
ERROR_DS_UNKNOWN_OPERATION = 8365

#
# MessageId: ERROR_DS_INVALID_ROLE_OWNER
#
# MessageText:
#
# The role owner attribute could not be read.
#
ERROR_DS_INVALID_ROLE_OWNER = 8366

#
# MessageId: ERROR_DS_COULDNT_CONTACT_FSMO
#
# MessageText:
#
# The requested FSMO operation failed. The current FSMO holder could not be contacted.
#
ERROR_DS_COULDNT_CONTACT_FSMO = 8367

#
# MessageId: ERROR_DS_CROSS_NC_DN_RENAME
#
# MessageText:
#
# Modification of a DN across a naming context is not permitted.
#
ERROR_DS_CROSS_NC_DN_RENAME = 8368

#
# MessageId: ERROR_DS_CANT_MOD_SYSTEM_ONLY
#
# MessageText:
#
# The attribute cannot be modified because it is owned by the system.
#
ERROR_DS_CANT_MOD_SYSTEM_ONLY = 8369

#
# MessageId: ERROR_DS_REPLICATOR_ONLY
#
# MessageText:
#
# Only the replicator can perform this function.
#
ERROR_DS_REPLICATOR_ONLY = 8370

#
# MessageId: ERROR_DS_OBJ_CLASS_NOT_DEFINED
#
# MessageText:
#
# The specified class is not defined.
#
ERROR_DS_OBJ_CLASS_NOT_DEFINED = 8371

#
# MessageId: ERROR_DS_OBJ_CLASS_NOT_SUBCLASS
#
# MessageText:
#
# The specified class is not a subclass.
#
ERROR_DS_OBJ_CLASS_NOT_SUBCLASS = 8372

#
# MessageId: ERROR_DS_NAME_REFERENCE_INVALID
#
# MessageText:
#
# The name reference is invalid.
#
ERROR_DS_NAME_REFERENCE_INVALID = 8373

#
# MessageId: ERROR_DS_CROSS_REF_EXISTS
#
# MessageText:
#
# A cross reference already exists.
#
ERROR_DS_CROSS_REF_EXISTS = 8374

#
# MessageId: ERROR_DS_CANT_DEL_MASTER_CROSSREF
#
# MessageText:
#
# It is not permitted to delete a master cross reference.
#
ERROR_DS_CANT_DEL_MASTER_CROSSREF = 8375

#
# MessageId: ERROR_DS_SUBTREE_NOTIFY_NOT_NC_HEAD
#
# MessageText:
#
# Subtree notifications are only supported on NC heads.
#
ERROR_DS_SUBTREE_NOTIFY_NOT_NC_HEAD = 8376

#
# MessageId: ERROR_DS_NOTIFY_FILTER_TOO_COMPLEX
#
# MessageText:
#
# Notification filter is too complex.
#
ERROR_DS_NOTIFY_FILTER_TOO_COMPLEX = 8377

#
# MessageId: ERROR_DS_DUP_RDN
#
# MessageText:
#
# Schema update failed: duplicate RDN.
#
ERROR_DS_DUP_RDN = 8378

#
# MessageId: ERROR_DS_DUP_OID
#
# MessageText:
#
# Schema update failed: duplicate OID.
#
ERROR_DS_DUP_OID = 8379

#
# MessageId: ERROR_DS_DUP_MAPI_ID
#
# MessageText:
#
# Schema update failed: duplicate MAPI identifier.
#
ERROR_DS_DUP_MAPI_ID = 8380

#
# MessageId: ERROR_DS_DUP_SCHEMA_ID_GUID
#
# MessageText:
#
# Schema update failed: duplicate schema-id GUID.
#
ERROR_DS_DUP_SCHEMA_ID_GUID = 8381

#
# MessageId: ERROR_DS_DUP_LDAP_DISPLAY_NAME
#
# MessageText:
#
# Schema update failed: duplicate LDAP display name.
#
ERROR_DS_DUP_LDAP_DISPLAY_NAME = 8382

#
# MessageId: ERROR_DS_SEMANTIC_ATT_TEST
#
# MessageText:
#
# Schema update failed: range-lower less than range upper.
#
ERROR_DS_SEMANTIC_ATT_TEST = 8383

#
# MessageId: ERROR_DS_SYNTAX_MISMATCH
#
# MessageText:
#
# Schema update failed: syntax mismatch.
#
ERROR_DS_SYNTAX_MISMATCH = 8384

#
# MessageId: ERROR_DS_EXISTS_IN_MUST_HAVE
#
# MessageText:
#
# Schema deletion failed: attribute is used in must-contain.
#
ERROR_DS_EXISTS_IN_MUST_HAVE = 8385

#
# MessageId: ERROR_DS_EXISTS_IN_MAY_HAVE
#
# MessageText:
#
# Schema deletion failed: attribute is used in may-contain.
#
ERROR_DS_EXISTS_IN_MAY_HAVE = 8386

#
# MessageId: ERROR_DS_NONEXISTENT_MAY_HAVE
#
# MessageText:
#
# Schema update failed: attribute in may-contain does not exist.
#
ERROR_DS_NONEXISTENT_MAY_HAVE = 8387

#
# MessageId: ERROR_DS_NONEXISTENT_MUST_HAVE
#
# MessageText:
#
# Schema update failed: attribute in must-contain does not exist.
#
ERROR_DS_NONEXISTENT_MUST_HAVE = 8388

#
# MessageId: ERROR_DS_AUX_CLS_TEST_FAIL
#
# MessageText:
#
# Schema update failed: class in aux-class list does not exist or is not an auxiliary class.
#
ERROR_DS_AUX_CLS_TEST_FAIL = 8389

#
# MessageId: ERROR_DS_NONEXISTENT_POSS_SUP
#
# MessageText:
#
# Schema update failed: class in poss-superiors does not exist.
#
ERROR_DS_NONEXISTENT_POSS_SUP = 8390

#
# MessageId: ERROR_DS_SUB_CLS_TEST_FAIL
#
# MessageText:
#
# Schema update failed: class in subclassof list does not exist or does not satisfy hierarchy rules.
#
ERROR_DS_SUB_CLS_TEST_FAIL = 8391

#
# MessageId: ERROR_DS_BAD_RDN_ATT_ID_SYNTAX
#
# MessageText:
#
# Schema update failed: Rdn-Att-Id has wrong syntax.
#
ERROR_DS_BAD_RDN_ATT_ID_SYNTAX = 8392

#
# MessageId: ERROR_DS_EXISTS_IN_AUX_CLS
#
# MessageText:
#
# Schema deletion failed: class is used as auxiliary class.
#
ERROR_DS_EXISTS_IN_AUX_CLS = 8393

#
# MessageId: ERROR_DS_EXISTS_IN_SUB_CLS
#
# MessageText:
#
# Schema deletion failed: class is used as sub class.
#
ERROR_DS_EXISTS_IN_SUB_CLS = 8394

#
# MessageId: ERROR_DS_EXISTS_IN_POSS_SUP
#
# MessageText:
#
# Schema deletion failed: class is used as poss superior.
#
ERROR_DS_EXISTS_IN_POSS_SUP = 8395

#
# MessageId: ERROR_DS_RECALCSCHEMA_FAILED
#
# MessageText:
#
# Schema update failed in recalculating validation cache.
#
ERROR_DS_RECALCSCHEMA_FAILED = 8396

#
# MessageId: ERROR_DS_TREE_DELETE_NOT_FINISHED
#
# MessageText:
#
# The tree deletion is not finished. The request must be made again to continue deleting the tree.
#
ERROR_DS_TREE_DELETE_NOT_FINISHED = 8397

#
# MessageId: ERROR_DS_CANT_DELETE
#
# MessageText:
#
# The requested delete operation could not be performed.
#
ERROR_DS_CANT_DELETE = 8398

#
# MessageId: ERROR_DS_ATT_SCHEMA_REQ_ID
#
# MessageText:
#
# Cannot read the governs class identifier for the schema record.
#
ERROR_DS_ATT_SCHEMA_REQ_ID = 8399

#
# MessageId: ERROR_DS_BAD_ATT_SCHEMA_SYNTAX
#
# MessageText:
#
# The attribute schema has bad syntax.
#
ERROR_DS_BAD_ATT_SCHEMA_SYNTAX = 8400

#
# MessageId: ERROR_DS_CANT_CACHE_ATT
#
# MessageText:
#
# The attribute could not be cached.
#
ERROR_DS_CANT_CACHE_ATT = 8401

#
# MessageId: ERROR_DS_CANT_CACHE_CLASS
#
# MessageText:
#
# The class could not be cached.
#
ERROR_DS_CANT_CACHE_CLASS = 8402

#
# MessageId: ERROR_DS_CANT_REMOVE_ATT_CACHE
#
# MessageText:
#
# The attribute could not be removed from the cache.
#
ERROR_DS_CANT_REMOVE_ATT_CACHE = 8403

#
# MessageId: ERROR_DS_CANT_REMOVE_CLASS_CACHE
#
# MessageText:
#
# The class could not be removed from the cache.
#
ERROR_DS_CANT_REMOVE_CLASS_CACHE = 8404

#
# MessageId: ERROR_DS_CANT_RETRIEVE_DN
#
# MessageText:
#
# The distinguished name attribute could not be read.
#
ERROR_DS_CANT_RETRIEVE_DN = 8405

#
# MessageId: ERROR_DS_MISSING_SUPREF
#
# MessageText:
#
# No superior reference has been configured for the directory service. The directory service is therefore unable to issue referrals to objects outside this forest.
#
ERROR_DS_MISSING_SUPREF = 8406

#
# MessageId: ERROR_DS_CANT_RETRIEVE_INSTANCE
#
# MessageText:
#
# The instance type attribute could not be retrieved.
#
ERROR_DS_CANT_RETRIEVE_INSTANCE = 8407

#
# MessageId: ERROR_DS_CODE_INCONSISTENCY
#
# MessageText:
#
# An internal error has occurred.
#
ERROR_DS_CODE_INCONSISTENCY = 8408

#
# MessageId: ERROR_DS_DATABASE_ERROR
#
# MessageText:
#
# A database error has occurred.
#
ERROR_DS_DATABASE_ERROR = 8409

#
# MessageId: ERROR_DS_GOVERNSID_MISSING
#
# MessageText:
#
# The attribute GOVERNSID is missing.
#
ERROR_DS_GOVERNSID_MISSING = 8410

#
# MessageId: ERROR_DS_MISSING_EXPECTED_ATT
#
# MessageText:
#
# An expected attribute is missing.
#
ERROR_DS_MISSING_EXPECTED_ATT = 8411

#
# MessageId: ERROR_DS_NCNAME_MISSING_CR_REF
#
# MessageText:
#
# The specified naming context is missing a cross reference.
#
ERROR_DS_NCNAME_MISSING_CR_REF = 8412

#
# MessageId: ERROR_DS_SECURITY_CHECKING_ERROR
#
# MessageText:
#
# A security checking error has occurred.
#
ERROR_DS_SECURITY_CHECKING_ERROR = 8413

#
# MessageId: ERROR_DS_SCHEMA_NOT_LOADED
#
# MessageText:
#
# The schema is not loaded.
#
ERROR_DS_SCHEMA_NOT_LOADED = 8414

#
# MessageId: ERROR_DS_SCHEMA_ALLOC_FAILED
#
# MessageText:
#
# Schema allocation failed. Please check if the machine is running low on memory.
#
ERROR_DS_SCHEMA_ALLOC_FAILED = 8415

#
# MessageId: ERROR_DS_ATT_SCHEMA_REQ_SYNTAX
#
# MessageText:
#
# Failed to obtain the required syntax for the attribute schema.
#
ERROR_DS_ATT_SCHEMA_REQ_SYNTAX = 8416

#
# MessageId: ERROR_DS_GCVERIFY_ERROR
#
# MessageText:
#
# The global catalog verification failed. The global catalog is not available or does not support the operation. Some part of the directory is currently not available.
#
ERROR_DS_GCVERIFY_ERROR = 8417

#
# MessageId: ERROR_DS_DRA_SCHEMA_MISMATCH
#
# MessageText:
#
# The replication operation failed because of a schema mismatch between the servers involved.
#
ERROR_DS_DRA_SCHEMA_MISMATCH = 8418

#
# MessageId: ERROR_DS_CANT_FIND_DSA_OBJ
#
# MessageText:
#
# The DSA object could not be found.
#
ERROR_DS_CANT_FIND_DSA_OBJ = 8419

#
# MessageId: ERROR_DS_CANT_FIND_EXPECTED_NC
#
# MessageText:
#
# The naming context could not be found.
#
ERROR_DS_CANT_FIND_EXPECTED_NC = 8420

#
# MessageId: ERROR_DS_CANT_FIND_NC_IN_CACHE
#
# MessageText:
#
# The naming context could not be found in the cache.
#
ERROR_DS_CANT_FIND_NC_IN_CACHE = 8421

#
# MessageId: ERROR_DS_CANT_RETRIEVE_CHILD
#
# MessageText:
#
# The child object could not be retrieved.
#
ERROR_DS_CANT_RETRIEVE_CHILD = 8422

#
# MessageId: ERROR_DS_SECURITY_ILLEGAL_MODIFY
#
# MessageText:
#
# The modification was not permitted for security reasons.
#
ERROR_DS_SECURITY_ILLEGAL_MODIFY = 8423

#
# MessageId: ERROR_DS_CANT_REPLACE_HIDDEN_REC
#
# MessageText:
#
# The operation cannot replace the hidden record.
#
ERROR_DS_CANT_REPLACE_HIDDEN_REC = 8424

#
# MessageId: ERROR_DS_BAD_HIERARCHY_FILE
#
# MessageText:
#
# The hierarchy file is invalid.
#
ERROR_DS_BAD_HIERARCHY_FILE = 8425

#
# MessageId: ERROR_DS_BUILD_HIERARCHY_TABLE_FAILED
#
# MessageText:
#
# The attempt to build the hierarchy table failed.
#
ERROR_DS_BUILD_HIERARCHY_TABLE_FAILED = 8426

#
# MessageId: ERROR_DS_CONFIG_PARAM_MISSING
#
# MessageText:
#
# The directory configuration parameter is missing from the registry.
#
ERROR_DS_CONFIG_PARAM_MISSING = 8427

#
# MessageId: ERROR_DS_COUNTING_AB_INDICES_FAILED
#
# MessageText:
#
# The attempt to count the address book indices failed.
#
ERROR_DS_COUNTING_AB_INDICES_FAILED = 8428

#
# MessageId: ERROR_DS_HIERARCHY_TABLE_MALLOC_FAILED
#
# MessageText:
#
# The allocation of the hierarchy table failed.
#
ERROR_DS_HIERARCHY_TABLE_MALLOC_FAILED = 8429

#
# MessageId: ERROR_DS_INTERNAL_FAILURE
#
# MessageText:
#
# The directory service encountered an internal failure.
#
ERROR_DS_INTERNAL_FAILURE = 8430

#
# MessageId: ERROR_DS_UNKNOWN_ERROR
#
# MessageText:
#
# The directory service encountered an unknown failure.
#
ERROR_DS_UNKNOWN_ERROR = 8431

#
# MessageId: ERROR_DS_ROOT_REQUIRES_CLASS_TOP
#
# MessageText:
#
# A root object requires a class of 'top'.
#
ERROR_DS_ROOT_REQUIRES_CLASS_TOP = 8432

#
# MessageId: ERROR_DS_REFUSING_FSMO_ROLES
#
# MessageText:
#
# This directory server is shutting down, and cannot take ownership of new floating single-master operation roles.
#
ERROR_DS_REFUSING_FSMO_ROLES = 8433

#
# MessageId: ERROR_DS_MISSING_FSMO_SETTINGS
#
# MessageText:
#
# The directory service is missing mandatory configuration information, and is unable to determine the ownership of floating single-master operation roles.
#
ERROR_DS_MISSING_FSMO_SETTINGS = 8434

#
# MessageId: ERROR_DS_UNABLE_TO_SURRENDER_ROLES
#
# MessageText:
#
# The directory service was unable to transfer ownership of one or more floating single-master operation roles to other servers.
#
ERROR_DS_UNABLE_TO_SURRENDER_ROLES = 8435

#
# MessageId: ERROR_DS_DRA_GENERIC
#
# MessageText:
#
# The replication operation failed.
#
ERROR_DS_DRA_GENERIC = 8436

#
# MessageId: ERROR_DS_DRA_INVALID_PARAMETER
#
# MessageText:
#
# An invalid parameter was specified for this replication operation.
#
ERROR_DS_DRA_INVALID_PARAMETER = 8437

#
# MessageId: ERROR_DS_DRA_BUSY
#
# MessageText:
#
# The directory service is too busy to complete the replication operation at this time.
#
ERROR_DS_DRA_BUSY = 8438

#
# MessageId: ERROR_DS_DRA_BAD_DN
#
# MessageText:
#
# The distinguished name specified for this replication operation is invalid.
#
ERROR_DS_DRA_BAD_DN = 8439

#
# MessageId: ERROR_DS_DRA_BAD_NC
#
# MessageText:
#
# The naming context specified for this replication operation is invalid.
#
ERROR_DS_DRA_BAD_NC = 8440

#
# MessageId: ERROR_DS_DRA_DN_EXISTS
#
# MessageText:
#
# The distinguished name specified for this replication operation already exists.
#
ERROR_DS_DRA_DN_EXISTS = 8441

#
# MessageId: ERROR_DS_DRA_INTERNAL_ERROR
#
# MessageText:
#
# The replication system encountered an internal error.
#
ERROR_DS_DRA_INTERNAL_ERROR = 8442

#
# MessageId: ERROR_DS_DRA_INCONSISTENT_DIT
#
# MessageText:
#
# The replication operation encountered a database inconsistency.
#
ERROR_DS_DRA_INCONSISTENT_DIT = 8443

#
# MessageId: ERROR_DS_DRA_CONNECTION_FAILED
#
# MessageText:
#
# The server specified for this replication operation could not be contacted.
#
ERROR_DS_DRA_CONNECTION_FAILED = 8444

#
# MessageId: ERROR_DS_DRA_BAD_INSTANCE_TYPE
#
# MessageText:
#
# The replication operation encountered an object with an invalid instance type.
#
ERROR_DS_DRA_BAD_INSTANCE_TYPE = 8445

#
# MessageId: ERROR_DS_DRA_OUT_OF_MEM
#
# MessageText:
#
# The replication operation failed to allocate memory.
#
ERROR_DS_DRA_OUT_OF_MEM = 8446

#
# MessageId: ERROR_DS_DRA_MAIL_PROBLEM
#
# MessageText:
#
# The replication operation encountered an error with the mail system.
#
ERROR_DS_DRA_MAIL_PROBLEM = 8447

#
# MessageId: ERROR_DS_DRA_REF_ALREADY_EXISTS
#
# MessageText:
#
# The replication reference information for the target server already exists.
#
ERROR_DS_DRA_REF_ALREADY_EXISTS = 8448

#
# MessageId: ERROR_DS_DRA_REF_NOT_FOUND
#
# MessageText:
#
# The replication reference information for the target server does not exist.
#
ERROR_DS_DRA_REF_NOT_FOUND = 8449

#
# MessageId: ERROR_DS_DRA_OBJ_IS_REP_SOURCE
#
# MessageText:
#
# The naming context cannot be removed because it is replicated to another server.
#
ERROR_DS_DRA_OBJ_IS_REP_SOURCE = 8450

#
# MessageId: ERROR_DS_DRA_DB_ERROR
#
# MessageText:
#
# The replication operation encountered a database error.
#
ERROR_DS_DRA_DB_ERROR = 8451

#
# MessageId: ERROR_DS_DRA_NO_REPLICA
#
# MessageText:
#
# The naming context is in the process of being removed or is not replicated from the specified server.
#
ERROR_DS_DRA_NO_REPLICA = 8452

#
# MessageId: ERROR_DS_DRA_ACCESS_DENIED
#
# MessageText:
#
# Replication access was denied.
#
ERROR_DS_DRA_ACCESS_DENIED = 8453

#
# MessageId: ERROR_DS_DRA_NOT_SUPPORTED
#
# MessageText:
#
# The requested operation is not supported by this version of the directory service.
#
ERROR_DS_DRA_NOT_SUPPORTED = 8454

#
# MessageId: ERROR_DS_DRA_RPC_CANCELLED
#
# MessageText:
#
# The replication remote procedure call was cancelled.
#
ERROR_DS_DRA_RPC_CANCELLED = 8455

#
# MessageId: ERROR_DS_DRA_SOURCE_DISABLED
#
# MessageText:
#
# The source server is currently rejecting replication requests.
#
ERROR_DS_DRA_SOURCE_DISABLED = 8456

#
# MessageId: ERROR_DS_DRA_SINK_DISABLED
#
# MessageText:
#
# The destination server is currently rejecting replication requests.
#
ERROR_DS_DRA_SINK_DISABLED = 8457

#
# MessageId: ERROR_DS_DRA_NAME_COLLISION
#
# MessageText:
#
# The replication operation failed due to a collision of object names.
#
ERROR_DS_DRA_NAME_COLLISION = 8458

#
# MessageId: ERROR_DS_DRA_SOURCE_REINSTALLED
#
# MessageText:
#
# The replication source has been reinstalled.
#
ERROR_DS_DRA_SOURCE_REINSTALLED = 8459

#
# MessageId: ERROR_DS_DRA_MISSING_PARENT
#
# MessageText:
#
# The replication operation failed because a required parent object is missing.
#
ERROR_DS_DRA_MISSING_PARENT = 8460

#
# MessageId: ERROR_DS_DRA_PREEMPTED
#
# MessageText:
#
# The replication operation was preempted.
#
ERROR_DS_DRA_PREEMPTED = 8461

#
# MessageId: ERROR_DS_DRA_ABANDON_SYNC
#
# MessageText:
#
# The replication synchronization attempt was abandoned because of a lack of updates.
#
ERROR_DS_DRA_ABANDON_SYNC = 8462

#
# MessageId: ERROR_DS_DRA_SHUTDOWN
#
# MessageText:
#
# The replication operation was terminated because the system is shutting down.
#
ERROR_DS_DRA_SHUTDOWN = 8463

#
# MessageId: ERROR_DS_DRA_INCOMPATIBLE_PARTIAL_SET
#
# MessageText:
#
# Synchronization attempt failed because the destination DC is currently waiting to synchronize new partial attributes from source. This condition is normal if a recent schema change modified the partial attribute set. The destination partial attribute set is not a subset of source partial attribute set.
#
ERROR_DS_DRA_INCOMPATIBLE_PARTIAL_SET = 8464

#
# MessageId: ERROR_DS_DRA_SOURCE_IS_PARTIAL_REPLICA
#
# MessageText:
#
# The replication synchronization attempt failed because a master replica attempted to sync from a partial replica.
#
ERROR_DS_DRA_SOURCE_IS_PARTIAL_REPLICA = 8465

#
# MessageId: ERROR_DS_DRA_EXTN_CONNECTION_FAILED
#
# MessageText:
#
# The server specified for this replication operation was contacted, but that server was unable to contact an additional server needed to complete the operation.
#
ERROR_DS_DRA_EXTN_CONNECTION_FAILED = 8466

#
# MessageId: ERROR_DS_INSTALL_SCHEMA_MISMATCH
#
# MessageText:
#
# The version of the directory service schema of the source forest is not compatible with the version of directory service on this computer.
#
ERROR_DS_INSTALL_SCHEMA_MISMATCH = 8467

#
# MessageId: ERROR_DS_DUP_LINK_ID
#
# MessageText:
#
# Schema update failed: An attribute with the same link identifier already exists.
#
ERROR_DS_DUP_LINK_ID = 8468

#
# MessageId: ERROR_DS_NAME_ERROR_RESOLVING
#
# MessageText:
#
# Name translation: Generic processing error.
#
ERROR_DS_NAME_ERROR_RESOLVING = 8469

#
# MessageId: ERROR_DS_NAME_ERROR_NOT_FOUND
#
# MessageText:
#
# Name translation: Could not find the name or insufficient right to see name.
#
ERROR_DS_NAME_ERROR_NOT_FOUND = 8470

#
# MessageId: ERROR_DS_NAME_ERROR_NOT_UNIQUE
#
# MessageText:
#
# Name translation: Input name mapped to more than one output name.
#
ERROR_DS_NAME_ERROR_NOT_UNIQUE = 8471

#
# MessageId: ERROR_DS_NAME_ERROR_NO_MAPPING
#
# MessageText:
#
# Name translation: Input name found, but not the associated output format.
#
ERROR_DS_NAME_ERROR_NO_MAPPING = 8472

#
# MessageId: ERROR_DS_NAME_ERROR_DOMAIN_ONLY
#
# MessageText:
#
# Name translation: Unable to resolve completely, only the domain was found.
#
ERROR_DS_NAME_ERROR_DOMAIN_ONLY = 8473

#
# MessageId: ERROR_DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING
#
# MessageText:
#
# Name translation: Unable to perform purely syntactical mapping at the client without going out to the wire.
#
ERROR_DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING = 8474

#
# MessageId: ERROR_DS_CONSTRUCTED_ATT_MOD
#
# MessageText:
#
# Modification of a constructed attribute is not allowed.
#
ERROR_DS_CONSTRUCTED_ATT_MOD = 8475

#
# MessageId: ERROR_DS_WRONG_OM_OBJ_CLASS
#
# MessageText:
#
# The OM-Object-Class specified is incorrect for an attribute with the specified syntax.
#
ERROR_DS_WRONG_OM_OBJ_CLASS = 8476

#
# MessageId: ERROR_DS_DRA_REPL_PENDING
#
# MessageText:
#
# The replication request has been posted; waiting for reply.
#
ERROR_DS_DRA_REPL_PENDING = 8477

#
# MessageId: ERROR_DS_DS_REQUIRED
#
# MessageText:
#
# The requested operation requires a directory service, and none was available.
#
ERROR_DS_DS_REQUIRED = 8478

#
# MessageId: ERROR_DS_INVALID_LDAP_DISPLAY_NAME
#
# MessageText:
#
# The LDAP display name of the class or attribute contains non-ASCII characters.
#
ERROR_DS_INVALID_LDAP_DISPLAY_NAME = 8479

#
# MessageId: ERROR_DS_NON_BASE_SEARCH
#
# MessageText:
#
# The requested search operation is only supported for base searches.
#
ERROR_DS_NON_BASE_SEARCH = 8480

#
# MessageId: ERROR_DS_CANT_RETRIEVE_ATTS
#
# MessageText:
#
# The search failed to retrieve attributes from the database.
#
ERROR_DS_CANT_RETRIEVE_ATTS = 8481

#
# MessageId: ERROR_DS_BACKLINK_WITHOUT_LINK
#
# MessageText:
#
# The schema update operation tried to add a backward link attribute that has no corresponding forward link.
#
ERROR_DS_BACKLINK_WITHOUT_LINK = 8482

#
# MessageId: ERROR_DS_EPOCH_MISMATCH
#
# MessageText:
#
# Source and destination of a cross-domain move do not agree on the object's epoch number. Either source or destination does not have the latest version of the object.
#
ERROR_DS_EPOCH_MISMATCH = 8483

#
# MessageId: ERROR_DS_SRC_NAME_MISMATCH
#
# MessageText:
#
# Source and destination of a cross-domain move do not agree on the object's current name. Either source or destination does not have the latest version of the object.
#
ERROR_DS_SRC_NAME_MISMATCH = 8484

#
# MessageId: ERROR_DS_SRC_AND_DST_NC_IDENTICAL
#
# MessageText:
#
# Source and destination for the cross-domain move operation are identical. Caller should use local move operation instead of cross-domain move operation.
#
ERROR_DS_SRC_AND_DST_NC_IDENTICAL = 8485

#
# MessageId: ERROR_DS_DST_NC_MISMATCH
#
# MessageText:
#
# Source and destination for a cross-domain move are not in agreement on the naming contexts in the forest. Either source or destination does not have the latest version of the Partitions container.
#
ERROR_DS_DST_NC_MISMATCH = 8486

#
# MessageId: ERROR_DS_NOT_AUTHORITIVE_FOR_DST_NC
#
# MessageText:
#
# Destination of a cross-domain move is not authoritative for the destination naming context.
#
ERROR_DS_NOT_AUTHORITIVE_FOR_DST_NC = 8487

#
# MessageId: ERROR_DS_SRC_GUID_MISMATCH
#
# MessageText:
#
# Source and destination of a cross-domain move do not agree on the identity of the source object. Either source or destination does not have the latest version of the source object.
#
ERROR_DS_SRC_GUID_MISMATCH = 8488

#
# MessageId: ERROR_DS_CANT_MOVE_DELETED_OBJECT
#
# MessageText:
#
# Object being moved across-domains is already known to be deleted by the destination server. The source server does not have the latest version of the source object.
#
ERROR_DS_CANT_MOVE_DELETED_OBJECT = 8489

#
# MessageId: ERROR_DS_PDC_OPERATION_IN_PROGRESS
#
# MessageText:
#
# Another operation which requires exclusive access to the PDC FSMO is already in progress.
#
ERROR_DS_PDC_OPERATION_IN_PROGRESS = 8490

#
# MessageId: ERROR_DS_CROSS_DOMAIN_CLEANUP_REQD
#
# MessageText:
#
# A cross-domain move operation failed such that two versions of the moved object exist - one each in the source and destination domains. The destination object needs to be removed to restore the system to a consistent state.
#
ERROR_DS_CROSS_DOMAIN_CLEANUP_REQD = 8491

#
# MessageId: ERROR_DS_ILLEGAL_XDOM_MOVE_OPERATION
#
# MessageText:
#
# This object may not be moved across domain boundaries either because cross-domain moves for this class are disallowed, or the object has some special characteristics, e.g.: trust account or restricted RID, which prevent its move.
#
ERROR_DS_ILLEGAL_XDOM_MOVE_OPERATION = 8492

#
# MessageId: ERROR_DS_CANT_WITH_ACCT_GROUP_MEMBERSHPS
#
# MessageText:
#
# Can't move objects with memberships across domain boundaries as once moved, this would violate the membership conditions of the account group. Remove the object from any account group memberships and retry.
#
ERROR_DS_CANT_WITH_ACCT_GROUP_MEMBERSHPS = 8493

#
# MessageId: ERROR_DS_NC_MUST_HAVE_NC_PARENT
#
# MessageText:
#
# A naming context head must be the immediate child of another naming context head, not of an interior node.
#
ERROR_DS_NC_MUST_HAVE_NC_PARENT = 8494

#
# MessageId: ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE
#
# MessageText:
#
# The directory cannot validate the proposed naming context name because it does not hold a replica of the naming context above the proposed naming context. Please ensure that the domain naming master role is held by a server that is configured as a global catalog server, and that the server is up to date with its replication partners. (Applies only to Windows 2000 Domain Naming masters)
#
ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE = 8495

#
# MessageId: ERROR_DS_DST_DOMAIN_NOT_NATIVE
#
# MessageText:
#
# Destination domain must be in native mode.
#
ERROR_DS_DST_DOMAIN_NOT_NATIVE = 8496

#
# MessageId: ERROR_DS_MISSING_INFRASTRUCTURE_CONTAINER
#
# MessageText:
#
# The operation cannot be performed because the server does not have an infrastructure container in the domain of interest.
#
ERROR_DS_MISSING_INFRASTRUCTURE_CONTAINER = 8497

#
# MessageId: ERROR_DS_CANT_MOVE_ACCOUNT_GROUP
#
# MessageText:
#
# Cross-domain move of non-empty account groups is not allowed.
#
ERROR_DS_CANT_MOVE_ACCOUNT_GROUP = 8498

#
# MessageId: ERROR_DS_CANT_MOVE_RESOURCE_GROUP
#
# MessageText:
#
# Cross-domain move of non-empty resource groups is not allowed.
#
ERROR_DS_CANT_MOVE_RESOURCE_GROUP = 8499

#
# MessageId: ERROR_DS_INVALID_SEARCH_FLAG
#
# MessageText:
#
# The search flags for the attribute are invalid. The ANR bit is valid only on attributes of Unicode or Teletex strings.
#
ERROR_DS_INVALID_SEARCH_FLAG = 8500

#
# MessageId: ERROR_DS_NO_TREE_DELETE_ABOVE_NC
#
# MessageText:
#
# Tree deletions starting at an object which has an NC head as a descendant are not allowed.
#
ERROR_DS_NO_TREE_DELETE_ABOVE_NC = 8501

#
# MessageId: ERROR_DS_COULDNT_LOCK_TREE_FOR_DELETE
#
# MessageText:
#
# The directory service failed to lock a tree in preparation for a tree deletion because the tree was in use.
#
ERROR_DS_COULDNT_LOCK_TREE_FOR_DELETE = 8502

#
# MessageId: ERROR_DS_COULDNT_IDENTIFY_OBJECTS_FOR_TREE_DELETE
#
# MessageText:
#
# The directory service failed to identify the list of objects to delete while attempting a tree deletion.
#
ERROR_DS_COULDNT_IDENTIFY_OBJECTS_FOR_TREE_DELETE = 8503

#
# MessageId: ERROR_DS_SAM_INIT_FAILURE
#
# MessageText:
#
# Security Accounts Manager initialization failed because of the following error: %1.
# Error Status: 0x%2. Please shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.
#
ERROR_DS_SAM_INIT_FAILURE = 8504

#
# MessageId: ERROR_DS_SENSITIVE_GROUP_VIOLATION
#
# MessageText:
#
# Only an administrator can modify the membership list of an administrative group.
#
ERROR_DS_SENSITIVE_GROUP_VIOLATION = 8505

#
# MessageId: ERROR_DS_CANT_MOD_PRIMARYGROUPID
#
# MessageText:
#
# Cannot change the primary group ID of a domain controller account.
#
ERROR_DS_CANT_MOD_PRIMARYGROUPID = 8506

#
# MessageId: ERROR_DS_ILLEGAL_BASE_SCHEMA_MOD
#
# MessageText:
#
# An attempt is made to modify the base schema.
#
ERROR_DS_ILLEGAL_BASE_SCHEMA_MOD = 8507

#
# MessageId: ERROR_DS_NONSAFE_SCHEMA_CHANGE
#
# MessageText:
#
# Adding a new mandatory attribute to an existing class, deleting a mandatory attribute from an existing class, or adding an optional attribute to the special class Top that is not a backlink attribute (directly or through inheritance, for example, by adding or deleting an auxiliary class) is not allowed.
#
ERROR_DS_NONSAFE_SCHEMA_CHANGE = 8508

#
# MessageId: ERROR_DS_SCHEMA_UPDATE_DISALLOWED
#
# MessageText:
#
# Schema update is not allowed on this DC because the DC is not the schema FSMO Role Owner.
#
ERROR_DS_SCHEMA_UPDATE_DISALLOWED = 8509

#
# MessageId: ERROR_DS_CANT_CREATE_UNDER_SCHEMA
#
# MessageText:
#
# An object of this class cannot be created under the schema container. You can only create attribute-schema and class-schema objects under the schema container.
#
ERROR_DS_CANT_CREATE_UNDER_SCHEMA = 8510

#
# MessageId: ERROR_DS_INSTALL_NO_SRC_SCH_VERSION
#
# MessageText:
#
# The replica/child install failed to get the objectVersion attribute on the schema container on the source DC. Either the attribute is missing on the schema container or the credentials supplied do not have permission to read it.
#
ERROR_DS_INSTALL_NO_SRC_SCH_VERSION = 8511

#
# MessageId: ERROR_DS_INSTALL_NO_SCH_VERSION_IN_INIFILE
#
# MessageText:
#
# The replica/child install failed to read the objectVersion attribute in the SCHEMA section of the file schema.ini in the system32 directory.
#
ERROR_DS_INSTALL_NO_SCH_VERSION_IN_INIFILE = 8512

#
# MessageId: ERROR_DS_INVALID_GROUP_TYPE
#
# MessageText:
#
# The specified group type is invalid.
#
ERROR_DS_INVALID_GROUP_TYPE = 8513

#
# MessageId: ERROR_DS_NO_NEST_GLOBALGROUP_IN_MIXEDDOMAIN
#
# MessageText:
#
# You cannot nest global groups in a mixed domain if the group is security-enabled.
#
ERROR_DS_NO_NEST_GLOBALGROUP_IN_MIXEDDOMAIN = 8514

#
# MessageId: ERROR_DS_NO_NEST_LOCALGROUP_IN_MIXEDDOMAIN
#
# MessageText:
#
# You cannot nest local groups in a mixed domain if the group is security-enabled.
#
ERROR_DS_NO_NEST_LOCALGROUP_IN_MIXEDDOMAIN = 8515

#
# MessageId: ERROR_DS_GLOBAL_CANT_HAVE_LOCAL_MEMBER
#
# MessageText:
#
# A global group cannot have a local group as a member.
#
ERROR_DS_GLOBAL_CANT_HAVE_LOCAL_MEMBER = 8516

#
# MessageId: ERROR_DS_GLOBAL_CANT_HAVE_UNIVERSAL_MEMBER
#
# MessageText:
#
# A global group cannot have a universal group as a member.
#
ERROR_DS_GLOBAL_CANT_HAVE_UNIVERSAL_MEMBER = 8517

#
# MessageId: ERROR_DS_UNIVERSAL_CANT_HAVE_LOCAL_MEMBER
#
# MessageText:
#
# A universal group cannot have a local group as a member.
#
ERROR_DS_UNIVERSAL_CANT_HAVE_LOCAL_MEMBER = 8518

#
# MessageId: ERROR_DS_GLOBAL_CANT_HAVE_CROSSDOMAIN_MEMBER
#
# MessageText:
#
# A global group cannot have a cross-domain member.
#
ERROR_DS_GLOBAL_CANT_HAVE_CROSSDOMAIN_MEMBER = 8519

#
# MessageId: ERROR_DS_LOCAL_CANT_HAVE_CROSSDOMAIN_LOCAL_MEMBER
#
# MessageText:
#
# A local group cannot have another cross domain local group as a member.
#
ERROR_DS_LOCAL_CANT_HAVE_CROSSDOMAIN_LOCAL_MEMBER = 8520

#
# MessageId: ERROR_DS_HAVE_PRIMARY_MEMBERS
#
# MessageText:
#
# A group with primary members cannot change to a security-disabled group.
#
ERROR_DS_HAVE_PRIMARY_MEMBERS = 8521

#
# MessageId: ERROR_DS_STRING_SD_CONVERSION_FAILED
#
# MessageText:
#
# The schema cache load failed to convert the string default SD on a class-schema object.
#
ERROR_DS_STRING_SD_CONVERSION_FAILED = 8522

#
# MessageId: ERROR_DS_NAMING_MASTER_GC
#
# MessageText:
#
# Only DSAs configured to be Global Catalog servers should be allowed to hold the Domain Naming Master FSMO role. (Applies only to Windows 2000 servers)
#
ERROR_DS_NAMING_MASTER_GC = 8523

#
# MessageId: ERROR_DS_DNS_LOOKUP_FAILURE
#
# MessageText:
#
# The DSA operation is unable to proceed because of a DNS lookup failure.
#
ERROR_DS_DNS_LOOKUP_FAILURE = 8524

#
# MessageId: ERROR_DS_COULDNT_UPDATE_SPNS
#
# MessageText:
#
# While processing a change to the DNS Host Name for an object, the Service Principal Name values could not be kept in sync.
#
ERROR_DS_COULDNT_UPDATE_SPNS = 8525

#
# MessageId: ERROR_DS_CANT_RETRIEVE_SD
#
# MessageText:
#
# The Security Descriptor attribute could not be read.
#
ERROR_DS_CANT_RETRIEVE_SD = 8526

#
# MessageId: ERROR_DS_KEY_NOT_UNIQUE
#
# MessageText:
#
# The object requested was not found, but an object with that key was found.
#
ERROR_DS_KEY_NOT_UNIQUE = 8527

#
# MessageId: ERROR_DS_WRONG_LINKED_ATT_SYNTAX
#
# MessageText:
#
# The syntax of the linked attribute being added is incorrect. Forward links can only have syntax 2.5.5.1, 2.5.5.7, and 2.5.5.14, and backlinks can only have syntax 2.5.5.1
#
ERROR_DS_WRONG_LINKED_ATT_SYNTAX = 8528

#
# MessageId: ERROR_DS_SAM_NEED_BOOTKEY_PASSWORD
#
# MessageText:
#
# Security Account Manager needs to get the boot password.
#
ERROR_DS_SAM_NEED_BOOTKEY_PASSWORD = 8529

#
# MessageId: ERROR_DS_SAM_NEED_BOOTKEY_FLOPPY
#
# MessageText:
#
# Security Account Manager needs to get the boot key from floppy disk.
#
ERROR_DS_SAM_NEED_BOOTKEY_FLOPPY = 8530

#
# MessageId: ERROR_DS_CANT_START
#
# MessageText:
#
# Directory Service cannot start.
#
ERROR_DS_CANT_START = 8531

#
# MessageId: ERROR_DS_INIT_FAILURE
#
# MessageText:
#
# Directory Services could not start.
#
ERROR_DS_INIT_FAILURE = 8532

#
# MessageId: ERROR_DS_NO_PKT_PRIVACY_ON_CONNECTION
#
# MessageText:
#
# The connection between client and server requires packet privacy or better.
#
ERROR_DS_NO_PKT_PRIVACY_ON_CONNECTION = 8533

#
# MessageId: ERROR_DS_SOURCE_DOMAIN_IN_FOREST
#
# MessageText:
#
# The source domain may not be in the same forest as destination.
#
ERROR_DS_SOURCE_DOMAIN_IN_FOREST = 8534

#
# MessageId: ERROR_DS_DESTINATION_DOMAIN_NOT_IN_FOREST
#
# MessageText:
#
# The destination domain must be in the forest.
#
ERROR_DS_DESTINATION_DOMAIN_NOT_IN_FOREST = 8535

#
# MessageId: ERROR_DS_DESTINATION_AUDITING_NOT_ENABLED
#
# MessageText:
#
# The operation requires that destination domain auditing be enabled.
#
ERROR_DS_DESTINATION_AUDITING_NOT_ENABLED = 8536

#
# MessageId: ERROR_DS_CANT_FIND_DC_FOR_SRC_DOMAIN
#
# MessageText:
#
# The operation couldn't locate a DC for the source domain.
#
ERROR_DS_CANT_FIND_DC_FOR_SRC_DOMAIN = 8537

#
# MessageId: ERROR_DS_SRC_OBJ_NOT_GROUP_OR_USER
#
# MessageText:
#
# The source object must be a group or user.
#
ERROR_DS_SRC_OBJ_NOT_GROUP_OR_USER = 8538

#
# MessageId: ERROR_DS_SRC_SID_EXISTS_IN_FOREST
#
# MessageText:
#
# The source object's SID already exists in destination forest.
#
ERROR_DS_SRC_SID_EXISTS_IN_FOREST = 8539

#
# MessageId: ERROR_DS_SRC_AND_DST_OBJECT_CLASS_MISMATCH
#
# MessageText:
#
# The source and destination object must be of the same type.
#
ERROR_DS_SRC_AND_DST_OBJECT_CLASS_MISMATCH = 8540

#
# MessageId: ERROR_SAM_INIT_FAILURE
#
# MessageText:
#
# Security Accounts Manager initialization failed because of the following error: %1.
# Error Status: 0x%2. Click OK to shut down the system and reboot into Safe Mode. Check the event log for detailed information.
#
ERROR_SAM_INIT_FAILURE = 8541

#
# MessageId: ERROR_DS_DRA_SCHEMA_INFO_SHIP
#
# MessageText:
#
# Schema information could not be included in the replication request.
#
ERROR_DS_DRA_SCHEMA_INFO_SHIP = 8542

#
# MessageId: ERROR_DS_DRA_SCHEMA_CONFLICT
#
# MessageText:
#
# The replication operation could not be completed due to a schema incompatibility.
#
ERROR_DS_DRA_SCHEMA_CONFLICT = 8543

#
# MessageId: ERROR_DS_DRA_EARLIER_SCHEMA_CONFLICT
#
# MessageText:
#
# The replication operation could not be completed due to a previous schema incompatibility.
#
ERROR_DS_DRA_EARLIER_SCHEMA_CONFLICT = 8544

#
# MessageId: ERROR_DS_DRA_OBJ_NC_MISMATCH
#
# MessageText:
#
# The replication update could not be applied because either the source or the destination has not yet received information regarding a recent cross-domain move operation.
#
ERROR_DS_DRA_OBJ_NC_MISMATCH = 8545

#
# MessageId: ERROR_DS_NC_STILL_HAS_DSAS
#
# MessageText:
#
# The requested domain could not be deleted because there exist domain controllers that still host this domain.
#
ERROR_DS_NC_STILL_HAS_DSAS = 8546

#
# MessageId: ERROR_DS_GC_REQUIRED
#
# MessageText:
#
# The requested operation can be performed only on a global catalog server.
#
ERROR_DS_GC_REQUIRED = 8547

#
# MessageId: ERROR_DS_LOCAL_MEMBER_OF_LOCAL_ONLY
#
# MessageText:
#
# A local group can only be a member of other local groups in the same domain.
#
ERROR_DS_LOCAL_MEMBER_OF_LOCAL_ONLY = 8548

#
# MessageId: ERROR_DS_NO_FPO_IN_UNIVERSAL_GROUPS
#
# MessageText:
#
# Foreign security principals cannot be members of universal groups.
#
ERROR_DS_NO_FPO_IN_UNIVERSAL_GROUPS = 8549

#
# MessageId: ERROR_DS_CANT_ADD_TO_GC
#
# MessageText:
#
# The attribute is not allowed to be replicated to the GC because of security reasons.
#
ERROR_DS_CANT_ADD_TO_GC = 8550

#
# MessageId: ERROR_DS_NO_CHECKPOINT_WITH_PDC
#
# MessageText:
#
# The checkpoint with the PDC could not be taken because there too many modifications being processed currently.
#
ERROR_DS_NO_CHECKPOINT_WITH_PDC = 8551

#
# MessageId: ERROR_DS_SOURCE_AUDITING_NOT_ENABLED
#
# MessageText:
#
# The operation requires that source domain auditing be enabled.
#
ERROR_DS_SOURCE_AUDITING_NOT_ENABLED = 8552

#
# MessageId: ERROR_DS_CANT_CREATE_IN_NONDOMAIN_NC
#
# MessageText:
#
# Security principal objects can only be created inside domain naming contexts.
#
ERROR_DS_CANT_CREATE_IN_NONDOMAIN_NC = 8553

#
# MessageId: ERROR_DS_INVALID_NAME_FOR_SPN
#
# MessageText:
#
# A Service Principal Name (SPN) could not be constructed because the provided hostname is not in the necessary format.
#
ERROR_DS_INVALID_NAME_FOR_SPN = 8554

#
# MessageId: ERROR_DS_FILTER_USES_CONTRUCTED_ATTRS
#
# MessageText:
#
# A Filter was passed that uses constructed attributes.
#
ERROR_DS_FILTER_USES_CONTRUCTED_ATTRS = 8555

#
# MessageId: ERROR_DS_UNICODEPWD_NOT_IN_QUOTES
#
# MessageText:
#
# The unicodePwd attribute value must be enclosed in double quotes.
#
ERROR_DS_UNICODEPWD_NOT_IN_QUOTES = 8556

#
# MessageId: ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED
#
# MessageText:
#
# Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.
#
ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED = 8557

#
# MessageId: ERROR_DS_MUST_BE_RUN_ON_DST_DC
#
# MessageText:
#
# For security reasons, the operation must be run on the destination DC.
#
ERROR_DS_MUST_BE_RUN_ON_DST_DC = 8558

#
# MessageId: ERROR_DS_SRC_DC_MUST_BE_SP4_OR_GREATER
#
# MessageText:
#
# For security reasons, the source DC must be NT4SP4 or greater.
#
ERROR_DS_SRC_DC_MUST_BE_SP4_OR_GREATER = 8559

#
# MessageId: ERROR_DS_CANT_TREE_DELETE_CRITICAL_OBJ
#
# MessageText:
#
# Critical Directory Service System objects cannot be deleted during tree delete operations. The tree delete may have been partially performed.
#
ERROR_DS_CANT_TREE_DELETE_CRITICAL_OBJ = 8560

#
# MessageId: ERROR_DS_INIT_FAILURE_CONSOLE
#
# MessageText:
#
# Directory Services could not start because of the following error: %1.
# Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.
#
ERROR_DS_INIT_FAILURE_CONSOLE = 8561

#
# MessageId: ERROR_DS_SAM_INIT_FAILURE_CONSOLE
#
# MessageText:
#
# Security Accounts Manager initialization failed because of the following error: %1.
# Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.
#
ERROR_DS_SAM_INIT_FAILURE_CONSOLE = 8562

#
# MessageId: ERROR_DS_FOREST_VERSION_TOO_HIGH
#
# MessageText:
#
# The version of the operating system is incompatible with the current AD DS forest functional level or AD LDS Configuration Set functional level. You must upgrade to a new version of the operating system before this server can become an AD DS Domain Controller or add an AD LDS Instance in this AD DS Forest or AD LDS Configuration Set.
#
ERROR_DS_FOREST_VERSION_TOO_HIGH = 8563

#
# MessageId: ERROR_DS_DOMAIN_VERSION_TOO_HIGH
#
# MessageText:
#
# The version of the operating system installed is incompatible with the current domain functional level. You must upgrade to a new version of the operating system before this server can become a domain controller in this domain.
#
ERROR_DS_DOMAIN_VERSION_TOO_HIGH = 8564

#
# MessageId: ERROR_DS_FOREST_VERSION_TOO_LOW
#
# MessageText:
#
# The version of the operating system installed on this server no longer supports the current AD DS Forest functional level or AD LDS Configuration Set functional level. You must raise the AD DS Forest functional level or AD LDS Configuration Set functional level before this server can become an AD DS Domain Controller or an AD LDS Instance in this Forest or Configuration Set.
#
ERROR_DS_FOREST_VERSION_TOO_LOW = 8565

#
# MessageId: ERROR_DS_DOMAIN_VERSION_TOO_LOW
#
# MessageText:
#
# The version of the operating system installed on this server no longer supports the current domain functional level. You must raise the domain functional level before this server can become a domain controller in this domain.
#
ERROR_DS_DOMAIN_VERSION_TOO_LOW = 8566

#
# MessageId: ERROR_DS_INCOMPATIBLE_VERSION
#
# MessageText:
#
# The version of the operating system installed on this server is incompatible with the functional level of the domain or forest.
#
ERROR_DS_INCOMPATIBLE_VERSION = 8567

#
# MessageId: ERROR_DS_LOW_DSA_VERSION
#
# MessageText:
#
# The functional level of the domain (or forest) cannot be raised to the requested value, because there exist one or more domain controllers in the domain (or forest) that are at a lower incompatible functional level.
#
ERROR_DS_LOW_DSA_VERSION = 8568

#
# MessageId: ERROR_DS_NO_BEHAVIOR_VERSION_IN_MIXEDDOMAIN
#
# MessageText:
#
# The forest functional level cannot be raised to the requested value since one or more domains are still in mixed domain mode. All domains in the forest must be in native mode, for you to raise the forest functional level.
#
ERROR_DS_NO_BEHAVIOR_VERSION_IN_MIXEDDOMAIN = 8569

#
# MessageId: ERROR_DS_NOT_SUPPORTED_SORT_ORDER
#
# MessageText:
#
# The sort order requested is not supported.
#
ERROR_DS_NOT_SUPPORTED_SORT_ORDER = 8570

#
# MessageId: ERROR_DS_NAME_NOT_UNIQUE
#
# MessageText:
#
# The requested name already exists as a unique identifier.
#
ERROR_DS_NAME_NOT_UNIQUE = 8571

#
# MessageId: ERROR_DS_MACHINE_ACCOUNT_CREATED_PRENT4
#
# MessageText:
#
# The machine account was created pre-NT4. The account needs to be recreated.
#
ERROR_DS_MACHINE_ACCOUNT_CREATED_PRENT4 = 8572

#
# MessageId: ERROR_DS_OUT_OF_VERSION_STORE
#
# MessageText:
#
# The database is out of version store.
#
ERROR_DS_OUT_OF_VERSION_STORE = 8573

#
# MessageId: ERROR_DS_INCOMPATIBLE_CONTROLS_USED
#
# MessageText:
#
# Unable to continue operation because multiple conflicting controls were used.
#
ERROR_DS_INCOMPATIBLE_CONTROLS_USED = 8574

#
# MessageId: ERROR_DS_NO_REF_DOMAIN
#
# MessageText:
#
# Unable to find a valid security descriptor reference domain for this partition.
#
ERROR_DS_NO_REF_DOMAIN = 8575

#
# MessageId: ERROR_DS_RESERVED_LINK_ID
#
# MessageText:
#
# Schema update failed: The link identifier is reserved.
#
ERROR_DS_RESERVED_LINK_ID = 8576

#
# MessageId: ERROR_DS_LINK_ID_NOT_AVAILABLE
#
# MessageText:
#
# Schema update failed: There are no link identifiers available.
#
ERROR_DS_LINK_ID_NOT_AVAILABLE = 8577

#
# MessageId: ERROR_DS_AG_CANT_HAVE_UNIVERSAL_MEMBER
#
# MessageText:
#
# An account group cannot have a universal group as a member.
#
ERROR_DS_AG_CANT_HAVE_UNIVERSAL_MEMBER = 8578

#
# MessageId: ERROR_DS_MODIFYDN_DISALLOWED_BY_INSTANCE_TYPE
#
# MessageText:
#
# Rename or move operations on naming context heads or read-only objects are not allowed.
#
ERROR_DS_MODIFYDN_DISALLOWED_BY_INSTANCE_TYPE = 8579

#
# MessageId: ERROR_DS_NO_OBJECT_MOVE_IN_SCHEMA_NC
#
# MessageText:
#
# Move operations on objects in the schema naming context are not allowed.
#
ERROR_DS_NO_OBJECT_MOVE_IN_SCHEMA_NC = 8580

#
# MessageId: ERROR_DS_MODIFYDN_DISALLOWED_BY_FLAG
#
# MessageText:
#
# A system flag has been set on the object and does not allow the object to be moved or renamed.
#
ERROR_DS_MODIFYDN_DISALLOWED_BY_FLAG = 8581

#
# MessageId: ERROR_DS_MODIFYDN_WRONG_GRANDPARENT
#
# MessageText:
#
# This object is not allowed to change its grandparent container. Moves are not forbidden on this object, but are restricted to sibling containers.
#
ERROR_DS_MODIFYDN_WRONG_GRANDPARENT = 8582

#
# MessageId: ERROR_DS_NAME_ERROR_TRUST_REFERRAL
#
# MessageText:
#
# Unable to resolve completely, a referral to another forest is generated.
#
ERROR_DS_NAME_ERROR_TRUST_REFERRAL = 8583

#
# MessageId: ERROR_NOT_SUPPORTED_ON_STANDARD_SERVER
#
# MessageText:
#
# The requested action is not supported on standard server.
#
ERROR_NOT_SUPPORTED_ON_STANDARD_SERVER = 8584

#
# MessageId: ERROR_DS_CANT_ACCESS_REMOTE_PART_OF_AD
#
# MessageText:
#
# Could not access a partition of the directory service located on a remote server. Make sure at least one server is running for the partition in question.
#
ERROR_DS_CANT_ACCESS_REMOTE_PART_OF_AD = 8585

#
# MessageId: ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE_V2
#
# MessageText:
#
# The directory cannot validate the proposed naming context (or partition) name because it does not hold a replica nor can it contact a replica of the naming context above the proposed naming context. Please ensure that the parent naming context is properly registered in DNS, and at least one replica of this naming context is reachable by the Domain Naming master.
#
ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE_V2 = 8586

#
# MessageId: ERROR_DS_THREAD_LIMIT_EXCEEDED
#
# MessageText:
#
# The thread limit for this request was exceeded.
#
ERROR_DS_THREAD_LIMIT_EXCEEDED = 8587

#
# MessageId: ERROR_DS_NOT_CLOSEST
#
# MessageText:
#
# The Global catalog server is not in the closest site.
#
ERROR_DS_NOT_CLOSEST = 8588

#
# MessageId: ERROR_DS_CANT_DERIVE_SPN_WITHOUT_SERVER_REF
#
# MessageText:
#
# The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the corresponding server object in the local DS database has no serverReference attribute.
#
ERROR_DS_CANT_DERIVE_SPN_WITHOUT_SERVER_REF = 8589

#
# MessageId: ERROR_DS_SINGLE_USER_MODE_FAILED
#
# MessageText:
#
# The Directory Service failed to enter single user mode.
#
ERROR_DS_SINGLE_USER_MODE_FAILED = 8590

#
# MessageId: ERROR_DS_NTDSCRIPT_SYNTAX_ERROR
#
# MessageText:
#
# The Directory Service cannot parse the script because of a syntax error.
#
ERROR_DS_NTDSCRIPT_SYNTAX_ERROR = 8591

#
# MessageId: ERROR_DS_NTDSCRIPT_PROCESS_ERROR
#
# MessageText:
#
# The Directory Service cannot process the script because of an error.
#
ERROR_DS_NTDSCRIPT_PROCESS_ERROR = 8592

#
# MessageId: ERROR_DS_DIFFERENT_REPL_EPOCHS
#
# MessageText:
#
# The directory service cannot perform the requested operation because the servers involved are of different replication epochs (which is usually related to a domain rename that is in progress).
#
ERROR_DS_DIFFERENT_REPL_EPOCHS = 8593

#
# MessageId: ERROR_DS_DRS_EXTENSIONS_CHANGED
#
# MessageText:
#
# The directory service binding must be renegotiated due to a change in the server extensions information.
#
ERROR_DS_DRS_EXTENSIONS_CHANGED = 8594

#
# MessageId: ERROR_DS_REPLICA_SET_CHANGE_NOT_ALLOWED_ON_DISABLED_CR
#
# MessageText:
#
# Operation not allowed on a disabled cross ref.
#
ERROR_DS_REPLICA_SET_CHANGE_NOT_ALLOWED_ON_DISABLED_CR = 8595

#
# MessageId: ERROR_DS_NO_MSDS_INTID
#
# MessageText:
#
# Schema update failed: No values for msDS-IntId are available.
#
ERROR_DS_NO_MSDS_INTID = 8596

#
# MessageId: ERROR_DS_DUP_MSDS_INTID
#
# MessageText:
#
# Schema update failed: Duplicate msDS-INtId. Retry the operation.
#
ERROR_DS_DUP_MSDS_INTID = 8597

#
# MessageId: ERROR_DS_EXISTS_IN_RDNATTID
#
# MessageText:
#
# Schema deletion failed: attribute is used in rDNAttID.
#
ERROR_DS_EXISTS_IN_RDNATTID = 8598

#
# MessageId: ERROR_DS_AUTHORIZATION_FAILED
#
# MessageText:
#
# The directory service failed to authorize the request.
#
ERROR_DS_AUTHORIZATION_FAILED = 8599

#
# MessageId: ERROR_DS_INVALID_SCRIPT
#
# MessageText:
#
# The Directory Service cannot process the script because it is invalid.
#
ERROR_DS_INVALID_SCRIPT = 8600

#
# MessageId: ERROR_DS_REMOTE_CROSSREF_OP_FAILED
#
# MessageText:
#
# The remote create cross reference operation failed on the Domain Naming Master FSMO. The operation's error is in the extended data.
#
ERROR_DS_REMOTE_CROSSREF_OP_FAILED = 8601

#
# MessageId: ERROR_DS_CROSS_REF_BUSY
#
# MessageText:
#
# A cross reference is in use locally with the same name.
#
ERROR_DS_CROSS_REF_BUSY = 8602

#
# MessageId: ERROR_DS_CANT_DERIVE_SPN_FOR_DELETED_DOMAIN
#
# MessageText:
#
# The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the server's domain has been deleted from the forest.
#
ERROR_DS_CANT_DERIVE_SPN_FOR_DELETED_DOMAIN = 8603

#
# MessageId: ERROR_DS_CANT_DEMOTE_WITH_WRITEABLE_NC
#
# MessageText:
#
# Writeable NCs prevent this DC from demoting.
#
ERROR_DS_CANT_DEMOTE_WITH_WRITEABLE_NC = 8604

#
# MessageId: ERROR_DS_DUPLICATE_ID_FOUND
#
# MessageText:
#
# The requested object has a non-unique identifier and cannot be retrieved.
#
ERROR_DS_DUPLICATE_ID_FOUND = 8605

#
# MessageId: ERROR_DS_INSUFFICIENT_ATTR_TO_CREATE_OBJECT
#
# MessageText:
#
# Insufficient attributes were given to create an object. This object may not exist because it may have been deleted and already garbage collected.
#
ERROR_DS_INSUFFICIENT_ATTR_TO_CREATE_OBJECT = 8606

#
# MessageId: ERROR_DS_GROUP_CONVERSION_ERROR
#
# MessageText:
#
# The group cannot be converted due to attribute restrictions on the requested group type.
#
ERROR_DS_GROUP_CONVERSION_ERROR = 8607

#
# MessageId: ERROR_DS_CANT_MOVE_APP_BASIC_GROUP
#
# MessageText:
#
# Cross-domain move of non-empty basic application groups is not allowed.
#
ERROR_DS_CANT_MOVE_APP_BASIC_GROUP = 8608

#
# MessageId: ERROR_DS_CANT_MOVE_APP_QUERY_GROUP
#
# MessageText:
#
# Cross-domain move of non-empty query based application groups is not allowed.
#
ERROR_DS_CANT_MOVE_APP_QUERY_GROUP = 8609

#
# MessageId: ERROR_DS_ROLE_NOT_VERIFIED
#
# MessageText:
#
# The FSMO role ownership could not be verified because its directory partition has not replicated successfully with at least one replication partner.
#
ERROR_DS_ROLE_NOT_VERIFIED = 8610

#
# MessageId: ERROR_DS_WKO_CONTAINER_CANNOT_BE_SPECIAL
#
# MessageText:
#
# The target container for a redirection of a well known object container cannot already be a special container.
#
ERROR_DS_WKO_CONTAINER_CANNOT_BE_SPECIAL = 8611

#
# MessageId: ERROR_DS_DOMAIN_RENAME_IN_PROGRESS
#
# MessageText:
#
# The Directory Service cannot perform the requested operation because a domain rename operation is in progress.
#
ERROR_DS_DOMAIN_RENAME_IN_PROGRESS = 8612

#
# MessageId: ERROR_DS_EXISTING_AD_CHILD_NC
#
# MessageText:
#
# The directory service detected a child partition below the requested partition name. The partition hierarchy must be created in a top down method.
#
ERROR_DS_EXISTING_AD_CHILD_NC = 8613

#
# MessageId: ERROR_DS_REPL_LIFETIME_EXCEEDED
#
# MessageText:
#
# The directory service cannot replicate with this server because the time since the last replication with this server has exceeded the tombstone lifetime.
#
ERROR_DS_REPL_LIFETIME_EXCEEDED = 8614

#
# MessageId: ERROR_DS_DISALLOWED_IN_SYSTEM_CONTAINER
#
# MessageText:
#
# The requested operation is not allowed on an object under the system container.
#
ERROR_DS_DISALLOWED_IN_SYSTEM_CONTAINER = 8615

#
# MessageId: ERROR_DS_LDAP_SEND_QUEUE_FULL
#
# MessageText:
#
# The LDAP servers network send queue has filled up because the client is not processing the results of its requests fast enough. No more requests will be processed until the client catches up. If the client does not catch up then it will be disconnected.
#
ERROR_DS_LDAP_SEND_QUEUE_FULL = 8616

#
# MessageId: ERROR_DS_DRA_OUT_SCHEDULE_WINDOW
#
# MessageText:
#
# The scheduled replication did not take place because the system was too busy to execute the request within the schedule window. The replication queue is overloaded. Consider reducing the number of partners or decreasing the scheduled replication frequency.
#
ERROR_DS_DRA_OUT_SCHEDULE_WINDOW = 8617

#
# MessageId: ERROR_DS_POLICY_NOT_KNOWN
#
# MessageText:
#
# At this time, it cannot be determined if the branch replication policy is available on the hub domain controller. Please retry at a later time to account for replication latencies.
#
ERROR_DS_POLICY_NOT_KNOWN = 8618

#
# MessageId: ERROR_NO_SITE_SETTINGS_OBJECT
#
# MessageText:
#
# The site settings object for the specified site does not exist.
#
ERROR_NO_SITE_SETTINGS_OBJECT = 8619

#
# MessageId: ERROR_NO_SECRETS
#
# MessageText:
#
# The local account store does not contain secret material for the specified account.
#
ERROR_NO_SECRETS = 8620

#
# MessageId: ERROR_NO_WRITABLE_DC_FOUND
#
# MessageText:
#
# Could not find a writable domain controller in the domain.
#
ERROR_NO_WRITABLE_DC_FOUND = 8621

#
# MessageId: ERROR_DS_NO_SERVER_OBJECT
#
# MessageText:
#
# The server object for the domain controller does not exist.
#
ERROR_DS_NO_SERVER_OBJECT = 8622

#
# MessageId: ERROR_DS_NO_NTDSA_OBJECT
#
# MessageText:
#
# The NTDS Settings object for the domain controller does not exist.
#
ERROR_DS_NO_NTDSA_OBJECT = 8623

#
# MessageId: ERROR_DS_NON_ASQ_SEARCH
#
# MessageText:
#
# The requested search operation is not supported for ASQ searches.
#
ERROR_DS_NON_ASQ_SEARCH = 8624

#
# MessageId: ERROR_DS_AUDIT_FAILURE
#
# MessageText:
#
# A required audit event could not be generated for the operation.
#
ERROR_DS_AUDIT_FAILURE = 8625

#
# MessageId: ERROR_DS_INVALID_SEARCH_FLAG_SUBTREE
#
# MessageText:
#
# The search flags for the attribute are invalid. The subtree index bit is valid only on single valued attributes.
#
ERROR_DS_INVALID_SEARCH_FLAG_SUBTREE = 8626

#
# MessageId: ERROR_DS_INVALID_SEARCH_FLAG_TUPLE
#
# MessageText:
#
# The search flags for the attribute are invalid. The tuple index bit is valid only on attributes of Unicode strings.
#
ERROR_DS_INVALID_SEARCH_FLAG_TUPLE = 8627

#
# MessageId: ERROR_DS_HIERARCHY_TABLE_TOO_DEEP
#
# MessageText:
#
# The address books are nested too deeply. Failed to build the hierarchy table.
#
ERROR_DS_HIERARCHY_TABLE_TOO_DEEP = 8628

#
# MessageId: ERROR_DS_DRA_CORRUPT_UTD_VECTOR
#
# MessageText:
#
# The specified up-to-date-ness vector is corrupt.
#
ERROR_DS_DRA_CORRUPT_UTD_VECTOR = 8629

#
# MessageId: ERROR_DS_DRA_SECRETS_DENIED
#
# MessageText:
#
# The request to replicate secrets is denied.
#
ERROR_DS_DRA_SECRETS_DENIED = 8630

#
# MessageId: ERROR_DS_RESERVED_MAPI_ID
#
# MessageText:
#
# Schema update failed: The MAPI identifier is reserved.
#
ERROR_DS_RESERVED_MAPI_ID = 8631

#
# MessageId: ERROR_DS_MAPI_ID_NOT_AVAILABLE
#
# MessageText:
#
# Schema update failed: There are no MAPI identifiers available.
#
ERROR_DS_MAPI_ID_NOT_AVAILABLE = 8632

#
# MessageId: ERROR_DS_DRA_MISSING_KRBTGT_SECRET
#
# MessageText:
#
# The replication operation failed because the required attributes of the local krbtgt object are missing.
#
ERROR_DS_DRA_MISSING_KRBTGT_SECRET = 8633

#
# MessageId: ERROR_DS_DOMAIN_NAME_EXISTS_IN_FOREST
#
# MessageText:
#
# The domain name of the trusted domain already exists in the forest.
#
ERROR_DS_DOMAIN_NAME_EXISTS_IN_FOREST = 8634

#
# MessageId: ERROR_DS_FLAT_NAME_EXISTS_IN_FOREST
#
# MessageText:
#
# The flat name of the trusted domain already exists in the forest.
#
ERROR_DS_FLAT_NAME_EXISTS_IN_FOREST = 8635

#
# MessageId: ERROR_INVALID_USER_PRINCIPAL_NAME
#
# MessageText:
#
# The User Principal Name (UPN) is invalid.
#
ERROR_INVALID_USER_PRINCIPAL_NAME = 8636

#
# MessageId: ERROR_DS_OID_MAPPED_GROUP_CANT_HAVE_MEMBERS
#
# MessageText:
#
# OID mapped groups cannot have members.
#
ERROR_DS_OID_MAPPED_GROUP_CANT_HAVE_MEMBERS = 8637

#
# MessageId: ERROR_DS_OID_NOT_FOUND
#
# MessageText:
#
# The specified OID cannot be found.
#
ERROR_DS_OID_NOT_FOUND = 8638

#
# MessageId: ERROR_DS_DRA_RECYCLED_TARGET
#
# MessageText:
#
# The replication operation failed because the target object referred by a link value is recycled.
#
ERROR_DS_DRA_RECYCLED_TARGET = 8639

#
# MessageId: ERROR_DS_DISALLOWED_NC_REDIRECT
#
# MessageText:
#
# The redirect operation failed because the target object is in a NC different from the domain NC of the current domain controller.
#
ERROR_DS_DISALLOWED_NC_REDIRECT = 8640

#
# MessageId: ERROR_DS_HIGH_ADLDS_FFL
#
# MessageText:
#
# The functional level of the AD LDS configuration set cannot be lowered to the requested value.
#
ERROR_DS_HIGH_ADLDS_FFL = 8641

#
# MessageId: ERROR_DS_HIGH_DSA_VERSION
#
# MessageText:
#
# The functional level of the domain (or forest) cannot be lowered to the requested value.
#
ERROR_DS_HIGH_DSA_VERSION = 8642

#
# MessageId: ERROR_DS_LOW_ADLDS_FFL
#
# MessageText:
#
# The functional level of the AD LDS configuration set cannot be raised to the requested value, because there exist one or more ADLDS instances that are at a lower incompatible functional level.
#
ERROR_DS_LOW_ADLDS_FFL = 8643

#
# MessageId: ERROR_DOMAIN_SID_SAME_AS_LOCAL_WORKSTATION
#
# MessageText:
#
# The domain join cannot be completed because the SID of the domain you attempted to join was identical to the SID of this machine. This is a symptom of an improperly cloned operating system install.  You should run sysprep on this machine in order to generate a new machine SID. Please see http://go.microsoft.com/fwlink/?LinkId=168895 for more information.
#
ERROR_DOMAIN_SID_SAME_AS_LOCAL_WORKSTATION = 8644

#
# MessageId: ERROR_DS_UNDELETE_SAM_VALIDATION_FAILED
#
# MessageText:
#
# The undelete operation failed because the Sam Account Name or Additional Sam Account Name of the object being undeleted conflicts with an existing live object.
#
ERROR_DS_UNDELETE_SAM_VALIDATION_FAILED = 8645

#
# MessageId: ERROR_INCORRECT_ACCOUNT_TYPE
#
# MessageText:
#
# The system is not authoritative for the specified account and therefore cannot complete the operation. Please retry the operation using the provider associated with this account. If this is an online provider please use the provider's online site.
#
ERROR_INCORRECT_ACCOUNT_TYPE = 8646

#
# MessageId: ERROR_DS_SPN_VALUE_NOT_UNIQUE_IN_FOREST
#
# MessageText:
#
# The operation failed because SPN value provided for addition/modification is not unique forest-wide.
#
ERROR_DS_SPN_VALUE_NOT_UNIQUE_IN_FOREST = 8647

#
# MessageId: ERROR_DS_UPN_VALUE_NOT_UNIQUE_IN_FOREST
#
# MessageText:
#
# The operation failed because UPN value provided for addition/modification is not unique forest-wide.
#
ERROR_DS_UPN_VALUE_NOT_UNIQUE_IN_FOREST = 8648


#/////////////////////////////////////////////////
#                                                /
#        End of Active Directory Error Codes     /
#                                                /
#                  8000 to  8999                 /
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#               DNS Error codes                 //
#                                               //
#                 9000 to 9999                  //
#/////////////////////////////////////////////////

# =============================
# Facility DNS Error Messages
# =============================

#
#  DNS response codes.
#

DNS_ERROR_RESPONSE_CODES_BASE = 9000

DNS_ERROR_RCODE_NO_ERROR = NO_ERROR

DNS_ERROR_MASK = 0

# DNS_ERROR_RCODE_FORMAT_ERROR          0x00002329
#
# MessageId: DNS_ERROR_RCODE_FORMAT_ERROR
#
# MessageText:
#
# DNS server unable to interpret format.
#
DNS_ERROR_RCODE_FORMAT_ERROR = 9001

# DNS_ERROR_RCODE_SERVER_FAILURE        0x0000232a
#
# MessageId: DNS_ERROR_RCODE_SERVER_FAILURE
#
# MessageText:
#
# DNS server failure.
#
DNS_ERROR_RCODE_SERVER_FAILURE = 9002

# DNS_ERROR_RCODE_NAME_ERROR            0x0000232b
#
# MessageId: DNS_ERROR_RCODE_NAME_ERROR
#
# MessageText:
#
# DNS name does not exist.
#
DNS_ERROR_RCODE_NAME_ERROR = 9003

# DNS_ERROR_RCODE_NOT_IMPLEMENTED       0x0000232c
#
# MessageId: DNS_ERROR_RCODE_NOT_IMPLEMENTED
#
# MessageText:
#
# DNS request not supported by name server.
#
DNS_ERROR_RCODE_NOT_IMPLEMENTED = 9004

# DNS_ERROR_RCODE_REFUSED               0x0000232d
#
# MessageId: DNS_ERROR_RCODE_REFUSED
#
# MessageText:
#
# DNS operation refused.
#
DNS_ERROR_RCODE_REFUSED = 9005

# DNS_ERROR_RCODE_YXDOMAIN              0x0000232e
#
# MessageId: DNS_ERROR_RCODE_YXDOMAIN
#
# MessageText:
#
# DNS name that ought not exist, does exist.
#
DNS_ERROR_RCODE_YXDOMAIN = 9006

# DNS_ERROR_RCODE_YXRRSET               0x0000232f
#
# MessageId: DNS_ERROR_RCODE_YXRRSET
#
# MessageText:
#
# DNS RR set that ought not exist, does exist.
#
DNS_ERROR_RCODE_YXRRSET = 9007

# DNS_ERROR_RCODE_NXRRSET               0x00002330
#
# MessageId: DNS_ERROR_RCODE_NXRRSET
#
# MessageText:
#
# DNS RR set that ought to exist, does not exist.
#
DNS_ERROR_RCODE_NXRRSET = 9008

# DNS_ERROR_RCODE_NOTAUTH               0x00002331
#
# MessageId: DNS_ERROR_RCODE_NOTAUTH
#
# MessageText:
#
# DNS server not authoritative for zone.
#
DNS_ERROR_RCODE_NOTAUTH = 9009

# DNS_ERROR_RCODE_NOTZONE               0x00002332
#
# MessageId: DNS_ERROR_RCODE_NOTZONE
#
# MessageText:
#
# DNS name in update or prereq is not in zone.
#
DNS_ERROR_RCODE_NOTZONE = 9010

# DNS_ERROR_RCODE_BADSIG                0x00002338
#
# MessageId: DNS_ERROR_RCODE_BADSIG
#
# MessageText:
#
# DNS signature failed to verify.
#
DNS_ERROR_RCODE_BADSIG = 9016

# DNS_ERROR_RCODE_BADKEY                0x00002339
#
# MessageId: DNS_ERROR_RCODE_BADKEY
#
# MessageText:
#
# DNS bad key.
#
DNS_ERROR_RCODE_BADKEY = 9017

# DNS_ERROR_RCODE_BADTIME               0x0000233a
#
# MessageId: DNS_ERROR_RCODE_BADTIME
#
# MessageText:
#
# DNS signature validity expired.
#
DNS_ERROR_RCODE_BADTIME = 9018

DNS_ERROR_RCODE_LAST = DNS_ERROR_RCODE_BADTIME


#
# DNSSEC errors
#

DNS_ERROR_DNSSEC_BASE = 9100

#
# MessageId: DNS_ERROR_KEYMASTER_REQUIRED
#
# MessageText:
#
# Only the DNS server acting as the key master for the zone may perform this operation.
#
DNS_ERROR_KEYMASTER_REQUIRED = 9101

#
# MessageId: DNS_ERROR_NOT_ALLOWED_ON_SIGNED_ZONE
#
# MessageText:
#
# This operation is not allowed on a zone that is signed or has signing keys.
#
DNS_ERROR_NOT_ALLOWED_ON_SIGNED_ZONE = 9102

#
# MessageId: DNS_ERROR_NSEC3_INCOMPATIBLE_WITH_RSA_SHA1
#
# MessageText:
#
# NSEC3 is not compatible with the RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC.
#
DNS_ERROR_NSEC3_INCOMPATIBLE_WITH_RSA_SHA1 = 9103

#
# MessageId: DNS_ERROR_NOT_ENOUGH_SIGNING_KEY_DESCRIPTORS
#
# MessageText:
#
# The zone does not have enough signing keys. There must be at least one key signing key (KSK) and at least one zone signing key (ZSK).
#
DNS_ERROR_NOT_ENOUGH_SIGNING_KEY_DESCRIPTORS = 9104

#
# MessageId: DNS_ERROR_UNSUPPORTED_ALGORITHM
#
# MessageText:
#
# The specified algorithm is not supported.
#
DNS_ERROR_UNSUPPORTED_ALGORITHM = 9105

#
# MessageId: DNS_ERROR_INVALID_KEY_SIZE
#
# MessageText:
#
# The specified key size is not supported.
#
DNS_ERROR_INVALID_KEY_SIZE = 9106

#
# MessageId: DNS_ERROR_SIGNING_KEY_NOT_ACCESSIBLE
#
# MessageText:
#
# One or more of the signing keys for a zone are not accessible to the DNS server. Zone signing will not be operational until this error is resolved.
#
DNS_ERROR_SIGNING_KEY_NOT_ACCESSIBLE = 9107

#
# MessageId: DNS_ERROR_KSP_DOES_NOT_SUPPORT_PROTECTION
#
# MessageText:
#
# The specified key storage provider does not support DPAPI++ data protection. Zone signing will not be operational until this error is resolved.
#
DNS_ERROR_KSP_DOES_NOT_SUPPORT_PROTECTION = 9108

#
# MessageId: DNS_ERROR_UNEXPECTED_DATA_PROTECTION_ERROR
#
# MessageText:
#
# An unexpected DPAPI++ error was encountered. Zone signing will not be operational until this error is resolved.
#
DNS_ERROR_UNEXPECTED_DATA_PROTECTION_ERROR = 9109

#
# MessageId: DNS_ERROR_UNEXPECTED_CNG_ERROR
#
# MessageText:
#
# An unexpected crypto error was encountered. Zone signing may not be operational until this error is resolved.
#
DNS_ERROR_UNEXPECTED_CNG_ERROR = 9110

#
# MessageId: DNS_ERROR_UNKNOWN_SIGNING_PARAMETER_VERSION
#
# MessageText:
#
# The DNS server encountered a signing key with an unknown version. Zone signing will not be operational until this error is resolved.
#
DNS_ERROR_UNKNOWN_SIGNING_PARAMETER_VERSION = 9111

#
# MessageId: DNS_ERROR_KSP_NOT_ACCESSIBLE
#
# MessageText:
#
# The specified key service provider cannot be opened by the DNS server.
#
DNS_ERROR_KSP_NOT_ACCESSIBLE = 9112

#
# MessageId: DNS_ERROR_TOO_MANY_SKDS
#
# MessageText:
#
# The DNS server cannot accept any more signing keys with the specified algorithm and KSK flag value for this zone.
#
DNS_ERROR_TOO_MANY_SKDS = 9113

#
# MessageId: DNS_ERROR_INVALID_ROLLOVER_PERIOD
#
# MessageText:
#
# The specified rollover period is invalid.
#
DNS_ERROR_INVALID_ROLLOVER_PERIOD = 9114

#
# MessageId: DNS_ERROR_INVALID_INITIAL_ROLLOVER_OFFSET
#
# MessageText:
#
# The specified initial rollover offset is invalid.
#
DNS_ERROR_INVALID_INITIAL_ROLLOVER_OFFSET = 9115

#
# MessageId: DNS_ERROR_ROLLOVER_IN_PROGRESS
#
# MessageText:
#
# The specified signing key is already in process of rolling over keys.
#
DNS_ERROR_ROLLOVER_IN_PROGRESS = 9116

#
# MessageId: DNS_ERROR_STANDBY_KEY_NOT_PRESENT
#
# MessageText:
#
# The specified signing key does not have a standby key to revoke.
#
DNS_ERROR_STANDBY_KEY_NOT_PRESENT = 9117

#
# MessageId: DNS_ERROR_NOT_ALLOWED_ON_ZSK
#
# MessageText:
#
# This operation is not allowed on a zone signing key (ZSK).
#
DNS_ERROR_NOT_ALLOWED_ON_ZSK = 9118

#
# MessageId: DNS_ERROR_NOT_ALLOWED_ON_ACTIVE_SKD
#
# MessageText:
#
# This operation is not allowed on an active signing key.
#
DNS_ERROR_NOT_ALLOWED_ON_ACTIVE_SKD = 9119

#
# MessageId: DNS_ERROR_ROLLOVER_ALREADY_QUEUED
#
# MessageText:
#
# The specified signing key is already queued for rollover.
#
DNS_ERROR_ROLLOVER_ALREADY_QUEUED = 9120

#
# MessageId: DNS_ERROR_NOT_ALLOWED_ON_UNSIGNED_ZONE
#
# MessageText:
#
# This operation is not allowed on an unsigned zone.
#
DNS_ERROR_NOT_ALLOWED_ON_UNSIGNED_ZONE = 9121

#
# MessageId: DNS_ERROR_BAD_KEYMASTER
#
# MessageText:
#
# This operation could not be completed because the DNS server listed as the current key master for this zone is down or misconfigured. Resolve the problem on the current key master for this zone or use another DNS server to seize the key master role.
#
DNS_ERROR_BAD_KEYMASTER = 9122

#
# MessageId: DNS_ERROR_INVALID_SIGNATURE_VALIDITY_PERIOD
#
# MessageText:
#
# The specified signature validity period is invalid.
#
DNS_ERROR_INVALID_SIGNATURE_VALIDITY_PERIOD = 9123

#
# MessageId: DNS_ERROR_INVALID_NSEC3_ITERATION_COUNT
#
# MessageText:
#
# The specified NSEC3 iteration count is higher than allowed by the minimum key length used in the zone.
#
DNS_ERROR_INVALID_NSEC3_ITERATION_COUNT = 9124

#
# MessageId: DNS_ERROR_DNSSEC_IS_DISABLED
#
# MessageText:
#
# This operation could not be completed because the DNS server has been configured with DNSSEC features disabled. Enable DNSSEC on the DNS server.
#
DNS_ERROR_DNSSEC_IS_DISABLED = 9125

#
# MessageId: DNS_ERROR_INVALID_XML
#
# MessageText:
#
# This operation could not be completed because the XML stream received is empty or syntactically invalid.
#
DNS_ERROR_INVALID_XML = 9126

#
# MessageId: DNS_ERROR_NO_VALID_TRUST_ANCHORS
#
# MessageText:
#
# This operation completed, but no trust anchors were added because all of the trust anchors received were either invalid, unsupported, expired, or would not become valid in less than 30 days.
#
DNS_ERROR_NO_VALID_TRUST_ANCHORS = 9127

#
# MessageId: DNS_ERROR_ROLLOVER_NOT_POKEABLE
#
# MessageText:
#
# The specified signing key is not waiting for parental DS update.
#
DNS_ERROR_ROLLOVER_NOT_POKEABLE = 9128

#
# MessageId: DNS_ERROR_NSEC3_NAME_COLLISION
#
# MessageText:
#
# Hash collision detected during NSEC3 signing. Specify a different user-provided salt, or use a randomly generated salt, and attempt to sign the zone again.
#
DNS_ERROR_NSEC3_NAME_COLLISION = 9129

#
# MessageId: DNS_ERROR_NSEC_INCOMPATIBLE_WITH_NSEC3_RSA_SHA1
#
# MessageText:
#
# NSEC is not compatible with the NSEC3-RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC3.
#
DNS_ERROR_NSEC_INCOMPATIBLE_WITH_NSEC3_RSA_SHA1 = 9130


#
# Packet format
#

DNS_ERROR_PACKET_FMT_BASE = 9500

# DNS_INFO_NO_RECORDS                   0x0000251d
#
# MessageId: DNS_INFO_NO_RECORDS
#
# MessageText:
#
# No records found for given DNS query.
#
DNS_INFO_NO_RECORDS = 9501

# DNS_ERROR_BAD_PACKET                  0x0000251e
#
# MessageId: DNS_ERROR_BAD_PACKET
#
# MessageText:
#
# Bad DNS packet.
#
DNS_ERROR_BAD_PACKET = 9502

# DNS_ERROR_NO_PACKET                   0x0000251f
#
# MessageId: DNS_ERROR_NO_PACKET
#
# MessageText:
#
# No DNS packet.
#
DNS_ERROR_NO_PACKET = 9503

# DNS_ERROR_RCODE                       0x00002520
#
# MessageId: DNS_ERROR_RCODE
#
# MessageText:
#
# DNS error, check rcode.
#
DNS_ERROR_RCODE = 9504

# DNS_ERROR_UNSECURE_PACKET             0x00002521
#
# MessageId: DNS_ERROR_UNSECURE_PACKET
#
# MessageText:
#
# Unsecured DNS packet.
#
DNS_ERROR_UNSECURE_PACKET = 9505

DNS_STATUS_PACKET_UNSECURE = DNS_ERROR_UNSECURE_PACKET

# DNS_REQUEST_PENDING                     0x00002522
#
# MessageId: DNS_REQUEST_PENDING
#
# MessageText:
#
# DNS query request is pending.
#
DNS_REQUEST_PENDING = 9506


#
# General API errors
#

DNS_ERROR_NO_MEMORY =            ERROR_OUTOFMEMORY
DNS_ERROR_INVALID_NAME =         ERROR_INVALID_NAME
DNS_ERROR_INVALID_DATA =         ERROR_INVALID_DATA

DNS_ERROR_GENERAL_API_BASE = 9550

# DNS_ERROR_INVALID_TYPE                0x0000254f
#
# MessageId: DNS_ERROR_INVALID_TYPE
#
# MessageText:
#
# Invalid DNS type.
#
DNS_ERROR_INVALID_TYPE = 9551

# DNS_ERROR_INVALID_IP_ADDRESS          0x00002550
#
# MessageId: DNS_ERROR_INVALID_IP_ADDRESS
#
# MessageText:
#
# Invalid IP address.
#
DNS_ERROR_INVALID_IP_ADDRESS = 9552

# DNS_ERROR_INVALID_PROPERTY            0x00002551
#
# MessageId: DNS_ERROR_INVALID_PROPERTY
#
# MessageText:
#
# Invalid property.
#
DNS_ERROR_INVALID_PROPERTY = 9553

# DNS_ERROR_TRY_AGAIN_LATER             0x00002552
#
# MessageId: DNS_ERROR_TRY_AGAIN_LATER
#
# MessageText:
#
# Try DNS operation again later.
#
DNS_ERROR_TRY_AGAIN_LATER = 9554

# DNS_ERROR_NOT_UNIQUE                  0x00002553
#
# MessageId: DNS_ERROR_NOT_UNIQUE
#
# MessageText:
#
# Record for given name and type is not unique.
#
DNS_ERROR_NOT_UNIQUE = 9555

# DNS_ERROR_NON_RFC_NAME                0x00002554
#
# MessageId: DNS_ERROR_NON_RFC_NAME
#
# MessageText:
#
# DNS name does not comply with RFC specifications.
#
DNS_ERROR_NON_RFC_NAME = 9556

# DNS_STATUS_FQDN                       0x00002555
#
# MessageId: DNS_STATUS_FQDN
#
# MessageText:
#
# DNS name is a fully-qualified DNS name.
#
DNS_STATUS_FQDN = 9557

# DNS_STATUS_DOTTED_NAME                0x00002556
#
# MessageId: DNS_STATUS_DOTTED_NAME
#
# MessageText:
#
# DNS name is dotted (multi-label).
#
DNS_STATUS_DOTTED_NAME = 9558

# DNS_STATUS_SINGLE_PART_NAME           0x00002557
#
# MessageId: DNS_STATUS_SINGLE_PART_NAME
#
# MessageText:
#
# DNS name is a single-part name.
#
DNS_STATUS_SINGLE_PART_NAME = 9559

# DNS_ERROR_INVALID_NAME_CHAR           0x00002558
#
# MessageId: DNS_ERROR_INVALID_NAME_CHAR
#
# MessageText:
#
# DNS name contains an invalid character.
#
DNS_ERROR_INVALID_NAME_CHAR = 9560

# DNS_ERROR_NUMERIC_NAME                0x00002559
#
# MessageId: DNS_ERROR_NUMERIC_NAME
#
# MessageText:
#
# DNS name is entirely numeric.
#
DNS_ERROR_NUMERIC_NAME = 9561

# DNS_ERROR_NOT_ALLOWED_ON_ROOT_SERVER  0x0000255A
#
# MessageId: DNS_ERROR_NOT_ALLOWED_ON_ROOT_SERVER
#
# MessageText:
#
# The operation requested is not permitted on a DNS root server.
#
DNS_ERROR_NOT_ALLOWED_ON_ROOT_SERVER = 9562

# DNS_ERROR_NOT_ALLOWED_UNDER_DELEGATION  0x0000255B
#
# MessageId: DNS_ERROR_NOT_ALLOWED_UNDER_DELEGATION
#
# MessageText:
#
# The record could not be created because this part of the DNS namespace has been delegated to another server.
#
DNS_ERROR_NOT_ALLOWED_UNDER_DELEGATION = 9563

# DNS_ERROR_CANNOT_FIND_ROOT_HINTS  0x0000255C
#
# MessageId: DNS_ERROR_CANNOT_FIND_ROOT_HINTS
#
# MessageText:
#
# The DNS server could not find a set of root hints.
#
DNS_ERROR_CANNOT_FIND_ROOT_HINTS = 9564

# DNS_ERROR_INCONSISTENT_ROOT_HINTS  0x0000255D
#
# MessageId: DNS_ERROR_INCONSISTENT_ROOT_HINTS
#
# MessageText:
#
# The DNS server found root hints but they were not consistent across all adapters.
#
DNS_ERROR_INCONSISTENT_ROOT_HINTS = 9565

# DNS_ERROR_DWORD_VALUE_TOO_SMALL    0x0000255E
#
# MessageId: DNS_ERROR_DWORD_VALUE_TOO_SMALL
#
# MessageText:
#
# The specified value is too small for this parameter.
#
DNS_ERROR_DWORD_VALUE_TOO_SMALL = 9566

# DNS_ERROR_DWORD_VALUE_TOO_LARGE    0x0000255F
#
# MessageId: DNS_ERROR_DWORD_VALUE_TOO_LARGE
#
# MessageText:
#
# The specified value is too large for this parameter.
#
DNS_ERROR_DWORD_VALUE_TOO_LARGE = 9567

# DNS_ERROR_BACKGROUND_LOADING       0x00002560
#
# MessageId: DNS_ERROR_BACKGROUND_LOADING
#
# MessageText:
#
# This operation is not allowed while the DNS server is loading zones in the background. Please try again later.
#
DNS_ERROR_BACKGROUND_LOADING = 9568

# DNS_ERROR_NOT_ALLOWED_ON_RODC      0x00002561
#
# MessageId: DNS_ERROR_NOT_ALLOWED_ON_RODC
#
# MessageText:
#
# The operation requested is not permitted on against a DNS server running on a read-only DC.
#
DNS_ERROR_NOT_ALLOWED_ON_RODC = 9569

# DNS_ERROR_NOT_ALLOWED_UNDER_DNAME   0x00002562
#
# MessageId: DNS_ERROR_NOT_ALLOWED_UNDER_DNAME
#
# MessageText:
#
# No data is allowed to exist underneath a DNAME record.
#
DNS_ERROR_NOT_ALLOWED_UNDER_DNAME = 9570

# DNS_ERROR_DELEGATION_REQUIRED       0x00002563
#
# MessageId: DNS_ERROR_DELEGATION_REQUIRED
#
# MessageText:
#
# This operation requires credentials delegation.
#
DNS_ERROR_DELEGATION_REQUIRED = 9571

# DNS_ERROR_INVALID_POLICY_TABLE        0x00002564
#
# MessageId: DNS_ERROR_INVALID_POLICY_TABLE
#
# MessageText:
#
# Name resolution policy table has been corrupted. DNS resolution will fail until it is fixed. Contact your network administrator.
#
DNS_ERROR_INVALID_POLICY_TABLE = 9572


#
# Zone errors
#

DNS_ERROR_ZONE_BASE = 9600

# DNS_ERROR_ZONE_DOES_NOT_EXIST         0x00002581
#
# MessageId: DNS_ERROR_ZONE_DOES_NOT_EXIST
#
# MessageText:
#
# DNS zone does not exist.
#
DNS_ERROR_ZONE_DOES_NOT_EXIST = 9601

# DNS_ERROR_NO_ZONE_INFO                0x00002582
#
# MessageId: DNS_ERROR_NO_ZONE_INFO
#
# MessageText:
#
# DNS zone information not available.
#
DNS_ERROR_NO_ZONE_INFO = 9602

# DNS_ERROR_INVALID_ZONE_OPERATION      0x00002583
#
# MessageId: DNS_ERROR_INVALID_ZONE_OPERATION
#
# MessageText:
#
# Invalid operation for DNS zone.
#
DNS_ERROR_INVALID_ZONE_OPERATION = 9603

# DNS_ERROR_ZONE_CONFIGURATION_ERROR    0x00002584
#
# MessageId: DNS_ERROR_ZONE_CONFIGURATION_ERROR
#
# MessageText:
#
# Invalid DNS zone configuration.
#
DNS_ERROR_ZONE_CONFIGURATION_ERROR = 9604

# DNS_ERROR_ZONE_HAS_NO_SOA_RECORD      0x00002585
#
# MessageId: DNS_ERROR_ZONE_HAS_NO_SOA_RECORD
#
# MessageText:
#
# DNS zone has no start of authority (SOA) record.
#
DNS_ERROR_ZONE_HAS_NO_SOA_RECORD = 9605

# DNS_ERROR_ZONE_HAS_NO_NS_RECORDS      0x00002586
#
# MessageId: DNS_ERROR_ZONE_HAS_NO_NS_RECORDS
#
# MessageText:
#
# DNS zone has no Name Server (NS) record.
#
DNS_ERROR_ZONE_HAS_NO_NS_RECORDS = 9606

# DNS_ERROR_ZONE_LOCKED                 0x00002587
#
# MessageId: DNS_ERROR_ZONE_LOCKED
#
# MessageText:
#
# DNS zone is locked.
#
DNS_ERROR_ZONE_LOCKED = 9607

# DNS_ERROR_ZONE_CREATION_FAILED        0x00002588
#
# MessageId: DNS_ERROR_ZONE_CREATION_FAILED
#
# MessageText:
#
# DNS zone creation failed.
#
DNS_ERROR_ZONE_CREATION_FAILED = 9608

# DNS_ERROR_ZONE_ALREADY_EXISTS         0x00002589
#
# MessageId: DNS_ERROR_ZONE_ALREADY_EXISTS
#
# MessageText:
#
# DNS zone already exists.
#
DNS_ERROR_ZONE_ALREADY_EXISTS = 9609

# DNS_ERROR_AUTOZONE_ALREADY_EXISTS     0x0000258a
#
# MessageId: DNS_ERROR_AUTOZONE_ALREADY_EXISTS
#
# MessageText:
#
# DNS automatic zone already exists.
#
DNS_ERROR_AUTOZONE_ALREADY_EXISTS = 9610

# DNS_ERROR_INVALID_ZONE_TYPE           0x0000258b
#
# MessageId: DNS_ERROR_INVALID_ZONE_TYPE
#
# MessageText:
#
# Invalid DNS zone type.
#
DNS_ERROR_INVALID_ZONE_TYPE = 9611

# DNS_ERROR_SECONDARY_REQUIRES_MASTER_IP 0x0000258c
#
# MessageId: DNS_ERROR_SECONDARY_REQUIRES_MASTER_IP
#
# MessageText:
#
# Secondary DNS zone requires master IP address.
#
DNS_ERROR_SECONDARY_REQUIRES_MASTER_IP = 9612

# DNS_ERROR_ZONE_NOT_SECONDARY          0x0000258d
#
# MessageId: DNS_ERROR_ZONE_NOT_SECONDARY
#
# MessageText:
#
# DNS zone not secondary.
#
DNS_ERROR_ZONE_NOT_SECONDARY = 9613

# DNS_ERROR_NEED_SECONDARY_ADDRESSES    0x0000258e
#
# MessageId: DNS_ERROR_NEED_SECONDARY_ADDRESSES
#
# MessageText:
#
# Need secondary IP address.
#
DNS_ERROR_NEED_SECONDARY_ADDRESSES = 9614

# DNS_ERROR_WINS_INIT_FAILED            0x0000258f
#
# MessageId: DNS_ERROR_WINS_INIT_FAILED
#
# MessageText:
#
# WINS initialization failed.
#
DNS_ERROR_WINS_INIT_FAILED = 9615

# DNS_ERROR_NEED_WINS_SERVERS           0x00002590
#
# MessageId: DNS_ERROR_NEED_WINS_SERVERS
#
# MessageText:
#
# Need WINS servers.
#
DNS_ERROR_NEED_WINS_SERVERS = 9616

# DNS_ERROR_NBSTAT_INIT_FAILED          0x00002591
#
# MessageId: DNS_ERROR_NBSTAT_INIT_FAILED
#
# MessageText:
#
# NBTSTAT initialization call failed.
#
DNS_ERROR_NBSTAT_INIT_FAILED = 9617

# DNS_ERROR_SOA_DELETE_INVALID          0x00002592
#
# MessageId: DNS_ERROR_SOA_DELETE_INVALID
#
# MessageText:
#
# Invalid delete of start of authority (SOA)
#
DNS_ERROR_SOA_DELETE_INVALID = 9618

# DNS_ERROR_FORWARDER_ALREADY_EXISTS    0x00002593
#
# MessageId: DNS_ERROR_FORWARDER_ALREADY_EXISTS
#
# MessageText:
#
# A conditional forwarding zone already exists for that name.
#
DNS_ERROR_FORWARDER_ALREADY_EXISTS = 9619

# DNS_ERROR_ZONE_REQUIRES_MASTER_IP     0x00002594
#
# MessageId: DNS_ERROR_ZONE_REQUIRES_MASTER_IP
#
# MessageText:
#
# This zone must be configured with one or more master DNS server IP addresses.
#
DNS_ERROR_ZONE_REQUIRES_MASTER_IP = 9620

# DNS_ERROR_ZONE_IS_SHUTDOWN            0x00002595
#
# MessageId: DNS_ERROR_ZONE_IS_SHUTDOWN
#
# MessageText:
#
# The operation cannot be performed because this zone is shut down.
#
DNS_ERROR_ZONE_IS_SHUTDOWN = 9621

# DNS_ERROR_ZONE_LOCKED_FOR_SIGNING     0x00002596
#
# MessageId: DNS_ERROR_ZONE_LOCKED_FOR_SIGNING
#
# MessageText:
#
# This operation cannot be performed because the zone is currently being signed. Please try again later.
#
DNS_ERROR_ZONE_LOCKED_FOR_SIGNING = 9622


#
# Datafile errors
#

DNS_ERROR_DATAFILE_BASE = 9650

# DNS                                   0x000025b3
#
# MessageId: DNS_ERROR_PRIMARY_REQUIRES_DATAFILE
#
# MessageText:
#
# Primary DNS zone requires datafile.
#
DNS_ERROR_PRIMARY_REQUIRES_DATAFILE = 9651

# DNS                                   0x000025b4
#
# MessageId: DNS_ERROR_INVALID_DATAFILE_NAME
#
# MessageText:
#
# Invalid datafile name for DNS zone.
#
DNS_ERROR_INVALID_DATAFILE_NAME = 9652

# DNS                                   0x000025b5
#
# MessageId: DNS_ERROR_DATAFILE_OPEN_FAILURE
#
# MessageText:
#
# Failed to open datafile for DNS zone.
#
DNS_ERROR_DATAFILE_OPEN_FAILURE = 9653

# DNS                                   0x000025b6
#
# MessageId: DNS_ERROR_FILE_WRITEBACK_FAILED
#
# MessageText:
#
# Failed to write datafile for DNS zone.
#
DNS_ERROR_FILE_WRITEBACK_FAILED = 9654

# DNS                                   0x000025b7
#
# MessageId: DNS_ERROR_DATAFILE_PARSING
#
# MessageText:
#
# Failure while reading datafile for DNS zone.
#
DNS_ERROR_DATAFILE_PARSING = 9655


#
# Database errors
#

DNS_ERROR_DATABASE_BASE = 9700

# DNS_ERROR_RECORD_DOES_NOT_EXIST       0x000025e5
#
# MessageId: DNS_ERROR_RECORD_DOES_NOT_EXIST
#
# MessageText:
#
# DNS record does not exist.
#
DNS_ERROR_RECORD_DOES_NOT_EXIST = 9701

# DNS_ERROR_RECORD_FORMAT               0x000025e6
#
# MessageId: DNS_ERROR_RECORD_FORMAT
#
# MessageText:
#
# DNS record format error.
#
DNS_ERROR_RECORD_FORMAT = 9702

# DNS_ERROR_NODE_CREATION_FAILED        0x000025e7
#
# MessageId: DNS_ERROR_NODE_CREATION_FAILED
#
# MessageText:
#
# Node creation failure in DNS.
#
DNS_ERROR_NODE_CREATION_FAILED = 9703

# DNS_ERROR_UNKNOWN_RECORD_TYPE         0x000025e8
#
# MessageId: DNS_ERROR_UNKNOWN_RECORD_TYPE
#
# MessageText:
#
# Unknown DNS record type.
#
DNS_ERROR_UNKNOWN_RECORD_TYPE = 9704

# DNS_ERROR_RECORD_TIMED_OUT            0x000025e9
#
# MessageId: DNS_ERROR_RECORD_TIMED_OUT
#
# MessageText:
#
# DNS record timed out.
#
DNS_ERROR_RECORD_TIMED_OUT = 9705

# DNS_ERROR_NAME_NOT_IN_ZONE            0x000025ea
#
# MessageId: DNS_ERROR_NAME_NOT_IN_ZONE
#
# MessageText:
#
# Name not in DNS zone.
#
DNS_ERROR_NAME_NOT_IN_ZONE = 9706

# DNS_ERROR_CNAME_LOOP                  0x000025eb
#
# MessageId: DNS_ERROR_CNAME_LOOP
#
# MessageText:
#
# CNAME loop detected.
#
DNS_ERROR_CNAME_LOOP = 9707

# DNS_ERROR_NODE_IS_CNAME               0x000025ec
#
# MessageId: DNS_ERROR_NODE_IS_CNAME
#
# MessageText:
#
# Node is a CNAME DNS record.
#
DNS_ERROR_NODE_IS_CNAME = 9708

# DNS_ERROR_CNAME_COLLISION             0x000025ed
#
# MessageId: DNS_ERROR_CNAME_COLLISION
#
# MessageText:
#
# A CNAME record already exists for given name.
#
DNS_ERROR_CNAME_COLLISION = 9709

# DNS_ERROR_RECORD_ONLY_AT_ZONE_ROOT    0x000025ee
#
# MessageId: DNS_ERROR_RECORD_ONLY_AT_ZONE_ROOT
#
# MessageText:
#
# Record only at DNS zone root.
#
DNS_ERROR_RECORD_ONLY_AT_ZONE_ROOT = 9710

# DNS_ERROR_RECORD_ALREADY_EXISTS       0x000025ef
#
# MessageId: DNS_ERROR_RECORD_ALREADY_EXISTS
#
# MessageText:
#
# DNS record already exists.
#
DNS_ERROR_RECORD_ALREADY_EXISTS = 9711

# DNS_ERROR_SECONDARY_DATA              0x000025f0
#
# MessageId: DNS_ERROR_SECONDARY_DATA
#
# MessageText:
#
# Secondary DNS zone data error.
#
DNS_ERROR_SECONDARY_DATA = 9712

# DNS_ERROR_NO_CREATE_CACHE_DATA        0x000025f1
#
# MessageId: DNS_ERROR_NO_CREATE_CACHE_DATA
#
# MessageText:
#
# Could not create DNS cache data.
#
DNS_ERROR_NO_CREATE_CACHE_DATA = 9713

# DNS_ERROR_NAME_DOES_NOT_EXIST         0x000025f2
#
# MessageId: DNS_ERROR_NAME_DOES_NOT_EXIST
#
# MessageText:
#
# DNS name does not exist.
#
DNS_ERROR_NAME_DOES_NOT_EXIST = 9714

# DNS_WARNING_PTR_CREATE_FAILED         0x000025f3
#
# MessageId: DNS_WARNING_PTR_CREATE_FAILED
#
# MessageText:
#
# Could not create pointer (PTR) record.
#
DNS_WARNING_PTR_CREATE_FAILED = 9715

# DNS_WARNING_DOMAIN_UNDELETED          0x000025f4
#
# MessageId: DNS_WARNING_DOMAIN_UNDELETED
#
# MessageText:
#
# DNS domain was undeleted.
#
DNS_WARNING_DOMAIN_UNDELETED = 9716

# DNS_ERROR_DS_UNAVAILABLE              0x000025f5
#
# MessageId: DNS_ERROR_DS_UNAVAILABLE
#
# MessageText:
#
# The directory service is unavailable.
#
DNS_ERROR_DS_UNAVAILABLE = 9717

# DNS_ERROR_DS_ZONE_ALREADY_EXISTS      0x000025f6
#
# MessageId: DNS_ERROR_DS_ZONE_ALREADY_EXISTS
#
# MessageText:
#
# DNS zone already exists in the directory service.
#
DNS_ERROR_DS_ZONE_ALREADY_EXISTS = 9718

# DNS_ERROR_NO_BOOTFILE_IF_DS_ZONE      0x000025f7
#
# MessageId: DNS_ERROR_NO_BOOTFILE_IF_DS_ZONE
#
# MessageText:
#
# DNS server not creating or reading the boot file for the directory service integrated DNS zone.
#
DNS_ERROR_NO_BOOTFILE_IF_DS_ZONE = 9719

# DNS_ERROR_NODE_IS_DNAME               0x000025f8
#
# MessageId: DNS_ERROR_NODE_IS_DNAME
#
# MessageText:
#
# Node is a DNAME DNS record.
#
DNS_ERROR_NODE_IS_DNAME = 9720

# DNS_ERROR_DNAME_COLLISION             0x000025f9
#
# MessageId: DNS_ERROR_DNAME_COLLISION
#
# MessageText:
#
# A DNAME record already exists for given name.
#
DNS_ERROR_DNAME_COLLISION = 9721

# DNS_ERROR_ALIAS_LOOP                  0x000025fa
#
# MessageId: DNS_ERROR_ALIAS_LOOP
#
# MessageText:
#
# An alias loop has been detected with either CNAME or DNAME records.
#
DNS_ERROR_ALIAS_LOOP = 9722


#
# Operation errors
#

DNS_ERROR_OPERATION_BASE = 9750

# DNS_INFO_AXFR_COMPLETE                0x00002617
#
# MessageId: DNS_INFO_AXFR_COMPLETE
#
# MessageText:
#
# DNS AXFR (zone transfer) complete.
#
DNS_INFO_AXFR_COMPLETE = 9751

# DNS_ERROR_AXFR                        0x00002618
#
# MessageId: DNS_ERROR_AXFR
#
# MessageText:
#
# DNS zone transfer failed.
#
DNS_ERROR_AXFR = 9752

# DNS_INFO_ADDED_LOCAL_WINS             0x00002619
#
# MessageId: DNS_INFO_ADDED_LOCAL_WINS
#
# MessageText:
#
# Added local WINS server.
#
DNS_INFO_ADDED_LOCAL_WINS = 9753


#
# Secure update
#

DNS_ERROR_SECURE_BASE = 9800

# DNS_STATUS_CONTINUE_NEEDED            0x00002649
#
# MessageId: DNS_STATUS_CONTINUE_NEEDED
#
# MessageText:
#
# Secure update call needs to continue update request.
#
DNS_STATUS_CONTINUE_NEEDED = 9801


#
# Setup errors
#

DNS_ERROR_SETUP_BASE = 9850

# DNS_ERROR_NO_TCPIP                    0x0000267b
#
# MessageId: DNS_ERROR_NO_TCPIP
#
# MessageText:
#
# TCP/IP network protocol not installed.
#
DNS_ERROR_NO_TCPIP = 9851

# DNS_ERROR_NO_DNS_SERVERS              0x0000267c
#
# MessageId: DNS_ERROR_NO_DNS_SERVERS
#
# MessageText:
#
# No DNS servers configured for local system.
#
DNS_ERROR_NO_DNS_SERVERS = 9852


#
# Directory partition (DP) errors
#

DNS_ERROR_DP_BASE = 9900

# DNS_ERROR_DP_DOES_NOT_EXIST           0x000026ad
#
# MessageId: DNS_ERROR_DP_DOES_NOT_EXIST
#
# MessageText:
#
# The specified directory partition does not exist.
#
DNS_ERROR_DP_DOES_NOT_EXIST = 9901

# DNS_ERROR_DP_ALREADY_EXISTS           0x000026ae
#
# MessageId: DNS_ERROR_DP_ALREADY_EXISTS
#
# MessageText:
#
# The specified directory partition already exists.
#
DNS_ERROR_DP_ALREADY_EXISTS = 9902

# DNS_ERROR_DP_NOT_ENLISTED             0x000026af
#
# MessageId: DNS_ERROR_DP_NOT_ENLISTED
#
# MessageText:
#
# This DNS server is not enlisted in the specified directory partition.
#
DNS_ERROR_DP_NOT_ENLISTED = 9903

# DNS_ERROR_DP_ALREADY_ENLISTED         0x000026b0
#
# MessageId: DNS_ERROR_DP_ALREADY_ENLISTED
#
# MessageText:
#
# This DNS server is already enlisted in the specified directory partition.
#
DNS_ERROR_DP_ALREADY_ENLISTED = 9904

# DNS_ERROR_DP_NOT_AVAILABLE            0x000026b1
#
# MessageId: DNS_ERROR_DP_NOT_AVAILABLE
#
# MessageText:
#
# The directory partition is not available at this time. Please wait a few minutes and try again.
#
DNS_ERROR_DP_NOT_AVAILABLE = 9905

# DNS_ERROR_DP_FSMO_ERROR               0x000026b2
#
# MessageId: DNS_ERROR_DP_FSMO_ERROR
#
# MessageText:
#
# The operation failed because the domain naming master FSMO role could not be reached. The domain controller holding the domain naming master FSMO role is down or unable to service the request or is not running Windows Server 2003 or later.
#
DNS_ERROR_DP_FSMO_ERROR = 9906


#
# DNS ZoneScope errors from 9951 to 9960
#
# DNS_ERROR_ZONESCOPE_ALREADY_EXISTS               0x000026df
#
# MessageId: DNS_ERROR_ZONESCOPE_ALREADY_EXISTS
#
# MessageText:
#
# The scope already exists for the zone.
#
DNS_ERROR_ZONESCOPE_ALREADY_EXISTS = 9951

# DNS_ERROR_ZONESCOPE_DOES_NOT_EXIST       0x000026e0
#
# MessageId: DNS_ERROR_ZONESCOPE_DOES_NOT_EXIST
#
# MessageText:
#
# The scope does not exist for the zone.
#
DNS_ERROR_ZONESCOPE_DOES_NOT_EXIST = 9952

# DNS_ERROR_DEFAULT_ZONESCOPE 0x000026e1
#
# MessageId: DNS_ERROR_DEFAULT_ZONESCOPE
#
# MessageText:
#
# The scope is the same as the default zone scope.
#
DNS_ERROR_DEFAULT_ZONESCOPE = 9953

# DNS_ERROR_INVALID_ZONESCOPE_NAME 0x000026e2
#
# MessageId: DNS_ERROR_INVALID_ZONESCOPE_NAME
#
# MessageText:
#
# The scope name contains invalid characters.
#
DNS_ERROR_INVALID_ZONESCOPE_NAME = 9954

# DNS_ERROR_NOT_ALLOWED_WITH_ZONESCOPES 0x000026e3
#
# MessageId: DNS_ERROR_NOT_ALLOWED_WITH_ZONESCOPES
#
# MessageText:
#
# Operation not allowed when the zone has scopes.
#
DNS_ERROR_NOT_ALLOWED_WITH_ZONESCOPES = 9955

# DNS_ERROR_LOAD_ZONESCOPE_FAILED 0x000026e4
#
# MessageId: DNS_ERROR_LOAD_ZONESCOPE_FAILED
#
# MessageText:
#
# Failed to load zone scope.
#
DNS_ERROR_LOAD_ZONESCOPE_FAILED = 9956

# DNS_ERROR_ZONESCOPE_FILE_WRITEBACK_FAILED 0x000026e5
#
# MessageId: DNS_ERROR_ZONESCOPE_FILE_WRITEBACK_FAILED
#
# MessageText:
#
# Failed to write data file for DNS zone scope. Please verify the file exists and is writable.
#
DNS_ERROR_ZONESCOPE_FILE_WRITEBACK_FAILED = 9957




#/////////////////////////////////////////////////
#                                               //
#             End of DNS Error Codes            //
#                                               //
#                  9000 to 9999                 //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#               WinSock Error Codes             //
#                                               //
#                 10000 to 11999                //
#/////////////////////////////////////////////////

#
# WinSock error codes are also defined in WinSock.h
# and WinSock2.h, hence the IFDEF
#
#ifndef WSABASEERR
WSABASEERR = 10000
#
# MessageId: WSAEINTR
#
# MessageText:
#
# A blocking operation was interrupted by a call to WSACancelBlockingCall.
#
WSAEINTR = 10004

#
# MessageId: WSAEBADF
#
# MessageText:
#
# The file handle supplied is not valid.
#
WSAEBADF = 10009

#
# MessageId: WSAEACCES
#
# MessageText:
#
# An attempt was made to access a socket in a way forbidden by its access permissions.
#
WSAEACCES = 10013

#
# MessageId: WSAEFAULT
#
# MessageText:
#
# The system detected an invalid pointer address in attempting to use a pointer argument in a call.
#
WSAEFAULT = 10014

#
# MessageId: WSAEINVAL
#
# MessageText:
#
# An invalid argument was supplied.
#
WSAEINVAL = 10022

#
# MessageId: WSAEMFILE
#
# MessageText:
#
# Too many open sockets.
#
WSAEMFILE = 10024

#
# MessageId: WSAEWOULDBLOCK
#
# MessageText:
#
# A non-blocking socket operation could not be completed immediately.
#
WSAEWOULDBLOCK = 10035

#
# MessageId: WSAEINPROGRESS
#
# MessageText:
#
# A blocking operation is currently executing.
#
WSAEINPROGRESS = 10036

#
# MessageId: WSAEALREADY
#
# MessageText:
#
# An operation was attempted on a non-blocking socket that already had an operation in progress.
#
WSAEALREADY = 10037

#
# MessageId: WSAENOTSOCK
#
# MessageText:
#
# An operation was attempted on something that is not a socket.
#
WSAENOTSOCK = 10038

#
# MessageId: WSAEDESTADDRREQ
#
# MessageText:
#
# A required address was omitted from an operation on a socket.
#
WSAEDESTADDRREQ = 10039

#
# MessageId: WSAEMSGSIZE
#
# MessageText:
#
# A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram into was smaller than the datagram itself.
#
WSAEMSGSIZE = 10040

#
# MessageId: WSAEPROTOTYPE
#
# MessageText:
#
# A protocol was specified in the socket function call that does not support the semantics of the socket type requested.
#
WSAEPROTOTYPE = 10041

#
# MessageId: WSAENOPROTOOPT
#
# MessageText:
#
# An unknown, invalid, or unsupported option or level was specified in a getsockopt or setsockopt call.
#
WSAENOPROTOOPT = 10042

#
# MessageId: WSAEPROTONOSUPPORT
#
# MessageText:
#
# The requested protocol has not been configured into the system, or no implementation for it exists.
#
WSAEPROTONOSUPPORT = 10043

#
# MessageId: WSAESOCKTNOSUPPORT
#
# MessageText:
#
# The support for the specified socket type does not exist in this address family.
#
WSAESOCKTNOSUPPORT = 10044

#
# MessageId: WSAEOPNOTSUPP
#
# MessageText:
#
# The attempted operation is not supported for the type of object referenced.
#
WSAEOPNOTSUPP = 10045

#
# MessageId: WSAEPFNOSUPPORT
#
# MessageText:
#
# The protocol family has not been configured into the system or no implementation for it exists.
#
WSAEPFNOSUPPORT = 10046

#
# MessageId: WSAEAFNOSUPPORT
#
# MessageText:
#
# An address incompatible with the requested protocol was used.
#
WSAEAFNOSUPPORT = 10047

#
# MessageId: WSAEADDRINUSE
#
# MessageText:
#
# Only one usage of each socket address (protocol/network address/port) is normally permitted.
#
WSAEADDRINUSE = 10048

#
# MessageId: WSAEADDRNOTAVAIL
#
# MessageText:
#
# The requested address is not valid in its context.
#
WSAEADDRNOTAVAIL = 10049

#
# MessageId: WSAENETDOWN
#
# MessageText:
#
# A socket operation encountered a dead network.
#
WSAENETDOWN = 10050

#
# MessageId: WSAENETUNREACH
#
# MessageText:
#
# A socket operation was attempted to an unreachable network.
#
WSAENETUNREACH = 10051

#
# MessageId: WSAENETRESET
#
# MessageText:
#
# The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress.
#
WSAENETRESET = 10052

#
# MessageId: WSAECONNABORTED
#
# MessageText:
#
# An established connection was aborted by the software in your host machine.
#
WSAECONNABORTED = 10053

#
# MessageId: WSAECONNRESET
#
# MessageText:
#
# An existing connection was forcibly closed by the remote host.
#
WSAECONNRESET = 10054

#
# MessageId: WSAENOBUFS
#
# MessageText:
#
# An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.
#
WSAENOBUFS = 10055

#
# MessageId: WSAEISCONN
#
# MessageText:
#
# A connect request was made on an already connected socket.
#
WSAEISCONN = 10056

#
# MessageId: WSAENOTCONN
#
# MessageText:
#
# A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied.
#
WSAENOTCONN = 10057

#
# MessageId: WSAESHUTDOWN
#
# MessageText:
#
# A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous shutdown call.
#
WSAESHUTDOWN = 10058

#
# MessageId: WSAETOOMANYREFS
#
# MessageText:
#
# Too many references to some kernel object.
#
WSAETOOMANYREFS = 10059

#
# MessageId: WSAETIMEDOUT
#
# MessageText:
#
# A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.
#
WSAETIMEDOUT = 10060

#
# MessageId: WSAECONNREFUSED
#
# MessageText:
#
# No connection could be made because the target machine actively refused it.
#
WSAECONNREFUSED = 10061

#
# MessageId: WSAELOOP
#
# MessageText:
#
# Cannot translate name.
#
WSAELOOP = 10062

#
# MessageId: WSAENAMETOOLONG
#
# MessageText:
#
# Name component or name was too long.
#
WSAENAMETOOLONG = 10063

#
# MessageId: WSAEHOSTDOWN
#
# MessageText:
#
# A socket operation failed because the destination host was down.
#
WSAEHOSTDOWN = 10064

#
# MessageId: WSAEHOSTUNREACH
#
# MessageText:
#
# A socket operation was attempted to an unreachable host.
#
WSAEHOSTUNREACH = 10065

#
# MessageId: WSAENOTEMPTY
#
# MessageText:
#
# Cannot remove a directory that is not empty.
#
WSAENOTEMPTY = 10066

#
# MessageId: WSAEPROCLIM
#
# MessageText:
#
# A Windows Sockets implementation may have a limit on the number of applications that may use it simultaneously.
#
WSAEPROCLIM = 10067

#
# MessageId: WSAEUSERS
#
# MessageText:
#
# Ran out of quota.
#
WSAEUSERS = 10068

#
# MessageId: WSAEDQUOT
#
# MessageText:
#
# Ran out of disk quota.
#
WSAEDQUOT = 10069

#
# MessageId: WSAESTALE
#
# MessageText:
#
# File handle reference is no longer available.
#
WSAESTALE = 10070

#
# MessageId: WSAEREMOTE
#
# MessageText:
#
# Item is not available locally.
#
WSAEREMOTE = 10071

#
# MessageId: WSASYSNOTREADY
#
# MessageText:
#
# WSAStartup cannot function at this time because the underlying system it uses to provide network services is currently unavailable.
#
WSASYSNOTREADY = 10091

#
# MessageId: WSAVERNOTSUPPORTED
#
# MessageText:
#
# The Windows Sockets version requested is not supported.
#
WSAVERNOTSUPPORTED = 10092

#
# MessageId: WSANOTINITIALISED
#
# MessageText:
#
# Either the application has not called WSAStartup, or WSAStartup failed.
#
WSANOTINITIALISED = 10093

#
# MessageId: WSAEDISCON
#
# MessageText:
#
# Returned by WSARecv or WSARecvFrom to indicate the remote party has initiated a graceful shutdown sequence.
#
WSAEDISCON = 10101

#
# MessageId: WSAENOMORE
#
# MessageText:
#
# No more results can be returned by WSALookupServiceNext.
#
WSAENOMORE = 10102

#
# MessageId: WSAECANCELLED
#
# MessageText:
#
# A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.
#
WSAECANCELLED = 10103

#
# MessageId: WSAEINVALIDPROCTABLE
#
# MessageText:
#
# The procedure call table is invalid.
#
WSAEINVALIDPROCTABLE = 10104

#
# MessageId: WSAEINVALIDPROVIDER
#
# MessageText:
#
# The requested service provider is invalid.
#
WSAEINVALIDPROVIDER = 10105

#
# MessageId: WSAEPROVIDERFAILEDINIT
#
# MessageText:
#
# The requested service provider could not be loaded or initialized.
#
WSAEPROVIDERFAILEDINIT = 10106

#
# MessageId: WSASYSCALLFAILURE
#
# MessageText:
#
# A system call has failed.
#
WSASYSCALLFAILURE = 10107

#
# MessageId: WSASERVICE_NOT_FOUND
#
# MessageText:
#
# No such service is known. The service cannot be found in the specified name space.
#
WSASERVICE_NOT_FOUND = 10108

#
# MessageId: WSATYPE_NOT_FOUND
#
# MessageText:
#
# The specified class was not found.
#
WSATYPE_NOT_FOUND = 10109

#
# MessageId: WSA_E_NO_MORE
#
# MessageText:
#
# No more results can be returned by WSALookupServiceNext.
#
WSA_E_NO_MORE = 10110

#
# MessageId: WSA_E_CANCELLED
#
# MessageText:
#
# A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.
#
WSA_E_CANCELLED = 10111

#
# MessageId: WSAEREFUSED
#
# MessageText:
#
# A database query failed because it was actively refused.
#
WSAEREFUSED = 10112

#
# MessageId: WSAHOST_NOT_FOUND
#
# MessageText:
#
# No such host is known.
#
WSAHOST_NOT_FOUND = 11001

#
# MessageId: WSATRY_AGAIN
#
# MessageText:
#
# This is usually a temporary error during hostname resolution and means that the local server did not receive a response from an authoritative server.
#
WSATRY_AGAIN = 11002

#
# MessageId: WSANO_RECOVERY
#
# MessageText:
#
# A non-recoverable error occurred during a database lookup.
#
WSANO_RECOVERY = 11003

#
# MessageId: WSANO_DATA
#
# MessageText:
#
# The requested name is valid, but no data of the requested type was found.
#
WSANO_DATA = 11004

#
# MessageId: WSA_QOS_RECEIVERS
#
# MessageText:
#
# At least one reserve has arrived.
#
WSA_QOS_RECEIVERS = 11005

#
# MessageId: WSA_QOS_SENDERS
#
# MessageText:
#
# At least one path has arrived.
#
WSA_QOS_SENDERS = 11006

#
# MessageId: WSA_QOS_NO_SENDERS
#
# MessageText:
#
# There are no senders.
#
WSA_QOS_NO_SENDERS = 11007

#
# MessageId: WSA_QOS_NO_RECEIVERS
#
# MessageText:
#
# There are no receivers.
#
WSA_QOS_NO_RECEIVERS = 11008

#
# MessageId: WSA_QOS_REQUEST_CONFIRMED
#
# MessageText:
#
# Reserve has been confirmed.
#
WSA_QOS_REQUEST_CONFIRMED = 11009

#
# MessageId: WSA_QOS_ADMISSION_FAILURE
#
# MessageText:
#
# Error due to lack of resources.
#
WSA_QOS_ADMISSION_FAILURE = 11010

#
# MessageId: WSA_QOS_POLICY_FAILURE
#
# MessageText:
#
# Rejected for administrative reasons - bad credentials.
#
WSA_QOS_POLICY_FAILURE = 11011

#
# MessageId: WSA_QOS_BAD_STYLE
#
# MessageText:
#
# Unknown or conflicting style.
#
WSA_QOS_BAD_STYLE = 11012

#
# MessageId: WSA_QOS_BAD_OBJECT
#
# MessageText:
#
# Problem with some part of the filterspec or providerspecific buffer in general.
#
WSA_QOS_BAD_OBJECT = 11013

#
# MessageId: WSA_QOS_TRAFFIC_CTRL_ERROR
#
# MessageText:
#
# Problem with some part of the flowspec.
#
WSA_QOS_TRAFFIC_CTRL_ERROR = 11014

#
# MessageId: WSA_QOS_GENERIC_ERROR
#
# MessageText:
#
# General QOS error.
#
WSA_QOS_GENERIC_ERROR = 11015

#
# MessageId: WSA_QOS_ESERVICETYPE
#
# MessageText:
#
# An invalid or unrecognized service type was found in the flowspec.
#
WSA_QOS_ESERVICETYPE = 11016

#
# MessageId: WSA_QOS_EFLOWSPEC
#
# MessageText:
#
# An invalid or inconsistent flowspec was found in the QOS structure.
#
WSA_QOS_EFLOWSPEC = 11017

#
# MessageId: WSA_QOS_EPROVSPECBUF
#
# MessageText:
#
# Invalid QOS provider-specific buffer.
#
WSA_QOS_EPROVSPECBUF = 11018

#
# MessageId: WSA_QOS_EFILTERSTYLE
#
# MessageText:
#
# An invalid QOS filter style was used.
#
WSA_QOS_EFILTERSTYLE = 11019

#
# MessageId: WSA_QOS_EFILTERTYPE
#
# MessageText:
#
# An invalid QOS filter type was used.
#
WSA_QOS_EFILTERTYPE = 11020

#
# MessageId: WSA_QOS_EFILTERCOUNT
#
# MessageText:
#
# An incorrect number of QOS FILTERSPECs were specified in the FLOWDESCRIPTOR.
#
WSA_QOS_EFILTERCOUNT = 11021

#
# MessageId: WSA_QOS_EOBJLENGTH
#
# MessageText:
#
# An object with an invalid ObjectLength field was specified in the QOS provider-specific buffer.
#
WSA_QOS_EOBJLENGTH = 11022

#
# MessageId: WSA_QOS_EFLOWCOUNT
#
# MessageText:
#
# An incorrect number of flow descriptors was specified in the QOS structure.
#
WSA_QOS_EFLOWCOUNT = 11023

#
# MessageId: WSA_QOS_EUNKOWNPSOBJ
#
# MessageText:
#
# An unrecognized object was found in the QOS provider-specific buffer.
#
WSA_QOS_EUNKOWNPSOBJ = 11024

#
# MessageId: WSA_QOS_EPOLICYOBJ
#
# MessageText:
#
# An invalid policy object was found in the QOS provider-specific buffer.
#
WSA_QOS_EPOLICYOBJ = 11025

#
# MessageId: WSA_QOS_EFLOWDESC
#
# MessageText:
#
# An invalid QOS flow descriptor was found in the flow descriptor list.
#
WSA_QOS_EFLOWDESC = 11026

#
# MessageId: WSA_QOS_EPSFLOWSPEC
#
# MessageText:
#
# An invalid or inconsistent flowspec was found in the QOS provider specific buffer.
#
WSA_QOS_EPSFLOWSPEC = 11027

#
# MessageId: WSA_QOS_EPSFILTERSPEC
#
# MessageText:
#
# An invalid FILTERSPEC was found in the QOS provider-specific buffer.
#
WSA_QOS_EPSFILTERSPEC = 11028

#
# MessageId: WSA_QOS_ESDMODEOBJ
#
# MessageText:
#
# An invalid shape discard mode object was found in the QOS provider specific buffer.
#
WSA_QOS_ESDMODEOBJ = 11029

#
# MessageId: WSA_QOS_ESHAPERATEOBJ
#
# MessageText:
#
# An invalid shaping rate object was found in the QOS provider-specific buffer.
#
WSA_QOS_ESHAPERATEOBJ = 11030

#
# MessageId: WSA_QOS_RESERVED_PETYPE
#
# MessageText:
#
# A reserved policy element was found in the QOS provider-specific buffer.
#
WSA_QOS_RESERVED_PETYPE = 11031

#
# MessageId: WSA_SECURE_HOST_NOT_FOUND
#
# MessageText:
#
# No such host is known securely.
#
WSA_SECURE_HOST_NOT_FOUND = 11032

#
# MessageId: WSA_IPSEC_NAME_POLICY_ERROR
#
# MessageText:
#
# Name based IPSEC policy could not be added.
#
WSA_IPSEC_NAME_POLICY_ERROR = 11033

#endif // defined(WSABASEERR)

#/////////////////////////////////////////////////
#                                               //
#           End of WinSock Error Codes          //
#                                               //
#                 10000 to 11999                //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#                  Available                    //
#                                               //
#                 12000 to 12999                //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#           Start of IPSec Error codes          //
#                                               //
#                 13000 to 13999                //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_IPSEC_QM_POLICY_EXISTS
#
# MessageText:
#
# The specified quick mode policy already exists.
#
ERROR_IPSEC_QM_POLICY_EXISTS = 13000

#
# MessageId: ERROR_IPSEC_QM_POLICY_NOT_FOUND
#
# MessageText:
#
# The specified quick mode policy was not found.
#
ERROR_IPSEC_QM_POLICY_NOT_FOUND = 13001

#
# MessageId: ERROR_IPSEC_QM_POLICY_IN_USE
#
# MessageText:
#
# The specified quick mode policy is being used.
#
ERROR_IPSEC_QM_POLICY_IN_USE = 13002

#
# MessageId: ERROR_IPSEC_MM_POLICY_EXISTS
#
# MessageText:
#
# The specified main mode policy already exists.
#
ERROR_IPSEC_MM_POLICY_EXISTS = 13003

#
# MessageId: ERROR_IPSEC_MM_POLICY_NOT_FOUND
#
# MessageText:
#
# The specified main mode policy was not found
#
ERROR_IPSEC_MM_POLICY_NOT_FOUND = 13004

#
# MessageId: ERROR_IPSEC_MM_POLICY_IN_USE
#
# MessageText:
#
# The specified main mode policy is being used.
#
ERROR_IPSEC_MM_POLICY_IN_USE = 13005

#
# MessageId: ERROR_IPSEC_MM_FILTER_EXISTS
#
# MessageText:
#
# The specified main mode filter already exists.
#
ERROR_IPSEC_MM_FILTER_EXISTS = 13006

#
# MessageId: ERROR_IPSEC_MM_FILTER_NOT_FOUND
#
# MessageText:
#
# The specified main mode filter was not found.
#
ERROR_IPSEC_MM_FILTER_NOT_FOUND = 13007

#
# MessageId: ERROR_IPSEC_TRANSPORT_FILTER_EXISTS
#
# MessageText:
#
# The specified transport mode filter already exists.
#
ERROR_IPSEC_TRANSPORT_FILTER_EXISTS = 13008

#
# MessageId: ERROR_IPSEC_TRANSPORT_FILTER_NOT_FOUND
#
# MessageText:
#
# The specified transport mode filter does not exist.
#
ERROR_IPSEC_TRANSPORT_FILTER_NOT_FOUND = 13009

#
# MessageId: ERROR_IPSEC_MM_AUTH_EXISTS
#
# MessageText:
#
# The specified main mode authentication list exists.
#
ERROR_IPSEC_MM_AUTH_EXISTS = 13010

#
# MessageId: ERROR_IPSEC_MM_AUTH_NOT_FOUND
#
# MessageText:
#
# The specified main mode authentication list was not found.
#
ERROR_IPSEC_MM_AUTH_NOT_FOUND = 13011

#
# MessageId: ERROR_IPSEC_MM_AUTH_IN_USE
#
# MessageText:
#
# The specified main mode authentication list is being used.
#
ERROR_IPSEC_MM_AUTH_IN_USE = 13012

#
# MessageId: ERROR_IPSEC_DEFAULT_MM_POLICY_NOT_FOUND
#
# MessageText:
#
# The specified default main mode policy was not found.
#
ERROR_IPSEC_DEFAULT_MM_POLICY_NOT_FOUND = 13013

#
# MessageId: ERROR_IPSEC_DEFAULT_MM_AUTH_NOT_FOUND
#
# MessageText:
#
# The specified default main mode authentication list was not found.
#
ERROR_IPSEC_DEFAULT_MM_AUTH_NOT_FOUND = 13014

#
# MessageId: ERROR_IPSEC_DEFAULT_QM_POLICY_NOT_FOUND
#
# MessageText:
#
# The specified default quick mode policy was not found.
#
ERROR_IPSEC_DEFAULT_QM_POLICY_NOT_FOUND = 13015

#
# MessageId: ERROR_IPSEC_TUNNEL_FILTER_EXISTS
#
# MessageText:
#
# The specified tunnel mode filter exists.
#
ERROR_IPSEC_TUNNEL_FILTER_EXISTS = 13016

#
# MessageId: ERROR_IPSEC_TUNNEL_FILTER_NOT_FOUND
#
# MessageText:
#
# The specified tunnel mode filter was not found.
#
ERROR_IPSEC_TUNNEL_FILTER_NOT_FOUND = 13017

#
# MessageId: ERROR_IPSEC_MM_FILTER_PENDING_DELETION
#
# MessageText:
#
# The Main Mode filter is pending deletion.
#
ERROR_IPSEC_MM_FILTER_PENDING_DELETION = 13018

#
# MessageId: ERROR_IPSEC_TRANSPORT_FILTER_PENDING_DELETION
#
# MessageText:
#
# The transport filter is pending deletion.
#
ERROR_IPSEC_TRANSPORT_FILTER_PENDING_DELETION = 13019

#
# MessageId: ERROR_IPSEC_TUNNEL_FILTER_PENDING_DELETION
#
# MessageText:
#
# The tunnel filter is pending deletion.
#
ERROR_IPSEC_TUNNEL_FILTER_PENDING_DELETION = 13020

#
# MessageId: ERROR_IPSEC_MM_POLICY_PENDING_DELETION
#
# MessageText:
#
# The Main Mode policy is pending deletion.
#
ERROR_IPSEC_MM_POLICY_PENDING_DELETION = 13021

#
# MessageId: ERROR_IPSEC_MM_AUTH_PENDING_DELETION
#
# MessageText:
#
# The Main Mode authentication bundle is pending deletion.
#
ERROR_IPSEC_MM_AUTH_PENDING_DELETION = 13022

#
# MessageId: ERROR_IPSEC_QM_POLICY_PENDING_DELETION
#
# MessageText:
#
# The Quick Mode policy is pending deletion.
#
ERROR_IPSEC_QM_POLICY_PENDING_DELETION = 13023

#
# MessageId: WARNING_IPSEC_MM_POLICY_PRUNED
#
# MessageText:
#
# The Main Mode policy was successfully added, but some of the requested offers are not supported.
#
WARNING_IPSEC_MM_POLICY_PRUNED = 13024

#
# MessageId: WARNING_IPSEC_QM_POLICY_PRUNED
#
# MessageText:
#
# The Quick Mode policy was successfully added, but some of the requested offers are not supported.
#
WARNING_IPSEC_QM_POLICY_PRUNED = 13025

#
# MessageId: ERROR_IPSEC_IKE_NEG_STATUS_BEGIN
#
# MessageText:
#
#  ERROR_IPSEC_IKE_NEG_STATUS_BEGIN
#
ERROR_IPSEC_IKE_NEG_STATUS_BEGIN = 13800

#
# MessageId: ERROR_IPSEC_IKE_AUTH_FAIL
#
# MessageText:
#
# IKE authentication credentials are unacceptable
#
ERROR_IPSEC_IKE_AUTH_FAIL = 13801

#
# MessageId: ERROR_IPSEC_IKE_ATTRIB_FAIL
#
# MessageText:
#
# IKE security attributes are unacceptable
#
ERROR_IPSEC_IKE_ATTRIB_FAIL = 13802

#
# MessageId: ERROR_IPSEC_IKE_NEGOTIATION_PENDING
#
# MessageText:
#
# IKE Negotiation in progress
#
ERROR_IPSEC_IKE_NEGOTIATION_PENDING = 13803

#
# MessageId: ERROR_IPSEC_IKE_GENERAL_PROCESSING_ERROR
#
# MessageText:
#
# General processing error
#
ERROR_IPSEC_IKE_GENERAL_PROCESSING_ERROR = 13804

#
# MessageId: ERROR_IPSEC_IKE_TIMED_OUT
#
# MessageText:
#
# Negotiation timed out
#
ERROR_IPSEC_IKE_TIMED_OUT = 13805

#
# MessageId: ERROR_IPSEC_IKE_NO_CERT
#
# MessageText:
#
# IKE failed to find valid machine certificate. Contact your Network Security Administrator about installing a valid certificate in the appropriate Certificate Store.
#
ERROR_IPSEC_IKE_NO_CERT = 13806

#
# MessageId: ERROR_IPSEC_IKE_SA_DELETED
#
# MessageText:
#
# IKE SA deleted by peer before establishment completed
#
ERROR_IPSEC_IKE_SA_DELETED = 13807

#
# MessageId: ERROR_IPSEC_IKE_SA_REAPED
#
# MessageText:
#
# IKE SA deleted before establishment completed
#
ERROR_IPSEC_IKE_SA_REAPED = 13808

#
# MessageId: ERROR_IPSEC_IKE_MM_ACQUIRE_DROP
#
# MessageText:
#
# Negotiation request sat in Queue too long
#
ERROR_IPSEC_IKE_MM_ACQUIRE_DROP = 13809

#
# MessageId: ERROR_IPSEC_IKE_QM_ACQUIRE_DROP
#
# MessageText:
#
# Negotiation request sat in Queue too long
#
ERROR_IPSEC_IKE_QM_ACQUIRE_DROP = 13810

#
# MessageId: ERROR_IPSEC_IKE_QUEUE_DROP_MM
#
# MessageText:
#
# Negotiation request sat in Queue too long
#
ERROR_IPSEC_IKE_QUEUE_DROP_MM = 13811

#
# MessageId: ERROR_IPSEC_IKE_QUEUE_DROP_NO_MM
#
# MessageText:
#
# Negotiation request sat in Queue too long
#
ERROR_IPSEC_IKE_QUEUE_DROP_NO_MM = 13812

#
# MessageId: ERROR_IPSEC_IKE_DROP_NO_RESPONSE
#
# MessageText:
#
# No response from peer
#
ERROR_IPSEC_IKE_DROP_NO_RESPONSE = 13813

#
# MessageId: ERROR_IPSEC_IKE_MM_DELAY_DROP
#
# MessageText:
#
# Negotiation took too long
#
ERROR_IPSEC_IKE_MM_DELAY_DROP = 13814

#
# MessageId: ERROR_IPSEC_IKE_QM_DELAY_DROP
#
# MessageText:
#
# Negotiation took too long
#
ERROR_IPSEC_IKE_QM_DELAY_DROP = 13815

#
# MessageId: ERROR_IPSEC_IKE_ERROR
#
# MessageText:
#
# Unknown error occurred
#
ERROR_IPSEC_IKE_ERROR = 13816

#
# MessageId: ERROR_IPSEC_IKE_CRL_FAILED
#
# MessageText:
#
# Certificate Revocation Check failed
#
ERROR_IPSEC_IKE_CRL_FAILED = 13817

#
# MessageId: ERROR_IPSEC_IKE_INVALID_KEY_USAGE
#
# MessageText:
#
# Invalid certificate key usage
#
ERROR_IPSEC_IKE_INVALID_KEY_USAGE = 13818

#
# MessageId: ERROR_IPSEC_IKE_INVALID_CERT_TYPE
#
# MessageText:
#
# Invalid certificate type
#
ERROR_IPSEC_IKE_INVALID_CERT_TYPE = 13819

#
# MessageId: ERROR_IPSEC_IKE_NO_PRIVATE_KEY
#
# MessageText:
#
# IKE negotiation failed because the machine certificate used does not have a private key. IPsec certificates require a private key. Contact your Network Security administrator about replacing with a certificate that has a private key.
#
ERROR_IPSEC_IKE_NO_PRIVATE_KEY = 13820

#
# MessageId: ERROR_IPSEC_IKE_SIMULTANEOUS_REKEY
#
# MessageText:
#
# Simultaneous rekeys were detected.
#
ERROR_IPSEC_IKE_SIMULTANEOUS_REKEY = 13821

#
# MessageId: ERROR_IPSEC_IKE_DH_FAIL
#
# MessageText:
#
# Failure in Diffie-Hellman computation
#
ERROR_IPSEC_IKE_DH_FAIL = 13822

#
# MessageId: ERROR_IPSEC_IKE_CRITICAL_PAYLOAD_NOT_RECOGNIZED
#
# MessageText:
#
# Don't know how to process critical payload
#
ERROR_IPSEC_IKE_CRITICAL_PAYLOAD_NOT_RECOGNIZED = 13823

#
# MessageId: ERROR_IPSEC_IKE_INVALID_HEADER
#
# MessageText:
#
# Invalid header
#
ERROR_IPSEC_IKE_INVALID_HEADER = 13824

#
# MessageId: ERROR_IPSEC_IKE_NO_POLICY
#
# MessageText:
#
# No policy configured
#
ERROR_IPSEC_IKE_NO_POLICY = 13825

#
# MessageId: ERROR_IPSEC_IKE_INVALID_SIGNATURE
#
# MessageText:
#
# Failed to verify signature
#
ERROR_IPSEC_IKE_INVALID_SIGNATURE = 13826

#
# MessageId: ERROR_IPSEC_IKE_KERBEROS_ERROR
#
# MessageText:
#
# Failed to authenticate using Kerberos
#
ERROR_IPSEC_IKE_KERBEROS_ERROR = 13827

#
# MessageId: ERROR_IPSEC_IKE_NO_PUBLIC_KEY
#
# MessageText:
#
# Peer's certificate did not have a public key
#
ERROR_IPSEC_IKE_NO_PUBLIC_KEY = 13828

# These must stay as a unit.
#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR
#
# MessageText:
#
# Error processing error payload
#
ERROR_IPSEC_IKE_PROCESS_ERR = 13829

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_SA
#
# MessageText:
#
# Error processing SA payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_SA = 13830

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_PROP
#
# MessageText:
#
# Error processing Proposal payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_PROP = 13831

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_TRANS
#
# MessageText:
#
# Error processing Transform payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_TRANS = 13832

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_KE
#
# MessageText:
#
# Error processing KE payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_KE = 13833

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_ID
#
# MessageText:
#
# Error processing ID payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_ID = 13834

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_CERT
#
# MessageText:
#
# Error processing Cert payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_CERT = 13835

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_CERT_REQ
#
# MessageText:
#
# Error processing Certificate Request payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_CERT_REQ = 13836

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_HASH
#
# MessageText:
#
# Error processing Hash payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_HASH = 13837

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_SIG
#
# MessageText:
#
# Error processing Signature payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_SIG = 13838

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_NONCE
#
# MessageText:
#
# Error processing Nonce payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_NONCE = 13839

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_NOTIFY
#
# MessageText:
#
# Error processing Notify payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_NOTIFY = 13840

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_DELETE
#
# MessageText:
#
# Error processing Delete Payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_DELETE = 13841

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_VENDOR
#
# MessageText:
#
# Error processing VendorId payload
#
ERROR_IPSEC_IKE_PROCESS_ERR_VENDOR = 13842

#
# MessageId: ERROR_IPSEC_IKE_INVALID_PAYLOAD
#
# MessageText:
#
# Invalid payload received
#
ERROR_IPSEC_IKE_INVALID_PAYLOAD = 13843

#
# MessageId: ERROR_IPSEC_IKE_LOAD_SOFT_SA
#
# MessageText:
#
# Soft SA loaded
#
ERROR_IPSEC_IKE_LOAD_SOFT_SA = 13844

#
# MessageId: ERROR_IPSEC_IKE_SOFT_SA_TORN_DOWN
#
# MessageText:
#
# Soft SA torn down
#
ERROR_IPSEC_IKE_SOFT_SA_TORN_DOWN = 13845

#
# MessageId: ERROR_IPSEC_IKE_INVALID_COOKIE
#
# MessageText:
#
# Invalid cookie received.
#
ERROR_IPSEC_IKE_INVALID_COOKIE = 13846

#
# MessageId: ERROR_IPSEC_IKE_NO_PEER_CERT
#
# MessageText:
#
# Peer failed to send valid machine certificate
#
ERROR_IPSEC_IKE_NO_PEER_CERT = 13847

#
# MessageId: ERROR_IPSEC_IKE_PEER_CRL_FAILED
#
# MessageText:
#
# Certification Revocation check of peer's certificate failed
#
ERROR_IPSEC_IKE_PEER_CRL_FAILED = 13848

#
# MessageId: ERROR_IPSEC_IKE_POLICY_CHANGE
#
# MessageText:
#
# New policy invalidated SAs formed with old policy
#
ERROR_IPSEC_IKE_POLICY_CHANGE = 13849

#
# MessageId: ERROR_IPSEC_IKE_NO_MM_POLICY
#
# MessageText:
#
# There is no available Main Mode IKE policy.
#
ERROR_IPSEC_IKE_NO_MM_POLICY = 13850

#
# MessageId: ERROR_IPSEC_IKE_NOTCBPRIV
#
# MessageText:
#
# Failed to enabled TCB privilege.
#
ERROR_IPSEC_IKE_NOTCBPRIV = 13851

#
# MessageId: ERROR_IPSEC_IKE_SECLOADFAIL
#
# MessageText:
#
# Failed to load SECURITY.DLL.
#
ERROR_IPSEC_IKE_SECLOADFAIL = 13852

#
# MessageId: ERROR_IPSEC_IKE_FAILSSPINIT
#
# MessageText:
#
# Failed to obtain security function table dispatch address from SSPI.
#
ERROR_IPSEC_IKE_FAILSSPINIT = 13853

#
# MessageId: ERROR_IPSEC_IKE_FAILQUERYSSP
#
# MessageText:
#
# Failed to query Kerberos package to obtain max token size.
#
ERROR_IPSEC_IKE_FAILQUERYSSP = 13854

#
# MessageId: ERROR_IPSEC_IKE_SRVACQFAIL
#
# MessageText:
#
# Failed to obtain Kerberos server credentials for ISAKMP/ERROR_IPSEC_IKE service. Kerberos authentication will not function. The most likely reason for this is lack of domain membership. This is normal if your computer is a member of a workgroup.
#
ERROR_IPSEC_IKE_SRVACQFAIL = 13855

#
# MessageId: ERROR_IPSEC_IKE_SRVQUERYCRED
#
# MessageText:
#
# Failed to determine SSPI principal name for ISAKMP/ERROR_IPSEC_IKE service (QueryCredentialsAttributes).
#
ERROR_IPSEC_IKE_SRVQUERYCRED = 13856

#
# MessageId: ERROR_IPSEC_IKE_GETSPIFAIL
#
# MessageText:
#
# Failed to obtain new SPI for the inbound SA from IPsec driver. The most common cause for this is that the driver does not have the correct filter. Check your policy to verify the filters.
#
ERROR_IPSEC_IKE_GETSPIFAIL = 13857

#
# MessageId: ERROR_IPSEC_IKE_INVALID_FILTER
#
# MessageText:
#
# Given filter is invalid
#
ERROR_IPSEC_IKE_INVALID_FILTER = 13858

#
# MessageId: ERROR_IPSEC_IKE_OUT_OF_MEMORY
#
# MessageText:
#
# Memory allocation failed.
#
ERROR_IPSEC_IKE_OUT_OF_MEMORY = 13859

#
# MessageId: ERROR_IPSEC_IKE_ADD_UPDATE_KEY_FAILED
#
# MessageText:
#
# Failed to add Security Association to IPsec Driver. The most common cause for this is if the IKE negotiation took too long to complete. If the problem persists, reduce the load on the faulting machine.
#
ERROR_IPSEC_IKE_ADD_UPDATE_KEY_FAILED = 13860

#
# MessageId: ERROR_IPSEC_IKE_INVALID_POLICY
#
# MessageText:
#
# Invalid policy
#
ERROR_IPSEC_IKE_INVALID_POLICY = 13861

#
# MessageId: ERROR_IPSEC_IKE_UNKNOWN_DOI
#
# MessageText:
#
# Invalid DOI
#
ERROR_IPSEC_IKE_UNKNOWN_DOI = 13862

#
# MessageId: ERROR_IPSEC_IKE_INVALID_SITUATION
#
# MessageText:
#
# Invalid situation
#
ERROR_IPSEC_IKE_INVALID_SITUATION = 13863

#
# MessageId: ERROR_IPSEC_IKE_DH_FAILURE
#
# MessageText:
#
# Diffie-Hellman failure
#
ERROR_IPSEC_IKE_DH_FAILURE = 13864

#
# MessageId: ERROR_IPSEC_IKE_INVALID_GROUP
#
# MessageText:
#
# Invalid Diffie-Hellman group
#
ERROR_IPSEC_IKE_INVALID_GROUP = 13865

#
# MessageId: ERROR_IPSEC_IKE_ENCRYPT
#
# MessageText:
#
# Error encrypting payload
#
ERROR_IPSEC_IKE_ENCRYPT = 13866

#
# MessageId: ERROR_IPSEC_IKE_DECRYPT
#
# MessageText:
#
# Error decrypting payload
#
ERROR_IPSEC_IKE_DECRYPT = 13867

#
# MessageId: ERROR_IPSEC_IKE_POLICY_MATCH
#
# MessageText:
#
# Policy match error
#
ERROR_IPSEC_IKE_POLICY_MATCH = 13868

#
# MessageId: ERROR_IPSEC_IKE_UNSUPPORTED_ID
#
# MessageText:
#
# Unsupported ID
#
ERROR_IPSEC_IKE_UNSUPPORTED_ID = 13869

#
# MessageId: ERROR_IPSEC_IKE_INVALID_HASH
#
# MessageText:
#
# Hash verification failed
#
ERROR_IPSEC_IKE_INVALID_HASH = 13870

#
# MessageId: ERROR_IPSEC_IKE_INVALID_HASH_ALG
#
# MessageText:
#
# Invalid hash algorithm
#
ERROR_IPSEC_IKE_INVALID_HASH_ALG = 13871

#
# MessageId: ERROR_IPSEC_IKE_INVALID_HASH_SIZE
#
# MessageText:
#
# Invalid hash size
#
ERROR_IPSEC_IKE_INVALID_HASH_SIZE = 13872

#
# MessageId: ERROR_IPSEC_IKE_INVALID_ENCRYPT_ALG
#
# MessageText:
#
# Invalid encryption algorithm
#
ERROR_IPSEC_IKE_INVALID_ENCRYPT_ALG = 13873

#
# MessageId: ERROR_IPSEC_IKE_INVALID_AUTH_ALG
#
# MessageText:
#
# Invalid authentication algorithm
#
ERROR_IPSEC_IKE_INVALID_AUTH_ALG = 13874

#
# MessageId: ERROR_IPSEC_IKE_INVALID_SIG
#
# MessageText:
#
# Invalid certificate signature
#
ERROR_IPSEC_IKE_INVALID_SIG = 13875

#
# MessageId: ERROR_IPSEC_IKE_LOAD_FAILED
#
# MessageText:
#
# Load failed
#
ERROR_IPSEC_IKE_LOAD_FAILED = 13876

#
# MessageId: ERROR_IPSEC_IKE_RPC_DELETE
#
# MessageText:
#
# Deleted via RPC call
#
ERROR_IPSEC_IKE_RPC_DELETE = 13877

#
# MessageId: ERROR_IPSEC_IKE_BENIGN_REINIT
#
# MessageText:
#
# Temporary state created to perform reinitialization. This is not a real failure.
#
ERROR_IPSEC_IKE_BENIGN_REINIT = 13878

#
# MessageId: ERROR_IPSEC_IKE_INVALID_RESPONDER_LIFETIME_NOTIFY
#
# MessageText:
#
# The lifetime value received in the Responder Lifetime Notify is below the Windows 2000 configured minimum value. Please fix the policy on the peer machine.
#
ERROR_IPSEC_IKE_INVALID_RESPONDER_LIFETIME_NOTIFY = 13879

#
# MessageId: ERROR_IPSEC_IKE_INVALID_MAJOR_VERSION
#
# MessageText:
#
# The recipient cannot handle version of IKE specified in the header.
#
ERROR_IPSEC_IKE_INVALID_MAJOR_VERSION = 13880

#
# MessageId: ERROR_IPSEC_IKE_INVALID_CERT_KEYLEN
#
# MessageText:
#
# Key length in certificate is too small for configured security requirements.
#
ERROR_IPSEC_IKE_INVALID_CERT_KEYLEN = 13881

#
# MessageId: ERROR_IPSEC_IKE_MM_LIMIT
#
# MessageText:
#
# Max number of established MM SAs to peer exceeded.
#
ERROR_IPSEC_IKE_MM_LIMIT = 13882

#
# MessageId: ERROR_IPSEC_IKE_NEGOTIATION_DISABLED
#
# MessageText:
#
# IKE received a policy that disables negotiation.
#
ERROR_IPSEC_IKE_NEGOTIATION_DISABLED = 13883

#
# MessageId: ERROR_IPSEC_IKE_QM_LIMIT
#
# MessageText:
#
# Reached maximum quick mode limit for the main mode. New main mode will be started.
#
ERROR_IPSEC_IKE_QM_LIMIT = 13884

#
# MessageId: ERROR_IPSEC_IKE_MM_EXPIRED
#
# MessageText:
#
# Main mode SA lifetime expired or peer sent a main mode delete.
#
ERROR_IPSEC_IKE_MM_EXPIRED = 13885

#
# MessageId: ERROR_IPSEC_IKE_PEER_MM_ASSUMED_INVALID
#
# MessageText:
#
# Main mode SA assumed to be invalid because peer stopped responding.
#
ERROR_IPSEC_IKE_PEER_MM_ASSUMED_INVALID = 13886

#
# MessageId: ERROR_IPSEC_IKE_CERT_CHAIN_POLICY_MISMATCH
#
# MessageText:
#
# Certificate doesn't chain to a trusted root in IPsec policy.
#
ERROR_IPSEC_IKE_CERT_CHAIN_POLICY_MISMATCH = 13887

#
# MessageId: ERROR_IPSEC_IKE_UNEXPECTED_MESSAGE_ID
#
# MessageText:
#
# Received unexpected message ID.
#
ERROR_IPSEC_IKE_UNEXPECTED_MESSAGE_ID = 13888

#
# MessageId: ERROR_IPSEC_IKE_INVALID_AUTH_PAYLOAD
#
# MessageText:
#
# Received invalid authentication offers.
#
ERROR_IPSEC_IKE_INVALID_AUTH_PAYLOAD = 13889

#
# MessageId: ERROR_IPSEC_IKE_DOS_COOKIE_SENT
#
# MessageText:
#
# Sent DoS cookie notify to initiator.
#
ERROR_IPSEC_IKE_DOS_COOKIE_SENT = 13890

#
# MessageId: ERROR_IPSEC_IKE_SHUTTING_DOWN
#
# MessageText:
#
# IKE service is shutting down.
#
ERROR_IPSEC_IKE_SHUTTING_DOWN = 13891

#
# MessageId: ERROR_IPSEC_IKE_CGA_AUTH_FAILED
#
# MessageText:
#
# Could not verify binding between CGA address and certificate.
#
ERROR_IPSEC_IKE_CGA_AUTH_FAILED = 13892

#
# MessageId: ERROR_IPSEC_IKE_PROCESS_ERR_NATOA
#
# MessageText:
#
# Error processing NatOA payload.
#
ERROR_IPSEC_IKE_PROCESS_ERR_NATOA = 13893

#
# MessageId: ERROR_IPSEC_IKE_INVALID_MM_FOR_QM
#
# MessageText:
#
# Parameters of the main mode are invalid for this quick mode.
#
ERROR_IPSEC_IKE_INVALID_MM_FOR_QM = 13894

#
# MessageId: ERROR_IPSEC_IKE_QM_EXPIRED
#
# MessageText:
#
# Quick mode SA was expired by IPsec driver.
#
ERROR_IPSEC_IKE_QM_EXPIRED = 13895

#
# MessageId: ERROR_IPSEC_IKE_TOO_MANY_FILTERS
#
# MessageText:
#
# Too many dynamically added IKEEXT filters were detected.
#
ERROR_IPSEC_IKE_TOO_MANY_FILTERS = 13896

# Do NOT change this final value.  It is used in a public API structure
#
# MessageId: ERROR_IPSEC_IKE_NEG_STATUS_END
#
# MessageText:
#
#  ERROR_IPSEC_IKE_NEG_STATUS_END
#
ERROR_IPSEC_IKE_NEG_STATUS_END = 13897

#
# MessageId: ERROR_IPSEC_IKE_KILL_DUMMY_NAP_TUNNEL
#
# MessageText:
#
# NAP reauth succeeded and must delete the dummy NAP IKEv2 tunnel.
#
ERROR_IPSEC_IKE_KILL_DUMMY_NAP_TUNNEL = 13898

#
# MessageId: ERROR_IPSEC_IKE_INNER_IP_ASSIGNMENT_FAILURE
#
# MessageText:
#
# Error in assigning inner IP address to initiator in tunnel mode.
#
ERROR_IPSEC_IKE_INNER_IP_ASSIGNMENT_FAILURE = 13899

#
# MessageId: ERROR_IPSEC_IKE_REQUIRE_CP_PAYLOAD_MISSING
#
# MessageText:
#
# Require configuration payload missing.
#
ERROR_IPSEC_IKE_REQUIRE_CP_PAYLOAD_MISSING = 13900

#
# MessageId: ERROR_IPSEC_KEY_MODULE_IMPERSONATION_NEGOTIATION_PENDING
#
# MessageText:
#
# A negotiation running as the security principle who issued the connection is in progress
#
ERROR_IPSEC_KEY_MODULE_IMPERSONATION_NEGOTIATION_PENDING = 13901

#
# MessageId: ERROR_IPSEC_IKE_COEXISTENCE_SUPPRESS
#
# MessageText:
#
# SA was deleted due to IKEv1/AuthIP co-existence suppress check.
#
ERROR_IPSEC_IKE_COEXISTENCE_SUPPRESS = 13902

#
# MessageId: ERROR_IPSEC_IKE_RATELIMIT_DROP
#
# MessageText:
#
# Incoming SA request was dropped due to peer IP address rate limiting.
#
ERROR_IPSEC_IKE_RATELIMIT_DROP = 13903

#
# MessageId: ERROR_IPSEC_IKE_PEER_DOESNT_SUPPORT_MOBIKE
#
# MessageText:
#
# Peer does not support MOBIKE.
#
ERROR_IPSEC_IKE_PEER_DOESNT_SUPPORT_MOBIKE = 13904

#
# MessageId: ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE
#
# MessageText:
#
# SA establishment is not authorized.
#
ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE = 13905

#
# MessageId: ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_FAILURE
#
# MessageText:
#
# SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential.
#
ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_FAILURE = 13906

#
# MessageId: ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE_WITH_OPTIONAL_RETRY
#
# MessageText:
#
# SA establishment is not authorized.  You may need to enter updated or different credentials such as a smartcard.
#
ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE_WITH_OPTIONAL_RETRY = 13907

#
# MessageId: ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_AND_CERTMAP_FAILURE
#
# MessageText:
#
# SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential. This might be related to certificate-to-account mapping failure for the SA.
#
ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_AND_CERTMAP_FAILURE = 13908

# Extended upper bound for IKE errors to accomodate new errors
#
# MessageId: ERROR_IPSEC_IKE_NEG_STATUS_EXTENDED_END
#
# MessageText:
#
#  ERROR_IPSEC_IKE_NEG_STATUS_EXTENDED_END
#
ERROR_IPSEC_IKE_NEG_STATUS_EXTENDED_END = 13909

#
# Following error codes are returned by IPsec kernel.
#
#
# MessageId: ERROR_IPSEC_BAD_SPI
#
# MessageText:
#
# The SPI in the packet does not match a valid IPsec SA.
#
ERROR_IPSEC_BAD_SPI = 13910

#
# MessageId: ERROR_IPSEC_SA_LIFETIME_EXPIRED
#
# MessageText:
#
# Packet was received on an IPsec SA whose lifetime has expired.
#
ERROR_IPSEC_SA_LIFETIME_EXPIRED = 13911

#
# MessageId: ERROR_IPSEC_WRONG_SA
#
# MessageText:
#
# Packet was received on an IPsec SA that does not match the packet characteristics.
#
ERROR_IPSEC_WRONG_SA = 13912

#
# MessageId: ERROR_IPSEC_REPLAY_CHECK_FAILED
#
# MessageText:
#
# Packet sequence number replay check failed.
#
ERROR_IPSEC_REPLAY_CHECK_FAILED = 13913

#
# MessageId: ERROR_IPSEC_INVALID_PACKET
#
# MessageText:
#
# IPsec header and/or trailer in the packet is invalid.
#
ERROR_IPSEC_INVALID_PACKET = 13914

#
# MessageId: ERROR_IPSEC_INTEGRITY_CHECK_FAILED
#
# MessageText:
#
# IPsec integrity check failed.
#
ERROR_IPSEC_INTEGRITY_CHECK_FAILED = 13915

#
# MessageId: ERROR_IPSEC_CLEAR_TEXT_DROP
#
# MessageText:
#
# IPsec dropped a clear text packet.
#
ERROR_IPSEC_CLEAR_TEXT_DROP = 13916

#
# MessageId: ERROR_IPSEC_AUTH_FIREWALL_DROP
#
# MessageText:
#
# IPsec dropped an incoming ESP packet in authenticated firewall mode. This drop is benign.
#
ERROR_IPSEC_AUTH_FIREWALL_DROP = 13917

#
# MessageId: ERROR_IPSEC_THROTTLE_DROP
#
# MessageText:
#
# IPsec dropped a packet due to DoS throttling.
#
ERROR_IPSEC_THROTTLE_DROP = 13918

#
# MessageId: ERROR_IPSEC_DOSP_BLOCK
#
# MessageText:
#
# IPsec DoS Protection matched an explicit block rule.
#
ERROR_IPSEC_DOSP_BLOCK = 13925

#
# MessageId: ERROR_IPSEC_DOSP_RECEIVED_MULTICAST
#
# MessageText:
#
# IPsec DoS Protection received an IPsec specific multicast packet which is not allowed.
#
ERROR_IPSEC_DOSP_RECEIVED_MULTICAST = 13926

#
# MessageId: ERROR_IPSEC_DOSP_INVALID_PACKET
#
# MessageText:
#
# IPsec DoS Protection received an incorrectly formatted packet.
#
ERROR_IPSEC_DOSP_INVALID_PACKET = 13927

#
# MessageId: ERROR_IPSEC_DOSP_STATE_LOOKUP_FAILED
#
# MessageText:
#
# IPsec DoS Protection failed to look up state.
#
ERROR_IPSEC_DOSP_STATE_LOOKUP_FAILED = 13928

#
# MessageId: ERROR_IPSEC_DOSP_MAX_ENTRIES
#
# MessageText:
#
# IPsec DoS Protection failed to create state because the maximum number of entries allowed by policy has been reached.
#
ERROR_IPSEC_DOSP_MAX_ENTRIES = 13929

#
# MessageId: ERROR_IPSEC_DOSP_KEYMOD_NOT_ALLOWED
#
# MessageText:
#
# IPsec DoS Protection received an IPsec negotiation packet for a keying module which is not allowed by policy.
#
ERROR_IPSEC_DOSP_KEYMOD_NOT_ALLOWED = 13930

#
# MessageId: ERROR_IPSEC_DOSP_NOT_INSTALLED
#
# MessageText:
#
# IPsec DoS Protection has not been enabled.
#
ERROR_IPSEC_DOSP_NOT_INSTALLED = 13931

#
# MessageId: ERROR_IPSEC_DOSP_MAX_PER_IP_RATELIMIT_QUEUES
#
# MessageText:
#
# IPsec DoS Protection failed to create a per internal IP rate limit queue because the maximum number of queues allowed by policy has been reached.
#
ERROR_IPSEC_DOSP_MAX_PER_IP_RATELIMIT_QUEUES = 13932


#/////////////////////////////////////////////////
#                                               //
#           End of IPSec Error codes            //
#                                               //
#                 13000 to 13999                //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#         Start of Side By Side Error Codes     //
#                                               //
#                 14000 to 14999                //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_SXS_SECTION_NOT_FOUND
#
# MessageText:
#
# The requested section was not present in the activation context.
#
ERROR_SXS_SECTION_NOT_FOUND = 14000

#
# MessageId: ERROR_SXS_CANT_GEN_ACTCTX
#
# MessageText:
#
# The application has failed to start because its side-by-side configuration is incorrect. Please see the application event log or use the command-line sxstrace.exe tool for more detail.
#
ERROR_SXS_CANT_GEN_ACTCTX = 14001

#
# MessageId: ERROR_SXS_INVALID_ACTCTXDATA_FORMAT
#
# MessageText:
#
# The application binding data format is invalid.
#
ERROR_SXS_INVALID_ACTCTXDATA_FORMAT = 14002

#
# MessageId: ERROR_SXS_ASSEMBLY_NOT_FOUND
#
# MessageText:
#
# The referenced assembly is not installed on your system.
#
ERROR_SXS_ASSEMBLY_NOT_FOUND = 14003

#
# MessageId: ERROR_SXS_MANIFEST_FORMAT_ERROR
#
# MessageText:
#
# The manifest file does not begin with the required tag and format information.
#
ERROR_SXS_MANIFEST_FORMAT_ERROR = 14004

#
# MessageId: ERROR_SXS_MANIFEST_PARSE_ERROR
#
# MessageText:
#
# The manifest file contains one or more syntax errors.
#
ERROR_SXS_MANIFEST_PARSE_ERROR = 14005

#
# MessageId: ERROR_SXS_ACTIVATION_CONTEXT_DISABLED
#
# MessageText:
#
# The application attempted to activate a disabled activation context.
#
ERROR_SXS_ACTIVATION_CONTEXT_DISABLED = 14006

#
# MessageId: ERROR_SXS_KEY_NOT_FOUND
#
# MessageText:
#
# The requested lookup key was not found in any active activation context.
#
ERROR_SXS_KEY_NOT_FOUND = 14007

#
# MessageId: ERROR_SXS_VERSION_CONFLICT
#
# MessageText:
#
# A component version required by the application conflicts with another component version already active.
#
ERROR_SXS_VERSION_CONFLICT = 14008

#
# MessageId: ERROR_SXS_WRONG_SECTION_TYPE
#
# MessageText:
#
# The type requested activation context section does not match the query API used.
#
ERROR_SXS_WRONG_SECTION_TYPE = 14009

#
# MessageId: ERROR_SXS_THREAD_QUERIES_DISABLED
#
# MessageText:
#
# Lack of system resources has required isolated activation to be disabled for the current thread of execution.
#
ERROR_SXS_THREAD_QUERIES_DISABLED = 14010

#
# MessageId: ERROR_SXS_PROCESS_DEFAULT_ALREADY_SET
#
# MessageText:
#
# An attempt to set the process default activation context failed because the process default activation context was already set.
#
ERROR_SXS_PROCESS_DEFAULT_ALREADY_SET = 14011

#
# MessageId: ERROR_SXS_UNKNOWN_ENCODING_GROUP
#
# MessageText:
#
# The encoding group identifier specified is not recognized.
#
ERROR_SXS_UNKNOWN_ENCODING_GROUP = 14012

#
# MessageId: ERROR_SXS_UNKNOWN_ENCODING
#
# MessageText:
#
# The encoding requested is not recognized.
#
ERROR_SXS_UNKNOWN_ENCODING = 14013

#
# MessageId: ERROR_SXS_INVALID_XML_NAMESPACE_URI
#
# MessageText:
#
# The manifest contains a reference to an invalid URI.
#
ERROR_SXS_INVALID_XML_NAMESPACE_URI = 14014

#
# MessageId: ERROR_SXS_ROOT_MANIFEST_DEPENDENCY_NOT_INSTALLED
#
# MessageText:
#
# The application manifest contains a reference to a dependent assembly which is not installed
#
ERROR_SXS_ROOT_MANIFEST_DEPENDENCY_NOT_INSTALLED = 14015

#
# MessageId: ERROR_SXS_LEAF_MANIFEST_DEPENDENCY_NOT_INSTALLED
#
# MessageText:
#
# The manifest for an assembly used by the application has a reference to a dependent assembly which is not installed
#
ERROR_SXS_LEAF_MANIFEST_DEPENDENCY_NOT_INSTALLED = 14016

#
# MessageId: ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE
#
# MessageText:
#
# The manifest contains an attribute for the assembly identity which is not valid.
#
ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE = 14017

#
# MessageId: ERROR_SXS_MANIFEST_MISSING_REQUIRED_DEFAULT_NAMESPACE
#
# MessageText:
#
# The manifest is missing the required default namespace specification on the assembly element.
#
ERROR_SXS_MANIFEST_MISSING_REQUIRED_DEFAULT_NAMESPACE = 14018

#
# MessageId: ERROR_SXS_MANIFEST_INVALID_REQUIRED_DEFAULT_NAMESPACE
#
# MessageText:
#
# The manifest has a default namespace specified on the assembly element but its value is not "urn:schemas-microsoft-com:asm.v1".
#
ERROR_SXS_MANIFEST_INVALID_REQUIRED_DEFAULT_NAMESPACE = 14019

#
# MessageId: ERROR_SXS_PRIVATE_MANIFEST_CROSS_PATH_WITH_REPARSE_POINT
#
# MessageText:
#
# The private manifest probed has crossed a path with an unsupported reparse point.
#
ERROR_SXS_PRIVATE_MANIFEST_CROSS_PATH_WITH_REPARSE_POINT = 14020

#
# MessageId: ERROR_SXS_DUPLICATE_DLL_NAME
#
# MessageText:
#
# Two or more components referenced directly or indirectly by the application manifest have files by the same name.
#
ERROR_SXS_DUPLICATE_DLL_NAME = 14021

#
# MessageId: ERROR_SXS_DUPLICATE_WINDOWCLASS_NAME
#
# MessageText:
#
# Two or more components referenced directly or indirectly by the application manifest have window classes with the same name.
#
ERROR_SXS_DUPLICATE_WINDOWCLASS_NAME = 14022

#
# MessageId: ERROR_SXS_DUPLICATE_CLSID
#
# MessageText:
#
# Two or more components referenced directly or indirectly by the application manifest have the same COM server CLSIDs.
#
ERROR_SXS_DUPLICATE_CLSID = 14023

#
# MessageId: ERROR_SXS_DUPLICATE_IID
#
# MessageText:
#
# Two or more components referenced directly or indirectly by the application manifest have proxies for the same COM interface IIDs.
#
ERROR_SXS_DUPLICATE_IID = 14024

#
# MessageId: ERROR_SXS_DUPLICATE_TLBID
#
# MessageText:
#
# Two or more components referenced directly or indirectly by the application manifest have the same COM type library TLBIDs.
#
ERROR_SXS_DUPLICATE_TLBID = 14025

#
# MessageId: ERROR_SXS_DUPLICATE_PROGID
#
# MessageText:
#
# Two or more components referenced directly or indirectly by the application manifest have the same COM ProgIDs.
#
ERROR_SXS_DUPLICATE_PROGID = 14026

#
# MessageId: ERROR_SXS_DUPLICATE_ASSEMBLY_NAME
#
# MessageText:
#
# Two or more components referenced directly or indirectly by the application manifest are different versions of the same component which is not permitted.
#
ERROR_SXS_DUPLICATE_ASSEMBLY_NAME = 14027

#
# MessageId: ERROR_SXS_FILE_HASH_MISMATCH
#
# MessageText:
#
# A component's file does not match the verification information present in the component manifest.
#
ERROR_SXS_FILE_HASH_MISMATCH = 14028

#
# MessageId: ERROR_SXS_POLICY_PARSE_ERROR
#
# MessageText:
#
# The policy manifest contains one or more syntax errors.
#
ERROR_SXS_POLICY_PARSE_ERROR = 14029

#
# MessageId: ERROR_SXS_XML_E_MISSINGQUOTE
#
# MessageText:
#
# Manifest Parse Error : A string literal was expected, but no opening quote character was found.
#
ERROR_SXS_XML_E_MISSINGQUOTE = 14030

#
# MessageId: ERROR_SXS_XML_E_COMMENTSYNTAX
#
# MessageText:
#
# Manifest Parse Error : Incorrect syntax was used in a comment.
#
ERROR_SXS_XML_E_COMMENTSYNTAX = 14031

#
# MessageId: ERROR_SXS_XML_E_BADSTARTNAMECHAR
#
# MessageText:
#
# Manifest Parse Error : A name was started with an invalid character.
#
ERROR_SXS_XML_E_BADSTARTNAMECHAR = 14032

#
# MessageId: ERROR_SXS_XML_E_BADNAMECHAR
#
# MessageText:
#
# Manifest Parse Error : A name contained an invalid character.
#
ERROR_SXS_XML_E_BADNAMECHAR = 14033

#
# MessageId: ERROR_SXS_XML_E_BADCHARINSTRING
#
# MessageText:
#
# Manifest Parse Error : A string literal contained an invalid character.
#
ERROR_SXS_XML_E_BADCHARINSTRING = 14034

#
# MessageId: ERROR_SXS_XML_E_XMLDECLSYNTAX
#
# MessageText:
#
# Manifest Parse Error : Invalid syntax for an xml declaration.
#
ERROR_SXS_XML_E_XMLDECLSYNTAX = 14035

#
# MessageId: ERROR_SXS_XML_E_BADCHARDATA
#
# MessageText:
#
# Manifest Parse Error : An Invalid character was found in text content.
#
ERROR_SXS_XML_E_BADCHARDATA = 14036

#
# MessageId: ERROR_SXS_XML_E_MISSINGWHITESPACE
#
# MessageText:
#
# Manifest Parse Error : Required white space was missing.
#
ERROR_SXS_XML_E_MISSINGWHITESPACE = 14037

#
# MessageId: ERROR_SXS_XML_E_EXPECTINGTAGEND
#
# MessageText:
#
# Manifest Parse Error : The character '>' was expected.
#
ERROR_SXS_XML_E_EXPECTINGTAGEND = 14038

#
# MessageId: ERROR_SXS_XML_E_MISSINGSEMICOLON
#
# MessageText:
#
# Manifest Parse Error : A semi colon character was expected.
#
ERROR_SXS_XML_E_MISSINGSEMICOLON = 14039

#
# MessageId: ERROR_SXS_XML_E_UNBALANCEDPAREN
#
# MessageText:
#
# Manifest Parse Error : Unbalanced parentheses.
#
ERROR_SXS_XML_E_UNBALANCEDPAREN = 14040

#
# MessageId: ERROR_SXS_XML_E_INTERNALERROR
#
# MessageText:
#
# Manifest Parse Error : Internal error.
#
ERROR_SXS_XML_E_INTERNALERROR = 14041

#
# MessageId: ERROR_SXS_XML_E_UNEXPECTED_WHITESPACE
#
# MessageText:
#
# Manifest Parse Error : Whitespace is not allowed at this location.
#
ERROR_SXS_XML_E_UNEXPECTED_WHITESPACE = 14042

#
# MessageId: ERROR_SXS_XML_E_INCOMPLETE_ENCODING
#
# MessageText:
#
# Manifest Parse Error : End of file reached in invalid state for current encoding.
#
ERROR_SXS_XML_E_INCOMPLETE_ENCODING = 14043

#
# MessageId: ERROR_SXS_XML_E_MISSING_PAREN
#
# MessageText:
#
# Manifest Parse Error : Missing parenthesis.
#
ERROR_SXS_XML_E_MISSING_PAREN = 14044

#
# MessageId: ERROR_SXS_XML_E_EXPECTINGCLOSEQUOTE
#
# MessageText:
#
# Manifest Parse Error : A single or double closing quote character (\' or \") is missing.
#
ERROR_SXS_XML_E_EXPECTINGCLOSEQUOTE = 14045

#
# MessageId: ERROR_SXS_XML_E_MULTIPLE_COLONS
#
# MessageText:
#
# Manifest Parse Error : Multiple colons are not allowed in a name.
#
ERROR_SXS_XML_E_MULTIPLE_COLONS = 14046

#
# MessageId: ERROR_SXS_XML_E_INVALID_DECIMAL
#
# MessageText:
#
# Manifest Parse Error : Invalid character for decimal digit.
#
ERROR_SXS_XML_E_INVALID_DECIMAL = 14047

#
# MessageId: ERROR_SXS_XML_E_INVALID_HEXIDECIMAL
#
# MessageText:
#
# Manifest Parse Error : Invalid character for hexadecimal digit.
#
ERROR_SXS_XML_E_INVALID_HEXIDECIMAL = 14048

#
# MessageId: ERROR_SXS_XML_E_INVALID_UNICODE
#
# MessageText:
#
# Manifest Parse Error : Invalid unicode character value for this platform.
#
ERROR_SXS_XML_E_INVALID_UNICODE = 14049

#
# MessageId: ERROR_SXS_XML_E_WHITESPACEORQUESTIONMARK
#
# MessageText:
#
# Manifest Parse Error : Expecting whitespace or '?'.
#
ERROR_SXS_XML_E_WHITESPACEORQUESTIONMARK = 14050

#
# MessageId: ERROR_SXS_XML_E_UNEXPECTEDENDTAG
#
# MessageText:
#
# Manifest Parse Error : End tag was not expected at this location.
#
ERROR_SXS_XML_E_UNEXPECTEDENDTAG = 14051

#
# MessageId: ERROR_SXS_XML_E_UNCLOSEDTAG
#
# MessageText:
#
# Manifest Parse Error : The following tags were not closed: %1.
#
ERROR_SXS_XML_E_UNCLOSEDTAG = 14052

#
# MessageId: ERROR_SXS_XML_E_DUPLICATEATTRIBUTE
#
# MessageText:
#
# Manifest Parse Error : Duplicate attribute.
#
ERROR_SXS_XML_E_DUPLICATEATTRIBUTE = 14053

#
# MessageId: ERROR_SXS_XML_E_MULTIPLEROOTS
#
# MessageText:
#
# Manifest Parse Error : Only one top level element is allowed in an XML document.
#
ERROR_SXS_XML_E_MULTIPLEROOTS = 14054

#
# MessageId: ERROR_SXS_XML_E_INVALIDATROOTLEVEL
#
# MessageText:
#
# Manifest Parse Error : Invalid at the top level of the document.
#
ERROR_SXS_XML_E_INVALIDATROOTLEVEL = 14055

#
# MessageId: ERROR_SXS_XML_E_BADXMLDECL
#
# MessageText:
#
# Manifest Parse Error : Invalid xml declaration.
#
ERROR_SXS_XML_E_BADXMLDECL = 14056

#
# MessageId: ERROR_SXS_XML_E_MISSINGROOT
#
# MessageText:
#
# Manifest Parse Error : XML document must have a top level element.
#
ERROR_SXS_XML_E_MISSINGROOT = 14057

#
# MessageId: ERROR_SXS_XML_E_UNEXPECTEDEOF
#
# MessageText:
#
# Manifest Parse Error : Unexpected end of file.
#
ERROR_SXS_XML_E_UNEXPECTEDEOF = 14058

#
# MessageId: ERROR_SXS_XML_E_BADPEREFINSUBSET
#
# MessageText:
#
# Manifest Parse Error : Parameter entities cannot be used inside markup declarations in an internal subset.
#
ERROR_SXS_XML_E_BADPEREFINSUBSET = 14059

#
# MessageId: ERROR_SXS_XML_E_UNCLOSEDSTARTTAG
#
# MessageText:
#
# Manifest Parse Error : Element was not closed.
#
ERROR_SXS_XML_E_UNCLOSEDSTARTTAG = 14060

#
# MessageId: ERROR_SXS_XML_E_UNCLOSEDENDTAG
#
# MessageText:
#
# Manifest Parse Error : End element was missing the character '>'.
#
ERROR_SXS_XML_E_UNCLOSEDENDTAG = 14061

#
# MessageId: ERROR_SXS_XML_E_UNCLOSEDSTRING
#
# MessageText:
#
# Manifest Parse Error : A string literal was not closed.
#
ERROR_SXS_XML_E_UNCLOSEDSTRING = 14062

#
# MessageId: ERROR_SXS_XML_E_UNCLOSEDCOMMENT
#
# MessageText:
#
# Manifest Parse Error : A comment was not closed.
#
ERROR_SXS_XML_E_UNCLOSEDCOMMENT = 14063

#
# MessageId: ERROR_SXS_XML_E_UNCLOSEDDECL
#
# MessageText:
#
# Manifest Parse Error : A declaration was not closed.
#
ERROR_SXS_XML_E_UNCLOSEDDECL = 14064

#
# MessageId: ERROR_SXS_XML_E_UNCLOSEDCDATA
#
# MessageText:
#
# Manifest Parse Error : A CDATA section was not closed.
#
ERROR_SXS_XML_E_UNCLOSEDCDATA = 14065

#
# MessageId: ERROR_SXS_XML_E_RESERVEDNAMESPACE
#
# MessageText:
#
# Manifest Parse Error : The namespace prefix is not allowed to start with the reserved string "xml".
#
ERROR_SXS_XML_E_RESERVEDNAMESPACE = 14066

#
# MessageId: ERROR_SXS_XML_E_INVALIDENCODING
#
# MessageText:
#
# Manifest Parse Error : System does not support the specified encoding.
#
ERROR_SXS_XML_E_INVALIDENCODING = 14067

#
# MessageId: ERROR_SXS_XML_E_INVALIDSWITCH
#
# MessageText:
#
# Manifest Parse Error : Switch from current encoding to specified encoding not supported.
#
ERROR_SXS_XML_E_INVALIDSWITCH = 14068

#
# MessageId: ERROR_SXS_XML_E_BADXMLCASE
#
# MessageText:
#
# Manifest Parse Error : The name 'xml' is reserved and must be lower case.
#
ERROR_SXS_XML_E_BADXMLCASE = 14069

#
# MessageId: ERROR_SXS_XML_E_INVALID_STANDALONE
#
# MessageText:
#
# Manifest Parse Error : The standalone attribute must have the value 'yes' or 'no'.
#
ERROR_SXS_XML_E_INVALID_STANDALONE = 14070

#
# MessageId: ERROR_SXS_XML_E_UNEXPECTED_STANDALONE
#
# MessageText:
#
# Manifest Parse Error : The standalone attribute cannot be used in external entities.
#
ERROR_SXS_XML_E_UNEXPECTED_STANDALONE = 14071

#
# MessageId: ERROR_SXS_XML_E_INVALID_VERSION
#
# MessageText:
#
# Manifest Parse Error : Invalid version number.
#
ERROR_SXS_XML_E_INVALID_VERSION = 14072

#
# MessageId: ERROR_SXS_XML_E_MISSINGEQUALS
#
# MessageText:
#
# Manifest Parse Error : Missing equals sign between attribute and attribute value.
#
ERROR_SXS_XML_E_MISSINGEQUALS = 14073

#
# MessageId: ERROR_SXS_PROTECTION_RECOVERY_FAILED
#
# MessageText:
#
# Assembly Protection Error : Unable to recover the specified assembly.
#
ERROR_SXS_PROTECTION_RECOVERY_FAILED = 14074

#
# MessageId: ERROR_SXS_PROTECTION_PUBLIC_KEY_TOO_SHORT
#
# MessageText:
#
# Assembly Protection Error : The public key for an assembly was too short to be allowed.
#
ERROR_SXS_PROTECTION_PUBLIC_KEY_TOO_SHORT = 14075

#
# MessageId: ERROR_SXS_PROTECTION_CATALOG_NOT_VALID
#
# MessageText:
#
# Assembly Protection Error : The catalog for an assembly is not valid, or does not match the assembly's manifest.
#
ERROR_SXS_PROTECTION_CATALOG_NOT_VALID = 14076

#
# MessageId: ERROR_SXS_UNTRANSLATABLE_HRESULT
#
# MessageText:
#
# An HRESULT could not be translated to a corresponding Win32 error code.
#
ERROR_SXS_UNTRANSLATABLE_HRESULT = 14077

#
# MessageId: ERROR_SXS_PROTECTION_CATALOG_FILE_MISSING
#
# MessageText:
#
# Assembly Protection Error : The catalog for an assembly is missing.
#
ERROR_SXS_PROTECTION_CATALOG_FILE_MISSING = 14078

#
# MessageId: ERROR_SXS_MISSING_ASSEMBLY_IDENTITY_ATTRIBUTE
#
# MessageText:
#
# The supplied assembly identity is missing one or more attributes which must be present in this context.
#
ERROR_SXS_MISSING_ASSEMBLY_IDENTITY_ATTRIBUTE = 14079

#
# MessageId: ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE_NAME
#
# MessageText:
#
# The supplied assembly identity has one or more attribute names that contain characters not permitted in XML names.
#
ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE_NAME = 14080

#
# MessageId: ERROR_SXS_ASSEMBLY_MISSING
#
# MessageText:
#
# The referenced assembly could not be found.
#
ERROR_SXS_ASSEMBLY_MISSING = 14081

#
# MessageId: ERROR_SXS_CORRUPT_ACTIVATION_STACK
#
# MessageText:
#
# The activation context activation stack for the running thread of execution is corrupt.
#
ERROR_SXS_CORRUPT_ACTIVATION_STACK = 14082

#
# MessageId: ERROR_SXS_CORRUPTION
#
# MessageText:
#
# The application isolation metadata for this process or thread has become corrupt.
#
ERROR_SXS_CORRUPTION = 14083

#
# MessageId: ERROR_SXS_EARLY_DEACTIVATION
#
# MessageText:
#
# The activation context being deactivated is not the most recently activated one.
#
ERROR_SXS_EARLY_DEACTIVATION = 14084

#
# MessageId: ERROR_SXS_INVALID_DEACTIVATION
#
# MessageText:
#
# The activation context being deactivated is not active for the current thread of execution.
#
ERROR_SXS_INVALID_DEACTIVATION = 14085

#
# MessageId: ERROR_SXS_MULTIPLE_DEACTIVATION
#
# MessageText:
#
# The activation context being deactivated has already been deactivated.
#
ERROR_SXS_MULTIPLE_DEACTIVATION = 14086

#
# MessageId: ERROR_SXS_PROCESS_TERMINATION_REQUESTED
#
# MessageText:
#
# A component used by the isolation facility has requested to terminate the process.
#
ERROR_SXS_PROCESS_TERMINATION_REQUESTED = 14087

#
# MessageId: ERROR_SXS_RELEASE_ACTIVATION_CONTEXT
#
# MessageText:
#
# A kernel mode component is releasing a reference on an activation context.
#
ERROR_SXS_RELEASE_ACTIVATION_CONTEXT = 14088

#
# MessageId: ERROR_SXS_SYSTEM_DEFAULT_ACTIVATION_CONTEXT_EMPTY
#
# MessageText:
#
# The activation context of system default assembly could not be generated.
#
ERROR_SXS_SYSTEM_DEFAULT_ACTIVATION_CONTEXT_EMPTY = 14089

#
# MessageId: ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_VALUE
#
# MessageText:
#
# The value of an attribute in an identity is not within the legal range.
#
ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_VALUE = 14090

#
# MessageId: ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_NAME
#
# MessageText:
#
# The name of an attribute in an identity is not within the legal range.
#
ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_NAME = 14091

#
# MessageId: ERROR_SXS_IDENTITY_DUPLICATE_ATTRIBUTE
#
# MessageText:
#
# An identity contains two definitions for the same attribute.
#
ERROR_SXS_IDENTITY_DUPLICATE_ATTRIBUTE = 14092

#
# MessageId: ERROR_SXS_IDENTITY_PARSE_ERROR
#
# MessageText:
#
# The identity string is malformed. This may be due to a trailing comma, more than two unnamed attributes, missing attribute name or missing attribute value.
#
ERROR_SXS_IDENTITY_PARSE_ERROR = 14093

#
# MessageId: ERROR_MALFORMED_SUBSTITUTION_STRING
#
# MessageText:
#
# A string containing localized substitutable content was malformed. Either a dollar sign ($) was followed by something other than a left parenthesis or another dollar sign or an substitution's right parenthesis was not found.
#
ERROR_MALFORMED_SUBSTITUTION_STRING = 14094

#
# MessageId: ERROR_SXS_INCORRECT_PUBLIC_KEY_TOKEN
#
# MessageText:
#
# The public key token does not correspond to the public key specified.
#
ERROR_SXS_INCORRECT_PUBLIC_KEY_TOKEN = 14095

#
# MessageId: ERROR_UNMAPPED_SUBSTITUTION_STRING
#
# MessageText:
#
# A substitution string had no mapping.
#
ERROR_UNMAPPED_SUBSTITUTION_STRING = 14096

#
# MessageId: ERROR_SXS_ASSEMBLY_NOT_LOCKED
#
# MessageText:
#
# The component must be locked before making the request.
#
ERROR_SXS_ASSEMBLY_NOT_LOCKED = 14097

#
# MessageId: ERROR_SXS_COMPONENT_STORE_CORRUPT
#
# MessageText:
#
# The component store has been corrupted.
#
ERROR_SXS_COMPONENT_STORE_CORRUPT = 14098

#
# MessageId: ERROR_ADVANCED_INSTALLER_FAILED
#
# MessageText:
#
# An advanced installer failed during setup or servicing.
#
ERROR_ADVANCED_INSTALLER_FAILED = 14099

#
# MessageId: ERROR_XML_ENCODING_MISMATCH
#
# MessageText:
#
# The character encoding in the XML declaration did not match the encoding used in the document.
#
ERROR_XML_ENCODING_MISMATCH = 14100

#
# MessageId: ERROR_SXS_MANIFEST_IDENTITY_SAME_BUT_CONTENTS_DIFFERENT
#
# MessageText:
#
# The identities of the manifests are identical but their contents are different.
#
ERROR_SXS_MANIFEST_IDENTITY_SAME_BUT_CONTENTS_DIFFERENT = 14101

#
# MessageId: ERROR_SXS_IDENTITIES_DIFFERENT
#
# MessageText:
#
# The component identities are different.
#
ERROR_SXS_IDENTITIES_DIFFERENT = 14102

#
# MessageId: ERROR_SXS_ASSEMBLY_IS_NOT_A_DEPLOYMENT
#
# MessageText:
#
# The assembly is not a deployment.
#
ERROR_SXS_ASSEMBLY_IS_NOT_A_DEPLOYMENT = 14103

#
# MessageId: ERROR_SXS_FILE_NOT_PART_OF_ASSEMBLY
#
# MessageText:
#
# The file is not a part of the assembly.
#
ERROR_SXS_FILE_NOT_PART_OF_ASSEMBLY = 14104

#
# MessageId: ERROR_SXS_MANIFEST_TOO_BIG
#
# MessageText:
#
# The size of the manifest exceeds the maximum allowed.
#
ERROR_SXS_MANIFEST_TOO_BIG = 14105

#
# MessageId: ERROR_SXS_SETTING_NOT_REGISTERED
#
# MessageText:
#
# The setting is not registered.
#
ERROR_SXS_SETTING_NOT_REGISTERED = 14106

#
# MessageId: ERROR_SXS_TRANSACTION_CLOSURE_INCOMPLETE
#
# MessageText:
#
# One or more required members of the transaction are not present.
#
ERROR_SXS_TRANSACTION_CLOSURE_INCOMPLETE = 14107

#
# MessageId: ERROR_SMI_PRIMITIVE_INSTALLER_FAILED
#
# MessageText:
#
# The SMI primitive installer failed during setup or servicing.
#
ERROR_SMI_PRIMITIVE_INSTALLER_FAILED = 14108

#
# MessageId: ERROR_GENERIC_COMMAND_FAILED
#
# MessageText:
#
# A generic command executable returned a result that indicates failure.
#
ERROR_GENERIC_COMMAND_FAILED = 14109

#
# MessageId: ERROR_SXS_FILE_HASH_MISSING
#
# MessageText:
#
# A component is missing file verification information in its manifest.
#
ERROR_SXS_FILE_HASH_MISSING = 14110


#/////////////////////////////////////////////////
#                                               //
#           End of Side By Side Error Codes     //
#                                               //
#                 14000 to 14999                //
#/////////////////////////////////////////////////


#/////////////////////////////////////////////////
#                                               //
#           Start of WinEvt Error codes         //
#                                               //
#                 15000 to 15079                //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_EVT_INVALID_CHANNEL_PATH
#
# MessageText:
#
# The specified channel path is invalid.
#
ERROR_EVT_INVALID_CHANNEL_PATH = 15000

#
# MessageId: ERROR_EVT_INVALID_QUERY
#
# MessageText:
#
# The specified query is invalid.
#
ERROR_EVT_INVALID_QUERY = 15001

#
# MessageId: ERROR_EVT_PUBLISHER_METADATA_NOT_FOUND
#
# MessageText:
#
# The publisher metadata cannot be found in the resource.
#
ERROR_EVT_PUBLISHER_METADATA_NOT_FOUND = 15002

#
# MessageId: ERROR_EVT_EVENT_TEMPLATE_NOT_FOUND
#
# MessageText:
#
# The template for an event definition cannot be found in the resource (error = %1).
#
ERROR_EVT_EVENT_TEMPLATE_NOT_FOUND = 15003

#
# MessageId: ERROR_EVT_INVALID_PUBLISHER_NAME
#
# MessageText:
#
# The specified publisher name is invalid.
#
ERROR_EVT_INVALID_PUBLISHER_NAME = 15004

#
# MessageId: ERROR_EVT_INVALID_EVENT_DATA
#
# MessageText:
#
# The event data raised by the publisher is not compatible with the event template definition in the publisher's manifest
#
ERROR_EVT_INVALID_EVENT_DATA = 15005

#
# MessageId: ERROR_EVT_CHANNEL_NOT_FOUND
#
# MessageText:
#
# The specified channel could not be found. Check channel configuration.
#
ERROR_EVT_CHANNEL_NOT_FOUND = 15007

#
# MessageId: ERROR_EVT_MALFORMED_XML_TEXT
#
# MessageText:
#
# The specified xml text was not well-formed. See Extended Error for more details.
#
ERROR_EVT_MALFORMED_XML_TEXT = 15008

#
# MessageId: ERROR_EVT_SUBSCRIPTION_TO_DIRECT_CHANNEL
#
# MessageText:
#
# The caller is trying to subscribe to a direct channel which is not allowed. The events for a direct channel go directly to a logfile and cannot be subscribed to.
#
ERROR_EVT_SUBSCRIPTION_TO_DIRECT_CHANNEL = 15009

#
# MessageId: ERROR_EVT_CONFIGURATION_ERROR
#
# MessageText:
#
# Configuration error.
#
ERROR_EVT_CONFIGURATION_ERROR = 15010

#
# MessageId: ERROR_EVT_QUERY_RESULT_STALE
#
# MessageText:
#
# The query result is stale / invalid. This may be due to the log being cleared or rolling over after the query result was created. Users should handle this code by releasing the query result object and reissuing the query.
#
ERROR_EVT_QUERY_RESULT_STALE = 15011

#
# MessageId: ERROR_EVT_QUERY_RESULT_INVALID_POSITION
#
# MessageText:
#
# Query result is currently at an invalid position.
#
ERROR_EVT_QUERY_RESULT_INVALID_POSITION = 15012

#
# MessageId: ERROR_EVT_NON_VALIDATING_MSXML
#
# MessageText:
#
# Registered MSXML doesn't support validation.
#
ERROR_EVT_NON_VALIDATING_MSXML = 15013

#
# MessageId: ERROR_EVT_FILTER_ALREADYSCOPED
#
# MessageText:
#
# An expression can only be followed by a change of scope operation if it itself evaluates to a node set and is not already part of some other change of scope operation.
#
ERROR_EVT_FILTER_ALREADYSCOPED = 15014

#
# MessageId: ERROR_EVT_FILTER_NOTELTSET
#
# MessageText:
#
# Can't perform a step operation from a term that does not represent an element set.
#
ERROR_EVT_FILTER_NOTELTSET = 15015

#
# MessageId: ERROR_EVT_FILTER_INVARG
#
# MessageText:
#
# Left hand side arguments to binary operators must be either attributes, nodes or variables and right hand side arguments must be constants.
#
ERROR_EVT_FILTER_INVARG = 15016

#
# MessageId: ERROR_EVT_FILTER_INVTEST
#
# MessageText:
#
# A step operation must involve either a node test or, in the case of a predicate, an algebraic expression against which to test each node in the node set identified by the preceeding node set can be evaluated.
#
ERROR_EVT_FILTER_INVTEST = 15017

#
# MessageId: ERROR_EVT_FILTER_INVTYPE
#
# MessageText:
#
# This data type is currently unsupported.
#
ERROR_EVT_FILTER_INVTYPE = 15018

#
# MessageId: ERROR_EVT_FILTER_PARSEERR
#
# MessageText:
#
# A syntax error occurred at position %1!d!
#
ERROR_EVT_FILTER_PARSEERR = 15019

#
# MessageId: ERROR_EVT_FILTER_UNSUPPORTEDOP
#
# MessageText:
#
# This operator is unsupported by this implementation of the filter.
#
ERROR_EVT_FILTER_UNSUPPORTEDOP = 15020

#
# MessageId: ERROR_EVT_FILTER_UNEXPECTEDTOKEN
#
# MessageText:
#
# The token encountered was unexpected.
#
ERROR_EVT_FILTER_UNEXPECTEDTOKEN = 15021

#
# MessageId: ERROR_EVT_INVALID_OPERATION_OVER_ENABLED_DIRECT_CHANNEL
#
# MessageText:
#
# The requested operation cannot be performed over an enabled direct channel. The channel must first be disabled before performing the requested operation.
#
ERROR_EVT_INVALID_OPERATION_OVER_ENABLED_DIRECT_CHANNEL = 15022

#
# MessageId: ERROR_EVT_INVALID_CHANNEL_PROPERTY_VALUE
#
# MessageText:
#
# Channel property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of channel.
#
ERROR_EVT_INVALID_CHANNEL_PROPERTY_VALUE = 15023

#
# MessageId: ERROR_EVT_INVALID_PUBLISHER_PROPERTY_VALUE
#
# MessageText:
#
# Publisher property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of publisher.
#
ERROR_EVT_INVALID_PUBLISHER_PROPERTY_VALUE = 15024

#
# MessageId: ERROR_EVT_CHANNEL_CANNOT_ACTIVATE
#
# MessageText:
#
# The channel fails to activate.
#
ERROR_EVT_CHANNEL_CANNOT_ACTIVATE = 15025

#
# MessageId: ERROR_EVT_FILTER_TOO_COMPLEX
#
# MessageText:
#
# The xpath expression exceeded supported complexity. Please symplify it or split it into two or more simple expressions.
#
ERROR_EVT_FILTER_TOO_COMPLEX = 15026

#
# MessageId: ERROR_EVT_MESSAGE_NOT_FOUND
#
# MessageText:
#
# the message resource is present but the message is not found in the string/message table
#
ERROR_EVT_MESSAGE_NOT_FOUND = 15027

#
# MessageId: ERROR_EVT_MESSAGE_ID_NOT_FOUND
#
# MessageText:
#
# The message id for the desired message could not be found.
#
ERROR_EVT_MESSAGE_ID_NOT_FOUND = 15028

#
# MessageId: ERROR_EVT_UNRESOLVED_VALUE_INSERT
#
# MessageText:
#
# The substitution string for insert index (%1) could not be found.
#
ERROR_EVT_UNRESOLVED_VALUE_INSERT = 15029

#
# MessageId: ERROR_EVT_UNRESOLVED_PARAMETER_INSERT
#
# MessageText:
#
# The description string for parameter reference (%1) could not be found.
#
ERROR_EVT_UNRESOLVED_PARAMETER_INSERT = 15030

#
# MessageId: ERROR_EVT_MAX_INSERTS_REACHED
#
# MessageText:
#
# The maximum number of replacements has been reached.
#
ERROR_EVT_MAX_INSERTS_REACHED = 15031

#
# MessageId: ERROR_EVT_EVENT_DEFINITION_NOT_FOUND
#
# MessageText:
#
# The event definition could not be found for event id (%1).
#
ERROR_EVT_EVENT_DEFINITION_NOT_FOUND = 15032

#
# MessageId: ERROR_EVT_MESSAGE_LOCALE_NOT_FOUND
#
# MessageText:
#
# The locale specific resource for the desired message is not present.
#
ERROR_EVT_MESSAGE_LOCALE_NOT_FOUND = 15033

#
# MessageId: ERROR_EVT_VERSION_TOO_OLD
#
# MessageText:
#
# The resource is too old to be compatible.
#
ERROR_EVT_VERSION_TOO_OLD = 15034

#
# MessageId: ERROR_EVT_VERSION_TOO_NEW
#
# MessageText:
#
# The resource is too new to be compatible.
#
ERROR_EVT_VERSION_TOO_NEW = 15035

#
# MessageId: ERROR_EVT_CANNOT_OPEN_CHANNEL_OF_QUERY
#
# MessageText:
#
# The channel at index %1!d! of the query can't be opened.
#
ERROR_EVT_CANNOT_OPEN_CHANNEL_OF_QUERY = 15036

#
# MessageId: ERROR_EVT_PUBLISHER_DISABLED
#
# MessageText:
#
# The publisher has been disabled and its resource is not available. This usually occurs when the publisher is in the process of being uninstalled or upgraded.
#
ERROR_EVT_PUBLISHER_DISABLED = 15037

#
# MessageId: ERROR_EVT_FILTER_OUT_OF_RANGE
#
# MessageText:
#
# Attempted to create a numeric type that is outside of its valid range.
#
ERROR_EVT_FILTER_OUT_OF_RANGE = 15038


#/////////////////////////////////////////////////
#                                               //
#           Start of Wecsvc Error codes         //
#                                               //
#                 15080 to 15099                //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_EC_SUBSCRIPTION_CANNOT_ACTIVATE
#
# MessageText:
#
# The subscription fails to activate.
#
ERROR_EC_SUBSCRIPTION_CANNOT_ACTIVATE = 15080

#
# MessageId: ERROR_EC_LOG_DISABLED
#
# MessageText:
#
# The log of the subscription is in disabled state, and can not be used to forward events to. The log must first be enabled before the subscription can be activated.
#
ERROR_EC_LOG_DISABLED = 15081

#
# MessageId: ERROR_EC_CIRCULAR_FORWARDING
#
# MessageText:
#
# When forwarding events from local machine to itself, the query of the subscription can't contain target log of the subscription.
#
ERROR_EC_CIRCULAR_FORWARDING = 15082

#
# MessageId: ERROR_EC_CREDSTORE_FULL
#
# MessageText:
#
# The credential store that is used to save credentials is full.
#
ERROR_EC_CREDSTORE_FULL = 15083

#
# MessageId: ERROR_EC_CRED_NOT_FOUND
#
# MessageText:
#
# The credential used by this subscription can't be found in credential store.
#
ERROR_EC_CRED_NOT_FOUND = 15084

#
# MessageId: ERROR_EC_NO_ACTIVE_CHANNEL
#
# MessageText:
#
# No active channel is found for the query.
#
ERROR_EC_NO_ACTIVE_CHANNEL = 15085


#/////////////////////////////////////////////////
#                                               //
#           Start of MUI Error codes            //
#                                               //
#                 15100 to 15199                //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_MUI_FILE_NOT_FOUND
#
# MessageText:
#
# The resource loader failed to find MUI file.
#
ERROR_MUI_FILE_NOT_FOUND = 15100

#
# MessageId: ERROR_MUI_INVALID_FILE
#
# MessageText:
#
# The resource loader failed to load MUI file because the file fail to pass validation.
#
ERROR_MUI_INVALID_FILE = 15101

#
# MessageId: ERROR_MUI_INVALID_RC_CONFIG
#
# MessageText:
#
# The RC Manifest is corrupted with garbage data or unsupported version or missing required item.
#
ERROR_MUI_INVALID_RC_CONFIG = 15102

#
# MessageId: ERROR_MUI_INVALID_LOCALE_NAME
#
# MessageText:
#
# The RC Manifest has invalid culture name.
#
ERROR_MUI_INVALID_LOCALE_NAME = 15103

#
# MessageId: ERROR_MUI_INVALID_ULTIMATEFALLBACK_NAME
#
# MessageText:
#
# The RC Manifest has invalid ultimatefallback name.
#
ERROR_MUI_INVALID_ULTIMATEFALLBACK_NAME = 15104

#
# MessageId: ERROR_MUI_FILE_NOT_LOADED
#
# MessageText:
#
# The resource loader cache doesn't have loaded MUI entry.
#
ERROR_MUI_FILE_NOT_LOADED = 15105

#
# MessageId: ERROR_RESOURCE_ENUM_USER_STOP
#
# MessageText:
#
# User stopped resource enumeration.
#
ERROR_RESOURCE_ENUM_USER_STOP = 15106

#
# MessageId: ERROR_MUI_INTLSETTINGS_UILANG_NOT_INSTALLED
#
# MessageText:
#
# UI language installation failed.
#
ERROR_MUI_INTLSETTINGS_UILANG_NOT_INSTALLED = 15107

#
# MessageId: ERROR_MUI_INTLSETTINGS_INVALID_LOCALE_NAME
#
# MessageText:
#
# Locale installation failed.
#
ERROR_MUI_INTLSETTINGS_INVALID_LOCALE_NAME = 15108

#
# MessageId: ERROR_MRM_RUNTIME_NO_DEFAULT_OR_NEUTRAL_RESOURCE
#
# MessageText:
#
# A resource does not have default or neutral value.
#
ERROR_MRM_RUNTIME_NO_DEFAULT_OR_NEUTRAL_RESOURCE = 15110

#
# MessageId: ERROR_MRM_INVALID_PRICONFIG
#
# MessageText:
#
# Invalid PRI config file.
#
ERROR_MRM_INVALID_PRICONFIG = 15111

#
# MessageId: ERROR_MRM_INVALID_FILE_TYPE
#
# MessageText:
#
# Invalid file type.
#
ERROR_MRM_INVALID_FILE_TYPE = 15112

#
# MessageId: ERROR_MRM_UNKNOWN_QUALIFIER
#
# MessageText:
#
# Unknown qualifier.
#
ERROR_MRM_UNKNOWN_QUALIFIER = 15113

#
# MessageId: ERROR_MRM_INVALID_QUALIFIER_VALUE
#
# MessageText:
#
# Invalid qualifier value.
#
ERROR_MRM_INVALID_QUALIFIER_VALUE = 15114

#
# MessageId: ERROR_MRM_NO_CANDIDATE
#
# MessageText:
#
# No Candidate found.
#
ERROR_MRM_NO_CANDIDATE = 15115

#
# MessageId: ERROR_MRM_NO_MATCH_OR_DEFAULT_CANDIDATE
#
# MessageText:
#
# The ResourceMap or NamedResource has an item that does not have default or neutral resource..
#
ERROR_MRM_NO_MATCH_OR_DEFAULT_CANDIDATE = 15116

#
# MessageId: ERROR_MRM_RESOURCE_TYPE_MISMATCH
#
# MessageText:
#
# Invalid ResourceCandidate type.
#
ERROR_MRM_RESOURCE_TYPE_MISMATCH = 15117

#
# MessageId: ERROR_MRM_DUPLICATE_MAP_NAME
#
# MessageText:
#
# Duplicate Resource Map.
#
ERROR_MRM_DUPLICATE_MAP_NAME = 15118

#
# MessageId: ERROR_MRM_DUPLICATE_ENTRY
#
# MessageText:
#
# Duplicate Entry.
#
ERROR_MRM_DUPLICATE_ENTRY = 15119

#
# MessageId: ERROR_MRM_INVALID_RESOURCE_IDENTIFIER
#
# MessageText:
#
# Invalid Resource Identifier.
#
ERROR_MRM_INVALID_RESOURCE_IDENTIFIER = 15120

#
# MessageId: ERROR_MRM_FILEPATH_TOO_LONG
#
# MessageText:
#
# Filepath too long.
#
ERROR_MRM_FILEPATH_TOO_LONG = 15121

#
# MessageId: ERROR_MRM_UNSUPPORTED_DIRECTORY_TYPE
#
# MessageText:
#
# Unsupported directory type.
#
ERROR_MRM_UNSUPPORTED_DIRECTORY_TYPE = 15122

#
# MessageId: ERROR_MRM_INVALID_PRI_FILE
#
# MessageText:
#
# Invalid PRI File.
#
ERROR_MRM_INVALID_PRI_FILE = 15126

#
# MessageId: ERROR_MRM_NAMED_RESOURCE_NOT_FOUND
#
# MessageText:
#
# NamedResource Not Found.
#
ERROR_MRM_NAMED_RESOURCE_NOT_FOUND = 15127

#
# MessageId: ERROR_MRM_MAP_NOT_FOUND
#
# MessageText:
#
# ResourceMap Not Found.
#
ERROR_MRM_MAP_NOT_FOUND = 15135

#
# MessageId: ERROR_MRM_UNSUPPORTED_PROFILE_TYPE
#
# MessageText:
#
# Unsupported MRT profile type.
#
ERROR_MRM_UNSUPPORTED_PROFILE_TYPE = 15136

#
# MessageId: ERROR_MRM_INVALID_QUALIFIER_OPERATOR
#
# MessageText:
#
# Invalid qualifier operator.
#
ERROR_MRM_INVALID_QUALIFIER_OPERATOR = 15137

#
# MessageId: ERROR_MRM_INDETERMINATE_QUALIFIER_VALUE
#
# MessageText:
#
# Unable to determine qualifier value or qualifier value has not been set.
#
ERROR_MRM_INDETERMINATE_QUALIFIER_VALUE = 15138

#
# MessageId: ERROR_MRM_AUTOMERGE_ENABLED
#
# MessageText:
#
# Automerge is enabled in the PRI file.
#
ERROR_MRM_AUTOMERGE_ENABLED = 15139

#
# MessageId: ERROR_MRM_TOO_MANY_RESOURCES
#
# MessageText:
#
# Too many resources defined for package.
#
ERROR_MRM_TOO_MANY_RESOURCES = 15140

#
# MessageId: ERROR_MRM_UNSUPPORTED_FILE_TYPE_FOR_MERGE
#
# MessageText:
#
# Resource File can not be used for merge operation.
#
ERROR_MRM_UNSUPPORTED_FILE_TYPE_FOR_MERGE = 15141

#
# MessageId: ERROR_MRM_UNSUPPORTED_FILE_TYPE_FOR_LOAD_UNLOAD_PRI_FILE
#
# MessageText:
#
# Load/UnloadPriFiles cannot be used with resource packages.
#
ERROR_MRM_UNSUPPORTED_FILE_TYPE_FOR_LOAD_UNLOAD_PRI_FILE = 15142

#
# MessageId: ERROR_MRM_NO_CURRENT_VIEW_ON_THREAD
#
# MessageText:
#
# Resource Contexts may not be created on threads that do not have a CoreWindow.
#
ERROR_MRM_NO_CURRENT_VIEW_ON_THREAD = 15143

#
# MessageId: ERROR_DIFFERENT_PROFILE_RESOURCE_MANAGER_EXIST
#
# MessageText:
#
# The singleton Resource Manager with different profile is already created.
#
ERROR_DIFFERENT_PROFILE_RESOURCE_MANAGER_EXIST = 15144

#
# MessageId: ERROR_OPERATION_NOT_ALLOWED_FROM_SYSTEM_COMPONENT
#
# MessageText:
#
# The system component cannot operate given API operation
#
ERROR_OPERATION_NOT_ALLOWED_FROM_SYSTEM_COMPONENT = 15145

#
# MessageId: ERROR_MRM_DIRECT_REF_TO_NON_DEFAULT_RESOURCE
#
# MessageText:
#
# The resource is a direct reference to a non-default resource candidate.
#
ERROR_MRM_DIRECT_REF_TO_NON_DEFAULT_RESOURCE = 15146

#
# MessageId: ERROR_MRM_GENERATION_COUNT_MISMATCH
#
# MessageText:
#
# Resource Map has been re-generated and the query string is not valid anymore.
#
ERROR_MRM_GENERATION_COUNT_MISMATCH = 15147


#/////////////////////////////////////////////////
#                                               //
# Start of Monitor Configuration API error codes//
#                                               //
#                 15200 to 15249                //
#/////////////////////////////////////////////////

#
# MessageId: ERROR_MCA_INVALID_CAPABILITIES_STRING
#
# MessageText:
#
# The monitor returned a DDC/CI capabilities string that did not comply with the ACCESS.bus 3.0, DDC/CI 1.1 or MCCS 2 Revision 1 specification.
#
ERROR_MCA_INVALID_CAPABILITIES_STRING = 15200

#
# MessageId: ERROR_MCA_INVALID_VCP_VERSION
#
# MessageText:
#
# The monitor's VCP Version (0xDF) VCP code returned an invalid version value.
#
ERROR_MCA_INVALID_VCP_VERSION = 15201

#
# MessageId: ERROR_MCA_MONITOR_VIOLATES_MCCS_SPECIFICATION
#
# MessageText:
#
# The monitor does not comply with the MCCS specification it claims to support.
#
ERROR_MCA_MONITOR_VIOLATES_MCCS_SPECIFICATION = 15202

#
# MessageId: ERROR_MCA_MCCS_VERSION_MISMATCH
#
# MessageText:
#
# The MCCS version in a monitor's mccs_ver capability does not match the MCCS version the monitor reports when the VCP Version (0xDF) VCP code is used.
#
ERROR_MCA_MCCS_VERSION_MISMATCH = 15203

#
# MessageId: ERROR_MCA_UNSUPPORTED_MCCS_VERSION
#
# MessageText:
#
# The Monitor Configuration API only works with monitors that support the MCCS 1.0 specification, MCCS 2.0 specification or the MCCS 2.0 Revision 1 specification.
#
ERROR_MCA_UNSUPPORTED_MCCS_VERSION = 15204

#
# MessageId: ERROR_MCA_INTERNAL_ERROR
#
# MessageText:
#
# An internal Monitor Configuration API error occurred.
#
ERROR_MCA_INTERNAL_ERROR = 15205

#
# MessageId: ERROR_MCA_INVALID_TECHNOLOGY_TYPE_RETURNED
#
# MessageText:
#
# The monitor returned an invalid monitor technology type. CRT, Plasma and LCD (TFT) are examples of monitor technology types. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.
#
ERROR_MCA_INVALID_TECHNOLOGY_TYPE_RETURNED = 15206

#
# MessageId: ERROR_MCA_UNSUPPORTED_COLOR_TEMPERATURE
#
# MessageText:
#
# The caller of SetMonitorColorTemperature specified a color temperature that the current monitor did not support. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.
#
ERROR_MCA_UNSUPPORTED_COLOR_TEMPERATURE = 15207


#////////////////////////////////////////////////
#                                              //
# End of Monitor Configuration API error codes //
#                                              //
#                15200 to 15249                //
#                                              //
#////////////////////////////////////////////////
#////////////////////////////////////////////////
#                                              //
#         Start of Syspart error codes         //
#                15250 - 15299                 //
#                                              //
#////////////////////////////////////////////////

#
# MessageId: ERROR_AMBIGUOUS_SYSTEM_DEVICE
#
# MessageText:
#
# The requested system device cannot be identified due to multiple indistinguishable devices potentially matching the identification criteria.
#
ERROR_AMBIGUOUS_SYSTEM_DEVICE = 15250

#
# MessageId: ERROR_SYSTEM_DEVICE_NOT_FOUND
#
# MessageText:
#
# The requested system device cannot be found.
#
ERROR_SYSTEM_DEVICE_NOT_FOUND = 15299

#////////////////////////////////////////////////
#                                              //
#         Start of Vortex error codes          //
#                15300 - 15320                 //
#                                              //
#////////////////////////////////////////////////

#
# MessageId: ERROR_HASH_NOT_SUPPORTED
#
# MessageText:
#
# Hash generation for the specified hash version and hash type is not enabled on the server.
#
ERROR_HASH_NOT_SUPPORTED = 15300

#
# MessageId: ERROR_HASH_NOT_PRESENT
#
# MessageText:
#
# The hash requested from the server is not available or no longer valid.
#
ERROR_HASH_NOT_PRESENT = 15301

#////////////////////////////////////////////////
#                                              //
#         Start of GPIO error codes            //
#                15321 - 15340                 //
#                                              //
#////////////////////////////////////////////////

#
# MessageId: ERROR_SECONDARY_IC_PROVIDER_NOT_REGISTERED
#
# MessageText:
#
# The secondary interrupt controller instance that manages the specified interrupt is not registered.
#
ERROR_SECONDARY_IC_PROVIDER_NOT_REGISTERED = 15321

#
# MessageId: ERROR_GPIO_CLIENT_INFORMATION_INVALID
#
# MessageText:
#
# The information supplied by the GPIO client driver is invalid.
#
ERROR_GPIO_CLIENT_INFORMATION_INVALID = 15322

#
# MessageId: ERROR_GPIO_VERSION_NOT_SUPPORTED
#
# MessageText:
#
# The version specified by the GPIO client driver is not supported.
#
ERROR_GPIO_VERSION_NOT_SUPPORTED = 15323

#
# MessageId: ERROR_GPIO_INVALID_REGISTRATION_PACKET
#
# MessageText:
#
# The registration packet supplied by the GPIO client driver is not valid.
#
ERROR_GPIO_INVALID_REGISTRATION_PACKET = 15324

#
# MessageId: ERROR_GPIO_OPERATION_DENIED
#
# MessageText:
#
# The requested operation is not suppported for the specified handle.
#
ERROR_GPIO_OPERATION_DENIED = 15325

#
# MessageId: ERROR_GPIO_INCOMPATIBLE_CONNECT_MODE
#
# MessageText:
#
# The requested connect mode conflicts with an existing mode on one or more of the specified pins.
#
ERROR_GPIO_INCOMPATIBLE_CONNECT_MODE = 15326

#
# MessageId: ERROR_GPIO_INTERRUPT_ALREADY_UNMASKED
#
# MessageText:
#
# The interrupt requested to be unmasked is not masked.
#
ERROR_GPIO_INTERRUPT_ALREADY_UNMASKED = 15327

#////////////////////////////////////////////////
#                                              //
#         Start of Run Level error codes       //
#                15400 - 15500                 //
#                                              //
#////////////////////////////////////////////////

#
# MessageId: ERROR_CANNOT_SWITCH_RUNLEVEL
#
# MessageText:
#
# The requested run level switch cannot be completed successfully.
#
ERROR_CANNOT_SWITCH_RUNLEVEL = 15400

#
# MessageId: ERROR_INVALID_RUNLEVEL_SETTING
#
# MessageText:
#
# The service has an invalid run level setting. The run level for a service
# must not be higher than the run level of its dependent services.
#
ERROR_INVALID_RUNLEVEL_SETTING = 15401

#
# MessageId: ERROR_RUNLEVEL_SWITCH_TIMEOUT
#
# MessageText:
#
# The requested run level switch cannot be completed successfully since
# one or more services will not stop or restart within the specified timeout.
#
ERROR_RUNLEVEL_SWITCH_TIMEOUT = 15402

#
# MessageId: ERROR_RUNLEVEL_SWITCH_AGENT_TIMEOUT
#
# MessageText:
#
# A run level switch agent did not respond within the specified timeout.
#
ERROR_RUNLEVEL_SWITCH_AGENT_TIMEOUT = 15403

#
# MessageId: ERROR_RUNLEVEL_SWITCH_IN_PROGRESS
#
# MessageText:
#
# A run level switch is currently in progress.
#
ERROR_RUNLEVEL_SWITCH_IN_PROGRESS = 15404

#
# MessageId: ERROR_SERVICES_FAILED_AUTOSTART
#
# MessageText:
#
# One or more services failed to start during the service startup phase of a run level switch.
#
ERROR_SERVICES_FAILED_AUTOSTART = 15405

#////////////////////////////////////////////////
#                                              //
#         Start of Com Task error codes        //
#                15501 - 15510                 //
#                                              //
#////////////////////////////////////////////////

#
# MessageId: ERROR_COM_TASK_STOP_PENDING
#
# MessageText:
#
# The task stop request cannot be completed immediately since
# task needs more time to shutdown.
#
ERROR_COM_TASK_STOP_PENDING = 15501

#//////////////////////////////////////
#                                    //
# APPX Caller Visible Error Codes    //
#          15600-15640               //
#//////////////////////////////////////
#
# MessageId: ERROR_INSTALL_OPEN_PACKAGE_FAILED
#
# MessageText:
#
# Package could not be opened.
#
ERROR_INSTALL_OPEN_PACKAGE_FAILED = 15600

#
# MessageId: ERROR_INSTALL_PACKAGE_NOT_FOUND
#
# MessageText:
#
# Package was not found.
#
ERROR_INSTALL_PACKAGE_NOT_FOUND = 15601

#
# MessageId: ERROR_INSTALL_INVALID_PACKAGE
#
# MessageText:
#
# Package data is invalid.
#
ERROR_INSTALL_INVALID_PACKAGE = 15602

#
# MessageId: ERROR_INSTALL_RESOLVE_DEPENDENCY_FAILED
#
# MessageText:
#
# Package failed updates, dependency or conflict validation.
#
ERROR_INSTALL_RESOLVE_DEPENDENCY_FAILED = 15603

#
# MessageId: ERROR_INSTALL_OUT_OF_DISK_SPACE
#
# MessageText:
#
# There is not enough disk space on your computer. Please free up some space and try again.
#
ERROR_INSTALL_OUT_OF_DISK_SPACE = 15604

#
# MessageId: ERROR_INSTALL_NETWORK_FAILURE
#
# MessageText:
#
# There was a problem downloading your product.
#
ERROR_INSTALL_NETWORK_FAILURE = 15605

#
# MessageId: ERROR_INSTALL_REGISTRATION_FAILURE
#
# MessageText:
#
# Package could not be registered.
#
ERROR_INSTALL_REGISTRATION_FAILURE = 15606

#
# MessageId: ERROR_INSTALL_DEREGISTRATION_FAILURE
#
# MessageText:
#
# Package could not be unregistered.
#
ERROR_INSTALL_DEREGISTRATION_FAILURE = 15607

#
# MessageId: ERROR_INSTALL_CANCEL
#
# MessageText:
#
# User cancelled the install request.
#
ERROR_INSTALL_CANCEL = 15608

#
# MessageId: ERROR_INSTALL_FAILED
#
# MessageText:
#
# Install failed. Please contact your software vendor.
#
ERROR_INSTALL_FAILED = 15609

#
# MessageId: ERROR_REMOVE_FAILED
#
# MessageText:
#
# Removal failed. Please contact your software vendor.
#
ERROR_REMOVE_FAILED = 15610

#
# MessageId: ERROR_PACKAGE_ALREADY_EXISTS
#
# MessageText:
#
# The provided package is already installed, and reinstallation of the package was blocked. Check the AppXDeployment-Server event log for details.
#
ERROR_PACKAGE_ALREADY_EXISTS = 15611

#
# MessageId: ERROR_NEEDS_REMEDIATION
#
# MessageText:
#
# The application cannot be started. Try reinstalling the application to fix the problem.
#
ERROR_NEEDS_REMEDIATION = 15612

#
# MessageId: ERROR_INSTALL_PREREQUISITE_FAILED
#
# MessageText:
#
# A Prerequisite for an install could not be satisfied.
#
ERROR_INSTALL_PREREQUISITE_FAILED = 15613

#
# MessageId: ERROR_PACKAGE_REPOSITORY_CORRUPTED
#
# MessageText:
#
# The package repository is corrupted.
#
ERROR_PACKAGE_REPOSITORY_CORRUPTED = 15614

#
# MessageId: ERROR_INSTALL_POLICY_FAILURE
#
# MessageText:
#
# To install this application you need either a Windows developer license or a sideloading-enabled system.
#
ERROR_INSTALL_POLICY_FAILURE = 15615

#
# MessageId: ERROR_PACKAGE_UPDATING
#
# MessageText:
#
# The application cannot be started because it is currently updating.
#
ERROR_PACKAGE_UPDATING = 15616

#
# MessageId: ERROR_DEPLOYMENT_BLOCKED_BY_POLICY
#
# MessageText:
#
# The package deployment operation is blocked by policy. Please contact your system administrator.
#
ERROR_DEPLOYMENT_BLOCKED_BY_POLICY = 15617

#
# MessageId: ERROR_PACKAGES_IN_USE
#
# MessageText:
#
# The package could not be installed because resources it modifies are currently in use.
#
ERROR_PACKAGES_IN_USE = 15618

#
# MessageId: ERROR_RECOVERY_FILE_CORRUPT
#
# MessageText:
#
# The package could not be recovered because necessary data for recovery have been corrupted.
#
ERROR_RECOVERY_FILE_CORRUPT = 15619

#
# MessageId: ERROR_INVALID_STAGED_SIGNATURE
#
# MessageText:
#
# The signature is invalid. To register in developer mode, AppxSignature.p7x and AppxBlockMap.xml must be valid or should not be present.
#
ERROR_INVALID_STAGED_SIGNATURE = 15620

#
# MessageId: ERROR_DELETING_EXISTING_APPLICATIONDATA_STORE_FAILED
#
# MessageText:
#
# An error occurred while deleting the package's previously existing application data.
#
ERROR_DELETING_EXISTING_APPLICATIONDATA_STORE_FAILED = 15621

#
# MessageId: ERROR_INSTALL_PACKAGE_DOWNGRADE
#
# MessageText:
#
# The package could not be installed because a higher version of this package is already installed.
#
ERROR_INSTALL_PACKAGE_DOWNGRADE = 15622

#
# MessageId: ERROR_SYSTEM_NEEDS_REMEDIATION
#
# MessageText:
#
# An error in a system binary was detected. Try refreshing the PC to fix the problem.
#
ERROR_SYSTEM_NEEDS_REMEDIATION = 15623

#
# MessageId: ERROR_APPX_INTEGRITY_FAILURE_CLR_NGEN
#
# MessageText:
#
# A corrupted CLR NGEN binary was detected on the system.
#
ERROR_APPX_INTEGRITY_FAILURE_CLR_NGEN = 15624

#
# MessageId: ERROR_RESILIENCY_FILE_CORRUPT
#
# MessageText:
#
# The operation could not be resumed because necessary data for recovery have been corrupted.
#
ERROR_RESILIENCY_FILE_CORRUPT = 15625

#
# MessageId: ERROR_INSTALL_FIREWALL_SERVICE_NOT_RUNNING
#
# MessageText:
#
# The package could not be installed because the Windows Firewall service is not running. Enable the Windows Firewall service and try again.
#
ERROR_INSTALL_FIREWALL_SERVICE_NOT_RUNNING = 15626

#////////////////////////
#                      //
# AppModel Error Codes //
#     15700-15720      //
#                      //
#////////////////////////
#
# MessageId: APPMODEL_ERROR_NO_PACKAGE
#
# MessageText:
#
# The process has no package identity.
#
APPMODEL_ERROR_NO_PACKAGE = 15700

#
# MessageId: APPMODEL_ERROR_PACKAGE_RUNTIME_CORRUPT
#
# MessageText:
#
# The package runtime information is corrupted.
#
APPMODEL_ERROR_PACKAGE_RUNTIME_CORRUPT = 15701

#
# MessageId: APPMODEL_ERROR_PACKAGE_IDENTITY_CORRUPT
#
# MessageText:
#
# The package identity is corrupted.
#
APPMODEL_ERROR_PACKAGE_IDENTITY_CORRUPT = 15702

#
# MessageId: APPMODEL_ERROR_NO_APPLICATION
#
# MessageText:
#
# The process has no application identity.
#
APPMODEL_ERROR_NO_APPLICATION = 15703

#
# MessageId: APPMODEL_ERROR_DYNAMIC_PROPERTY_READ_FAILED
#
# MessageText:
#
# One or more AppModel Runtime group policy values could not be read. Please contact your system administrator with the contents of your AppModel Runtime event log.
#
APPMODEL_ERROR_DYNAMIC_PROPERTY_READ_FAILED = 15704

#
# MessageId: APPMODEL_ERROR_DYNAMIC_PROPERTY_INVALID
#
# MessageText:
#
# One or more AppModel Runtime group policy values are invalid. Please contact your system administrator with the contents of your AppModel Runtime event log.
#
APPMODEL_ERROR_DYNAMIC_PROPERTY_INVALID = 15705

#///////////////////////////
#                         //
# Appx StateManager Codes //
#     15800-15840         //
#                         //
#///////////////////////////
#
# MessageId: ERROR_STATE_LOAD_STORE_FAILED
#
# MessageText:
#
# Loading the state store failed.
#
ERROR_STATE_LOAD_STORE_FAILED = 15800

#
# MessageId: ERROR_STATE_GET_VERSION_FAILED
#
# MessageText:
#
# Retrieving the state version for the application failed.
#
ERROR_STATE_GET_VERSION_FAILED = 15801

#
# MessageId: ERROR_STATE_SET_VERSION_FAILED
#
# MessageText:
#
# Setting the state version for the application failed.
#
ERROR_STATE_SET_VERSION_FAILED = 15802

#
# MessageId: ERROR_STATE_STRUCTURED_RESET_FAILED
#
# MessageText:
#
# Resetting the structured state of the application failed.
#
ERROR_STATE_STRUCTURED_RESET_FAILED = 15803

#
# MessageId: ERROR_STATE_OPEN_CONTAINER_FAILED
#
# MessageText:
#
# State Manager failed to open the container.
#
ERROR_STATE_OPEN_CONTAINER_FAILED = 15804

#
# MessageId: ERROR_STATE_CREATE_CONTAINER_FAILED
#
# MessageText:
#
# State Manager failed to create the container.
#
ERROR_STATE_CREATE_CONTAINER_FAILED = 15805

#
# MessageId: ERROR_STATE_DELETE_CONTAINER_FAILED
#
# MessageText:
#
# State Manager failed to delete the container.
#
ERROR_STATE_DELETE_CONTAINER_FAILED = 15806

#
# MessageId: ERROR_STATE_READ_SETTING_FAILED
#
# MessageText:
#
# State Manager failed to read the setting.
#
ERROR_STATE_READ_SETTING_FAILED = 15807

#
# MessageId: ERROR_STATE_WRITE_SETTING_FAILED
#
# MessageText:
#
# State Manager failed to write the setting.
#
ERROR_STATE_WRITE_SETTING_FAILED = 15808

#
# MessageId: ERROR_STATE_DELETE_SETTING_FAILED
#
# MessageText:
#
# State Manager failed to delete the setting.
#
ERROR_STATE_DELETE_SETTING_FAILED = 15809

#
# MessageId: ERROR_STATE_QUERY_SETTING_FAILED
#
# MessageText:
#
# State Manager failed to query the setting.
#
ERROR_STATE_QUERY_SETTING_FAILED = 15810

#
# MessageId: ERROR_STATE_READ_COMPOSITE_SETTING_FAILED
#
# MessageText:
#
# State Manager failed to read the composite setting.
#
ERROR_STATE_READ_COMPOSITE_SETTING_FAILED = 15811

#
# MessageId: ERROR_STATE_WRITE_COMPOSITE_SETTING_FAILED
#
# MessageText:
#
# State Manager failed to write the composite setting.
#
ERROR_STATE_WRITE_COMPOSITE_SETTING_FAILED = 15812

#
# MessageId: ERROR_STATE_ENUMERATE_CONTAINER_FAILED
#
# MessageText:
#
# State Manager failed to enumerate the containers.
#
ERROR_STATE_ENUMERATE_CONTAINER_FAILED = 15813

#
# MessageId: ERROR_STATE_ENUMERATE_SETTINGS_FAILED
#
# MessageText:
#
# State Manager failed to enumerate the settings.
#
ERROR_STATE_ENUMERATE_SETTINGS_FAILED = 15814

#
# MessageId: ERROR_STATE_COMPOSITE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED
#
# MessageText:
#
# The size of the state manager composite setting value has exceeded the limit.
#
ERROR_STATE_COMPOSITE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED = 15815

#
# MessageId: ERROR_STATE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED
#
# MessageText:
#
# The size of the state manager setting value has exceeded the limit.
#
ERROR_STATE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED = 15816

#
# MessageId: ERROR_STATE_SETTING_NAME_SIZE_LIMIT_EXCEEDED
#
# MessageText:
#
# The length of the state manager setting name has exceeded the limit.
#
ERROR_STATE_SETTING_NAME_SIZE_LIMIT_EXCEEDED = 15817

#
# MessageId: ERROR_STATE_CONTAINER_NAME_SIZE_LIMIT_EXCEEDED
#
# MessageText:
#
# The length of the state manager container name has exceeded the limit.
#
ERROR_STATE_CONTAINER_NAME_SIZE_LIMIT_EXCEEDED = 15818

#///////////////////////////////
#                             //
# Application Partition Codes //
#     15841-15860             //
#                             //
#///////////////////////////////
#
# MessageId: ERROR_API_UNAVAILABLE
#
# MessageText:
#
# This API cannot be used in the context of the caller's application type.
#
ERROR_API_UNAVAILABLE = 15841

#///////////////////////////////
#                             //
# Windows Store Codes         //
#     15861-15880             //
#                             //
#///////////////////////////////
#
# MessageId: STORE_ERROR_UNLICENSED
#
# MessageText:
#
# This PC does not have a valid license for the application or product.
#
STORE_ERROR_UNLICENSED = 15861

#
# MessageId: STORE_ERROR_UNLICENSED_USER
#
# MessageText:
#
# The authenticated user does not have a valid license for the application or product.
#
STORE_ERROR_UNLICENSED_USER = 15862

#
# MessageId: STORE_ERROR_PENDING_COM_TRANSACTION
#
# MessageText:
#
# The commerce transaction associated with this license is still pending verification.
#
STORE_ERROR_PENDING_COM_TRANSACTION = 15863

#
# MessageId: STORE_ERROR_LICENSE_REVOKED
#
# MessageText:
#
# The license has been revoked for this user.
#
STORE_ERROR_LICENSE_REVOKED = 15864

#//////////////////////////////////
#                                //
#     COM Error Codes            //
#                                //
#//////////////////////////////////


#
# The return value of COM functions and methods is an HRESULT.
# This is not a handle to anything, but is merely a 32-bit value
# with several fields encoded in the value. The parts of an
# HRESULT are shown below.
#
# Many of the macros and functions below were orginally defined to
# operate on SCODEs. SCODEs are no longer used. The macros are
# still present for compatibility and easy porting of Win16 code.
# Newly written code should use the HRESULT macros and functions.
#

#
#  HRESULTs are 32 bit values layed out as follows:
#
#   3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
#   1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
#  +-+-+-+-+-+---------------------+-------------------------------+
#  |S|R|C|N|r|    Facility         |               Code            |
#  +-+-+-+-+-+---------------------+-------------------------------+
#
#  where
#
#      S - Severity - indicates success/fail
#
#          0 - Success
#          1 - Fail (COERROR)
#
#      R - reserved portion of the facility code, corresponds to NT's
#              second severity bit.
#
#      C - reserved portion of the facility code, corresponds to NT's
#              C field.
#
#      N - reserved portion of the facility code. Used to indicate a
#              mapped NT status value.
#
#      r - reserved portion of the facility code. Reserved for internal
#              use. Used to indicate HRESULT values that are not status
#              values, but are instead message ids for display strings.
#
#      Facility - is the facility code
#
#      Code - is the facility's status code
#

#
# Severity values
#

SEVERITY_SUCCESS = 0
SEVERITY_ERROR = 1


#
# Generic test for success on any status value (non-negative numbers
# indicate success).
#

#define SUCCEEDED(hr) (((HRESULT)(hr)) >= 0)

#
# and the inverse
#

#define FAILED(hr) (((HRESULT)(hr)) < 0)


#
# Generic test for error on any status value.
#

#define IS_ERROR(Status) (((unsigned long)(Status)) >> 31 == SEVERITY_ERROR)

#
# Return the code
#

#define HRESULT_CODE(hr)    ((hr) & 0xFFFF)
#define SCODE_CODE(sc)      ((sc) & 0xFFFF)

#
#  Return the facility
#

#define HRESULT_FACILITY(hr)  (((hr) >> 16) & 0x1fff)
#define SCODE_FACILITY(sc)    (((sc) >> 16) & 0x1fff)

#
#  Return the severity
#

#define HRESULT_SEVERITY(hr)  (((hr) >> 31) & 0x1)
#define SCODE_SEVERITY(sc)    (((sc) >> 31) & 0x1)

#
# Create an HRESULT value from component pieces
#

#define MAKE_HRESULT(sev,fac,code) \
    # ((HRESULT) (((unsigned long)(sev)<<31) | ((unsigned long)(fac)<<16) | ((unsigned long)(code))) )
#define MAKE_SCODE(sev,fac,code) \
    # ((SCODE) (((unsigned long)(sev)<<31) | ((unsigned long)(fac)<<16) | ((unsigned long)(code))) )


#
# Map a WIN32 error value into a HRESULT
# Note: This assumes that WIN32 errors fall in the range -32k to 32k.
#
# Define bits here so macros are guaranteed to work

FACILITY_NT_BIT = 0

#
# HRESULT_FROM_WIN32(x) used to be a macro, however we now run it as an inline function
# to prevent double evaluation of 'x'. If you still need the macro, you can use __HRESULT_FROM_WIN32(x)
#
__HRESULT_FROM_WIN3 = 2

#if !defined(_HRESULT_DEFINED) && !defined(__midl)
#define _HRESULT_DEFINED
# typedef _Return_type_success_(return >= 0) long HRESULT;
#endif

#ifndef __midl
# FORCEINLINE HRESULT HRESULT_FROM_WIN32(unsigned long x) { return (HRESULT)(x) <= 0 ? (HRESULT)(x) : (HRESULT) (((x) & 0x0000FFFF) | (FACILITY_WIN32 << 16) | 0x80000000);}
#else
HRESULT_FROM_WIN3 = 2
#endif

#
# Map an NT status value into a HRESULT
#

#define HRESULT_FROM_NT(x)      ((HRESULT) ((x) | FACILITY_NT_BIT))


# ****** OBSOLETE functions

# HRESULT functions
# As noted above, these functions are obsolete and should not be used.


# Extract the SCODE from a HRESULT

#define GetScode(hr) ((SCODE) (hr))

# Convert an SCODE into an HRESULT.

#define ResultFromScode(sc) ((HRESULT) (sc))


# PropagateResult is a noop
#define PropagateResult(hrPrevious, scBase) ((HRESULT) scBase)


# ****** End of OBSOLETE functions.

#define E_NOT_SET                HRESULT_FROM_WIN32(ERROR_NOT_FOUND)
#define E_NOT_VALID_STATE        HRESULT_FROM_WIN32(ERROR_INVALID_STATE)
#define E_NOT_SUFFICIENT_BUFFER  HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER)

# ---------------------- HRESULT value definitions -----------------
#
# HRESULT definitions
#

#ifdef RC_INVOKED
#define _HRESULT_TYPEDEF_(_sc) _sc
#else // RC_INVOKED
#define _HRESULT_TYPEDEF_(_sc) ((HRESULT)_sc)
#endif // RC_INVOKED

NOERROR = 0

#
# Error definitions follow
#

#
# Codes 0x4000-0x40ff are reserved for OLE
#
#
# Error codes
#
#
# MessageId: E_UNEXPECTED
#
# MessageText:
#
# Catastrophic failure
#
E_UNEXPECTED = 0x8000FFFF

#if defined(_WIN32) && !defined(_MAC)
#
# MessageId: E_NOTIMPL
#
# MessageText:
#
# Not implemented
#
E_NOTIMPL = 0x80004001

#
# MessageId: E_OUTOFMEMORY
#
# MessageText:
#
# Ran out of memory
#
E_OUTOFMEMORY = 0x8007000E

#
# MessageId: E_INVALIDARG
#
# MessageText:
#
# One or more arguments are invalid
#
E_INVALIDARG = 0x80070057

#
# MessageId: E_NOINTERFACE
#
# MessageText:
#
# No such interface supported
#
E_NOINTERFACE = 0x80004002

#
# MessageId: E_POINTER
#
# MessageText:
#
# Invalid pointer
#
E_POINTER = 0x80004003

#
# MessageId: E_HANDLE
#
# MessageText:
#
# Invalid handle
#
E_HANDLE = 0x80070006

#
# MessageId: E_ABORT
#
# MessageText:
#
# Operation aborted
#
E_ABORT = 0x80004004

#
# MessageId: E_FAIL
#
# MessageText:
#
# Unspecified error
#
E_FAIL = 0x80004005

#
# MessageId: E_ACCESSDENIED
#
# MessageText:
#
# General access denied error
#
E_ACCESSDENIED = 0x80070005

#else
#
# MessageId: E_NOTIMPL
#
# MessageText:
#
# Not implemented
#
E_NOTIMPL = 0x80000001

#
# MessageId: E_OUTOFMEMORY
#
# MessageText:
#
# Ran out of memory
#
E_OUTOFMEMORY = 0x80000002

#
# MessageId: E_INVALIDARG
#
# MessageText:
#
# One or more arguments are invalid
#
E_INVALIDARG = 0x80000003

#
# MessageId: E_NOINTERFACE
#
# MessageText:
#
# No such interface supported
#
E_NOINTERFACE = 0x80000004

#
# MessageId: E_POINTER
#
# MessageText:
#
# Invalid pointer
#
E_POINTER = 0x80000005

#
# MessageId: E_HANDLE
#
# MessageText:
#
# Invalid handle
#
E_HANDLE = 0x80000006

#
# MessageId: E_ABORT
#
# MessageText:
#
# Operation aborted
#
E_ABORT = 0x80000007

#
# MessageId: E_FAIL
#
# MessageText:
#
# Unspecified error
#
E_FAIL = 0x80000008

#
# MessageId: E_ACCESSDENIED
#
# MessageText:
#
# General access denied error
#
E_ACCESSDENIED = 0x80000009

#endif //WIN32
#
# MessageId: E_PENDING
#
# MessageText:
#
# The data necessary to complete this operation is not yet available.
#
E_PENDING = 0x8000000A

#
# MessageId: E_BOUNDS
#
# MessageText:
#
# The operation attempted to access data outside the valid range
#
E_BOUNDS = 0x8000000B

#
# MessageId: E_CHANGED_STATE
#
# MessageText:
#
# A concurrent or interleaved operation changed the state of the object, invalidating this operation.
#
E_CHANGED_STATE = 0x8000000C

#
# MessageId: E_ILLEGAL_STATE_CHANGE
#
# MessageText:
#
# An illegal state change was requested.
#
E_ILLEGAL_STATE_CHANGE = 0x8000000D

#
# MessageId: E_ILLEGAL_METHOD_CALL
#
# MessageText:
#
# A method was called at an unexpected time.
#
E_ILLEGAL_METHOD_CALL = 0x8000000E

#
# MessageId: RO_E_METADATA_NAME_NOT_FOUND
#
# MessageText:
#
# Typename or Namespace was not found in metadata file.
#
RO_E_METADATA_NAME_NOT_FOUND = 0x8000000F

#
# MessageId: RO_E_METADATA_NAME_IS_NAMESPACE
#
# MessageText:
#
# Name is an existing namespace rather than a typename.
#
RO_E_METADATA_NAME_IS_NAMESPACE = 0x80000010

#
# MessageId: RO_E_METADATA_INVALID_TYPE_FORMAT
#
# MessageText:
#
# Typename has an invalid format.
#
RO_E_METADATA_INVALID_TYPE_FORMAT = 0x80000011

#
# MessageId: RO_E_INVALID_METADATA_FILE
#
# MessageText:
#
# Metadata file is invalid or corrupted.
#
RO_E_INVALID_METADATA_FILE = 0x80000012

#
# MessageId: RO_E_CLOSED
#
# MessageText:
#
# The object has been closed.
#
RO_E_CLOSED = 0x80000013

#
# MessageId: RO_E_EXCLUSIVE_WRITE
#
# MessageText:
#
# Only one thread may access the object during a write operation.
#
RO_E_EXCLUSIVE_WRITE = 0x80000014

#
# MessageId: RO_E_CHANGE_NOTIFICATION_IN_PROGRESS
#
# MessageText:
#
# Operation is prohibited during change notification.
#
RO_E_CHANGE_NOTIFICATION_IN_PROGRESS = 0x80000015

#
# MessageId: RO_E_ERROR_STRING_NOT_FOUND
#
# MessageText:
#
# The text associated with this error code could not be found.
#
RO_E_ERROR_STRING_NOT_FOUND = 0x80000016

#
# MessageId: E_STRING_NOT_NULL_TERMINATED
#
# MessageText:
#
# String not null terminated.
#
E_STRING_NOT_NULL_TERMINATED = 0x80000017

#
# MessageId: E_ILLEGAL_DELEGATE_ASSIGNMENT
#
# MessageText:
#
# A delegate was assigned when not allowed.
#
E_ILLEGAL_DELEGATE_ASSIGNMENT = 0x80000018

#
# MessageId: E_ASYNC_OPERATION_NOT_STARTED
#
# MessageText:
#
# An async operation was not properly started.
#
E_ASYNC_OPERATION_NOT_STARTED = 0x80000019

#
# MessageId: E_APPLICATION_EXITING
#
# MessageText:
#
# The application is exiting and cannot service this request
#
E_APPLICATION_EXITING = 0x8000001A

#
# MessageId: E_APPLICATION_VIEW_EXITING
#
# MessageText:
#
# The application view is exiting and cannot service this request
#
E_APPLICATION_VIEW_EXITING = 0x8000001B

#
# MessageId: RO_E_MUST_BE_AGILE
#
# MessageText:
#
# The object must support the IAgileObject interface
#
RO_E_MUST_BE_AGILE = 0x8000001C

#
# MessageId: RO_E_UNSUPPORTED_FROM_MTA
#
# MessageText:
#
# Activating a single-threaded class from MTA is not supported
#
RO_E_UNSUPPORTED_FROM_MTA = 0x8000001D

#
# MessageId: RO_E_COMMITTED
#
# MessageText:
#
# The object has been committed.
#
RO_E_COMMITTED = 0x8000001E

#
# MessageId: RO_E_BLOCKED_CROSS_ASTA_CALL
#
# MessageText:
#
# A COM call to an ASTA was blocked because the call chain originated in or passed through another ASTA. This call pattern is deadlock-prone and disallowed by apartment call control.
#
RO_E_BLOCKED_CROSS_ASTA_CALL = 0x8000001F

#
# MessageId: CO_E_INIT_TLS
#
# MessageText:
#
# Thread local storage failure
#
CO_E_INIT_TLS = 0x80004006

#
# MessageId: CO_E_INIT_SHARED_ALLOCATOR
#
# MessageText:
#
# Get shared memory allocator failure
#
CO_E_INIT_SHARED_ALLOCATOR = 0x80004007

#
# MessageId: CO_E_INIT_MEMORY_ALLOCATOR
#
# MessageText:
#
# Get memory allocator failure
#
CO_E_INIT_MEMORY_ALLOCATOR = 0x80004008

#
# MessageId: CO_E_INIT_CLASS_CACHE
#
# MessageText:
#
# Unable to initialize class cache
#
CO_E_INIT_CLASS_CACHE = 0x80004009

#
# MessageId: CO_E_INIT_RPC_CHANNEL
#
# MessageText:
#
# Unable to initialize RPC services
#
CO_E_INIT_RPC_CHANNEL = 0x8000400A

#
# MessageId: CO_E_INIT_TLS_SET_CHANNEL_CONTROL
#
# MessageText:
#
# Cannot set thread local storage channel control
#
CO_E_INIT_TLS_SET_CHANNEL_CONTROL = 0x8000400B

#
# MessageId: CO_E_INIT_TLS_CHANNEL_CONTROL
#
# MessageText:
#
# Could not allocate thread local storage channel control
#
CO_E_INIT_TLS_CHANNEL_CONTROL = 0x8000400C

#
# MessageId: CO_E_INIT_UNACCEPTED_USER_ALLOCATOR
#
# MessageText:
#
# The user supplied memory allocator is unacceptable
#
CO_E_INIT_UNACCEPTED_USER_ALLOCATOR = 0x8000400D

#
# MessageId: CO_E_INIT_SCM_MUTEX_EXISTS
#
# MessageText:
#
# The OLE service mutex already exists
#
CO_E_INIT_SCM_MUTEX_EXISTS = 0x8000400E

#
# MessageId: CO_E_INIT_SCM_FILE_MAPPING_EXISTS
#
# MessageText:
#
# The OLE service file mapping already exists
#
CO_E_INIT_SCM_FILE_MAPPING_EXISTS = 0x8000400F

#
# MessageId: CO_E_INIT_SCM_MAP_VIEW_OF_FILE
#
# MessageText:
#
# Unable to map view of file for OLE service
#
CO_E_INIT_SCM_MAP_VIEW_OF_FILE = 0x80004010

#
# MessageId: CO_E_INIT_SCM_EXEC_FAILURE
#
# MessageText:
#
# Failure attempting to launch OLE service
#
CO_E_INIT_SCM_EXEC_FAILURE = 0x80004011

#
# MessageId: CO_E_INIT_ONLY_SINGLE_THREADED
#
# MessageText:
#
# There was an attempt to call CoInitialize a second time while single threaded
#
CO_E_INIT_ONLY_SINGLE_THREADED = 0x80004012

#
# MessageId: CO_E_CANT_REMOTE
#
# MessageText:
#
# A Remote activation was necessary but was not allowed
#
CO_E_CANT_REMOTE = 0x80004013

#
# MessageId: CO_E_BAD_SERVER_NAME
#
# MessageText:
#
# A Remote activation was necessary but the server name provided was invalid
#
CO_E_BAD_SERVER_NAME = 0x80004014

#
# MessageId: CO_E_WRONG_SERVER_IDENTITY
#
# MessageText:
#
# The class is configured to run as a security id different from the caller
#
CO_E_WRONG_SERVER_IDENTITY = 0x80004015

#
# MessageId: CO_E_OLE1DDE_DISABLED
#
# MessageText:
#
# Use of Ole1 services requiring DDE windows is disabled
#
CO_E_OLE = 1

#
# MessageId: CO_E_RUNAS_SYNTAX
#
# MessageText:
#
# A RunAs specification must be <domain name>\<user name> or simply <user name>
#
CO_E_RUNAS_SYNTAX = 0x80004017

#
# MessageId: CO_E_CREATEPROCESS_FAILURE
#
# MessageText:
#
# The server process could not be started. The pathname may be incorrect.
#
CO_E_CREATEPROCESS_FAILURE = 0x80004018

#
# MessageId: CO_E_RUNAS_CREATEPROCESS_FAILURE
#
# MessageText:
#
# The server process could not be started as the configured identity. The pathname may be incorrect or unavailable.
#
CO_E_RUNAS_CREATEPROCESS_FAILURE = 0x80004019

#
# MessageId: CO_E_RUNAS_LOGON_FAILURE
#
# MessageText:
#
# The server process could not be started because the configured identity is incorrect. Check the username and password.
#
CO_E_RUNAS_LOGON_FAILURE = 0x8000401A

#
# MessageId: CO_E_LAUNCH_PERMSSION_DENIED
#
# MessageText:
#
# The client is not allowed to launch this server.
#
CO_E_LAUNCH_PERMSSION_DENIED = 0x8000401B

#
# MessageId: CO_E_START_SERVICE_FAILURE
#
# MessageText:
#
# The service providing this server could not be started.
#
CO_E_START_SERVICE_FAILURE = 0x8000401C

#
# MessageId: CO_E_REMOTE_COMMUNICATION_FAILURE
#
# MessageText:
#
# This computer was unable to communicate with the computer providing the server.
#
CO_E_REMOTE_COMMUNICATION_FAILURE = 0x8000401D

#
# MessageId: CO_E_SERVER_START_TIMEOUT
#
# MessageText:
#
# The server did not respond after being launched.
#
CO_E_SERVER_START_TIMEOUT = 0x8000401E

#
# MessageId: CO_E_CLSREG_INCONSISTENT
#
# MessageText:
#
# The registration information for this server is inconsistent or incomplete.
#
CO_E_CLSREG_INCONSISTENT = 0x8000401F

#
# MessageId: CO_E_IIDREG_INCONSISTENT
#
# MessageText:
#
# The registration information for this interface is inconsistent or incomplete.
#
CO_E_IIDREG_INCONSISTENT = 0x80004020

#
# MessageId: CO_E_NOT_SUPPORTED
#
# MessageText:
#
# The operation attempted is not supported.
#
CO_E_NOT_SUPPORTED = 0x80004021

#
# MessageId: CO_E_RELOAD_DLL
#
# MessageText:
#
# A dll must be loaded.
#
CO_E_RELOAD_DLL = 0x80004022

#
# MessageId: CO_E_MSI_ERROR
#
# MessageText:
#
# A Microsoft Software Installer error was encountered.
#
CO_E_MSI_ERROR = 0x80004023

#
# MessageId: CO_E_ATTEMPT_TO_CREATE_OUTSIDE_CLIENT_CONTEXT
#
# MessageText:
#
# The specified activation could not occur in the client context as specified.
#
CO_E_ATTEMPT_TO_CREATE_OUTSIDE_CLIENT_CONTEXT = 0x80004024

#
# MessageId: CO_E_SERVER_PAUSED
#
# MessageText:
#
# Activations on the server are paused.
#
CO_E_SERVER_PAUSED = 0x80004025

#
# MessageId: CO_E_SERVER_NOT_PAUSED
#
# MessageText:
#
# Activations on the server are not paused.
#
CO_E_SERVER_NOT_PAUSED = 0x80004026

#
# MessageId: CO_E_CLASS_DISABLED
#
# MessageText:
#
# The component or application containing the component has been disabled.
#
CO_E_CLASS_DISABLED = 0x80004027

#
# MessageId: CO_E_CLRNOTAVAILABLE
#
# MessageText:
#
# The common language runtime is not available
#
CO_E_CLRNOTAVAILABLE = 0x80004028

#
# MessageId: CO_E_ASYNC_WORK_REJECTED
#
# MessageText:
#
# The thread-pool rejected the submitted asynchronous work.
#
CO_E_ASYNC_WORK_REJECTED = 0x80004029

#
# MessageId: CO_E_SERVER_INIT_TIMEOUT
#
# MessageText:
#
# The server started, but did not finish initializing in a timely fashion.
#
CO_E_SERVER_INIT_TIMEOUT = 0x8000402A

#
# MessageId: CO_E_NO_SECCTX_IN_ACTIVATE
#
# MessageText:
#
# Unable to complete the call since there is no COM+ security context inside IObjectControl.Activate.
#
CO_E_NO_SECCTX_IN_ACTIVATE = 0x8000402B

#
# MessageId: CO_E_TRACKER_CONFIG
#
# MessageText:
#
# The provided tracker configuration is invalid
#
CO_E_TRACKER_CONFIG = 0x80004030

#
# MessageId: CO_E_THREADPOOL_CONFIG
#
# MessageText:
#
# The provided thread pool configuration is invalid
#
CO_E_THREADPOOL_CONFIG = 0x80004031

#
# MessageId: CO_E_SXS_CONFIG
#
# MessageText:
#
# The provided side-by-side configuration is invalid
#
CO_E_SXS_CONFIG = 0x80004032

#
# MessageId: CO_E_MALFORMED_SPN
#
# MessageText:
#
# The server principal name (SPN) obtained during security negotiation is malformed.
#
CO_E_MALFORMED_SPN = 0x80004033

#
# MessageId: CO_E_UNREVOKED_REGISTRATION_ON_APARTMENT_SHUTDOWN
#
# MessageText:
#
# The caller failed to revoke a per-apartment registration before apartment shutdown.
#
CO_E_UNREVOKED_REGISTRATION_ON_APARTMENT_SHUTDOWN = 0x80004034

#
# MessageId: CO_E_PREMATURE_STUB_RUNDOWN
#
# MessageText:
#
# The object has been rundown by the stub manager while there are external clients.
#
CO_E_PREMATURE_STUB_RUNDOWN = 0x80004035


#
# Success codes
#
#define S_OK                                   ((HRESULT)0L)
#define S_FALSE                                ((HRESULT)1L)

# ******************
# FACILITY_ITF
# ******************

#
# Codes 0x0-0x01ff are reserved for the OLE group of
# interfaces.
#


#
# Generic OLE errors that may be returned by many inerfaces
#

#define OLE_E_FIRST ((HRESULT)0x80040000L)
#define OLE_E_LAST  ((HRESULT)0x800400FFL)
#define OLE_S_FIRST ((HRESULT)0x00040000L)
#define OLE_S_LAST  ((HRESULT)0x000400FFL)

#
# Old OLE errors
#
#
# MessageId: OLE_E_OLEVERB
#
# MessageText:
#
# Invalid OLEVERB structure
#
OLE_E_OLEVERB = 0x80040000

#
# MessageId: OLE_E_ADVF
#
# MessageText:
#
# Invalid advise flags
#
OLE_E_ADVF = 0x80040001

#
# MessageId: OLE_E_ENUM_NOMORE
#
# MessageText:
#
# Can't enumerate any more, because the associated data is missing
#
OLE_E_ENUM_NOMORE = 0x80040002

#
# MessageId: OLE_E_ADVISENOTSUPPORTED
#
# MessageText:
#
# This implementation doesn't take advises
#
OLE_E_ADVISENOTSUPPORTED = 0x80040003

#
# MessageId: OLE_E_NOCONNECTION
#
# MessageText:
#
# There is no connection for this connection ID
#
OLE_E_NOCONNECTION = 0x80040004

#
# MessageId: OLE_E_NOTRUNNING
#
# MessageText:
#
# Need to run the object to perform this operation
#
OLE_E_NOTRUNNING = 0x80040005

#
# MessageId: OLE_E_NOCACHE
#
# MessageText:
#
# There is no cache to operate on
#
OLE_E_NOCACHE = 0x80040006

#
# MessageId: OLE_E_BLANK
#
# MessageText:
#
# Uninitialized object
#
OLE_E_BLANK = 0x80040007

#
# MessageId: OLE_E_CLASSDIFF
#
# MessageText:
#
# Linked object's source class has changed
#
OLE_E_CLASSDIFF = 0x80040008

#
# MessageId: OLE_E_CANT_GETMONIKER
#
# MessageText:
#
# Not able to get the moniker of the object
#
OLE_E_CANT_GETMONIKER = 0x80040009

#
# MessageId: OLE_E_CANT_BINDTOSOURCE
#
# MessageText:
#
# Not able to bind to the source
#
OLE_E_CANT_BINDTOSOURCE = 0x8004000A

#
# MessageId: OLE_E_STATIC
#
# MessageText:
#
# Object is static; operation not allowed
#
OLE_E_STATIC = 0x8004000B

#
# MessageId: OLE_E_PROMPTSAVECANCELLED
#
# MessageText:
#
# User canceled out of save dialog
#
OLE_E_PROMPTSAVECANCELLED = 0x8004000C

#
# MessageId: OLE_E_INVALIDRECT
#
# MessageText:
#
# Invalid rectangle
#
OLE_E_INVALIDRECT = 0x8004000D

#
# MessageId: OLE_E_WRONGCOMPOBJ
#
# MessageText:
#
# compobj.dll is too old for the ole2.dll initialized
#
OLE_E_WRONGCOMPOBJ = 0x8004000E

#
# MessageId: OLE_E_INVALIDHWND
#
# MessageText:
#
# Invalid window handle
#
OLE_E_INVALIDHWND = 0x8004000F

#
# MessageId: OLE_E_NOT_INPLACEACTIVE
#
# MessageText:
#
# Object is not in any of the inplace active states
#
OLE_E_NOT_INPLACEACTIVE = 0x80040010

#
# MessageId: OLE_E_CANTCONVERT
#
# MessageText:
#
# Not able to convert object
#
OLE_E_CANTCONVERT = 0x80040011

#
# MessageId: OLE_E_NOSTORAGE
#
# MessageText:
#
# Not able to perform the operation because object is not given storage yet
#
OLE_E_NOSTORAGE = 0x80040012

#
# MessageId: DV_E_FORMATETC
#
# MessageText:
#
# Invalid FORMATETC structure
#
DV_E_FORMATETC = 0x80040064

#
# MessageId: DV_E_DVTARGETDEVICE
#
# MessageText:
#
# Invalid DVTARGETDEVICE structure
#
DV_E_DVTARGETDEVICE = 0x80040065

#
# MessageId: DV_E_STGMEDIUM
#
# MessageText:
#
# Invalid STDGMEDIUM structure
#
DV_E_STGMEDIUM = 0x80040066

#
# MessageId: DV_E_STATDATA
#
# MessageText:
#
# Invalid STATDATA structure
#
DV_E_STATDATA = 0x80040067

#
# MessageId: DV_E_LINDEX
#
# MessageText:
#
# Invalid lindex
#
DV_E_LINDEX = 0x80040068

#
# MessageId: DV_E_TYMED
#
# MessageText:
#
# Invalid tymed
#
DV_E_TYMED = 0x80040069

#
# MessageId: DV_E_CLIPFORMAT
#
# MessageText:
#
# Invalid clipboard format
#
DV_E_CLIPFORMAT = 0x8004006A

#
# MessageId: DV_E_DVASPECT
#
# MessageText:
#
# Invalid aspect(s)
#
DV_E_DVASPECT = 0x8004006B

#
# MessageId: DV_E_DVTARGETDEVICE_SIZE
#
# MessageText:
#
# tdSize parameter of the DVTARGETDEVICE structure is invalid
#
DV_E_DVTARGETDEVICE_SIZE = 0x8004006C

#
# MessageId: DV_E_NOIVIEWOBJECT
#
# MessageText:
#
# Object doesn't support IViewObject interface
#
DV_E_NOIVIEWOBJECT = 0x8004006D

DRAGDROP_E_FIRST = 0
DRAGDROP_E_LAST = 0
DRAGDROP_S_FIRST = 0
DRAGDROP_S_LAST = 0
#
# MessageId: DRAGDROP_E_NOTREGISTERED
#
# MessageText:
#
# Trying to revoke a drop target that has not been registered
#
DRAGDROP_E_NOTREGISTERED = 0x80040100

#
# MessageId: DRAGDROP_E_ALREADYREGISTERED
#
# MessageText:
#
# This window has already been registered as a drop target
#
DRAGDROP_E_ALREADYREGISTERED = 0x80040101

#
# MessageId: DRAGDROP_E_INVALIDHWND
#
# MessageText:
#
# Invalid window handle
#
DRAGDROP_E_INVALIDHWND = 0x80040102

#
# MessageId: DRAGDROP_E_CONCURRENT_DRAG_ATTEMPTED
#
# MessageText:
#
# A drag operation is already in progress
#
DRAGDROP_E_CONCURRENT_DRAG_ATTEMPTED = 0x80040103

CLASSFACTORY_E_FIRST = 0
CLASSFACTORY_E_LAST = 0
CLASSFACTORY_S_FIRST = 0
CLASSFACTORY_S_LAST = 0
#
# MessageId: CLASS_E_NOAGGREGATION
#
# MessageText:
#
# Class does not support aggregation (or class object is remote)
#
CLASS_E_NOAGGREGATION = 0x80040110

#
# MessageId: CLASS_E_CLASSNOTAVAILABLE
#
# MessageText:
#
# ClassFactory cannot supply requested class
#
CLASS_E_CLASSNOTAVAILABLE = 0x80040111

#
# MessageId: CLASS_E_NOTLICENSED
#
# MessageText:
#
# Class is not licensed for use
#
CLASS_E_NOTLICENSED = 0x80040112

MARSHAL_E_FIRST = 0
MARSHAL_E_LAST = 0
MARSHAL_S_FIRST = 0
MARSHAL_S_LAST = 0
DATA_E_FIRST = 0
DATA_E_LAST = 0
DATA_S_FIRST = 0
DATA_S_LAST = 0
VIEW_E_FIRST = 0
VIEW_E_LAST = 0
VIEW_S_FIRST = 0
VIEW_S_LAST = 0
#
# MessageId: VIEW_E_DRAW
#
# MessageText:
#
# Error drawing view
#
VIEW_E_DRAW = 0x80040140

REGDB_E_FIRST = 0
REGDB_E_LAST = 0
REGDB_S_FIRST = 0
REGDB_S_LAST = 0
#
# MessageId: REGDB_E_READREGDB
#
# MessageText:
#
# Could not read key from registry
#
REGDB_E_READREGDB = 0x80040150

#
# MessageId: REGDB_E_WRITEREGDB
#
# MessageText:
#
# Could not write key to registry
#
REGDB_E_WRITEREGDB = 0x80040151

#
# MessageId: REGDB_E_KEYMISSING
#
# MessageText:
#
# Could not find the key in the registry
#
REGDB_E_KEYMISSING = 0x80040152

#
# MessageId: REGDB_E_INVALIDVALUE
#
# MessageText:
#
# Invalid value for registry
#
REGDB_E_INVALIDVALUE = 0x80040153

#
# MessageId: REGDB_E_CLASSNOTREG
#
# MessageText:
#
# Class not registered
#
REGDB_E_CLASSNOTREG = 0x80040154

#
# MessageId: REGDB_E_IIDNOTREG
#
# MessageText:
#
# Interface not registered
#
REGDB_E_IIDNOTREG = 0x80040155

#
# MessageId: REGDB_E_BADTHREADINGMODEL
#
# MessageText:
#
# Threading model entry is not valid
#
REGDB_E_BADTHREADINGMODEL = 0x80040156

CAT_E_FIRST = 0
CAT_E_LAST = 0
#
# MessageId: CAT_E_CATIDNOEXIST
#
# MessageText:
#
# CATID does not exist
#
CAT_E_CATIDNOEXIST = 0x80040160

#
# MessageId: CAT_E_NODESCRIPTION
#
# MessageText:
#
# Description not found
#
CAT_E_NODESCRIPTION = 0x80040161

#//////////////////////////////////
#                                //
#     Class Store Error Codes    //
#                                //
#//////////////////////////////////
CS_E_FIRST = 0
CS_E_LAST = 0
#
# MessageId: CS_E_PACKAGE_NOTFOUND
#
# MessageText:
#
# No package in the software installation data in the Active Directory meets this criteria.
#
CS_E_PACKAGE_NOTFOUND = 0x80040164

#
# MessageId: CS_E_NOT_DELETABLE
#
# MessageText:
#
# Deleting this will break the referential integrity of the software installation data in the Active Directory.
#
CS_E_NOT_DELETABLE = 0x80040165

#
# MessageId: CS_E_CLASS_NOTFOUND
#
# MessageText:
#
# The CLSID was not found in the software installation data in the Active Directory.
#
CS_E_CLASS_NOTFOUND = 0x80040166

#
# MessageId: CS_E_INVALID_VERSION
#
# MessageText:
#
# The software installation data in the Active Directory is corrupt.
#
CS_E_INVALID_VERSION = 0x80040167

#
# MessageId: CS_E_NO_CLASSSTORE
#
# MessageText:
#
# There is no software installation data in the Active Directory.
#
CS_E_NO_CLASSSTORE = 0x80040168

#
# MessageId: CS_E_OBJECT_NOTFOUND
#
# MessageText:
#
# There is no software installation data object in the Active Directory.
#
CS_E_OBJECT_NOTFOUND = 0x80040169

#
# MessageId: CS_E_OBJECT_ALREADY_EXISTS
#
# MessageText:
#
# The software installation data object in the Active Directory already exists.
#
CS_E_OBJECT_ALREADY_EXISTS = 0x8004016A

#
# MessageId: CS_E_INVALID_PATH
#
# MessageText:
#
# The path to the software installation data in the Active Directory is not correct.
#
CS_E_INVALID_PATH = 0x8004016B

#
# MessageId: CS_E_NETWORK_ERROR
#
# MessageText:
#
# A network error interrupted the operation.
#
CS_E_NETWORK_ERROR = 0x8004016C

#
# MessageId: CS_E_ADMIN_LIMIT_EXCEEDED
#
# MessageText:
#
# The size of this object exceeds the maximum size set by the Administrator.
#
CS_E_ADMIN_LIMIT_EXCEEDED = 0x8004016D

#
# MessageId: CS_E_SCHEMA_MISMATCH
#
# MessageText:
#
# The schema for the software installation data in the Active Directory does not match the required schema.
#
CS_E_SCHEMA_MISMATCH = 0x8004016E

#
# MessageId: CS_E_INTERNAL_ERROR
#
# MessageText:
#
# An error occurred in the software installation data in the Active Directory.
#
CS_E_INTERNAL_ERROR = 0x8004016F

CACHE_E_FIRST = 0
CACHE_E_LAST = 0
CACHE_S_FIRST = 0
CACHE_S_LAST = 0
#
# MessageId: CACHE_E_NOCACHE_UPDATED
#
# MessageText:
#
# Cache not updated
#
CACHE_E_NOCACHE_UPDATED = 0x80040170

OLEOBJ_E_FIRST = 0
OLEOBJ_E_LAST = 0
OLEOBJ_S_FIRST = 0
OLEOBJ_S_LAST = 0
#
# MessageId: OLEOBJ_E_NOVERBS
#
# MessageText:
#
# No verbs for OLE object
#
OLEOBJ_E_NOVERBS = 0x80040180

#
# MessageId: OLEOBJ_E_INVALIDVERB
#
# MessageText:
#
# Invalid verb for OLE object
#
OLEOBJ_E_INVALIDVERB = 0x80040181

CLIENTSITE_E_FIRST = 0
CLIENTSITE_E_LAST = 0
CLIENTSITE_S_FIRST = 0
CLIENTSITE_S_LAST = 0
#
# MessageId: INPLACE_E_NOTUNDOABLE
#
# MessageText:
#
# Undo is not available
#
INPLACE_E_NOTUNDOABLE = 0x800401A0

#
# MessageId: INPLACE_E_NOTOOLSPACE
#
# MessageText:
#
# Space for tools is not available
#
INPLACE_E_NOTOOLSPACE = 0x800401A1

INPLACE_E_FIRST = 0
INPLACE_E_LAST = 0
INPLACE_S_FIRST = 0
INPLACE_S_LAST = 0
ENUM_E_FIRST = 0
ENUM_E_LAST = 0
ENUM_S_FIRST = 0
ENUM_S_LAST = 0
CONVERT10_E_FIRST = 0
CONVERT10_E_LAST = 0
CONVERT10_S_FIRST = 0
CONVERT10_S_LAST = 0
#
# MessageId: CONVERT10_E_OLESTREAM_GET
#
# MessageText:
#
# OLESTREAM Get method failed
#
CONVERT1 = 0

#
# MessageId: CONVERT10_E_OLESTREAM_PUT
#
# MessageText:
#
# OLESTREAM Put method failed
#
CONVERT1 = 0

#
# MessageId: CONVERT10_E_OLESTREAM_FMT
#
# MessageText:
#
# Contents of the OLESTREAM not in correct format
#
CONVERT1 = 0

#
# MessageId: CONVERT10_E_OLESTREAM_BITMAP_TO_DIB
#
# MessageText:
#
# There was an error in a Windows GDI call while converting the bitmap to a DIB
#
CONVERT1 = 0

#
# MessageId: CONVERT10_E_STG_FMT
#
# MessageText:
#
# Contents of the IStorage not in correct format
#
CONVERT1 = 0

#
# MessageId: CONVERT10_E_STG_NO_STD_STREAM
#
# MessageText:
#
# Contents of IStorage is missing one of the standard streams
#
CONVERT1 = 0

#
# MessageId: CONVERT10_E_STG_DIB_TO_BITMAP
#
# MessageText:
#
# There was an error in a Windows GDI call while converting the DIB to a bitmap.
#
CONVERT1 = 0

CLIPBRD_E_FIRST = 0
CLIPBRD_E_LAST = 0
CLIPBRD_S_FIRST = 0
CLIPBRD_S_LAST = 0
#
# MessageId: CLIPBRD_E_CANT_OPEN
#
# MessageText:
#
# OpenClipboard Failed
#
CLIPBRD_E_CANT_OPEN = 0x800401D0

#
# MessageId: CLIPBRD_E_CANT_EMPTY
#
# MessageText:
#
# EmptyClipboard Failed
#
CLIPBRD_E_CANT_EMPTY = 0x800401D1

#
# MessageId: CLIPBRD_E_CANT_SET
#
# MessageText:
#
# SetClipboard Failed
#
CLIPBRD_E_CANT_SET = 0x800401D2

#
# MessageId: CLIPBRD_E_BAD_DATA
#
# MessageText:
#
# Data on clipboard is invalid
#
CLIPBRD_E_BAD_DATA = 0x800401D3

#
# MessageId: CLIPBRD_E_CANT_CLOSE
#
# MessageText:
#
# CloseClipboard Failed
#
CLIPBRD_E_CANT_CLOSE = 0x800401D4

MK_E_FIRST = 0
MK_E_LAST = 0
MK_S_FIRST = 0
MK_S_LAST = 0
#
# MessageId: MK_E_CONNECTMANUALLY
#
# MessageText:
#
# Moniker needs to be connected manually
#
MK_E_CONNECTMANUALLY = 0x800401E0

#
# MessageId: MK_E_EXCEEDEDDEADLINE
#
# MessageText:
#
# Operation exceeded deadline
#
MK_E_EXCEEDEDDEADLINE = 0x800401E1

#
# MessageId: MK_E_NEEDGENERIC
#
# MessageText:
#
# Moniker needs to be generic
#
MK_E_NEEDGENERIC = 0x800401E2

#
# MessageId: MK_E_UNAVAILABLE
#
# MessageText:
#
# Operation unavailable
#
MK_E_UNAVAILABLE = 0x800401E3

#
# MessageId: MK_E_SYNTAX
#
# MessageText:
#
# Invalid syntax
#
MK_E_SYNTAX = 0x800401E4

#
# MessageId: MK_E_NOOBJECT
#
# MessageText:
#
# No object for moniker
#
MK_E_NOOBJECT = 0x800401E5

#
# MessageId: MK_E_INVALIDEXTENSION
#
# MessageText:
#
# Bad extension for file
#
MK_E_INVALIDEXTENSION = 0x800401E6

#
# MessageId: MK_E_INTERMEDIATEINTERFACENOTSUPPORTED
#
# MessageText:
#
# Intermediate operation failed
#
MK_E_INTERMEDIATEINTERFACENOTSUPPORTED = 0x800401E7

#
# MessageId: MK_E_NOTBINDABLE
#
# MessageText:
#
# Moniker is not bindable
#
MK_E_NOTBINDABLE = 0x800401E8

#
# MessageId: MK_E_NOTBOUND
#
# MessageText:
#
# Moniker is not bound
#
MK_E_NOTBOUND = 0x800401E9

#
# MessageId: MK_E_CANTOPENFILE
#
# MessageText:
#
# Moniker cannot open file
#
MK_E_CANTOPENFILE = 0x800401EA

#
# MessageId: MK_E_MUSTBOTHERUSER
#
# MessageText:
#
# User input required for operation to succeed
#
MK_E_MUSTBOTHERUSER = 0x800401EB

#
# MessageId: MK_E_NOINVERSE
#
# MessageText:
#
# Moniker class has no inverse
#
MK_E_NOINVERSE = 0x800401EC

#
# MessageId: MK_E_NOSTORAGE
#
# MessageText:
#
# Moniker does not refer to storage
#
MK_E_NOSTORAGE = 0x800401ED

#
# MessageId: MK_E_NOPREFIX
#
# MessageText:
#
# No common prefix
#
MK_E_NOPREFIX = 0x800401EE

#
# MessageId: MK_E_ENUMERATION_FAILED
#
# MessageText:
#
# Moniker could not be enumerated
#
MK_E_ENUMERATION_FAILED = 0x800401EF

CO_E_FIRST = 0
CO_E_LAST = 0
CO_S_FIRST = 0
CO_S_LAST = 0
#
# MessageId: CO_E_NOTINITIALIZED
#
# MessageText:
#
# CoInitialize has not been called.
#
CO_E_NOTINITIALIZED = 0x800401F0

#
# MessageId: CO_E_ALREADYINITIALIZED
#
# MessageText:
#
# CoInitialize has already been called.
#
CO_E_ALREADYINITIALIZED = 0x800401F1

#
# MessageId: CO_E_CANTDETERMINECLASS
#
# MessageText:
#
# Class of object cannot be determined
#
CO_E_CANTDETERMINECLASS = 0x800401F2

#
# MessageId: CO_E_CLASSSTRING
#
# MessageText:
#
# Invalid class string
#
CO_E_CLASSSTRING = 0x800401F3

#
# MessageId: CO_E_IIDSTRING
#
# MessageText:
#
# Invalid interface string
#
CO_E_IIDSTRING = 0x800401F4

#
# MessageId: CO_E_APPNOTFOUND
#
# MessageText:
#
# Application not found
#
CO_E_APPNOTFOUND = 0x800401F5

#
# MessageId: CO_E_APPSINGLEUSE
#
# MessageText:
#
# Application cannot be run more than once
#
CO_E_APPSINGLEUSE = 0x800401F6

#
# MessageId: CO_E_ERRORINAPP
#
# MessageText:
#
# Some error in application program
#
CO_E_ERRORINAPP = 0x800401F7

#
# MessageId: CO_E_DLLNOTFOUND
#
# MessageText:
#
# DLL for class not found
#
CO_E_DLLNOTFOUND = 0x800401F8

#
# MessageId: CO_E_ERRORINDLL
#
# MessageText:
#
# Error in the DLL
#
CO_E_ERRORINDLL = 0x800401F9

#
# MessageId: CO_E_WRONGOSFORAPP
#
# MessageText:
#
# Wrong OS or OS version for application
#
CO_E_WRONGOSFORAPP = 0x800401FA

#
# MessageId: CO_E_OBJNOTREG
#
# MessageText:
#
# Object is not registered
#
CO_E_OBJNOTREG = 0x800401FB

#
# MessageId: CO_E_OBJISREG
#
# MessageText:
#
# Object is already registered
#
CO_E_OBJISREG = 0x800401FC

#
# MessageId: CO_E_OBJNOTCONNECTED
#
# MessageText:
#
# Object is not connected to server
#
CO_E_OBJNOTCONNECTED = 0x800401FD

#
# MessageId: CO_E_APPDIDNTREG
#
# MessageText:
#
# Application was launched but it didn't register a class factory
#
CO_E_APPDIDNTREG = 0x800401FE

#
# MessageId: CO_E_RELEASED
#
# MessageText:
#
# Object has been released
#
CO_E_RELEASED = 0x800401FF

EVENT_E_FIRST = 0
EVENT_E_LAST = 0
EVENT_S_FIRST = 0
EVENT_S_LAST = 0
#
# MessageId: EVENT_S_SOME_SUBSCRIBERS_FAILED
#
# MessageText:
#
# An event was able to invoke some but not all of the subscribers
#
EVENT_S_SOME_SUBSCRIBERS_FAILED = 0x00040200

#
# MessageId: EVENT_E_ALL_SUBSCRIBERS_FAILED
#
# MessageText:
#
# An event was unable to invoke any of the subscribers
#
EVENT_E_ALL_SUBSCRIBERS_FAILED = 0x80040201

#
# MessageId: EVENT_S_NOSUBSCRIBERS
#
# MessageText:
#
# An event was delivered but there were no subscribers
#
EVENT_S_NOSUBSCRIBERS = 0x00040202

#
# MessageId: EVENT_E_QUERYSYNTAX
#
# MessageText:
#
# A syntax error occurred trying to evaluate a query string
#
EVENT_E_QUERYSYNTAX = 0x80040203

#
# MessageId: EVENT_E_QUERYFIELD
#
# MessageText:
#
# An invalid field name was used in a query string
#
EVENT_E_QUERYFIELD = 0x80040204

#
# MessageId: EVENT_E_INTERNALEXCEPTION
#
# MessageText:
#
# An unexpected exception was raised
#
EVENT_E_INTERNALEXCEPTION = 0x80040205

#
# MessageId: EVENT_E_INTERNALERROR
#
# MessageText:
#
# An unexpected internal error was detected
#
EVENT_E_INTERNALERROR = 0x80040206

#
# MessageId: EVENT_E_INVALID_PER_USER_SID
#
# MessageText:
#
# The owner SID on a per-user subscription doesn't exist
#
EVENT_E_INVALID_PER_USER_SID = 0x80040207

#
# MessageId: EVENT_E_USER_EXCEPTION
#
# MessageText:
#
# A user-supplied component or subscriber raised an exception
#
EVENT_E_USER_EXCEPTION = 0x80040208

#
# MessageId: EVENT_E_TOO_MANY_METHODS
#
# MessageText:
#
# An interface has too many methods to fire events from
#
EVENT_E_TOO_MANY_METHODS = 0x80040209

#
# MessageId: EVENT_E_MISSING_EVENTCLASS
#
# MessageText:
#
# A subscription cannot be stored unless its event class already exists
#
EVENT_E_MISSING_EVENTCLASS = 0x8004020A

#
# MessageId: EVENT_E_NOT_ALL_REMOVED
#
# MessageText:
#
# Not all the objects requested could be removed
#
EVENT_E_NOT_ALL_REMOVED = 0x8004020B

#
# MessageId: EVENT_E_COMPLUS_NOT_INSTALLED
#
# MessageText:
#
# COM+ is required for this operation, but is not installed
#
EVENT_E_COMPLUS_NOT_INSTALLED = 0x8004020C

#
# MessageId: EVENT_E_CANT_MODIFY_OR_DELETE_UNCONFIGURED_OBJECT
#
# MessageText:
#
# Cannot modify or delete an object that was not added using the COM+ Admin SDK
#
EVENT_E_CANT_MODIFY_OR_DELETE_UNCONFIGURED_OBJECT = 0x8004020D

#
# MessageId: EVENT_E_CANT_MODIFY_OR_DELETE_CONFIGURED_OBJECT
#
# MessageText:
#
# Cannot modify or delete an object that was added using the COM+ Admin SDK
#
EVENT_E_CANT_MODIFY_OR_DELETE_CONFIGURED_OBJECT = 0x8004020E

#
# MessageId: EVENT_E_INVALID_EVENT_CLASS_PARTITION
#
# MessageText:
#
# The event class for this subscription is in an invalid partition
#
EVENT_E_INVALID_EVENT_CLASS_PARTITION = 0x8004020F

#
# MessageId: EVENT_E_PER_USER_SID_NOT_LOGGED_ON
#
# MessageText:
#
# The owner of the PerUser subscription is not logged on to the system specified
#
EVENT_E_PER_USER_SID_NOT_LOGGED_ON = 0x80040210

#
# MessageId: TPC_E_INVALID_PROPERTY
#
# MessageText:
#
# TabletPC inking error code. The property was not found, or supported by the recognizer
#
TPC_E_INVALID_PROPERTY = 0x80040241

#
# MessageId: TPC_E_NO_DEFAULT_TABLET
#
# MessageText:
#
# TabletPC inking error code. No default tablet
#
TPC_E_NO_DEFAULT_TABLET = 0x80040212

#
# MessageId: TPC_E_UNKNOWN_PROPERTY
#
# MessageText:
#
# TabletPC inking error code. Unknown property specified
#
TPC_E_UNKNOWN_PROPERTY = 0x8004021B

#
# MessageId: TPC_E_INVALID_INPUT_RECT
#
# MessageText:
#
# TabletPC inking error code. An invalid input rectangle was specified
#
TPC_E_INVALID_INPUT_RECT = 0x80040219

#
# MessageId: TPC_E_INVALID_STROKE
#
# MessageText:
#
# TabletPC inking error code. The stroke object was deleted
#
TPC_E_INVALID_STROKE = 0x80040222

#
# MessageId: TPC_E_INITIALIZE_FAIL
#
# MessageText:
#
# TabletPC inking error code. Initialization failure
#
TPC_E_INITIALIZE_FAIL = 0x80040223

#
# MessageId: TPC_E_NOT_RELEVANT
#
# MessageText:
#
# TabletPC inking error code. The data required for the operation was not supplied
#
TPC_E_NOT_RELEVANT = 0x80040232

#
# MessageId: TPC_E_INVALID_PACKET_DESCRIPTION
#
# MessageText:
#
# TabletPC inking error code. Invalid packet description
#
TPC_E_INVALID_PACKET_DESCRIPTION = 0x80040233

#
# MessageId: TPC_E_RECOGNIZER_NOT_REGISTERED
#
# MessageText:
#
# TabletPC inking error code. There are no handwriting recognizers registered
#
TPC_E_RECOGNIZER_NOT_REGISTERED = 0x80040235

#
# MessageId: TPC_E_INVALID_RIGHTS
#
# MessageText:
#
# TabletPC inking error code. User does not have the necessary rights to read recognizer information
#
TPC_E_INVALID_RIGHTS = 0x80040236

#
# MessageId: TPC_E_OUT_OF_ORDER_CALL
#
# MessageText:
#
# TabletPC inking error code. API calls were made in an incorrect order
#
TPC_E_OUT_OF_ORDER_CALL = 0x80040237

#
# MessageId: TPC_E_QUEUE_FULL
#
# MessageText:
#
# TabletPC inking error code. Queue is full
#
TPC_E_QUEUE_FULL = 0x80040238

#
# MessageId: TPC_E_INVALID_CONFIGURATION
#
# MessageText:
#
# TabletPC inking error code. RtpEnabled called multiple times
#
TPC_E_INVALID_CONFIGURATION = 0x80040239

#
# MessageId: TPC_E_INVALID_DATA_FROM_RECOGNIZER
#
# MessageText:
#
# TabletPC inking error code. A recognizer returned invalid data
#
TPC_E_INVALID_DATA_FROM_RECOGNIZER = 0x8004023A

#
# MessageId: TPC_S_TRUNCATED
#
# MessageText:
#
# TabletPC inking error code. String was truncated
#
TPC_S_TRUNCATED = 0x00040252

#
# MessageId: TPC_S_INTERRUPTED
#
# MessageText:
#
# TabletPC inking error code. Recognition or training was interrupted
#
TPC_S_INTERRUPTED = 0x00040253

#
# MessageId: TPC_S_NO_DATA_TO_PROCESS
#
# MessageText:
#
# TabletPC inking error code. No personalization update to the recognizer because no training data found
#
TPC_S_NO_DATA_TO_PROCESS = 0x00040254

XACT_E_FIRST = 0
XACT_E_LAST = 0
XACT_S_FIRST = 0
XACT_S_LAST = 0
#
# MessageId: XACT_E_ALREADYOTHERSINGLEPHASE
#
# MessageText:
#
# Another single phase resource manager has already been enlisted in this transaction.
#
XACT_E_ALREADYOTHERSINGLEPHASE = 0x8004D000

#
# MessageId: XACT_E_CANTRETAIN
#
# MessageText:
#
# A retaining commit or abort is not supported
#
XACT_E_CANTRETAIN = 0x8004D001

#
# MessageId: XACT_E_COMMITFAILED
#
# MessageText:
#
# The transaction failed to commit for an unknown reason. The transaction was aborted.
#
XACT_E_COMMITFAILED = 0x8004D002

#
# MessageId: XACT_E_COMMITPREVENTED
#
# MessageText:
#
# Cannot call commit on this transaction object because the calling application did not initiate the transaction.
#
XACT_E_COMMITPREVENTED = 0x8004D003

#
# MessageId: XACT_E_HEURISTICABORT
#
# MessageText:
#
# Instead of committing, the resource heuristically aborted.
#
XACT_E_HEURISTICABORT = 0x8004D004

#
# MessageId: XACT_E_HEURISTICCOMMIT
#
# MessageText:
#
# Instead of aborting, the resource heuristically committed.
#
XACT_E_HEURISTICCOMMIT = 0x8004D005

#
# MessageId: XACT_E_HEURISTICDAMAGE
#
# MessageText:
#
# Some of the states of the resource were committed while others were aborted, likely because of heuristic decisions.
#
XACT_E_HEURISTICDAMAGE = 0x8004D006

#
# MessageId: XACT_E_HEURISTICDANGER
#
# MessageText:
#
# Some of the states of the resource may have been committed while others may have been aborted, likely because of heuristic decisions.
#
XACT_E_HEURISTICDANGER = 0x8004D007

#
# MessageId: XACT_E_ISOLATIONLEVEL
#
# MessageText:
#
# The requested isolation level is not valid or supported.
#
XACT_E_ISOLATIONLEVEL = 0x8004D008

#
# MessageId: XACT_E_NOASYNC
#
# MessageText:
#
# The transaction manager doesn't support an asynchronous operation for this method.
#
XACT_E_NOASYNC = 0x8004D009

#
# MessageId: XACT_E_NOENLIST
#
# MessageText:
#
# Unable to enlist in the transaction.
#
XACT_E_NOENLIST = 0x8004D00A

#
# MessageId: XACT_E_NOISORETAIN
#
# MessageText:
#
# The requested semantics of retention of isolation across retaining commit and abort boundaries cannot be supported by this transaction implementation, or isoFlags was not equal to zero.
#
XACT_E_NOISORETAIN = 0x8004D00B

#
# MessageId: XACT_E_NORESOURCE
#
# MessageText:
#
# There is no resource presently associated with this enlistment
#
XACT_E_NORESOURCE = 0x8004D00C

#
# MessageId: XACT_E_NOTCURRENT
#
# MessageText:
#
# The transaction failed to commit due to the failure of optimistic concurrency control in at least one of the resource managers.
#
XACT_E_NOTCURRENT = 0x8004D00D

#
# MessageId: XACT_E_NOTRANSACTION
#
# MessageText:
#
# The transaction has already been implicitly or explicitly committed or aborted
#
XACT_E_NOTRANSACTION = 0x8004D00E

#
# MessageId: XACT_E_NOTSUPPORTED
#
# MessageText:
#
# An invalid combination of flags was specified
#
XACT_E_NOTSUPPORTED = 0x8004D00F

#
# MessageId: XACT_E_UNKNOWNRMGRID
#
# MessageText:
#
# The resource manager id is not associated with this transaction or the transaction manager.
#
XACT_E_UNKNOWNRMGRID = 0x8004D010

#
# MessageId: XACT_E_WRONGSTATE
#
# MessageText:
#
# This method was called in the wrong state
#
XACT_E_WRONGSTATE = 0x8004D011

#
# MessageId: XACT_E_WRONGUOW
#
# MessageText:
#
# The indicated unit of work does not match the unit of work expected by the resource manager.
#
XACT_E_WRONGUOW = 0x8004D012

#
# MessageId: XACT_E_XTIONEXISTS
#
# MessageText:
#
# An enlistment in a transaction already exists.
#
XACT_E_XTIONEXISTS = 0x8004D013

#
# MessageId: XACT_E_NOIMPORTOBJECT
#
# MessageText:
#
# An import object for the transaction could not be found.
#
XACT_E_NOIMPORTOBJECT = 0x8004D014

#
# MessageId: XACT_E_INVALIDCOOKIE
#
# MessageText:
#
# The transaction cookie is invalid.
#
XACT_E_INVALIDCOOKIE = 0x8004D015

#
# MessageId: XACT_E_INDOUBT
#
# MessageText:
#
# The transaction status is in doubt. A communication failure occurred, or a transaction manager or resource manager has failed
#
XACT_E_INDOUBT = 0x8004D016

#
# MessageId: XACT_E_NOTIMEOUT
#
# MessageText:
#
# A time-out was specified, but time-outs are not supported.
#
XACT_E_NOTIMEOUT = 0x8004D017

#
# MessageId: XACT_E_ALREADYINPROGRESS
#
# MessageText:
#
# The requested operation is already in progress for the transaction.
#
XACT_E_ALREADYINPROGRESS = 0x8004D018

#
# MessageId: XACT_E_ABORTED
#
# MessageText:
#
# The transaction has already been aborted.
#
XACT_E_ABORTED = 0x8004D019

#
# MessageId: XACT_E_LOGFULL
#
# MessageText:
#
# The Transaction Manager returned a log full error.
#
XACT_E_LOGFULL = 0x8004D01A

#
# MessageId: XACT_E_TMNOTAVAILABLE
#
# MessageText:
#
# The Transaction Manager is not available.
#
XACT_E_TMNOTAVAILABLE = 0x8004D01B

#
# MessageId: XACT_E_CONNECTION_DOWN
#
# MessageText:
#
# A connection with the transaction manager was lost.
#
XACT_E_CONNECTION_DOWN = 0x8004D01C

#
# MessageId: XACT_E_CONNECTION_DENIED
#
# MessageText:
#
# A request to establish a connection with the transaction manager was denied.
#
XACT_E_CONNECTION_DENIED = 0x8004D01D

#
# MessageId: XACT_E_REENLISTTIMEOUT
#
# MessageText:
#
# Resource manager reenlistment to determine transaction status timed out.
#
XACT_E_REENLISTTIMEOUT = 0x8004D01E

#
# MessageId: XACT_E_TIP_CONNECT_FAILED
#
# MessageText:
#
# This transaction manager failed to establish a connection with another TIP transaction manager.
#
XACT_E_TIP_CONNECT_FAILED = 0x8004D01F

#
# MessageId: XACT_E_TIP_PROTOCOL_ERROR
#
# MessageText:
#
# This transaction manager encountered a protocol error with another TIP transaction manager.
#
XACT_E_TIP_PROTOCOL_ERROR = 0x8004D020

#
# MessageId: XACT_E_TIP_PULL_FAILED
#
# MessageText:
#
# This transaction manager could not propagate a transaction from another TIP transaction manager.
#
XACT_E_TIP_PULL_FAILED = 0x8004D021

#
# MessageId: XACT_E_DEST_TMNOTAVAILABLE
#
# MessageText:
#
# The Transaction Manager on the destination machine is not available.
#
XACT_E_DEST_TMNOTAVAILABLE = 0x8004D022

#
# MessageId: XACT_E_TIP_DISABLED
#
# MessageText:
#
# The Transaction Manager has disabled its support for TIP.
#
XACT_E_TIP_DISABLED = 0x8004D023

#
# MessageId: XACT_E_NETWORK_TX_DISABLED
#
# MessageText:
#
# The transaction manager has disabled its support for remote/network transactions.
#
XACT_E_NETWORK_TX_DISABLED = 0x8004D024

#
# MessageId: XACT_E_PARTNER_NETWORK_TX_DISABLED
#
# MessageText:
#
# The partner transaction manager has disabled its support for remote/network transactions.
#
XACT_E_PARTNER_NETWORK_TX_DISABLED = 0x8004D025

#
# MessageId: XACT_E_XA_TX_DISABLED
#
# MessageText:
#
# The transaction manager has disabled its support for XA transactions.
#
XACT_E_XA_TX_DISABLED = 0x8004D026

#
# MessageId: XACT_E_UNABLE_TO_READ_DTC_CONFIG
#
# MessageText:
#
# MSDTC was unable to read its configuration information.
#
XACT_E_UNABLE_TO_READ_DTC_CONFIG = 0x8004D027

#
# MessageId: XACT_E_UNABLE_TO_LOAD_DTC_PROXY
#
# MessageText:
#
# MSDTC was unable to load the dtc proxy dll.
#
XACT_E_UNABLE_TO_LOAD_DTC_PROXY = 0x8004D028

#
# MessageId: XACT_E_ABORTING
#
# MessageText:
#
# The local transaction has aborted.
#
XACT_E_ABORTING = 0x8004D029

#
# MessageId: XACT_E_PUSH_COMM_FAILURE
#
# MessageText:
#
# The MSDTC transaction manager was unable to push the transaction to the destination transaction manager due to communication problems. Possible causes are: a firewall is present and it doesn't have an exception for the MSDTC process, the two machines cannot find each other by their NetBIOS names, or the support for network transactions is not enabled for one of the two transaction managers.
#
XACT_E_PUSH_COMM_FAILURE = 0x8004D02A

#
# MessageId: XACT_E_PULL_COMM_FAILURE
#
# MessageText:
#
# The MSDTC transaction manager was unable to pull the transaction from the source transaction manager due to communication problems. Possible causes are: a firewall is present and it doesn't have an exception for the MSDTC process, the two machines cannot find each other by their NetBIOS names, or the support for network transactions is not enabled for one of the two transaction managers.
#
XACT_E_PULL_COMM_FAILURE = 0x8004D02B

#
# MessageId: XACT_E_LU_TX_DISABLED
#
# MessageText:
#
# The MSDTC transaction manager has disabled its support for SNA LU 6.2 transactions.
#
XACT_E_LU_TX_DISABLED = 0x8004D02C

#
# TXF & CRM errors start 4d080.
#
# MessageId: XACT_E_CLERKNOTFOUND
#
# MessageText:
#
#  XACT_E_CLERKNOTFOUND
#
XACT_E_CLERKNOTFOUND = 0x8004D080

#
# MessageId: XACT_E_CLERKEXISTS
#
# MessageText:
#
#  XACT_E_CLERKEXISTS
#
XACT_E_CLERKEXISTS = 0x8004D081

#
# MessageId: XACT_E_RECOVERYINPROGRESS
#
# MessageText:
#
#  XACT_E_RECOVERYINPROGRESS
#
XACT_E_RECOVERYINPROGRESS = 0x8004D082

#
# MessageId: XACT_E_TRANSACTIONCLOSED
#
# MessageText:
#
#  XACT_E_TRANSACTIONCLOSED
#
XACT_E_TRANSACTIONCLOSED = 0x8004D083

#
# MessageId: XACT_E_INVALIDLSN
#
# MessageText:
#
#  XACT_E_INVALIDLSN
#
XACT_E_INVALIDLSN = 0x8004D084

#
# MessageId: XACT_E_REPLAYREQUEST
#
# MessageText:
#
#  XACT_E_REPLAYREQUEST
#
XACT_E_REPLAYREQUEST = 0x8004D085

# Begin XACT_DTC_CONSTANTS enumerated values defined in txdtc.h

# SymbolicName=XACT_E_CONNECTION_REQUEST_DENIED
#
# MessageId: 0x8004D100L (No symbolic name defined)
#
# MessageText:
#
# The request to connect to the specified transaction coordinator was denied.
#


# SymbolicName=XACT_E_TOOMANY_ENLISTMENTS
#
# MessageId: 0x8004D101L (No symbolic name defined)
#
# MessageText:
#
# The maximum number of enlistments for the specified transaction has been reached.
#


# SymbolicName=XACT_E_DUPLICATE_GUID
#
# MessageId: 0x8004D102L (No symbolic name defined)
#
# MessageText:
#
# A resource manager with the same identifier is already registered with the specified transaction coordinator.
#


# SymbolicName=XACT_E_NOTSINGLEPHASE
#
# MessageId: 0x8004D103L (No symbolic name defined)
#
# MessageText:
#
# The prepare request given was not eligible for single phase optimizations.
#


# SymbolicName=XACT_E_RECOVERYALREADYDONE
#
# MessageId: 0x8004D104L (No symbolic name defined)
#
# MessageText:
#
# RecoveryComplete has already been called for the given resource manager.
#


# SymbolicName=XACT_E_PROTOCOL
#
# MessageId: 0x8004D105L (No symbolic name defined)
#
# MessageText:
#
# The interface call made was incorrect for the current state of the protocol.
#


# SymbolicName=XACT_E_RM_FAILURE
#
# MessageId: 0x8004D106L (No symbolic name defined)
#
# MessageText:
#
# xa_open call failed for the XA resource.
#


# SymbolicName=XACT_E_RECOVERY_FAILED
#
# MessageId: 0x8004D107L (No symbolic name defined)
#
# MessageText:
#
# xa_recover call failed for the XA resource.
#


# SymbolicName=XACT_E_LU_NOT_FOUND
#
# MessageId: 0x8004D108L (No symbolic name defined)
#
# MessageText:
#
# The Logical Unit of Work specified cannot be found.
#


# SymbolicName=XACT_E_DUPLICATE_LU
#
# MessageId: 0x8004D109L (No symbolic name defined)
#
# MessageText:
#
# The specified Logical Unit of Work already exists.
#


# SymbolicName=XACT_E_LU_NOT_CONNECTED
#
# MessageId: 0x8004D10AL (No symbolic name defined)
#
# MessageText:
#
# Subordinate creation failed. The specified Logical Unit of Work was not connected.
#


# SymbolicName=XACT_E_DUPLICATE_TRANSID
#
# MessageId: 0x8004D10BL (No symbolic name defined)
#
# MessageText:
#
# A transaction with the given identifier already exists.
#


# SymbolicName=XACT_E_LU_BUSY
#
# MessageId: 0x8004D10CL (No symbolic name defined)
#
# MessageText:
#
# The resource is in use.
#


# SymbolicName=XACT_E_LU_NO_RECOVERY_PROCESS
#
# MessageId: 0x8004D10DL (No symbolic name defined)
#
# MessageText:
#
# The LU Recovery process is down.
#


# SymbolicName=XACT_E_LU_DOWN
#
# MessageId: 0x8004D10EL (No symbolic name defined)
#
# MessageText:
#
# The remote session was lost.
#


# SymbolicName=XACT_E_LU_RECOVERING
#
# MessageId: 0x8004D10FL (No symbolic name defined)
#
# MessageText:
#
# The resource is currently recovering.
#


# SymbolicName=XACT_E_LU_RECOVERY_MISMATCH
#
# MessageId: 0x8004D110L (No symbolic name defined)
#
# MessageText:
#
# There was a mismatch in driving recovery.
#


# SymbolicName=XACT_E_RM_UNAVAILABLE
#
# MessageId: 0x8004D111L (No symbolic name defined)
#
# MessageText:
#
# An error occurred with the XA resource.
#


# End XACT_DTC_CONSTANTS enumerated values defined in txdtc.h

#
# OleTx Success codes.
#
#
# MessageId: XACT_S_ASYNC
#
# MessageText:
#
# An asynchronous operation was specified. The operation has begun, but its outcome is not known yet.
#
XACT_S_ASYNC = 0x0004D000

#
# MessageId: XACT_S_DEFECT
#
# MessageText:
#
#  XACT_S_DEFECT
#
XACT_S_DEFECT = 0x0004D001

#
# MessageId: XACT_S_READONLY
#
# MessageText:
#
# The method call succeeded because the transaction was read-only.
#
XACT_S_READONLY = 0x0004D002

#
# MessageId: XACT_S_SOMENORETAIN
#
# MessageText:
#
# The transaction was successfully aborted. However, this is a coordinated transaction, and some number of enlisted resources were aborted outright because they could not support abort-retaining semantics
#
XACT_S_SOMENORETAIN = 0x0004D003

#
# MessageId: XACT_S_OKINFORM
#
# MessageText:
#
# No changes were made during this call, but the sink wants another chance to look if any other sinks make further changes.
#
XACT_S_OKINFORM = 0x0004D004

#
# MessageId: XACT_S_MADECHANGESCONTENT
#
# MessageText:
#
# The sink is content and wishes the transaction to proceed. Changes were made to one or more resources during this call.
#
XACT_S_MADECHANGESCONTENT = 0x0004D005

#
# MessageId: XACT_S_MADECHANGESINFORM
#
# MessageText:
#
# The sink is for the moment and wishes the transaction to proceed, but if other changes are made following this return by other event sinks then this sink wants another chance to look
#
XACT_S_MADECHANGESINFORM = 0x0004D006

#
# MessageId: XACT_S_ALLNORETAIN
#
# MessageText:
#
# The transaction was successfully aborted. However, the abort was non-retaining.
#
XACT_S_ALLNORETAIN = 0x0004D007

#
# MessageId: XACT_S_ABORTING
#
# MessageText:
#
# An abort operation was already in progress.
#
XACT_S_ABORTING = 0x0004D008

#
# MessageId: XACT_S_SINGLEPHASE
#
# MessageText:
#
# The resource manager has performed a single-phase commit of the transaction.
#
XACT_S_SINGLEPHASE = 0x0004D009

#
# MessageId: XACT_S_LOCALLY_OK
#
# MessageText:
#
# The local transaction has not aborted.
#
XACT_S_LOCALLY_OK = 0x0004D00A

#
# MessageId: XACT_S_LASTRESOURCEMANAGER
#
# MessageText:
#
# The resource manager has requested to be the coordinator (last resource manager) for the transaction.
#
XACT_S_LASTRESOURCEMANAGER = 0x0004D010

CONTEXT_E_FIRST = 0
CONTEXT_E_LAST = 0
CONTEXT_S_FIRST = 0
CONTEXT_S_LAST = 0
#
# MessageId: CONTEXT_E_ABORTED
#
# MessageText:
#
# The root transaction wanted to commit, but transaction aborted
#
CONTEXT_E_ABORTED = 0x8004E002

#
# MessageId: CONTEXT_E_ABORTING
#
# MessageText:
#
# You made a method call on a COM+ component that has a transaction that has already aborted or in the process of aborting.
#
CONTEXT_E_ABORTING = 0x8004E003

#
# MessageId: CONTEXT_E_NOCONTEXT
#
# MessageText:
#
# There is no MTS object context
#
CONTEXT_E_NOCONTEXT = 0x8004E004

#
# MessageId: CONTEXT_E_WOULD_DEADLOCK
#
# MessageText:
#
# The component is configured to use synchronization and this method call would cause a deadlock to occur.
#
CONTEXT_E_WOULD_DEADLOCK = 0x8004E005

#
# MessageId: CONTEXT_E_SYNCH_TIMEOUT
#
# MessageText:
#
# The component is configured to use synchronization and a thread has timed out waiting to enter the context.
#
CONTEXT_E_SYNCH_TIMEOUT = 0x8004E006

#
# MessageId: CONTEXT_E_OLDREF
#
# MessageText:
#
# You made a method call on a COM+ component that has a transaction that has already committed or aborted.
#
CONTEXT_E_OLDREF = 0x8004E007

#
# MessageId: CONTEXT_E_ROLENOTFOUND
#
# MessageText:
#
# The specified role was not configured for the application
#
CONTEXT_E_ROLENOTFOUND = 0x8004E00C

#
# MessageId: CONTEXT_E_TMNOTAVAILABLE
#
# MessageText:
#
# COM+ was unable to talk to the Microsoft Distributed Transaction Coordinator
#
CONTEXT_E_TMNOTAVAILABLE = 0x8004E00F

#
# MessageId: CO_E_ACTIVATIONFAILED
#
# MessageText:
#
# An unexpected error occurred during COM+ Activation.
#
CO_E_ACTIVATIONFAILED = 0x8004E021

#
# MessageId: CO_E_ACTIVATIONFAILED_EVENTLOGGED
#
# MessageText:
#
# COM+ Activation failed. Check the event log for more information
#
CO_E_ACTIVATIONFAILED_EVENTLOGGED = 0x8004E022

#
# MessageId: CO_E_ACTIVATIONFAILED_CATALOGERROR
#
# MessageText:
#
# COM+ Activation failed due to a catalog or configuration error.
#
CO_E_ACTIVATIONFAILED_CATALOGERROR = 0x8004E023

#
# MessageId: CO_E_ACTIVATIONFAILED_TIMEOUT
#
# MessageText:
#
# COM+ activation failed because the activation could not be completed in the specified amount of time.
#
CO_E_ACTIVATIONFAILED_TIMEOUT = 0x8004E024

#
# MessageId: CO_E_INITIALIZATIONFAILED
#
# MessageText:
#
# COM+ Activation failed because an initialization function failed. Check the event log for more information.
#
CO_E_INITIALIZATIONFAILED = 0x8004E025

#
# MessageId: CONTEXT_E_NOJIT
#
# MessageText:
#
# The requested operation requires that JIT be in the current context and it is not
#
CONTEXT_E_NOJIT = 0x8004E026

#
# MessageId: CONTEXT_E_NOTRANSACTION
#
# MessageText:
#
# The requested operation requires that the current context have a Transaction, and it does not
#
CONTEXT_E_NOTRANSACTION = 0x8004E027

#
# MessageId: CO_E_THREADINGMODEL_CHANGED
#
# MessageText:
#
# The components threading model has changed after install into a COM+ Application. Please re-install component.
#
CO_E_THREADINGMODEL_CHANGED = 0x8004E028

#
# MessageId: CO_E_NOIISINTRINSICS
#
# MessageText:
#
# IIS intrinsics not available. Start your work with IIS.
#
CO_E_NOIISINTRINSICS = 0x8004E029

#
# MessageId: CO_E_NOCOOKIES
#
# MessageText:
#
# An attempt to write a cookie failed.
#
CO_E_NOCOOKIES = 0x8004E02A

#
# MessageId: CO_E_DBERROR
#
# MessageText:
#
# An attempt to use a database generated a database specific error.
#
CO_E_DBERROR = 0x8004E02B

#
# MessageId: CO_E_NOTPOOLED
#
# MessageText:
#
# The COM+ component you created must use object pooling to work.
#
CO_E_NOTPOOLED = 0x8004E02C

#
# MessageId: CO_E_NOTCONSTRUCTED
#
# MessageText:
#
# The COM+ component you created must use object construction to work correctly.
#
CO_E_NOTCONSTRUCTED = 0x8004E02D

#
# MessageId: CO_E_NOSYNCHRONIZATION
#
# MessageText:
#
# The COM+ component requires synchronization, and it is not configured for it.
#
CO_E_NOSYNCHRONIZATION = 0x8004E02E

#
# MessageId: CO_E_ISOLEVELMISMATCH
#
# MessageText:
#
# The TxIsolation Level property for the COM+ component being created is stronger than the TxIsolationLevel for the "root" component for the transaction. The creation failed.
#
CO_E_ISOLEVELMISMATCH = 0x8004E02F

#
# MessageId: CO_E_CALL_OUT_OF_TX_SCOPE_NOT_ALLOWED
#
# MessageText:
#
# The component attempted to make a cross-context call between invocations of EnterTransactionScopeand ExitTransactionScope. This is not allowed. Cross-context calls cannot be made while inside of a transaction scope.
#
CO_E_CALL_OUT_OF_TX_SCOPE_NOT_ALLOWED = 0x8004E030

#
# MessageId: CO_E_EXIT_TRANSACTION_SCOPE_NOT_CALLED
#
# MessageText:
#
# The component made a call to EnterTransactionScope, but did not make a corresponding call to ExitTransactionScope before returning.
#
CO_E_EXIT_TRANSACTION_SCOPE_NOT_CALLED = 0x8004E031

#
# Old OLE Success Codes
#
#
# MessageId: OLE_S_USEREG
#
# MessageText:
#
# Use the registry database to provide the requested information
#
OLE_S_USEREG = 0x00040000

#
# MessageId: OLE_S_STATIC
#
# MessageText:
#
# Success, but static
#
OLE_S_STATIC = 0x00040001

#
# MessageId: OLE_S_MAC_CLIPFORMAT
#
# MessageText:
#
# Macintosh clipboard format
#
OLE_S_MAC_CLIPFORMAT = 0x00040002

#
# MessageId: DRAGDROP_S_DROP
#
# MessageText:
#
# Successful drop took place
#
DRAGDROP_S_DROP = 0x00040100

#
# MessageId: DRAGDROP_S_CANCEL
#
# MessageText:
#
# Drag-drop operation canceled
#
DRAGDROP_S_CANCEL = 0x00040101

#
# MessageId: DRAGDROP_S_USEDEFAULTCURSORS
#
# MessageText:
#
# Use the default cursor
#
DRAGDROP_S_USEDEFAULTCURSORS = 0x00040102

#
# MessageId: DATA_S_SAMEFORMATETC
#
# MessageText:
#
# Data has same FORMATETC
#
DATA_S_SAMEFORMATETC = 0x00040130

#
# MessageId: VIEW_S_ALREADY_FROZEN
#
# MessageText:
#
# View is already frozen
#
VIEW_S_ALREADY_FROZEN = 0x00040140

#
# MessageId: CACHE_S_FORMATETC_NOTSUPPORTED
#
# MessageText:
#
# FORMATETC not supported
#
CACHE_S_FORMATETC_NOTSUPPORTED = 0x00040170

#
# MessageId: CACHE_S_SAMECACHE
#
# MessageText:
#
# Same cache
#
CACHE_S_SAMECACHE = 0x00040171

#
# MessageId: CACHE_S_SOMECACHES_NOTUPDATED
#
# MessageText:
#
# Some cache(s) not updated
#
CACHE_S_SOMECACHES_NOTUPDATED = 0x00040172

#
# MessageId: OLEOBJ_S_INVALIDVERB
#
# MessageText:
#
# Invalid verb for OLE object
#
OLEOBJ_S_INVALIDVERB = 0x00040180

#
# MessageId: OLEOBJ_S_CANNOT_DOVERB_NOW
#
# MessageText:
#
# Verb number is valid but verb cannot be done now
#
OLEOBJ_S_CANNOT_DOVERB_NOW = 0x00040181

#
# MessageId: OLEOBJ_S_INVALIDHWND
#
# MessageText:
#
# Invalid window handle passed
#
OLEOBJ_S_INVALIDHWND = 0x00040182

#
# MessageId: INPLACE_S_TRUNCATED
#
# MessageText:
#
# Message is too long; some of it had to be truncated before displaying
#
INPLACE_S_TRUNCATED = 0x000401A0

#
# MessageId: CONVERT10_S_NO_PRESENTATION
#
# MessageText:
#
# Unable to convert OLESTREAM to IStorage
#
CONVERT1 = 0

#
# MessageId: MK_S_REDUCED_TO_SELF
#
# MessageText:
#
# Moniker reduced to itself
#
MK_S_REDUCED_TO_SELF = 0x000401E2

#
# MessageId: MK_S_ME
#
# MessageText:
#
# Common prefix is this moniker
#
MK_S_ME = 0x000401E4

#
# MessageId: MK_S_HIM
#
# MessageText:
#
# Common prefix is input moniker
#
MK_S_HIM = 0x000401E5

#
# MessageId: MK_S_US
#
# MessageText:
#
# Common prefix is both monikers
#
MK_S_US = 0x000401E6

#
# MessageId: MK_S_MONIKERALREADYREGISTERED
#
# MessageText:
#
# Moniker is already registered in running object table
#
MK_S_MONIKERALREADYREGISTERED = 0x000401E7

#
# Task Scheduler errors
#
#
# MessageId: SCHED_S_TASK_READY
#
# MessageText:
#
# The task is ready to run at its next scheduled time.
#
SCHED_S_TASK_READY = 0x00041300

#
# MessageId: SCHED_S_TASK_RUNNING
#
# MessageText:
#
# The task is currently running.
#
SCHED_S_TASK_RUNNING = 0x00041301

#
# MessageId: SCHED_S_TASK_DISABLED
#
# MessageText:
#
# The task will not run at the scheduled times because it has been disabled.
#
SCHED_S_TASK_DISABLED = 0x00041302

#
# MessageId: SCHED_S_TASK_HAS_NOT_RUN
#
# MessageText:
#
# The task has not yet run.
#
SCHED_S_TASK_HAS_NOT_RUN = 0x00041303

#
# MessageId: SCHED_S_TASK_NO_MORE_RUNS
#
# MessageText:
#
# There are no more runs scheduled for this task.
#
SCHED_S_TASK_NO_MORE_RUNS = 0x00041304

#
# MessageId: SCHED_S_TASK_NOT_SCHEDULED
#
# MessageText:
#
# One or more of the properties that are needed to run this task on a schedule have not been set.
#
SCHED_S_TASK_NOT_SCHEDULED = 0x00041305

#
# MessageId: SCHED_S_TASK_TERMINATED
#
# MessageText:
#
# The last run of the task was terminated by the user.
#
SCHED_S_TASK_TERMINATED = 0x00041306

#
# MessageId: SCHED_S_TASK_NO_VALID_TRIGGERS
#
# MessageText:
#
# Either the task has no triggers or the existing triggers are disabled or not set.
#
SCHED_S_TASK_NO_VALID_TRIGGERS = 0x00041307

#
# MessageId: SCHED_S_EVENT_TRIGGER
#
# MessageText:
#
# Event triggers don't have set run times.
#
SCHED_S_EVENT_TRIGGER = 0x00041308

#
# MessageId: SCHED_E_TRIGGER_NOT_FOUND
#
# MessageText:
#
# Trigger not found.
#
SCHED_E_TRIGGER_NOT_FOUND = 0x80041309

#
# MessageId: SCHED_E_TASK_NOT_READY
#
# MessageText:
#
# One or more of the properties that are needed to run this task have not been set.
#
SCHED_E_TASK_NOT_READY = 0x8004130A

#
# MessageId: SCHED_E_TASK_NOT_RUNNING
#
# MessageText:
#
# There is no running instance of the task.
#
SCHED_E_TASK_NOT_RUNNING = 0x8004130B

#
# MessageId: SCHED_E_SERVICE_NOT_INSTALLED
#
# MessageText:
#
# The Task Scheduler Service is not installed on this computer.
#
SCHED_E_SERVICE_NOT_INSTALLED = 0x8004130C

#
# MessageId: SCHED_E_CANNOT_OPEN_TASK
#
# MessageText:
#
# The task object could not be opened.
#
SCHED_E_CANNOT_OPEN_TASK = 0x8004130D

#
# MessageId: SCHED_E_INVALID_TASK
#
# MessageText:
#
# The object is either an invalid task object or is not a task object.
#
SCHED_E_INVALID_TASK = 0x8004130E

#
# MessageId: SCHED_E_ACCOUNT_INFORMATION_NOT_SET
#
# MessageText:
#
# No account information could be found in the Task Scheduler security database for the task indicated.
#
SCHED_E_ACCOUNT_INFORMATION_NOT_SET = 0x8004130F

#
# MessageId: SCHED_E_ACCOUNT_NAME_NOT_FOUND
#
# MessageText:
#
# Unable to establish existence of the account specified.
#
SCHED_E_ACCOUNT_NAME_NOT_FOUND = 0x80041310

#
# MessageId: SCHED_E_ACCOUNT_DBASE_CORRUPT
#
# MessageText:
#
# Corruption was detected in the Task Scheduler security database; the database has been reset.
#
SCHED_E_ACCOUNT_DBASE_CORRUPT = 0x80041311

#
# MessageId: SCHED_E_NO_SECURITY_SERVICES
#
# MessageText:
#
# Task Scheduler security services are available only on Windows NT.
#
SCHED_E_NO_SECURITY_SERVICES = 0x80041312

#
# MessageId: SCHED_E_UNKNOWN_OBJECT_VERSION
#
# MessageText:
#
# The task object version is either unsupported or invalid.
#
SCHED_E_UNKNOWN_OBJECT_VERSION = 0x80041313

#
# MessageId: SCHED_E_UNSUPPORTED_ACCOUNT_OPTION
#
# MessageText:
#
# The task has been configured with an unsupported combination of account settings and run time options.
#
SCHED_E_UNSUPPORTED_ACCOUNT_OPTION = 0x80041314

#
# MessageId: SCHED_E_SERVICE_NOT_RUNNING
#
# MessageText:
#
# The Task Scheduler Service is not running.
#
SCHED_E_SERVICE_NOT_RUNNING = 0x80041315

#
# MessageId: SCHED_E_UNEXPECTEDNODE
#
# MessageText:
#
# The task XML contains an unexpected node.
#
SCHED_E_UNEXPECTEDNODE = 0x80041316

#
# MessageId: SCHED_E_NAMESPACE
#
# MessageText:
#
# The task XML contains an element or attribute from an unexpected namespace.
#
SCHED_E_NAMESPACE = 0x80041317

#
# MessageId: SCHED_E_INVALIDVALUE
#
# MessageText:
#
# The task XML contains a value which is incorrectly formatted or out of range.
#
SCHED_E_INVALIDVALUE = 0x80041318

#
# MessageId: SCHED_E_MISSINGNODE
#
# MessageText:
#
# The task XML is missing a required element or attribute.
#
SCHED_E_MISSINGNODE = 0x80041319

#
# MessageId: SCHED_E_MALFORMEDXML
#
# MessageText:
#
# The task XML is malformed.
#
SCHED_E_MALFORMEDXML = 0x8004131A

#
# MessageId: SCHED_S_SOME_TRIGGERS_FAILED
#
# MessageText:
#
# The task is registered, but not all specified triggers will start the task, check task scheduler event log for detailed information.
#
SCHED_S_SOME_TRIGGERS_FAILED = 0x0004131B

#
# MessageId: SCHED_S_BATCH_LOGON_PROBLEM
#
# MessageText:
#
# The task is registered, but may fail to start. Batch logon privilege needs to be enabled for the task principal.
#
SCHED_S_BATCH_LOGON_PROBLEM = 0x0004131C

#
# MessageId: SCHED_E_TOO_MANY_NODES
#
# MessageText:
#
# The task XML contains too many nodes of the same type.
#
SCHED_E_TOO_MANY_NODES = 0x8004131D

#
# MessageId: SCHED_E_PAST_END_BOUNDARY
#
# MessageText:
#
# The task cannot be started after the trigger's end boundary.
#
SCHED_E_PAST_END_BOUNDARY = 0x8004131E

#
# MessageId: SCHED_E_ALREADY_RUNNING
#
# MessageText:
#
# An instance of this task is already running.
#
SCHED_E_ALREADY_RUNNING = 0x8004131F

#
# MessageId: SCHED_E_USER_NOT_LOGGED_ON
#
# MessageText:
#
# The task will not run because the user is not logged on.
#
SCHED_E_USER_NOT_LOGGED_ON = 0x80041320

#
# MessageId: SCHED_E_INVALID_TASK_HASH
#
# MessageText:
#
# The task image is corrupt or has been tampered with.
#
SCHED_E_INVALID_TASK_HASH = 0x80041321

#
# MessageId: SCHED_E_SERVICE_NOT_AVAILABLE
#
# MessageText:
#
# The Task Scheduler service is not available.
#
SCHED_E_SERVICE_NOT_AVAILABLE = 0x80041322

#
# MessageId: SCHED_E_SERVICE_TOO_BUSY
#
# MessageText:
#
# The Task Scheduler service is too busy to handle your request. Please try again later.
#
SCHED_E_SERVICE_TOO_BUSY = 0x80041323

#
# MessageId: SCHED_E_TASK_ATTEMPTED
#
# MessageText:
#
# The Task Scheduler service attempted to run the task, but the task did not run due to one of the constraints in the task definition.
#
SCHED_E_TASK_ATTEMPTED = 0x80041324

#
# MessageId: SCHED_S_TASK_QUEUED
#
# MessageText:
#
# The Task Scheduler service has asked the task to run.
#
SCHED_S_TASK_QUEUED = 0x00041325

#
# MessageId: SCHED_E_TASK_DISABLED
#
# MessageText:
#
# The task is disabled.
#
SCHED_E_TASK_DISABLED = 0x80041326

#
# MessageId: SCHED_E_TASK_NOT_V1_COMPAT
#
# MessageText:
#
# The task has properties that are not compatible with previous versions of Windows.
#
SCHED_E_TASK_NOT_V = 1

#
# MessageId: SCHED_E_START_ON_DEMAND
#
# MessageText:
#
# The task settings do not allow the task to start on demand.
#
SCHED_E_START_ON_DEMAND = 0x80041328

#
# MessageId: SCHED_E_TASK_NOT_UBPM_COMPAT
#
# MessageText:
#
# The combination of properties that task is using is not compatible with the scheduling engine.
#
SCHED_E_TASK_NOT_UBPM_COMPAT = 0x80041329

#
# MessageId: SCHED_E_DEPRECATED_FEATURE_USED
#
# MessageText:
#
# The task definition uses a deprecated feature.
#
SCHED_E_DEPRECATED_FEATURE_USED = 0x80041330

# ******************
# FACILITY_WINDOWS
# ******************
#
# Codes 0x0-0x01ff are reserved for the OLE group of
# interfaces.
#
#
# MessageId: CO_E_CLASS_CREATE_FAILED
#
# MessageText:
#
# Attempt to create a class object failed
#
CO_E_CLASS_CREATE_FAILED = 0x80080001

#
# MessageId: CO_E_SCM_ERROR
#
# MessageText:
#
# OLE service could not bind object
#
CO_E_SCM_ERROR = 0x80080002

#
# MessageId: CO_E_SCM_RPC_FAILURE
#
# MessageText:
#
# RPC communication failed with OLE service
#
CO_E_SCM_RPC_FAILURE = 0x80080003

#
# MessageId: CO_E_BAD_PATH
#
# MessageText:
#
# Bad path to object
#
CO_E_BAD_PATH = 0x80080004

#
# MessageId: CO_E_SERVER_EXEC_FAILURE
#
# MessageText:
#
# Server execution failed
#
CO_E_SERVER_EXEC_FAILURE = 0x80080005

#
# MessageId: CO_E_OBJSRV_RPC_FAILURE
#
# MessageText:
#
# OLE service could not communicate with the object server
#
CO_E_OBJSRV_RPC_FAILURE = 0x80080006

#
# MessageId: MK_E_NO_NORMALIZED
#
# MessageText:
#
# Moniker path could not be normalized
#
MK_E_NO_NORMALIZED = 0x80080007

#
# MessageId: CO_E_SERVER_STOPPING
#
# MessageText:
#
# Object server is stopping when OLE service contacts it
#
CO_E_SERVER_STOPPING = 0x80080008

#
# MessageId: MEM_E_INVALID_ROOT
#
# MessageText:
#
# An invalid root block pointer was specified
#
MEM_E_INVALID_ROOT = 0x80080009

#
# MessageId: MEM_E_INVALID_LINK
#
# MessageText:
#
# An allocation chain contained an invalid link pointer
#
MEM_E_INVALID_LINK = 0x80080010

#
# MessageId: MEM_E_INVALID_SIZE
#
# MessageText:
#
# The requested allocation size was too large
#
MEM_E_INVALID_SIZE = 0x80080011

#
# MessageId: CO_S_NOTALLINTERFACES
#
# MessageText:
#
# Not all the requested interfaces were available
#
CO_S_NOTALLINTERFACES = 0x00080012

#
# MessageId: CO_S_MACHINENAMENOTFOUND
#
# MessageText:
#
# The specified machine name was not found in the cache.
#
CO_S_MACHINENAMENOTFOUND = 0x00080013

#
# MessageId: CO_E_MISSING_DISPLAYNAME
#
# MessageText:
#
# The activation requires a display name to be present under the CLSID key.
#
CO_E_MISSING_DISPLAYNAME = 0x80080015

#
# MessageId: CO_E_RUNAS_VALUE_MUST_BE_AAA
#
# MessageText:
#
# The activation requires that the RunAs value for the application is Activate As Activator.
#
CO_E_RUNAS_VALUE_MUST_BE_AAA = 0x80080016

#
# MessageId: CO_E_ELEVATION_DISABLED
#
# MessageText:
#
# The class is not configured to support Elevated activation.
#
CO_E_ELEVATION_DISABLED = 0x80080017

#
# Codes 0x0200-0x02ff are reserved for the APPX errors
#
#
# MessageId: APPX_E_PACKAGING_INTERNAL
#
# MessageText:
#
# Appx packaging API has encountered an internal error.
#
APPX_E_PACKAGING_INTERNAL = 0x80080200

#
# MessageId: APPX_E_INTERLEAVING_NOT_ALLOWED
#
# MessageText:
#
# The file is not a valid Appx package because its contents are interleaved.
#
APPX_E_INTERLEAVING_NOT_ALLOWED = 0x80080201

#
# MessageId: APPX_E_RELATIONSHIPS_NOT_ALLOWED
#
# MessageText:
#
# The file is not a valid Appx package because it contains OPC relationships.
#
APPX_E_RELATIONSHIPS_NOT_ALLOWED = 0x80080202

#
# MessageId: APPX_E_MISSING_REQUIRED_FILE
#
# MessageText:
#
# The file is not a valid Appx package because it is missing a manifest or block map, or missing a signature file when the code integrity file is present.
#
APPX_E_MISSING_REQUIRED_FILE = 0x80080203

#
# MessageId: APPX_E_INVALID_MANIFEST
#
# MessageText:
#
# The Appx package's manifest is invalid.
#
APPX_E_INVALID_MANIFEST = 0x80080204

#
# MessageId: APPX_E_INVALID_BLOCKMAP
#
# MessageText:
#
# The Appx package's block map is invalid.
#
APPX_E_INVALID_BLOCKMAP = 0x80080205

#
# MessageId: APPX_E_CORRUPT_CONTENT
#
# MessageText:
#
# The Appx package's content cannot be read because it is corrupt.
#
APPX_E_CORRUPT_CONTENT = 0x80080206

#
# MessageId: APPX_E_BLOCK_HASH_INVALID
#
# MessageText:
#
# The computed hash value of the block does not match the one stored in the block map.
#
APPX_E_BLOCK_HASH_INVALID = 0x80080207

#
# MessageId: APPX_E_REQUESTED_RANGE_TOO_LARGE
#
# MessageText:
#
# The requested byte range is over 4GB when translated to byte range of blocks.
#
APPX_E_REQUESTED_RANGE_TOO_LARGE = 0x80080208

#
# MessageId: APPX_E_INVALID_SIP_CLIENT_DATA
#
# MessageText:
#
# The SIP_SUBJECTINFO structure used to sign the package didn't contain the required data.
#
APPX_E_INVALID_SIP_CLIENT_DATA = 0x80080209

# ******************
# FACILITY_DISPATCH
# ******************
#
# MessageId: DISP_E_UNKNOWNINTERFACE
#
# MessageText:
#
# Unknown interface.
#
DISP_E_UNKNOWNINTERFACE = 0x80020001

#
# MessageId: DISP_E_MEMBERNOTFOUND
#
# MessageText:
#
# Member not found.
#
DISP_E_MEMBERNOTFOUND = 0x80020003

#
# MessageId: DISP_E_PARAMNOTFOUND
#
# MessageText:
#
# Parameter not found.
#
DISP_E_PARAMNOTFOUND = 0x80020004

#
# MessageId: DISP_E_TYPEMISMATCH
#
# MessageText:
#
# Type mismatch.
#
DISP_E_TYPEMISMATCH = 0x80020005

#
# MessageId: DISP_E_UNKNOWNNAME
#
# MessageText:
#
# Unknown name.
#
DISP_E_UNKNOWNNAME = 0x80020006

#
# MessageId: DISP_E_NONAMEDARGS
#
# MessageText:
#
# No named arguments.
#
DISP_E_NONAMEDARGS = 0x80020007

#
# MessageId: DISP_E_BADVARTYPE
#
# MessageText:
#
# Bad variable type.
#
DISP_E_BADVARTYPE = 0x80020008

#
# MessageId: DISP_E_EXCEPTION
#
# MessageText:
#
# Exception occurred.
#
DISP_E_EXCEPTION = 0x80020009

#
# MessageId: DISP_E_OVERFLOW
#
# MessageText:
#
# Out of present range.
#
DISP_E_OVERFLOW = 0x8002000A

#
# MessageId: DISP_E_BADINDEX
#
# MessageText:
#
# Invalid index.
#
DISP_E_BADINDEX = 0x8002000B

#
# MessageId: DISP_E_UNKNOWNLCID
#
# MessageText:
#
# Unknown language.
#
DISP_E_UNKNOWNLCID = 0x8002000C

#
# MessageId: DISP_E_ARRAYISLOCKED
#
# MessageText:
#
# Memory is locked.
#
DISP_E_ARRAYISLOCKED = 0x8002000D

#
# MessageId: DISP_E_BADPARAMCOUNT
#
# MessageText:
#
# Invalid number of parameters.
#
DISP_E_BADPARAMCOUNT = 0x8002000E

#
# MessageId: DISP_E_PARAMNOTOPTIONAL
#
# MessageText:
#
# Parameter not optional.
#
DISP_E_PARAMNOTOPTIONAL = 0x8002000F

#
# MessageId: DISP_E_BADCALLEE
#
# MessageText:
#
# Invalid callee.
#
DISP_E_BADCALLEE = 0x80020010

#
# MessageId: DISP_E_NOTACOLLECTION
#
# MessageText:
#
# Does not support a collection.
#
DISP_E_NOTACOLLECTION = 0x80020011

#
# MessageId: DISP_E_DIVBYZERO
#
# MessageText:
#
# Division by zero.
#
DISP_E_DIVBYZERO = 0x80020012

#
# MessageId: DISP_E_BUFFERTOOSMALL
#
# MessageText:
#
# Buffer too small
#
DISP_E_BUFFERTOOSMALL = 0x80020013

#
# MessageId: TYPE_E_BUFFERTOOSMALL
#
# MessageText:
#
# Buffer too small.
#
TYPE_E_BUFFERTOOSMALL = 0x80028016

#
# MessageId: TYPE_E_FIELDNOTFOUND
#
# MessageText:
#
# Field name not defined in the record.
#
TYPE_E_FIELDNOTFOUND = 0x80028017

#
# MessageId: TYPE_E_INVDATAREAD
#
# MessageText:
#
# Old format or invalid type library.
#
TYPE_E_INVDATAREAD = 0x80028018

#
# MessageId: TYPE_E_UNSUPFORMAT
#
# MessageText:
#
# Old format or invalid type library.
#
TYPE_E_UNSUPFORMAT = 0x80028019

#
# MessageId: TYPE_E_REGISTRYACCESS
#
# MessageText:
#
# Error accessing the OLE registry.
#
TYPE_E_REGISTRYACCESS = 0x8002801C

#
# MessageId: TYPE_E_LIBNOTREGISTERED
#
# MessageText:
#
# Library not registered.
#
TYPE_E_LIBNOTREGISTERED = 0x8002801D

#
# MessageId: TYPE_E_UNDEFINEDTYPE
#
# MessageText:
#
# Bound to unknown type.
#
TYPE_E_UNDEFINEDTYPE = 0x80028027

#
# MessageId: TYPE_E_QUALIFIEDNAMEDISALLOWED
#
# MessageText:
#
# Qualified name disallowed.
#
TYPE_E_QUALIFIEDNAMEDISALLOWED = 0x80028028

#
# MessageId: TYPE_E_INVALIDSTATE
#
# MessageText:
#
# Invalid forward reference, or reference to uncompiled type.
#
TYPE_E_INVALIDSTATE = 0x80028029

#
# MessageId: TYPE_E_WRONGTYPEKIND
#
# MessageText:
#
# Type mismatch.
#
TYPE_E_WRONGTYPEKIND = 0x8002802A

#
# MessageId: TYPE_E_ELEMENTNOTFOUND
#
# MessageText:
#
# Element not found.
#
TYPE_E_ELEMENTNOTFOUND = 0x8002802B

#
# MessageId: TYPE_E_AMBIGUOUSNAME
#
# MessageText:
#
# Ambiguous name.
#
TYPE_E_AMBIGUOUSNAME = 0x8002802C

#
# MessageId: TYPE_E_NAMECONFLICT
#
# MessageText:
#
# Name already exists in the library.
#
TYPE_E_NAMECONFLICT = 0x8002802D

#
# MessageId: TYPE_E_UNKNOWNLCID
#
# MessageText:
#
# Unknown LCID.
#
TYPE_E_UNKNOWNLCID = 0x8002802E

#
# MessageId: TYPE_E_DLLFUNCTIONNOTFOUND
#
# MessageText:
#
# Function not defined in specified DLL.
#
TYPE_E_DLLFUNCTIONNOTFOUND = 0x8002802F

#
# MessageId: TYPE_E_BADMODULEKIND
#
# MessageText:
#
# Wrong module kind for the operation.
#
TYPE_E_BADMODULEKIND = 0x800288BD

#
# MessageId: TYPE_E_SIZETOOBIG
#
# MessageText:
#
# Size may not exceed 64K.
#
TYPE_E_SIZETOOBIG = 0x800288C5

#
# MessageId: TYPE_E_DUPLICATEID
#
# MessageText:
#
# Duplicate ID in inheritance hierarchy.
#
TYPE_E_DUPLICATEID = 0x800288C6

#
# MessageId: TYPE_E_INVALIDID
#
# MessageText:
#
# Incorrect inheritance depth in standard OLE hmember.
#
TYPE_E_INVALIDID = 0x800288CF

#
# MessageId: TYPE_E_TYPEMISMATCH
#
# MessageText:
#
# Type mismatch.
#
TYPE_E_TYPEMISMATCH = 0x80028CA0

#
# MessageId: TYPE_E_OUTOFBOUNDS
#
# MessageText:
#
# Invalid number of arguments.
#
TYPE_E_OUTOFBOUNDS = 0x80028CA1

#
# MessageId: TYPE_E_IOERROR
#
# MessageText:
#
# I/O Error.
#
TYPE_E_IOERROR = 0x80028CA2

#
# MessageId: TYPE_E_CANTCREATETMPFILE
#
# MessageText:
#
# Error creating unique tmp file.
#
TYPE_E_CANTCREATETMPFILE = 0x80028CA3

#
# MessageId: TYPE_E_CANTLOADLIBRARY
#
# MessageText:
#
# Error loading type library/DLL.
#
TYPE_E_CANTLOADLIBRARY = 0x80029C4A

#
# MessageId: TYPE_E_INCONSISTENTPROPFUNCS
#
# MessageText:
#
# Inconsistent property functions.
#
TYPE_E_INCONSISTENTPROPFUNCS = 0x80029C83

#
# MessageId: TYPE_E_CIRCULARTYPE
#
# MessageText:
#
# Circular dependency between types/modules.
#
TYPE_E_CIRCULARTYPE = 0x80029C84

# ******************
# FACILITY_STORAGE
# ******************
#
# MessageId: STG_E_INVALIDFUNCTION
#
# MessageText:
#
# Unable to perform requested operation.
#
STG_E_INVALIDFUNCTION = 0x80030001

#
# MessageId: STG_E_FILENOTFOUND
#
# MessageText:
#
# %1 could not be found.
#
STG_E_FILENOTFOUND = 0x80030002

#
# MessageId: STG_E_PATHNOTFOUND
#
# MessageText:
#
# The path %1 could not be found.
#
STG_E_PATHNOTFOUND = 0x80030003

#
# MessageId: STG_E_TOOMANYOPENFILES
#
# MessageText:
#
# There are insufficient resources to open another file.
#
STG_E_TOOMANYOPENFILES = 0x80030004

#
# MessageId: STG_E_ACCESSDENIED
#
# MessageText:
#
# Access Denied.
#
STG_E_ACCESSDENIED = 0x80030005

#
# MessageId: STG_E_INVALIDHANDLE
#
# MessageText:
#
# Attempted an operation on an invalid object.
#
STG_E_INVALIDHANDLE = 0x80030006

#
# MessageId: STG_E_INSUFFICIENTMEMORY
#
# MessageText:
#
# There is insufficient memory available to complete operation.
#
STG_E_INSUFFICIENTMEMORY = 0x80030008

#
# MessageId: STG_E_INVALIDPOINTER
#
# MessageText:
#
# Invalid pointer error.
#
STG_E_INVALIDPOINTER = 0x80030009

#
# MessageId: STG_E_NOMOREFILES
#
# MessageText:
#
# There are no more entries to return.
#
STG_E_NOMOREFILES = 0x80030012

#
# MessageId: STG_E_DISKISWRITEPROTECTED
#
# MessageText:
#
# Disk is write-protected.
#
STG_E_DISKISWRITEPROTECTED = 0x80030013

#
# MessageId: STG_E_SEEKERROR
#
# MessageText:
#
# An error occurred during a seek operation.
#
STG_E_SEEKERROR = 0x80030019

#
# MessageId: STG_E_WRITEFAULT
#
# MessageText:
#
# A disk error occurred during a write operation.
#
STG_E_WRITEFAULT = 0x8003001D

#
# MessageId: STG_E_READFAULT
#
# MessageText:
#
# A disk error occurred during a read operation.
#
STG_E_READFAULT = 0x8003001E

#
# MessageId: STG_E_SHAREVIOLATION
#
# MessageText:
#
# A share violation has occurred.
#
STG_E_SHAREVIOLATION = 0x80030020

#
# MessageId: STG_E_LOCKVIOLATION
#
# MessageText:
#
# A lock violation has occurred.
#
STG_E_LOCKVIOLATION = 0x80030021

#
# MessageId: STG_E_FILEALREADYEXISTS
#
# MessageText:
#
# %1 already exists.
#
STG_E_FILEALREADYEXISTS = 0x80030050

#
# MessageId: STG_E_INVALIDPARAMETER
#
# MessageText:
#
# Invalid parameter error.
#
STG_E_INVALIDPARAMETER = 0x80030057

#
# MessageId: STG_E_MEDIUMFULL
#
# MessageText:
#
# There is insufficient disk space to complete operation.
#
STG_E_MEDIUMFULL = 0x80030070

#
# MessageId: STG_E_PROPSETMISMATCHED
#
# MessageText:
#
# Illegal write of non-simple property to simple property set.
#
STG_E_PROPSETMISMATCHED = 0x800300F0

#
# MessageId: STG_E_ABNORMALAPIEXIT
#
# MessageText:
#
# An API call exited abnormally.
#
STG_E_ABNORMALAPIEXIT = 0x800300FA

#
# MessageId: STG_E_INVALIDHEADER
#
# MessageText:
#
# The file %1 is not a valid compound file.
#
STG_E_INVALIDHEADER = 0x800300FB

#
# MessageId: STG_E_INVALIDNAME
#
# MessageText:
#
# The name %1 is not valid.
#
STG_E_INVALIDNAME = 0x800300FC

#
# MessageId: STG_E_UNKNOWN
#
# MessageText:
#
# An unexpected error occurred.
#
STG_E_UNKNOWN = 0x800300FD

#
# MessageId: STG_E_UNIMPLEMENTEDFUNCTION
#
# MessageText:
#
# That function is not implemented.
#
STG_E_UNIMPLEMENTEDFUNCTION = 0x800300FE

#
# MessageId: STG_E_INVALIDFLAG
#
# MessageText:
#
# Invalid flag error.
#
STG_E_INVALIDFLAG = 0x800300FF

#
# MessageId: STG_E_INUSE
#
# MessageText:
#
# Attempted to use an object that is busy.
#
STG_E_INUSE = 0x80030100

#
# MessageId: STG_E_NOTCURRENT
#
# MessageText:
#
# The storage has been changed since the last commit.
#
STG_E_NOTCURRENT = 0x80030101

#
# MessageId: STG_E_REVERTED
#
# MessageText:
#
# Attempted to use an object that has ceased to exist.
#
STG_E_REVERTED = 0x80030102

#
# MessageId: STG_E_CANTSAVE
#
# MessageText:
#
# Can't save.
#
STG_E_CANTSAVE = 0x80030103

#
# MessageId: STG_E_OLDFORMAT
#
# MessageText:
#
# The compound file %1 was produced with an incompatible version of storage.
#
STG_E_OLDFORMAT = 0x80030104

#
# MessageId: STG_E_OLDDLL
#
# MessageText:
#
# The compound file %1 was produced with a newer version of storage.
#
STG_E_OLDDLL = 0x80030105

#
# MessageId: STG_E_SHAREREQUIRED
#
# MessageText:
#
# Share.exe or equivalent is required for operation.
#
STG_E_SHAREREQUIRED = 0x80030106

#
# MessageId: STG_E_NOTFILEBASEDSTORAGE
#
# MessageText:
#
# Illegal operation called on non-file based storage.
#
STG_E_NOTFILEBASEDSTORAGE = 0x80030107

#
# MessageId: STG_E_EXTANTMARSHALLINGS
#
# MessageText:
#
# Illegal operation called on object with extant marshallings.
#
STG_E_EXTANTMARSHALLINGS = 0x80030108

#
# MessageId: STG_E_DOCFILECORRUPT
#
# MessageText:
#
# The docfile has been corrupted.
#
STG_E_DOCFILECORRUPT = 0x80030109

#
# MessageId: STG_E_BADBASEADDRESS
#
# MessageText:
#
# OLE32.DLL has been loaded at the wrong address.
#
STG_E_BADBASEADDRESS = 0x80030110

#
# MessageId: STG_E_DOCFILETOOLARGE
#
# MessageText:
#
# The compound file is too large for the current implementation
#
STG_E_DOCFILETOOLARGE = 0x80030111

#
# MessageId: STG_E_NOTSIMPLEFORMAT
#
# MessageText:
#
# The compound file was not created with the STGM_SIMPLE flag
#
STG_E_NOTSIMPLEFORMAT = 0x80030112

#
# MessageId: STG_E_INCOMPLETE
#
# MessageText:
#
# The file download was aborted abnormally. The file is incomplete.
#
STG_E_INCOMPLETE = 0x80030201

#
# MessageId: STG_E_TERMINATED
#
# MessageText:
#
# The file download has been terminated.
#
STG_E_TERMINATED = 0x80030202

#
# MessageId: STG_S_CONVERTED
#
# MessageText:
#
# The underlying file was converted to compound file format.
#
STG_S_CONVERTED = 0x00030200

#
# MessageId: STG_S_BLOCK
#
# MessageText:
#
# The storage operation should block until more data is available.
#
STG_S_BLOCK = 0x00030201

#
# MessageId: STG_S_RETRYNOW
#
# MessageText:
#
# The storage operation should retry immediately.
#
STG_S_RETRYNOW = 0x00030202

#
# MessageId: STG_S_MONITORING
#
# MessageText:
#
# The notified event sink will not influence the storage operation.
#
STG_S_MONITORING = 0x00030203

#
# MessageId: STG_S_MULTIPLEOPENS
#
# MessageText:
#
# Multiple opens prevent consolidated. (commit succeeded).
#
STG_S_MULTIPLEOPENS = 0x00030204

#
# MessageId: STG_S_CONSOLIDATIONFAILED
#
# MessageText:
#
# Consolidation of the storage file failed. (commit succeeded).
#
STG_S_CONSOLIDATIONFAILED = 0x00030205

#
# MessageId: STG_S_CANNOTCONSOLIDATE
#
# MessageText:
#
# Consolidation of the storage file is inappropriate. (commit succeeded).
#
STG_S_CANNOTCONSOLIDATE = 0x00030206

# /*++

#  MessageId's 0x0305 - 0x031f (inclusive) are reserved for **STORAGE**
#  copy protection errors.

# --*/
#
# MessageId: STG_E_STATUS_COPY_PROTECTION_FAILURE
#
# MessageText:
#
# Generic Copy Protection Error.
#
STG_E_STATUS_COPY_PROTECTION_FAILURE = 0x80030305

#
# MessageId: STG_E_CSS_AUTHENTICATION_FAILURE
#
# MessageText:
#
# Copy Protection Error - DVD CSS Authentication failed.
#
STG_E_CSS_AUTHENTICATION_FAILURE = 0x80030306

#
# MessageId: STG_E_CSS_KEY_NOT_PRESENT
#
# MessageText:
#
# Copy Protection Error - The given sector does not have a valid CSS key.
#
STG_E_CSS_KEY_NOT_PRESENT = 0x80030307

#
# MessageId: STG_E_CSS_KEY_NOT_ESTABLISHED
#
# MessageText:
#
# Copy Protection Error - DVD session key not established.
#
STG_E_CSS_KEY_NOT_ESTABLISHED = 0x80030308

#
# MessageId: STG_E_CSS_SCRAMBLED_SECTOR
#
# MessageText:
#
# Copy Protection Error - The read failed because the sector is encrypted.
#
STG_E_CSS_SCRAMBLED_SECTOR = 0x80030309

#
# MessageId: STG_E_CSS_REGION_MISMATCH
#
# MessageText:
#
# Copy Protection Error - The current DVD's region does not correspond to the region setting of the drive.
#
STG_E_CSS_REGION_MISMATCH = 0x8003030A

#
# MessageId: STG_E_RESETS_EXHAUSTED
#
# MessageText:
#
# Copy Protection Error - The drive's region setting may be permanent or the number of user resets has been exhausted.
#
STG_E_RESETS_EXHAUSTED = 0x8003030B

# /*++

#  MessageId's 0x0305 - 0x031f (inclusive) are reserved for **STORAGE**
#  copy protection errors.

# --*/
# ******************
# FACILITY_RPC
# ******************
#
# Codes 0x0-0x11 are propagated from 16 bit OLE.
#
#
# MessageId: RPC_E_CALL_REJECTED
#
# MessageText:
#
# Call was rejected by callee.
#
RPC_E_CALL_REJECTED = 0x80010001

#
# MessageId: RPC_E_CALL_CANCELED
#
# MessageText:
#
# Call was canceled by the message filter.
#
RPC_E_CALL_CANCELED = 0x80010002

#
# MessageId: RPC_E_CANTPOST_INSENDCALL
#
# MessageText:
#
# The caller is dispatching an intertask SendMessage call and cannot call out via PostMessage.
#
RPC_E_CANTPOST_INSENDCALL = 0x80010003

#
# MessageId: RPC_E_CANTCALLOUT_INASYNCCALL
#
# MessageText:
#
# The caller is dispatching an asynchronous call and cannot make an outgoing call on behalf of this call.
#
RPC_E_CANTCALLOUT_INASYNCCALL = 0x80010004

#
# MessageId: RPC_E_CANTCALLOUT_INEXTERNALCALL
#
# MessageText:
#
# It is illegal to call out while inside message filter.
#
RPC_E_CANTCALLOUT_INEXTERNALCALL = 0x80010005

#
# MessageId: RPC_E_CONNECTION_TERMINATED
#
# MessageText:
#
# The connection terminated or is in a bogus state and cannot be used any more. Other connections are still valid.
#
RPC_E_CONNECTION_TERMINATED = 0x80010006

#
# MessageId: RPC_E_SERVER_DIED
#
# MessageText:
#
# The callee (server [not server application]) is not available and disappeared; all connections are invalid. The call may have executed.
#
RPC_E_SERVER_DIED = 0x80010007

#
# MessageId: RPC_E_CLIENT_DIED
#
# MessageText:
#
# The caller (client) disappeared while the callee (server) was processing a call.
#
RPC_E_CLIENT_DIED = 0x80010008

#
# MessageId: RPC_E_INVALID_DATAPACKET
#
# MessageText:
#
# The data packet with the marshalled parameter data is incorrect.
#
RPC_E_INVALID_DATAPACKET = 0x80010009

#
# MessageId: RPC_E_CANTTRANSMIT_CALL
#
# MessageText:
#
# The call was not transmitted properly; the message queue was full and was not emptied after yielding.
#
RPC_E_CANTTRANSMIT_CALL = 0x8001000A

#
# MessageId: RPC_E_CLIENT_CANTMARSHAL_DATA
#
# MessageText:
#
# The client (caller) cannot marshall the parameter data - low memory, etc.
#
RPC_E_CLIENT_CANTMARSHAL_DATA = 0x8001000B

#
# MessageId: RPC_E_CLIENT_CANTUNMARSHAL_DATA
#
# MessageText:
#
# The client (caller) cannot unmarshall the return data - low memory, etc.
#
RPC_E_CLIENT_CANTUNMARSHAL_DATA = 0x8001000C

#
# MessageId: RPC_E_SERVER_CANTMARSHAL_DATA
#
# MessageText:
#
# The server (callee) cannot marshall the return data - low memory, etc.
#
RPC_E_SERVER_CANTMARSHAL_DATA = 0x8001000D

#
# MessageId: RPC_E_SERVER_CANTUNMARSHAL_DATA
#
# MessageText:
#
# The server (callee) cannot unmarshall the parameter data - low memory, etc.
#
RPC_E_SERVER_CANTUNMARSHAL_DATA = 0x8001000E

#
# MessageId: RPC_E_INVALID_DATA
#
# MessageText:
#
# Received data is invalid; could be server or client data.
#
RPC_E_INVALID_DATA = 0x8001000F

#
# MessageId: RPC_E_INVALID_PARAMETER
#
# MessageText:
#
# A particular parameter is invalid and cannot be (un)marshalled.
#
RPC_E_INVALID_PARAMETER = 0x80010010

#
# MessageId: RPC_E_CANTCALLOUT_AGAIN
#
# MessageText:
#
# There is no second outgoing call on same channel in DDE conversation.
#
RPC_E_CANTCALLOUT_AGAIN = 0x80010011

#
# MessageId: RPC_E_SERVER_DIED_DNE
#
# MessageText:
#
# The callee (server [not server application]) is not available and disappeared; all connections are invalid. The call did not execute.
#
RPC_E_SERVER_DIED_DNE = 0x80010012

#
# MessageId: RPC_E_SYS_CALL_FAILED
#
# MessageText:
#
# System call failed.
#
RPC_E_SYS_CALL_FAILED = 0x80010100

#
# MessageId: RPC_E_OUT_OF_RESOURCES
#
# MessageText:
#
# Could not allocate some required resource (memory, events, ...)
#
RPC_E_OUT_OF_RESOURCES = 0x80010101

#
# MessageId: RPC_E_ATTEMPTED_MULTITHREAD
#
# MessageText:
#
# Attempted to make calls on more than one thread in single threaded mode.
#
RPC_E_ATTEMPTED_MULTITHREAD = 0x80010102

#
# MessageId: RPC_E_NOT_REGISTERED
#
# MessageText:
#
# The requested interface is not registered on the server object.
#
RPC_E_NOT_REGISTERED = 0x80010103

#
# MessageId: RPC_E_FAULT
#
# MessageText:
#
# RPC could not call the server or could not return the results of calling the server.
#
RPC_E_FAULT = 0x80010104

#
# MessageId: RPC_E_SERVERFAULT
#
# MessageText:
#
# The server threw an exception.
#
RPC_E_SERVERFAULT = 0x80010105

#
# MessageId: RPC_E_CHANGED_MODE
#
# MessageText:
#
# Cannot change thread mode after it is set.
#
RPC_E_CHANGED_MODE = 0x80010106

#
# MessageId: RPC_E_INVALIDMETHOD
#
# MessageText:
#
# The method called does not exist on the server.
#
RPC_E_INVALIDMETHOD = 0x80010107

#
# MessageId: RPC_E_DISCONNECTED
#
# MessageText:
#
# The object invoked has disconnected from its clients.
#
RPC_E_DISCONNECTED = 0x80010108

#
# MessageId: RPC_E_RETRY
#
# MessageText:
#
# The object invoked chose not to process the call now. Try again later.
#
RPC_E_RETRY = 0x80010109

#
# MessageId: RPC_E_SERVERCALL_RETRYLATER
#
# MessageText:
#
# The message filter indicated that the application is busy.
#
RPC_E_SERVERCALL_RETRYLATER = 0x8001010A

#
# MessageId: RPC_E_SERVERCALL_REJECTED
#
# MessageText:
#
# The message filter rejected the call.
#
RPC_E_SERVERCALL_REJECTED = 0x8001010B

#
# MessageId: RPC_E_INVALID_CALLDATA
#
# MessageText:
#
# A call control interfaces was called with invalid data.
#
RPC_E_INVALID_CALLDATA = 0x8001010C

#
# MessageId: RPC_E_CANTCALLOUT_ININPUTSYNCCALL
#
# MessageText:
#
# An outgoing call cannot be made since the application is dispatching an input-synchronous call.
#
RPC_E_CANTCALLOUT_ININPUTSYNCCALL = 0x8001010D

#
# MessageId: RPC_E_WRONG_THREAD
#
# MessageText:
#
# The application called an interface that was marshalled for a different thread.
#
RPC_E_WRONG_THREAD = 0x8001010E

#
# MessageId: RPC_E_THREAD_NOT_INIT
#
# MessageText:
#
# CoInitialize has not been called on the current thread.
#
RPC_E_THREAD_NOT_INIT = 0x8001010F

#
# MessageId: RPC_E_VERSION_MISMATCH
#
# MessageText:
#
# The version of OLE on the client and server machines does not match.
#
RPC_E_VERSION_MISMATCH = 0x80010110

#
# MessageId: RPC_E_INVALID_HEADER
#
# MessageText:
#
# OLE received a packet with an invalid header.
#
RPC_E_INVALID_HEADER = 0x80010111

#
# MessageId: RPC_E_INVALID_EXTENSION
#
# MessageText:
#
# OLE received a packet with an invalid extension.
#
RPC_E_INVALID_EXTENSION = 0x80010112

#
# MessageId: RPC_E_INVALID_IPID
#
# MessageText:
#
# The requested object or interface does not exist.
#
RPC_E_INVALID_IPID = 0x80010113

#
# MessageId: RPC_E_INVALID_OBJECT
#
# MessageText:
#
# The requested object does not exist.
#
RPC_E_INVALID_OBJECT = 0x80010114

#
# MessageId: RPC_S_CALLPENDING
#
# MessageText:
#
# OLE has sent a request and is waiting for a reply.
#
RPC_S_CALLPENDING = 0x80010115

#
# MessageId: RPC_S_WAITONTIMER
#
# MessageText:
#
# OLE is waiting before retrying a request.
#
RPC_S_WAITONTIMER = 0x80010116

#
# MessageId: RPC_E_CALL_COMPLETE
#
# MessageText:
#
# Call context cannot be accessed after call completed.
#
RPC_E_CALL_COMPLETE = 0x80010117

#
# MessageId: RPC_E_UNSECURE_CALL
#
# MessageText:
#
# Impersonate on unsecure calls is not supported.
#
RPC_E_UNSECURE_CALL = 0x80010118

#
# MessageId: RPC_E_TOO_LATE
#
# MessageText:
#
# Security must be initialized before any interfaces are marshalled or unmarshalled. It cannot be changed once initialized.
#
RPC_E_TOO_LATE = 0x80010119

#
# MessageId: RPC_E_NO_GOOD_SECURITY_PACKAGES
#
# MessageText:
#
# No security packages are installed on this machine or the user is not logged on or there are no compatible security packages between the client and server.
#
RPC_E_NO_GOOD_SECURITY_PACKAGES = 0x8001011A

#
# MessageId: RPC_E_ACCESS_DENIED
#
# MessageText:
#
# Access is denied.
#
RPC_E_ACCESS_DENIED = 0x8001011B

#
# MessageId: RPC_E_REMOTE_DISABLED
#
# MessageText:
#
# Remote calls are not allowed for this process.
#
RPC_E_REMOTE_DISABLED = 0x8001011C

#
# MessageId: RPC_E_INVALID_OBJREF
#
# MessageText:
#
# The marshaled interface data packet (OBJREF) has an invalid or unknown format.
#
RPC_E_INVALID_OBJREF = 0x8001011D

#
# MessageId: RPC_E_NO_CONTEXT
#
# MessageText:
#
# No context is associated with this call. This happens for some custom marshalled calls and on the client side of the call.
#
RPC_E_NO_CONTEXT = 0x8001011E

#
# MessageId: RPC_E_TIMEOUT
#
# MessageText:
#
# This operation returned because the timeout period expired.
#
RPC_E_TIMEOUT = 0x8001011F

#
# MessageId: RPC_E_NO_SYNC
#
# MessageText:
#
# There are no synchronize objects to wait on.
#
RPC_E_NO_SYNC = 0x80010120

#
# MessageId: RPC_E_FULLSIC_REQUIRED
#
# MessageText:
#
# Full subject issuer chain SSL principal name expected from the server.
#
RPC_E_FULLSIC_REQUIRED = 0x80010121

#
# MessageId: RPC_E_INVALID_STD_NAME
#
# MessageText:
#
# Principal name is not a valid MSSTD name.
#
RPC_E_INVALID_STD_NAME = 0x80010122

#
# MessageId: CO_E_FAILEDTOIMPERSONATE
#
# MessageText:
#
# Unable to impersonate DCOM client
#
CO_E_FAILEDTOIMPERSONATE = 0x80010123

#
# MessageId: CO_E_FAILEDTOGETSECCTX
#
# MessageText:
#
# Unable to obtain server's security context
#
CO_E_FAILEDTOGETSECCTX = 0x80010124

#
# MessageId: CO_E_FAILEDTOOPENTHREADTOKEN
#
# MessageText:
#
# Unable to open the access token of the current thread
#
CO_E_FAILEDTOOPENTHREADTOKEN = 0x80010125

#
# MessageId: CO_E_FAILEDTOGETTOKENINFO
#
# MessageText:
#
# Unable to obtain user info from an access token
#
CO_E_FAILEDTOGETTOKENINFO = 0x80010126

#
# MessageId: CO_E_TRUSTEEDOESNTMATCHCLIENT
#
# MessageText:
#
# The client who called IAccessControl::IsAccessPermitted was not the trustee provided to the method
#
CO_E_TRUSTEEDOESNTMATCHCLIENT = 0x80010127

#
# MessageId: CO_E_FAILEDTOQUERYCLIENTBLANKET
#
# MessageText:
#
# Unable to obtain the client's security blanket
#
CO_E_FAILEDTOQUERYCLIENTBLANKET = 0x80010128

#
# MessageId: CO_E_FAILEDTOSETDACL
#
# MessageText:
#
# Unable to set a discretionary ACL into a security descriptor
#
CO_E_FAILEDTOSETDACL = 0x80010129

#
# MessageId: CO_E_ACCESSCHECKFAILED
#
# MessageText:
#
# The system function, AccessCheck, returned false
#
CO_E_ACCESSCHECKFAILED = 0x8001012A

#
# MessageId: CO_E_NETACCESSAPIFAILED
#
# MessageText:
#
# Either NetAccessDel or NetAccessAdd returned an error code.
#
CO_E_NETACCESSAPIFAILED = 0x8001012B

#
# MessageId: CO_E_WRONGTRUSTEENAMESYNTAX
#
# MessageText:
#
# One of the trustee strings provided by the user did not conform to the <Domain>\<Name> syntax and it was not the "*" string
#
CO_E_WRONGTRUSTEENAMESYNTAX = 0x8001012C

#
# MessageId: CO_E_INVALIDSID
#
# MessageText:
#
# One of the security identifiers provided by the user was invalid
#
CO_E_INVALIDSID = 0x8001012D

#
# MessageId: CO_E_CONVERSIONFAILED
#
# MessageText:
#
# Unable to convert a wide character trustee string to a multibyte trustee string
#
CO_E_CONVERSIONFAILED = 0x8001012E

#
# MessageId: CO_E_NOMATCHINGSIDFOUND
#
# MessageText:
#
# Unable to find a security identifier that corresponds to a trustee string provided by the user
#
CO_E_NOMATCHINGSIDFOUND = 0x8001012F

#
# MessageId: CO_E_LOOKUPACCSIDFAILED
#
# MessageText:
#
# The system function, LookupAccountSID, failed
#
CO_E_LOOKUPACCSIDFAILED = 0x80010130

#
# MessageId: CO_E_NOMATCHINGNAMEFOUND
#
# MessageText:
#
# Unable to find a trustee name that corresponds to a security identifier provided by the user
#
CO_E_NOMATCHINGNAMEFOUND = 0x80010131

#
# MessageId: CO_E_LOOKUPACCNAMEFAILED
#
# MessageText:
#
# The system function, LookupAccountName, failed
#
CO_E_LOOKUPACCNAMEFAILED = 0x80010132

#
# MessageId: CO_E_SETSERLHNDLFAILED
#
# MessageText:
#
# Unable to set or reset a serialization handle
#
CO_E_SETSERLHNDLFAILED = 0x80010133

#
# MessageId: CO_E_FAILEDTOGETWINDIR
#
# MessageText:
#
# Unable to obtain the Windows directory
#
CO_E_FAILEDTOGETWINDIR = 0x80010134

#
# MessageId: CO_E_PATHTOOLONG
#
# MessageText:
#
# Path too long
#
CO_E_PATHTOOLONG = 0x80010135

#
# MessageId: CO_E_FAILEDTOGENUUID
#
# MessageText:
#
# Unable to generate a uuid.
#
CO_E_FAILEDTOGENUUID = 0x80010136

#
# MessageId: CO_E_FAILEDTOCREATEFILE
#
# MessageText:
#
# Unable to create file
#
CO_E_FAILEDTOCREATEFILE = 0x80010137

#
# MessageId: CO_E_FAILEDTOCLOSEHANDLE
#
# MessageText:
#
# Unable to close a serialization handle or a file handle.
#
CO_E_FAILEDTOCLOSEHANDLE = 0x80010138

#
# MessageId: CO_E_EXCEEDSYSACLLIMIT
#
# MessageText:
#
# The number of ACEs in an ACL exceeds the system limit.
#
CO_E_EXCEEDSYSACLLIMIT = 0x80010139

#
# MessageId: CO_E_ACESINWRONGORDER
#
# MessageText:
#
# Not all the DENY_ACCESS ACEs are arranged in front of the GRANT_ACCESS ACEs in the stream.
#
CO_E_ACESINWRONGORDER = 0x8001013A

#
# MessageId: CO_E_INCOMPATIBLESTREAMVERSION
#
# MessageText:
#
# The version of ACL format in the stream is not supported by this implementation of IAccessControl
#
CO_E_INCOMPATIBLESTREAMVERSION = 0x8001013B

#
# MessageId: CO_E_FAILEDTOOPENPROCESSTOKEN
#
# MessageText:
#
# Unable to open the access token of the server process
#
CO_E_FAILEDTOOPENPROCESSTOKEN = 0x8001013C

#
# MessageId: CO_E_DECODEFAILED
#
# MessageText:
#
# Unable to decode the ACL in the stream provided by the user
#
CO_E_DECODEFAILED = 0x8001013D

#
# MessageId: CO_E_ACNOTINITIALIZED
#
# MessageText:
#
# The COM IAccessControl object is not initialized
#
CO_E_ACNOTINITIALIZED = 0x8001013F

#
# MessageId: CO_E_CANCEL_DISABLED
#
# MessageText:
#
# Call Cancellation is disabled
#
CO_E_CANCEL_DISABLED = 0x80010140

#
# MessageId: RPC_E_UNEXPECTED
#
# MessageText:
#
# An internal error occurred.
#
RPC_E_UNEXPECTED = 0x8001FFFF



#////////////////////////////////////
#                                  //
# Additional Security Status Codes //
#                                  //
# Facility=Security                //
#                                  //
#////////////////////////////////////


#
# MessageId: ERROR_AUDITING_DISABLED
#
# MessageText:
#
# The specified event is currently not being audited.
#
ERROR_AUDITING_DISABLED = 0xC0090001

#
# MessageId: ERROR_ALL_SIDS_FILTERED
#
# MessageText:
#
# The SID filtering operation removed all SIDs.
#
ERROR_ALL_SIDS_FILTERED = 0xC0090002

#
# MessageId: ERROR_BIZRULES_NOT_ENABLED
#
# MessageText:
#
# Business rule scripts are disabled for the calling application.
#
ERROR_BIZRULES_NOT_ENABLED = 0xC0090003



#///////////////////////////////////////////
#                                         //
# end of Additional Security Status Codes //
#                                         //
#///////////////////////////////////////////



 ####################
 ##
 ##  FACILITY_SSPI
 ##
 ####################

#
# MessageId: NTE_BAD_UID
#
# MessageText:
#
# Bad UID.
#
NTE_BAD_UID = 0x80090001

#
# MessageId: NTE_BAD_HASH
#
# MessageText:
#
# Bad Hash.
#
NTE_BAD_HASH = 0x80090002

#
# MessageId: NTE_BAD_KEY
#
# MessageText:
#
# Bad Key.
#
NTE_BAD_KEY = 0x80090003

#
# MessageId: NTE_BAD_LEN
#
# MessageText:
#
# Bad Length.
#
NTE_BAD_LEN = 0x80090004

#
# MessageId: NTE_BAD_DATA
#
# MessageText:
#
# Bad Data.
#
NTE_BAD_DATA = 0x80090005

#
# MessageId: NTE_BAD_SIGNATURE
#
# MessageText:
#
# Invalid Signature.
#
NTE_BAD_SIGNATURE = 0x80090006

#
# MessageId: NTE_BAD_VER
#
# MessageText:
#
# Bad Version of provider.
#
NTE_BAD_VER = 0x80090007

#
# MessageId: NTE_BAD_ALGID
#
# MessageText:
#
# Invalid algorithm specified.
#
NTE_BAD_ALGID = 0x80090008

#
# MessageId: NTE_BAD_FLAGS
#
# MessageText:
#
# Invalid flags specified.
#
NTE_BAD_FLAGS = 0x80090009

#
# MessageId: NTE_BAD_TYPE
#
# MessageText:
#
# Invalid type specified.
#
NTE_BAD_TYPE = 0x8009000A

#
# MessageId: NTE_BAD_KEY_STATE
#
# MessageText:
#
# Key not valid for use in specified state.
#
NTE_BAD_KEY_STATE = 0x8009000B

#
# MessageId: NTE_BAD_HASH_STATE
#
# MessageText:
#
# Hash not valid for use in specified state.
#
NTE_BAD_HASH_STATE = 0x8009000C

#
# MessageId: NTE_NO_KEY
#
# MessageText:
#
# Key does not exist.
#
NTE_NO_KEY = 0x8009000D

#
# MessageId: NTE_NO_MEMORY
#
# MessageText:
#
# Insufficient memory available for the operation.
#
NTE_NO_MEMORY = 0x8009000E

#
# MessageId: NTE_EXISTS
#
# MessageText:
#
# Object already exists.
#
NTE_EXISTS = 0x8009000F

#
# MessageId: NTE_PERM
#
# MessageText:
#
# Access denied.
#
NTE_PERM = 0x80090010

#
# MessageId: NTE_NOT_FOUND
#
# MessageText:
#
# Object was not found.
#
NTE_NOT_FOUND = 0x80090011

#
# MessageId: NTE_DOUBLE_ENCRYPT
#
# MessageText:
#
# Data already encrypted.
#
NTE_DOUBLE_ENCRYPT = 0x80090012

#
# MessageId: NTE_BAD_PROVIDER
#
# MessageText:
#
# Invalid provider specified.
#
NTE_BAD_PROVIDER = 0x80090013

#
# MessageId: NTE_BAD_PROV_TYPE
#
# MessageText:
#
# Invalid provider type specified.
#
NTE_BAD_PROV_TYPE = 0x80090014

#
# MessageId: NTE_BAD_PUBLIC_KEY
#
# MessageText:
#
# Provider's public key is invalid.
#
NTE_BAD_PUBLIC_KEY = 0x80090015

#
# MessageId: NTE_BAD_KEYSET
#
# MessageText:
#
# Keyset does not exist
#
NTE_BAD_KEYSET = 0x80090016

#
# MessageId: NTE_PROV_TYPE_NOT_DEF
#
# MessageText:
#
# Provider type not defined.
#
NTE_PROV_TYPE_NOT_DEF = 0x80090017

#
# MessageId: NTE_PROV_TYPE_ENTRY_BAD
#
# MessageText:
#
# Provider type as registered is invalid.
#
NTE_PROV_TYPE_ENTRY_BAD = 0x80090018

#
# MessageId: NTE_KEYSET_NOT_DEF
#
# MessageText:
#
# The keyset is not defined.
#
NTE_KEYSET_NOT_DEF = 0x80090019

#
# MessageId: NTE_KEYSET_ENTRY_BAD
#
# MessageText:
#
# Keyset as registered is invalid.
#
NTE_KEYSET_ENTRY_BAD = 0x8009001A

#
# MessageId: NTE_PROV_TYPE_NO_MATCH
#
# MessageText:
#
# Provider type does not match registered value.
#
NTE_PROV_TYPE_NO_MATCH = 0x8009001B

#
# MessageId: NTE_SIGNATURE_FILE_BAD
#
# MessageText:
#
# The digital signature file is corrupt.
#
NTE_SIGNATURE_FILE_BAD = 0x8009001C

#
# MessageId: NTE_PROVIDER_DLL_FAIL
#
# MessageText:
#
# Provider DLL failed to initialize correctly.
#
NTE_PROVIDER_DLL_FAIL = 0x8009001D

#
# MessageId: NTE_PROV_DLL_NOT_FOUND
#
# MessageText:
#
# Provider DLL could not be found.
#
NTE_PROV_DLL_NOT_FOUND = 0x8009001E

#
# MessageId: NTE_BAD_KEYSET_PARAM
#
# MessageText:
#
# The Keyset parameter is invalid.
#
NTE_BAD_KEYSET_PARAM = 0x8009001F

#
# MessageId: NTE_FAIL
#
# MessageText:
#
# An internal error occurred.
#
NTE_FAIL = 0x80090020

#
# MessageId: NTE_SYS_ERR
#
# MessageText:
#
# A base error occurred.
#
NTE_SYS_ERR = 0x80090021

#
# MessageId: NTE_SILENT_CONTEXT
#
# MessageText:
#
# Provider could not perform the action since the context was acquired as silent.
#
NTE_SILENT_CONTEXT = 0x80090022

#
# MessageId: NTE_TOKEN_KEYSET_STORAGE_FULL
#
# MessageText:
#
# The security token does not have storage space available for an additional container.
#
NTE_TOKEN_KEYSET_STORAGE_FULL = 0x80090023

#
# MessageId: NTE_TEMPORARY_PROFILE
#
# MessageText:
#
# The profile for the user is a temporary profile.
#
NTE_TEMPORARY_PROFILE = 0x80090024

#
# MessageId: NTE_FIXEDPARAMETER
#
# MessageText:
#
# The key parameters could not be set because the CSP uses fixed parameters.
#
NTE_FIXEDPARAMETER = 0x80090025

#
# MessageId: NTE_INVALID_HANDLE
#
# MessageText:
#
# The supplied handle is invalid.
#
NTE_INVALID_HANDLE = 0x80090026

#
# MessageId: NTE_INVALID_PARAMETER
#
# MessageText:
#
# The parameter is incorrect.
#
NTE_INVALID_PARAMETER = 0x80090027

#
# MessageId: NTE_BUFFER_TOO_SMALL
#
# MessageText:
#
# The buffer supplied to a function was too small.
#
NTE_BUFFER_TOO_SMALL = 0x80090028

#
# MessageId: NTE_NOT_SUPPORTED
#
# MessageText:
#
# The requested operation is not supported.
#
NTE_NOT_SUPPORTED = 0x80090029

#
# MessageId: NTE_NO_MORE_ITEMS
#
# MessageText:
#
# No more data is available.
#
NTE_NO_MORE_ITEMS = 0x8009002A

#
# MessageId: NTE_BUFFERS_OVERLAP
#
# MessageText:
#
# The supplied buffers overlap incorrectly.
#
NTE_BUFFERS_OVERLAP = 0x8009002B

#
# MessageId: NTE_DECRYPTION_FAILURE
#
# MessageText:
#
# The specified data could not be decrypted.
#
NTE_DECRYPTION_FAILURE = 0x8009002C

#
# MessageId: NTE_INTERNAL_ERROR
#
# MessageText:
#
# An internal consistency check failed.
#
NTE_INTERNAL_ERROR = 0x8009002D

#
# MessageId: NTE_UI_REQUIRED
#
# MessageText:
#
# This operation requires input from the user.
#
NTE_UI_REQUIRED = 0x8009002E

#
# MessageId: NTE_HMAC_NOT_SUPPORTED
#
# MessageText:
#
# The cryptographic provider does not support HMAC.
#
NTE_HMAC_NOT_SUPPORTED = 0x8009002F

#
# MessageId: NTE_DEVICE_NOT_READY
#
# MessageText:
#
# The device that is required by this cryptographic provider is not ready for use.
#
NTE_DEVICE_NOT_READY = 0x80090030

#
# MessageId: NTE_AUTHENTICATION_IGNORED
#
# MessageText:
#
# The dictionary attack mitigation is triggered and the provided authorization was ignored by the provider.
#
NTE_AUTHENTICATION_IGNORED = 0x80090031

#
# MessageId: NTE_VALIDATION_FAILED
#
# MessageText:
#
# The validation of the provided data failed the integrity or signature validation.
#
NTE_VALIDATION_FAILED = 0x80090032

#
# MessageId: NTE_INCORRECT_PASSWORD
#
# MessageText:
#
# Incorrect password.
#
NTE_INCORRECT_PASSWORD = 0x80090033

#
# MessageId: NTE_ENCRYPTION_FAILURE
#
# MessageText:
#
# Encryption failed.
#
NTE_ENCRYPTION_FAILURE = 0x80090034

#
# MessageId: NTE_DEVICE_NOT_FOUND
#
# MessageText:
#
# The device that is required by this cryptographic provider is not found on this platform.
#
NTE_DEVICE_NOT_FOUND = 0x80090035

#
# MessageId: SEC_E_INSUFFICIENT_MEMORY
#
# MessageText:
#
# Not enough memory is available to complete this request
#
SEC_E_INSUFFICIENT_MEMORY = 0x80090300

#
# MessageId: SEC_E_INVALID_HANDLE
#
# MessageText:
#
# The handle specified is invalid
#
SEC_E_INVALID_HANDLE = 0x80090301

#
# MessageId: SEC_E_UNSUPPORTED_FUNCTION
#
# MessageText:
#
# The function requested is not supported
#
SEC_E_UNSUPPORTED_FUNCTION = 0x80090302

#
# MessageId: SEC_E_TARGET_UNKNOWN
#
# MessageText:
#
# The specified target is unknown or unreachable
#
SEC_E_TARGET_UNKNOWN = 0x80090303

#
# MessageId: SEC_E_INTERNAL_ERROR
#
# MessageText:
#
# The Local Security Authority cannot be contacted
#
SEC_E_INTERNAL_ERROR = 0x80090304

#
# MessageId: SEC_E_SECPKG_NOT_FOUND
#
# MessageText:
#
# The requested security package does not exist
#
SEC_E_SECPKG_NOT_FOUND = 0x80090305

#
# MessageId: SEC_E_NOT_OWNER
#
# MessageText:
#
# The caller is not the owner of the desired credentials
#
SEC_E_NOT_OWNER = 0x80090306

#
# MessageId: SEC_E_CANNOT_INSTALL
#
# MessageText:
#
# The security package failed to initialize, and cannot be installed
#
SEC_E_CANNOT_INSTALL = 0x80090307

#
# MessageId: SEC_E_INVALID_TOKEN
#
# MessageText:
#
# The token supplied to the function is invalid
#
SEC_E_INVALID_TOKEN = 0x80090308

#
# MessageId: SEC_E_CANNOT_PACK
#
# MessageText:
#
# The security package is not able to marshall the logon buffer, so the logon attempt has failed
#
SEC_E_CANNOT_PACK = 0x80090309

#
# MessageId: SEC_E_QOP_NOT_SUPPORTED
#
# MessageText:
#
# The per-message Quality of Protection is not supported by the security package
#
SEC_E_QOP_NOT_SUPPORTED = 0x8009030A

#
# MessageId: SEC_E_NO_IMPERSONATION
#
# MessageText:
#
# The security context does not allow impersonation of the client
#
SEC_E_NO_IMPERSONATION = 0x8009030B

#
# MessageId: SEC_E_LOGON_DENIED
#
# MessageText:
#
# The logon attempt failed
#
SEC_E_LOGON_DENIED = 0x8009030C

#
# MessageId: SEC_E_UNKNOWN_CREDENTIALS
#
# MessageText:
#
# The credentials supplied to the package were not recognized
#
SEC_E_UNKNOWN_CREDENTIALS = 0x8009030D

#
# MessageId: SEC_E_NO_CREDENTIALS
#
# MessageText:
#
# No credentials are available in the security package
#
SEC_E_NO_CREDENTIALS = 0x8009030E

#
# MessageId: SEC_E_MESSAGE_ALTERED
#
# MessageText:
#
# The message or signature supplied for verification has been altered
#
SEC_E_MESSAGE_ALTERED = 0x8009030F

#
# MessageId: SEC_E_OUT_OF_SEQUENCE
#
# MessageText:
#
# The message supplied for verification is out of sequence
#
SEC_E_OUT_OF_SEQUENCE = 0x80090310

#
# MessageId: SEC_E_NO_AUTHENTICATING_AUTHORITY
#
# MessageText:
#
# No authority could be contacted for authentication.
#
SEC_E_NO_AUTHENTICATING_AUTHORITY = 0x80090311

#
# MessageId: SEC_I_CONTINUE_NEEDED
#
# MessageText:
#
# The function completed successfully, but must be called again to complete the context
#
SEC_I_CONTINUE_NEEDED = 0x00090312

#
# MessageId: SEC_I_COMPLETE_NEEDED
#
# MessageText:
#
# The function completed successfully, but CompleteToken must be called
#
SEC_I_COMPLETE_NEEDED = 0x00090313

#
# MessageId: SEC_I_COMPLETE_AND_CONTINUE
#
# MessageText:
#
# The function completed successfully, but both CompleteToken and this function must be called to complete the context
#
SEC_I_COMPLETE_AND_CONTINUE = 0x00090314

#
# MessageId: SEC_I_LOCAL_LOGON
#
# MessageText:
#
# The logon was completed, but no network authority was available. The logon was made using locally known information
#
SEC_I_LOCAL_LOGON = 0x00090315

#
# MessageId: SEC_E_BAD_PKGID
#
# MessageText:
#
# The requested security package does not exist
#
SEC_E_BAD_PKGID = 0x80090316

#
# MessageId: SEC_E_CONTEXT_EXPIRED
#
# MessageText:
#
# The context has expired and can no longer be used.
#
SEC_E_CONTEXT_EXPIRED = 0x80090317

#
# MessageId: SEC_I_CONTEXT_EXPIRED
#
# MessageText:
#
# The context has expired and can no longer be used.
#
SEC_I_CONTEXT_EXPIRED = 0x00090317

#
# MessageId: SEC_E_INCOMPLETE_MESSAGE
#
# MessageText:
#
# The supplied message is incomplete. The signature was not verified.
#
SEC_E_INCOMPLETE_MESSAGE = 0x80090318

#
# MessageId: SEC_E_INCOMPLETE_CREDENTIALS
#
# MessageText:
#
# The credentials supplied were not complete, and could not be verified. The context could not be initialized.
#
SEC_E_INCOMPLETE_CREDENTIALS = 0x80090320

#
# MessageId: SEC_E_BUFFER_TOO_SMALL
#
# MessageText:
#
# The buffers supplied to a function was too small.
#
SEC_E_BUFFER_TOO_SMALL = 0x80090321

#
# MessageId: SEC_I_INCOMPLETE_CREDENTIALS
#
# MessageText:
#
# The credentials supplied were not complete, and could not be verified. Additional information can be returned from the context.
#
SEC_I_INCOMPLETE_CREDENTIALS = 0x00090320

#
# MessageId: SEC_I_RENEGOTIATE
#
# MessageText:
#
# The context data must be renegotiated with the peer.
#
SEC_I_RENEGOTIATE = 0x00090321

#
# MessageId: SEC_E_WRONG_PRINCIPAL
#
# MessageText:
#
# The target principal name is incorrect.
#
SEC_E_WRONG_PRINCIPAL = 0x80090322

#
# MessageId: SEC_I_NO_LSA_CONTEXT
#
# MessageText:
#
# There is no LSA mode context associated with this context.
#
SEC_I_NO_LSA_CONTEXT = 0x00090323

#
# MessageId: SEC_E_TIME_SKEW
#
# MessageText:
#
# The clocks on the client and server machines are skewed.
#
SEC_E_TIME_SKEW = 0x80090324

#
# MessageId: SEC_E_UNTRUSTED_ROOT
#
# MessageText:
#
# The certificate chain was issued by an authority that is not trusted.
#
SEC_E_UNTRUSTED_ROOT = 0x80090325

#
# MessageId: SEC_E_ILLEGAL_MESSAGE
#
# MessageText:
#
# The message received was unexpected or badly formatted.
#
SEC_E_ILLEGAL_MESSAGE = 0x80090326

#
# MessageId: SEC_E_CERT_UNKNOWN
#
# MessageText:
#
# An unknown error occurred while processing the certificate.
#
SEC_E_CERT_UNKNOWN = 0x80090327

#
# MessageId: SEC_E_CERT_EXPIRED
#
# MessageText:
#
# The received certificate has expired.
#
SEC_E_CERT_EXPIRED = 0x80090328

#
# MessageId: SEC_E_ENCRYPT_FAILURE
#
# MessageText:
#
# The specified data could not be encrypted.
#
SEC_E_ENCRYPT_FAILURE = 0x80090329

#
# MessageId: SEC_E_DECRYPT_FAILURE
#
# MessageText:
#
# The specified data could not be decrypted.
# 
#
SEC_E_DECRYPT_FAILURE = 0x80090330

#
# MessageId: SEC_E_ALGORITHM_MISMATCH
#
# MessageText:
#
# The client and server cannot communicate, because they do not possess a common algorithm.
#
SEC_E_ALGORITHM_MISMATCH = 0x80090331

#
# MessageId: SEC_E_SECURITY_QOS_FAILED
#
# MessageText:
#
# The security context could not be established due to a failure in the requested quality of service (e.g. mutual authentication or delegation).
#
SEC_E_SECURITY_QOS_FAILED = 0x80090332

#
# MessageId: SEC_E_UNFINISHED_CONTEXT_DELETED
#
# MessageText:
#
# A security context was deleted before the context was completed. This is considered a logon failure.
#
SEC_E_UNFINISHED_CONTEXT_DELETED = 0x80090333

#
# MessageId: SEC_E_NO_TGT_REPLY
#
# MessageText:
#
# The client is trying to negotiate a context and the server requires user-to-user but didn't send a TGT reply.
#
SEC_E_NO_TGT_REPLY = 0x80090334

#
# MessageId: SEC_E_NO_IP_ADDRESSES
#
# MessageText:
#
# Unable to accomplish the requested task because the local machine does not have any IP addresses.
#
SEC_E_NO_IP_ADDRESSES = 0x80090335

#
# MessageId: SEC_E_WRONG_CREDENTIAL_HANDLE
#
# MessageText:
#
# The supplied credential handle does not match the credential associated with the security context.
#
SEC_E_WRONG_CREDENTIAL_HANDLE = 0x80090336

#
# MessageId: SEC_E_CRYPTO_SYSTEM_INVALID
#
# MessageText:
#
# The crypto system or checksum function is invalid because a required function is unavailable.
#
SEC_E_CRYPTO_SYSTEM_INVALID = 0x80090337

#
# MessageId: SEC_E_MAX_REFERRALS_EXCEEDED
#
# MessageText:
#
# The number of maximum ticket referrals has been exceeded.
#
SEC_E_MAX_REFERRALS_EXCEEDED = 0x80090338

#
# MessageId: SEC_E_MUST_BE_KDC
#
# MessageText:
#
# The local machine must be a Kerberos KDC (domain controller) and it is not.
#
SEC_E_MUST_BE_KDC = 0x80090339

#
# MessageId: SEC_E_STRONG_CRYPTO_NOT_SUPPORTED
#
# MessageText:
#
# The other end of the security negotiation is requires strong crypto but it is not supported on the local machine.
#
SEC_E_STRONG_CRYPTO_NOT_SUPPORTED = 0x8009033A

#
# MessageId: SEC_E_TOO_MANY_PRINCIPALS
#
# MessageText:
#
# The KDC reply contained more than one principal name.
#
SEC_E_TOO_MANY_PRINCIPALS = 0x8009033B

#
# MessageId: SEC_E_NO_PA_DATA
#
# MessageText:
#
# Expected to find PA data for a hint of what etype to use, but it was not found.
#
SEC_E_NO_PA_DATA = 0x8009033C

#
# MessageId: SEC_E_PKINIT_NAME_MISMATCH
#
# MessageText:
#
# The client certificate does not contain a valid UPN, or does not match the client name in the logon request. Please contact your administrator.
#
SEC_E_PKINIT_NAME_MISMATCH = 0x8009033D

#
# MessageId: SEC_E_SMARTCARD_LOGON_REQUIRED
#
# MessageText:
#
# Smartcard logon is required and was not used.
#
SEC_E_SMARTCARD_LOGON_REQUIRED = 0x8009033E

#
# MessageId: SEC_E_SHUTDOWN_IN_PROGRESS
#
# MessageText:
#
# A system shutdown is in progress.
#
SEC_E_SHUTDOWN_IN_PROGRESS = 0x8009033F

#
# MessageId: SEC_E_KDC_INVALID_REQUEST
#
# MessageText:
#
# An invalid request was sent to the KDC.
#
SEC_E_KDC_INVALID_REQUEST = 0x80090340

#
# MessageId: SEC_E_KDC_UNABLE_TO_REFER
#
# MessageText:
#
# The KDC was unable to generate a referral for the service requested.
#
SEC_E_KDC_UNABLE_TO_REFER = 0x80090341

#
# MessageId: SEC_E_KDC_UNKNOWN_ETYPE
#
# MessageText:
#
# The encryption type requested is not supported by the KDC.
#
SEC_E_KDC_UNKNOWN_ETYPE = 0x80090342

#
# MessageId: SEC_E_UNSUPPORTED_PREAUTH
#
# MessageText:
#
# An unsupported preauthentication mechanism was presented to the Kerberos package.
#
SEC_E_UNSUPPORTED_PREAUTH = 0x80090343

#
# MessageId: SEC_E_DELEGATION_REQUIRED
#
# MessageText:
#
# The requested operation cannot be completed. The computer must be trusted for delegation and the current user account must be configured to allow delegation.
#
SEC_E_DELEGATION_REQUIRED = 0x80090345

#
# MessageId: SEC_E_BAD_BINDINGS
#
# MessageText:
#
# Client's supplied SSPI channel bindings were incorrect.
#
SEC_E_BAD_BINDINGS = 0x80090346

#
# MessageId: SEC_E_MULTIPLE_ACCOUNTS
#
# MessageText:
#
# The received certificate was mapped to multiple accounts.
#
SEC_E_MULTIPLE_ACCOUNTS = 0x80090347

#
# MessageId: SEC_E_NO_KERB_KEY
#
# MessageText:
#
#  SEC_E_NO_KERB_KEY
#
SEC_E_NO_KERB_KEY = 0x80090348

#
# MessageId: SEC_E_CERT_WRONG_USAGE
#
# MessageText:
#
# The certificate is not valid for the requested usage.
#
SEC_E_CERT_WRONG_USAGE = 0x80090349

#
# MessageId: SEC_E_DOWNGRADE_DETECTED
#
# MessageText:
#
# The system cannot contact a domain controller to service the authentication request. Please try again later.
#
SEC_E_DOWNGRADE_DETECTED = 0x80090350

#
# MessageId: SEC_E_SMARTCARD_CERT_REVOKED
#
# MessageText:
#
# The smartcard certificate used for authentication has been revoked. Please contact your system administrator. There may be additional information in the event log.
#
SEC_E_SMARTCARD_CERT_REVOKED = 0x80090351

#
# MessageId: SEC_E_ISSUING_CA_UNTRUSTED
#
# MessageText:
#
# An untrusted certificate authority was detected while processing the smartcard certificate used for authentication. Please contact your system administrator.
#
SEC_E_ISSUING_CA_UNTRUSTED = 0x80090352

#
# MessageId: SEC_E_REVOCATION_OFFLINE_C
#
# MessageText:
#
# The revocation status of the smartcard certificate used for authentication could not be determined. Please contact your system administrator.
#
SEC_E_REVOCATION_OFFLINE_C = 0x80090353

#
# MessageId: SEC_E_PKINIT_CLIENT_FAILURE
#
# MessageText:
#
# The smartcard certificate used for authentication was not trusted. Please contact your system administrator.
#
SEC_E_PKINIT_CLIENT_FAILURE = 0x80090354

#
# MessageId: SEC_E_SMARTCARD_CERT_EXPIRED
#
# MessageText:
#
# The smartcard certificate used for authentication has expired. Please contact your system administrator.
#
SEC_E_SMARTCARD_CERT_EXPIRED = 0x80090355

#
# MessageId: SEC_E_NO_S4U_PROT_SUPPORT
#
# MessageText:
#
# The Kerberos subsystem encountered an error. A service for user protocol request was made against a domain controller which does not support service for user.
#
SEC_E_NO_S = 4

#
# MessageId: SEC_E_CROSSREALM_DELEGATION_FAILURE
#
# MessageText:
#
# An attempt was made by this server to make a Kerberos constrained delegation request for a target outside of the server's realm. This is not supported, and indicates a misconfiguration on this server's allowed to delegate to list. Please contact your administrator.
#
SEC_E_CROSSREALM_DELEGATION_FAILURE = 0x80090357

#
# MessageId: SEC_E_REVOCATION_OFFLINE_KDC
#
# MessageText:
#
# The revocation status of the domain controller certificate used for smartcard authentication could not be determined. There is additional information in the system event log. Please contact your system administrator.
#
SEC_E_REVOCATION_OFFLINE_KDC = 0x80090358

#
# MessageId: SEC_E_ISSUING_CA_UNTRUSTED_KDC
#
# MessageText:
#
# An untrusted certificate authority was detected while processing the domain controller certificate used for authentication. There is additional information in the system event log. Please contact your system administrator.
#
SEC_E_ISSUING_CA_UNTRUSTED_KDC = 0x80090359

#
# MessageId: SEC_E_KDC_CERT_EXPIRED
#
# MessageText:
#
# The domain controller certificate used for smartcard logon has expired. Please contact your system administrator with the contents of your system event log.
#
SEC_E_KDC_CERT_EXPIRED = 0x8009035A

#
# MessageId: SEC_E_KDC_CERT_REVOKED
#
# MessageText:
#
# The domain controller certificate used for smartcard logon has been revoked. Please contact your system administrator with the contents of your system event log.
#
SEC_E_KDC_CERT_REVOKED = 0x8009035B

#
# MessageId: SEC_I_SIGNATURE_NEEDED
#
# MessageText:
#
# A signature operation must be performed before the user can authenticate.
#
SEC_I_SIGNATURE_NEEDED = 0x0009035C

#
# MessageId: SEC_E_INVALID_PARAMETER
#
# MessageText:
#
# One or more of the parameters passed to the function was invalid.
#
SEC_E_INVALID_PARAMETER = 0x8009035D

#
# MessageId: SEC_E_DELEGATION_POLICY
#
# MessageText:
#
# Client policy does not allow credential delegation to target server.
#
SEC_E_DELEGATION_POLICY = 0x8009035E

#
# MessageId: SEC_E_POLICY_NLTM_ONLY
#
# MessageText:
#
# Client policy does not allow credential delegation to target server with NLTM only authentication.
#
SEC_E_POLICY_NLTM_ONLY = 0x8009035F

#
# MessageId: SEC_I_NO_RENEGOTIATION
#
# MessageText:
#
# The recipient rejected the renegotiation request.
#
SEC_I_NO_RENEGOTIATION = 0x00090360

#
# MessageId: SEC_E_NO_CONTEXT
#
# MessageText:
#
# The required security context does not exist.
#
SEC_E_NO_CONTEXT = 0x80090361

#
# MessageId: SEC_E_PKU2U_CERT_FAILURE
#
# MessageText:
#
# The PKU2U protocol encountered an error while attempting to utilize the associated certificates.
#
SEC_E_PKU = 2

#
# MessageId: SEC_E_MUTUAL_AUTH_FAILED
#
# MessageText:
#
# The identity of the server computer could not be verified.
#
SEC_E_MUTUAL_AUTH_FAILED = 0x80090363

#
# MessageId: SEC_I_MESSAGE_FRAGMENT
#
# MessageText:
#
# The returned buffer is only a fragment of the message.  More fragments need to be returned.
#
SEC_I_MESSAGE_FRAGMENT = 0x00090364

#
# MessageId: SEC_E_ONLY_HTTPS_ALLOWED
#
# MessageText:
#
# Only https scheme is allowed.
#
SEC_E_ONLY_HTTPS_ALLOWED = 0x80090365

#
# MessageId: SEC_I_CONTINUE_NEEDED_MESSAGE_OK
#
# MessageText:
#
# The function completed successfully, but must be called again to complete the context.  Early start can be used.
#
SEC_I_CONTINUE_NEEDED_MESSAGE_OK = 0x00090366

#
# MessageId: SEC_E_APPLICATION_PROTOCOL_MISMATCH
#
# MessageText:
#
# No common application protocol exists between the client and the server. Application protocol negotiation failed.
#
SEC_E_APPLICATION_PROTOCOL_MISMATCH = 0x80090367

#
# Provided for backwards compatibility
#

SEC_E_NO_SPM = SEC_E_INTERNAL_ERROR
SEC_E_NOT_SUPPORTED = SEC_E_UNSUPPORTED_FUNCTION

#
# MessageId: CRYPT_E_MSG_ERROR
#
# MessageText:
#
# An error occurred while performing an operation on a cryptographic message.
#
CRYPT_E_MSG_ERROR = 0x80091001

#
# MessageId: CRYPT_E_UNKNOWN_ALGO
#
# MessageText:
#
# Unknown cryptographic algorithm.
#
CRYPT_E_UNKNOWN_ALGO = 0x80091002

#
# MessageId: CRYPT_E_OID_FORMAT
#
# MessageText:
#
# The object identifier is poorly formatted.
#
CRYPT_E_OID_FORMAT = 0x80091003

#
# MessageId: CRYPT_E_INVALID_MSG_TYPE
#
# MessageText:
#
# Invalid cryptographic message type.
#
CRYPT_E_INVALID_MSG_TYPE = 0x80091004

#
# MessageId: CRYPT_E_UNEXPECTED_ENCODING
#
# MessageText:
#
# Unexpected cryptographic message encoding.
#
CRYPT_E_UNEXPECTED_ENCODING = 0x80091005

#
# MessageId: CRYPT_E_AUTH_ATTR_MISSING
#
# MessageText:
#
# The cryptographic message does not contain an expected authenticated attribute.
#
CRYPT_E_AUTH_ATTR_MISSING = 0x80091006

#
# MessageId: CRYPT_E_HASH_VALUE
#
# MessageText:
#
# The hash value is not correct.
#
CRYPT_E_HASH_VALUE = 0x80091007

#
# MessageId: CRYPT_E_INVALID_INDEX
#
# MessageText:
#
# The index value is not valid.
#
CRYPT_E_INVALID_INDEX = 0x80091008

#
# MessageId: CRYPT_E_ALREADY_DECRYPTED
#
# MessageText:
#
# The content of the cryptographic message has already been decrypted.
#
CRYPT_E_ALREADY_DECRYPTED = 0x80091009

#
# MessageId: CRYPT_E_NOT_DECRYPTED
#
# MessageText:
#
# The content of the cryptographic message has not been decrypted yet.
#
CRYPT_E_NOT_DECRYPTED = 0x8009100A

#
# MessageId: CRYPT_E_RECIPIENT_NOT_FOUND
#
# MessageText:
#
# The enveloped-data message does not contain the specified recipient.
#
CRYPT_E_RECIPIENT_NOT_FOUND = 0x8009100B

#
# MessageId: CRYPT_E_CONTROL_TYPE
#
# MessageText:
#
# Invalid control type.
#
CRYPT_E_CONTROL_TYPE = 0x8009100C

#
# MessageId: CRYPT_E_ISSUER_SERIALNUMBER
#
# MessageText:
#
# Invalid issuer and/or serial number.
#
CRYPT_E_ISSUER_SERIALNUMBER = 0x8009100D

#
# MessageId: CRYPT_E_SIGNER_NOT_FOUND
#
# MessageText:
#
# Cannot find the original signer.
#
CRYPT_E_SIGNER_NOT_FOUND = 0x8009100E

#
# MessageId: CRYPT_E_ATTRIBUTES_MISSING
#
# MessageText:
#
# The cryptographic message does not contain all of the requested attributes.
#
CRYPT_E_ATTRIBUTES_MISSING = 0x8009100F

#
# MessageId: CRYPT_E_STREAM_MSG_NOT_READY
#
# MessageText:
#
# The streamed cryptographic message is not ready to return data.
#
CRYPT_E_STREAM_MSG_NOT_READY = 0x80091010

#
# MessageId: CRYPT_E_STREAM_INSUFFICIENT_DATA
#
# MessageText:
#
# The streamed cryptographic message requires more data to complete the decode operation.
#
CRYPT_E_STREAM_INSUFFICIENT_DATA = 0x80091011

#
# MessageId: CRYPT_I_NEW_PROTECTION_REQUIRED
#
# MessageText:
#
# The protected data needs to be re-protected.
#
CRYPT_I_NEW_PROTECTION_REQUIRED = 0x00091012

#
# MessageId: CRYPT_E_BAD_LEN
#
# MessageText:
#
# The length specified for the output data was insufficient.
#
CRYPT_E_BAD_LEN = 0x80092001

#
# MessageId: CRYPT_E_BAD_ENCODE
#
# MessageText:
#
# An error occurred during encode or decode operation.
#
CRYPT_E_BAD_ENCODE = 0x80092002

#
# MessageId: CRYPT_E_FILE_ERROR
#
# MessageText:
#
# An error occurred while reading or writing to a file.
#
CRYPT_E_FILE_ERROR = 0x80092003

#
# MessageId: CRYPT_E_NOT_FOUND
#
# MessageText:
#
# Cannot find object or property.
#
CRYPT_E_NOT_FOUND = 0x80092004

#
# MessageId: CRYPT_E_EXISTS
#
# MessageText:
#
# The object or property already exists.
#
CRYPT_E_EXISTS = 0x80092005

#
# MessageId: CRYPT_E_NO_PROVIDER
#
# MessageText:
#
# No provider was specified for the store or object.
#
CRYPT_E_NO_PROVIDER = 0x80092006

#
# MessageId: CRYPT_E_SELF_SIGNED
#
# MessageText:
#
# The specified certificate is self signed.
#
CRYPT_E_SELF_SIGNED = 0x80092007

#
# MessageId: CRYPT_E_DELETED_PREV
#
# MessageText:
#
# The previous certificate or CRL context was deleted.
#
CRYPT_E_DELETED_PREV = 0x80092008

#
# MessageId: CRYPT_E_NO_MATCH
#
# MessageText:
#
# Cannot find the requested object.
#
CRYPT_E_NO_MATCH = 0x80092009

#
# MessageId: CRYPT_E_UNEXPECTED_MSG_TYPE
#
# MessageText:
#
# The certificate does not have a property that references a private key.
#
CRYPT_E_UNEXPECTED_MSG_TYPE = 0x8009200A

#
# MessageId: CRYPT_E_NO_KEY_PROPERTY
#
# MessageText:
#
# Cannot find the certificate and private key for decryption.
#
CRYPT_E_NO_KEY_PROPERTY = 0x8009200B

#
# MessageId: CRYPT_E_NO_DECRYPT_CERT
#
# MessageText:
#
# Cannot find the certificate and private key to use for decryption.
#
CRYPT_E_NO_DECRYPT_CERT = 0x8009200C

#
# MessageId: CRYPT_E_BAD_MSG
#
# MessageText:
#
# Not a cryptographic message or the cryptographic message is not formatted correctly.
#
CRYPT_E_BAD_MSG = 0x8009200D

#
# MessageId: CRYPT_E_NO_SIGNER
#
# MessageText:
#
# The signed cryptographic message does not have a signer for the specified signer index.
#
CRYPT_E_NO_SIGNER = 0x8009200E

#
# MessageId: CRYPT_E_PENDING_CLOSE
#
# MessageText:
#
# Final closure is pending until additional frees or closes.
#
CRYPT_E_PENDING_CLOSE = 0x8009200F

#
# MessageId: CRYPT_E_REVOKED
#
# MessageText:
#
# The certificate is revoked.
#
CRYPT_E_REVOKED = 0x80092010

#
# MessageId: CRYPT_E_NO_REVOCATION_DLL
#
# MessageText:
#
# No Dll or exported function was found to verify revocation.
#
CRYPT_E_NO_REVOCATION_DLL = 0x80092011

#
# MessageId: CRYPT_E_NO_REVOCATION_CHECK
#
# MessageText:
#
# The revocation function was unable to check revocation for the certificate.
#
CRYPT_E_NO_REVOCATION_CHECK = 0x80092012

#
# MessageId: CRYPT_E_REVOCATION_OFFLINE
#
# MessageText:
#
# The revocation function was unable to check revocation because the revocation server was offline.
#
CRYPT_E_REVOCATION_OFFLINE = 0x80092013

#
# MessageId: CRYPT_E_NOT_IN_REVOCATION_DATABASE
#
# MessageText:
#
# The certificate is not in the revocation server's database.
#
CRYPT_E_NOT_IN_REVOCATION_DATABASE = 0x80092014

#
# MessageId: CRYPT_E_INVALID_NUMERIC_STRING
#
# MessageText:
#
# The string contains a non-numeric character.
#
CRYPT_E_INVALID_NUMERIC_STRING = 0x80092020

#
# MessageId: CRYPT_E_INVALID_PRINTABLE_STRING
#
# MessageText:
#
# The string contains a non-printable character.
#
CRYPT_E_INVALID_PRINTABLE_STRING = 0x80092021

#
# MessageId: CRYPT_E_INVALID_IA5_STRING
#
# MessageText:
#
# The string contains a character not in the 7 bit ASCII character set.
#
CRYPT_E_INVALID_IA = 5

#
# MessageId: CRYPT_E_INVALID_X500_STRING
#
# MessageText:
#
# The string contains an invalid X500 name attribute key, oid, value or delimiter.
#
CRYPT_E_INVALID_X50 = 0

#
# MessageId: CRYPT_E_NOT_CHAR_STRING
#
# MessageText:
#
# The dwValueType for the CERT_NAME_VALUE is not one of the character strings. Most likely it is either a CERT_RDN_ENCODED_BLOB or CERT_RDN_OCTET_STRING.
#
CRYPT_E_NOT_CHAR_STRING = 0x80092024

#
# MessageId: CRYPT_E_FILERESIZED
#
# MessageText:
#
# The Put operation cannot continue. The file needs to be resized. However, there is already a signature present. A complete signing operation must be done.
#
CRYPT_E_FILERESIZED = 0x80092025

#
# MessageId: CRYPT_E_SECURITY_SETTINGS
#
# MessageText:
#
# The cryptographic operation failed due to a local security option setting.
#
CRYPT_E_SECURITY_SETTINGS = 0x80092026

#
# MessageId: CRYPT_E_NO_VERIFY_USAGE_DLL
#
# MessageText:
#
# No DLL or exported function was found to verify subject usage.
#
CRYPT_E_NO_VERIFY_USAGE_DLL = 0x80092027

#
# MessageId: CRYPT_E_NO_VERIFY_USAGE_CHECK
#
# MessageText:
#
# The called function was unable to do a usage check on the subject.
#
CRYPT_E_NO_VERIFY_USAGE_CHECK = 0x80092028

#
# MessageId: CRYPT_E_VERIFY_USAGE_OFFLINE
#
# MessageText:
#
# Since the server was offline, the called function was unable to complete the usage check.
#
CRYPT_E_VERIFY_USAGE_OFFLINE = 0x80092029

#
# MessageId: CRYPT_E_NOT_IN_CTL
#
# MessageText:
#
# The subject was not found in a Certificate Trust List (CTL).
#
CRYPT_E_NOT_IN_CTL = 0x8009202A

#
# MessageId: CRYPT_E_NO_TRUSTED_SIGNER
#
# MessageText:
#
# None of the signers of the cryptographic message or certificate trust list is trusted.
#
CRYPT_E_NO_TRUSTED_SIGNER = 0x8009202B

#
# MessageId: CRYPT_E_MISSING_PUBKEY_PARA
#
# MessageText:
#
# The public key's algorithm parameters are missing.
#
CRYPT_E_MISSING_PUBKEY_PARA = 0x8009202C

#
# MessageId: CRYPT_E_OBJECT_LOCATOR_OBJECT_NOT_FOUND
#
# MessageText:
#
# An object could not be located using the object locator infrastructure with the given name.
#
CRYPT_E_OBJECT_LOCATOR_OBJECT_NOT_FOUND = 0x8009202D

#
# MessageId: CRYPT_E_OSS_ERROR
#
# MessageText:
#
# OSS Certificate encode/decode error code base
# 
# See asn1code.h for a definition of the OSS runtime errors. The OSS error values are offset by CRYPT_E_OSS_ERROR.
#
CRYPT_E_OSS_ERROR = 0x80093000

#
# MessageId: OSS_MORE_BUF
#
# MessageText:
#
# OSS ASN.1 Error: Output Buffer is too small.
#
OSS_MORE_BUF = 0x80093001

#
# MessageId: OSS_NEGATIVE_UINTEGER
#
# MessageText:
#
# OSS ASN.1 Error: Signed integer is encoded as a unsigned integer.
#
OSS_NEGATIVE_UINTEGER = 0x80093002

#
# MessageId: OSS_PDU_RANGE
#
# MessageText:
#
# OSS ASN.1 Error: Unknown ASN.1 data type.
#
OSS_PDU_RANGE = 0x80093003

#
# MessageId: OSS_MORE_INPUT
#
# MessageText:
#
# OSS ASN.1 Error: Output buffer is too small, the decoded data has been truncated.
#
OSS_MORE_INPUT = 0x80093004

#
# MessageId: OSS_DATA_ERROR
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_DATA_ERROR = 0x80093005

#
# MessageId: OSS_BAD_ARG
#
# MessageText:
#
# OSS ASN.1 Error: Invalid argument.
#
OSS_BAD_ARG = 0x80093006

#
# MessageId: OSS_BAD_VERSION
#
# MessageText:
#
# OSS ASN.1 Error: Encode/Decode version mismatch.
#
OSS_BAD_VERSION = 0x80093007

#
# MessageId: OSS_OUT_MEMORY
#
# MessageText:
#
# OSS ASN.1 Error: Out of memory.
#
OSS_OUT_MEMORY = 0x80093008

#
# MessageId: OSS_PDU_MISMATCH
#
# MessageText:
#
# OSS ASN.1 Error: Encode/Decode Error.
#
OSS_PDU_MISMATCH = 0x80093009

#
# MessageId: OSS_LIMITED
#
# MessageText:
#
# OSS ASN.1 Error: Internal Error.
#
OSS_LIMITED = 0x8009300A

#
# MessageId: OSS_BAD_PTR
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_BAD_PTR = 0x8009300B

#
# MessageId: OSS_BAD_TIME
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_BAD_TIME = 0x8009300C

#
# MessageId: OSS_INDEFINITE_NOT_SUPPORTED
#
# MessageText:
#
# OSS ASN.1 Error: Unsupported BER indefinite-length encoding.
#
OSS_INDEFINITE_NOT_SUPPORTED = 0x8009300D

#
# MessageId: OSS_MEM_ERROR
#
# MessageText:
#
# OSS ASN.1 Error: Access violation.
#
OSS_MEM_ERROR = 0x8009300E

#
# MessageId: OSS_BAD_TABLE
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_BAD_TABLE = 0x8009300F

#
# MessageId: OSS_TOO_LONG
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_TOO_LONG = 0x80093010

#
# MessageId: OSS_CONSTRAINT_VIOLATED
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_CONSTRAINT_VIOLATED = 0x80093011

#
# MessageId: OSS_FATAL_ERROR
#
# MessageText:
#
# OSS ASN.1 Error: Internal Error.
#
OSS_FATAL_ERROR = 0x80093012

#
# MessageId: OSS_ACCESS_SERIALIZATION_ERROR
#
# MessageText:
#
# OSS ASN.1 Error: Multi-threading conflict.
#
OSS_ACCESS_SERIALIZATION_ERROR = 0x80093013

#
# MessageId: OSS_NULL_TBL
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_NULL_TBL = 0x80093014

#
# MessageId: OSS_NULL_FCN
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_NULL_FCN = 0x80093015

#
# MessageId: OSS_BAD_ENCRULES
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_BAD_ENCRULES = 0x80093016

#
# MessageId: OSS_UNAVAIL_ENCRULES
#
# MessageText:
#
# OSS ASN.1 Error: Encode/Decode function not implemented.
#
OSS_UNAVAIL_ENCRULES = 0x80093017

#
# MessageId: OSS_CANT_OPEN_TRACE_WINDOW
#
# MessageText:
#
# OSS ASN.1 Error: Trace file error.
#
OSS_CANT_OPEN_TRACE_WINDOW = 0x80093018

#
# MessageId: OSS_UNIMPLEMENTED
#
# MessageText:
#
# OSS ASN.1 Error: Function not implemented.
#
OSS_UNIMPLEMENTED = 0x80093019

#
# MessageId: OSS_OID_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_OID_DLL_NOT_LINKED = 0x8009301A

#
# MessageId: OSS_CANT_OPEN_TRACE_FILE
#
# MessageText:
#
# OSS ASN.1 Error: Trace file error.
#
OSS_CANT_OPEN_TRACE_FILE = 0x8009301B

#
# MessageId: OSS_TRACE_FILE_ALREADY_OPEN
#
# MessageText:
#
# OSS ASN.1 Error: Trace file error.
#
OSS_TRACE_FILE_ALREADY_OPEN = 0x8009301C

#
# MessageId: OSS_TABLE_MISMATCH
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_TABLE_MISMATCH = 0x8009301D

#
# MessageId: OSS_TYPE_NOT_SUPPORTED
#
# MessageText:
#
# OSS ASN.1 Error: Invalid data.
#
OSS_TYPE_NOT_SUPPORTED = 0x8009301E

#
# MessageId: OSS_REAL_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_REAL_DLL_NOT_LINKED = 0x8009301F

#
# MessageId: OSS_REAL_CODE_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_REAL_CODE_NOT_LINKED = 0x80093020

#
# MessageId: OSS_OUT_OF_RANGE
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_OUT_OF_RANGE = 0x80093021

#
# MessageId: OSS_COPIER_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_COPIER_DLL_NOT_LINKED = 0x80093022

#
# MessageId: OSS_CONSTRAINT_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_CONSTRAINT_DLL_NOT_LINKED = 0x80093023

#
# MessageId: OSS_COMPARATOR_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_COMPARATOR_DLL_NOT_LINKED = 0x80093024

#
# MessageId: OSS_COMPARATOR_CODE_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_COMPARATOR_CODE_NOT_LINKED = 0x80093025

#
# MessageId: OSS_MEM_MGR_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_MEM_MGR_DLL_NOT_LINKED = 0x80093026

#
# MessageId: OSS_PDV_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_PDV_DLL_NOT_LINKED = 0x80093027

#
# MessageId: OSS_PDV_CODE_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_PDV_CODE_NOT_LINKED = 0x80093028

#
# MessageId: OSS_API_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_API_DLL_NOT_LINKED = 0x80093029

#
# MessageId: OSS_BERDER_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_BERDER_DLL_NOT_LINKED = 0x8009302A

#
# MessageId: OSS_PER_DLL_NOT_LINKED
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_PER_DLL_NOT_LINKED = 0x8009302B

#
# MessageId: OSS_OPEN_TYPE_ERROR
#
# MessageText:
#
# OSS ASN.1 Error: Program link error.
#
OSS_OPEN_TYPE_ERROR = 0x8009302C

#
# MessageId: OSS_MUTEX_NOT_CREATED
#
# MessageText:
#
# OSS ASN.1 Error: System resource error.
#
OSS_MUTEX_NOT_CREATED = 0x8009302D

#
# MessageId: OSS_CANT_CLOSE_TRACE_FILE
#
# MessageText:
#
# OSS ASN.1 Error: Trace file error.
#
OSS_CANT_CLOSE_TRACE_FILE = 0x8009302E

#
# MessageId: CRYPT_E_ASN1_ERROR
#
# MessageText:
#
# ASN1 Certificate encode/decode error code base. The ASN1 error values are offset by CRYPT_E_ASN1_ERROR.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_INTERNAL
#
# MessageText:
#
# ASN1 internal encode or decode error.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_EOD
#
# MessageText:
#
# ASN1 unexpected end of data.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_CORRUPT
#
# MessageText:
#
# ASN1 corrupted data.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_LARGE
#
# MessageText:
#
# ASN1 value too large.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_CONSTRAINT
#
# MessageText:
#
# ASN1 constraint violated.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_MEMORY
#
# MessageText:
#
# ASN1 out of memory.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_OVERFLOW
#
# MessageText:
#
# ASN1 buffer overflow.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_BADPDU
#
# MessageText:
#
# ASN1 function not supported for this PDU.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_BADARGS
#
# MessageText:
#
# ASN1 bad arguments to function call.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_BADREAL
#
# MessageText:
#
# ASN1 bad real value.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_BADTAG
#
# MessageText:
#
# ASN1 bad tag value met.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_CHOICE
#
# MessageText:
#
# ASN1 bad choice value.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_RULE
#
# MessageText:
#
# ASN1 bad encoding rule.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_UTF8
#
# MessageText:
#
# ASN1 bad unicode (UTF8).
#
CRYPT_E_ASN1_UTF = 8

#
# MessageId: CRYPT_E_ASN1_PDU_TYPE
#
# MessageText:
#
# ASN1 bad PDU type.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_NYI
#
# MessageText:
#
# ASN1 not yet implemented.
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_EXTENDED
#
# MessageText:
#
# ASN1 skipped unknown extension(s).
#
CRYPT_E_ASN = 1

#
# MessageId: CRYPT_E_ASN1_NOEOD
#
# MessageText:
#
# ASN1 end of data expected
#
CRYPT_E_ASN = 1

#
# MessageId: CERTSRV_E_BAD_REQUESTSUBJECT
#
# MessageText:
#
# The request subject name is invalid or too long.
#
CERTSRV_E_BAD_REQUESTSUBJECT = 0x80094001

#
# MessageId: CERTSRV_E_NO_REQUEST
#
# MessageText:
#
# The request does not exist.
#
CERTSRV_E_NO_REQUEST = 0x80094002

#
# MessageId: CERTSRV_E_BAD_REQUESTSTATUS
#
# MessageText:
#
# The request's current status does not allow this operation.
#
CERTSRV_E_BAD_REQUESTSTATUS = 0x80094003

#
# MessageId: CERTSRV_E_PROPERTY_EMPTY
#
# MessageText:
#
# The requested property value is empty.
#
CERTSRV_E_PROPERTY_EMPTY = 0x80094004

#
# MessageId: CERTSRV_E_INVALID_CA_CERTIFICATE
#
# MessageText:
#
# The certification authority's certificate contains invalid data.
#
CERTSRV_E_INVALID_CA_CERTIFICATE = 0x80094005

#
# MessageId: CERTSRV_E_SERVER_SUSPENDED
#
# MessageText:
#
# Certificate service has been suspended for a database restore operation.
#
CERTSRV_E_SERVER_SUSPENDED = 0x80094006

#
# MessageId: CERTSRV_E_ENCODING_LENGTH
#
# MessageText:
#
# The certificate contains an encoded length that is potentially incompatible with older enrollment software.
#
CERTSRV_E_ENCODING_LENGTH = 0x80094007

#
# MessageId: CERTSRV_E_ROLECONFLICT
#
# MessageText:
#
# The operation is denied. The user has multiple roles assigned and the certification authority is configured to enforce role separation.
#
CERTSRV_E_ROLECONFLICT = 0x80094008

#
# MessageId: CERTSRV_E_RESTRICTEDOFFICER
#
# MessageText:
#
# The operation is denied. It can only be performed by a certificate manager that is allowed to manage certificates for the current requester.
#
CERTSRV_E_RESTRICTEDOFFICER = 0x80094009

#
# MessageId: CERTSRV_E_KEY_ARCHIVAL_NOT_CONFIGURED
#
# MessageText:
#
# Cannot archive private key. The certification authority is not configured for key archival.
#
CERTSRV_E_KEY_ARCHIVAL_NOT_CONFIGURED = 0x8009400A

#
# MessageId: CERTSRV_E_NO_VALID_KRA
#
# MessageText:
#
# Cannot archive private key. The certification authority could not verify one or more key recovery certificates.
#
CERTSRV_E_NO_VALID_KRA = 0x8009400B

#
# MessageId: CERTSRV_E_BAD_REQUEST_KEY_ARCHIVAL
#
# MessageText:
#
# The request is incorrectly formatted. The encrypted private key must be in an unauthenticated attribute in an outermost signature.
#
CERTSRV_E_BAD_REQUEST_KEY_ARCHIVAL = 0x8009400C

#
# MessageId: CERTSRV_E_NO_CAADMIN_DEFINED
#
# MessageText:
#
# At least one security principal must have the permission to manage this CA.
#
CERTSRV_E_NO_CAADMIN_DEFINED = 0x8009400D

#
# MessageId: CERTSRV_E_BAD_RENEWAL_CERT_ATTRIBUTE
#
# MessageText:
#
# The request contains an invalid renewal certificate attribute.
#
CERTSRV_E_BAD_RENEWAL_CERT_ATTRIBUTE = 0x8009400E

#
# MessageId: CERTSRV_E_NO_DB_SESSIONS
#
# MessageText:
#
# An attempt was made to open a Certification Authority database session, but there are already too many active sessions. The server may need to be configured to allow additional sessions.
#
CERTSRV_E_NO_DB_SESSIONS = 0x8009400F

#
# MessageId: CERTSRV_E_ALIGNMENT_FAULT
#
# MessageText:
#
# A memory reference caused a data alignment fault.
#
CERTSRV_E_ALIGNMENT_FAULT = 0x80094010

#
# MessageId: CERTSRV_E_ENROLL_DENIED
#
# MessageText:
#
# The permissions on this certification authority do not allow the current user to enroll for certificates.
#
CERTSRV_E_ENROLL_DENIED = 0x80094011

#
# MessageId: CERTSRV_E_TEMPLATE_DENIED
#
# MessageText:
#
# The permissions on the certificate template do not allow the current user to enroll for this type of certificate.
#
CERTSRV_E_TEMPLATE_DENIED = 0x80094012

#
# MessageId: CERTSRV_E_DOWNLEVEL_DC_SSL_OR_UPGRADE
#
# MessageText:
#
# The contacted domain controller cannot support signed LDAP traffic. Update the domain controller or configure Certificate Services to use SSL for Active Directory access.
#
CERTSRV_E_DOWNLEVEL_DC_SSL_OR_UPGRADE = 0x80094013

#
# MessageId: CERTSRV_E_ADMIN_DENIED_REQUEST
#
# MessageText:
#
# The request was denied by a certificate manager or CA administrator.
#
CERTSRV_E_ADMIN_DENIED_REQUEST = 0x80094014

#
# MessageId: CERTSRV_E_NO_POLICY_SERVER
#
# MessageText:
#
# An enrollment policy server cannot be located.
#
CERTSRV_E_NO_POLICY_SERVER = 0x80094015

#
# MessageId: CERTSRV_E_WEAK_SIGNATURE_OR_KEY
#
# MessageText:
#
# A signature algorithm or public key length does not meet the system's minimum required strength.
#
CERTSRV_E_WEAK_SIGNATURE_OR_KEY = 0x80094016

#
# MessageId: CERTSRV_E_KEY_ATTESTATION_NOT_SUPPORTED
#
# MessageText:
#
# Failed to create an attested key.  This computer or the cryptographic provider may not meet the hardware requirements to support key attestation.
#
CERTSRV_E_KEY_ATTESTATION_NOT_SUPPORTED = 0x80094017

#
# MessageId: CERTSRV_E_ENCRYPTION_CERT_REQUIRED
#
# MessageText:
#
# No encryption certificate was specified.
#
CERTSRV_E_ENCRYPTION_CERT_REQUIRED = 0x80094018

#
# MessageId: CERTSRV_E_UNSUPPORTED_CERT_TYPE
#
# MessageText:
#
# The requested certificate template is not supported by this CA.
#
CERTSRV_E_UNSUPPORTED_CERT_TYPE = 0x80094800

#
# MessageId: CERTSRV_E_NO_CERT_TYPE
#
# MessageText:
#
# The request contains no certificate template information.
#
CERTSRV_E_NO_CERT_TYPE = 0x80094801

#
# MessageId: CERTSRV_E_TEMPLATE_CONFLICT
#
# MessageText:
#
# The request contains conflicting template information.
#
CERTSRV_E_TEMPLATE_CONFLICT = 0x80094802

#
# MessageId: CERTSRV_E_SUBJECT_ALT_NAME_REQUIRED
#
# MessageText:
#
# The request is missing a required Subject Alternate name extension.
#
CERTSRV_E_SUBJECT_ALT_NAME_REQUIRED = 0x80094803

#
# MessageId: CERTSRV_E_ARCHIVED_KEY_REQUIRED
#
# MessageText:
#
# The request is missing a required private key for archival by the server.
#
CERTSRV_E_ARCHIVED_KEY_REQUIRED = 0x80094804

#
# MessageId: CERTSRV_E_SMIME_REQUIRED
#
# MessageText:
#
# The request is missing a required SMIME capabilities extension.
#
CERTSRV_E_SMIME_REQUIRED = 0x80094805

#
# MessageId: CERTSRV_E_BAD_RENEWAL_SUBJECT
#
# MessageText:
#
# The request was made on behalf of a subject other than the caller. The certificate template must be configured to require at least one signature to authorize the request.
#
CERTSRV_E_BAD_RENEWAL_SUBJECT = 0x80094806

#
# MessageId: CERTSRV_E_BAD_TEMPLATE_VERSION
#
# MessageText:
#
# The request template version is newer than the supported template version.
#
CERTSRV_E_BAD_TEMPLATE_VERSION = 0x80094807

#
# MessageId: CERTSRV_E_TEMPLATE_POLICY_REQUIRED
#
# MessageText:
#
# The template is missing a required signature policy attribute.
#
CERTSRV_E_TEMPLATE_POLICY_REQUIRED = 0x80094808

#
# MessageId: CERTSRV_E_SIGNATURE_POLICY_REQUIRED
#
# MessageText:
#
# The request is missing required signature policy information.
#
CERTSRV_E_SIGNATURE_POLICY_REQUIRED = 0x80094809

#
# MessageId: CERTSRV_E_SIGNATURE_COUNT
#
# MessageText:
#
# The request is missing one or more required signatures.
#
CERTSRV_E_SIGNATURE_COUNT = 0x8009480A

#
# MessageId: CERTSRV_E_SIGNATURE_REJECTED
#
# MessageText:
#
# One or more signatures did not include the required application or issuance policies. The request is missing one or more required valid signatures.
#
CERTSRV_E_SIGNATURE_REJECTED = 0x8009480B

#
# MessageId: CERTSRV_E_ISSUANCE_POLICY_REQUIRED
#
# MessageText:
#
# The request is missing one or more required signature issuance policies.
#
CERTSRV_E_ISSUANCE_POLICY_REQUIRED = 0x8009480C

#
# MessageId: CERTSRV_E_SUBJECT_UPN_REQUIRED
#
# MessageText:
#
# The UPN is unavailable and cannot be added to the Subject Alternate name.
#
CERTSRV_E_SUBJECT_UPN_REQUIRED = 0x8009480D

#
# MessageId: CERTSRV_E_SUBJECT_DIRECTORY_GUID_REQUIRED
#
# MessageText:
#
# The Active Directory GUID is unavailable and cannot be added to the Subject Alternate name.
#
CERTSRV_E_SUBJECT_DIRECTORY_GUID_REQUIRED = 0x8009480E

#
# MessageId: CERTSRV_E_SUBJECT_DNS_REQUIRED
#
# MessageText:
#
# The DNS name is unavailable and cannot be added to the Subject Alternate name.
#
CERTSRV_E_SUBJECT_DNS_REQUIRED = 0x8009480F

#
# MessageId: CERTSRV_E_ARCHIVED_KEY_UNEXPECTED
#
# MessageText:
#
# The request includes a private key for archival by the server, but key archival is not enabled for the specified certificate template.
#
CERTSRV_E_ARCHIVED_KEY_UNEXPECTED = 0x80094810

#
# MessageId: CERTSRV_E_KEY_LENGTH
#
# MessageText:
#
# The public key does not meet the minimum size required by the specified certificate template.
#
CERTSRV_E_KEY_LENGTH = 0x80094811

#
# MessageId: CERTSRV_E_SUBJECT_EMAIL_REQUIRED
#
# MessageText:
#
# The EMail name is unavailable and cannot be added to the Subject or Subject Alternate name.
#
CERTSRV_E_SUBJECT_EMAIL_REQUIRED = 0x80094812

#
# MessageId: CERTSRV_E_UNKNOWN_CERT_TYPE
#
# MessageText:
#
# One or more certificate templates to be enabled on this certification authority could not be found.
#
CERTSRV_E_UNKNOWN_CERT_TYPE = 0x80094813

#
# MessageId: CERTSRV_E_CERT_TYPE_OVERLAP
#
# MessageText:
#
# The certificate template renewal period is longer than the certificate validity period. The template should be reconfigured or the CA certificate renewed.
#
CERTSRV_E_CERT_TYPE_OVERLAP = 0x80094814

#
# MessageId: CERTSRV_E_TOO_MANY_SIGNATURES
#
# MessageText:
#
# The certificate template requires too many RA signatures. Only one RA signature is allowed.
#
CERTSRV_E_TOO_MANY_SIGNATURES = 0x80094815

#
# MessageId: CERTSRV_E_RENEWAL_BAD_PUBLIC_KEY
#
# MessageText:
#
# The certificate template requires renewal with the same public key, but the request uses a different public key.
#
CERTSRV_E_RENEWAL_BAD_PUBLIC_KEY = 0x80094816

#
# MessageId: CERTSRV_E_INVALID_EK
#
# MessageText:
#
# The certification authority cannot interpret or verify the endorsement key information supplied in the request, or the information is inconsistent.
#
CERTSRV_E_INVALID_EK = 0x80094817

#
# MessageId: CERTSRV_E_INVALID_IDBINDING
#
# MessageText:
#
# The certification authority cannot validate the Attestation Identity Key Id Binding.
#
CERTSRV_E_INVALID_IDBINDING = 0x80094818

#
# MessageId: CERTSRV_E_INVALID_ATTESTATION
#
# MessageText:
#
# The certification authority cannot validate the private key attestation data.
#
CERTSRV_E_INVALID_ATTESTATION = 0x80094819

#
# MessageId: CERTSRV_E_KEY_ATTESTATION
#
# MessageText:
#
# The request does not support private key attestation as defined in the certificate template.
#
CERTSRV_E_KEY_ATTESTATION = 0x8009481A

#
# MessageId: CERTSRV_E_CORRUPT_KEY_ATTESTATION
#
# MessageText:
#
# The request public key is not consistent with the private key attestation data.
#
CERTSRV_E_CORRUPT_KEY_ATTESTATION = 0x8009481B

#
# MessageId: CERTSRV_E_EXPIRED_CHALLENGE
#
# MessageText:
#
# The private key attestation challenge cannot be validated because the encryption certificate has expired, or the certificate or key is unavailable.
#
CERTSRV_E_EXPIRED_CHALLENGE = 0x8009481C

#
# MessageId: CERTSRV_E_INVALID_RESPONSE
#
# MessageText:
#
# The attestation response could not be validated. It is either unexpected or incorrect.
#
CERTSRV_E_INVALID_RESPONSE = 0x8009481D

#
# MessageId: CERTSRV_E_INVALID_REQUESTID
#
# MessageText:
#
# A valid Request ID was not detected in the request attributes, or an invalid one was submitted.
#
CERTSRV_E_INVALID_REQUESTID = 0x8009481E

#
# The range 0x5000-0x51ff is reserved for XENROLL errors.
#
#
# MessageId: XENROLL_E_KEY_NOT_EXPORTABLE
#
# MessageText:
#
# The key is not exportable.
#
XENROLL_E_KEY_NOT_EXPORTABLE = 0x80095000

#
# MessageId: XENROLL_E_CANNOT_ADD_ROOT_CERT
#
# MessageText:
#
# You cannot add the root CA certificate into your local store.
#
XENROLL_E_CANNOT_ADD_ROOT_CERT = 0x80095001

#
# MessageId: XENROLL_E_RESPONSE_KA_HASH_NOT_FOUND
#
# MessageText:
#
# The key archival hash attribute was not found in the response.
#
XENROLL_E_RESPONSE_KA_HASH_NOT_FOUND = 0x80095002

#
# MessageId: XENROLL_E_RESPONSE_UNEXPECTED_KA_HASH
#
# MessageText:
#
# An unexpected key archival hash attribute was found in the response.
#
XENROLL_E_RESPONSE_UNEXPECTED_KA_HASH = 0x80095003

#
# MessageId: XENROLL_E_RESPONSE_KA_HASH_MISMATCH
#
# MessageText:
#
# There is a key archival hash mismatch between the request and the response.
#
XENROLL_E_RESPONSE_KA_HASH_MISMATCH = 0x80095004

#
# MessageId: XENROLL_E_KEYSPEC_SMIME_MISMATCH
#
# MessageText:
#
# Signing certificate cannot include SMIME extension.
#
XENROLL_E_KEYSPEC_SMIME_MISMATCH = 0x80095005

#
# MessageId: TRUST_E_SYSTEM_ERROR
#
# MessageText:
#
# A system-level error occurred while verifying trust.
#
TRUST_E_SYSTEM_ERROR = 0x80096001

#
# MessageId: TRUST_E_NO_SIGNER_CERT
#
# MessageText:
#
# The certificate for the signer of the message is invalid or not found.
#
TRUST_E_NO_SIGNER_CERT = 0x80096002

#
# MessageId: TRUST_E_COUNTER_SIGNER
#
# MessageText:
#
# One of the counter signatures was invalid.
#
TRUST_E_COUNTER_SIGNER = 0x80096003

#
# MessageId: TRUST_E_CERT_SIGNATURE
#
# MessageText:
#
# The signature of the certificate cannot be verified.
#
TRUST_E_CERT_SIGNATURE = 0x80096004

#
# MessageId: TRUST_E_TIME_STAMP
#
# MessageText:
#
# The timestamp signature and/or certificate could not be verified or is malformed.
#
TRUST_E_TIME_STAMP = 0x80096005

#
# MessageId: TRUST_E_BAD_DIGEST
#
# MessageText:
#
# The digital signature of the object did not verify.
#
TRUST_E_BAD_DIGEST = 0x80096010

#
# MessageId: TRUST_E_BASIC_CONSTRAINTS
#
# MessageText:
#
# A certificate's basic constraint extension has not been observed.
#
TRUST_E_BASIC_CONSTRAINTS = 0x80096019

#
# MessageId: TRUST_E_FINANCIAL_CRITERIA
#
# MessageText:
#
# The certificate does not meet or contain the Authenticode(tm) financial extensions.
#
TRUST_E_FINANCIAL_CRITERIA = 0x8009601E

#
# Error codes for mssipotf.dll
# Most of the error codes can only occur when an error occurs
#    during font file signing
#
#
#
# MessageId: MSSIPOTF_E_OUTOFMEMRANGE
#
# MessageText:
#
# Tried to reference a part of the file outside the proper range.
#
MSSIPOTF_E_OUTOFMEMRANGE = 0x80097001

#
# MessageId: MSSIPOTF_E_CANTGETOBJECT
#
# MessageText:
#
# Could not retrieve an object from the file.
#
MSSIPOTF_E_CANTGETOBJECT = 0x80097002

#
# MessageId: MSSIPOTF_E_NOHEADTABLE
#
# MessageText:
#
# Could not find the head table in the file.
#
MSSIPOTF_E_NOHEADTABLE = 0x80097003

#
# MessageId: MSSIPOTF_E_BAD_MAGICNUMBER
#
# MessageText:
#
# The magic number in the head table is incorrect.
#
MSSIPOTF_E_BAD_MAGICNUMBER = 0x80097004

#
# MessageId: MSSIPOTF_E_BAD_OFFSET_TABLE
#
# MessageText:
#
# The offset table has incorrect values.
#
MSSIPOTF_E_BAD_OFFSET_TABLE = 0x80097005

#
# MessageId: MSSIPOTF_E_TABLE_TAGORDER
#
# MessageText:
#
# Duplicate table tags or tags out of alphabetical order.
#
MSSIPOTF_E_TABLE_TAGORDER = 0x80097006

#
# MessageId: MSSIPOTF_E_TABLE_LONGWORD
#
# MessageText:
#
# A table does not start on a long word boundary.
#
MSSIPOTF_E_TABLE_LONGWORD = 0x80097007

#
# MessageId: MSSIPOTF_E_BAD_FIRST_TABLE_PLACEMENT
#
# MessageText:
#
# First table does not appear after header information.
#
MSSIPOTF_E_BAD_FIRST_TABLE_PLACEMENT = 0x80097008

#
# MessageId: MSSIPOTF_E_TABLES_OVERLAP
#
# MessageText:
#
# Two or more tables overlap.
#
MSSIPOTF_E_TABLES_OVERLAP = 0x80097009

#
# MessageId: MSSIPOTF_E_TABLE_PADBYTES
#
# MessageText:
#
# Too many pad bytes between tables or pad bytes are not 0.
#
MSSIPOTF_E_TABLE_PADBYTES = 0x8009700A

#
# MessageId: MSSIPOTF_E_FILETOOSMALL
#
# MessageText:
#
# File is too small to contain the last table.
#
MSSIPOTF_E_FILETOOSMALL = 0x8009700B

#
# MessageId: MSSIPOTF_E_TABLE_CHECKSUM
#
# MessageText:
#
# A table checksum is incorrect.
#
MSSIPOTF_E_TABLE_CHECKSUM = 0x8009700C

#
# MessageId: MSSIPOTF_E_FILE_CHECKSUM
#
# MessageText:
#
# The file checksum is incorrect.
#
MSSIPOTF_E_FILE_CHECKSUM = 0x8009700D

#
# MessageId: MSSIPOTF_E_FAILED_POLICY
#
# MessageText:
#
# The signature does not have the correct attributes for the policy.
#
MSSIPOTF_E_FAILED_POLICY = 0x80097010

#
# MessageId: MSSIPOTF_E_FAILED_HINTS_CHECK
#
# MessageText:
#
# The file did not pass the hints check.
#
MSSIPOTF_E_FAILED_HINTS_CHECK = 0x80097011

#
# MessageId: MSSIPOTF_E_NOT_OPENTYPE
#
# MessageText:
#
# The file is not an OpenType file.
#
MSSIPOTF_E_NOT_OPENTYPE = 0x80097012

#
# MessageId: MSSIPOTF_E_FILE
#
# MessageText:
#
# Failed on a file operation (open, map, read, write).
#
MSSIPOTF_E_FILE = 0x80097013

#
# MessageId: MSSIPOTF_E_CRYPT
#
# MessageText:
#
# A call to a CryptoAPI function failed.
#
MSSIPOTF_E_CRYPT = 0x80097014

#
# MessageId: MSSIPOTF_E_BADVERSION
#
# MessageText:
#
# There is a bad version number in the file.
#
MSSIPOTF_E_BADVERSION = 0x80097015

#
# MessageId: MSSIPOTF_E_DSIG_STRUCTURE
#
# MessageText:
#
# The structure of the DSIG table is incorrect.
#
MSSIPOTF_E_DSIG_STRUCTURE = 0x80097016

#
# MessageId: MSSIPOTF_E_PCONST_CHECK
#
# MessageText:
#
# A check failed in a partially constant table.
#
MSSIPOTF_E_PCONST_CHECK = 0x80097017

#
# MessageId: MSSIPOTF_E_STRUCTURE
#
# MessageText:
#
# Some kind of structural error.
#
MSSIPOTF_E_STRUCTURE = 0x80097018

#
# MessageId: ERROR_CRED_REQUIRES_CONFIRMATION
#
# MessageText:
#
# The requested credential requires confirmation.
#
ERROR_CRED_REQUIRES_CONFIRMATION = 0x80097019

NTE_OP_OK = 0

#
# Note that additional FACILITY_SSPI errors are in issperr.h
#
# ******************
# FACILITY_CERT
# ******************
#
# MessageId: TRUST_E_PROVIDER_UNKNOWN
#
# MessageText:
#
# Unknown trust provider.
#
TRUST_E_PROVIDER_UNKNOWN = 0x800B0001

#
# MessageId: TRUST_E_ACTION_UNKNOWN
#
# MessageText:
#
# The trust verification action specified is not supported by the specified trust provider.
#
TRUST_E_ACTION_UNKNOWN = 0x800B0002

#
# MessageId: TRUST_E_SUBJECT_FORM_UNKNOWN
#
# MessageText:
#
# The form specified for the subject is not one supported or known by the specified trust provider.
#
TRUST_E_SUBJECT_FORM_UNKNOWN = 0x800B0003

#
# MessageId: TRUST_E_SUBJECT_NOT_TRUSTED
#
# MessageText:
#
# The subject is not trusted for the specified action.
#
TRUST_E_SUBJECT_NOT_TRUSTED = 0x800B0004

#
# MessageId: DIGSIG_E_ENCODE
#
# MessageText:
#
# Error due to problem in ASN.1 encoding process.
#
DIGSIG_E_ENCODE = 0x800B0005

#
# MessageId: DIGSIG_E_DECODE
#
# MessageText:
#
# Error due to problem in ASN.1 decoding process.
#
DIGSIG_E_DECODE = 0x800B0006

#
# MessageId: DIGSIG_E_EXTENSIBILITY
#
# MessageText:
#
# Reading / writing Extensions where Attributes are appropriate, and vice versa.
#
DIGSIG_E_EXTENSIBILITY = 0x800B0007

#
# MessageId: DIGSIG_E_CRYPTO
#
# MessageText:
#
# Unspecified cryptographic failure.
#
DIGSIG_E_CRYPTO = 0x800B0008

#
# MessageId: PERSIST_E_SIZEDEFINITE
#
# MessageText:
#
# The size of the data could not be determined.
#
PERSIST_E_SIZEDEFINITE = 0x800B0009

#
# MessageId: PERSIST_E_SIZEINDEFINITE
#
# MessageText:
#
# The size of the indefinite-sized data could not be determined.
#
PERSIST_E_SIZEINDEFINITE = 0x800B000A

#
# MessageId: PERSIST_E_NOTSELFSIZING
#
# MessageText:
#
# This object does not read and write self-sizing data.
#
PERSIST_E_NOTSELFSIZING = 0x800B000B

#
# MessageId: TRUST_E_NOSIGNATURE
#
# MessageText:
#
# No signature was present in the subject.
#
TRUST_E_NOSIGNATURE = 0x800B0100

#
# MessageId: CERT_E_EXPIRED
#
# MessageText:
#
# A required certificate is not within its validity period when verifying against the current system clock or the timestamp in the signed file.
#
CERT_E_EXPIRED = 0x800B0101

#
# MessageId: CERT_E_VALIDITYPERIODNESTING
#
# MessageText:
#
# The validity periods of the certification chain do not nest correctly.
#
CERT_E_VALIDITYPERIODNESTING = 0x800B0102

#
# MessageId: CERT_E_ROLE
#
# MessageText:
#
# A certificate that can only be used as an end-entity is being used as a CA or vice versa.
#
CERT_E_ROLE = 0x800B0103

#
# MessageId: CERT_E_PATHLENCONST
#
# MessageText:
#
# A path length constraint in the certification chain has been violated.
#
CERT_E_PATHLENCONST = 0x800B0104

#
# MessageId: CERT_E_CRITICAL
#
# MessageText:
#
# A certificate contains an unknown extension that is marked 'critical'.
#
CERT_E_CRITICAL = 0x800B0105

#
# MessageId: CERT_E_PURPOSE
#
# MessageText:
#
# A certificate being used for a purpose other than the ones specified by its CA.
#
CERT_E_PURPOSE = 0x800B0106

#
# MessageId: CERT_E_ISSUERCHAINING
#
# MessageText:
#
# A parent of a given certificate in fact did not issue that child certificate.
#
CERT_E_ISSUERCHAINING = 0x800B0107

#
# MessageId: CERT_E_MALFORMED
#
# MessageText:
#
# A certificate is missing or has an empty value for an important field, such as a subject or issuer name.
#
CERT_E_MALFORMED = 0x800B0108

#
# MessageId: CERT_E_UNTRUSTEDROOT
#
# MessageText:
#
# A certificate chain processed, but terminated in a root certificate which is not trusted by the trust provider.
#
CERT_E_UNTRUSTEDROOT = 0x800B0109

#
# MessageId: CERT_E_CHAINING
#
# MessageText:
#
# A certificate chain could not be built to a trusted root authority.
#
CERT_E_CHAINING = 0x800B010A

#
# MessageId: TRUST_E_FAIL
#
# MessageText:
#
# Generic trust failure.
#
TRUST_E_FAIL = 0x800B010B

#
# MessageId: CERT_E_REVOKED
#
# MessageText:
#
# A certificate was explicitly revoked by its issuer.
#
CERT_E_REVOKED = 0x800B010C

#
# MessageId: CERT_E_UNTRUSTEDTESTROOT
#
# MessageText:
#
# The certification path terminates with the test root which is not trusted with the current policy settings.
#
CERT_E_UNTRUSTEDTESTROOT = 0x800B010D

#
# MessageId: CERT_E_REVOCATION_FAILURE
#
# MessageText:
#
# The revocation process could not continue - the certificate(s) could not be checked.
#
CERT_E_REVOCATION_FAILURE = 0x800B010E

#
# MessageId: CERT_E_CN_NO_MATCH
#
# MessageText:
#
# The certificate's CN name does not match the passed value.
#
CERT_E_CN_NO_MATCH = 0x800B010F

#
# MessageId: CERT_E_WRONG_USAGE
#
# MessageText:
#
# The certificate is not valid for the requested usage.
#
CERT_E_WRONG_USAGE = 0x800B0110

#
# MessageId: TRUST_E_EXPLICIT_DISTRUST
#
# MessageText:
#
# The certificate was explicitly marked as untrusted by the user.
#
TRUST_E_EXPLICIT_DISTRUST = 0x800B0111

#
# MessageId: CERT_E_UNTRUSTEDCA
#
# MessageText:
#
# A certification chain processed correctly, but one of the CA certificates is not trusted by the policy provider.
#
CERT_E_UNTRUSTEDCA = 0x800B0112

#
# MessageId: CERT_E_INVALID_POLICY
#
# MessageText:
#
# The certificate has invalid policy.
#
CERT_E_INVALID_POLICY = 0x800B0113

#
# MessageId: CERT_E_INVALID_NAME
#
# MessageText:
#
# The certificate has an invalid name. The name is not included in the permitted list or is explicitly excluded.
#
CERT_E_INVALID_NAME = 0x800B0114

# *****************
# FACILITY_MEDIASERVER
# *****************
#
# Also known as FACILITY_MF and FACILITY_NS
#
# The error codes are defined in mferror.mc, dlnaerror.mc, nserror.mc, and neterror.mc
#
# *****************
# FACILITY_SETUPAPI
# *****************
#
# Since these error codes aren't in the standard Win32 range (i.e., 0-64K), define a
# macro to map either Win32 or SetupAPI error codes into an HRESULT.
#
#define HRESULT_FROM_SETUPAPI(x) ((((x) & (APPLICATION_ERROR_MASK|ERROR_SEVERITY_ERROR)) == (APPLICATION_ERROR_MASK|ERROR_SEVERITY_ERROR)) \
                                 # ? ((HRESULT) (((x) & 0x0000FFFF) | (FACILITY_SETUPAPI << 16) | 0x80000000))                               \
                                 # : HRESULT_FROM_WIN32(x))
#
# MessageId: SPAPI_E_EXPECTED_SECTION_NAME
#
# MessageText:
#
# A non-empty line was encountered in the INF before the start of a section.
#
SPAPI_E_EXPECTED_SECTION_NAME = 0x800F0000

#
# MessageId: SPAPI_E_BAD_SECTION_NAME_LINE
#
# MessageText:
#
# A section name marker in the INF is not complete, or does not exist on a line by itself.
#
SPAPI_E_BAD_SECTION_NAME_LINE = 0x800F0001

#
# MessageId: SPAPI_E_SECTION_NAME_TOO_LONG
#
# MessageText:
#
# An INF section was encountered whose name exceeds the maximum section name length.
#
SPAPI_E_SECTION_NAME_TOO_LONG = 0x800F0002

#
# MessageId: SPAPI_E_GENERAL_SYNTAX
#
# MessageText:
#
# The syntax of the INF is invalid.
#
SPAPI_E_GENERAL_SYNTAX = 0x800F0003

#
# MessageId: SPAPI_E_WRONG_INF_STYLE
#
# MessageText:
#
# The style of the INF is different than what was requested.
#
SPAPI_E_WRONG_INF_STYLE = 0x800F0100

#
# MessageId: SPAPI_E_SECTION_NOT_FOUND
#
# MessageText:
#
# The required section was not found in the INF.
#
SPAPI_E_SECTION_NOT_FOUND = 0x800F0101

#
# MessageId: SPAPI_E_LINE_NOT_FOUND
#
# MessageText:
#
# The required line was not found in the INF.
#
SPAPI_E_LINE_NOT_FOUND = 0x800F0102

#
# MessageId: SPAPI_E_NO_BACKUP
#
# MessageText:
#
# The files affected by the installation of this file queue have not been backed up for uninstall.
#
SPAPI_E_NO_BACKUP = 0x800F0103

#
# MessageId: SPAPI_E_NO_ASSOCIATED_CLASS
#
# MessageText:
#
# The INF or the device information set or element does not have an associated install class.
#
SPAPI_E_NO_ASSOCIATED_CLASS = 0x800F0200

#
# MessageId: SPAPI_E_CLASS_MISMATCH
#
# MessageText:
#
# The INF or the device information set or element does not match the specified install class.
#
SPAPI_E_CLASS_MISMATCH = 0x800F0201

#
# MessageId: SPAPI_E_DUPLICATE_FOUND
#
# MessageText:
#
# An existing device was found that is a duplicate of the device being manually installed.
#
SPAPI_E_DUPLICATE_FOUND = 0x800F0202

#
# MessageId: SPAPI_E_NO_DRIVER_SELECTED
#
# MessageText:
#
# There is no driver selected for the device information set or element.
#
SPAPI_E_NO_DRIVER_SELECTED = 0x800F0203

#
# MessageId: SPAPI_E_KEY_DOES_NOT_EXIST
#
# MessageText:
#
# The requested device registry key does not exist.
#
SPAPI_E_KEY_DOES_NOT_EXIST = 0x800F0204

#
# MessageId: SPAPI_E_INVALID_DEVINST_NAME
#
# MessageText:
#
# The device instance name is invalid.
#
SPAPI_E_INVALID_DEVINST_NAME = 0x800F0205

#
# MessageId: SPAPI_E_INVALID_CLASS
#
# MessageText:
#
# The install class is not present or is invalid.
#
SPAPI_E_INVALID_CLASS = 0x800F0206

#
# MessageId: SPAPI_E_DEVINST_ALREADY_EXISTS
#
# MessageText:
#
# The device instance cannot be created because it already exists.
#
SPAPI_E_DEVINST_ALREADY_EXISTS = 0x800F0207

#
# MessageId: SPAPI_E_DEVINFO_NOT_REGISTERED
#
# MessageText:
#
# The operation cannot be performed on a device information element that has not been registered.
#
SPAPI_E_DEVINFO_NOT_REGISTERED = 0x800F0208

#
# MessageId: SPAPI_E_INVALID_REG_PROPERTY
#
# MessageText:
#
# The device property code is invalid.
#
SPAPI_E_INVALID_REG_PROPERTY = 0x800F0209

#
# MessageId: SPAPI_E_NO_INF
#
# MessageText:
#
# The INF from which a driver list is to be built does not exist.
#
SPAPI_E_NO_INF = 0x800F020A

#
# MessageId: SPAPI_E_NO_SUCH_DEVINST
#
# MessageText:
#
# The device instance does not exist in the hardware tree.
#
SPAPI_E_NO_SUCH_DEVINST = 0x800F020B

#
# MessageId: SPAPI_E_CANT_LOAD_CLASS_ICON
#
# MessageText:
#
# The icon representing this install class cannot be loaded.
#
SPAPI_E_CANT_LOAD_CLASS_ICON = 0x800F020C

#
# MessageId: SPAPI_E_INVALID_CLASS_INSTALLER
#
# MessageText:
#
# The class installer registry entry is invalid.
#
SPAPI_E_INVALID_CLASS_INSTALLER = 0x800F020D

#
# MessageId: SPAPI_E_DI_DO_DEFAULT
#
# MessageText:
#
# The class installer has indicated that the default action should be performed for this installation request.
#
SPAPI_E_DI_DO_DEFAULT = 0x800F020E

#
# MessageId: SPAPI_E_DI_NOFILECOPY
#
# MessageText:
#
# The operation does not require any files to be copied.
#
SPAPI_E_DI_NOFILECOPY = 0x800F020F

#
# MessageId: SPAPI_E_INVALID_HWPROFILE
#
# MessageText:
#
# The specified hardware profile does not exist.
#
SPAPI_E_INVALID_HWPROFILE = 0x800F0210

#
# MessageId: SPAPI_E_NO_DEVICE_SELECTED
#
# MessageText:
#
# There is no device information element currently selected for this device information set.
#
SPAPI_E_NO_DEVICE_SELECTED = 0x800F0211

#
# MessageId: SPAPI_E_DEVINFO_LIST_LOCKED
#
# MessageText:
#
# The operation cannot be performed because the device information set is locked.
#
SPAPI_E_DEVINFO_LIST_LOCKED = 0x800F0212

#
# MessageId: SPAPI_E_DEVINFO_DATA_LOCKED
#
# MessageText:
#
# The operation cannot be performed because the device information element is locked.
#
SPAPI_E_DEVINFO_DATA_LOCKED = 0x800F0213

#
# MessageId: SPAPI_E_DI_BAD_PATH
#
# MessageText:
#
# The specified path does not contain any applicable device INFs.
#
SPAPI_E_DI_BAD_PATH = 0x800F0214

#
# MessageId: SPAPI_E_NO_CLASSINSTALL_PARAMS
#
# MessageText:
#
# No class installer parameters have been set for the device information set or element.
#
SPAPI_E_NO_CLASSINSTALL_PARAMS = 0x800F0215

#
# MessageId: SPAPI_E_FILEQUEUE_LOCKED
#
# MessageText:
#
# The operation cannot be performed because the file queue is locked.
#
SPAPI_E_FILEQUEUE_LOCKED = 0x800F0216

#
# MessageId: SPAPI_E_BAD_SERVICE_INSTALLSECT
#
# MessageText:
#
# A service installation section in this INF is invalid.
#
SPAPI_E_BAD_SERVICE_INSTALLSECT = 0x800F0217

#
# MessageId: SPAPI_E_NO_CLASS_DRIVER_LIST
#
# MessageText:
#
# There is no class driver list for the device information element.
#
SPAPI_E_NO_CLASS_DRIVER_LIST = 0x800F0218

#
# MessageId: SPAPI_E_NO_ASSOCIATED_SERVICE
#
# MessageText:
#
# The installation failed because a function driver was not specified for this device instance.
#
SPAPI_E_NO_ASSOCIATED_SERVICE = 0x800F0219

#
# MessageId: SPAPI_E_NO_DEFAULT_DEVICE_INTERFACE
#
# MessageText:
#
# There is presently no default device interface designated for this interface class.
#
SPAPI_E_NO_DEFAULT_DEVICE_INTERFACE = 0x800F021A

#
# MessageId: SPAPI_E_DEVICE_INTERFACE_ACTIVE
#
# MessageText:
#
# The operation cannot be performed because the device interface is currently active.
#
SPAPI_E_DEVICE_INTERFACE_ACTIVE = 0x800F021B

#
# MessageId: SPAPI_E_DEVICE_INTERFACE_REMOVED
#
# MessageText:
#
# The operation cannot be performed because the device interface has been removed from the system.
#
SPAPI_E_DEVICE_INTERFACE_REMOVED = 0x800F021C

#
# MessageId: SPAPI_E_BAD_INTERFACE_INSTALLSECT
#
# MessageText:
#
# An interface installation section in this INF is invalid.
#
SPAPI_E_BAD_INTERFACE_INSTALLSECT = 0x800F021D

#
# MessageId: SPAPI_E_NO_SUCH_INTERFACE_CLASS
#
# MessageText:
#
# This interface class does not exist in the system.
#
SPAPI_E_NO_SUCH_INTERFACE_CLASS = 0x800F021E

#
# MessageId: SPAPI_E_INVALID_REFERENCE_STRING
#
# MessageText:
#
# The reference string supplied for this interface device is invalid.
#
SPAPI_E_INVALID_REFERENCE_STRING = 0x800F021F

#
# MessageId: SPAPI_E_INVALID_MACHINENAME
#
# MessageText:
#
# The specified machine name does not conform to UNC naming conventions.
#
SPAPI_E_INVALID_MACHINENAME = 0x800F0220

#
# MessageId: SPAPI_E_REMOTE_COMM_FAILURE
#
# MessageText:
#
# A general remote communication error occurred.
#
SPAPI_E_REMOTE_COMM_FAILURE = 0x800F0221

#
# MessageId: SPAPI_E_MACHINE_UNAVAILABLE
#
# MessageText:
#
# The machine selected for remote communication is not available at this time.
#
SPAPI_E_MACHINE_UNAVAILABLE = 0x800F0222

#
# MessageId: SPAPI_E_NO_CONFIGMGR_SERVICES
#
# MessageText:
#
# The Plug and Play service is not available on the remote machine.
#
SPAPI_E_NO_CONFIGMGR_SERVICES = 0x800F0223

#
# MessageId: SPAPI_E_INVALID_PROPPAGE_PROVIDER
#
# MessageText:
#
# The property page provider registry entry is invalid.
#
SPAPI_E_INVALID_PROPPAGE_PROVIDER = 0x800F0224

#
# MessageId: SPAPI_E_NO_SUCH_DEVICE_INTERFACE
#
# MessageText:
#
# The requested device interface is not present in the system.
#
SPAPI_E_NO_SUCH_DEVICE_INTERFACE = 0x800F0225

#
# MessageId: SPAPI_E_DI_POSTPROCESSING_REQUIRED
#
# MessageText:
#
# The device's co-installer has additional work to perform after installation is complete.
#
SPAPI_E_DI_POSTPROCESSING_REQUIRED = 0x800F0226

#
# MessageId: SPAPI_E_INVALID_COINSTALLER
#
# MessageText:
#
# The device's co-installer is invalid.
#
SPAPI_E_INVALID_COINSTALLER = 0x800F0227

#
# MessageId: SPAPI_E_NO_COMPAT_DRIVERS
#
# MessageText:
#
# There are no compatible drivers for this device.
#
SPAPI_E_NO_COMPAT_DRIVERS = 0x800F0228

#
# MessageId: SPAPI_E_NO_DEVICE_ICON
#
# MessageText:
#
# There is no icon that represents this device or device type.
#
SPAPI_E_NO_DEVICE_ICON = 0x800F0229

#
# MessageId: SPAPI_E_INVALID_INF_LOGCONFIG
#
# MessageText:
#
# A logical configuration specified in this INF is invalid.
#
SPAPI_E_INVALID_INF_LOGCONFIG = 0x800F022A

#
# MessageId: SPAPI_E_DI_DONT_INSTALL
#
# MessageText:
#
# The class installer has denied the request to install or upgrade this device.
#
SPAPI_E_DI_DONT_INSTALL = 0x800F022B

#
# MessageId: SPAPI_E_INVALID_FILTER_DRIVER
#
# MessageText:
#
# One of the filter drivers installed for this device is invalid.
#
SPAPI_E_INVALID_FILTER_DRIVER = 0x800F022C

#
# MessageId: SPAPI_E_NON_WINDOWS_NT_DRIVER
#
# MessageText:
#
# The driver selected for this device does not support this version of Windows.
#
SPAPI_E_NON_WINDOWS_NT_DRIVER = 0x800F022D

#
# MessageId: SPAPI_E_NON_WINDOWS_DRIVER
#
# MessageText:
#
# The driver selected for this device does not support Windows.
#
SPAPI_E_NON_WINDOWS_DRIVER = 0x800F022E

#
# MessageId: SPAPI_E_NO_CATALOG_FOR_OEM_INF
#
# MessageText:
#
# The third-party INF does not contain digital signature information.
#
SPAPI_E_NO_CATALOG_FOR_OEM_INF = 0x800F022F

#
# MessageId: SPAPI_E_DEVINSTALL_QUEUE_NONNATIVE
#
# MessageText:
#
# An invalid attempt was made to use a device installation file queue for verification of digital signatures relative to other platforms.
#
SPAPI_E_DEVINSTALL_QUEUE_NONNATIVE = 0x800F0230

#
# MessageId: SPAPI_E_NOT_DISABLEABLE
#
# MessageText:
#
# The device cannot be disabled.
#
SPAPI_E_NOT_DISABLEABLE = 0x800F0231

#
# MessageId: SPAPI_E_CANT_REMOVE_DEVINST
#
# MessageText:
#
# The device could not be dynamically removed.
#
SPAPI_E_CANT_REMOVE_DEVINST = 0x800F0232

#
# MessageId: SPAPI_E_INVALID_TARGET
#
# MessageText:
#
# Cannot copy to specified target.
#
SPAPI_E_INVALID_TARGET = 0x800F0233

#
# MessageId: SPAPI_E_DRIVER_NONNATIVE
#
# MessageText:
#
# Driver is not intended for this platform.
#
SPAPI_E_DRIVER_NONNATIVE = 0x800F0234

#
# MessageId: SPAPI_E_IN_WOW64
#
# MessageText:
#
# Operation not allowed in WOW64.
#
SPAPI_E_IN_WOW6 = 4

#
# MessageId: SPAPI_E_SET_SYSTEM_RESTORE_POINT
#
# MessageText:
#
# The operation involving unsigned file copying was rolled back, so that a system restore point could be set.
#
SPAPI_E_SET_SYSTEM_RESTORE_POINT = 0x800F0236

#
# MessageId: SPAPI_E_INCORRECTLY_COPIED_INF
#
# MessageText:
#
# An INF was copied into the Windows INF directory in an improper manner.
#
SPAPI_E_INCORRECTLY_COPIED_INF = 0x800F0237

#
# MessageId: SPAPI_E_SCE_DISABLED
#
# MessageText:
#
# The Security Configuration Editor (SCE) APIs have been disabled on this Embedded product.
#
SPAPI_E_SCE_DISABLED = 0x800F0238

#
# MessageId: SPAPI_E_UNKNOWN_EXCEPTION
#
# MessageText:
#
# An unknown exception was encountered.
#
SPAPI_E_UNKNOWN_EXCEPTION = 0x800F0239

#
# MessageId: SPAPI_E_PNP_REGISTRY_ERROR
#
# MessageText:
#
# A problem was encountered when accessing the Plug and Play registry database.
#
SPAPI_E_PNP_REGISTRY_ERROR = 0x800F023A

#
# MessageId: SPAPI_E_REMOTE_REQUEST_UNSUPPORTED
#
# MessageText:
#
# The requested operation is not supported for a remote machine.
#
SPAPI_E_REMOTE_REQUEST_UNSUPPORTED = 0x800F023B

#
# MessageId: SPAPI_E_NOT_AN_INSTALLED_OEM_INF
#
# MessageText:
#
# The specified file is not an installed OEM INF.
#
SPAPI_E_NOT_AN_INSTALLED_OEM_INF = 0x800F023C

#
# MessageId: SPAPI_E_INF_IN_USE_BY_DEVICES
#
# MessageText:
#
# One or more devices are presently installed using the specified INF.
#
SPAPI_E_INF_IN_USE_BY_DEVICES = 0x800F023D

#
# MessageId: SPAPI_E_DI_FUNCTION_OBSOLETE
#
# MessageText:
#
# The requested device install operation is obsolete.
#
SPAPI_E_DI_FUNCTION_OBSOLETE = 0x800F023E

#
# MessageId: SPAPI_E_NO_AUTHENTICODE_CATALOG
#
# MessageText:
#
# A file could not be verified because it does not have an associated catalog signed via Authenticode(tm).
#
SPAPI_E_NO_AUTHENTICODE_CATALOG = 0x800F023F

#
# MessageId: SPAPI_E_AUTHENTICODE_DISALLOWED
#
# MessageText:
#
# Authenticode(tm) signature verification is not supported for the specified INF.
#
SPAPI_E_AUTHENTICODE_DISALLOWED = 0x800F0240

#
# MessageId: SPAPI_E_AUTHENTICODE_TRUSTED_PUBLISHER
#
# MessageText:
#
# The INF was signed with an Authenticode(tm) catalog from a trusted publisher.
#
SPAPI_E_AUTHENTICODE_TRUSTED_PUBLISHER = 0x800F0241

#
# MessageId: SPAPI_E_AUTHENTICODE_TRUST_NOT_ESTABLISHED
#
# MessageText:
#
# The publisher of an Authenticode(tm) signed catalog has not yet been established as trusted.
#
SPAPI_E_AUTHENTICODE_TRUST_NOT_ESTABLISHED = 0x800F0242

#
# MessageId: SPAPI_E_AUTHENTICODE_PUBLISHER_NOT_TRUSTED
#
# MessageText:
#
# The publisher of an Authenticode(tm) signed catalog was not established as trusted.
#
SPAPI_E_AUTHENTICODE_PUBLISHER_NOT_TRUSTED = 0x800F0243

#
# MessageId: SPAPI_E_SIGNATURE_OSATTRIBUTE_MISMATCH
#
# MessageText:
#
# The software was tested for compliance with Windows Logo requirements on a different version of Windows, and may not be compatible with this version.
#
SPAPI_E_SIGNATURE_OSATTRIBUTE_MISMATCH = 0x800F0244

#
# MessageId: SPAPI_E_ONLY_VALIDATE_VIA_AUTHENTICODE
#
# MessageText:
#
# The file may only be validated by a catalog signed via Authenticode(tm).
#
SPAPI_E_ONLY_VALIDATE_VIA_AUTHENTICODE = 0x800F0245

#
# MessageId: SPAPI_E_DEVICE_INSTALLER_NOT_READY
#
# MessageText:
#
# One of the installers for this device cannot perform the installation at this time.
#
SPAPI_E_DEVICE_INSTALLER_NOT_READY = 0x800F0246

#
# MessageId: SPAPI_E_DRIVER_STORE_ADD_FAILED
#
# MessageText:
#
# A problem was encountered while attempting to add the driver to the store.
#
SPAPI_E_DRIVER_STORE_ADD_FAILED = 0x800F0247

#
# MessageId: SPAPI_E_DEVICE_INSTALL_BLOCKED
#
# MessageText:
#
# The installation of this device is forbidden by system policy. Contact your system administrator.
#
SPAPI_E_DEVICE_INSTALL_BLOCKED = 0x800F0248

#
# MessageId: SPAPI_E_DRIVER_INSTALL_BLOCKED
#
# MessageText:
#
# The installation of this driver is forbidden by system policy. Contact your system administrator.
#
SPAPI_E_DRIVER_INSTALL_BLOCKED = 0x800F0249

#
# MessageId: SPAPI_E_WRONG_INF_TYPE
#
# MessageText:
#
# The specified INF is the wrong type for this operation.
#
SPAPI_E_WRONG_INF_TYPE = 0x800F024A

#
# MessageId: SPAPI_E_FILE_HASH_NOT_IN_CATALOG
#
# MessageText:
#
# The hash for the file is not present in the specified catalog file. The file is likely corrupt or the victim of tampering.
#
SPAPI_E_FILE_HASH_NOT_IN_CATALOG = 0x800F024B

#
# MessageId: SPAPI_E_DRIVER_STORE_DELETE_FAILED
#
# MessageText:
#
# A problem was encountered while attempting to delete the driver from the store.
#
SPAPI_E_DRIVER_STORE_DELETE_FAILED = 0x800F024C

#
# MessageId: SPAPI_E_UNRECOVERABLE_STACK_OVERFLOW
#
# MessageText:
#
# An unrecoverable stack overflow was encountered.
#
SPAPI_E_UNRECOVERABLE_STACK_OVERFLOW = 0x800F0300

#
# MessageId: SPAPI_E_ERROR_NOT_INSTALLED
#
# MessageText:
#
# No installed components were detected.
#
SPAPI_E_ERROR_NOT_INSTALLED = 0x800F1000

# *****************
# FACILITY_SCARD
# *****************
#
# =============================
# Facility SCARD Error Messages
# =============================
#
SCARD_S_SUCCESS = NO_ERROR
#
# MessageId: SCARD_F_INTERNAL_ERROR
#
# MessageText:
#
# An internal consistency check failed.
#
SCARD_F_INTERNAL_ERROR = 0x80100001

#
# MessageId: SCARD_E_CANCELLED
#
# MessageText:
#
# The action was cancelled by an SCardCancel request.
#
SCARD_E_CANCELLED = 0x80100002

#
# MessageId: SCARD_E_INVALID_HANDLE
#
# MessageText:
#
# The supplied handle was invalid.
#
SCARD_E_INVALID_HANDLE = 0x80100003

#
# MessageId: SCARD_E_INVALID_PARAMETER
#
# MessageText:
#
# One or more of the supplied parameters could not be properly interpreted.
#
SCARD_E_INVALID_PARAMETER = 0x80100004

#
# MessageId: SCARD_E_INVALID_TARGET
#
# MessageText:
#
# Registry startup information is missing or invalid.
#
SCARD_E_INVALID_TARGET = 0x80100005

#
# MessageId: SCARD_E_NO_MEMORY
#
# MessageText:
#
# Not enough memory available to complete this command.
#
SCARD_E_NO_MEMORY = 0x80100006

#
# MessageId: SCARD_F_WAITED_TOO_LONG
#
# MessageText:
#
# An internal consistency timer has expired.
#
SCARD_F_WAITED_TOO_LONG = 0x80100007

#
# MessageId: SCARD_E_INSUFFICIENT_BUFFER
#
# MessageText:
#
# The data buffer to receive returned data is too small for the returned data.
#
SCARD_E_INSUFFICIENT_BUFFER = 0x80100008

#
# MessageId: SCARD_E_UNKNOWN_READER
#
# MessageText:
#
# The specified reader name is not recognized.
#
SCARD_E_UNKNOWN_READER = 0x80100009

#
# MessageId: SCARD_E_TIMEOUT
#
# MessageText:
#
# The user-specified timeout value has expired.
#
SCARD_E_TIMEOUT = 0x8010000A

#
# MessageId: SCARD_E_SHARING_VIOLATION
#
# MessageText:
#
# The smart card cannot be accessed because of other connections outstanding.
#
SCARD_E_SHARING_VIOLATION = 0x8010000B

#
# MessageId: SCARD_E_NO_SMARTCARD
#
# MessageText:
#
# The operation requires a smart card, but no smart card is currently in the device.
#
SCARD_E_NO_SMARTCARD = 0x8010000C

#
# MessageId: SCARD_E_UNKNOWN_CARD
#
# MessageText:
#
# The specified smart card name is not recognized.
#
SCARD_E_UNKNOWN_CARD = 0x8010000D

#
# MessageId: SCARD_E_CANT_DISPOSE
#
# MessageText:
#
# The system could not dispose of the media in the requested manner.
#
SCARD_E_CANT_DISPOSE = 0x8010000E

#
# MessageId: SCARD_E_PROTO_MISMATCH
#
# MessageText:
#
# The requested protocols are incompatible with the protocol currently in use with the smart card.
#
SCARD_E_PROTO_MISMATCH = 0x8010000F

#
# MessageId: SCARD_E_NOT_READY
#
# MessageText:
#
# The reader or smart card is not ready to accept commands.
#
SCARD_E_NOT_READY = 0x80100010

#
# MessageId: SCARD_E_INVALID_VALUE
#
# MessageText:
#
# One or more of the supplied parameters values could not be properly interpreted.
#
SCARD_E_INVALID_VALUE = 0x80100011

#
# MessageId: SCARD_E_SYSTEM_CANCELLED
#
# MessageText:
#
# The action was cancelled by the system, presumably to log off or shut down.
#
SCARD_E_SYSTEM_CANCELLED = 0x80100012

#
# MessageId: SCARD_F_COMM_ERROR
#
# MessageText:
#
# An internal communications error has been detected.
#
SCARD_F_COMM_ERROR = 0x80100013

#
# MessageId: SCARD_F_UNKNOWN_ERROR
#
# MessageText:
#
# An internal error has been detected, but the source is unknown.
#
SCARD_F_UNKNOWN_ERROR = 0x80100014

#
# MessageId: SCARD_E_INVALID_ATR
#
# MessageText:
#
# An ATR obtained from the registry is not a valid ATR string.
#
SCARD_E_INVALID_ATR = 0x80100015

#
# MessageId: SCARD_E_NOT_TRANSACTED
#
# MessageText:
#
# An attempt was made to end a non-existent transaction.
#
SCARD_E_NOT_TRANSACTED = 0x80100016

#
# MessageId: SCARD_E_READER_UNAVAILABLE
#
# MessageText:
#
# The specified reader is not currently available for use.
#
SCARD_E_READER_UNAVAILABLE = 0x80100017

#
# MessageId: SCARD_P_SHUTDOWN
#
# MessageText:
#
# The operation has been aborted to allow the server application to exit.
#
SCARD_P_SHUTDOWN = 0x80100018

#
# MessageId: SCARD_E_PCI_TOO_SMALL
#
# MessageText:
#
# The PCI Receive buffer was too small.
#
SCARD_E_PCI_TOO_SMALL = 0x80100019

#
# MessageId: SCARD_E_READER_UNSUPPORTED
#
# MessageText:
#
# The reader driver does not meet minimal requirements for support.
#
SCARD_E_READER_UNSUPPORTED = 0x8010001A

#
# MessageId: SCARD_E_DUPLICATE_READER
#
# MessageText:
#
# The reader driver did not produce a unique reader name.
#
SCARD_E_DUPLICATE_READER = 0x8010001B

#
# MessageId: SCARD_E_CARD_UNSUPPORTED
#
# MessageText:
#
# The smart card does not meet minimal requirements for support.
#
SCARD_E_CARD_UNSUPPORTED = 0x8010001C

#
# MessageId: SCARD_E_NO_SERVICE
#
# MessageText:
#
# The Smart Card Resource Manager is not running.
#
SCARD_E_NO_SERVICE = 0x8010001D

#
# MessageId: SCARD_E_SERVICE_STOPPED
#
# MessageText:
#
# The Smart Card Resource Manager has shut down.
#
SCARD_E_SERVICE_STOPPED = 0x8010001E

#
# MessageId: SCARD_E_UNEXPECTED
#
# MessageText:
#
# An unexpected card error has occurred.
#
SCARD_E_UNEXPECTED = 0x8010001F

#
# MessageId: SCARD_E_ICC_INSTALLATION
#
# MessageText:
#
# No Primary Provider can be found for the smart card.
#
SCARD_E_ICC_INSTALLATION = 0x80100020

#
# MessageId: SCARD_E_ICC_CREATEORDER
#
# MessageText:
#
# The requested order of object creation is not supported.
#
SCARD_E_ICC_CREATEORDER = 0x80100021

#
# MessageId: SCARD_E_UNSUPPORTED_FEATURE
#
# MessageText:
#
# This smart card does not support the requested feature.
#
SCARD_E_UNSUPPORTED_FEATURE = 0x80100022

#
# MessageId: SCARD_E_DIR_NOT_FOUND
#
# MessageText:
#
# The identified directory does not exist in the smart card.
#
SCARD_E_DIR_NOT_FOUND = 0x80100023

#
# MessageId: SCARD_E_FILE_NOT_FOUND
#
# MessageText:
#
# The identified file does not exist in the smart card.
#
SCARD_E_FILE_NOT_FOUND = 0x80100024

#
# MessageId: SCARD_E_NO_DIR
#
# MessageText:
#
# The supplied path does not represent a smart card directory.
#
SCARD_E_NO_DIR = 0x80100025

#
# MessageId: SCARD_E_NO_FILE
#
# MessageText:
#
# The supplied path does not represent a smart card file.
#
SCARD_E_NO_FILE = 0x80100026

#
# MessageId: SCARD_E_NO_ACCESS
#
# MessageText:
#
# Access is denied to this file.
#
SCARD_E_NO_ACCESS = 0x80100027

#
# MessageId: SCARD_E_WRITE_TOO_MANY
#
# MessageText:
#
# The smart card does not have enough memory to store the information.
#
SCARD_E_WRITE_TOO_MANY = 0x80100028

#
# MessageId: SCARD_E_BAD_SEEK
#
# MessageText:
#
# There was an error trying to set the smart card file object pointer.
#
SCARD_E_BAD_SEEK = 0x80100029

#
# MessageId: SCARD_E_INVALID_CHV
#
# MessageText:
#
# The supplied PIN is incorrect.
#
SCARD_E_INVALID_CHV = 0x8010002A

#
# MessageId: SCARD_E_UNKNOWN_RES_MNG
#
# MessageText:
#
# An unrecognized error code was returned from a layered component.
#
SCARD_E_UNKNOWN_RES_MNG = 0x8010002B

#
# MessageId: SCARD_E_NO_SUCH_CERTIFICATE
#
# MessageText:
#
# The requested certificate does not exist.
#
SCARD_E_NO_SUCH_CERTIFICATE = 0x8010002C

#
# MessageId: SCARD_E_CERTIFICATE_UNAVAILABLE
#
# MessageText:
#
# The requested certificate could not be obtained.
#
SCARD_E_CERTIFICATE_UNAVAILABLE = 0x8010002D

#
# MessageId: SCARD_E_NO_READERS_AVAILABLE
#
# MessageText:
#
# Cannot find a smart card reader.
#
SCARD_E_NO_READERS_AVAILABLE = 0x8010002E

#
# MessageId: SCARD_E_COMM_DATA_LOST
#
# MessageText:
#
# A communications error with the smart card has been detected. Retry the operation.
#
SCARD_E_COMM_DATA_LOST = 0x8010002F

#
# MessageId: SCARD_E_NO_KEY_CONTAINER
#
# MessageText:
#
# The requested key container does not exist on the smart card.
#
SCARD_E_NO_KEY_CONTAINER = 0x80100030

#
# MessageId: SCARD_E_SERVER_TOO_BUSY
#
# MessageText:
#
# The Smart Card Resource Manager is too busy to complete this operation.
#
SCARD_E_SERVER_TOO_BUSY = 0x80100031

#
# MessageId: SCARD_E_PIN_CACHE_EXPIRED
#
# MessageText:
#
# The smart card PIN cache has expired.
#
SCARD_E_PIN_CACHE_EXPIRED = 0x80100032

#
# MessageId: SCARD_E_NO_PIN_CACHE
#
# MessageText:
#
# The smart card PIN cannot be cached.
#
SCARD_E_NO_PIN_CACHE = 0x80100033

#
# MessageId: SCARD_E_READ_ONLY_CARD
#
# MessageText:
#
# The smart card is read only and cannot be written to.
#
SCARD_E_READ_ONLY_CARD = 0x80100034

#
# These are warning codes.
#
#
# MessageId: SCARD_W_UNSUPPORTED_CARD
#
# MessageText:
#
# The reader cannot communicate with the smart card, due to ATR configuration conflicts.
#
SCARD_W_UNSUPPORTED_CARD = 0x80100065

#
# MessageId: SCARD_W_UNRESPONSIVE_CARD
#
# MessageText:
#
# The smart card is not responding to a reset.
#
SCARD_W_UNRESPONSIVE_CARD = 0x80100066

#
# MessageId: SCARD_W_UNPOWERED_CARD
#
# MessageText:
#
# Power has been removed from the smart card, so that further communication is not possible.
#
SCARD_W_UNPOWERED_CARD = 0x80100067

#
# MessageId: SCARD_W_RESET_CARD
#
# MessageText:
#
# The smart card has been reset, so any shared state information is invalid.
#
SCARD_W_RESET_CARD = 0x80100068

#
# MessageId: SCARD_W_REMOVED_CARD
#
# MessageText:
#
# The smart card has been removed, so that further communication is not possible.
#
SCARD_W_REMOVED_CARD = 0x80100069

#
# MessageId: SCARD_W_SECURITY_VIOLATION
#
# MessageText:
#
# Access was denied because of a security violation.
#
SCARD_W_SECURITY_VIOLATION = 0x8010006A

#
# MessageId: SCARD_W_WRONG_CHV
#
# MessageText:
#
# The card cannot be accessed because the wrong PIN was presented.
#
SCARD_W_WRONG_CHV = 0x8010006B

#
# MessageId: SCARD_W_CHV_BLOCKED
#
# MessageText:
#
# The card cannot be accessed because the maximum number of PIN entry attempts has been reached.
#
SCARD_W_CHV_BLOCKED = 0x8010006C

#
# MessageId: SCARD_W_EOF
#
# MessageText:
#
# The end of the smart card file has been reached.
#
SCARD_W_EOF = 0x8010006D

#
# MessageId: SCARD_W_CANCELLED_BY_USER
#
# MessageText:
#
# The action was cancelled by the user.
#
SCARD_W_CANCELLED_BY_USER = 0x8010006E

#
# MessageId: SCARD_W_CARD_NOT_AUTHENTICATED
#
# MessageText:
#
# No PIN was presented to the smart card.
#
SCARD_W_CARD_NOT_AUTHENTICATED = 0x8010006F

#
# MessageId: SCARD_W_CACHE_ITEM_NOT_FOUND
#
# MessageText:
#
# The requested item could not be found in the cache.
#
SCARD_W_CACHE_ITEM_NOT_FOUND = 0x80100070

#
# MessageId: SCARD_W_CACHE_ITEM_STALE
#
# MessageText:
#
# The requested cache item is too old and was deleted from the cache.
#
SCARD_W_CACHE_ITEM_STALE = 0x80100071

#
# MessageId: SCARD_W_CACHE_ITEM_TOO_BIG
#
# MessageText:
#
# The new cache item exceeds the maximum per-item size defined for the cache.
#
SCARD_W_CACHE_ITEM_TOO_BIG = 0x80100072

# *****************
# FACILITY_COMPLUS
# *****************
#
# ===============================
# Facility COMPLUS Error Messages
# ===============================
#
#
# The following are the subranges  within the COMPLUS facility
# 0x400 - 0x4ff               COMADMIN_E_CAT
# 0x600 - 0x6ff               COMQC errors
# 0x700 - 0x7ff               MSDTC errors
# 0x800 - 0x8ff               Other COMADMIN errors
#
# COMPLUS Admin errors
#
#
# MessageId: COMADMIN_E_OBJECTERRORS
#
# MessageText:
#
# Errors occurred accessing one or more objects - the ErrorInfo collection may have more detail
#
COMADMIN_E_OBJECTERRORS = 0x80110401

#
# MessageId: COMADMIN_E_OBJECTINVALID
#
# MessageText:
#
# One or more of the object's properties are missing or invalid
#
COMADMIN_E_OBJECTINVALID = 0x80110402

#
# MessageId: COMADMIN_E_KEYMISSING
#
# MessageText:
#
# The object was not found in the catalog
#
COMADMIN_E_KEYMISSING = 0x80110403

#
# MessageId: COMADMIN_E_ALREADYINSTALLED
#
# MessageText:
#
# The object is already registered
#
COMADMIN_E_ALREADYINSTALLED = 0x80110404

#
# MessageId: COMADMIN_E_APP_FILE_WRITEFAIL
#
# MessageText:
#
# Error occurred writing to the application file
#
COMADMIN_E_APP_FILE_WRITEFAIL = 0x80110407

#
# MessageId: COMADMIN_E_APP_FILE_READFAIL
#
# MessageText:
#
# Error occurred reading the application file
#
COMADMIN_E_APP_FILE_READFAIL = 0x80110408

#
# MessageId: COMADMIN_E_APP_FILE_VERSION
#
# MessageText:
#
# Invalid version number in application file
#
COMADMIN_E_APP_FILE_VERSION = 0x80110409

#
# MessageId: COMADMIN_E_BADPATH
#
# MessageText:
#
# The file path is invalid
#
COMADMIN_E_BADPATH = 0x8011040A

#
# MessageId: COMADMIN_E_APPLICATIONEXISTS
#
# MessageText:
#
# The application is already installed
#
COMADMIN_E_APPLICATIONEXISTS = 0x8011040B

#
# MessageId: COMADMIN_E_ROLEEXISTS
#
# MessageText:
#
# The role already exists
#
COMADMIN_E_ROLEEXISTS = 0x8011040C

#
# MessageId: COMADMIN_E_CANTCOPYFILE
#
# MessageText:
#
# An error occurred copying the file
#
COMADMIN_E_CANTCOPYFILE = 0x8011040D

#
# MessageId: COMADMIN_E_NOUSER
#
# MessageText:
#
# One or more users are not valid
#
COMADMIN_E_NOUSER = 0x8011040F

#
# MessageId: COMADMIN_E_INVALIDUSERIDS
#
# MessageText:
#
# One or more users in the application file are not valid
#
COMADMIN_E_INVALIDUSERIDS = 0x80110410

#
# MessageId: COMADMIN_E_NOREGISTRYCLSID
#
# MessageText:
#
# The component's CLSID is missing or corrupt
#
COMADMIN_E_NOREGISTRYCLSID = 0x80110411

#
# MessageId: COMADMIN_E_BADREGISTRYPROGID
#
# MessageText:
#
# The component's progID is missing or corrupt
#
COMADMIN_E_BADREGISTRYPROGID = 0x80110412

#
# MessageId: COMADMIN_E_AUTHENTICATIONLEVEL
#
# MessageText:
#
# Unable to set required authentication level for update request
#
COMADMIN_E_AUTHENTICATIONLEVEL = 0x80110413

#
# MessageId: COMADMIN_E_USERPASSWDNOTVALID
#
# MessageText:
#
# The identity or password set on the application is not valid
#
COMADMIN_E_USERPASSWDNOTVALID = 0x80110414

#
# MessageId: COMADMIN_E_CLSIDORIIDMISMATCH
#
# MessageText:
#
# Application file CLSIDs or IIDs do not match corresponding DLLs
#
COMADMIN_E_CLSIDORIIDMISMATCH = 0x80110418

#
# MessageId: COMADMIN_E_REMOTEINTERFACE
#
# MessageText:
#
# Interface information is either missing or changed
#
COMADMIN_E_REMOTEINTERFACE = 0x80110419

#
# MessageId: COMADMIN_E_DLLREGISTERSERVER
#
# MessageText:
#
# DllRegisterServer failed on component install
#
COMADMIN_E_DLLREGISTERSERVER = 0x8011041A

#
# MessageId: COMADMIN_E_NOSERVERSHARE
#
# MessageText:
#
# No server file share available
#
COMADMIN_E_NOSERVERSHARE = 0x8011041B

#
# MessageId: COMADMIN_E_DLLLOADFAILED
#
# MessageText:
#
# DLL could not be loaded
#
COMADMIN_E_DLLLOADFAILED = 0x8011041D

#
# MessageId: COMADMIN_E_BADREGISTRYLIBID
#
# MessageText:
#
# The registered TypeLib ID is not valid
#
COMADMIN_E_BADREGISTRYLIBID = 0x8011041E

#
# MessageId: COMADMIN_E_APPDIRNOTFOUND
#
# MessageText:
#
# Application install directory not found
#
COMADMIN_E_APPDIRNOTFOUND = 0x8011041F

#
# MessageId: COMADMIN_E_REGISTRARFAILED
#
# MessageText:
#
# Errors occurred while in the component registrar
#
COMADMIN_E_REGISTRARFAILED = 0x80110423

#
# MessageId: COMADMIN_E_COMPFILE_DOESNOTEXIST
#
# MessageText:
#
# The file does not exist
#
COMADMIN_E_COMPFILE_DOESNOTEXIST = 0x80110424

#
# MessageId: COMADMIN_E_COMPFILE_LOADDLLFAIL
#
# MessageText:
#
# The DLL could not be loaded
#
COMADMIN_E_COMPFILE_LOADDLLFAIL = 0x80110425

#
# MessageId: COMADMIN_E_COMPFILE_GETCLASSOBJ
#
# MessageText:
#
# GetClassObject failed in the DLL
#
COMADMIN_E_COMPFILE_GETCLASSOBJ = 0x80110426

#
# MessageId: COMADMIN_E_COMPFILE_CLASSNOTAVAIL
#
# MessageText:
#
# The DLL does not support the components listed in the TypeLib
#
COMADMIN_E_COMPFILE_CLASSNOTAVAIL = 0x80110427

#
# MessageId: COMADMIN_E_COMPFILE_BADTLB
#
# MessageText:
#
# The TypeLib could not be loaded
#
COMADMIN_E_COMPFILE_BADTLB = 0x80110428

#
# MessageId: COMADMIN_E_COMPFILE_NOTINSTALLABLE
#
# MessageText:
#
# The file does not contain components or component information
#
COMADMIN_E_COMPFILE_NOTINSTALLABLE = 0x80110429

#
# MessageId: COMADMIN_E_NOTCHANGEABLE
#
# MessageText:
#
# Changes to this object and its sub-objects have been disabled
#
COMADMIN_E_NOTCHANGEABLE = 0x8011042A

#
# MessageId: COMADMIN_E_NOTDELETEABLE
#
# MessageText:
#
# The delete function has been disabled for this object
#
COMADMIN_E_NOTDELETEABLE = 0x8011042B

#
# MessageId: COMADMIN_E_SESSION
#
# MessageText:
#
# The server catalog version is not supported
#
COMADMIN_E_SESSION = 0x8011042C

#
# MessageId: COMADMIN_E_COMP_MOVE_LOCKED
#
# MessageText:
#
# The component move was disallowed, because the source or destination application is either a system application or currently locked against changes
#
COMADMIN_E_COMP_MOVE_LOCKED = 0x8011042D

#
# MessageId: COMADMIN_E_COMP_MOVE_BAD_DEST
#
# MessageText:
#
# The component move failed because the destination application no longer exists
#
COMADMIN_E_COMP_MOVE_BAD_DEST = 0x8011042E

#
# MessageId: COMADMIN_E_REGISTERTLB
#
# MessageText:
#
# The system was unable to register the TypeLib
#
COMADMIN_E_REGISTERTLB = 0x80110430

#
# MessageId: COMADMIN_E_SYSTEMAPP
#
# MessageText:
#
# This operation cannot be performed on the system application
#
COMADMIN_E_SYSTEMAPP = 0x80110433

#
# MessageId: COMADMIN_E_COMPFILE_NOREGISTRAR
#
# MessageText:
#
# The component registrar referenced in this file is not available
#
COMADMIN_E_COMPFILE_NOREGISTRAR = 0x80110434

#
# MessageId: COMADMIN_E_COREQCOMPINSTALLED
#
# MessageText:
#
# A component in the same DLL is already installed
#
COMADMIN_E_COREQCOMPINSTALLED = 0x80110435

#
# MessageId: COMADMIN_E_SERVICENOTINSTALLED
#
# MessageText:
#
# The service is not installed
#
COMADMIN_E_SERVICENOTINSTALLED = 0x80110436

#
# MessageId: COMADMIN_E_PROPERTYSAVEFAILED
#
# MessageText:
#
# One or more property settings are either invalid or in conflict with each other
#
COMADMIN_E_PROPERTYSAVEFAILED = 0x80110437

#
# MessageId: COMADMIN_E_OBJECTEXISTS
#
# MessageText:
#
# The object you are attempting to add or rename already exists
#
COMADMIN_E_OBJECTEXISTS = 0x80110438

#
# MessageId: COMADMIN_E_COMPONENTEXISTS
#
# MessageText:
#
# The component already exists
#
COMADMIN_E_COMPONENTEXISTS = 0x80110439

#
# MessageId: COMADMIN_E_REGFILE_CORRUPT
#
# MessageText:
#
# The registration file is corrupt
#
COMADMIN_E_REGFILE_CORRUPT = 0x8011043B

#
# MessageId: COMADMIN_E_PROPERTY_OVERFLOW
#
# MessageText:
#
# The property value is too large
#
COMADMIN_E_PROPERTY_OVERFLOW = 0x8011043C

#
# MessageId: COMADMIN_E_NOTINREGISTRY
#
# MessageText:
#
# Object was not found in registry
#
COMADMIN_E_NOTINREGISTRY = 0x8011043E

#
# MessageId: COMADMIN_E_OBJECTNOTPOOLABLE
#
# MessageText:
#
# This object is not poolable
#
COMADMIN_E_OBJECTNOTPOOLABLE = 0x8011043F

#
# MessageId: COMADMIN_E_APPLID_MATCHES_CLSID
#
# MessageText:
#
# A CLSID with the same GUID as the new application ID is already installed on this machine
#
COMADMIN_E_APPLID_MATCHES_CLSID = 0x80110446

#
# MessageId: COMADMIN_E_ROLE_DOES_NOT_EXIST
#
# MessageText:
#
# A role assigned to a component, interface, or method did not exist in the application
#
COMADMIN_E_ROLE_DOES_NOT_EXIST = 0x80110447

#
# MessageId: COMADMIN_E_START_APP_NEEDS_COMPONENTS
#
# MessageText:
#
# You must have components in an application in order to start the application
#
COMADMIN_E_START_APP_NEEDS_COMPONENTS = 0x80110448

#
# MessageId: COMADMIN_E_REQUIRES_DIFFERENT_PLATFORM
#
# MessageText:
#
# This operation is not enabled on this platform
#
COMADMIN_E_REQUIRES_DIFFERENT_PLATFORM = 0x80110449

#
# MessageId: COMADMIN_E_CAN_NOT_EXPORT_APP_PROXY
#
# MessageText:
#
# Application Proxy is not exportable
#
COMADMIN_E_CAN_NOT_EXPORT_APP_PROXY = 0x8011044A

#
# MessageId: COMADMIN_E_CAN_NOT_START_APP
#
# MessageText:
#
# Failed to start application because it is either a library application or an application proxy
#
COMADMIN_E_CAN_NOT_START_APP = 0x8011044B

#
# MessageId: COMADMIN_E_CAN_NOT_EXPORT_SYS_APP
#
# MessageText:
#
# System application is not exportable
#
COMADMIN_E_CAN_NOT_EXPORT_SYS_APP = 0x8011044C

#
# MessageId: COMADMIN_E_CANT_SUBSCRIBE_TO_COMPONENT
#
# MessageText:
#
# Cannot subscribe to this component (the component may have been imported)
#
COMADMIN_E_CANT_SUBSCRIBE_TO_COMPONENT = 0x8011044D

#
# MessageId: COMADMIN_E_EVENTCLASS_CANT_BE_SUBSCRIBER
#
# MessageText:
#
# An event class cannot also be a subscriber component
#
COMADMIN_E_EVENTCLASS_CANT_BE_SUBSCRIBER = 0x8011044E

#
# MessageId: COMADMIN_E_LIB_APP_PROXY_INCOMPATIBLE
#
# MessageText:
#
# Library applications and application proxies are incompatible
#
COMADMIN_E_LIB_APP_PROXY_INCOMPATIBLE = 0x8011044F

#
# MessageId: COMADMIN_E_BASE_PARTITION_ONLY
#
# MessageText:
#
# This function is valid for the base partition only
#
COMADMIN_E_BASE_PARTITION_ONLY = 0x80110450

#
# MessageId: COMADMIN_E_START_APP_DISABLED
#
# MessageText:
#
# You cannot start an application that has been disabled
#
COMADMIN_E_START_APP_DISABLED = 0x80110451

#
# MessageId: COMADMIN_E_CAT_DUPLICATE_PARTITION_NAME
#
# MessageText:
#
# The specified partition name is already in use on this computer
#
COMADMIN_E_CAT_DUPLICATE_PARTITION_NAME = 0x80110457

#
# MessageId: COMADMIN_E_CAT_INVALID_PARTITION_NAME
#
# MessageText:
#
# The specified partition name is invalid. Check that the name contains at least one visible character
#
COMADMIN_E_CAT_INVALID_PARTITION_NAME = 0x80110458

#
# MessageId: COMADMIN_E_CAT_PARTITION_IN_USE
#
# MessageText:
#
# The partition cannot be deleted because it is the default partition for one or more users
#
COMADMIN_E_CAT_PARTITION_IN_USE = 0x80110459

#
# MessageId: COMADMIN_E_FILE_PARTITION_DUPLICATE_FILES
#
# MessageText:
#
# The partition cannot be exported, because one or more components in the partition have the same file name
#
COMADMIN_E_FILE_PARTITION_DUPLICATE_FILES = 0x8011045A

#
# MessageId: COMADMIN_E_CAT_IMPORTED_COMPONENTS_NOT_ALLOWED
#
# MessageText:
#
# Applications that contain one or more imported components cannot be installed into a non-base partition
#
COMADMIN_E_CAT_IMPORTED_COMPONENTS_NOT_ALLOWED = 0x8011045B

#
# MessageId: COMADMIN_E_AMBIGUOUS_APPLICATION_NAME
#
# MessageText:
#
# The application name is not unique and cannot be resolved to an application id
#
COMADMIN_E_AMBIGUOUS_APPLICATION_NAME = 0x8011045C

#
# MessageId: COMADMIN_E_AMBIGUOUS_PARTITION_NAME
#
# MessageText:
#
# The partition name is not unique and cannot be resolved to a partition id
#
COMADMIN_E_AMBIGUOUS_PARTITION_NAME = 0x8011045D

#
# MessageId: COMADMIN_E_REGDB_NOTINITIALIZED
#
# MessageText:
#
# The COM+ registry database has not been initialized
#
COMADMIN_E_REGDB_NOTINITIALIZED = 0x80110472

#
# MessageId: COMADMIN_E_REGDB_NOTOPEN
#
# MessageText:
#
# The COM+ registry database is not open
#
COMADMIN_E_REGDB_NOTOPEN = 0x80110473

#
# MessageId: COMADMIN_E_REGDB_SYSTEMERR
#
# MessageText:
#
# The COM+ registry database detected a system error
#
COMADMIN_E_REGDB_SYSTEMERR = 0x80110474

#
# MessageId: COMADMIN_E_REGDB_ALREADYRUNNING
#
# MessageText:
#
# The COM+ registry database is already running
#
COMADMIN_E_REGDB_ALREADYRUNNING = 0x80110475

#
# MessageId: COMADMIN_E_MIG_VERSIONNOTSUPPORTED
#
# MessageText:
#
# This version of the COM+ registry database cannot be migrated
#
COMADMIN_E_MIG_VERSIONNOTSUPPORTED = 0x80110480

#
# MessageId: COMADMIN_E_MIG_SCHEMANOTFOUND
#
# MessageText:
#
# The schema version to be migrated could not be found in the COM+ registry database
#
COMADMIN_E_MIG_SCHEMANOTFOUND = 0x80110481

#
# MessageId: COMADMIN_E_CAT_BITNESSMISMATCH
#
# MessageText:
#
# There was a type mismatch between binaries
#
COMADMIN_E_CAT_BITNESSMISMATCH = 0x80110482

#
# MessageId: COMADMIN_E_CAT_UNACCEPTABLEBITNESS
#
# MessageText:
#
# A binary of unknown or invalid type was provided
#
COMADMIN_E_CAT_UNACCEPTABLEBITNESS = 0x80110483

#
# MessageId: COMADMIN_E_CAT_WRONGAPPBITNESS
#
# MessageText:
#
# There was a type mismatch between a binary and an application
#
COMADMIN_E_CAT_WRONGAPPBITNESS = 0x80110484

#
# MessageId: COMADMIN_E_CAT_PAUSE_RESUME_NOT_SUPPORTED
#
# MessageText:
#
# The application cannot be paused or resumed
#
COMADMIN_E_CAT_PAUSE_RESUME_NOT_SUPPORTED = 0x80110485

#
# MessageId: COMADMIN_E_CAT_SERVERFAULT
#
# MessageText:
#
# The COM+ Catalog Server threw an exception during execution
#
COMADMIN_E_CAT_SERVERFAULT = 0x80110486

#
# COMPLUS Queued component errors
#
#
# MessageId: COMQC_E_APPLICATION_NOT_QUEUED
#
# MessageText:
#
# Only COM+ Applications marked "queued" can be invoked using the "queue" moniker
#
COMQC_E_APPLICATION_NOT_QUEUED = 0x80110600

#
# MessageId: COMQC_E_NO_QUEUEABLE_INTERFACES
#
# MessageText:
#
# At least one interface must be marked "queued" in order to create a queued component instance with the "queue" moniker
#
COMQC_E_NO_QUEUEABLE_INTERFACES = 0x80110601

#
# MessageId: COMQC_E_QUEUING_SERVICE_NOT_AVAILABLE
#
# MessageText:
#
# MSMQ is required for the requested operation and is not installed
#
COMQC_E_QUEUING_SERVICE_NOT_AVAILABLE = 0x80110602

#
# MessageId: COMQC_E_NO_IPERSISTSTREAM
#
# MessageText:
#
# Unable to marshal an interface that does not support IPersistStream
#
COMQC_E_NO_IPERSISTSTREAM = 0x80110603

#
# MessageId: COMQC_E_BAD_MESSAGE
#
# MessageText:
#
# The message is improperly formatted or was damaged in transit
#
COMQC_E_BAD_MESSAGE = 0x80110604

#
# MessageId: COMQC_E_UNAUTHENTICATED
#
# MessageText:
#
# An unauthenticated message was received by an application that accepts only authenticated messages
#
COMQC_E_UNAUTHENTICATED = 0x80110605

#
# MessageId: COMQC_E_UNTRUSTED_ENQUEUER
#
# MessageText:
#
# The message was requeued or moved by a user not in the "QC Trusted User" role
#
COMQC_E_UNTRUSTED_ENQUEUER = 0x80110606

#
# The range 0x700-0x7ff is reserved for MSDTC errors.
#
#
# MessageId: MSDTC_E_DUPLICATE_RESOURCE
#
# MessageText:
#
# Cannot create a duplicate resource of type Distributed Transaction Coordinator
#
MSDTC_E_DUPLICATE_RESOURCE = 0x80110701

#
# More COMADMIN errors from 0x8**
#
#
# MessageId: COMADMIN_E_OBJECT_PARENT_MISSING
#
# MessageText:
#
# One of the objects being inserted or updated does not belong to a valid parent collection
#
COMADMIN_E_OBJECT_PARENT_MISSING = 0x80110808

#
# MessageId: COMADMIN_E_OBJECT_DOES_NOT_EXIST
#
# MessageText:
#
# One of the specified objects cannot be found
#
COMADMIN_E_OBJECT_DOES_NOT_EXIST = 0x80110809

#
# MessageId: COMADMIN_E_APP_NOT_RUNNING
#
# MessageText:
#
# The specified application is not currently running
#
COMADMIN_E_APP_NOT_RUNNING = 0x8011080A

#
# MessageId: COMADMIN_E_INVALID_PARTITION
#
# MessageText:
#
# The partition(s) specified are not valid.
#
COMADMIN_E_INVALID_PARTITION = 0x8011080B

#
# MessageId: COMADMIN_E_SVCAPP_NOT_POOLABLE_OR_RECYCLABLE
#
# MessageText:
#
# COM+ applications that run as NT service may not be pooled or recycled
#
COMADMIN_E_SVCAPP_NOT_POOLABLE_OR_RECYCLABLE = 0x8011080D

#
# MessageId: COMADMIN_E_USER_IN_SET
#
# MessageText:
#
# One or more users are already assigned to a local partition set.
#
COMADMIN_E_USER_IN_SET = 0x8011080E

#
# MessageId: COMADMIN_E_CANTRECYCLELIBRARYAPPS
#
# MessageText:
#
# Library applications may not be recycled.
#
COMADMIN_E_CANTRECYCLELIBRARYAPPS = 0x8011080F

#
# MessageId: COMADMIN_E_CANTRECYCLESERVICEAPPS
#
# MessageText:
#
# Applications running as NT services may not be recycled.
#
COMADMIN_E_CANTRECYCLESERVICEAPPS = 0x80110811

#
# MessageId: COMADMIN_E_PROCESSALREADYRECYCLED
#
# MessageText:
#
# The process has already been recycled.
#
COMADMIN_E_PROCESSALREADYRECYCLED = 0x80110812

#
# MessageId: COMADMIN_E_PAUSEDPROCESSMAYNOTBERECYCLED
#
# MessageText:
#
# A paused process may not be recycled.
#
COMADMIN_E_PAUSEDPROCESSMAYNOTBERECYCLED = 0x80110813

#
# MessageId: COMADMIN_E_CANTMAKEINPROCSERVICE
#
# MessageText:
#
# Library applications may not be NT services.
#
COMADMIN_E_CANTMAKEINPROCSERVICE = 0x80110814

#
# MessageId: COMADMIN_E_PROGIDINUSEBYCLSID
#
# MessageText:
#
# The ProgID provided to the copy operation is invalid. The ProgID is in use by another registered CLSID.
#
COMADMIN_E_PROGIDINUSEBYCLSID = 0x80110815

#
# MessageId: COMADMIN_E_DEFAULT_PARTITION_NOT_IN_SET
#
# MessageText:
#
# The partition specified as default is not a member of the partition set.
#
COMADMIN_E_DEFAULT_PARTITION_NOT_IN_SET = 0x80110816

#
# MessageId: COMADMIN_E_RECYCLEDPROCESSMAYNOTBEPAUSED
#
# MessageText:
#
# A recycled process may not be paused.
#
COMADMIN_E_RECYCLEDPROCESSMAYNOTBEPAUSED = 0x80110817

#
# MessageId: COMADMIN_E_PARTITION_ACCESSDENIED
#
# MessageText:
#
# Access to the specified partition is denied.
#
COMADMIN_E_PARTITION_ACCESSDENIED = 0x80110818

#
# MessageId: COMADMIN_E_PARTITION_MSI_ONLY
#
# MessageText:
#
# Only Application Files (*.MSI files) can be installed into partitions.
#
COMADMIN_E_PARTITION_MSI_ONLY = 0x80110819

#
# MessageId: COMADMIN_E_LEGACYCOMPS_NOT_ALLOWED_IN_1_0_FORMAT
#
# MessageText:
#
# Applications containing one or more legacy components may not be exported to 1.0 format.
#
COMADMIN_E_LEGACYCOMPS_NOT_ALLOWED_IN_1_ = 0

#
# MessageId: COMADMIN_E_LEGACYCOMPS_NOT_ALLOWED_IN_NONBASE_PARTITIONS
#
# MessageText:
#
# Legacy components may not exist in non-base partitions.
#
COMADMIN_E_LEGACYCOMPS_NOT_ALLOWED_IN_NONBASE_PARTITIONS = 0x8011081B

#
# MessageId: COMADMIN_E_COMP_MOVE_SOURCE
#
# MessageText:
#
# A component cannot be moved (or copied) from the System Application, an application proxy or a non-changeable application
#
COMADMIN_E_COMP_MOVE_SOURCE = 0x8011081C

#
# MessageId: COMADMIN_E_COMP_MOVE_DEST
#
# MessageText:
#
# A component cannot be moved (or copied) to the System Application, an application proxy or a non-changeable application
#
COMADMIN_E_COMP_MOVE_DEST = 0x8011081D

#
# MessageId: COMADMIN_E_COMP_MOVE_PRIVATE
#
# MessageText:
#
# A private component cannot be moved (or copied) to a library application or to the base partition
#
COMADMIN_E_COMP_MOVE_PRIVATE = 0x8011081E

#
# MessageId: COMADMIN_E_BASEPARTITION_REQUIRED_IN_SET
#
# MessageText:
#
# The Base Application Partition exists in all partition sets and cannot be removed.
#
COMADMIN_E_BASEPARTITION_REQUIRED_IN_SET = 0x8011081F

#
# MessageId: COMADMIN_E_CANNOT_ALIAS_EVENTCLASS
#
# MessageText:
#
# Alas, Event Class components cannot be aliased.
#
COMADMIN_E_CANNOT_ALIAS_EVENTCLASS = 0x80110820

#
# MessageId: COMADMIN_E_PRIVATE_ACCESSDENIED
#
# MessageText:
#
# Access is denied because the component is private.
#
COMADMIN_E_PRIVATE_ACCESSDENIED = 0x80110821

#
# MessageId: COMADMIN_E_SAFERINVALID
#
# MessageText:
#
# The specified SAFER level is invalid.
#
COMADMIN_E_SAFERINVALID = 0x80110822

#
# MessageId: COMADMIN_E_REGISTRY_ACCESSDENIED
#
# MessageText:
#
# The specified user cannot write to the system registry
#
COMADMIN_E_REGISTRY_ACCESSDENIED = 0x80110823

#
# MessageId: COMADMIN_E_PARTITIONS_DISABLED
#
# MessageText:
#
# COM+ partitions are currently disabled.
#
COMADMIN_E_PARTITIONS_DISABLED = 0x80110824

#
# FACILITY_WER
#
#
# MessageId: WER_S_REPORT_DEBUG
#
# MessageText:
#
# Debugger was attached.
#
WER_S_REPORT_DEBUG = 0x001B0000

#
# MessageId: WER_S_REPORT_UPLOADED
#
# MessageText:
#
# Report was uploaded.
#
WER_S_REPORT_UPLOADED = 0x001B0001

#
# MessageId: WER_S_REPORT_QUEUED
#
# MessageText:
#
# Report was queued.
#
WER_S_REPORT_QUEUED = 0x001B0002

#
# MessageId: WER_S_DISABLED
#
# MessageText:
#
# Reporting was disabled.
#
WER_S_DISABLED = 0x001B0003

#
# MessageId: WER_S_SUSPENDED_UPLOAD
#
# MessageText:
#
# Reporting was temporarily suspended.
#
WER_S_SUSPENDED_UPLOAD = 0x001B0004

#
# MessageId: WER_S_DISABLED_QUEUE
#
# MessageText:
#
# Report was not queued to queueing being disabled.
#
WER_S_DISABLED_QUEUE = 0x001B0005

#
# MessageId: WER_S_DISABLED_ARCHIVE
#
# MessageText:
#
# Report was uploaded, but not archived due to archiving being disabled.
#
WER_S_DISABLED_ARCHIVE = 0x001B0006

#
# MessageId: WER_S_REPORT_ASYNC
#
# MessageText:
#
# Reporting was successfully spun off as an asynchronous operation.
#
WER_S_REPORT_ASYNC = 0x001B0007

#
# MessageId: WER_S_IGNORE_ASSERT_INSTANCE
#
# MessageText:
#
# The assertion was handled.
#
WER_S_IGNORE_ASSERT_INSTANCE = 0x001B0008

#
# MessageId: WER_S_IGNORE_ALL_ASSERTS
#
# MessageText:
#
# The assertion was handled and added to a permanent ignore list.
#
WER_S_IGNORE_ALL_ASSERTS = 0x001B0009

#
# MessageId: WER_S_ASSERT_CONTINUE
#
# MessageText:
#
# The assertion was resumed as unhandled.
#
WER_S_ASSERT_CONTINUE = 0x001B000A

#
# MessageId: WER_S_THROTTLED
#
# MessageText:
#
# Report was throttled.
#
WER_S_THROTTLED = 0x001B000B

#
# MessageId: WER_E_CRASH_FAILURE
#
# MessageText:
#
# Crash reporting failed.
#
WER_E_CRASH_FAILURE = 0x801B8000

#
# MessageId: WER_E_CANCELED
#
# MessageText:
#
# Report aborted due to user cancelation.
#
WER_E_CANCELED = 0x801B8001

#
# MessageId: WER_E_NETWORK_FAILURE
#
# MessageText:
#
# Report aborted due to network failure.
#
WER_E_NETWORK_FAILURE = 0x801B8002

#
# MessageId: WER_E_NOT_INITIALIZED
#
# MessageText:
#
# Report not initialized.
#
WER_E_NOT_INITIALIZED = 0x801B8003

#
# MessageId: WER_E_ALREADY_REPORTING
#
# MessageText:
#
# Reporting is already in progress for the specified process.
#
WER_E_ALREADY_REPORTING = 0x801B8004

#
# MessageId: WER_E_DUMP_THROTTLED
#
# MessageText:
#
# Dump not generated due to a throttle.
#
WER_E_DUMP_THROTTLED = 0x801B8005

# ***********************
# FACILITY_USERMODE_FILTER_MANAGER
# ***********************
#
# Translation macro for converting FilterManager error codes only from:
#     NTSTATUS  --> HRESULT
#
#define FILTER_HRESULT_FROM_FLT_NTSTATUS(x) (ASSERT((x & 0xfff0000) == 0x001c0000),(HRESULT) (((x) & 0x8000FFFF) | (FACILITY_USERMODE_FILTER_MANAGER << 16)))
#
# MessageId: ERROR_FLT_IO_COMPLETE
#
# MessageText:
#
# The IO was completed by a filter.
#
ERROR_FLT_IO_COMPLETE = 0x001F0001

#
# MessageId: ERROR_FLT_NO_HANDLER_DEFINED
#
# MessageText:
#
# A handler was not defined by the filter for this operation.
#
ERROR_FLT_NO_HANDLER_DEFINED = 0x801F0001

#
# MessageId: ERROR_FLT_CONTEXT_ALREADY_DEFINED
#
# MessageText:
#
# A context is already defined for this object.
#
ERROR_FLT_CONTEXT_ALREADY_DEFINED = 0x801F0002

#
# MessageId: ERROR_FLT_INVALID_ASYNCHRONOUS_REQUEST
#
# MessageText:
#
# Asynchronous requests are not valid for this operation.
#
ERROR_FLT_INVALID_ASYNCHRONOUS_REQUEST = 0x801F0003

#
# MessageId: ERROR_FLT_DISALLOW_FAST_IO
#
# MessageText:
#
# Disallow the Fast IO path for this operation.
#
ERROR_FLT_DISALLOW_FAST_IO = 0x801F0004

#
# MessageId: ERROR_FLT_INVALID_NAME_REQUEST
#
# MessageText:
#
# An invalid name request was made. The name requested cannot be retrieved at this time.
#
ERROR_FLT_INVALID_NAME_REQUEST = 0x801F0005

#
# MessageId: ERROR_FLT_NOT_SAFE_TO_POST_OPERATION
#
# MessageText:
#
# Posting this operation to a worker thread for further processing is not safe at this time because it could lead to a system deadlock.
#
ERROR_FLT_NOT_SAFE_TO_POST_OPERATION = 0x801F0006

#
# MessageId: ERROR_FLT_NOT_INITIALIZED
#
# MessageText:
#
# The Filter Manager was not initialized when a filter tried to register. Make sure that the Filter Manager is getting loaded as a driver.
#
ERROR_FLT_NOT_INITIALIZED = 0x801F0007

#
# MessageId: ERROR_FLT_FILTER_NOT_READY
#
# MessageText:
#
# The filter is not ready for attachment to volumes because it has not finished initializing (FltStartFiltering has not been called).
#
ERROR_FLT_FILTER_NOT_READY = 0x801F0008

#
# MessageId: ERROR_FLT_POST_OPERATION_CLEANUP
#
# MessageText:
#
# The filter must cleanup any operation specific context at this time because it is being removed from the system before the operation is completed by the lower drivers.
#
ERROR_FLT_POST_OPERATION_CLEANUP = 0x801F0009

#
# MessageId: ERROR_FLT_INTERNAL_ERROR
#
# MessageText:
#
# The Filter Manager had an internal error from which it cannot recover, therefore the operation has been failed. This is usually the result of a filter returning an invalid value from a pre-operation callback.
#
ERROR_FLT_INTERNAL_ERROR = 0x801F000A

#
# MessageId: ERROR_FLT_DELETING_OBJECT
#
# MessageText:
#
# The object specified for this action is in the process of being deleted, therefore the action requested cannot be completed at this time.
#
ERROR_FLT_DELETING_OBJECT = 0x801F000B

#
# MessageId: ERROR_FLT_MUST_BE_NONPAGED_POOL
#
# MessageText:
#
# Non-paged pool must be used for this type of context.
#
ERROR_FLT_MUST_BE_NONPAGED_POOL = 0x801F000C

#
# MessageId: ERROR_FLT_DUPLICATE_ENTRY
#
# MessageText:
#
# A duplicate handler definition has been provided for an operation.
#
ERROR_FLT_DUPLICATE_ENTRY = 0x801F000D

#
# MessageId: ERROR_FLT_CBDQ_DISABLED
#
# MessageText:
#
# The callback data queue has been disabled.
#
ERROR_FLT_CBDQ_DISABLED = 0x801F000E

#
# MessageId: ERROR_FLT_DO_NOT_ATTACH
#
# MessageText:
#
# Do not attach the filter to the volume at this time.
#
ERROR_FLT_DO_NOT_ATTACH = 0x801F000F

#
# MessageId: ERROR_FLT_DO_NOT_DETACH
#
# MessageText:
#
# Do not detach the filter from the volume at this time.
#
ERROR_FLT_DO_NOT_DETACH = 0x801F0010

#
# MessageId: ERROR_FLT_INSTANCE_ALTITUDE_COLLISION
#
# MessageText:
#
# An instance already exists at this altitude on the volume specified.
#
ERROR_FLT_INSTANCE_ALTITUDE_COLLISION = 0x801F0011

#
# MessageId: ERROR_FLT_INSTANCE_NAME_COLLISION
#
# MessageText:
#
# An instance already exists with this name on the volume specified.
#
ERROR_FLT_INSTANCE_NAME_COLLISION = 0x801F0012

#
# MessageId: ERROR_FLT_FILTER_NOT_FOUND
#
# MessageText:
#
# The system could not find the filter specified.
#
ERROR_FLT_FILTER_NOT_FOUND = 0x801F0013

#
# MessageId: ERROR_FLT_VOLUME_NOT_FOUND
#
# MessageText:
#
# The system could not find the volume specified.
#
ERROR_FLT_VOLUME_NOT_FOUND = 0x801F0014

#
# MessageId: ERROR_FLT_INSTANCE_NOT_FOUND
#
# MessageText:
#
# The system could not find the instance specified.
#
ERROR_FLT_INSTANCE_NOT_FOUND = 0x801F0015

#
# MessageId: ERROR_FLT_CONTEXT_ALLOCATION_NOT_FOUND
#
# MessageText:
#
# No registered context allocation definition was found for the given request.
#
ERROR_FLT_CONTEXT_ALLOCATION_NOT_FOUND = 0x801F0016

#
# MessageId: ERROR_FLT_INVALID_CONTEXT_REGISTRATION
#
# MessageText:
#
# An invalid parameter was specified during context registration.
#
ERROR_FLT_INVALID_CONTEXT_REGISTRATION = 0x801F0017

#
# MessageId: ERROR_FLT_NAME_CACHE_MISS
#
# MessageText:
#
# The name requested was not found in Filter Manager's name cache and could not be retrieved from the file system.
#
ERROR_FLT_NAME_CACHE_MISS = 0x801F0018

#
# MessageId: ERROR_FLT_NO_DEVICE_OBJECT
#
# MessageText:
#
# The requested device object does not exist for the given volume.
#
ERROR_FLT_NO_DEVICE_OBJECT = 0x801F0019

#
# MessageId: ERROR_FLT_VOLUME_ALREADY_MOUNTED
#
# MessageText:
#
# The specified volume is already mounted.
#
ERROR_FLT_VOLUME_ALREADY_MOUNTED = 0x801F001A

#
# MessageId: ERROR_FLT_ALREADY_ENLISTED
#
# MessageText:
#
# The specified Transaction Context is already enlisted in a transaction
#
ERROR_FLT_ALREADY_ENLISTED = 0x801F001B

#
# MessageId: ERROR_FLT_CONTEXT_ALREADY_LINKED
#
# MessageText:
#
# The specifiec context is already attached to another object
#
ERROR_FLT_CONTEXT_ALREADY_LINKED = 0x801F001C

#
# MessageId: ERROR_FLT_NO_WAITER_FOR_REPLY
#
# MessageText:
#
# No waiter is present for the filter's reply to this message.
#
ERROR_FLT_NO_WAITER_FOR_REPLY = 0x801F0020

#
# MessageId: ERROR_FLT_REGISTRATION_BUSY
#
# MessageText:
#
# The filesystem database resource is in use. Registration cannot complete at this time.
#
ERROR_FLT_REGISTRATION_BUSY = 0x801F0023

#
# ===============================
# Facility Graphics Error Messages
# ===============================
#
#
# The following are the subranges within the Graphics facility
#
# 0x0000 - 0x0fff     Display Driver Loader driver & Video Port errors (displdr.sys, videoprt.sys)
# 0x1000 - 0x1fff     Monitor Class Function driver errors             (monitor.sys)
# 0x2000 - 0x2fff     Windows Graphics Kernel Subsystem errors         (dxgkrnl.sys)
# 0x3000 - 0x3fff               Desktop Window Manager errors
#   0x2000 - 0x20ff      Common errors
#   0x2100 - 0x21ff      Video Memory Manager (VidMM) subsystem errors
#   0x2200 - 0x22ff      Video GPU Scheduler (VidSch) subsystem errors
#   0x2300 - 0x23ff      Video Display Mode Management (VidDMM) subsystem errors
#
# Display Driver Loader driver & Video Port errors {0x0000..0x0fff}
#
#
# MessageId: ERROR_HUNG_DISPLAY_DRIVER_THREAD
#
# MessageText:
#
# {Display Driver Stopped Responding}
# The %hs display driver has stopped working normally. Save your work and reboot the system to restore full display functionality.
# The next time you reboot the machine a dialog will be displayed giving you a chance to report this failure to Microsoft.
#
ERROR_HUNG_DISPLAY_DRIVER_THREAD = 0x80260001

#
# Desktop Window Manager errors {0x3000..0x3fff}
#
#
# MessageId: DWM_E_COMPOSITIONDISABLED
#
# MessageText:
#
# {Desktop composition is disabled}
# The operation could not be completed because desktop composition is disabled.
#
DWM_E_COMPOSITIONDISABLED = 0x80263001

#
# MessageId: DWM_E_REMOTING_NOT_SUPPORTED
#
# MessageText:
#
# {Some desktop composition APIs are not supported while remoting}
# The operation is not supported while running in a remote session.
#
DWM_E_REMOTING_NOT_SUPPORTED = 0x80263002

#
# MessageId: DWM_E_NO_REDIRECTION_SURFACE_AVAILABLE
#
# MessageText:
#
# {No DWM redirection surface is available}
# The DWM was unable to provide a redireciton surface to complete the DirectX present.
#
DWM_E_NO_REDIRECTION_SURFACE_AVAILABLE = 0x80263003

#
# MessageId: DWM_E_NOT_QUEUING_PRESENTS
#
# MessageText:
#
# {DWM is not queuing presents for the specified window}
# The window specified is not currently using queued presents.
#
DWM_E_NOT_QUEUING_PRESENTS = 0x80263004

#
# MessageId: DWM_E_ADAPTER_NOT_FOUND
#
# MessageText:
#
# {The adapter specified by the LUID is not found}
# DWM can not find the adapter specified by the LUID.
#
DWM_E_ADAPTER_NOT_FOUND = 0x80263005

#
# MessageId: DWM_S_GDI_REDIRECTION_SURFACE
#
# MessageText:
#
# {GDI redirection surface was returned}
# GDI redirection surface of the top level window was returned.
#
DWM_S_GDI_REDIRECTION_SURFACE = 0x00263005

#
# MessageId: DWM_E_TEXTURE_TOO_LARGE
#
# MessageText:
#
# {Redirection surface can not be created.  The size of the surface is larger than what is supported on this machine}
# Redirection surface can not be created.  The size of the surface is larger than what is supported on this machine.
#
DWM_E_TEXTURE_TOO_LARGE = 0x80263007

#
# Monitor class function driver errors {0x1000..0x1fff}
#
#
# MessageId: ERROR_MONITOR_NO_DESCRIPTOR
#
# MessageText:
#
# Monitor descriptor could not be obtained.
#
ERROR_MONITOR_NO_DESCRIPTOR = 0x80261001

#
# MessageId: ERROR_MONITOR_UNKNOWN_DESCRIPTOR_FORMAT
#
# MessageText:
#
# Format of the obtained monitor descriptor is not supported by this release.
#
ERROR_MONITOR_UNKNOWN_DESCRIPTOR_FORMAT = 0x80261002

#
# MessageId: ERROR_MONITOR_INVALID_DESCRIPTOR_CHECKSUM
#
# MessageText:
#
# Checksum of the obtained monitor descriptor is invalid.
#
ERROR_MONITOR_INVALID_DESCRIPTOR_CHECKSUM = 0xC0261003

#
# MessageId: ERROR_MONITOR_INVALID_STANDARD_TIMING_BLOCK
#
# MessageText:
#
# Monitor descriptor contains an invalid standard timing block.
#
ERROR_MONITOR_INVALID_STANDARD_TIMING_BLOCK = 0xC0261004

#
# MessageId: ERROR_MONITOR_WMI_DATABLOCK_REGISTRATION_FAILED
#
# MessageText:
#
# WMI data block registration failed for one of the MSMonitorClass WMI subclasses.
#
ERROR_MONITOR_WMI_DATABLOCK_REGISTRATION_FAILED = 0xC0261005

#
# MessageId: ERROR_MONITOR_INVALID_SERIAL_NUMBER_MONDSC_BLOCK
#
# MessageText:
#
# Provided monitor descriptor block is either corrupted or does not contain monitor's detailed serial number.
#
ERROR_MONITOR_INVALID_SERIAL_NUMBER_MONDSC_BLOCK = 0xC0261006

#
# MessageId: ERROR_MONITOR_INVALID_USER_FRIENDLY_MONDSC_BLOCK
#
# MessageText:
#
# Provided monitor descriptor block is either corrupted or does not contain monitor's user friendly name.
#
ERROR_MONITOR_INVALID_USER_FRIENDLY_MONDSC_BLOCK = 0xC0261007

#
# MessageId: ERROR_MONITOR_NO_MORE_DESCRIPTOR_DATA
#
# MessageText:
#
# There is no monitor descriptor data at the specified (offset, size) region.
#
ERROR_MONITOR_NO_MORE_DESCRIPTOR_DATA = 0xC0261008

#
# MessageId: ERROR_MONITOR_INVALID_DETAILED_TIMING_BLOCK
#
# MessageText:
#
# Monitor descriptor contains an invalid detailed timing block.
#
ERROR_MONITOR_INVALID_DETAILED_TIMING_BLOCK = 0xC0261009

#
# MessageId: ERROR_MONITOR_INVALID_MANUFACTURE_DATE
#
# MessageText:
#
# Monitor descriptor contains invalid manufacture date.
#
ERROR_MONITOR_INVALID_MANUFACTURE_DATE = 0xC026100A

#
# Windows Graphics Kernel Subsystem errors {0x2000..0x2fff}
#
# TODO: Add DXG Win32 errors here
#
# Common errors {0x2000..0x20ff}
#
#
# MessageId: ERROR_GRAPHICS_NOT_EXCLUSIVE_MODE_OWNER
#
# MessageText:
#
# Exclusive mode ownership is needed to create unmanaged primary allocation.
#
ERROR_GRAPHICS_NOT_EXCLUSIVE_MODE_OWNER = 0xC0262000

#
# MessageId: ERROR_GRAPHICS_INSUFFICIENT_DMA_BUFFER
#
# MessageText:
#
# The driver needs more DMA buffer space in order to complete the requested operation.
#
ERROR_GRAPHICS_INSUFFICIENT_DMA_BUFFER = 0xC0262001

#
# MessageId: ERROR_GRAPHICS_INVALID_DISPLAY_ADAPTER
#
# MessageText:
#
# Specified display adapter handle is invalid.
#
ERROR_GRAPHICS_INVALID_DISPLAY_ADAPTER = 0xC0262002

#
# MessageId: ERROR_GRAPHICS_ADAPTER_WAS_RESET
#
# MessageText:
#
# Specified display adapter and all of its state has been reset.
#
ERROR_GRAPHICS_ADAPTER_WAS_RESET = 0xC0262003

#
# MessageId: ERROR_GRAPHICS_INVALID_DRIVER_MODEL
#
# MessageText:
#
# The driver stack doesn't match the expected driver model.
#
ERROR_GRAPHICS_INVALID_DRIVER_MODEL = 0xC0262004

#
# MessageId: ERROR_GRAPHICS_PRESENT_MODE_CHANGED
#
# MessageText:
#
# Present happened but ended up into the changed desktop mode
#
ERROR_GRAPHICS_PRESENT_MODE_CHANGED = 0xC0262005

#
# MessageId: ERROR_GRAPHICS_PRESENT_OCCLUDED
#
# MessageText:
#
# Nothing to present due to desktop occlusion
#
ERROR_GRAPHICS_PRESENT_OCCLUDED = 0xC0262006

#
# MessageId: ERROR_GRAPHICS_PRESENT_DENIED
#
# MessageText:
#
# Not able to present due to denial of desktop access
#
ERROR_GRAPHICS_PRESENT_DENIED = 0xC0262007

#
# MessageId: ERROR_GRAPHICS_CANNOTCOLORCONVERT
#
# MessageText:
#
# Not able to present with color convertion
#
ERROR_GRAPHICS_CANNOTCOLORCONVERT = 0xC0262008

#
# MessageId: ERROR_GRAPHICS_DRIVER_MISMATCH
#
# MessageText:
#
# The kernel driver detected a version mismatch between it and the user mode driver.
#
ERROR_GRAPHICS_DRIVER_MISMATCH = 0xC0262009

#
# MessageId: ERROR_GRAPHICS_PARTIAL_DATA_POPULATED
#
# MessageText:
#
# Specified buffer is not big enough to contain entire requested dataset. Partial data populated up to the size of the buffer. Caller needs to provide buffer of size as specified in the partially populated buffer's content (interface specific).
#
ERROR_GRAPHICS_PARTIAL_DATA_POPULATED = 0x4026200A

#
# MessageId: ERROR_GRAPHICS_PRESENT_REDIRECTION_DISABLED
#
# MessageText:
#
# Present redirection is disabled (desktop windowing management subsystem is off).
#
ERROR_GRAPHICS_PRESENT_REDIRECTION_DISABLED = 0xC026200B

#
# MessageId: ERROR_GRAPHICS_PRESENT_UNOCCLUDED
#
# MessageText:
#
# Previous exclusive VidPn source owner has released its ownership
#
ERROR_GRAPHICS_PRESENT_UNOCCLUDED = 0xC026200C

#
# MessageId: ERROR_GRAPHICS_WINDOWDC_NOT_AVAILABLE
#
# MessageText:
#
# Window DC is not available for presentation
#
ERROR_GRAPHICS_WINDOWDC_NOT_AVAILABLE = 0xC026200D

#
# MessageId: ERROR_GRAPHICS_WINDOWLESS_PRESENT_DISABLED
#
# MessageText:
#
# Windowless present is disabled (desktop windowing management subsystem is off).
#
ERROR_GRAPHICS_WINDOWLESS_PRESENT_DISABLED = 0xC026200E

#
# Video Memory Manager (VidMM) subsystem errors {0x2100..0x21ff}
#
#
# MessageId: ERROR_GRAPHICS_NO_VIDEO_MEMORY
#
# MessageText:
#
# Not enough video memory available to complete the operation.
#
ERROR_GRAPHICS_NO_VIDEO_MEMORY = 0xC0262100

#
# MessageId: ERROR_GRAPHICS_CANT_LOCK_MEMORY
#
# MessageText:
#
# Couldn't probe and lock the underlying memory of an allocation.
#
ERROR_GRAPHICS_CANT_LOCK_MEMORY = 0xC0262101

#
# MessageId: ERROR_GRAPHICS_ALLOCATION_BUSY
#
# MessageText:
#
# The allocation is currently busy.
#
ERROR_GRAPHICS_ALLOCATION_BUSY = 0xC0262102

#
# MessageId: ERROR_GRAPHICS_TOO_MANY_REFERENCES
#
# MessageText:
#
# An object being referenced has reach the maximum reference count already and can't be reference further.
#
ERROR_GRAPHICS_TOO_MANY_REFERENCES = 0xC0262103

#
# MessageId: ERROR_GRAPHICS_TRY_AGAIN_LATER
#
# MessageText:
#
# A problem couldn't be solved due to some currently existing condition. The problem should be tried again later.
#
ERROR_GRAPHICS_TRY_AGAIN_LATER = 0xC0262104

#
# MessageId: ERROR_GRAPHICS_TRY_AGAIN_NOW
#
# MessageText:
#
# A problem couldn't be solved due to some currently existing condition. The problem should be tried again immediately.
#
ERROR_GRAPHICS_TRY_AGAIN_NOW = 0xC0262105

#
# MessageId: ERROR_GRAPHICS_ALLOCATION_INVALID
#
# MessageText:
#
# The allocation is invalid.
#
ERROR_GRAPHICS_ALLOCATION_INVALID = 0xC0262106

#
# MessageId: ERROR_GRAPHICS_UNSWIZZLING_APERTURE_UNAVAILABLE
#
# MessageText:
#
# No more unswizzling aperture are currently available.
#
ERROR_GRAPHICS_UNSWIZZLING_APERTURE_UNAVAILABLE = 0xC0262107

#
# MessageId: ERROR_GRAPHICS_UNSWIZZLING_APERTURE_UNSUPPORTED
#
# MessageText:
#
# The current allocation can't be unswizzled by an aperture.
#
ERROR_GRAPHICS_UNSWIZZLING_APERTURE_UNSUPPORTED = 0xC0262108

#
# MessageId: ERROR_GRAPHICS_CANT_EVICT_PINNED_ALLOCATION
#
# MessageText:
#
# The request failed because a pinned allocation can't be evicted.
#
ERROR_GRAPHICS_CANT_EVICT_PINNED_ALLOCATION = 0xC0262109

#
# MessageId: ERROR_GRAPHICS_INVALID_ALLOCATION_USAGE
#
# MessageText:
#
# The allocation can't be used from its current segment location for the specified operation.
#
ERROR_GRAPHICS_INVALID_ALLOCATION_USAGE = 0xC0262110

#
# MessageId: ERROR_GRAPHICS_CANT_RENDER_LOCKED_ALLOCATION
#
# MessageText:
#
# A locked allocation can't be used in the current command buffer.
#
ERROR_GRAPHICS_CANT_RENDER_LOCKED_ALLOCATION = 0xC0262111

#
# MessageId: ERROR_GRAPHICS_ALLOCATION_CLOSED
#
# MessageText:
#
# The allocation being referenced has been closed permanently.
#
ERROR_GRAPHICS_ALLOCATION_CLOSED = 0xC0262112

#
# MessageId: ERROR_GRAPHICS_INVALID_ALLOCATION_INSTANCE
#
# MessageText:
#
# An invalid allocation instance is being referenced.
#
ERROR_GRAPHICS_INVALID_ALLOCATION_INSTANCE = 0xC0262113

#
# MessageId: ERROR_GRAPHICS_INVALID_ALLOCATION_HANDLE
#
# MessageText:
#
# An invalid allocation handle is being referenced.
#
ERROR_GRAPHICS_INVALID_ALLOCATION_HANDLE = 0xC0262114

#
# MessageId: ERROR_GRAPHICS_WRONG_ALLOCATION_DEVICE
#
# MessageText:
#
# The allocation being referenced doesn't belong to the current device.
#
ERROR_GRAPHICS_WRONG_ALLOCATION_DEVICE = 0xC0262115

#
# MessageId: ERROR_GRAPHICS_ALLOCATION_CONTENT_LOST
#
# MessageText:
#
# The specified allocation lost its content.
#
ERROR_GRAPHICS_ALLOCATION_CONTENT_LOST = 0xC0262116

#
# Video GPU Scheduler (VidSch) subsystem errors {0x2200..0x22ff}
#
#
# MessageId: ERROR_GRAPHICS_GPU_EXCEPTION_ON_DEVICE
#
# MessageText:
#
# GPU exception is detected on the given device. The device is not able to be scheduled.
#
ERROR_GRAPHICS_GPU_EXCEPTION_ON_DEVICE = 0xC0262200

#
# MessageId: ERROR_GRAPHICS_SKIP_ALLOCATION_PREPARATION
#
# MessageText:
#
# Skip preparation of allocations referenced by the DMA buffer.
#
ERROR_GRAPHICS_SKIP_ALLOCATION_PREPARATION = 0x40262201

#
# Video Present Network Management (VidPNMgr) subsystem errors {0x2300..0x23ff}
#
#
# MessageId: ERROR_GRAPHICS_INVALID_VIDPN_TOPOLOGY
#
# MessageText:
#
# Specified VidPN topology is invalid.
#
ERROR_GRAPHICS_INVALID_VIDPN_TOPOLOGY = 0xC0262300

#
# MessageId: ERROR_GRAPHICS_VIDPN_TOPOLOGY_NOT_SUPPORTED
#
# MessageText:
#
# Specified VidPN topology is valid but is not supported by this model of the display adapter.
#
ERROR_GRAPHICS_VIDPN_TOPOLOGY_NOT_SUPPORTED = 0xC0262301

#
# MessageId: ERROR_GRAPHICS_VIDPN_TOPOLOGY_CURRENTLY_NOT_SUPPORTED
#
# MessageText:
#
# Specified VidPN topology is valid but is not supported by the display adapter at this time, due to current allocation of its resources.
#
ERROR_GRAPHICS_VIDPN_TOPOLOGY_CURRENTLY_NOT_SUPPORTED = 0xC0262302

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDPN
#
# MessageText:
#
# Specified VidPN handle is invalid.
#
ERROR_GRAPHICS_INVALID_VIDPN = 0xC0262303

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE
#
# MessageText:
#
# Specified video present source is invalid.
#
ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE = 0xC0262304

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET
#
# MessageText:
#
# Specified video present target is invalid.
#
ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET = 0xC0262305

#
# MessageId: ERROR_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED
#
# MessageText:
#
# Specified VidPN modality is not supported (e.g. at least two of the pinned modes are not cofunctional).
#
ERROR_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED = 0xC0262306

#
# MessageId: ERROR_GRAPHICS_MODE_NOT_PINNED
#
# MessageText:
#
# No mode is pinned on the specified VidPN source/target.
#
ERROR_GRAPHICS_MODE_NOT_PINNED = 0x00262307

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDPN_SOURCEMODESET
#
# MessageText:
#
# Specified VidPN source mode set is invalid.
#
ERROR_GRAPHICS_INVALID_VIDPN_SOURCEMODESET = 0xC0262308

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDPN_TARGETMODESET
#
# MessageText:
#
# Specified VidPN target mode set is invalid.
#
ERROR_GRAPHICS_INVALID_VIDPN_TARGETMODESET = 0xC0262309

#
# MessageId: ERROR_GRAPHICS_INVALID_FREQUENCY
#
# MessageText:
#
# Specified video signal frequency is invalid.
#
ERROR_GRAPHICS_INVALID_FREQUENCY = 0xC026230A

#
# MessageId: ERROR_GRAPHICS_INVALID_ACTIVE_REGION
#
# MessageText:
#
# Specified video signal active region is invalid.
#
ERROR_GRAPHICS_INVALID_ACTIVE_REGION = 0xC026230B

#
# MessageId: ERROR_GRAPHICS_INVALID_TOTAL_REGION
#
# MessageText:
#
# Specified video signal total region is invalid.
#
ERROR_GRAPHICS_INVALID_TOTAL_REGION = 0xC026230C

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE_MODE
#
# MessageText:
#
# Specified video present source mode is invalid.
#
ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE_MODE = 0xC0262310

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET_MODE
#
# MessageText:
#
# Specified video present target mode is invalid.
#
ERROR_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET_MODE = 0xC0262311

#
# MessageId: ERROR_GRAPHICS_PINNED_MODE_MUST_REMAIN_IN_SET
#
# MessageText:
#
# Pinned mode must remain in the set on VidPN's cofunctional modality enumeration.
#
ERROR_GRAPHICS_PINNED_MODE_MUST_REMAIN_IN_SET = 0xC0262312

#
# MessageId: ERROR_GRAPHICS_PATH_ALREADY_IN_TOPOLOGY
#
# MessageText:
#
# Specified video present path is already in VidPN's topology.
#
ERROR_GRAPHICS_PATH_ALREADY_IN_TOPOLOGY = 0xC0262313

#
# MessageId: ERROR_GRAPHICS_MODE_ALREADY_IN_MODESET
#
# MessageText:
#
# Specified mode is already in the mode set.
#
ERROR_GRAPHICS_MODE_ALREADY_IN_MODESET = 0xC0262314

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDEOPRESENTSOURCESET
#
# MessageText:
#
# Specified video present source set is invalid.
#
ERROR_GRAPHICS_INVALID_VIDEOPRESENTSOURCESET = 0xC0262315

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDEOPRESENTTARGETSET
#
# MessageText:
#
# Specified video present target set is invalid.
#
ERROR_GRAPHICS_INVALID_VIDEOPRESENTTARGETSET = 0xC0262316

#
# MessageId: ERROR_GRAPHICS_SOURCE_ALREADY_IN_SET
#
# MessageText:
#
# Specified video present source is already in the video present source set.
#
ERROR_GRAPHICS_SOURCE_ALREADY_IN_SET = 0xC0262317

#
# MessageId: ERROR_GRAPHICS_TARGET_ALREADY_IN_SET
#
# MessageText:
#
# Specified video present target is already in the video present target set.
#
ERROR_GRAPHICS_TARGET_ALREADY_IN_SET = 0xC0262318

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDPN_PRESENT_PATH
#
# MessageText:
#
# Specified VidPN present path is invalid.
#
ERROR_GRAPHICS_INVALID_VIDPN_PRESENT_PATH = 0xC0262319

#
# MessageId: ERROR_GRAPHICS_NO_RECOMMENDED_VIDPN_TOPOLOGY
#
# MessageText:
#
# Miniport has no recommendation for augmentation of the specified VidPN's topology.
#
ERROR_GRAPHICS_NO_RECOMMENDED_VIDPN_TOPOLOGY = 0xC026231A

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGESET
#
# MessageText:
#
# Specified monitor frequency range set is invalid.
#
ERROR_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGESET = 0xC026231B

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGE
#
# MessageText:
#
# Specified monitor frequency range is invalid.
#
ERROR_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGE = 0xC026231C

#
# MessageId: ERROR_GRAPHICS_FREQUENCYRANGE_NOT_IN_SET
#
# MessageText:
#
# Specified frequency range is not in the specified monitor frequency range set.
#
ERROR_GRAPHICS_FREQUENCYRANGE_NOT_IN_SET = 0xC026231D

#
# MessageId: ERROR_GRAPHICS_NO_PREFERRED_MODE
#
# MessageText:
#
# Specified mode set does not specify preference for one of its modes.
#
ERROR_GRAPHICS_NO_PREFERRED_MODE = 0x0026231E

#
# MessageId: ERROR_GRAPHICS_FREQUENCYRANGE_ALREADY_IN_SET
#
# MessageText:
#
# Specified frequency range is already in the specified monitor frequency range set.
#
ERROR_GRAPHICS_FREQUENCYRANGE_ALREADY_IN_SET = 0xC026231F

#
# MessageId: ERROR_GRAPHICS_STALE_MODESET
#
# MessageText:
#
# Specified mode set is stale. Please reacquire the new mode set.
#
ERROR_GRAPHICS_STALE_MODESET = 0xC0262320

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITOR_SOURCEMODESET
#
# MessageText:
#
# Specified monitor source mode set is invalid.
#
ERROR_GRAPHICS_INVALID_MONITOR_SOURCEMODESET = 0xC0262321

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITOR_SOURCE_MODE
#
# MessageText:
#
# Specified monitor source mode is invalid.
#
ERROR_GRAPHICS_INVALID_MONITOR_SOURCE_MODE = 0xC0262322

#
# MessageId: ERROR_GRAPHICS_NO_RECOMMENDED_FUNCTIONAL_VIDPN
#
# MessageText:
#
# Miniport does not have any recommendation regarding the request to provide a functional VidPN given the current display adapter configuration.
#
ERROR_GRAPHICS_NO_RECOMMENDED_FUNCTIONAL_VIDPN = 0xC0262323

#
# MessageId: ERROR_GRAPHICS_MODE_ID_MUST_BE_UNIQUE
#
# MessageText:
#
# ID of the specified mode is already used by another mode in the set.
#
ERROR_GRAPHICS_MODE_ID_MUST_BE_UNIQUE = 0xC0262324

#
# MessageId: ERROR_GRAPHICS_EMPTY_ADAPTER_MONITOR_MODE_SUPPORT_INTERSECTION
#
# MessageText:
#
# System failed to determine a mode that is supported by both the display adapter and the monitor connected to it.
#
ERROR_GRAPHICS_EMPTY_ADAPTER_MONITOR_MODE_SUPPORT_INTERSECTION = 0xC0262325

#
# MessageId: ERROR_GRAPHICS_VIDEO_PRESENT_TARGETS_LESS_THAN_SOURCES
#
# MessageText:
#
# Number of video present targets must be greater than or equal to the number of video present sources.
#
ERROR_GRAPHICS_VIDEO_PRESENT_TARGETS_LESS_THAN_SOURCES = 0xC0262326

#
# MessageId: ERROR_GRAPHICS_PATH_NOT_IN_TOPOLOGY
#
# MessageText:
#
# Specified present path is not in VidPN's topology.
#
ERROR_GRAPHICS_PATH_NOT_IN_TOPOLOGY = 0xC0262327

#
# MessageId: ERROR_GRAPHICS_ADAPTER_MUST_HAVE_AT_LEAST_ONE_SOURCE
#
# MessageText:
#
# Display adapter must have at least one video present source.
#
ERROR_GRAPHICS_ADAPTER_MUST_HAVE_AT_LEAST_ONE_SOURCE = 0xC0262328

#
# MessageId: ERROR_GRAPHICS_ADAPTER_MUST_HAVE_AT_LEAST_ONE_TARGET
#
# MessageText:
#
# Display adapter must have at least one video present target.
#
ERROR_GRAPHICS_ADAPTER_MUST_HAVE_AT_LEAST_ONE_TARGET = 0xC0262329

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITORDESCRIPTORSET
#
# MessageText:
#
# Specified monitor descriptor set is invalid.
#
ERROR_GRAPHICS_INVALID_MONITORDESCRIPTORSET = 0xC026232A

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITORDESCRIPTOR
#
# MessageText:
#
# Specified monitor descriptor is invalid.
#
ERROR_GRAPHICS_INVALID_MONITORDESCRIPTOR = 0xC026232B

#
# MessageId: ERROR_GRAPHICS_MONITORDESCRIPTOR_NOT_IN_SET
#
# MessageText:
#
# Specified descriptor is not in the specified monitor descriptor set.
#
ERROR_GRAPHICS_MONITORDESCRIPTOR_NOT_IN_SET = 0xC026232C

#
# MessageId: ERROR_GRAPHICS_MONITORDESCRIPTOR_ALREADY_IN_SET
#
# MessageText:
#
# Specified descriptor is already in the specified monitor descriptor set.
#
ERROR_GRAPHICS_MONITORDESCRIPTOR_ALREADY_IN_SET = 0xC026232D

#
# MessageId: ERROR_GRAPHICS_MONITORDESCRIPTOR_ID_MUST_BE_UNIQUE
#
# MessageText:
#
# ID of the specified monitor descriptor is already used by another descriptor in the set.
#
ERROR_GRAPHICS_MONITORDESCRIPTOR_ID_MUST_BE_UNIQUE = 0xC026232E

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDPN_TARGET_SUBSET_TYPE
#
# MessageText:
#
# Specified video present target subset type is invalid.
#
ERROR_GRAPHICS_INVALID_VIDPN_TARGET_SUBSET_TYPE = 0xC026232F

#
# MessageId: ERROR_GRAPHICS_RESOURCES_NOT_RELATED
#
# MessageText:
#
# Two or more of the specified resources are not related to each other, as defined by the interface semantics.
#
ERROR_GRAPHICS_RESOURCES_NOT_RELATED = 0xC0262330

#
# MessageId: ERROR_GRAPHICS_SOURCE_ID_MUST_BE_UNIQUE
#
# MessageText:
#
# ID of the specified video present source is already used by another source in the set.
#
ERROR_GRAPHICS_SOURCE_ID_MUST_BE_UNIQUE = 0xC0262331

#
# MessageId: ERROR_GRAPHICS_TARGET_ID_MUST_BE_UNIQUE
#
# MessageText:
#
# ID of the specified video present target is already used by another target in the set.
#
ERROR_GRAPHICS_TARGET_ID_MUST_BE_UNIQUE = 0xC0262332

#
# MessageId: ERROR_GRAPHICS_NO_AVAILABLE_VIDPN_TARGET
#
# MessageText:
#
# Specified VidPN source cannot be used because there is no available VidPN target to connect it to.
#
ERROR_GRAPHICS_NO_AVAILABLE_VIDPN_TARGET = 0xC0262333

#
# MessageId: ERROR_GRAPHICS_MONITOR_COULD_NOT_BE_ASSOCIATED_WITH_ADAPTER
#
# MessageText:
#
# Newly arrived monitor could not be associated with a display adapter.
#
ERROR_GRAPHICS_MONITOR_COULD_NOT_BE_ASSOCIATED_WITH_ADAPTER = 0xC0262334

#
# MessageId: ERROR_GRAPHICS_NO_VIDPNMGR
#
# MessageText:
#
# Display adapter in question does not have an associated VidPN manager.
#
ERROR_GRAPHICS_NO_VIDPNMGR = 0xC0262335

#
# MessageId: ERROR_GRAPHICS_NO_ACTIVE_VIDPN
#
# MessageText:
#
# VidPN manager of the display adapter in question does not have an active VidPN.
#
ERROR_GRAPHICS_NO_ACTIVE_VIDPN = 0xC0262336

#
# MessageId: ERROR_GRAPHICS_STALE_VIDPN_TOPOLOGY
#
# MessageText:
#
# Specified VidPN topology is stale. Please reacquire the new topology.
#
ERROR_GRAPHICS_STALE_VIDPN_TOPOLOGY = 0xC0262337

#
# MessageId: ERROR_GRAPHICS_MONITOR_NOT_CONNECTED
#
# MessageText:
#
# There is no monitor connected on the specified video present target.
#
ERROR_GRAPHICS_MONITOR_NOT_CONNECTED = 0xC0262338

#
# MessageId: ERROR_GRAPHICS_SOURCE_NOT_IN_TOPOLOGY
#
# MessageText:
#
# Specified source is not part of the specified VidPN's topology.
#
ERROR_GRAPHICS_SOURCE_NOT_IN_TOPOLOGY = 0xC0262339

#
# MessageId: ERROR_GRAPHICS_INVALID_PRIMARYSURFACE_SIZE
#
# MessageText:
#
# Specified primary surface size is invalid.
#
ERROR_GRAPHICS_INVALID_PRIMARYSURFACE_SIZE = 0xC026233A

#
# MessageId: ERROR_GRAPHICS_INVALID_VISIBLEREGION_SIZE
#
# MessageText:
#
# Specified visible region size is invalid.
#
ERROR_GRAPHICS_INVALID_VISIBLEREGION_SIZE = 0xC026233B

#
# MessageId: ERROR_GRAPHICS_INVALID_STRIDE
#
# MessageText:
#
# Specified stride is invalid.
#
ERROR_GRAPHICS_INVALID_STRIDE = 0xC026233C

#
# MessageId: ERROR_GRAPHICS_INVALID_PIXELFORMAT
#
# MessageText:
#
# Specified pixel format is invalid.
#
ERROR_GRAPHICS_INVALID_PIXELFORMAT = 0xC026233D

#
# MessageId: ERROR_GRAPHICS_INVALID_COLORBASIS
#
# MessageText:
#
# Specified color basis is invalid.
#
ERROR_GRAPHICS_INVALID_COLORBASIS = 0xC026233E

#
# MessageId: ERROR_GRAPHICS_INVALID_PIXELVALUEACCESSMODE
#
# MessageText:
#
# Specified pixel value access mode is invalid.
#
ERROR_GRAPHICS_INVALID_PIXELVALUEACCESSMODE = 0xC026233F

#
# MessageId: ERROR_GRAPHICS_TARGET_NOT_IN_TOPOLOGY
#
# MessageText:
#
# Specified target is not part of the specified VidPN's topology.
#
ERROR_GRAPHICS_TARGET_NOT_IN_TOPOLOGY = 0xC0262340

#
# MessageId: ERROR_GRAPHICS_NO_DISPLAY_MODE_MANAGEMENT_SUPPORT
#
# MessageText:
#
# Failed to acquire display mode management interface.
#
ERROR_GRAPHICS_NO_DISPLAY_MODE_MANAGEMENT_SUPPORT = 0xC0262341

#
# MessageId: ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE
#
# MessageText:
#
# Specified VidPN source is already owned by a DMM client and cannot be used until that client releases it.
#
ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE = 0xC0262342

#
# MessageId: ERROR_GRAPHICS_CANT_ACCESS_ACTIVE_VIDPN
#
# MessageText:
#
# Specified VidPN is active and cannot be accessed.
#
ERROR_GRAPHICS_CANT_ACCESS_ACTIVE_VIDPN = 0xC0262343

#
# MessageId: ERROR_GRAPHICS_INVALID_PATH_IMPORTANCE_ORDINAL
#
# MessageText:
#
# Specified VidPN present path importance ordinal is invalid.
#
ERROR_GRAPHICS_INVALID_PATH_IMPORTANCE_ORDINAL = 0xC0262344

#
# MessageId: ERROR_GRAPHICS_INVALID_PATH_CONTENT_GEOMETRY_TRANSFORMATION
#
# MessageText:
#
# Specified VidPN present path content geometry transformation is invalid.
#
ERROR_GRAPHICS_INVALID_PATH_CONTENT_GEOMETRY_TRANSFORMATION = 0xC0262345

#
# MessageId: ERROR_GRAPHICS_PATH_CONTENT_GEOMETRY_TRANSFORMATION_NOT_SUPPORTED
#
# MessageText:
#
# Specified content geometry transformation is not supported on the respective VidPN present path.
#
ERROR_GRAPHICS_PATH_CONTENT_GEOMETRY_TRANSFORMATION_NOT_SUPPORTED = 0xC0262346

#
# MessageId: ERROR_GRAPHICS_INVALID_GAMMA_RAMP
#
# MessageText:
#
# Specified gamma ramp is invalid.
#
ERROR_GRAPHICS_INVALID_GAMMA_RAMP = 0xC0262347

#
# MessageId: ERROR_GRAPHICS_GAMMA_RAMP_NOT_SUPPORTED
#
# MessageText:
#
# Specified gamma ramp is not supported on the respective VidPN present path.
#
ERROR_GRAPHICS_GAMMA_RAMP_NOT_SUPPORTED = 0xC0262348

#
# MessageId: ERROR_GRAPHICS_MULTISAMPLING_NOT_SUPPORTED
#
# MessageText:
#
# Multi-sampling is not supported on the respective VidPN present path.
#
ERROR_GRAPHICS_MULTISAMPLING_NOT_SUPPORTED = 0xC0262349

#
# MessageId: ERROR_GRAPHICS_MODE_NOT_IN_MODESET
#
# MessageText:
#
# Specified mode is not in the specified mode set.
#
ERROR_GRAPHICS_MODE_NOT_IN_MODESET = 0xC026234A

#
# MessageId: ERROR_GRAPHICS_DATASET_IS_EMPTY
#
# MessageText:
#
# Specified data set (e.g. mode set, frequency range set, descriptor set, topology, etc.) is empty.
#
ERROR_GRAPHICS_DATASET_IS_EMPTY = 0x0026234B

#
# MessageId: ERROR_GRAPHICS_NO_MORE_ELEMENTS_IN_DATASET
#
# MessageText:
#
# Specified data set (e.g. mode set, frequency range set, descriptor set, topology, etc.) does not contain any more elements.
#
ERROR_GRAPHICS_NO_MORE_ELEMENTS_IN_DATASET = 0x0026234C

#
# MessageId: ERROR_GRAPHICS_INVALID_VIDPN_TOPOLOGY_RECOMMENDATION_REASON
#
# MessageText:
#
# Specified VidPN topology recommendation reason is invalid.
#
ERROR_GRAPHICS_INVALID_VIDPN_TOPOLOGY_RECOMMENDATION_REASON = 0xC026234D

#
# MessageId: ERROR_GRAPHICS_INVALID_PATH_CONTENT_TYPE
#
# MessageText:
#
# Specified VidPN present path content type is invalid.
#
ERROR_GRAPHICS_INVALID_PATH_CONTENT_TYPE = 0xC026234E

#
# MessageId: ERROR_GRAPHICS_INVALID_COPYPROTECTION_TYPE
#
# MessageText:
#
# Specified VidPN present path copy protection type is invalid.
#
ERROR_GRAPHICS_INVALID_COPYPROTECTION_TYPE = 0xC026234F

#
# MessageId: ERROR_GRAPHICS_UNASSIGNED_MODESET_ALREADY_EXISTS
#
# MessageText:
#
# No more than one unassigned mode set can exist at any given time for a given VidPN source/target.
#
ERROR_GRAPHICS_UNASSIGNED_MODESET_ALREADY_EXISTS = 0xC0262350

#
# MessageId: ERROR_GRAPHICS_PATH_CONTENT_GEOMETRY_TRANSFORMATION_NOT_PINNED
#
# MessageText:
#
# Specified content transformation is not pinned on the specified VidPN present path.
#
ERROR_GRAPHICS_PATH_CONTENT_GEOMETRY_TRANSFORMATION_NOT_PINNED = 0x00262351

#
# MessageId: ERROR_GRAPHICS_INVALID_SCANLINE_ORDERING
#
# MessageText:
#
# Specified scanline ordering type is invalid.
#
ERROR_GRAPHICS_INVALID_SCANLINE_ORDERING = 0xC0262352

#
# MessageId: ERROR_GRAPHICS_TOPOLOGY_CHANGES_NOT_ALLOWED
#
# MessageText:
#
# Topology changes are not allowed for the specified VidPN.
#
ERROR_GRAPHICS_TOPOLOGY_CHANGES_NOT_ALLOWED = 0xC0262353

#
# MessageId: ERROR_GRAPHICS_NO_AVAILABLE_IMPORTANCE_ORDINALS
#
# MessageText:
#
# All available importance ordinals are already used in specified topology.
#
ERROR_GRAPHICS_NO_AVAILABLE_IMPORTANCE_ORDINALS = 0xC0262354

#
# MessageId: ERROR_GRAPHICS_INCOMPATIBLE_PRIVATE_FORMAT
#
# MessageText:
#
# Specified primary surface has a different private format attribute than the current primary surface
#
ERROR_GRAPHICS_INCOMPATIBLE_PRIVATE_FORMAT = 0xC0262355

#
# MessageId: ERROR_GRAPHICS_INVALID_MODE_PRUNING_ALGORITHM
#
# MessageText:
#
# Specified mode pruning algorithm is invalid
#
ERROR_GRAPHICS_INVALID_MODE_PRUNING_ALGORITHM = 0xC0262356

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITOR_CAPABILITY_ORIGIN
#
# MessageText:
#
# Specified monitor capability origin is invalid.
#
ERROR_GRAPHICS_INVALID_MONITOR_CAPABILITY_ORIGIN = 0xC0262357

#
# MessageId: ERROR_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGE_CONSTRAINT
#
# MessageText:
#
# Specified monitor frequency range constraint is invalid.
#
ERROR_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGE_CONSTRAINT = 0xC0262358

#
# MessageId: ERROR_GRAPHICS_MAX_NUM_PATHS_REACHED
#
# MessageText:
#
# Maximum supported number of present paths has been reached.
#
ERROR_GRAPHICS_MAX_NUM_PATHS_REACHED = 0xC0262359

#
# MessageId: ERROR_GRAPHICS_CANCEL_VIDPN_TOPOLOGY_AUGMENTATION
#
# MessageText:
#
# Miniport requested that augmentation be cancelled for the specified source of the specified VidPN's topology.
#
ERROR_GRAPHICS_CANCEL_VIDPN_TOPOLOGY_AUGMENTATION = 0xC026235A

#
# MessageId: ERROR_GRAPHICS_INVALID_CLIENT_TYPE
#
# MessageText:
#
# Specified client type was not recognized.
#
ERROR_GRAPHICS_INVALID_CLIENT_TYPE = 0xC026235B

#
# MessageId: ERROR_GRAPHICS_CLIENTVIDPN_NOT_SET
#
# MessageText:
#
# Client VidPN is not set on this adapter (e.g. no user mode initiated mode changes took place on this adapter yet).
#
ERROR_GRAPHICS_CLIENTVIDPN_NOT_SET = 0xC026235C

#
# Port specific status codes {0x2400..0x24ff}
#
#
# MessageId: ERROR_GRAPHICS_SPECIFIED_CHILD_ALREADY_CONNECTED
#
# MessageText:
#
# Specified display adapter child device already has an external device connected to it.
#
ERROR_GRAPHICS_SPECIFIED_CHILD_ALREADY_CONNECTED = 0xC0262400

#
# MessageId: ERROR_GRAPHICS_CHILD_DESCRIPTOR_NOT_SUPPORTED
#
# MessageText:
#
# Specified display adapter child device does not support descriptor exposure.
#
ERROR_GRAPHICS_CHILD_DESCRIPTOR_NOT_SUPPORTED = 0xC0262401

#
# MessageId: ERROR_GRAPHICS_UNKNOWN_CHILD_STATUS
#
# MessageText:
#
# Child device presence was not reliably detected.
#
ERROR_GRAPHICS_UNKNOWN_CHILD_STATUS = 0x4026242F

#
# MessageId: ERROR_GRAPHICS_NOT_A_LINKED_ADAPTER
#
# MessageText:
#
# The display adapter is not linked to any other adapters.
#
ERROR_GRAPHICS_NOT_A_LINKED_ADAPTER = 0xC0262430

#
# MessageId: ERROR_GRAPHICS_LEADLINK_NOT_ENUMERATED
#
# MessageText:
#
# Lead adapter in a linked configuration was not enumerated yet.
#
ERROR_GRAPHICS_LEADLINK_NOT_ENUMERATED = 0xC0262431

#
# MessageId: ERROR_GRAPHICS_CHAINLINKS_NOT_ENUMERATED
#
# MessageText:
#
# Some chain adapters in a linked configuration were not enumerated yet.
#
ERROR_GRAPHICS_CHAINLINKS_NOT_ENUMERATED = 0xC0262432

#
# MessageId: ERROR_GRAPHICS_ADAPTER_CHAIN_NOT_READY
#
# MessageText:
#
# The chain of linked adapters is not ready to start because of an unknown failure.
#
ERROR_GRAPHICS_ADAPTER_CHAIN_NOT_READY = 0xC0262433

#
# MessageId: ERROR_GRAPHICS_CHAINLINKS_NOT_STARTED
#
# MessageText:
#
# An attempt was made to start a lead link display adapter when the chain links were not started yet.
#
ERROR_GRAPHICS_CHAINLINKS_NOT_STARTED = 0xC0262434

#
# MessageId: ERROR_GRAPHICS_CHAINLINKS_NOT_POWERED_ON
#
# MessageText:
#
# An attempt was made to power up a lead link display adapter when the chain links were powered down.
#
ERROR_GRAPHICS_CHAINLINKS_NOT_POWERED_ON = 0xC0262435

#
# MessageId: ERROR_GRAPHICS_INCONSISTENT_DEVICE_LINK_STATE
#
# MessageText:
#
# The adapter link was found to be in an inconsistent state. Not all adapters are in an expected PNP/Power state.
#
ERROR_GRAPHICS_INCONSISTENT_DEVICE_LINK_STATE = 0xC0262436

#
# MessageId: ERROR_GRAPHICS_LEADLINK_START_DEFERRED
#
# MessageText:
#
# Starting the leadlink adapter has been deferred temporarily.
#
ERROR_GRAPHICS_LEADLINK_START_DEFERRED = 0x40262437

#
# MessageId: ERROR_GRAPHICS_NOT_POST_DEVICE_DRIVER
#
# MessageText:
#
# The driver trying to start is not the same as the driver for the POSTed display adapter.
#
ERROR_GRAPHICS_NOT_POST_DEVICE_DRIVER = 0xC0262438

#
# MessageId: ERROR_GRAPHICS_POLLING_TOO_FREQUENTLY
#
# MessageText:
#
# The display adapter is being polled for children too frequently at the same polling level.
#
ERROR_GRAPHICS_POLLING_TOO_FREQUENTLY = 0x40262439

#
# MessageId: ERROR_GRAPHICS_START_DEFERRED
#
# MessageText:
#
# Starting the adapter has been deferred temporarily.
#
ERROR_GRAPHICS_START_DEFERRED = 0x4026243A

#
# MessageId: ERROR_GRAPHICS_ADAPTER_ACCESS_NOT_EXCLUDED
#
# MessageText:
#
# An operation is being attempted that requires the display adapter to be in a quiescent state.
#
ERROR_GRAPHICS_ADAPTER_ACCESS_NOT_EXCLUDED = 0xC026243B

#
# OPM, UAB and PVP specific error codes {0x2500..0x257f}
#
#
# MessageId: ERROR_GRAPHICS_OPM_NOT_SUPPORTED
#
# MessageText:
#
# The driver does not support OPM.
#
ERROR_GRAPHICS_OPM_NOT_SUPPORTED = 0xC0262500

#
# MessageId: ERROR_GRAPHICS_COPP_NOT_SUPPORTED
#
# MessageText:
#
# The driver does not support COPP.
#
ERROR_GRAPHICS_COPP_NOT_SUPPORTED = 0xC0262501

#
# MessageId: ERROR_GRAPHICS_UAB_NOT_SUPPORTED
#
# MessageText:
#
# The driver does not support UAB.
#
ERROR_GRAPHICS_UAB_NOT_SUPPORTED = 0xC0262502

#
# MessageId: ERROR_GRAPHICS_OPM_INVALID_ENCRYPTED_PARAMETERS
#
# MessageText:
#
# The specified encrypted parameters are invalid.
#
ERROR_GRAPHICS_OPM_INVALID_ENCRYPTED_PARAMETERS = 0xC0262503

#
# MessageId: ERROR_GRAPHICS_OPM_NO_VIDEO_OUTPUTS_EXIST
#
# MessageText:
#
# The GDI display device passed to this function does not have any active video outputs.
#
ERROR_GRAPHICS_OPM_NO_VIDEO_OUTPUTS_EXIST = 0xC0262505

#
# MessageId: ERROR_GRAPHICS_OPM_INTERNAL_ERROR
#
# MessageText:
#
# An internal error caused this operation to fail.
#
ERROR_GRAPHICS_OPM_INTERNAL_ERROR = 0xC026250B

#
# MessageId: ERROR_GRAPHICS_OPM_INVALID_HANDLE
#
# MessageText:
#
# The function failed because the caller passed in an invalid OPM user mode handle.
#
ERROR_GRAPHICS_OPM_INVALID_HANDLE = 0xC026250C

#
# MessageId: ERROR_GRAPHICS_PVP_INVALID_CERTIFICATE_LENGTH
#
# MessageText:
#
# A certificate could not be returned because the certificate buffer passed to the function was too small.
#
ERROR_GRAPHICS_PVP_INVALID_CERTIFICATE_LENGTH = 0xC026250E

#
# MessageId: ERROR_GRAPHICS_OPM_SPANNING_MODE_ENABLED
#
# MessageText:
#
# A video output could not be created because the frame buffer is in spanning mode.
#
ERROR_GRAPHICS_OPM_SPANNING_MODE_ENABLED = 0xC026250F

#
# MessageId: ERROR_GRAPHICS_OPM_THEATER_MODE_ENABLED
#
# MessageText:
#
# A video output could not be created because the frame buffer is in theater mode.
#
ERROR_GRAPHICS_OPM_THEATER_MODE_ENABLED = 0xC0262510

#
# MessageId: ERROR_GRAPHICS_PVP_HFS_FAILED
#
# MessageText:
#
# The function failed because the display adapter's Hardware Functionality Scan failed to validate the graphics hardware.
#
ERROR_GRAPHICS_PVP_HFS_FAILED = 0xC0262511

#
# MessageId: ERROR_GRAPHICS_OPM_INVALID_SRM
#
# MessageText:
#
# The HDCP System Renewability Message passed to this function did not comply with section 5 of the HDCP 1.1 specification.
#
ERROR_GRAPHICS_OPM_INVALID_SRM = 0xC0262512

#
# MessageId: ERROR_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_HDCP
#
# MessageText:
#
# The video output cannot enable the High-bandwidth Digital Content Protection (HDCP) System because it does not support HDCP.
#
ERROR_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_HDCP = 0xC0262513

#
# MessageId: ERROR_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_ACP
#
# MessageText:
#
# The video output cannot enable Analogue Copy Protection (ACP) because it does not support ACP.
#
ERROR_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_ACP = 0xC0262514

#
# MessageId: ERROR_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_CGMSA
#
# MessageText:
#
# The video output cannot enable the Content Generation Management System Analogue (CGMS-A) protection technology because it does not support CGMS-A.
#
ERROR_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_CGMSA = 0xC0262515

#
# MessageId: ERROR_GRAPHICS_OPM_HDCP_SRM_NEVER_SET
#
# MessageText:
#
# The IOPMVideoOutput::GetInformation method cannot return the version of the SRM being used because the application never successfully passed an SRM to the video output.
#
ERROR_GRAPHICS_OPM_HDCP_SRM_NEVER_SET = 0xC0262516

#
# MessageId: ERROR_GRAPHICS_OPM_RESOLUTION_TOO_HIGH
#
# MessageText:
#
# The IOPMVideoOutput::Configure method cannot enable the specified output protection technology because the output's screen resolution is too high.
#
ERROR_GRAPHICS_OPM_RESOLUTION_TOO_HIGH = 0xC0262517

#
# MessageId: ERROR_GRAPHICS_OPM_ALL_HDCP_HARDWARE_ALREADY_IN_USE
#
# MessageText:
#
# The IOPMVideoOutput::Configure method cannot enable HDCP because the display adapter's HDCP hardware is already being used by other physical outputs.
#
ERROR_GRAPHICS_OPM_ALL_HDCP_HARDWARE_ALREADY_IN_USE = 0xC0262518

#
# MessageId: ERROR_GRAPHICS_OPM_VIDEO_OUTPUT_NO_LONGER_EXISTS
#
# MessageText:
#
# The operating system asynchronously destroyed this OPM video output because the operating system's state changed. This error typically occurs because the monitor PDO associated with this video output was removed, the monitor PDO associated with this video output was stopped, the video output's session became a non-console session or the video output's desktop became an inactive desktop.
#
ERROR_GRAPHICS_OPM_VIDEO_OUTPUT_NO_LONGER_EXISTS = 0xC026251A

#
# MessageId: ERROR_GRAPHICS_OPM_SESSION_TYPE_CHANGE_IN_PROGRESS
#
# MessageText:
#
# The method failed because the session is changing its type. No IOPMVideoOutput methods can be called when a session is changing its type. There are currently three types of sessions: console, disconnected and remote.
#
ERROR_GRAPHICS_OPM_SESSION_TYPE_CHANGE_IN_PROGRESS = 0xC026251B

#
# MessageId: ERROR_GRAPHICS_OPM_VIDEO_OUTPUT_DOES_NOT_HAVE_COPP_SEMANTICS
#
# MessageText:
#
# Either the IOPMVideoOutput::COPPCompatibleGetInformation, IOPMVideoOutput::GetInformation, or IOPMVideoOutput::Configure method failed. This error is returned when the caller tries to use a COPP specific command while the video output has OPM semantics only.
#
ERROR_GRAPHICS_OPM_VIDEO_OUTPUT_DOES_NOT_HAVE_COPP_SEMANTICS = 0xC026251C

#
# MessageId: ERROR_GRAPHICS_OPM_INVALID_INFORMATION_REQUEST
#
# MessageText:
#
# The IOPMVideoOutput::GetInformation and IOPMVideoOutput::COPPCompatibleGetInformation methods return this error if the passed in sequence number is not the expected sequence number or the passed in OMAC value is invalid.
#
ERROR_GRAPHICS_OPM_INVALID_INFORMATION_REQUEST = 0xC026251D

#
# MessageId: ERROR_GRAPHICS_OPM_DRIVER_INTERNAL_ERROR
#
# MessageText:
#
# The method failed because an unexpected error occurred inside of a display driver.
#
ERROR_GRAPHICS_OPM_DRIVER_INTERNAL_ERROR = 0xC026251E

#
# MessageId: ERROR_GRAPHICS_OPM_VIDEO_OUTPUT_DOES_NOT_HAVE_OPM_SEMANTICS
#
# MessageText:
#
# Either the IOPMVideoOutput::COPPCompatibleGetInformation, IOPMVideoOutput::GetInformation, or IOPMVideoOutput::Configure method failed. This error is returned when the caller tries to use an OPM specific command while the video output has COPP semantics only.
#
ERROR_GRAPHICS_OPM_VIDEO_OUTPUT_DOES_NOT_HAVE_OPM_SEMANTICS = 0xC026251F

#
# MessageId: ERROR_GRAPHICS_OPM_SIGNALING_NOT_SUPPORTED
#
# MessageText:
#
# The IOPMVideoOutput::COPPCompatibleGetInformation or IOPMVideoOutput::Configure method failed because the display driver does not support the OPM_GET_ACP_AND_CGMSA_SIGNALING and OPM_SET_ACP_AND_CGMSA_SIGNALING GUIDs.
#
ERROR_GRAPHICS_OPM_SIGNALING_NOT_SUPPORTED = 0xC0262520

#
# MessageId: ERROR_GRAPHICS_OPM_INVALID_CONFIGURATION_REQUEST
#
# MessageText:
#
# The IOPMVideoOutput::Configure function returns this error code if the passed in sequence number is not the expected sequence number or the passed in OMAC value is invalid.
#
ERROR_GRAPHICS_OPM_INVALID_CONFIGURATION_REQUEST = 0xC0262521

#
# Monitor Configuration API error codes {0x2580..0x25DF}
#
#
# MessageId: ERROR_GRAPHICS_I2C_NOT_SUPPORTED
#
# MessageText:
#
# The monitor connected to the specified video output does not have an I2C bus.
#
ERROR_GRAPHICS_I = 2

#
# MessageId: ERROR_GRAPHICS_I2C_DEVICE_DOES_NOT_EXIST
#
# MessageText:
#
# No device on the I2C bus has the specified address.
#
ERROR_GRAPHICS_I = 2

#
# MessageId: ERROR_GRAPHICS_I2C_ERROR_TRANSMITTING_DATA
#
# MessageText:
#
# An error occurred while transmitting data to the device on the I2C bus.
#
ERROR_GRAPHICS_I = 2

#
# MessageId: ERROR_GRAPHICS_I2C_ERROR_RECEIVING_DATA
#
# MessageText:
#
# An error occurred while receiving data from the device on the I2C bus.
#
ERROR_GRAPHICS_I = 2

#
# MessageId: ERROR_GRAPHICS_DDCCI_VCP_NOT_SUPPORTED
#
# MessageText:
#
# The monitor does not support the specified VCP code.
#
ERROR_GRAPHICS_DDCCI_VCP_NOT_SUPPORTED = 0xC0262584

#
# MessageId: ERROR_GRAPHICS_DDCCI_INVALID_DATA
#
# MessageText:
#
# The data received from the monitor is invalid.
#
ERROR_GRAPHICS_DDCCI_INVALID_DATA = 0xC0262585

#
# MessageId: ERROR_GRAPHICS_DDCCI_MONITOR_RETURNED_INVALID_TIMING_STATUS_BYTE
#
# MessageText:
#
# The function failed because a monitor returned an invalid Timing Status byte when the operating system used the DDC/CI Get Timing Report & Timing Message command to get a timing report from a monitor.
#
ERROR_GRAPHICS_DDCCI_MONITOR_RETURNED_INVALID_TIMING_STATUS_BYTE = 0xC0262586

#
# MessageId: ERROR_GRAPHICS_MCA_INVALID_CAPABILITIES_STRING
#
# MessageText:
#
# The monitor returned a DDC/CI capabilities string which did not comply with the ACCESS.bus 3.0, DDC/CI 1.1, or MCCS 2 Revision 1 specification.
#
ERROR_GRAPHICS_MCA_INVALID_CAPABILITIES_STRING = 0xC0262587

#
# MessageId: ERROR_GRAPHICS_MCA_INTERNAL_ERROR
#
# MessageText:
#
# An internal Monitor Configuration API error occurred.
#
ERROR_GRAPHICS_MCA_INTERNAL_ERROR = 0xC0262588

#
# MessageId: ERROR_GRAPHICS_DDCCI_INVALID_MESSAGE_COMMAND
#
# MessageText:
#
# An operation failed because a DDC/CI message had an invalid value in its command field.
#
ERROR_GRAPHICS_DDCCI_INVALID_MESSAGE_COMMAND = 0xC0262589

#
# MessageId: ERROR_GRAPHICS_DDCCI_INVALID_MESSAGE_LENGTH
#
# MessageText:
#
# An error occurred because the field length of a DDC/CI message contained an invalid value.
#
ERROR_GRAPHICS_DDCCI_INVALID_MESSAGE_LENGTH = 0xC026258A

#
# MessageId: ERROR_GRAPHICS_DDCCI_INVALID_MESSAGE_CHECKSUM
#
# MessageText:
#
# An error occurred because the checksum field in a DDC/CI message did not match the message's computed checksum value. This error implies that the data was corrupted while it was being transmitted from a monitor to a computer.
#
ERROR_GRAPHICS_DDCCI_INVALID_MESSAGE_CHECKSUM = 0xC026258B

#
# MessageId: ERROR_GRAPHICS_INVALID_PHYSICAL_MONITOR_HANDLE
#
# MessageText:
#
# This function failed because an invalid monitor handle was passed to it.
#
ERROR_GRAPHICS_INVALID_PHYSICAL_MONITOR_HANDLE = 0xC026258C

#
# MessageId: ERROR_GRAPHICS_MONITOR_NO_LONGER_EXISTS
#
# MessageText:
#
# The operating system asynchronously destroyed the monitor which corresponds to this handle because the operating system's state changed. This error typically occurs because the monitor PDO associated with this handle was removed, the monitor PDO associated with this handle was stopped, or a display mode change occurred. A display mode change occurs when windows sends a WM_DISPLAYCHANGE windows message to applications.
#
ERROR_GRAPHICS_MONITOR_NO_LONGER_EXISTS = 0xC026258D

#
# MessageId: ERROR_GRAPHICS_DDCCI_CURRENT_CURRENT_VALUE_GREATER_THAN_MAXIMUM_VALUE
#
# MessageText:
#
# A continuous VCP code's current value is greater than its maximum value. This error code indicates that a monitor returned an invalid value.
#
ERROR_GRAPHICS_DDCCI_CURRENT_CURRENT_VALUE_GREATER_THAN_MAXIMUM_VALUE = 0xC02625D8

#
# MessageId: ERROR_GRAPHICS_MCA_INVALID_VCP_VERSION
#
# MessageText:
#
# The monitor's VCP Version (0xDF) VCP code returned an invalid version value.
#
ERROR_GRAPHICS_MCA_INVALID_VCP_VERSION = 0xC02625D9

#
# MessageId: ERROR_GRAPHICS_MCA_MONITOR_VIOLATES_MCCS_SPECIFICATION
#
# MessageText:
#
# The monitor does not comply with the MCCS specification it claims to support.
#
ERROR_GRAPHICS_MCA_MONITOR_VIOLATES_MCCS_SPECIFICATION = 0xC02625DA

#
# MessageId: ERROR_GRAPHICS_MCA_MCCS_VERSION_MISMATCH
#
# MessageText:
#
# The MCCS version in a monitor's mccs_ver capability does not match the MCCS version the monitor reports when the VCP Version (0xDF) VCP code is used.
#
ERROR_GRAPHICS_MCA_MCCS_VERSION_MISMATCH = 0xC02625DB

#
# MessageId: ERROR_GRAPHICS_MCA_UNSUPPORTED_MCCS_VERSION
#
# MessageText:
#
# The Monitor Configuration API only works with monitors which support the MCCS 1.0 specification, MCCS 2.0 specification or the MCCS 2.0 Revision 1 specification.
#
ERROR_GRAPHICS_MCA_UNSUPPORTED_MCCS_VERSION = 0xC02625DC

#
# MessageId: ERROR_GRAPHICS_MCA_INVALID_TECHNOLOGY_TYPE_RETURNED
#
# MessageText:
#
# The monitor returned an invalid monitor technology type. CRT, Plasma and LCD (TFT) are examples of monitor technology types. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.
#
ERROR_GRAPHICS_MCA_INVALID_TECHNOLOGY_TYPE_RETURNED = 0xC02625DE

#
# MessageId: ERROR_GRAPHICS_MCA_UNSUPPORTED_COLOR_TEMPERATURE
#
# MessageText:
#
# SetMonitorColorTemperature()'s caller passed a color temperature to it which the current monitor did not support. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.
#
ERROR_GRAPHICS_MCA_UNSUPPORTED_COLOR_TEMPERATURE = 0xC02625DF

#
# OPM, UAB, PVP and DDC/CI shared error codes {0x25E0..0x25ff}
#
#
# MessageId: ERROR_GRAPHICS_ONLY_CONSOLE_SESSION_SUPPORTED
#
# MessageText:
#
# This function can only be used if a program is running in the local console session. It cannot be used if the program is running on a remote desktop session or on a terminal server session.
#
ERROR_GRAPHICS_ONLY_CONSOLE_SESSION_SUPPORTED = 0xC02625E0

#
# MessageId: ERROR_GRAPHICS_NO_DISPLAY_DEVICE_CORRESPONDS_TO_NAME
#
# MessageText:
#
# This function cannot find an actual GDI display device which corresponds to the specified GDI display device name.
#
ERROR_GRAPHICS_NO_DISPLAY_DEVICE_CORRESPONDS_TO_NAME = 0xC02625E1

#
# MessageId: ERROR_GRAPHICS_DISPLAY_DEVICE_NOT_ATTACHED_TO_DESKTOP
#
# MessageText:
#
# The function failed because the specified GDI display device was not attached to the Windows desktop.
#
ERROR_GRAPHICS_DISPLAY_DEVICE_NOT_ATTACHED_TO_DESKTOP = 0xC02625E2

#
# MessageId: ERROR_GRAPHICS_MIRRORING_DEVICES_NOT_SUPPORTED
#
# MessageText:
#
# This function does not support GDI mirroring display devices because GDI mirroring display devices do not have any physical monitors associated with them.
#
ERROR_GRAPHICS_MIRRORING_DEVICES_NOT_SUPPORTED = 0xC02625E3

#
# MessageId: ERROR_GRAPHICS_INVALID_POINTER
#
# MessageText:
#
# The function failed because an invalid pointer parameter was passed to it. A pointer parameter is invalid if it is NULL, points to an invalid address, points to a kernel mode address, or is not correctly aligned.
#
ERROR_GRAPHICS_INVALID_POINTER = 0xC02625E4

#
# MessageId: ERROR_GRAPHICS_NO_MONITORS_CORRESPOND_TO_DISPLAY_DEVICE
#
# MessageText:
#
# The function failed because the specified GDI device did not have any monitors associated with it.
#
ERROR_GRAPHICS_NO_MONITORS_CORRESPOND_TO_DISPLAY_DEVICE = 0xC02625E5

#
# MessageId: ERROR_GRAPHICS_PARAMETER_ARRAY_TOO_SMALL
#
# MessageText:
#
# An array passed to the function cannot hold all of the data that the function must copy into the array.
#
ERROR_GRAPHICS_PARAMETER_ARRAY_TOO_SMALL = 0xC02625E6

#
# MessageId: ERROR_GRAPHICS_INTERNAL_ERROR
#
# MessageText:
#
# An internal error caused an operation to fail.
#
ERROR_GRAPHICS_INTERNAL_ERROR = 0xC02625E7

#
# MessageId: ERROR_GRAPHICS_SESSION_TYPE_CHANGE_IN_PROGRESS
#
# MessageText:
#
# The function failed because the current session is changing its type. This function cannot be called when the current session is changing its type. There are currently three types of sessions: console, disconnected and remote.
#
ERROR_GRAPHICS_SESSION_TYPE_CHANGE_IN_PROGRESS = 0xC02605E8


# FACILITY_NAP

#
# MessageId: NAP_E_INVALID_PACKET
#
# MessageText:
#
# The NAP SoH packet is invalid.
#
NAP_E_INVALID_PACKET = 0x80270001

#
# MessageId: NAP_E_MISSING_SOH
#
# MessageText:
#
# An SoH was missing from the NAP packet.
#
NAP_E_MISSING_SOH = 0x80270002

#
# MessageId: NAP_E_CONFLICTING_ID
#
# MessageText:
#
# The entity ID conflicts with an already registered id.
#
NAP_E_CONFLICTING_ID = 0x80270003

#
# MessageId: NAP_E_NO_CACHED_SOH
#
# MessageText:
#
# No cached SoH is present.
#
NAP_E_NO_CACHED_SOH = 0x80270004

#
# MessageId: NAP_E_STILL_BOUND
#
# MessageText:
#
# The entity is still bound to the NAP system.
#
NAP_E_STILL_BOUND = 0x80270005

#
# MessageId: NAP_E_NOT_REGISTERED
#
# MessageText:
#
# The entity is not registered with the NAP system.
#
NAP_E_NOT_REGISTERED = 0x80270006

#
# MessageId: NAP_E_NOT_INITIALIZED
#
# MessageText:
#
# The entity is not initialized with the NAP system.
#
NAP_E_NOT_INITIALIZED = 0x80270007

#
# MessageId: NAP_E_MISMATCHED_ID
#
# MessageText:
#
# The correlation id in the SoH-Request and SoH-Response do not match up.
#
NAP_E_MISMATCHED_ID = 0x80270008

#
# MessageId: NAP_E_NOT_PENDING
#
# MessageText:
#
# Completion was indicated on a request that is not currently pending.
#
NAP_E_NOT_PENDING = 0x80270009

#
# MessageId: NAP_E_ID_NOT_FOUND
#
# MessageText:
#
# The NAP component's id was not found.
#
NAP_E_ID_NOT_FOUND = 0x8027000A

#
# MessageId: NAP_E_MAXSIZE_TOO_SMALL
#
# MessageText:
#
# The maximum size of the connection is too small for an SoH packet.
#
NAP_E_MAXSIZE_TOO_SMALL = 0x8027000B

#
# MessageId: NAP_E_SERVICE_NOT_RUNNING
#
# MessageText:
#
# The NapAgent service is not running.
#
NAP_E_SERVICE_NOT_RUNNING = 0x8027000C

#
# MessageId: NAP_S_CERT_ALREADY_PRESENT
#
# MessageText:
#
# A certificate is already present in the cert store.
#
NAP_S_CERT_ALREADY_PRESENT = 0x0027000D

#
# MessageId: NAP_E_ENTITY_DISABLED
#
# MessageText:
#
# The entity is disabled with the NapAgent service.
#
NAP_E_ENTITY_DISABLED = 0x8027000E

#
# MessageId: NAP_E_NETSH_GROUPPOLICY_ERROR
#
# MessageText:
#
# Group Policy is not configured.
#
NAP_E_NETSH_GROUPPOLICY_ERROR = 0x8027000F

#
# MessageId: NAP_E_TOO_MANY_CALLS
#
# MessageText:
#
# Too many simultaneous calls.
#
NAP_E_TOO_MANY_CALLS = 0x80270010

#
# MessageId: NAP_E_SHV_CONFIG_EXISTED
#
# MessageText:
#
# SHV configuration already existed.
#
NAP_E_SHV_CONFIG_EXISTED = 0x80270011

#
# MessageId: NAP_E_SHV_CONFIG_NOT_FOUND
#
# MessageText:
#
# SHV configuration is not found.
#
NAP_E_SHV_CONFIG_NOT_FOUND = 0x80270012

#
# MessageId: NAP_E_SHV_TIMEOUT
#
# MessageText:
#
# SHV timed out on the request.
#
NAP_E_SHV_TIMEOUT = 0x80270013

#
# ===============================
# TPM Services and TPM Software Error Messages
# ===============================
#
# The TPM services and TPM software facilities are used by the various
# TPM software components. There are two facilities because the services
# errors are within the TCG-defined error space and the software errors
# are not.
#
# The following are the subranges within the TPM Services facility.
# The TPM hardware errors are defined in the document
# TPM Main Specification 1.2 Part 2 TPM Structures.
# The TBS errors are slotted into the TCG error namespace at the TBS layer.
#
# 0x0000 - 0x08ff     TPM hardware errors
# 0x4000 - 0x40ff     TPM Base Services errors (tbssvc.dll)
#
# The following are the subranges within the TPM Software facility. The TBS
# has two classes of errors - those that can be returned (the public errors,
# defined in the TBS spec), which are in the TPM services facility,  and
# those that are internal or implementation specific, which are here in the
# TPM software facility.
#
# 0x0000 - 0x00ff     TPM device driver errors (tpm.sys)
# 0x0100 - 0x01ff     TPM API errors (tpmapi.lib)
# 0x0200 - 0x02ff     TBS internal errors (tbssvc.dll)
# 0x0300 - 0x03ff     TPM Physical Presence errors
#
#
# TPM hardware error codes {0x0000..0x08ff}
# This space is further subdivided into hardware errors, vendor-specific
# errors, and non-fatal errors.
#
#
# TPM hardware errors {0x0000..0x003ff}
#
#
# MessageId: TPM_E_ERROR_MASK
#
# MessageText:
#
# This is an error mask to convert TPM hardware errors to win errors.
#
TPM_E_ERROR_MASK = 0x80280000

#
# MessageId: TPM_E_AUTHFAIL
#
# MessageText:
#
# Authentication failed.
#
TPM_E_AUTHFAIL = 0x80280001

#
# MessageId: TPM_E_BADINDEX
#
# MessageText:
#
# The index to a PCR, DIR or other register is incorrect.
#
TPM_E_BADINDEX = 0x80280002

#
# MessageId: TPM_E_BAD_PARAMETER
#
# MessageText:
#
# One or more parameter is bad.
#
TPM_E_BAD_PARAMETER = 0x80280003

#
# MessageId: TPM_E_AUDITFAILURE
#
# MessageText:
#
# An operation completed successfully but the auditing of that operation failed.
#
TPM_E_AUDITFAILURE = 0x80280004

#
# MessageId: TPM_E_CLEAR_DISABLED
#
# MessageText:
#
# The clear disable flag is set and all clear operations now require physical access.
#
TPM_E_CLEAR_DISABLED = 0x80280005

#
# MessageId: TPM_E_DEACTIVATED
#
# MessageText:
#
# Activate the Trusted Platform Module (TPM).
#
TPM_E_DEACTIVATED = 0x80280006

#
# MessageId: TPM_E_DISABLED
#
# MessageText:
#
# Enable the Trusted Platform Module (TPM).
#
TPM_E_DISABLED = 0x80280007

#
# MessageId: TPM_E_DISABLED_CMD
#
# MessageText:
#
# The target command has been disabled.
#
TPM_E_DISABLED_CMD = 0x80280008

#
# MessageId: TPM_E_FAIL
#
# MessageText:
#
# The operation failed.
#
TPM_E_FAIL = 0x80280009

#
# MessageId: TPM_E_BAD_ORDINAL
#
# MessageText:
#
# The ordinal was unknown or inconsistent.
#
TPM_E_BAD_ORDINAL = 0x8028000A

#
# MessageId: TPM_E_INSTALL_DISABLED
#
# MessageText:
#
# The ability to install an owner is disabled.
#
TPM_E_INSTALL_DISABLED = 0x8028000B

#
# MessageId: TPM_E_INVALID_KEYHANDLE
#
# MessageText:
#
# The key handle cannot be interpreted.
#
TPM_E_INVALID_KEYHANDLE = 0x8028000C

#
# MessageId: TPM_E_KEYNOTFOUND
#
# MessageText:
#
# The key handle points to an invalid key.
#
TPM_E_KEYNOTFOUND = 0x8028000D

#
# MessageId: TPM_E_INAPPROPRIATE_ENC
#
# MessageText:
#
# Unacceptable encryption scheme.
#
TPM_E_INAPPROPRIATE_ENC = 0x8028000E

#
# MessageId: TPM_E_MIGRATEFAIL
#
# MessageText:
#
# Migration authorization failed.
#
TPM_E_MIGRATEFAIL = 0x8028000F

#
# MessageId: TPM_E_INVALID_PCR_INFO
#
# MessageText:
#
# PCR information could not be interpreted.
#
TPM_E_INVALID_PCR_INFO = 0x80280010

#
# MessageId: TPM_E_NOSPACE
#
# MessageText:
#
# No room to load key.
#
TPM_E_NOSPACE = 0x80280011

#
# MessageId: TPM_E_NOSRK
#
# MessageText:
#
# There is no Storage Root Key (SRK) set.
#
TPM_E_NOSRK = 0x80280012

#
# MessageId: TPM_E_NOTSEALED_BLOB
#
# MessageText:
#
# An encrypted blob is invalid or was not created by this TPM.
#
TPM_E_NOTSEALED_BLOB = 0x80280013

#
# MessageId: TPM_E_OWNER_SET
#
# MessageText:
#
# The Trusted Platform Module (TPM) already has an owner.
#
TPM_E_OWNER_SET = 0x80280014

#
# MessageId: TPM_E_RESOURCES
#
# MessageText:
#
# The TPM has insufficient internal resources to perform the requested action.
#
TPM_E_RESOURCES = 0x80280015

#
# MessageId: TPM_E_SHORTRANDOM
#
# MessageText:
#
# A random string was too short.
#
TPM_E_SHORTRANDOM = 0x80280016

#
# MessageId: TPM_E_SIZE
#
# MessageText:
#
# The TPM does not have the space to perform the operation.
#
TPM_E_SIZE = 0x80280017

#
# MessageId: TPM_E_WRONGPCRVAL
#
# MessageText:
#
# The named PCR value does not match the current PCR value.
#
TPM_E_WRONGPCRVAL = 0x80280018

#
# MessageId: TPM_E_BAD_PARAM_SIZE
#
# MessageText:
#
# The paramSize argument to the command has the incorrect value .
#
TPM_E_BAD_PARAM_SIZE = 0x80280019

#
# MessageId: TPM_E_SHA_THREAD
#
# MessageText:
#
# There is no existing SHA-1 thread.
#
TPM_E_SHA_THREAD = 0x8028001A

#
# MessageId: TPM_E_SHA_ERROR
#
# MessageText:
#
# The calculation is unable to proceed because the existing SHA-1 thread has already encountered an error.
#
TPM_E_SHA_ERROR = 0x8028001B

#
# MessageId: TPM_E_FAILEDSELFTEST
#
# MessageText:
#
# The TPM hardware device reported a failure during its internal self test. Try restarting the computer to resolve the problem. If the problem continues, check for the latest BIOS or firmware update for your TPM hardware. Consult the computer manufacturer's documentation for instructions.
#
TPM_E_FAILEDSELFTEST = 0x8028001C

#
# MessageId: TPM_E_AUTH2FAIL
#
# MessageText:
#
# The authorization for the second key in a 2 key function failed authorization.
#
TPM_E_AUTH = 2

#
# MessageId: TPM_E_BADTAG
#
# MessageText:
#
# The tag value sent to for a command is invalid.
#
TPM_E_BADTAG = 0x8028001E

#
# MessageId: TPM_E_IOERROR
#
# MessageText:
#
# An IO error occurred transmitting information to the TPM.
#
TPM_E_IOERROR = 0x8028001F

#
# MessageId: TPM_E_ENCRYPT_ERROR
#
# MessageText:
#
# The encryption process had a problem.
#
TPM_E_ENCRYPT_ERROR = 0x80280020

#
# MessageId: TPM_E_DECRYPT_ERROR
#
# MessageText:
#
# The decryption process did not complete.
#
TPM_E_DECRYPT_ERROR = 0x80280021

#
# MessageId: TPM_E_INVALID_AUTHHANDLE
#
# MessageText:
#
# An invalid handle was used.
#
TPM_E_INVALID_AUTHHANDLE = 0x80280022

#
# MessageId: TPM_E_NO_ENDORSEMENT
#
# MessageText:
#
# The TPM does not have an Endorsement Key (EK) installed.
#
TPM_E_NO_ENDORSEMENT = 0x80280023

#
# MessageId: TPM_E_INVALID_KEYUSAGE
#
# MessageText:
#
# The usage of a key is not allowed.
#
TPM_E_INVALID_KEYUSAGE = 0x80280024

#
# MessageId: TPM_E_WRONG_ENTITYTYPE
#
# MessageText:
#
# The submitted entity type is not allowed.
#
TPM_E_WRONG_ENTITYTYPE = 0x80280025

#
# MessageId: TPM_E_INVALID_POSTINIT
#
# MessageText:
#
# The command was received in the wrong sequence relative to TPM_Init and a subsequent TPM_Startup.
#
TPM_E_INVALID_POSTINIT = 0x80280026

#
# MessageId: TPM_E_INAPPROPRIATE_SIG
#
# MessageText:
#
# Signed data cannot include additional DER information.
#
TPM_E_INAPPROPRIATE_SIG = 0x80280027

#
# MessageId: TPM_E_BAD_KEY_PROPERTY
#
# MessageText:
#
# The key properties in TPM_KEY_PARMs are not supported by this TPM.
#
TPM_E_BAD_KEY_PROPERTY = 0x80280028

#
# MessageId: TPM_E_BAD_MIGRATION
#
# MessageText:
#
# The migration properties of this key are incorrect.
#
TPM_E_BAD_MIGRATION = 0x80280029

#
# MessageId: TPM_E_BAD_SCHEME
#
# MessageText:
#
# The signature or encryption scheme for this key is incorrect or not permitted in this situation.
#
TPM_E_BAD_SCHEME = 0x8028002A

#
# MessageId: TPM_E_BAD_DATASIZE
#
# MessageText:
#
# The size of the data (or blob) parameter is bad or inconsistent with the referenced key.
#
TPM_E_BAD_DATASIZE = 0x8028002B

#
# MessageId: TPM_E_BAD_MODE
#
# MessageText:
#
# A mode parameter is bad, such as capArea or subCapArea for TPM_GetCapability, phsicalPresence parameter for TPM_PhysicalPresence, or migrationType for TPM_CreateMigrationBlob.
#
TPM_E_BAD_MODE = 0x8028002C

#
# MessageId: TPM_E_BAD_PRESENCE
#
# MessageText:
#
# Either the physicalPresence or physicalPresenceLock bits have the wrong value.
#
TPM_E_BAD_PRESENCE = 0x8028002D

#
# MessageId: TPM_E_BAD_VERSION
#
# MessageText:
#
# The TPM cannot perform this version of the capability.
#
TPM_E_BAD_VERSION = 0x8028002E

#
# MessageId: TPM_E_NO_WRAP_TRANSPORT
#
# MessageText:
#
# The TPM does not allow for wrapped transport sessions.
#
TPM_E_NO_WRAP_TRANSPORT = 0x8028002F

#
# MessageId: TPM_E_AUDITFAIL_UNSUCCESSFUL
#
# MessageText:
#
# TPM audit construction failed and the underlying command was returning a failure code also.
#
TPM_E_AUDITFAIL_UNSUCCESSFUL = 0x80280030

#
# MessageId: TPM_E_AUDITFAIL_SUCCESSFUL
#
# MessageText:
#
# TPM audit construction failed and the underlying command was returning success.
#
TPM_E_AUDITFAIL_SUCCESSFUL = 0x80280031

#
# MessageId: TPM_E_NOTRESETABLE
#
# MessageText:
#
# Attempt to reset a PCR register that does not have the resettable attribute.
#
TPM_E_NOTRESETABLE = 0x80280032

#
# MessageId: TPM_E_NOTLOCAL
#
# MessageText:
#
# Attempt to reset a PCR register that requires locality and locality modifier not part of command transport.
#
TPM_E_NOTLOCAL = 0x80280033

#
# MessageId: TPM_E_BAD_TYPE
#
# MessageText:
#
# Make identity blob not properly typed.
#
TPM_E_BAD_TYPE = 0x80280034

#
# MessageId: TPM_E_INVALID_RESOURCE
#
# MessageText:
#
# When saving context identified resource type does not match actual resource.
#
TPM_E_INVALID_RESOURCE = 0x80280035

#
# MessageId: TPM_E_NOTFIPS
#
# MessageText:
#
# The TPM is attempting to execute a command only available when in FIPS mode.
#
TPM_E_NOTFIPS = 0x80280036

#
# MessageId: TPM_E_INVALID_FAMILY
#
# MessageText:
#
# The command is attempting to use an invalid family ID.
#
TPM_E_INVALID_FAMILY = 0x80280037

#
# MessageId: TPM_E_NO_NV_PERMISSION
#
# MessageText:
#
# The permission to manipulate the NV storage is not available.
#
TPM_E_NO_NV_PERMISSION = 0x80280038

#
# MessageId: TPM_E_REQUIRES_SIGN
#
# MessageText:
#
# The operation requires a signed command.
#
TPM_E_REQUIRES_SIGN = 0x80280039

#
# MessageId: TPM_E_KEY_NOTSUPPORTED
#
# MessageText:
#
# Wrong operation to load an NV key.
#
TPM_E_KEY_NOTSUPPORTED = 0x8028003A

#
# MessageId: TPM_E_AUTH_CONFLICT
#
# MessageText:
#
# NV_LoadKey blob requires both owner and blob authorization.
#
TPM_E_AUTH_CONFLICT = 0x8028003B

#
# MessageId: TPM_E_AREA_LOCKED
#
# MessageText:
#
# The NV area is locked and not writtable.
#
TPM_E_AREA_LOCKED = 0x8028003C

#
# MessageId: TPM_E_BAD_LOCALITY
#
# MessageText:
#
# The locality is incorrect for the attempted operation.
#
TPM_E_BAD_LOCALITY = 0x8028003D

#
# MessageId: TPM_E_READ_ONLY
#
# MessageText:
#
# The NV area is read only and can't be written to.
#
TPM_E_READ_ONLY = 0x8028003E

#
# MessageId: TPM_E_PER_NOWRITE
#
# MessageText:
#
# There is no protection on the write to the NV area.
#
TPM_E_PER_NOWRITE = 0x8028003F

#
# MessageId: TPM_E_FAMILYCOUNT
#
# MessageText:
#
# The family count value does not match.
#
TPM_E_FAMILYCOUNT = 0x80280040

#
# MessageId: TPM_E_WRITE_LOCKED
#
# MessageText:
#
# The NV area has already been written to.
#
TPM_E_WRITE_LOCKED = 0x80280041

#
# MessageId: TPM_E_BAD_ATTRIBUTES
#
# MessageText:
#
# The NV area attributes conflict.
#
TPM_E_BAD_ATTRIBUTES = 0x80280042

#
# MessageId: TPM_E_INVALID_STRUCTURE
#
# MessageText:
#
# The structure tag and version are invalid or inconsistent.
#
TPM_E_INVALID_STRUCTURE = 0x80280043

#
# MessageId: TPM_E_KEY_OWNER_CONTROL
#
# MessageText:
#
# The key is under control of the TPM Owner and can only be evicted by the TPM Owner.
#
TPM_E_KEY_OWNER_CONTROL = 0x80280044

#
# MessageId: TPM_E_BAD_COUNTER
#
# MessageText:
#
# The counter handle is incorrect.
#
TPM_E_BAD_COUNTER = 0x80280045

#
# MessageId: TPM_E_NOT_FULLWRITE
#
# MessageText:
#
# The write is not a complete write of the area.
#
TPM_E_NOT_FULLWRITE = 0x80280046

#
# MessageId: TPM_E_CONTEXT_GAP
#
# MessageText:
#
# The gap between saved context counts is too large.
#
TPM_E_CONTEXT_GAP = 0x80280047

#
# MessageId: TPM_E_MAXNVWRITES
#
# MessageText:
#
# The maximum number of NV writes without an owner has been exceeded.
#
TPM_E_MAXNVWRITES = 0x80280048

#
# MessageId: TPM_E_NOOPERATOR
#
# MessageText:
#
# No operator AuthData value is set.
#
TPM_E_NOOPERATOR = 0x80280049

#
# MessageId: TPM_E_RESOURCEMISSING
#
# MessageText:
#
# The resource pointed to by context is not loaded.
#
TPM_E_RESOURCEMISSING = 0x8028004A

#
# MessageId: TPM_E_DELEGATE_LOCK
#
# MessageText:
#
# The delegate administration is locked.
#
TPM_E_DELEGATE_LOCK = 0x8028004B

#
# MessageId: TPM_E_DELEGATE_FAMILY
#
# MessageText:
#
# Attempt to manage a family other then the delegated family.
#
TPM_E_DELEGATE_FAMILY = 0x8028004C

#
# MessageId: TPM_E_DELEGATE_ADMIN
#
# MessageText:
#
# Delegation table management not enabled.
#
TPM_E_DELEGATE_ADMIN = 0x8028004D

#
# MessageId: TPM_E_TRANSPORT_NOTEXCLUSIVE
#
# MessageText:
#
# There was a command executed outside of an exclusive transport session.
#
TPM_E_TRANSPORT_NOTEXCLUSIVE = 0x8028004E

#
# MessageId: TPM_E_OWNER_CONTROL
#
# MessageText:
#
# Attempt to context save a owner evict controlled key.
#
TPM_E_OWNER_CONTROL = 0x8028004F

#
# MessageId: TPM_E_DAA_RESOURCES
#
# MessageText:
#
# The DAA command has no resources availble to execute the command.
#
TPM_E_DAA_RESOURCES = 0x80280050

#
# MessageId: TPM_E_DAA_INPUT_DATA0
#
# MessageText:
#
# The consistency check on DAA parameter inputData0 has failed.
#
TPM_E_DAA_INPUT_DATA = 0

#
# MessageId: TPM_E_DAA_INPUT_DATA1
#
# MessageText:
#
# The consistency check on DAA parameter inputData1 has failed.
#
TPM_E_DAA_INPUT_DATA = 1

#
# MessageId: TPM_E_DAA_ISSUER_SETTINGS
#
# MessageText:
#
# The consistency check on DAA_issuerSettings has failed.
#
TPM_E_DAA_ISSUER_SETTINGS = 0x80280053

#
# MessageId: TPM_E_DAA_TPM_SETTINGS
#
# MessageText:
#
# The consistency check on DAA_tpmSpecific has failed.
#
TPM_E_DAA_TPM_SETTINGS = 0x80280054

#
# MessageId: TPM_E_DAA_STAGE
#
# MessageText:
#
# The atomic process indicated by the submitted DAA command is not the expected process.
#
TPM_E_DAA_STAGE = 0x80280055

#
# MessageId: TPM_E_DAA_ISSUER_VALIDITY
#
# MessageText:
#
# The issuer's validity check has detected an inconsistency.
#
TPM_E_DAA_ISSUER_VALIDITY = 0x80280056

#
# MessageId: TPM_E_DAA_WRONG_W
#
# MessageText:
#
# The consistency check on w has failed.
#
TPM_E_DAA_WRONG_W = 0x80280057

#
# MessageId: TPM_E_BAD_HANDLE
#
# MessageText:
#
# The handle is incorrect.
#
TPM_E_BAD_HANDLE = 0x80280058

#
# MessageId: TPM_E_BAD_DELEGATE
#
# MessageText:
#
# Delegation is not correct.
#
TPM_E_BAD_DELEGATE = 0x80280059

#
# MessageId: TPM_E_BADCONTEXT
#
# MessageText:
#
# The context blob is invalid.
#
TPM_E_BADCONTEXT = 0x8028005A

#
# MessageId: TPM_E_TOOMANYCONTEXTS
#
# MessageText:
#
# Too many contexts held by the TPM.
#
TPM_E_TOOMANYCONTEXTS = 0x8028005B

#
# MessageId: TPM_E_MA_TICKET_SIGNATURE
#
# MessageText:
#
# Migration authority signature validation failure.
#
TPM_E_MA_TICKET_SIGNATURE = 0x8028005C

#
# MessageId: TPM_E_MA_DESTINATION
#
# MessageText:
#
# Migration destination not authenticated.
#
TPM_E_MA_DESTINATION = 0x8028005D

#
# MessageId: TPM_E_MA_SOURCE
#
# MessageText:
#
# Migration source incorrect.
#
TPM_E_MA_SOURCE = 0x8028005E

#
# MessageId: TPM_E_MA_AUTHORITY
#
# MessageText:
#
# Incorrect migration authority.
#
TPM_E_MA_AUTHORITY = 0x8028005F

#
# MessageId: TPM_E_PERMANENTEK
#
# MessageText:
#
# Attempt to revoke the EK and the EK is not revocable.
#
TPM_E_PERMANENTEK = 0x80280061

#
# MessageId: TPM_E_BAD_SIGNATURE
#
# MessageText:
#
# Bad signature of CMK ticket.
#
TPM_E_BAD_SIGNATURE = 0x80280062

#
# MessageId: TPM_E_NOCONTEXTSPACE
#
# MessageText:
#
# There is no room in the context list for additional contexts.
#
TPM_E_NOCONTEXTSPACE = 0x80280063

#
# TPM vendor specific hardware errors {0x0400..0x04ff}
#
#
# MessageId: TPM_E_COMMAND_BLOCKED
#
# MessageText:
#
# The command was blocked.
#
TPM_E_COMMAND_BLOCKED = 0x80280400

#
# MessageId: TPM_E_INVALID_HANDLE
#
# MessageText:
#
# The specified handle was not found.
#
TPM_E_INVALID_HANDLE = 0x80280401

#
# MessageId: TPM_E_DUPLICATE_VHANDLE
#
# MessageText:
#
# The TPM returned a duplicate handle and the command needs to be resubmitted.
#
TPM_E_DUPLICATE_VHANDLE = 0x80280402

#
# MessageId: TPM_E_EMBEDDED_COMMAND_BLOCKED
#
# MessageText:
#
# The command within the transport was blocked.
#
TPM_E_EMBEDDED_COMMAND_BLOCKED = 0x80280403

#
# MessageId: TPM_E_EMBEDDED_COMMAND_UNSUPPORTED
#
# MessageText:
#
# The command within the transport is not supported.
#
TPM_E_EMBEDDED_COMMAND_UNSUPPORTED = 0x80280404

#
# TPM non-fatal hardware errors {0x0800..0x08ff}
#
#
# MessageId: TPM_E_RETRY
#
# MessageText:
#
# The TPM is too busy to respond to the command immediately, but the command could be resubmitted at a later time.
#
TPM_E_RETRY = 0x80280800

#
# MessageId: TPM_E_NEEDS_SELFTEST
#
# MessageText:
#
# SelfTestFull has not been run.
#
TPM_E_NEEDS_SELFTEST = 0x80280801

#
# MessageId: TPM_E_DOING_SELFTEST
#
# MessageText:
#
# The TPM is currently executing a full selftest.
#
TPM_E_DOING_SELFTEST = 0x80280802

#
# MessageId: TPM_E_DEFEND_LOCK_RUNNING
#
# MessageText:
#
# The TPM is defending against dictionary attacks and is in a time-out period.
#
TPM_E_DEFEND_LOCK_RUNNING = 0x80280803

#
# TPM Base Services error codes {0x4000..0x40ff}
#
#
# MessageId: TBS_E_INTERNAL_ERROR
#
# MessageText:
#
# An internal error has occurred within the Trusted Platform Module support program.
#
TBS_E_INTERNAL_ERROR = 0x80284001

#
# MessageId: TBS_E_BAD_PARAMETER
#
# MessageText:
#
# One or more input parameters is bad.
#
TBS_E_BAD_PARAMETER = 0x80284002

#
# MessageId: TBS_E_INVALID_OUTPUT_POINTER
#
# MessageText:
#
# A specified output pointer is bad.
#
TBS_E_INVALID_OUTPUT_POINTER = 0x80284003

#
# MessageId: TBS_E_INVALID_CONTEXT
#
# MessageText:
#
# The specified context handle does not refer to a valid context.
#
TBS_E_INVALID_CONTEXT = 0x80284004

#
# MessageId: TBS_E_INSUFFICIENT_BUFFER
#
# MessageText:
#
# A specified output buffer is too small.
#
TBS_E_INSUFFICIENT_BUFFER = 0x80284005

#
# MessageId: TBS_E_IOERROR
#
# MessageText:
#
# An error occurred while communicating with the TPM.
#
TBS_E_IOERROR = 0x80284006

#
# MessageId: TBS_E_INVALID_CONTEXT_PARAM
#
# MessageText:
#
# One or more context parameters is invalid.
#
TBS_E_INVALID_CONTEXT_PARAM = 0x80284007

#
# MessageId: TBS_E_SERVICE_NOT_RUNNING
#
# MessageText:
#
# The TBS service is not running and could not be started.
#
TBS_E_SERVICE_NOT_RUNNING = 0x80284008

#
# MessageId: TBS_E_TOO_MANY_TBS_CONTEXTS
#
# MessageText:
#
# A new context could not be created because there are too many open contexts.
#
TBS_E_TOO_MANY_TBS_CONTEXTS = 0x80284009

#
# MessageId: TBS_E_TOO_MANY_RESOURCES
#
# MessageText:
#
# A new virtual resource could not be created because there are too many open virtual resources.
#
TBS_E_TOO_MANY_RESOURCES = 0x8028400A

#
# MessageId: TBS_E_SERVICE_START_PENDING
#
# MessageText:
#
# The TBS service has been started but is not yet running.
#
TBS_E_SERVICE_START_PENDING = 0x8028400B

#
# MessageId: TBS_E_PPI_NOT_SUPPORTED
#
# MessageText:
#
# The physical presence interface is not supported.
#
TBS_E_PPI_NOT_SUPPORTED = 0x8028400C

#
# MessageId: TBS_E_COMMAND_CANCELED
#
# MessageText:
#
# The command was canceled.
#
TBS_E_COMMAND_CANCELED = 0x8028400D

#
# MessageId: TBS_E_BUFFER_TOO_LARGE
#
# MessageText:
#
# The input or output buffer is too large.
#
TBS_E_BUFFER_TOO_LARGE = 0x8028400E

#
# MessageId: TBS_E_TPM_NOT_FOUND
#
# MessageText:
#
# A compatible Trusted Platform Module (TPM) Security Device cannot be found on this computer.
#
TBS_E_TPM_NOT_FOUND = 0x8028400F

#
# MessageId: TBS_E_SERVICE_DISABLED
#
# MessageText:
#
# The TBS service has been disabled.
#
TBS_E_SERVICE_DISABLED = 0x80284010

#
# MessageId: TBS_E_NO_EVENT_LOG
#
# MessageText:
#
# No TCG event log is available.
#
TBS_E_NO_EVENT_LOG = 0x80284011

#
# MessageId: TBS_E_ACCESS_DENIED
#
# MessageText:
#
# The caller does not have the appropriate rights to perform the requested operation.
#
TBS_E_ACCESS_DENIED = 0x80284012

#
# MessageId: TBS_E_PROVISIONING_NOT_ALLOWED
#
# MessageText:
#
# The TPM provisioning action is not allowed by the specified flags.  For provisioning to be successful, one of several actions may be required.  The TPM management console (tpm.msc) action to make the TPM Ready may help.  For further information, see the documentation for the Win32_Tpm WMI method 'Provision'.  (The actions that may be required include importing the TPM Owner Authorization value into the system, calling the Win32_Tpm WMI method for provisioning the TPM and specifying TRUE for either 'ForceClear_Allowed' or 'PhysicalPresencePrompts_Allowed' (as indicated by the value returned in the Additional Information), or enabling the TPM in the system BIOS.)
#
TBS_E_PROVISIONING_NOT_ALLOWED = 0x80284013

#
# MessageId: TBS_E_PPI_FUNCTION_UNSUPPORTED
#
# MessageText:
#
# The Physical Presence Interface of this firmware does not support the requested method.
#
TBS_E_PPI_FUNCTION_UNSUPPORTED = 0x80284014

#
# MessageId: TBS_E_OWNERAUTH_NOT_FOUND
#
# MessageText:
#
# The requested TPM OwnerAuth value was not found.
#
TBS_E_OWNERAUTH_NOT_FOUND = 0x80284015

#
# MessageId: TBS_E_PROVISIONING_INCOMPLETE
#
# MessageText:
#
# The TPM provisioning did not complete.  For more information on completing the provisioning, call the Win32_Tpm WMI method for provisioning the TPM ('Provision') and check the returned Information.
#
TBS_E_PROVISIONING_INCOMPLETE = 0x80284016

#
# TPM API error codes {0x0100..0x01ff}
#
#
# MessageId: TPMAPI_E_INVALID_STATE
#
# MessageText:
#
# The command buffer is not in the correct state.
#
TPMAPI_E_INVALID_STATE = 0x80290100

#
# MessageId: TPMAPI_E_NOT_ENOUGH_DATA
#
# MessageText:
#
# The command buffer does not contain enough data to satisfy the request.
#
TPMAPI_E_NOT_ENOUGH_DATA = 0x80290101

#
# MessageId: TPMAPI_E_TOO_MUCH_DATA
#
# MessageText:
#
# The command buffer cannot contain any more data.
#
TPMAPI_E_TOO_MUCH_DATA = 0x80290102

#
# MessageId: TPMAPI_E_INVALID_OUTPUT_POINTER
#
# MessageText:
#
# One or more output parameters was NULL or invalid.
#
TPMAPI_E_INVALID_OUTPUT_POINTER = 0x80290103

#
# MessageId: TPMAPI_E_INVALID_PARAMETER
#
# MessageText:
#
# One or more input parameters is invalid.
#
TPMAPI_E_INVALID_PARAMETER = 0x80290104

#
# MessageId: TPMAPI_E_OUT_OF_MEMORY
#
# MessageText:
#
# Not enough memory was available to satisfy the request.
#
TPMAPI_E_OUT_OF_MEMORY = 0x80290105

#
# MessageId: TPMAPI_E_BUFFER_TOO_SMALL
#
# MessageText:
#
# The specified buffer was too small.
#
TPMAPI_E_BUFFER_TOO_SMALL = 0x80290106

#
# MessageId: TPMAPI_E_INTERNAL_ERROR
#
# MessageText:
#
# An internal error was detected.
#
TPMAPI_E_INTERNAL_ERROR = 0x80290107

#
# MessageId: TPMAPI_E_ACCESS_DENIED
#
# MessageText:
#
# The caller does not have the appropriate rights to perform the requested operation.
#
TPMAPI_E_ACCESS_DENIED = 0x80290108

#
# MessageId: TPMAPI_E_AUTHORIZATION_FAILED
#
# MessageText:
#
# The specified authorization information was invalid.
#
TPMAPI_E_AUTHORIZATION_FAILED = 0x80290109

#
# MessageId: TPMAPI_E_INVALID_CONTEXT_HANDLE
#
# MessageText:
#
# The specified context handle was not valid.
#
TPMAPI_E_INVALID_CONTEXT_HANDLE = 0x8029010A

#
# MessageId: TPMAPI_E_TBS_COMMUNICATION_ERROR
#
# MessageText:
#
# An error occurred while communicating with the TBS.
#
TPMAPI_E_TBS_COMMUNICATION_ERROR = 0x8029010B

#
# MessageId: TPMAPI_E_TPM_COMMAND_ERROR
#
# MessageText:
#
# The TPM returned an unexpected result.
#
TPMAPI_E_TPM_COMMAND_ERROR = 0x8029010C

#
# MessageId: TPMAPI_E_MESSAGE_TOO_LARGE
#
# MessageText:
#
# The message was too large for the encoding scheme.
#
TPMAPI_E_MESSAGE_TOO_LARGE = 0x8029010D

#
# MessageId: TPMAPI_E_INVALID_ENCODING
#
# MessageText:
#
# The encoding in the blob was not recognized.
#
TPMAPI_E_INVALID_ENCODING = 0x8029010E

#
# MessageId: TPMAPI_E_INVALID_KEY_SIZE
#
# MessageText:
#
# The key size is not valid.
#
TPMAPI_E_INVALID_KEY_SIZE = 0x8029010F

#
# MessageId: TPMAPI_E_ENCRYPTION_FAILED
#
# MessageText:
#
# The encryption operation failed.
#
TPMAPI_E_ENCRYPTION_FAILED = 0x80290110

#
# MessageId: TPMAPI_E_INVALID_KEY_PARAMS
#
# MessageText:
#
# The key parameters structure was not valid
#
TPMAPI_E_INVALID_KEY_PARAMS = 0x80290111

#
# MessageId: TPMAPI_E_INVALID_MIGRATION_AUTHORIZATION_BLOB
#
# MessageText:
#
# The requested supplied data does not appear to be a valid migration authorization blob.
#
TPMAPI_E_INVALID_MIGRATION_AUTHORIZATION_BLOB = 0x80290112

#
# MessageId: TPMAPI_E_INVALID_PCR_INDEX
#
# MessageText:
#
# The specified PCR index was invalid
#
TPMAPI_E_INVALID_PCR_INDEX = 0x80290113

#
# MessageId: TPMAPI_E_INVALID_DELEGATE_BLOB
#
# MessageText:
#
# The data given does not appear to be a valid delegate blob.
#
TPMAPI_E_INVALID_DELEGATE_BLOB = 0x80290114

#
# MessageId: TPMAPI_E_INVALID_CONTEXT_PARAMS
#
# MessageText:
#
# One or more of the specified context parameters was not valid.
#
TPMAPI_E_INVALID_CONTEXT_PARAMS = 0x80290115

#
# MessageId: TPMAPI_E_INVALID_KEY_BLOB
#
# MessageText:
#
# The data given does not appear to be a valid key blob
#
TPMAPI_E_INVALID_KEY_BLOB = 0x80290116

#
# MessageId: TPMAPI_E_INVALID_PCR_DATA
#
# MessageText:
#
# The specified PCR data was invalid.
#
TPMAPI_E_INVALID_PCR_DATA = 0x80290117

#
# MessageId: TPMAPI_E_INVALID_OWNER_AUTH
#
# MessageText:
#
# The format of the owner auth data was invalid.
#
TPMAPI_E_INVALID_OWNER_AUTH = 0x80290118

#
# MessageId: TPMAPI_E_FIPS_RNG_CHECK_FAILED
#
# MessageText:
#
# The random number generated did not pass FIPS RNG check.
#
TPMAPI_E_FIPS_RNG_CHECK_FAILED = 0x80290119

#
# MessageId: TPMAPI_E_EMPTY_TCG_LOG
#
# MessageText:
#
# The TCG Event Log does not contain any data.
#
TPMAPI_E_EMPTY_TCG_LOG = 0x8029011A

#
# MessageId: TPMAPI_E_INVALID_TCG_LOG_ENTRY
#
# MessageText:
#
# An entry in the TCG Event Log was invalid.
#
TPMAPI_E_INVALID_TCG_LOG_ENTRY = 0x8029011B

#
# MessageId: TPMAPI_E_TCG_SEPARATOR_ABSENT
#
# MessageText:
#
# A TCG Separator was not found.
#
TPMAPI_E_TCG_SEPARATOR_ABSENT = 0x8029011C

#
# MessageId: TPMAPI_E_TCG_INVALID_DIGEST_ENTRY
#
# MessageText:
#
# A digest value in a TCG Log entry did not match hashed data.
#
TPMAPI_E_TCG_INVALID_DIGEST_ENTRY = 0x8029011D

#
# MessageId: TPMAPI_E_POLICY_DENIES_OPERATION
#
# MessageText:
#
# The requested operation was blocked by current TPM policy. Please contact your system administrator for assistance.
#
TPMAPI_E_POLICY_DENIES_OPERATION = 0x8029011E

#
# TBS implementation error codes {0x0200..0x02ff}
#
#
# MessageId: TBSIMP_E_BUFFER_TOO_SMALL
#
# MessageText:
#
# The specified buffer was too small.
#
TBSIMP_E_BUFFER_TOO_SMALL = 0x80290200

#
# MessageId: TBSIMP_E_CLEANUP_FAILED
#
# MessageText:
#
# The context could not be cleaned up.
#
TBSIMP_E_CLEANUP_FAILED = 0x80290201

#
# MessageId: TBSIMP_E_INVALID_CONTEXT_HANDLE
#
# MessageText:
#
# The specified context handle is invalid.
#
TBSIMP_E_INVALID_CONTEXT_HANDLE = 0x80290202

#
# MessageId: TBSIMP_E_INVALID_CONTEXT_PARAM
#
# MessageText:
#
# An invalid context parameter was specified.
#
TBSIMP_E_INVALID_CONTEXT_PARAM = 0x80290203

#
# MessageId: TBSIMP_E_TPM_ERROR
#
# MessageText:
#
# An error occurred while communicating with the TPM
#
TBSIMP_E_TPM_ERROR = 0x80290204

#
# MessageId: TBSIMP_E_HASH_BAD_KEY
#
# MessageText:
#
# No entry with the specified key was found.
#
TBSIMP_E_HASH_BAD_KEY = 0x80290205

#
# MessageId: TBSIMP_E_DUPLICATE_VHANDLE
#
# MessageText:
#
# The specified virtual handle matches a virtual handle already in use.
#
TBSIMP_E_DUPLICATE_VHANDLE = 0x80290206

#
# MessageId: TBSIMP_E_INVALID_OUTPUT_POINTER
#
# MessageText:
#
# The pointer to the returned handle location was NULL or invalid
#
TBSIMP_E_INVALID_OUTPUT_POINTER = 0x80290207

#
# MessageId: TBSIMP_E_INVALID_PARAMETER
#
# MessageText:
#
# One or more parameters is invalid
#
TBSIMP_E_INVALID_PARAMETER = 0x80290208

#
# MessageId: TBSIMP_E_RPC_INIT_FAILED
#
# MessageText:
#
# The RPC subsystem could not be initialized.
#
TBSIMP_E_RPC_INIT_FAILED = 0x80290209

#
# MessageId: TBSIMP_E_SCHEDULER_NOT_RUNNING
#
# MessageText:
#
# The TBS scheduler is not running.
#
TBSIMP_E_SCHEDULER_NOT_RUNNING = 0x8029020A

#
# MessageId: TBSIMP_E_COMMAND_CANCELED
#
# MessageText:
#
# The command was canceled.
#
TBSIMP_E_COMMAND_CANCELED = 0x8029020B

#
# MessageId: TBSIMP_E_OUT_OF_MEMORY
#
# MessageText:
#
# There was not enough memory to fulfill the request
#
TBSIMP_E_OUT_OF_MEMORY = 0x8029020C

#
# MessageId: TBSIMP_E_LIST_NO_MORE_ITEMS
#
# MessageText:
#
# The specified list is empty, or the iteration has reached the end of the list.
#
TBSIMP_E_LIST_NO_MORE_ITEMS = 0x8029020D

#
# MessageId: TBSIMP_E_LIST_NOT_FOUND
#
# MessageText:
#
# The specified item was not found in the list.
#
TBSIMP_E_LIST_NOT_FOUND = 0x8029020E

#
# MessageId: TBSIMP_E_NOT_ENOUGH_SPACE
#
# MessageText:
#
# The TPM does not have enough space to load the requested resource.
#
TBSIMP_E_NOT_ENOUGH_SPACE = 0x8029020F

#
# MessageId: TBSIMP_E_NOT_ENOUGH_TPM_CONTEXTS
#
# MessageText:
#
# There are too many TPM contexts in use.
#
TBSIMP_E_NOT_ENOUGH_TPM_CONTEXTS = 0x80290210

#
# MessageId: TBSIMP_E_COMMAND_FAILED
#
# MessageText:
#
# The TPM command failed.
#
TBSIMP_E_COMMAND_FAILED = 0x80290211

#
# MessageId: TBSIMP_E_UNKNOWN_ORDINAL
#
# MessageText:
#
# The TBS does not recognize the specified ordinal.
#
TBSIMP_E_UNKNOWN_ORDINAL = 0x80290212

#
# MessageId: TBSIMP_E_RESOURCE_EXPIRED
#
# MessageText:
#
# The requested resource is no longer available.
#
TBSIMP_E_RESOURCE_EXPIRED = 0x80290213

#
# MessageId: TBSIMP_E_INVALID_RESOURCE
#
# MessageText:
#
# The resource type did not match.
#
TBSIMP_E_INVALID_RESOURCE = 0x80290214

#
# MessageId: TBSIMP_E_NOTHING_TO_UNLOAD
#
# MessageText:
#
# No resources can be unloaded.
#
TBSIMP_E_NOTHING_TO_UNLOAD = 0x80290215

#
# MessageId: TBSIMP_E_HASH_TABLE_FULL
#
# MessageText:
#
# No new entries can be added to the hash table.
#
TBSIMP_E_HASH_TABLE_FULL = 0x80290216

#
# MessageId: TBSIMP_E_TOO_MANY_TBS_CONTEXTS
#
# MessageText:
#
# A new TBS context could not be created because there are too many open contexts.
#
TBSIMP_E_TOO_MANY_TBS_CONTEXTS = 0x80290217

#
# MessageId: TBSIMP_E_TOO_MANY_RESOURCES
#
# MessageText:
#
# A new virtual resource could not be created because there are too many open virtual resources.
#
TBSIMP_E_TOO_MANY_RESOURCES = 0x80290218

#
# MessageId: TBSIMP_E_PPI_NOT_SUPPORTED
#
# MessageText:
#
# The physical presence interface is not supported.
#
TBSIMP_E_PPI_NOT_SUPPORTED = 0x80290219

#
# MessageId: TBSIMP_E_TPM_INCOMPATIBLE
#
# MessageText:
#
# TBS is not compatible with the version of TPM found on the system.
#
TBSIMP_E_TPM_INCOMPATIBLE = 0x8029021A

#
# MessageId: TBSIMP_E_NO_EVENT_LOG
#
# MessageText:
#
# No TCG event log is available.
#
TBSIMP_E_NO_EVENT_LOG = 0x8029021B

#
# TPM Physical Presence implementation error codes {0x0300..0x03ff}
#
#
# MessageId: TPM_E_PPI_ACPI_FAILURE
#
# MessageText:
#
# A general error was detected when attempting to acquire the BIOS's response to a Physical Presence command.
#
TPM_E_PPI_ACPI_FAILURE = 0x80290300

#
# MessageId: TPM_E_PPI_USER_ABORT
#
# MessageText:
#
# The user failed to confirm the TPM operation request.
#
TPM_E_PPI_USER_ABORT = 0x80290301

#
# MessageId: TPM_E_PPI_BIOS_FAILURE
#
# MessageText:
#
# The BIOS failure prevented the successful execution of the requested TPM operation (e.g. invalid TPM operation request, BIOS communication error with the TPM).
#
TPM_E_PPI_BIOS_FAILURE = 0x80290302

#
# MessageId: TPM_E_PPI_NOT_SUPPORTED
#
# MessageText:
#
# The BIOS does not support the physical presence interface.
#
TPM_E_PPI_NOT_SUPPORTED = 0x80290303

#
# MessageId: TPM_E_PPI_BLOCKED_IN_BIOS
#
# MessageText:
#
# The Physical Presence command was blocked by current BIOS settings. The system owner may be able to reconfigure the BIOS settings to allow the command.
#
TPM_E_PPI_BLOCKED_IN_BIOS = 0x80290304

#
# Platform Crypto Provider (PCPTPM12.dll and future platform crypto providers)  error codes {0x0400..0x04ff}
#
#
# MessageId: TPM_E_PCP_ERROR_MASK
#
# MessageText:
#
# This is an error mask to convert Platform Crypto Provider errors to win errors.
#
TPM_E_PCP_ERROR_MASK = 0x80290400

#
# MessageId: TPM_E_PCP_DEVICE_NOT_READY
#
# MessageText:
#
# The Platform Crypto Device is currently not ready. It needs to be fully provisioned to be operational.
#
TPM_E_PCP_DEVICE_NOT_READY = 0x80290401

#
# MessageId: TPM_E_PCP_INVALID_HANDLE
#
# MessageText:
#
# The handle provided to the Platform Crypto Provider is invalid.
#
TPM_E_PCP_INVALID_HANDLE = 0x80290402

#
# MessageId: TPM_E_PCP_INVALID_PARAMETER
#
# MessageText:
#
# A parameter provided to the Platform Crypto Provider is invalid.
#
TPM_E_PCP_INVALID_PARAMETER = 0x80290403

#
# MessageId: TPM_E_PCP_FLAG_NOT_SUPPORTED
#
# MessageText:
#
# A provided flag to the Platform Crypto Provider is not supported.
#
TPM_E_PCP_FLAG_NOT_SUPPORTED = 0x80290404

#
# MessageId: TPM_E_PCP_NOT_SUPPORTED
#
# MessageText:
#
# The requested operation is not supported by this Platform Crypto Provider.
#
TPM_E_PCP_NOT_SUPPORTED = 0x80290405

#
# MessageId: TPM_E_PCP_BUFFER_TOO_SMALL
#
# MessageText:
#
# The buffer is too small to contain all data. No information has been written to the buffer.
#
TPM_E_PCP_BUFFER_TOO_SMALL = 0x80290406

#
# MessageId: TPM_E_PCP_INTERNAL_ERROR
#
# MessageText:
#
# An unexpected internal error has occurred in the Platform Crypto Provider.
#
TPM_E_PCP_INTERNAL_ERROR = 0x80290407

#
# MessageId: TPM_E_PCP_AUTHENTICATION_FAILED
#
# MessageText:
#
# The authorization to use a provider object has failed.
#
TPM_E_PCP_AUTHENTICATION_FAILED = 0x80290408

#
# MessageId: TPM_E_PCP_AUTHENTICATION_IGNORED
#
# MessageText:
#
# The Platform Crypto Device has ignored the authorization for the provider object, to mitigate against a dictionary attack.
#
TPM_E_PCP_AUTHENTICATION_IGNORED = 0x80290409

#
# MessageId: TPM_E_PCP_POLICY_NOT_FOUND
#
# MessageText:
#
# The referenced policy was not found.
#
TPM_E_PCP_POLICY_NOT_FOUND = 0x8029040A

#
# MessageId: TPM_E_PCP_PROFILE_NOT_FOUND
#
# MessageText:
#
# The referenced profile was not found.
#
TPM_E_PCP_PROFILE_NOT_FOUND = 0x8029040B

#
# MessageId: TPM_E_PCP_VALIDATION_FAILED
#
# MessageText:
#
# The validation was not succesful.
#
TPM_E_PCP_VALIDATION_FAILED = 0x8029040C

#
# If the application is designed to use TCG defined TPM return codes
# then undefine the Windows defined codes for the same symbols. The application
# declares usage of TCG return codes by defining WIN_OMIT_TSS_TPM_RETURN_CODES
# before including windows.h
#
#ifdef WIN_OMIT_TSS_TPM_RETURN_CODES
#undef TPM_E_AREA_LOCKED
#undef TPM_E_AUDITFAILURE
#undef TPM_E_AUDITFAIL_SUCCESSFUL
#undef TPM_E_AUDITFAIL_UNSUCCESSFUL
#undef TPM_E_AUTH2FAIL
#undef TPM_E_AUTHFAIL
#undef TPM_E_AUTH_CONFLICT
#undef TPM_E_BADCONTEXT
#undef TPM_E_BADINDEX
#undef TPM_E_BADTAG
#undef TPM_E_BAD_ATTRIBUTES
#undef TPM_E_BAD_COUNTER
#undef TPM_E_BAD_DATASIZE
#undef TPM_E_BAD_DELEGATE
#undef TPM_E_BAD_HANDLE
#undef TPM_E_BAD_KEY_PROPERTY
#undef TPM_E_BAD_LOCALITY
#undef TPM_E_BAD_MIGRATION
#undef TPM_E_BAD_MODE
#undef TPM_E_BAD_ORDINAL
#undef TPM_E_BAD_PARAMETER
#undef TPM_E_BAD_PARAM_SIZE
#undef TPM_E_BAD_PRESENCE
#undef TPM_E_BAD_SCHEME
#undef TPM_E_BAD_SIGNATURE
#undef TPM_E_BAD_TYPE
#undef TPM_E_BAD_VERSION
#undef TPM_E_CLEAR_DISABLED
#undef TPM_E_CONTEXT_GAP
#undef TPM_E_DAA_INPUT_DATA0
#undef TPM_E_DAA_INPUT_DATA1
#undef TPM_E_DAA_ISSUER_SETTINGS
#undef TPM_E_DAA_ISSUER_VALIDITY
#undef TPM_E_DAA_RESOURCES
#undef TPM_E_DAA_STAGE
#undef TPM_E_DAA_TPM_SETTINGS
#undef TPM_E_DAA_WRONG_W
#undef TPM_E_DEACTIVATED
#undef TPM_E_DECRYPT_ERROR
#undef TPM_E_DEFEND_LOCK_RUNNING
#undef TPM_E_DELEGATE_ADMIN
#undef TPM_E_DELEGATE_FAMILY
#undef TPM_E_DELEGATE_LOCK
#undef TPM_E_DISABLED
#undef TPM_E_DISABLED_CMD
#undef TPM_E_DOING_SELFTEST
#undef TPM_E_ENCRYPT_ERROR
#undef TPM_E_FAIL
#undef TPM_E_FAILEDSELFTEST
#undef TPM_E_FAMILYCOUNT
#undef TPM_E_INAPPROPRIATE_ENC
#undef TPM_E_INAPPROPRIATE_SIG
#undef TPM_E_INSTALL_DISABLED
#undef TPM_E_INVALID_AUTHHANDLE
#undef TPM_E_INVALID_FAMILY
#undef TPM_E_INVALID_KEYHANDLE
#undef TPM_E_INVALID_KEYUSAGE
#undef TPM_E_INVALID_PCR_INFO
#undef TPM_E_INVALID_POSTINIT
#undef TPM_E_INVALID_RESOURCE
#undef TPM_E_INVALID_STRUCTURE
#undef TPM_E_IOERROR
#undef TPM_E_KEYNOTFOUND
#undef TPM_E_KEY_NOTSUPPORTED
#undef TPM_E_KEY_OWNER_CONTROL
#undef TPM_E_MAXNVWRITES
#undef TPM_E_MA_AUTHORITY
#undef TPM_E_MA_DESTINATION
#undef TPM_E_MA_SOURCE
#undef TPM_E_MA_TICKET_SIGNATURE
#undef TPM_E_MIGRATEFAIL
#undef TPM_E_NEEDS_SELFTEST
#undef TPM_E_NOCONTEXTSPACE
#undef TPM_E_NOOPERATOR
#undef TPM_E_NOSPACE
#undef TPM_E_NOSRK
#undef TPM_E_NOTFIPS
#undef TPM_E_NOTLOCAL
#undef TPM_E_NOTRESETABLE
#undef TPM_E_NOTSEALED_BLOB
#undef TPM_E_NOT_FULLWRITE
#undef TPM_E_NO_ENDORSEMENT
#undef TPM_E_NO_NV_PERMISSION
#undef TPM_E_NO_WRAP_TRANSPORT
#undef TPM_E_OWNER_CONTROL
#undef TPM_E_OWNER_SET
#undef TPM_E_PERMANENTEK
#undef TPM_E_PER_NOWRITE
#undef TPM_E_READ_ONLY
#undef TPM_E_REQUIRES_SIGN
#undef TPM_E_RESOURCEMISSING
#undef TPM_E_RESOURCES
#undef TPM_E_RETRY
#undef TPM_E_SHA_ERROR
#undef TPM_E_SHA_THREAD
#undef TPM_E_SHORTRANDOM
#undef TPM_E_SIZE
#undef TPM_E_TOOMANYCONTEXTS
#undef TPM_E_TRANSPORT_NOTEXCLUSIVE
#undef TPM_E_WRITE_LOCKED
#undef TPM_E_WRONGPCRVAL
#undef TPM_E_WRONG_ENTITYTYPE
#undef TPM_SUCCESS
#endif
#
# =======================================================
# Facility Performance Logs & Alerts (PLA) Error Messages
# =======================================================
#
#
# MessageId: PLA_E_DCS_NOT_FOUND
#
# MessageText:
#
# Data Collector Set was not found.
#
PLA_E_DCS_NOT_FOUND = 0x80300002

#
# MessageId: PLA_E_DCS_IN_USE
#
# MessageText:
#
# The Data Collector Set or one of its dependencies is already in use.
#
PLA_E_DCS_IN_USE = 0x803000AA

#
# MessageId: PLA_E_TOO_MANY_FOLDERS
#
# MessageText:
#
# Unable to start Data Collector Set because there are too many folders.
#
PLA_E_TOO_MANY_FOLDERS = 0x80300045

#
# MessageId: PLA_E_NO_MIN_DISK
#
# MessageText:
#
# Not enough free disk space to start Data Collector Set.
#
PLA_E_NO_MIN_DISK = 0x80300070

#
# MessageId: PLA_E_DCS_ALREADY_EXISTS
#
# MessageText:
#
# Data Collector Set already exists.
#
PLA_E_DCS_ALREADY_EXISTS = 0x803000B7

#
# MessageId: PLA_S_PROPERTY_IGNORED
#
# MessageText:
#
# Property value will be ignored.
#
PLA_S_PROPERTY_IGNORED = 0x00300100

#
# MessageId: PLA_E_PROPERTY_CONFLICT
#
# MessageText:
#
# Property value conflict.
#
PLA_E_PROPERTY_CONFLICT = 0x80300101

#
# MessageId: PLA_E_DCS_SINGLETON_REQUIRED
#
# MessageText:
#
# The current configuration for this Data Collector Set requires that it contain exactly one Data Collector.
#
PLA_E_DCS_SINGLETON_REQUIRED = 0x80300102

#
# MessageId: PLA_E_CREDENTIALS_REQUIRED
#
# MessageText:
#
# A user account is required in order to commit the current Data Collector Set properties.
#
PLA_E_CREDENTIALS_REQUIRED = 0x80300103

#
# MessageId: PLA_E_DCS_NOT_RUNNING
#
# MessageText:
#
# Data Collector Set is not running.
#
PLA_E_DCS_NOT_RUNNING = 0x80300104

#
# MessageId: PLA_E_CONFLICT_INCL_EXCL_API
#
# MessageText:
#
# A conflict was detected in the list of include/exclude APIs. Do not specify the same API in both the include list and the exclude list.
#
PLA_E_CONFLICT_INCL_EXCL_API = 0x80300105

#
# MessageId: PLA_E_NETWORK_EXE_NOT_VALID
#
# MessageText:
#
# The executable path you have specified refers to a network share or UNC path.
#
PLA_E_NETWORK_EXE_NOT_VALID = 0x80300106

#
# MessageId: PLA_E_EXE_ALREADY_CONFIGURED
#
# MessageText:
#
# The executable path you have specified is already configured for API tracing.
#
PLA_E_EXE_ALREADY_CONFIGURED = 0x80300107

#
# MessageId: PLA_E_EXE_PATH_NOT_VALID
#
# MessageText:
#
# The executable path you have specified does not exist. Verify that the specified path is correct.
#
PLA_E_EXE_PATH_NOT_VALID = 0x80300108

#
# MessageId: PLA_E_DC_ALREADY_EXISTS
#
# MessageText:
#
# Data Collector already exists.
#
PLA_E_DC_ALREADY_EXISTS = 0x80300109

#
# MessageId: PLA_E_DCS_START_WAIT_TIMEOUT
#
# MessageText:
#
# The wait for the Data Collector Set start notification has timed out.
#
PLA_E_DCS_START_WAIT_TIMEOUT = 0x8030010A

#
# MessageId: PLA_E_DC_START_WAIT_TIMEOUT
#
# MessageText:
#
# The wait for the Data Collector to start has timed out.
#
PLA_E_DC_START_WAIT_TIMEOUT = 0x8030010B

#
# MessageId: PLA_E_REPORT_WAIT_TIMEOUT
#
# MessageText:
#
# The wait for the report generation tool to finish has timed out.
#
PLA_E_REPORT_WAIT_TIMEOUT = 0x8030010C

#
# MessageId: PLA_E_NO_DUPLICATES
#
# MessageText:
#
# Duplicate items are not allowed.
#
PLA_E_NO_DUPLICATES = 0x8030010D

#
# MessageId: PLA_E_EXE_FULL_PATH_REQUIRED
#
# MessageText:
#
# When specifying the executable that you want to trace, you must specify a full path to the executable and not just a filename.
#
PLA_E_EXE_FULL_PATH_REQUIRED = 0x8030010E

#
# MessageId: PLA_E_INVALID_SESSION_NAME
#
# MessageText:
#
# The session name provided is invalid.
#
PLA_E_INVALID_SESSION_NAME = 0x8030010F

#
# MessageId: PLA_E_PLA_CHANNEL_NOT_ENABLED
#
# MessageText:
#
# The Event Log channel Microsoft-Windows-Diagnosis-PLA/Operational must be enabled to perform this operation.
#
PLA_E_PLA_CHANNEL_NOT_ENABLED = 0x80300110

#
# MessageId: PLA_E_TASKSCHED_CHANNEL_NOT_ENABLED
#
# MessageText:
#
# The Event Log channel Microsoft-Windows-TaskScheduler must be enabled to perform this operation.
#
PLA_E_TASKSCHED_CHANNEL_NOT_ENABLED = 0x80300111

#
# MessageId: PLA_E_RULES_MANAGER_FAILED
#
# MessageText:
#
# The execution of the Rules Manager failed.
#
PLA_E_RULES_MANAGER_FAILED = 0x80300112

#
# MessageId: PLA_E_CABAPI_FAILURE
#
# MessageText:
#
# An error occurred while attempting to compress or extract the data.
#
PLA_E_CABAPI_FAILURE = 0x80300113

#
# =======================================================
# Full Volume Encryption Error Messages
# =======================================================
#
#
# MessageId: FVE_E_LOCKED_VOLUME
#
# MessageText:
#
# This drive is locked by BitLocker Drive Encryption. You must unlock this drive from Control Panel.
#
FVE_E_LOCKED_VOLUME = 0x80310000

#
# MessageId: FVE_E_NOT_ENCRYPTED
#
# MessageText:
#
# This drive is not encrypted.
#
FVE_E_NOT_ENCRYPTED = 0x80310001

#
# MessageId: FVE_E_NO_TPM_BIOS
#
# MessageText:
#
# The BIOS did not correctly communicate with the Trusted Platform Module (TPM). Contact the computer manufacturer for BIOS upgrade instructions.
#
FVE_E_NO_TPM_BIOS = 0x80310002

#
# MessageId: FVE_E_NO_MBR_METRIC
#
# MessageText:
#
# The BIOS did not correctly communicate with the master boot record (MBR). Contact the computer manufacturer for BIOS upgrade instructions.
#
FVE_E_NO_MBR_METRIC = 0x80310003

#
# MessageId: FVE_E_NO_BOOTSECTOR_METRIC
#
# MessageText:
#
# A required TPM measurement is missing. If there is a bootable CD or DVD in your computer, remove it, restart the computer, and turn on BitLocker again. If the problem persists, ensure the master boot record is up to date.
#
FVE_E_NO_BOOTSECTOR_METRIC = 0x80310004

#
# MessageId: FVE_E_NO_BOOTMGR_METRIC
#
# MessageText:
#
# The boot sector of this drive is not compatible with BitLocker Drive Encryption. Use the Bootrec.exe tool in the Windows Recovery Environment to update or repair the boot manager (BOOTMGR).
#
FVE_E_NO_BOOTMGR_METRIC = 0x80310005

#
# MessageId: FVE_E_WRONG_BOOTMGR
#
# MessageText:
#
# The boot manager of this operating system is not compatible with BitLocker Drive Encryption. Use the Bootrec.exe tool in the Windows Recovery Environment to update or repair the boot manager (BOOTMGR).
#
FVE_E_WRONG_BOOTMGR = 0x80310006

#
# MessageId: FVE_E_SECURE_KEY_REQUIRED
#
# MessageText:
#
# At least one secure key protector is required for this operation to be performed.
#
FVE_E_SECURE_KEY_REQUIRED = 0x80310007

#
# MessageId: FVE_E_NOT_ACTIVATED
#
# MessageText:
#
# BitLocker Drive Encryption is not enabled on this drive. Turn on BitLocker.
#
FVE_E_NOT_ACTIVATED = 0x80310008

#
# MessageId: FVE_E_ACTION_NOT_ALLOWED
#
# MessageText:
#
# BitLocker Drive Encryption cannot perform the requested action. This condition may occur when two requests are issued at the same time. Wait a few moments and then try the action again.
#
FVE_E_ACTION_NOT_ALLOWED = 0x80310009

#
# MessageId: FVE_E_AD_SCHEMA_NOT_INSTALLED
#
# MessageText:
#
# The Active Directory Domain Services forest does not contain the required attributes and classes to host BitLocker Drive Encryption or Trusted Platform Module information. Contact your domain administrator to verify that any required BitLocker Active Directory schema extensions have been installed.
#
FVE_E_AD_SCHEMA_NOT_INSTALLED = 0x8031000A

#
# MessageId: FVE_E_AD_INVALID_DATATYPE
#
# MessageText:
#
# The type of the data obtained from Active Directory was not expected. The BitLocker recovery information may be missing or corrupted.
#
FVE_E_AD_INVALID_DATATYPE = 0x8031000B

#
# MessageId: FVE_E_AD_INVALID_DATASIZE
#
# MessageText:
#
# The size of the data obtained from Active Directory was not expected. The BitLocker recovery information may be missing or corrupted.
#
FVE_E_AD_INVALID_DATASIZE = 0x8031000C

#
# MessageId: FVE_E_AD_NO_VALUES
#
# MessageText:
#
# The attribute read from Active Directory does not contain any values. The BitLocker recovery information may be missing or corrupted.
#
FVE_E_AD_NO_VALUES = 0x8031000D

#
# MessageId: FVE_E_AD_ATTR_NOT_SET
#
# MessageText:
#
# The attribute was not set. Verify that you are logged on with a domain account that has the ability to write information to Active Directory objects.
#
FVE_E_AD_ATTR_NOT_SET = 0x8031000E

#
# MessageId: FVE_E_AD_GUID_NOT_FOUND
#
# MessageText:
#
# The specified attribute cannot be found in Active Directory Domain Services. Contact your domain administrator to verify that any required BitLocker Active Directory schema extensions have been installed.
#
FVE_E_AD_GUID_NOT_FOUND = 0x8031000F

#
# MessageId: FVE_E_BAD_INFORMATION
#
# MessageText:
#
# The BitLocker metadata for the encrypted drive is not valid. You can attempt to repair the drive to restore access.
#
FVE_E_BAD_INFORMATION = 0x80310010

#
# MessageId: FVE_E_TOO_SMALL
#
# MessageText:
#
# The drive cannot be encrypted because it does not have enough free space. Delete any unnecessary data on the drive to create additional free space and then try again.
#
FVE_E_TOO_SMALL = 0x80310011

#
# MessageId: FVE_E_SYSTEM_VOLUME
#
# MessageText:
#
# The drive cannot be encrypted because it contains system boot information. Create a separate partition for use as the system drive that contains the boot information and a second partition for use as the operating system drive and then encrypt the operating system drive.
#
FVE_E_SYSTEM_VOLUME = 0x80310012

#
# MessageId: FVE_E_FAILED_WRONG_FS
#
# MessageText:
#
# The drive cannot be encrypted because the file system is not supported.
#
FVE_E_FAILED_WRONG_FS = 0x80310013

#
# MessageId: FVE_E_BAD_PARTITION_SIZE
#
# MessageText:
#
# The file system size is larger than the partition size in the partition table. This drive may be corrupt or may have been tampered with. To use it with BitLocker, you must reformat the partition.
#
FVE_E_BAD_PARTITION_SIZE = 0x80310014

#
# MessageId: FVE_E_NOT_SUPPORTED
#
# MessageText:
#
# This drive cannot be encrypted.
#
FVE_E_NOT_SUPPORTED = 0x80310015

#
# MessageId: FVE_E_BAD_DATA
#
# MessageText:
#
# The data is not valid.
#
FVE_E_BAD_DATA = 0x80310016

#
# MessageId: FVE_E_VOLUME_NOT_BOUND
#
# MessageText:
#
# The data drive specified is not set to automatically unlock on the current computer and cannot be unlocked automatically.
#
FVE_E_VOLUME_NOT_BOUND = 0x80310017

#
# MessageId: FVE_E_TPM_NOT_OWNED
#
# MessageText:
#
# You must initialize the Trusted Platform Module (TPM) before you can use BitLocker Drive Encryption.
#
FVE_E_TPM_NOT_OWNED = 0x80310018

#
# MessageId: FVE_E_NOT_DATA_VOLUME
#
# MessageText:
#
# The operation attempted cannot be performed on an operating system drive.
#
FVE_E_NOT_DATA_VOLUME = 0x80310019

#
# MessageId: FVE_E_AD_INSUFFICIENT_BUFFER
#
# MessageText:
#
# The buffer supplied to a function was insufficient to contain the returned data. Increase the buffer size before running the function again.
#
FVE_E_AD_INSUFFICIENT_BUFFER = 0x8031001A

#
# MessageId: FVE_E_CONV_READ
#
# MessageText:
#
# A read operation failed while converting the drive. The drive was not converted. Please re-enable BitLocker.
#
FVE_E_CONV_READ = 0x8031001B

#
# MessageId: FVE_E_CONV_WRITE
#
# MessageText:
#
# A write operation failed while converting the drive. The drive was not converted. Please re-enable BitLocker.
#
FVE_E_CONV_WRITE = 0x8031001C

#
# MessageId: FVE_E_KEY_REQUIRED
#
# MessageText:
#
# One or more BitLocker key protectors are required. You cannot delete the last key on this drive.
#
FVE_E_KEY_REQUIRED = 0x8031001D

#
# MessageId: FVE_E_CLUSTERING_NOT_SUPPORTED
#
# MessageText:
#
# Cluster configurations are not supported by BitLocker Drive Encryption.
#
FVE_E_CLUSTERING_NOT_SUPPORTED = 0x8031001E

#
# MessageId: FVE_E_VOLUME_BOUND_ALREADY
#
# MessageText:
#
# The drive specified is already configured to be automatically unlocked on the current computer.
#
FVE_E_VOLUME_BOUND_ALREADY = 0x8031001F

#
# MessageId: FVE_E_OS_NOT_PROTECTED
#
# MessageText:
#
# The operating system drive is not protected by BitLocker Drive Encryption.
#
FVE_E_OS_NOT_PROTECTED = 0x80310020

#
# MessageId: FVE_E_PROTECTION_DISABLED
#
# MessageText:
#
# BitLocker Drive Encryption has been suspended on this drive. All BitLocker key protectors configured for this drive are effectively disabled, and the drive will be automatically unlocked using an unencrypted (clear) key.
#
FVE_E_PROTECTION_DISABLED = 0x80310021

#
# MessageId: FVE_E_RECOVERY_KEY_REQUIRED
#
# MessageText:
#
# The drive you are attempting to lock does not have any key protectors available for encryption because BitLocker protection is currently suspended. Re-enable BitLocker to lock this drive.
#
FVE_E_RECOVERY_KEY_REQUIRED = 0x80310022

#
# MessageId: FVE_E_FOREIGN_VOLUME
#
# MessageText:
#
# BitLocker cannot use the Trusted Platform Module (TPM) to protect a data drive. TPM protection can only be used with the operating system drive.
#
FVE_E_FOREIGN_VOLUME = 0x80310023

#
# MessageId: FVE_E_OVERLAPPED_UPDATE
#
# MessageText:
#
# The BitLocker metadata for the encrypted drive cannot be updated because it was locked for updating by another process. Please try this process again.
#
FVE_E_OVERLAPPED_UPDATE = 0x80310024

#
# MessageId: FVE_E_TPM_SRK_AUTH_NOT_ZERO
#
# MessageText:
#
# The authorization data for the storage root key (SRK) of the Trusted Platform Module (TPM) is not zero and is therefore incompatible with BitLocker. Please initialize the TPM before attempting to use it with BitLocker.
#
FVE_E_TPM_SRK_AUTH_NOT_ZERO = 0x80310025

#
# MessageId: FVE_E_FAILED_SECTOR_SIZE
#
# MessageText:
#
# The drive encryption algorithm cannot be used on this sector size.
#
FVE_E_FAILED_SECTOR_SIZE = 0x80310026

#
# MessageId: FVE_E_FAILED_AUTHENTICATION
#
# MessageText:
#
# The drive cannot be unlocked with the key provided. Confirm that you have provided the correct key and try again.
#
FVE_E_FAILED_AUTHENTICATION = 0x80310027

#
# MessageId: FVE_E_NOT_OS_VOLUME
#
# MessageText:
#
# The drive specified is not the operating system drive.
#
FVE_E_NOT_OS_VOLUME = 0x80310028

#
# MessageId: FVE_E_AUTOUNLOCK_ENABLED
#
# MessageText:
#
# BitLocker Drive Encryption cannot be turned off on the operating system drive until the auto unlock feature has been disabled for the fixed data drives and removable data drives associated with this computer.
#
FVE_E_AUTOUNLOCK_ENABLED = 0x80310029

#
# MessageId: FVE_E_WRONG_BOOTSECTOR
#
# MessageText:
#
# The system partition boot sector does not perform Trusted Platform Module (TPM) measurements. Use the Bootrec.exe tool in the Windows Recovery Environment to update or repair the boot sector.
#
FVE_E_WRONG_BOOTSECTOR = 0x8031002A

#
# MessageId: FVE_E_WRONG_SYSTEM_FS
#
# MessageText:
#
# BitLocker Drive Encryption operating system drives must be formatted with the NTFS file system in order to be encrypted. Convert the drive to NTFS, and then turn on BitLocker.
#
FVE_E_WRONG_SYSTEM_FS = 0x8031002B

#
# MessageId: FVE_E_POLICY_PASSWORD_REQUIRED
#
# MessageText:
#
# Group Policy settings require that a recovery password be specified before encrypting the drive.
#
FVE_E_POLICY_PASSWORD_REQUIRED = 0x8031002C

#
# MessageId: FVE_E_CANNOT_SET_FVEK_ENCRYPTED
#
# MessageText:
#
# The drive encryption algorithm and key cannot be set on a previously encrypted drive. To encrypt this drive with BitLocker Drive Encryption, remove the previous encryption and then turn on BitLocker.
#
FVE_E_CANNOT_SET_FVEK_ENCRYPTED = 0x8031002D

#
# MessageId: FVE_E_CANNOT_ENCRYPT_NO_KEY
#
# MessageText:
#
# BitLocker Drive Encryption cannot encrypt the specified drive because an encryption key is not available. Add a key protector to encrypt this drive.
#
FVE_E_CANNOT_ENCRYPT_NO_KEY = 0x8031002E

#
# MessageId: FVE_E_BOOTABLE_CDDVD
#
# MessageText:
#
# BitLocker Drive Encryption detected bootable media (CD or DVD) in the computer. Remove the media and restart the computer before configuring BitLocker.
#
FVE_E_BOOTABLE_CDDVD = 0x80310030

#
# MessageId: FVE_E_PROTECTOR_EXISTS
#
# MessageText:
#
# This key protector cannot be added. Only one key protector of this type is allowed for this drive.
#
FVE_E_PROTECTOR_EXISTS = 0x80310031

#
# MessageId: FVE_E_RELATIVE_PATH
#
# MessageText:
#
# The recovery password file was not found because a relative path was specified. Recovery passwords must be saved to a fully qualified path. Environment variables configured on the computer can be used in the path.
#
FVE_E_RELATIVE_PATH = 0x80310032

#
# MessageId: FVE_E_PROTECTOR_NOT_FOUND
#
# MessageText:
#
# The specified key protector was not found on the drive. Try another key protector.
#
FVE_E_PROTECTOR_NOT_FOUND = 0x80310033

#
# MessageId: FVE_E_INVALID_KEY_FORMAT
#
# MessageText:
#
# The recovery key provided is corrupt and cannot be used to access the drive. An alternative recovery method, such as recovery password, a data recovery agent, or a backup version of the recovery key must be used to recover access to the drive.
#
FVE_E_INVALID_KEY_FORMAT = 0x80310034

#
# MessageId: FVE_E_INVALID_PASSWORD_FORMAT
#
# MessageText:
#
# The format of the recovery password provided is invalid. BitLocker recovery passwords are 48 digits. Verify that the recovery password is in the correct format and then try again.
#
FVE_E_INVALID_PASSWORD_FORMAT = 0x80310035

#
# MessageId: FVE_E_FIPS_RNG_CHECK_FAILED
#
# MessageText:
#
# The random number generator check test failed.
#
FVE_E_FIPS_RNG_CHECK_FAILED = 0x80310036

#
# MessageId: FVE_E_FIPS_PREVENTS_RECOVERY_PASSWORD
#
# MessageText:
#
# The Group Policy setting requiring FIPS compliance prevents a local recovery password from being generated or used by BitLocker Drive Encryption. When operating in FIPS-compliant mode, BitLocker recovery options can be either a recovery key stored on a USB drive or recovery through a data recovery agent.
#
FVE_E_FIPS_PREVENTS_RECOVERY_PASSWORD = 0x80310037

#
# MessageId: FVE_E_FIPS_PREVENTS_EXTERNAL_KEY_EXPORT
#
# MessageText:
#
# The Group Policy setting requiring FIPS compliance prevents the recovery password from being saved to Active Directory. When operating in FIPS-compliant mode, BitLocker recovery options can be either a recovery key stored on a USB drive or recovery through a data recovery agent. Check your Group Policy settings configuration.
#
FVE_E_FIPS_PREVENTS_EXTERNAL_KEY_EXPORT = 0x80310038

#
# MessageId: FVE_E_NOT_DECRYPTED
#
# MessageText:
#
# The drive must be fully decrypted to complete this operation.
#
FVE_E_NOT_DECRYPTED = 0x80310039

#
# MessageId: FVE_E_INVALID_PROTECTOR_TYPE
#
# MessageText:
#
# The key protector specified cannot be used for this operation.
#
FVE_E_INVALID_PROTECTOR_TYPE = 0x8031003A

#
# MessageId: FVE_E_NO_PROTECTORS_TO_TEST
#
# MessageText:
#
# No key protectors exist on the drive to perform the hardware test.
#
FVE_E_NO_PROTECTORS_TO_TEST = 0x8031003B

#
# MessageId: FVE_E_KEYFILE_NOT_FOUND
#
# MessageText:
#
# The BitLocker startup key or recovery password cannot be found on the USB device. Verify that you have the correct USB device, that the USB device is plugged into the computer on an active USB port, restart the computer, and then try again. If the problem persists, contact the computer manufacturer for BIOS upgrade instructions.
#
FVE_E_KEYFILE_NOT_FOUND = 0x8031003C

#
# MessageId: FVE_E_KEYFILE_INVALID
#
# MessageText:
#
# The BitLocker startup key or recovery password file provided is corrupt or invalid. Verify that you have the correct startup key or recovery password file and try again.
#
FVE_E_KEYFILE_INVALID = 0x8031003D

#
# MessageId: FVE_E_KEYFILE_NO_VMK
#
# MessageText:
#
# The BitLocker encryption key cannot be obtained from the startup key or recovery password. Verify that you have the correct startup key or recovery password and try again.
#
FVE_E_KEYFILE_NO_VMK = 0x8031003E

#
# MessageId: FVE_E_TPM_DISABLED
#
# MessageText:
#
# The Trusted Platform Module (TPM) is disabled. The TPM must be enabled, initialized, and have valid ownership before it can be used with BitLocker Drive Encryption.
#
FVE_E_TPM_DISABLED = 0x8031003F

#
# MessageId: FVE_E_NOT_ALLOWED_IN_SAFE_MODE
#
# MessageText:
#
# The BitLocker configuration of the specified drive cannot be managed because this computer is currently operating in Safe Mode. While in Safe Mode, BitLocker Drive Encryption can only be used for recovery purposes.
#
FVE_E_NOT_ALLOWED_IN_SAFE_MODE = 0x80310040

#
# MessageId: FVE_E_TPM_INVALID_PCR
#
# MessageText:
#
# The Trusted Platform Module (TPM) was unable to unlock the drive. Either the system boot information changed after choosing BitLocker settings or the PIN did not match. If the problem persists after several tries, there may be a hardware or firmware problem.
#
FVE_E_TPM_INVALID_PCR = 0x80310041

#
# MessageId: FVE_E_TPM_NO_VMK
#
# MessageText:
#
# The BitLocker encryption key cannot be obtained from the Trusted Platform Module (TPM).
#
FVE_E_TPM_NO_VMK = 0x80310042

#
# MessageId: FVE_E_PIN_INVALID
#
# MessageText:
#
# The BitLocker encryption key cannot be obtained from the Trusted Platform Module (TPM) and PIN.
#
FVE_E_PIN_INVALID = 0x80310043

#
# MessageId: FVE_E_AUTH_INVALID_APPLICATION
#
# MessageText:
#
# A boot application has changed since BitLocker Drive Encryption was enabled.
#
FVE_E_AUTH_INVALID_APPLICATION = 0x80310044

#
# MessageId: FVE_E_AUTH_INVALID_CONFIG
#
# MessageText:
#
# The Boot Configuration Data (BCD) settings have changed since BitLocker Drive Encryption was enabled.
#
FVE_E_AUTH_INVALID_CONFIG = 0x80310045

#
# MessageId: FVE_E_FIPS_DISABLE_PROTECTION_NOT_ALLOWED
#
# MessageText:
#
# The Group Policy setting requiring FIPS compliance prohibits the use of unencrypted keys, which prevents BitLocker from being suspended on this drive. Please contact your domain administrator for more information.
#
FVE_E_FIPS_DISABLE_PROTECTION_NOT_ALLOWED = 0x80310046

#
# MessageId: FVE_E_FS_NOT_EXTENDED
#
# MessageText:
#
# This drive cannot be encrypted by BitLocker Drive Encryption because the file system does not extend to the end of the drive. Repartition this drive and then try again.
#
FVE_E_FS_NOT_EXTENDED = 0x80310047

#
# MessageId: FVE_E_FIRMWARE_TYPE_NOT_SUPPORTED
#
# MessageText:
#
# BitLocker Drive Encryption cannot be enabled on the operating system drive. Contact the computer manufacturer for BIOS upgrade instructions.
#
FVE_E_FIRMWARE_TYPE_NOT_SUPPORTED = 0x80310048

#
# MessageId: FVE_E_NO_LICENSE
#
# MessageText:
#
# This version of Windows does not include BitLocker Drive Encryption. To use BitLocker Drive Encryption, please upgrade the operating system.
#
FVE_E_NO_LICENSE = 0x80310049

#
# MessageId: FVE_E_NOT_ON_STACK
#
# MessageText:
#
# BitLocker Drive Encryption cannot be used because critical BitLocker system files are missing or corrupted. Use Windows Startup Repair to restore these files to your computer.
#
FVE_E_NOT_ON_STACK = 0x8031004A

#
# MessageId: FVE_E_FS_MOUNTED
#
# MessageText:
#
# The drive cannot be locked when the drive is in use.
#
FVE_E_FS_MOUNTED = 0x8031004B

#
# MessageId: FVE_E_TOKEN_NOT_IMPERSONATED
#
# MessageText:
#
# The access token associated with the current thread is not an impersonated token.
#
FVE_E_TOKEN_NOT_IMPERSONATED = 0x8031004C

#
# MessageId: FVE_E_DRY_RUN_FAILED
#
# MessageText:
#
# The BitLocker encryption key cannot be obtained. Verify that the Trusted Platform Module (TPM) is enabled and ownership has been taken. If this computer does not have a TPM, verify that the USB drive is inserted and available.
#
FVE_E_DRY_RUN_FAILED = 0x8031004D

#
# MessageId: FVE_E_REBOOT_REQUIRED
#
# MessageText:
#
# You must restart your computer before continuing with BitLocker Drive Encryption.
#
FVE_E_REBOOT_REQUIRED = 0x8031004E

#
# MessageId: FVE_E_DEBUGGER_ENABLED
#
# MessageText:
#
# Drive encryption cannot occur while boot debugging is enabled. Use the bcdedit command-line tool to turn off boot debugging.
#
FVE_E_DEBUGGER_ENABLED = 0x8031004F

#
# MessageId: FVE_E_RAW_ACCESS
#
# MessageText:
#
# No action was taken as BitLocker Drive Encryption is in raw access mode.
#
FVE_E_RAW_ACCESS = 0x80310050

#
# MessageId: FVE_E_RAW_BLOCKED
#
# MessageText:
#
# BitLocker Drive Encryption cannot enter raw access mode for this drive because the drive is currently in use.
#
FVE_E_RAW_BLOCKED = 0x80310051

#
# MessageId: FVE_E_BCD_APPLICATIONS_PATH_INCORRECT
#
# MessageText:
#
# The path specified in the Boot Configuration Data (BCD) for a BitLocker Drive Encryption integrity-protected application is incorrect. Please verify and correct your BCD settings and try again.
#
FVE_E_BCD_APPLICATIONS_PATH_INCORRECT = 0x80310052

#
# MessageId: FVE_E_NOT_ALLOWED_IN_VERSION
#
# MessageText:
#
# BitLocker Drive Encryption can only be used for limited provisioning or recovery purposes when the computer is running in pre-installation or recovery environments.
#
FVE_E_NOT_ALLOWED_IN_VERSION = 0x80310053

#
# MessageId: FVE_E_NO_AUTOUNLOCK_MASTER_KEY
#
# MessageText:
#
# The auto-unlock master key was not available from the operating system drive.
#
FVE_E_NO_AUTOUNLOCK_MASTER_KEY = 0x80310054

#
# MessageId: FVE_E_MOR_FAILED
#
# MessageText:
#
# The system firmware failed to enable clearing of system memory when the computer was restarted.
#
FVE_E_MOR_FAILED = 0x80310055

#
# MessageId: FVE_E_HIDDEN_VOLUME
#
# MessageText:
#
# The hidden drive cannot be encrypted.
#
FVE_E_HIDDEN_VOLUME = 0x80310056

#
# MessageId: FVE_E_TRANSIENT_STATE
#
# MessageText:
#
# BitLocker encryption keys were ignored because the drive was in a transient state.
#
FVE_E_TRANSIENT_STATE = 0x80310057

#
# MessageId: FVE_E_PUBKEY_NOT_ALLOWED
#
# MessageText:
#
# Public key based protectors are not allowed on this drive.
#
FVE_E_PUBKEY_NOT_ALLOWED = 0x80310058

#
# MessageId: FVE_E_VOLUME_HANDLE_OPEN
#
# MessageText:
#
# BitLocker Drive Encryption is already performing an operation on this drive. Please complete all operations before continuing.
#
FVE_E_VOLUME_HANDLE_OPEN = 0x80310059

#
# MessageId: FVE_E_NO_FEATURE_LICENSE
#
# MessageText:
#
# This version of Windows does not support this feature of BitLocker Drive Encryption. To use this feature, upgrade the operating system.
#
FVE_E_NO_FEATURE_LICENSE = 0x8031005A

#
# MessageId: FVE_E_INVALID_STARTUP_OPTIONS
#
# MessageText:
#
# The Group Policy settings for BitLocker startup options are in conflict and cannot be applied. Contact your system administrator for more information.
#
FVE_E_INVALID_STARTUP_OPTIONS = 0x8031005B

#
# MessageId: FVE_E_POLICY_RECOVERY_PASSWORD_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit the creation of a recovery password.
#
FVE_E_POLICY_RECOVERY_PASSWORD_NOT_ALLOWED = 0x8031005C

#
# MessageId: FVE_E_POLICY_RECOVERY_PASSWORD_REQUIRED
#
# MessageText:
#
# Group Policy settings require the creation of a recovery password.
#
FVE_E_POLICY_RECOVERY_PASSWORD_REQUIRED = 0x8031005D

#
# MessageId: FVE_E_POLICY_RECOVERY_KEY_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit the creation of a recovery key.
#
FVE_E_POLICY_RECOVERY_KEY_NOT_ALLOWED = 0x8031005E

#
# MessageId: FVE_E_POLICY_RECOVERY_KEY_REQUIRED
#
# MessageText:
#
# Group Policy settings require the creation of a recovery key.
#
FVE_E_POLICY_RECOVERY_KEY_REQUIRED = 0x8031005F

#
# MessageId: FVE_E_POLICY_STARTUP_PIN_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit the use of a PIN at startup. Please choose a different BitLocker startup option.
#
FVE_E_POLICY_STARTUP_PIN_NOT_ALLOWED = 0x80310060

#
# MessageId: FVE_E_POLICY_STARTUP_PIN_REQUIRED
#
# MessageText:
#
# Group Policy settings require the use of a PIN at startup. Please choose this BitLocker startup option.
#
FVE_E_POLICY_STARTUP_PIN_REQUIRED = 0x80310061

#
# MessageId: FVE_E_POLICY_STARTUP_KEY_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit the use of a startup key. Please choose a different BitLocker startup option.
#
FVE_E_POLICY_STARTUP_KEY_NOT_ALLOWED = 0x80310062

#
# MessageId: FVE_E_POLICY_STARTUP_KEY_REQUIRED
#
# MessageText:
#
# Group Policy settings require the use of a startup key. Please choose this BitLocker startup option.
#
FVE_E_POLICY_STARTUP_KEY_REQUIRED = 0x80310063

#
# MessageId: FVE_E_POLICY_STARTUP_PIN_KEY_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit the use of a startup key and PIN. Please choose a different BitLocker startup option.
#
FVE_E_POLICY_STARTUP_PIN_KEY_NOT_ALLOWED = 0x80310064

#
# MessageId: FVE_E_POLICY_STARTUP_PIN_KEY_REQUIRED
#
# MessageText:
#
# Group Policy settings require the use of a startup key and PIN. Please choose this BitLocker startup option.
#
FVE_E_POLICY_STARTUP_PIN_KEY_REQUIRED = 0x80310065

#
# MessageId: FVE_E_POLICY_STARTUP_TPM_NOT_ALLOWED
#
# MessageText:
#
# Group policy does not permit the use of TPM-only at startup. Please choose a different BitLocker startup option.
#
FVE_E_POLICY_STARTUP_TPM_NOT_ALLOWED = 0x80310066

#
# MessageId: FVE_E_POLICY_STARTUP_TPM_REQUIRED
#
# MessageText:
#
# Group Policy settings require the use of TPM-only at startup. Please choose this BitLocker startup option.
#
FVE_E_POLICY_STARTUP_TPM_REQUIRED = 0x80310067

#
# MessageId: FVE_E_POLICY_INVALID_PIN_LENGTH
#
# MessageText:
#
# The PIN provided does not meet minimum or maximum length requirements.
#
FVE_E_POLICY_INVALID_PIN_LENGTH = 0x80310068

#
# MessageId: FVE_E_KEY_PROTECTOR_NOT_SUPPORTED
#
# MessageText:
#
# The key protector is not supported by the version of BitLocker Drive Encryption currently on the drive. Upgrade the drive to add the key protector.
#
FVE_E_KEY_PROTECTOR_NOT_SUPPORTED = 0x80310069

#
# MessageId: FVE_E_POLICY_PASSPHRASE_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit the creation of a password.
#
FVE_E_POLICY_PASSPHRASE_NOT_ALLOWED = 0x8031006A

#
# MessageId: FVE_E_POLICY_PASSPHRASE_REQUIRED
#
# MessageText:
#
# Group Policy settings require the creation of a password.
#
FVE_E_POLICY_PASSPHRASE_REQUIRED = 0x8031006B

#
# MessageId: FVE_E_FIPS_PREVENTS_PASSPHRASE
#
# MessageText:
#
# The Group Policy setting requiring FIPS compliance prevents passwords from being generated or used. Please contact your system administrator for more information.
#
FVE_E_FIPS_PREVENTS_PASSPHRASE = 0x8031006C

#
# MessageId: FVE_E_OS_VOLUME_PASSPHRASE_NOT_ALLOWED
#
# MessageText:
#
# A password cannot be added to the operating system drive.
#
FVE_E_OS_VOLUME_PASSPHRASE_NOT_ALLOWED = 0x8031006D

#
# MessageId: FVE_E_INVALID_BITLOCKER_OID
#
# MessageText:
#
# The BitLocker object identifier (OID) on the drive appears to be invalid or corrupt. Use manage-BDE to reset the OID on this drive.
#
FVE_E_INVALID_BITLOCKER_OID = 0x8031006E

#
# MessageId: FVE_E_VOLUME_TOO_SMALL
#
# MessageText:
#
# The drive is too small to be protected using BitLocker Drive Encryption.
#
FVE_E_VOLUME_TOO_SMALL = 0x8031006F

#
# MessageId: FVE_E_DV_NOT_SUPPORTED_ON_FS
#
# MessageText:
#
# The selected discovery drive type is incompatible with the file system on the drive. BitLocker To Go discovery drives must be created on FAT formatted drives.
#
FVE_E_DV_NOT_SUPPORTED_ON_FS = 0x80310070

#
# MessageId: FVE_E_DV_NOT_ALLOWED_BY_GP
#
# MessageText:
#
# The selected discovery drive type is not allowed by the computer's Group Policy settings. Verify that Group Policy settings allow the creation of discovery drives for use with BitLocker To Go.
#
FVE_E_DV_NOT_ALLOWED_BY_GP = 0x80310071

#
# MessageId: FVE_E_POLICY_USER_CERTIFICATE_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit user certificates such as smart cards to be used with BitLocker Drive Encryption.
#
FVE_E_POLICY_USER_CERTIFICATE_NOT_ALLOWED = 0x80310072

#
# MessageId: FVE_E_POLICY_USER_CERTIFICATE_REQUIRED
#
# MessageText:
#
# Group Policy settings require that you have a valid user certificate, such as a smart card, to be used with BitLocker Drive Encryption.
#
FVE_E_POLICY_USER_CERTIFICATE_REQUIRED = 0x80310073

#
# MessageId: FVE_E_POLICY_USER_CERT_MUST_BE_HW
#
# MessageText:
#
# Group Policy settings requires that you use a smart card-based key protector with BitLocker Drive Encryption.
#
FVE_E_POLICY_USER_CERT_MUST_BE_HW = 0x80310074

#
# MessageId: FVE_E_POLICY_USER_CONFIGURE_FDV_AUTOUNLOCK_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit BitLocker-protected fixed data drives to be automatically unlocked.
#
FVE_E_POLICY_USER_CONFIGURE_FDV_AUTOUNLOCK_NOT_ALLOWED = 0x80310075

#
# MessageId: FVE_E_POLICY_USER_CONFIGURE_RDV_AUTOUNLOCK_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit BitLocker-protected removable data drives to be automatically unlocked.
#
FVE_E_POLICY_USER_CONFIGURE_RDV_AUTOUNLOCK_NOT_ALLOWED = 0x80310076

#
# MessageId: FVE_E_POLICY_USER_CONFIGURE_RDV_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit you to configure BitLocker Drive Encryption on removable data drives.
#
FVE_E_POLICY_USER_CONFIGURE_RDV_NOT_ALLOWED = 0x80310077

#
# MessageId: FVE_E_POLICY_USER_ENABLE_RDV_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit you to turn on BitLocker Drive Encryption on removable data drives. Please contact your system administrator if you need to turn on BitLocker.
#
FVE_E_POLICY_USER_ENABLE_RDV_NOT_ALLOWED = 0x80310078

#
# MessageId: FVE_E_POLICY_USER_DISABLE_RDV_NOT_ALLOWED
#
# MessageText:
#
# Group Policy settings do not permit turning off BitLocker Drive Encryption on removable data drives. Please contact your system administrator if you need to turn off BitLocker.
#
FVE_E_POLICY_USER_DISABLE_RDV_NOT_ALLOWED = 0x80310079

#
# MessageId: FVE_E_POLICY_INVALID_PASSPHRASE_LENGTH
#
# MessageText:
#
# Your password does not meet minimum password length requirements. By default, passwords must be at least 8 characters in length. Check with your system administrator for the password length requirement in your organization.
#
FVE_E_POLICY_INVALID_PASSPHRASE_LENGTH = 0x80310080

#
# MessageId: FVE_E_POLICY_PASSPHRASE_TOO_SIMPLE
#
# MessageText:
#
# Your password does not meet the complexity requirements set by your system administrator. Try adding upper and lowercase characters, numbers, and symbols.
#
FVE_E_POLICY_PASSPHRASE_TOO_SIMPLE = 0x80310081

#
# MessageId: FVE_E_RECOVERY_PARTITION
#
# MessageText:
#
# This drive cannot be encrypted because it is reserved for Windows System Recovery Options.
#
FVE_E_RECOVERY_PARTITION = 0x80310082

#
# MessageId: FVE_E_POLICY_CONFLICT_FDV_RK_OFF_AUK_ON
#
# MessageText:
#
# BitLocker Drive Encryption cannot be applied to this drive because of conflicting Group Policy settings. BitLocker cannot be configured to automatically unlock fixed data drives when user recovery options are disabled. If you want BitLocker-protected fixed data drives to be automatically unlocked after key validation has occurred, please ask your system administrator to resolve the settings conflict before enabling BitLocker.
#
FVE_E_POLICY_CONFLICT_FDV_RK_OFF_AUK_ON = 0x80310083

#
# MessageId: FVE_E_POLICY_CONFLICT_RDV_RK_OFF_AUK_ON
#
# MessageText:
#
# BitLocker Drive Encryption cannot be applied to this drive because of conflicting Group Policy settings. BitLocker cannot be configured to automatically unlock removable data drives when user recovery option are disabled. If you want BitLocker-protected removable data drives to be automatically unlocked after key validation has occurred, please ask your system administrator to resolve the settings conflict before enabling BitLocker.
#
FVE_E_POLICY_CONFLICT_RDV_RK_OFF_AUK_ON = 0x80310084

#
# MessageId: FVE_E_NON_BITLOCKER_OID
#
# MessageText:
#
# The Enhanced Key Usage (EKU) attribute of the specified certificate does not permit it to be used for BitLocker Drive Encryption. BitLocker does not require that a certificate have an EKU attribute, but if one is configured it must be set to an object identifier (OID) that matches the OID configured for BitLocker.
#
FVE_E_NON_BITLOCKER_OID = 0x80310085

#
# MessageId: FVE_E_POLICY_PROHIBITS_SELFSIGNED
#
# MessageText:
#
# BitLocker Drive Encryption cannot be applied to this drive as currently configured because of Group Policy settings. The certificate you provided for drive encryption is self-signed. Current Group Policy settings do not permit the use of self-signed certificates. Obtain a new certificate from your certification authority before attempting to enable BitLocker.
#
FVE_E_POLICY_PROHIBITS_SELFSIGNED = 0x80310086

#
# MessageId: FVE_E_POLICY_CONFLICT_RO_AND_STARTUP_KEY_REQUIRED
#
# MessageText:
#
# BitLocker Encryption cannot be applied to this drive because of conflicting Group Policy settings. When write access to drives not protected by BitLocker is denied, the use of a USB startup key cannot be required. Please have your system administrator resolve these policy conflicts before attempting to enable BitLocker.
#
FVE_E_POLICY_CONFLICT_RO_AND_STARTUP_KEY_REQUIRED = 0x80310087

#
# MessageId: FVE_E_CONV_RECOVERY_FAILED
#
# MessageText:
#
# BitLocker Drive Encryption failed to recover from an abruptly terminated conversion. This could be due to either all conversion logs being corrupted or the media being write-protected.
#
FVE_E_CONV_RECOVERY_FAILED = 0x80310088

#
# MessageId: FVE_E_VIRTUALIZED_SPACE_TOO_BIG
#
# MessageText:
#
# The requested virtualization size is too big.
#
FVE_E_VIRTUALIZED_SPACE_TOO_BIG = 0x80310089

#
# MessageId: FVE_E_POLICY_CONFLICT_OSV_RP_OFF_ADB_ON
#
# MessageText:
#
# BitLocker Drive Encryption cannot be applied to this drive because there are conflicting Group Policy settings for recovery options on operating system drives. Storing recovery information to Active Directory Domain Services cannot be required when the generation of recovery passwords is not permitted. Please have your system administrator resolve these policy conflicts before attempting to enable BitLocker.
#
FVE_E_POLICY_CONFLICT_OSV_RP_OFF_ADB_ON = 0x80310090

#
# MessageId: FVE_E_POLICY_CONFLICT_FDV_RP_OFF_ADB_ON
#
# MessageText:
#
# BitLocker Drive Encryption cannot be applied to this drive because there are conflicting Group Policy settings for recovery options on fixed data drives. Storing recovery information to Active Directory Domain Services cannot be required when the generation of recovery passwords is not permitted. Please have your system administrator resolve these policy conflicts before attempting to enable BitLocker.
#
FVE_E_POLICY_CONFLICT_FDV_RP_OFF_ADB_ON = 0x80310091

#
# MessageId: FVE_E_POLICY_CONFLICT_RDV_RP_OFF_ADB_ON
#
# MessageText:
#
# BitLocker Drive Encryption cannot be applied to this drive because there are conflicting Group Policy settings for recovery options on removable data drives. Storing recovery information to Active Directory Domain Services cannot be required when the generation of recovery passwords is not permitted. Please have your system administrator resolve these policy conflicts before attempting to enable BitLocker.
#
FVE_E_POLICY_CONFLICT_RDV_RP_OFF_ADB_ON = 0x80310092

#
# MessageId: FVE_E_NON_BITLOCKER_KU
#
# MessageText:
#
# The Key Usage (KU) attribute of the specified certificate does not permit it to be used for BitLocker Drive Encryption. BitLocker does not require that a certificate have a KU attribute, but if one is configured it must be set to either Key Encipherment or Key Agreement.
#
FVE_E_NON_BITLOCKER_KU = 0x80310093

#
# MessageId: FVE_E_PRIVATEKEY_AUTH_FAILED
#
# MessageText:
#
# The private key associated with the specified certificate cannot be authorized. The private key authorization was either not provided or the provided authorization was invalid.
#
FVE_E_PRIVATEKEY_AUTH_FAILED = 0x80310094

#
# MessageId: FVE_E_REMOVAL_OF_DRA_FAILED
#
# MessageText:
#
# Removal of the data recovery agent certificate must be done using the Certificates snap-in.
#
FVE_E_REMOVAL_OF_DRA_FAILED = 0x80310095

#
# MessageId: FVE_E_OPERATION_NOT_SUPPORTED_ON_VISTA_VOLUME
#
# MessageText:
#
# This drive was encrypted using the version of BitLocker Drive Encryption included with Windows Vista and Windows Server 2008 which does not support organizational identifiers. To specify organizational identifiers for this drive upgrade the drive encryption to the latest version using the "manage-bde -upgrade" command.
#
FVE_E_OPERATION_NOT_SUPPORTED_ON_VISTA_VOLUME = 0x80310096

#
# MessageId: FVE_E_CANT_LOCK_AUTOUNLOCK_ENABLED_VOLUME
#
# MessageText:
#
# The drive cannot be locked because it is automatically unlocked on this computer.  Remove the automatic unlock protector to lock this drive.
#
FVE_E_CANT_LOCK_AUTOUNLOCK_ENABLED_VOLUME = 0x80310097

#
# MessageId: FVE_E_FIPS_HASH_KDF_NOT_ALLOWED
#
# MessageText:
#
# The default BitLocker Key Derivation Function SP800-56A for ECC smart cards is not supported by your smart card. The Group Policy setting requiring FIPS-compliance prevents BitLocker from using any other key derivation function for encryption. You have to use a FIPS compliant smart card in FIPS restricted environments.
#
FVE_E_FIPS_HASH_KDF_NOT_ALLOWED = 0x80310098

#
# MessageId: FVE_E_ENH_PIN_INVALID
#
# MessageText:
#
# The BitLocker encryption key could not be obtained from the Trusted Platform Module (TPM) and enhanced PIN. Try using a PIN containing only numerals.
#
FVE_E_ENH_PIN_INVALID = 0x80310099

#
# MessageId: FVE_E_INVALID_PIN_CHARS
#
# MessageText:
#
# The requested TPM PIN contains invalid characters.
#
FVE_E_INVALID_PIN_CHARS = 0x8031009A

#
# MessageId: FVE_E_INVALID_DATUM_TYPE
#
# MessageText:
#
# The management information stored on the drive contained an unknown type. If you are using an old version of Windows, try accessing the drive from the latest version.
#
FVE_E_INVALID_DATUM_TYPE = 0x8031009B

#
# MessageId: FVE_E_EFI_ONLY
#
# MessageText:
#
# The feature is only supported on EFI systems.
#
FVE_E_EFI_ONLY = 0x8031009C

#
# MessageId: FVE_E_MULTIPLE_NKP_CERTS
#
# MessageText:
#
# More than one Network Key Protector certificate has been found on the system.
#
FVE_E_MULTIPLE_NKP_CERTS = 0x8031009D

#
# MessageId: FVE_E_REMOVAL_OF_NKP_FAILED
#
# MessageText:
#
# Removal of the Network Key Protector certificate must be done using the Certificates snap-in.
#
FVE_E_REMOVAL_OF_NKP_FAILED = 0x8031009E

#
# MessageId: FVE_E_INVALID_NKP_CERT
#
# MessageText:
#
# An invalid certificate has been found in the Network Key Protector certificate store.
#
FVE_E_INVALID_NKP_CERT = 0x8031009F

#
# MessageId: FVE_E_NO_EXISTING_PIN
#
# MessageText:
#
# This drive isn't protected with a PIN.
#
FVE_E_NO_EXISTING_PIN = 0x803100A0

#
# MessageId: FVE_E_PROTECTOR_CHANGE_PIN_MISMATCH
#
# MessageText:
#
# Please enter the correct current PIN.
#
FVE_E_PROTECTOR_CHANGE_PIN_MISMATCH = 0x803100A1

#
# MessageId: FVE_E_PIN_PROTECTOR_CHANGE_BY_STD_USER_DISALLOWED
#
# MessageText:
#
# You must be logged on with an administrator account to change the PIN. Click the link to reset the PIN as an administrator.
#
FVE_E_PIN_PROTECTOR_CHANGE_BY_STD_USER_DISALLOWED = 0x803100A2

#
# MessageId: FVE_E_PROTECTOR_CHANGE_MAX_PIN_CHANGE_ATTEMPTS_REACHED
#
# MessageText:
#
# BitLocker has disabled PIN changes after too many failed requests. Click the link to reset the PIN as an administrator.
#
FVE_E_PROTECTOR_CHANGE_MAX_PIN_CHANGE_ATTEMPTS_REACHED = 0x803100A3

#
# MessageId: FVE_E_POLICY_PASSPHRASE_REQUIRES_ASCII
#
# MessageText:
#
# Your system administrator requires that passwords contain only printable ASCII characters. This includes unaccented letters (A-Z, a-z), numbers (0-9), space, arithmetic signs, common punctuation, separators, and the following symbols: # $ & @ ^ _ ~ .
#
FVE_E_POLICY_PASSPHRASE_REQUIRES_ASCII = 0x803100A4

#
# MessageId: FVE_E_FULL_ENCRYPTION_NOT_ALLOWED_ON_TP_STORAGE
#
# MessageText:
#
# BitLocker Drive Encryption only supports Used Space Only encryption on thin provisioned storage.
#
FVE_E_FULL_ENCRYPTION_NOT_ALLOWED_ON_TP_STORAGE = 0x803100A5

#
# MessageId: FVE_E_WIPE_NOT_ALLOWED_ON_TP_STORAGE
#
# MessageText:
#
# BitLocker Drive Encryption does not support wiping free space on thin provisioned storage.
#
FVE_E_WIPE_NOT_ALLOWED_ON_TP_STORAGE = 0x803100A6

#
# MessageId: FVE_E_KEY_LENGTH_NOT_SUPPORTED_BY_EDRIVE
#
# MessageText:
#
# The required authentication key length is not supported by the drive.
#
FVE_E_KEY_LENGTH_NOT_SUPPORTED_BY_EDRIVE = 0x803100A7

#
# MessageId: FVE_E_NO_EXISTING_PASSPHRASE
#
# MessageText:
#
# This drive isn't protected with a password.
#
FVE_E_NO_EXISTING_PASSPHRASE = 0x803100A8

#
# MessageId: FVE_E_PROTECTOR_CHANGE_PASSPHRASE_MISMATCH
#
# MessageText:
#
# Please enter the correct current password.
#
FVE_E_PROTECTOR_CHANGE_PASSPHRASE_MISMATCH = 0x803100A9

#
# MessageId: FVE_E_PASSPHRASE_TOO_LONG
#
# MessageText:
#
# The password cannot exceed 256 characters.
#
FVE_E_PASSPHRASE_TOO_LONG = 0x803100AA

#
# MessageId: FVE_E_NO_PASSPHRASE_WITH_TPM
#
# MessageText:
#
# A password key protector cannot be added because a TPM protector exists on the drive.
#
FVE_E_NO_PASSPHRASE_WITH_TPM = 0x803100AB

#
# MessageId: FVE_E_NO_TPM_WITH_PASSPHRASE
#
# MessageText:
#
# A TPM key protector cannot be added because a password protector exists on the drive.
#
FVE_E_NO_TPM_WITH_PASSPHRASE = 0x803100AC

#
# MessageId: FVE_E_NOT_ALLOWED_ON_CSV_STACK
#
# MessageText:
#
# This command can only be performed from the coordinator node for the specified CSV volume.
#
FVE_E_NOT_ALLOWED_ON_CSV_STACK = 0x803100AD

#
# MessageId: FVE_E_NOT_ALLOWED_ON_CLUSTER
#
# MessageText:
#
# This command cannot be performed on a volume when it is part of a cluster.
#
FVE_E_NOT_ALLOWED_ON_CLUSTER = 0x803100AE

#
# MessageId: FVE_E_EDRIVE_NO_FAILOVER_TO_SW
#
# MessageText:
#
# BitLocker did not revert to using BitLocker software encryption due to group policy configuration.
#
FVE_E_EDRIVE_NO_FAILOVER_TO_SW = 0x803100AF

#
# MessageId: FVE_E_EDRIVE_BAND_IN_USE
#
# MessageText:
#
# The drive cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.
#
FVE_E_EDRIVE_BAND_IN_USE = 0x803100B0

#
# MessageId: FVE_E_EDRIVE_DISALLOWED_BY_GP
#
# MessageText:
#
# Group Policy settings do not allow the use of hardware-based encryption.
#
FVE_E_EDRIVE_DISALLOWED_BY_GP = 0x803100B1

#
# MessageId: FVE_E_EDRIVE_INCOMPATIBLE_VOLUME
#
# MessageText:
#
# The drive specified does not support hardware-based encryption.
#
FVE_E_EDRIVE_INCOMPATIBLE_VOLUME = 0x803100B2

#
# MessageId: FVE_E_NOT_ALLOWED_TO_UPGRADE_WHILE_CONVERTING
#
# MessageText:
#
# BitLocker cannot be upgraded during disk encryption or decryption.
#
FVE_E_NOT_ALLOWED_TO_UPGRADE_WHILE_CONVERTING = 0x803100B3

#
# MessageId: FVE_E_EDRIVE_DV_NOT_SUPPORTED
#
# MessageText:
#
# Discovery Volumes are not supported for volumes using hardware encryption.
#
FVE_E_EDRIVE_DV_NOT_SUPPORTED = 0x803100B4

#
# MessageId: FVE_E_NO_PREBOOT_KEYBOARD_DETECTED
#
# MessageText:
#
# No pre-boot keyboard detected. The user may not be able to provide required input to unlock the volume.
#
FVE_E_NO_PREBOOT_KEYBOARD_DETECTED = 0x803100B5

#
# MessageId: FVE_E_NO_PREBOOT_KEYBOARD_OR_WINRE_DETECTED
#
# MessageText:
#
# No pre-boot keyboard or Windows Recovery Environment detected. The user may not be able to provide required input to unlock the volume.
#
FVE_E_NO_PREBOOT_KEYBOARD_OR_WINRE_DETECTED = 0x803100B6

#
# MessageId: FVE_E_POLICY_REQUIRES_STARTUP_PIN_ON_TOUCH_DEVICE
#
# MessageText:
#
# Group Policy settings require the creation of a startup PIN, but a pre-boot keyboard is not available on this device. The user may not be able to provide required input to unlock the volume.
#
FVE_E_POLICY_REQUIRES_STARTUP_PIN_ON_TOUCH_DEVICE = 0x803100B7

#
# MessageId: FVE_E_POLICY_REQUIRES_RECOVERY_PASSWORD_ON_TOUCH_DEVICE
#
# MessageText:
#
# Group Policy settings require the creation of a recovery password, but neither a pre-boot keyboard nor Windows Recovery Environment is available on this device. The user may not be able to provide required input to unlock the volume.
#
FVE_E_POLICY_REQUIRES_RECOVERY_PASSWORD_ON_TOUCH_DEVICE = 0x803100B8

#
# MessageId: FVE_E_WIPE_CANCEL_NOT_APPLICABLE
#
# MessageText:
#
# Wipe of free space is not currently taking place.
#
FVE_E_WIPE_CANCEL_NOT_APPLICABLE = 0x803100B9

#
# MessageId: FVE_E_SECUREBOOT_DISABLED
#
# MessageText:
#
# BitLocker cannot use Secure Boot for platform integrity because Secure Boot has been disabled.
#
FVE_E_SECUREBOOT_DISABLED = 0x803100BA

#
# MessageId: FVE_E_SECUREBOOT_CONFIGURATION_INVALID
#
# MessageText:
#
# BitLocker cannot use Secure Boot for platform integrity because the Secure Boot configuration does not meet the requirements for BitLocker.
#
FVE_E_SECUREBOOT_CONFIGURATION_INVALID = 0x803100BB

#
# MessageId: FVE_E_EDRIVE_DRY_RUN_FAILED
#
# MessageText:
#
# Your computer doesn't support BitLocker hardware-based encryption. Check with your computer manufacturer for firmware updates.
#
FVE_E_EDRIVE_DRY_RUN_FAILED = 0x803100BC

#
# MessageId: FVE_E_SHADOW_COPY_PRESENT
#
# MessageText:
#
# BitLocker cannot be enabled on the volume because it contains a Volume Shadow Copy. Remove all Volume Shadow Copies before encrypting the volume.
#
FVE_E_SHADOW_COPY_PRESENT = 0x803100BD

#
# MessageId: FVE_E_POLICY_INVALID_ENHANCED_BCD_SETTINGS
#
# MessageText:
#
# BitLocker Drive Encryption cannot be applied to this drive because the Group Policy setting for Enhanced Boot Configuration Data contains invalid data. Please have your system administrator resolve this invalid configuration before attempting to enable BitLocker.
#
FVE_E_POLICY_INVALID_ENHANCED_BCD_SETTINGS = 0x803100BE

#
# MessageId: FVE_E_EDRIVE_INCOMPATIBLE_FIRMWARE
#
# MessageText:
#
# This PC's firmware is not capable of supporting hardware encryption.
#
FVE_E_EDRIVE_INCOMPATIBLE_FIRMWARE = 0x803100BF

#
# MessageId: FVE_E_PROTECTOR_CHANGE_MAX_PASSPHRASE_CHANGE_ATTEMPTS_REACHED
#
# MessageText:
#
# BitLocker has disabled password changes after too many failed requests. Click the link to reset the password as an administrator.
#
FVE_E_PROTECTOR_CHANGE_MAX_PASSPHRASE_CHANGE_ATTEMPTS_REACHED = 0x803100C0

#
# MessageId: FVE_E_PASSPHRASE_PROTECTOR_CHANGE_BY_STD_USER_DISALLOWED
#
# MessageText:
#
# You must be logged on with an administrator account to change the password. Click the link to reset the password as an administrator.
#
FVE_E_PASSPHRASE_PROTECTOR_CHANGE_BY_STD_USER_DISALLOWED = 0x803100C1

#
# MessageId: FVE_E_LIVEID_ACCOUNT_SUSPENDED
#
# MessageText:
#
# BitLocker cannot save the recovery password because the specified Microsoft account is Suspended.
#
FVE_E_LIVEID_ACCOUNT_SUSPENDED = 0x803100C2

#
# MessageId: FVE_E_LIVEID_ACCOUNT_BLOCKED
#
# MessageText:
#
# BitLocker cannot save the recovery password because the specified Microsoft account is Blocked.
#
FVE_E_LIVEID_ACCOUNT_BLOCKED = 0x803100C3

#
# MessageId: FVE_E_NOT_PROVISIONED_ON_ALL_VOLUMES
#
# MessageText:
#
# This PC is not provisioned to support device encryption. Please enable BitLocker on all volumes to comply with device encryption policy.
#
FVE_E_NOT_PROVISIONED_ON_ALL_VOLUMES = 0x803100C4

#
# MessageId: FVE_E_DE_FIXED_DATA_NOT_SUPPORTED
#
# MessageText:
#
# This PC cannot support device encryption because unencrypted fixed data volumes are present.
#
FVE_E_DE_FIXED_DATA_NOT_SUPPORTED = 0x803100C5

#
# MessageId: FVE_E_DE_HARDWARE_NOT_COMPLIANT
#
# MessageText:
#
# This PC does not meet the hardware requirements to support device encryption.
#
FVE_E_DE_HARDWARE_NOT_COMPLIANT = 0x803100C6

#
# MessageId: FVE_E_DE_WINRE_NOT_CONFIGURED
#
# MessageText:
#
# This PC cannot support device encryption because WinRE is not properly configured.
#
FVE_E_DE_WINRE_NOT_CONFIGURED = 0x803100C7

#
# MessageId: FVE_E_DE_PROTECTION_SUSPENDED
#
# MessageText:
#
# Protection is enabled on the volume but has been suspended. This is likely to have happened due to an update being applied to your system. Please try again after a reboot.
#
FVE_E_DE_PROTECTION_SUSPENDED = 0x803100C8

#
# MessageId: FVE_E_DE_OS_VOLUME_NOT_PROTECTED
#
# MessageText:
#
# This PC is not provisioned to support device encryption.
#
FVE_E_DE_OS_VOLUME_NOT_PROTECTED = 0x803100C9

#
# MessageId: FVE_E_DE_DEVICE_LOCKEDOUT
#
# MessageText:
#
# Device Lock has been triggered due to too many incorrect password attempts.
#
FVE_E_DE_DEVICE_LOCKEDOUT = 0x803100CA

#
# MessageId: FVE_E_DE_PROTECTION_NOT_YET_ENABLED
#
# MessageText:
#
# Protection has not been enabled on the volume. Enabling protection requires a connected account. If you already have a connected account and are seeing this error, please refer to the event log for more information.
#
FVE_E_DE_PROTECTION_NOT_YET_ENABLED = 0x803100CB

#
# MessageId: FVE_E_INVALID_PIN_CHARS_DETAILED
#
# MessageText:
#
# Your PIN can only contain numbers from 0 to 9.
#
FVE_E_INVALID_PIN_CHARS_DETAILED = 0x803100CC

#
# MessageId: FVE_E_DEVICE_LOCKOUT_COUNTER_UNAVAILABLE
#
# MessageText:
#
# BitLocker cannot use hardware replay protection because no counter is available on your PC.
#
FVE_E_DEVICE_LOCKOUT_COUNTER_UNAVAILABLE = 0x803100CD

#
# MessageId: FVE_E_DEVICELOCKOUT_COUNTER_MISMATCH
#
# MessageText:
#
# Device Lockout state validation failed due to counter mismatch.
#
FVE_E_DEVICELOCKOUT_COUNTER_MISMATCH = 0x803100CE

#
# MessageId: FVE_E_BUFFER_TOO_LARGE
#
# MessageText:
#
# The input buffer is too large.
#
FVE_E_BUFFER_TOO_LARGE = 0x803100CF

#
# MessageId: FVE_E_NO_SUCH_CAPABILITY_ON_TARGET
#
# MessageText:
#
# The target of an invocation does not support requested capability.
#
FVE_E_NO_SUCH_CAPABILITY_ON_TARGET = 0x803100D0

#
# MessageId: FVE_E_DE_PREVENTED_FOR_OS
#
# MessageText:
#
# Device encryption is currently blocked by this PC's configuration.
#
FVE_E_DE_PREVENTED_FOR_OS = 0x803100D1

#
# MessageId: FVE_E_DE_VOLUME_OPTED_OUT
#
# MessageText:
#
# This drive has been opted out of device encryption.
#
FVE_E_DE_VOLUME_OPTED_OUT = 0x803100D2

#
# MessageId: FVE_E_DE_VOLUME_NOT_SUPPORTED
#
# MessageText:
#
# Device encryption isn't available for this drive.
#
FVE_E_DE_VOLUME_NOT_SUPPORTED = 0x803100D3

#
# MessageId: FVE_E_EOW_NOT_SUPPORTED_IN_VERSION
#
# MessageText:
#
# The encrypt on write mode for BitLocker is not supported in this version of Windows. You can turn on BitLocker without using the encrypt on write mode.
#
FVE_E_EOW_NOT_SUPPORTED_IN_VERSION = 0x803100D4

#
# MessageId: FVE_E_ADBACKUP_NOT_ENABLED
#
# MessageText:
#
# Group policy prevents you from backing up your recovery password to Active Directory for this drive type. For more info, contact your system administrator.
#
FVE_E_ADBACKUP_NOT_ENABLED = 0x803100D5

#
# MessageId: FVE_E_VOLUME_EXTEND_PREVENTS_EOW_DECRYPT
#
# MessageText:
#
# Device encryption can't be turned off while this drive is being encrypted. Please try again later.
#
FVE_E_VOLUME_EXTEND_PREVENTS_EOW_DECRYPT = 0x803100D6

#
# MessageId: FVE_E_NOT_DE_VOLUME
#
# MessageText:
#
# This action isn't supported because this drive isn't automatically managed with device encryption.
#
FVE_E_NOT_DE_VOLUME = 0x803100D7

#
# MessageId: FVE_E_PROTECTION_CANNOT_BE_DISABLED
#
# MessageText:
#
# BitLocker can't be suspended on this drive until the next restart.
#
FVE_E_PROTECTION_CANNOT_BE_DISABLED = 0x803100D8

#
# =======================================================
# Windows Filtering Platform Error Messages
# =======================================================
#
#
# MessageId: FWP_E_CALLOUT_NOT_FOUND
#
# MessageText:
#
# The callout does not exist.
#
FWP_E_CALLOUT_NOT_FOUND = 0x80320001

#
# MessageId: FWP_E_CONDITION_NOT_FOUND
#
# MessageText:
#
# The filter condition does not exist.
#
FWP_E_CONDITION_NOT_FOUND = 0x80320002

#
# MessageId: FWP_E_FILTER_NOT_FOUND
#
# MessageText:
#
# The filter does not exist.
#
FWP_E_FILTER_NOT_FOUND = 0x80320003

#
# MessageId: FWP_E_LAYER_NOT_FOUND
#
# MessageText:
#
# The layer does not exist.
#
FWP_E_LAYER_NOT_FOUND = 0x80320004

#
# MessageId: FWP_E_PROVIDER_NOT_FOUND
#
# MessageText:
#
# The provider does not exist.
#
FWP_E_PROVIDER_NOT_FOUND = 0x80320005

#
# MessageId: FWP_E_PROVIDER_CONTEXT_NOT_FOUND
#
# MessageText:
#
# The provider context does not exist.
#
FWP_E_PROVIDER_CONTEXT_NOT_FOUND = 0x80320006

#
# MessageId: FWP_E_SUBLAYER_NOT_FOUND
#
# MessageText:
#
# The sublayer does not exist.
#
FWP_E_SUBLAYER_NOT_FOUND = 0x80320007

#
# MessageId: FWP_E_NOT_FOUND
#
# MessageText:
#
# The object does not exist.
#
FWP_E_NOT_FOUND = 0x80320008

#
# MessageId: FWP_E_ALREADY_EXISTS
#
# MessageText:
#
# An object with that GUID or LUID already exists.
#
FWP_E_ALREADY_EXISTS = 0x80320009

#
# MessageId: FWP_E_IN_USE
#
# MessageText:
#
# The object is referenced by other objects so cannot be deleted.
#
FWP_E_IN_USE = 0x8032000A

#
# MessageId: FWP_E_DYNAMIC_SESSION_IN_PROGRESS
#
# MessageText:
#
# The call is not allowed from within a dynamic session.
#
FWP_E_DYNAMIC_SESSION_IN_PROGRESS = 0x8032000B

#
# MessageId: FWP_E_WRONG_SESSION
#
# MessageText:
#
# The call was made from the wrong session so cannot be completed.
#
FWP_E_WRONG_SESSION = 0x8032000C

#
# MessageId: FWP_E_NO_TXN_IN_PROGRESS
#
# MessageText:
#
# The call must be made from within an explicit transaction.
#
FWP_E_NO_TXN_IN_PROGRESS = 0x8032000D

#
# MessageId: FWP_E_TXN_IN_PROGRESS
#
# MessageText:
#
# The call is not allowed from within an explicit transaction.
#
FWP_E_TXN_IN_PROGRESS = 0x8032000E

#
# MessageId: FWP_E_TXN_ABORTED
#
# MessageText:
#
# The explicit transaction has been forcibly cancelled.
#
FWP_E_TXN_ABORTED = 0x8032000F

#
# MessageId: FWP_E_SESSION_ABORTED
#
# MessageText:
#
# The session has been cancelled.
#
FWP_E_SESSION_ABORTED = 0x80320010

#
# MessageId: FWP_E_INCOMPATIBLE_TXN
#
# MessageText:
#
# The call is not allowed from within a read-only transaction.
#
FWP_E_INCOMPATIBLE_TXN = 0x80320011

#
# MessageId: FWP_E_TIMEOUT
#
# MessageText:
#
# The call timed out while waiting to acquire the transaction lock.
#
FWP_E_TIMEOUT = 0x80320012

#
# MessageId: FWP_E_NET_EVENTS_DISABLED
#
# MessageText:
#
# Collection of network diagnostic events is disabled.
#
FWP_E_NET_EVENTS_DISABLED = 0x80320013

#
# MessageId: FWP_E_INCOMPATIBLE_LAYER
#
# MessageText:
#
# The operation is not supported by the specified layer.
#
FWP_E_INCOMPATIBLE_LAYER = 0x80320014

#
# MessageId: FWP_E_KM_CLIENTS_ONLY
#
# MessageText:
#
# The call is allowed for kernel-mode callers only.
#
FWP_E_KM_CLIENTS_ONLY = 0x80320015

#
# MessageId: FWP_E_LIFETIME_MISMATCH
#
# MessageText:
#
# The call tried to associate two objects with incompatible lifetimes.
#
FWP_E_LIFETIME_MISMATCH = 0x80320016

#
# MessageId: FWP_E_BUILTIN_OBJECT
#
# MessageText:
#
# The object is built in so cannot be deleted.
#
FWP_E_BUILTIN_OBJECT = 0x80320017

#
# MessageId: FWP_E_TOO_MANY_CALLOUTS
#
# MessageText:
#
# The maximum number of callouts has been reached.
#
FWP_E_TOO_MANY_CALLOUTS = 0x80320018

#
# MessageId: FWP_E_NOTIFICATION_DROPPED
#
# MessageText:
#
# A notification could not be delivered because a message queue is at its maximum capacity.
#
FWP_E_NOTIFICATION_DROPPED = 0x80320019

#
# MessageId: FWP_E_TRAFFIC_MISMATCH
#
# MessageText:
#
# The traffic parameters do not match those for the security association context.
#
FWP_E_TRAFFIC_MISMATCH = 0x8032001A

#
# MessageId: FWP_E_INCOMPATIBLE_SA_STATE
#
# MessageText:
#
# The call is not allowed for the current security association state.
#
FWP_E_INCOMPATIBLE_SA_STATE = 0x8032001B

#
# MessageId: FWP_E_NULL_POINTER
#
# MessageText:
#
# A required pointer is null.
#
FWP_E_NULL_POINTER = 0x8032001C

#
# MessageId: FWP_E_INVALID_ENUMERATOR
#
# MessageText:
#
# An enumerator is not valid.
#
FWP_E_INVALID_ENUMERATOR = 0x8032001D

#
# MessageId: FWP_E_INVALID_FLAGS
#
# MessageText:
#
# The flags field contains an invalid value.
#
FWP_E_INVALID_FLAGS = 0x8032001E

#
# MessageId: FWP_E_INVALID_NET_MASK
#
# MessageText:
#
# A network mask is not valid.
#
FWP_E_INVALID_NET_MASK = 0x8032001F

#
# MessageId: FWP_E_INVALID_RANGE
#
# MessageText:
#
# An FWP_RANGE is not valid.
#
FWP_E_INVALID_RANGE = 0x80320020

#
# MessageId: FWP_E_INVALID_INTERVAL
#
# MessageText:
#
# The time interval is not valid.
#
FWP_E_INVALID_INTERVAL = 0x80320021

#
# MessageId: FWP_E_ZERO_LENGTH_ARRAY
#
# MessageText:
#
# An array that must contain at least one element is zero length.
#
FWP_E_ZERO_LENGTH_ARRAY = 0x80320022

#
# MessageId: FWP_E_NULL_DISPLAY_NAME
#
# MessageText:
#
# The displayData.name field cannot be null.
#
FWP_E_NULL_DISPLAY_NAME = 0x80320023

#
# MessageId: FWP_E_INVALID_ACTION_TYPE
#
# MessageText:
#
# The action type is not one of the allowed action types for a filter.
#
FWP_E_INVALID_ACTION_TYPE = 0x80320024

#
# MessageId: FWP_E_INVALID_WEIGHT
#
# MessageText:
#
# The filter weight is not valid.
#
FWP_E_INVALID_WEIGHT = 0x80320025

#
# MessageId: FWP_E_MATCH_TYPE_MISMATCH
#
# MessageText:
#
# A filter condition contains a match type that is not compatible with the operands.
#
FWP_E_MATCH_TYPE_MISMATCH = 0x80320026

#
# MessageId: FWP_E_TYPE_MISMATCH
#
# MessageText:
#
# An FWP_VALUE or FWPM_CONDITION_VALUE is of the wrong type.
#
FWP_E_TYPE_MISMATCH = 0x80320027

#
# MessageId: FWP_E_OUT_OF_BOUNDS
#
# MessageText:
#
# An integer value is outside the allowed range.
#
FWP_E_OUT_OF_BOUNDS = 0x80320028

#
# MessageId: FWP_E_RESERVED
#
# MessageText:
#
# A reserved field is non-zero.
#
FWP_E_RESERVED = 0x80320029

#
# MessageId: FWP_E_DUPLICATE_CONDITION
#
# MessageText:
#
# A filter cannot contain multiple conditions operating on a single field.
#
FWP_E_DUPLICATE_CONDITION = 0x8032002A

#
# MessageId: FWP_E_DUPLICATE_KEYMOD
#
# MessageText:
#
# A policy cannot contain the same keying module more than once.
#
FWP_E_DUPLICATE_KEYMOD = 0x8032002B

#
# MessageId: FWP_E_ACTION_INCOMPATIBLE_WITH_LAYER
#
# MessageText:
#
# The action type is not compatible with the layer.
#
FWP_E_ACTION_INCOMPATIBLE_WITH_LAYER = 0x8032002C

#
# MessageId: FWP_E_ACTION_INCOMPATIBLE_WITH_SUBLAYER
#
# MessageText:
#
# The action type is not compatible with the sublayer.
#
FWP_E_ACTION_INCOMPATIBLE_WITH_SUBLAYER = 0x8032002D

#
# MessageId: FWP_E_CONTEXT_INCOMPATIBLE_WITH_LAYER
#
# MessageText:
#
# The raw context or the provider context is not compatible with the layer.
#
FWP_E_CONTEXT_INCOMPATIBLE_WITH_LAYER = 0x8032002E

#
# MessageId: FWP_E_CONTEXT_INCOMPATIBLE_WITH_CALLOUT
#
# MessageText:
#
# The raw context or the provider context is not compatible with the callout.
#
FWP_E_CONTEXT_INCOMPATIBLE_WITH_CALLOUT = 0x8032002F

#
# MessageId: FWP_E_INCOMPATIBLE_AUTH_METHOD
#
# MessageText:
#
# The authentication method is not compatible with the policy type.
#
FWP_E_INCOMPATIBLE_AUTH_METHOD = 0x80320030

#
# MessageId: FWP_E_INCOMPATIBLE_DH_GROUP
#
# MessageText:
#
# The Diffie-Hellman group is not compatible with the policy type.
#
FWP_E_INCOMPATIBLE_DH_GROUP = 0x80320031

#
# MessageId: FWP_E_EM_NOT_SUPPORTED
#
# MessageText:
#
# An IKE policy cannot contain an Extended Mode policy.
#
FWP_E_EM_NOT_SUPPORTED = 0x80320032

#
# MessageId: FWP_E_NEVER_MATCH
#
# MessageText:
#
# The enumeration template or subscription will never match any objects.
#
FWP_E_NEVER_MATCH = 0x80320033

#
# MessageId: FWP_E_PROVIDER_CONTEXT_MISMATCH
#
# MessageText:
#
# The provider context is of the wrong type.
#
FWP_E_PROVIDER_CONTEXT_MISMATCH = 0x80320034

#
# MessageId: FWP_E_INVALID_PARAMETER
#
# MessageText:
#
# The parameter is incorrect.
#
FWP_E_INVALID_PARAMETER = 0x80320035

#
# MessageId: FWP_E_TOO_MANY_SUBLAYERS
#
# MessageText:
#
# The maximum number of sublayers has been reached.
#
FWP_E_TOO_MANY_SUBLAYERS = 0x80320036

#
# MessageId: FWP_E_CALLOUT_NOTIFICATION_FAILED
#
# MessageText:
#
# The notification function for a callout returned an error.
#
FWP_E_CALLOUT_NOTIFICATION_FAILED = 0x80320037

#
# MessageId: FWP_E_INVALID_AUTH_TRANSFORM
#
# MessageText:
#
# The IPsec authentication transform is not valid.
#
FWP_E_INVALID_AUTH_TRANSFORM = 0x80320038

#
# MessageId: FWP_E_INVALID_CIPHER_TRANSFORM
#
# MessageText:
#
# The IPsec cipher transform is not valid.
#
FWP_E_INVALID_CIPHER_TRANSFORM = 0x80320039

#
# MessageId: FWP_E_INCOMPATIBLE_CIPHER_TRANSFORM
#
# MessageText:
#
# The IPsec cipher transform is not compatible with the policy.
#
FWP_E_INCOMPATIBLE_CIPHER_TRANSFORM = 0x8032003A

#
# MessageId: FWP_E_INVALID_TRANSFORM_COMBINATION
#
# MessageText:
#
# The combination of IPsec transform types is not valid.
#
FWP_E_INVALID_TRANSFORM_COMBINATION = 0x8032003B

#
# MessageId: FWP_E_DUPLICATE_AUTH_METHOD
#
# MessageText:
#
# A policy cannot contain the same auth method more than once.
#
FWP_E_DUPLICATE_AUTH_METHOD = 0x8032003C

#
# MessageId: FWP_E_INVALID_TUNNEL_ENDPOINT
#
# MessageText:
#
# A tunnel endpoint configuration is invalid.
#
FWP_E_INVALID_TUNNEL_ENDPOINT = 0x8032003D

#
# MessageId: FWP_E_L2_DRIVER_NOT_READY
#
# MessageText:
#
# The WFP MAC Layers are not ready.
#
FWP_E_L = 2

#
# MessageId: FWP_E_KEY_DICTATOR_ALREADY_REGISTERED
#
# MessageText:
#
# A key manager capable of key dictation is already registered
#
FWP_E_KEY_DICTATOR_ALREADY_REGISTERED = 0x8032003F

#
# MessageId: FWP_E_KEY_DICTATION_INVALID_KEYING_MATERIAL
#
# MessageText:
#
# A key manager dictated invalid keys
#
FWP_E_KEY_DICTATION_INVALID_KEYING_MATERIAL = 0x80320040

#
# MessageId: FWP_E_CONNECTIONS_DISABLED
#
# MessageText:
#
# The BFE IPsec Connection Tracking is disabled.
#
FWP_E_CONNECTIONS_DISABLED = 0x80320041

#
# MessageId: FWP_E_INVALID_DNS_NAME
#
# MessageText:
#
# The DNS name is invalid.
#
FWP_E_INVALID_DNS_NAME = 0x80320042

#
# MessageId: FWP_E_STILL_ON
#
# MessageText:
#
# The engine option is still enabled due to other configuration settings.
#
FWP_E_STILL_ON = 0x80320043

#
# MessageId: FWP_E_IKEEXT_NOT_RUNNING
#
# MessageText:
#
# The IKEEXT service is not running.  This service only runs when there is IPsec policy applied to the machine.
#
FWP_E_IKEEXT_NOT_RUNNING = 0x80320044

#
# MessageId: FWP_E_DROP_NOICMP
#
# MessageText:
#
# The packet should be dropped, no ICMP should be sent.
#
FWP_E_DROP_NOICMP = 0x80320104


#/////////////////////////////////////////////////
#                                               //
#       Web Services Platform Error Codes       //
#                                               //
#/////////////////////////////////////////////////

#
# MessageId: WS_S_ASYNC
#
# MessageText:
#
# The function call is completing asynchronously.
#
WS_S_ASYNC = 0x003D0000

#
# MessageId: WS_S_END
#
# MessageText:
#
# There are no more messages available on the channel.
#
WS_S_END = 0x003D0001

#
# MessageId: WS_E_INVALID_FORMAT
#
# MessageText:
#
# The input data was not in the expected format or did not have the expected value.
#
WS_E_INVALID_FORMAT = 0x803D0000

#
# MessageId: WS_E_OBJECT_FAULTED
#
# MessageText:
#
# The operation could not be completed because the object is in a faulted state due to a previous error.
#
WS_E_OBJECT_FAULTED = 0x803D0001

#
# MessageId: WS_E_NUMERIC_OVERFLOW
#
# MessageText:
#
# The operation could not be completed because it would lead to numeric overflow.
#
WS_E_NUMERIC_OVERFLOW = 0x803D0002

#
# MessageId: WS_E_INVALID_OPERATION
#
# MessageText:
#
# The operation is not allowed due to the current state of the object.
#
WS_E_INVALID_OPERATION = 0x803D0003

#
# MessageId: WS_E_OPERATION_ABORTED
#
# MessageText:
#
# The operation was aborted.
#
WS_E_OPERATION_ABORTED = 0x803D0004

#
# MessageId: WS_E_ENDPOINT_ACCESS_DENIED
#
# MessageText:
#
# Access was denied by the remote endpoint.
#
WS_E_ENDPOINT_ACCESS_DENIED = 0x803D0005

#
# MessageId: WS_E_OPERATION_TIMED_OUT
#
# MessageText:
#
# The operation did not complete within the time allotted.
#
WS_E_OPERATION_TIMED_OUT = 0x803D0006

#
# MessageId: WS_E_OPERATION_ABANDONED
#
# MessageText:
#
# The operation was abandoned.
#
WS_E_OPERATION_ABANDONED = 0x803D0007

#
# MessageId: WS_E_QUOTA_EXCEEDED
#
# MessageText:
#
# A quota was exceeded.
#
WS_E_QUOTA_EXCEEDED = 0x803D0008

#
# MessageId: WS_E_NO_TRANSLATION_AVAILABLE
#
# MessageText:
#
# The information was not available in the specified language.
#
WS_E_NO_TRANSLATION_AVAILABLE = 0x803D0009

#
# MessageId: WS_E_SECURITY_VERIFICATION_FAILURE
#
# MessageText:
#
# Security verification was not successful for the received data.
#
WS_E_SECURITY_VERIFICATION_FAILURE = 0x803D000A

#
# MessageId: WS_E_ADDRESS_IN_USE
#
# MessageText:
#
# The address is already being used.
#
WS_E_ADDRESS_IN_USE = 0x803D000B

#
# MessageId: WS_E_ADDRESS_NOT_AVAILABLE
#
# MessageText:
#
# The address is not valid for this context.
#
WS_E_ADDRESS_NOT_AVAILABLE = 0x803D000C

#
# MessageId: WS_E_ENDPOINT_NOT_FOUND
#
# MessageText:
#
# The remote endpoint does not exist or could not be located.
#
WS_E_ENDPOINT_NOT_FOUND = 0x803D000D

#
# MessageId: WS_E_ENDPOINT_NOT_AVAILABLE
#
# MessageText:
#
# The remote endpoint is not currently in service at this location.
#
WS_E_ENDPOINT_NOT_AVAILABLE = 0x803D000E

#
# MessageId: WS_E_ENDPOINT_FAILURE
#
# MessageText:
#
# The remote endpoint could not process the request.
#
WS_E_ENDPOINT_FAILURE = 0x803D000F

#
# MessageId: WS_E_ENDPOINT_UNREACHABLE
#
# MessageText:
#
# The remote endpoint was not reachable.
#
WS_E_ENDPOINT_UNREACHABLE = 0x803D0010

#
# MessageId: WS_E_ENDPOINT_ACTION_NOT_SUPPORTED
#
# MessageText:
#
# The operation was not supported by the remote endpoint.
#
WS_E_ENDPOINT_ACTION_NOT_SUPPORTED = 0x803D0011

#
# MessageId: WS_E_ENDPOINT_TOO_BUSY
#
# MessageText:
#
# The remote endpoint is unable to process the request due to being overloaded.
#
WS_E_ENDPOINT_TOO_BUSY = 0x803D0012

#
# MessageId: WS_E_ENDPOINT_FAULT_RECEIVED
#
# MessageText:
#
# A message containing a fault was received from the remote endpoint.
#
WS_E_ENDPOINT_FAULT_RECEIVED = 0x803D0013

#
# MessageId: WS_E_ENDPOINT_DISCONNECTED
#
# MessageText:
#
# The connection with the remote endpoint was terminated.
#
WS_E_ENDPOINT_DISCONNECTED = 0x803D0014

#
# MessageId: WS_E_PROXY_FAILURE
#
# MessageText:
#
# The HTTP proxy server could not process the request.
#
WS_E_PROXY_FAILURE = 0x803D0015

#
# MessageId: WS_E_PROXY_ACCESS_DENIED
#
# MessageText:
#
# Access was denied by the HTTP proxy server.
#
WS_E_PROXY_ACCESS_DENIED = 0x803D0016

#
# MessageId: WS_E_NOT_SUPPORTED
#
# MessageText:
#
# The requested feature is not available on this platform.
#
WS_E_NOT_SUPPORTED = 0x803D0017

#
# MessageId: WS_E_PROXY_REQUIRES_BASIC_AUTH
#
# MessageText:
#
# The HTTP proxy server requires HTTP authentication scheme 'basic'.
#
WS_E_PROXY_REQUIRES_BASIC_AUTH = 0x803D0018

#
# MessageId: WS_E_PROXY_REQUIRES_DIGEST_AUTH
#
# MessageText:
#
# The HTTP proxy server requires HTTP authentication scheme 'digest'.
#
WS_E_PROXY_REQUIRES_DIGEST_AUTH = 0x803D0019

#
# MessageId: WS_E_PROXY_REQUIRES_NTLM_AUTH
#
# MessageText:
#
# The HTTP proxy server requires HTTP authentication scheme 'NTLM'.
#
WS_E_PROXY_REQUIRES_NTLM_AUTH = 0x803D001A

#
# MessageId: WS_E_PROXY_REQUIRES_NEGOTIATE_AUTH
#
# MessageText:
#
# The HTTP proxy server requires HTTP authentication scheme 'negotiate'.
#
WS_E_PROXY_REQUIRES_NEGOTIATE_AUTH = 0x803D001B

#
# MessageId: WS_E_SERVER_REQUIRES_BASIC_AUTH
#
# MessageText:
#
# The remote endpoint requires HTTP authentication scheme 'basic'.
#
WS_E_SERVER_REQUIRES_BASIC_AUTH = 0x803D001C

#
# MessageId: WS_E_SERVER_REQUIRES_DIGEST_AUTH
#
# MessageText:
#
# The remote endpoint requires HTTP authentication scheme 'digest'.
#
WS_E_SERVER_REQUIRES_DIGEST_AUTH = 0x803D001D

#
# MessageId: WS_E_SERVER_REQUIRES_NTLM_AUTH
#
# MessageText:
#
# The remote endpoint requires HTTP authentication scheme 'NTLM'.
#
WS_E_SERVER_REQUIRES_NTLM_AUTH = 0x803D001E

#
# MessageId: WS_E_SERVER_REQUIRES_NEGOTIATE_AUTH
#
# MessageText:
#
# The remote endpoint requires HTTP authentication scheme 'negotiate'.
#
WS_E_SERVER_REQUIRES_NEGOTIATE_AUTH = 0x803D001F

#
# MessageId: WS_E_INVALID_ENDPOINT_URL
#
# MessageText:
#
# The endpoint address URL is invalid.
#
WS_E_INVALID_ENDPOINT_URL = 0x803D0020

#
# MessageId: WS_E_OTHER
#
# MessageText:
#
# Unrecognized error occurred in the Windows Web Services framework.
#
WS_E_OTHER = 0x803D0021

#
# MessageId: WS_E_SECURITY_TOKEN_EXPIRED
#
# MessageText:
#
# A security token was rejected by the server because it has expired.
#
WS_E_SECURITY_TOKEN_EXPIRED = 0x803D0022

#
# MessageId: WS_E_SECURITY_SYSTEM_FAILURE
#
# MessageText:
#
# A security operation failed in the Windows Web Services framework.
#
WS_E_SECURITY_SYSTEM_FAILURE = 0x803D0023


#
# NDIS error codes (ndis.sys)
#


#ifdef RC_INVOKED
#define _NDIS_ERROR_TYPEDEF_(_sc)  _sc
#else // RC_INVOKED
#define _NDIS_ERROR_TYPEDEF_(_sc)  (DWORD)(_sc)
#endif // RC_INVOKED

#
# MessageId: ERROR_NDIS_INTERFACE_CLOSING
#
# MessageText:
#
# The binding to the network interface is being closed.
#
ERROR_NDIS_INTERFACE_CLOSING = 0x80340002

#
# MessageId: ERROR_NDIS_BAD_VERSION
#
# MessageText:
#
# An invalid version was specified.
#
ERROR_NDIS_BAD_VERSION = 0x80340004

#
# MessageId: ERROR_NDIS_BAD_CHARACTERISTICS
#
# MessageText:
#
# An invalid characteristics table was used.
#
ERROR_NDIS_BAD_CHARACTERISTICS = 0x80340005

#
# MessageId: ERROR_NDIS_ADAPTER_NOT_FOUND
#
# MessageText:
#
# Failed to find the network interface or network interface is not ready.
#
ERROR_NDIS_ADAPTER_NOT_FOUND = 0x80340006

#
# MessageId: ERROR_NDIS_OPEN_FAILED
#
# MessageText:
#
# Failed to open the network interface.
#
ERROR_NDIS_OPEN_FAILED = 0x80340007

#
# MessageId: ERROR_NDIS_DEVICE_FAILED
#
# MessageText:
#
# Network interface has encountered an internal unrecoverable failure.
#
ERROR_NDIS_DEVICE_FAILED = 0x80340008

#
# MessageId: ERROR_NDIS_MULTICAST_FULL
#
# MessageText:
#
# The multicast list on the network interface is full.
#
ERROR_NDIS_MULTICAST_FULL = 0x80340009

#
# MessageId: ERROR_NDIS_MULTICAST_EXISTS
#
# MessageText:
#
# An attempt was made to add a duplicate multicast address to the list.
#
ERROR_NDIS_MULTICAST_EXISTS = 0x8034000A

#
# MessageId: ERROR_NDIS_MULTICAST_NOT_FOUND
#
# MessageText:
#
# At attempt was made to remove a multicast address that was never added.
#
ERROR_NDIS_MULTICAST_NOT_FOUND = 0x8034000B

#
# MessageId: ERROR_NDIS_REQUEST_ABORTED
#
# MessageText:
#
# Netowork interface aborted the request.
#
ERROR_NDIS_REQUEST_ABORTED = 0x8034000C

#
# MessageId: ERROR_NDIS_RESET_IN_PROGRESS
#
# MessageText:
#
# Network interface can not process the request because it is being reset.
#
ERROR_NDIS_RESET_IN_PROGRESS = 0x8034000D

#
# MessageId: ERROR_NDIS_NOT_SUPPORTED
#
# MessageText:
#
# Netword interface does not support this request.
#
ERROR_NDIS_NOT_SUPPORTED = 0x803400BB

#
# MessageId: ERROR_NDIS_INVALID_PACKET
#
# MessageText:
#
# An attempt was made to send an invalid packet on a network interface.
#
ERROR_NDIS_INVALID_PACKET = 0x8034000F

#
# MessageId: ERROR_NDIS_ADAPTER_NOT_READY
#
# MessageText:
#
# Network interface is not ready to complete this operation.
#
ERROR_NDIS_ADAPTER_NOT_READY = 0x80340011

#
# MessageId: ERROR_NDIS_INVALID_LENGTH
#
# MessageText:
#
# The length of the buffer submitted for this operation is not valid.
#
ERROR_NDIS_INVALID_LENGTH = 0x80340014

#
# MessageId: ERROR_NDIS_INVALID_DATA
#
# MessageText:
#
# The data used for this operation is not valid.
#
ERROR_NDIS_INVALID_DATA = 0x80340015

#
# MessageId: ERROR_NDIS_BUFFER_TOO_SHORT
#
# MessageText:
#
# The length of buffer submitted for this operation is too small.
#
ERROR_NDIS_BUFFER_TOO_SHORT = 0x80340016

#
# MessageId: ERROR_NDIS_INVALID_OID
#
# MessageText:
#
# Network interface does not support this OID (Object Identifier)
#
ERROR_NDIS_INVALID_OID = 0x80340017

#
# MessageId: ERROR_NDIS_ADAPTER_REMOVED
#
# MessageText:
#
# The network interface has been removed.
#
ERROR_NDIS_ADAPTER_REMOVED = 0x80340018

#
# MessageId: ERROR_NDIS_UNSUPPORTED_MEDIA
#
# MessageText:
#
# Network interface does not support this media type.
#
ERROR_NDIS_UNSUPPORTED_MEDIA = 0x80340019

#
# MessageId: ERROR_NDIS_GROUP_ADDRESS_IN_USE
#
# MessageText:
#
# An attempt was made to remove a token ring group address that is in use by other components.
#
ERROR_NDIS_GROUP_ADDRESS_IN_USE = 0x8034001A

#
# MessageId: ERROR_NDIS_FILE_NOT_FOUND
#
# MessageText:
#
# An attempt was made to map a file that can not be found.
#
ERROR_NDIS_FILE_NOT_FOUND = 0x8034001B

#
# MessageId: ERROR_NDIS_ERROR_READING_FILE
#
# MessageText:
#
# An error occurred while NDIS tried to map the file.
#
ERROR_NDIS_ERROR_READING_FILE = 0x8034001C

#
# MessageId: ERROR_NDIS_ALREADY_MAPPED
#
# MessageText:
#
# An attempt was made to map a file that is alreay mapped.
#
ERROR_NDIS_ALREADY_MAPPED = 0x8034001D

#
# MessageId: ERROR_NDIS_RESOURCE_CONFLICT
#
# MessageText:
#
# An attempt to allocate a hardware resource failed because the resource is used by another component.
#
ERROR_NDIS_RESOURCE_CONFLICT = 0x8034001E

#
# MessageId: ERROR_NDIS_MEDIA_DISCONNECTED
#
# MessageText:
#
# The I/O operation failed because network media is disconnected or wireless access point is out of range.
#
ERROR_NDIS_MEDIA_DISCONNECTED = 0x8034001F

#
# MessageId: ERROR_NDIS_INVALID_ADDRESS
#
# MessageText:
#
# The network address used in the request is invalid.
#
ERROR_NDIS_INVALID_ADDRESS = 0x80340022

#
# MessageId: ERROR_NDIS_INVALID_DEVICE_REQUEST
#
# MessageText:
#
# The specified request is not a valid operation for the target device.
#
ERROR_NDIS_INVALID_DEVICE_REQUEST = 0x80340010

#
# MessageId: ERROR_NDIS_PAUSED
#
# MessageText:
#
# The offload operation on the network interface has been paused.
#
ERROR_NDIS_PAUSED = 0x8034002A

#
# MessageId: ERROR_NDIS_INTERFACE_NOT_FOUND
#
# MessageText:
#
# Network interface was not found.
#
ERROR_NDIS_INTERFACE_NOT_FOUND = 0x8034002B

#
# MessageId: ERROR_NDIS_UNSUPPORTED_REVISION
#
# MessageText:
#
# The revision number specified in the structure is not supported.
#
ERROR_NDIS_UNSUPPORTED_REVISION = 0x8034002C

#
# MessageId: ERROR_NDIS_INVALID_PORT
#
# MessageText:
#
# The specified port does not exist on this network interface.
#
ERROR_NDIS_INVALID_PORT = 0x8034002D

#
# MessageId: ERROR_NDIS_INVALID_PORT_STATE
#
# MessageText:
#
# The current state of the specified port on this network interface does not support the requested operation.
#
ERROR_NDIS_INVALID_PORT_STATE = 0x8034002E

#
# MessageId: ERROR_NDIS_LOW_POWER_STATE
#
# MessageText:
#
# The miniport adapter is in low power state.
#
ERROR_NDIS_LOW_POWER_STATE = 0x8034002F

#
# MessageId: ERROR_NDIS_REINIT_REQUIRED
#
# MessageText:
#
# This operation requires the miniport adapter to be reinitialized.
#
ERROR_NDIS_REINIT_REQUIRED = 0x80340030


#
# NDIS error codes (802.11 wireless LAN)
#

#
# MessageId: ERROR_NDIS_DOT11_AUTO_CONFIG_ENABLED
#
# MessageText:
#
# The wireless local area network interface is in auto configuration mode and doesn't support the requested parameter change operation.
#
ERROR_NDIS_DOT1 = 1

#
# MessageId: ERROR_NDIS_DOT11_MEDIA_IN_USE
#
# MessageText:
#
# The wireless local area network interface is busy and can not perform the requested operation.
#
ERROR_NDIS_DOT1 = 1

#
# MessageId: ERROR_NDIS_DOT11_POWER_STATE_INVALID
#
# MessageText:
#
# The wireless local area network interface is powered down and doesn't support the requested operation.
#
ERROR_NDIS_DOT1 = 1

#
# MessageId: ERROR_NDIS_PM_WOL_PATTERN_LIST_FULL
#
# MessageText:
#
# The list of wake on LAN patterns is full.
#
ERROR_NDIS_PM_WOL_PATTERN_LIST_FULL = 0x80342003

#
# MessageId: ERROR_NDIS_PM_PROTOCOL_OFFLOAD_LIST_FULL
#
# MessageText:
#
# The list of low power protocol offloads is full.
#
ERROR_NDIS_PM_PROTOCOL_OFFLOAD_LIST_FULL = 0x80342004

#
# NDIS informational code (ndis.sys)
#

#
# MessageId: ERROR_NDIS_INDICATION_REQUIRED
#
# MessageText:
#
# The request will be completed later by NDIS status indication.
#
ERROR_NDIS_INDICATION_REQUIRED = 0x00340001

#
# NDIS Chimney Offload codes (ndis.sys)
#

#
# MessageId: ERROR_NDIS_OFFLOAD_POLICY
#
# MessageText:
#
# The TCP connection is not offloadable because of a local policy setting.
#
ERROR_NDIS_OFFLOAD_POLICY = 0xC034100F

#
# MessageId: ERROR_NDIS_OFFLOAD_CONNECTION_REJECTED
#
# MessageText:
#
# The TCP connection is not offloadable by the Chimney Offload target.
#
ERROR_NDIS_OFFLOAD_CONNECTION_REJECTED = 0xC0341012

#
# MessageId: ERROR_NDIS_OFFLOAD_PATH_REJECTED
#
# MessageText:
#
# The IP Path object is not in an offloadable state.
#
ERROR_NDIS_OFFLOAD_PATH_REJECTED = 0xC0341013

#
# Hypervisor error codes
#

#
# MessageId: ERROR_HV_INVALID_HYPERCALL_CODE
#
# MessageText:
#
# The hypervisor does not support the operation because the specified hypercall code is not supported.
#
ERROR_HV_INVALID_HYPERCALL_CODE = 0xC0350002

#
# MessageId: ERROR_HV_INVALID_HYPERCALL_INPUT
#
# MessageText:
#
# The hypervisor does not support the operation because the encoding for the hypercall input register is not supported.
#
ERROR_HV_INVALID_HYPERCALL_INPUT = 0xC0350003

#
# MessageId: ERROR_HV_INVALID_ALIGNMENT
#
# MessageText:
#
# The hypervisor could not perform the operation beacuse a parameter has an invalid alignment.
#
ERROR_HV_INVALID_ALIGNMENT = 0xC0350004

#
# MessageId: ERROR_HV_INVALID_PARAMETER
#
# MessageText:
#
# The hypervisor could not perform the operation beacuse an invalid parameter was specified.
#
ERROR_HV_INVALID_PARAMETER = 0xC0350005

#
# MessageId: ERROR_HV_ACCESS_DENIED
#
# MessageText:
#
# Access to the specified object was denied.
#
ERROR_HV_ACCESS_DENIED = 0xC0350006

#
# MessageId: ERROR_HV_INVALID_PARTITION_STATE
#
# MessageText:
#
# The hypervisor could not perform the operation because the partition is entering or in an invalid state.
#
ERROR_HV_INVALID_PARTITION_STATE = 0xC0350007

#
# MessageId: ERROR_HV_OPERATION_DENIED
#
# MessageText:
#
# The operation is not allowed in the current state.
#
ERROR_HV_OPERATION_DENIED = 0xC0350008

#
# MessageId: ERROR_HV_UNKNOWN_PROPERTY
#
# MessageText:
#
# The hypervisor does not recognize the specified partition property.
#
ERROR_HV_UNKNOWN_PROPERTY = 0xC0350009

#
# MessageId: ERROR_HV_PROPERTY_VALUE_OUT_OF_RANGE
#
# MessageText:
#
# The specified value of a partition property is out of range or violates an invariant.
#
ERROR_HV_PROPERTY_VALUE_OUT_OF_RANGE = 0xC035000A

#
# MessageId: ERROR_HV_INSUFFICIENT_MEMORY
#
# MessageText:
#
# There is not enough memory in the hypervisor pool to complete the operation.
#
ERROR_HV_INSUFFICIENT_MEMORY = 0xC035000B

#
# MessageId: ERROR_HV_PARTITION_TOO_DEEP
#
# MessageText:
#
# The maximum partition depth has been exceeded for the partition hierarchy.
#
ERROR_HV_PARTITION_TOO_DEEP = 0xC035000C

#
# MessageId: ERROR_HV_INVALID_PARTITION_ID
#
# MessageText:
#
# A partition with the specified partition Id does not exist.
#
ERROR_HV_INVALID_PARTITION_ID = 0xC035000D

#
# MessageId: ERROR_HV_INVALID_VP_INDEX
#
# MessageText:
#
# The hypervisor could not perform the operation because the specified VP index is invalid.
#
ERROR_HV_INVALID_VP_INDEX = 0xC035000E

#
# MessageId: ERROR_HV_INVALID_PORT_ID
#
# MessageText:
#
# The hypervisor could not perform the operation because the specified port identifier is invalid.
#
ERROR_HV_INVALID_PORT_ID = 0xC0350011

#
# MessageId: ERROR_HV_INVALID_CONNECTION_ID
#
# MessageText:
#
# The hypervisor could not perform the operation because the specified connection identifier is invalid.
#
ERROR_HV_INVALID_CONNECTION_ID = 0xC0350012

#
# MessageId: ERROR_HV_INSUFFICIENT_BUFFERS
#
# MessageText:
#
# Not enough buffers were supplied to send a message.
#
ERROR_HV_INSUFFICIENT_BUFFERS = 0xC0350013

#
# MessageId: ERROR_HV_NOT_ACKNOWLEDGED
#
# MessageText:
#
# The previous virtual interrupt has not been acknowledged.
#
ERROR_HV_NOT_ACKNOWLEDGED = 0xC0350014

#
# MessageId: ERROR_HV_ACKNOWLEDGED
#
# MessageText:
#
# The previous virtual interrupt has already been acknowledged.
#
ERROR_HV_ACKNOWLEDGED = 0xC0350016

#
# MessageId: ERROR_HV_INVALID_SAVE_RESTORE_STATE
#
# MessageText:
#
# The indicated partition is not in a valid state for saving or restoring.
#
ERROR_HV_INVALID_SAVE_RESTORE_STATE = 0xC0350017

#
# MessageId: ERROR_HV_INVALID_SYNIC_STATE
#
# MessageText:
#
# The hypervisor could not complete the operation because a required feature of the synthetic interrupt controller (SynIC) was disabled.
#
ERROR_HV_INVALID_SYNIC_STATE = 0xC0350018

#
# MessageId: ERROR_HV_OBJECT_IN_USE
#
# MessageText:
#
# The hypervisor could not perform the operation because the object or value was either already in use or being used for a purpose that would not permit completing the operation.
#
ERROR_HV_OBJECT_IN_USE = 0xC0350019

#
# MessageId: ERROR_HV_INVALID_PROXIMITY_DOMAIN_INFO
#
# MessageText:
#
# The proximity domain information is invalid.
#
ERROR_HV_INVALID_PROXIMITY_DOMAIN_INFO = 0xC035001A

#
# MessageId: ERROR_HV_NO_DATA
#
# MessageText:
#
# An attempt to retrieve debugging data failed because none was available.
#
ERROR_HV_NO_DATA = 0xC035001B

#
# MessageId: ERROR_HV_INACTIVE
#
# MessageText:
#
# The physical connection being used for debuggging has not recorded any receive activity since the last operation.
#
ERROR_HV_INACTIVE = 0xC035001C

#
# MessageId: ERROR_HV_NO_RESOURCES
#
# MessageText:
#
# There are not enough resources to complete the operation.
#
ERROR_HV_NO_RESOURCES = 0xC035001D

#
# MessageId: ERROR_HV_FEATURE_UNAVAILABLE
#
# MessageText:
#
# A hypervisor feature is not available to the user.
#
ERROR_HV_FEATURE_UNAVAILABLE = 0xC035001E

#
# MessageId: ERROR_HV_INSUFFICIENT_BUFFER
#
# MessageText:
#
# The specified buffer was too small to contain all of the requested data.
#
ERROR_HV_INSUFFICIENT_BUFFER = 0xC0350033

#
# MessageId: ERROR_HV_INSUFFICIENT_DEVICE_DOMAINS
#
# MessageText:
#
# The maximum number of domains supported by the platform I/O remapping hardware is currently in use. No domains are available to assign this device to this partition.
#
ERROR_HV_INSUFFICIENT_DEVICE_DOMAINS = 0xC0350038

#
# MessageId: ERROR_HV_INVALID_LP_INDEX
#
# MessageText:
#
# The hypervisor could not perform the operation because the specified LP index is invalid.
#
ERROR_HV_INVALID_LP_INDEX = 0xC0350041

#
# MessageId: ERROR_HV_NOT_PRESENT
#
# MessageText:
#
# No hypervisor is present on this system.
#
ERROR_HV_NOT_PRESENT = 0xC0351000

#
# Virtualization error codes - these codes are used by the Virtualization Infrustructure Driver (VID) and other components
#                              of the virtualization stack.
#
# Errors:
#

#
# MessageId: ERROR_VID_DUPLICATE_HANDLER
#
# MessageText:
#
# The handler for the virtualization infrastructure driver is already registered. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_DUPLICATE_HANDLER = 0xC0370001

#
# MessageId: ERROR_VID_TOO_MANY_HANDLERS
#
# MessageText:
#
# The number of registered handlers for the virtualization infrastructure driver exceeded the maximum. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_TOO_MANY_HANDLERS = 0xC0370002

#
# MessageId: ERROR_VID_QUEUE_FULL
#
# MessageText:
#
# The message queue for the virtualization infrastructure driver is full and cannot accept new messages. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_QUEUE_FULL = 0xC0370003

#
# MessageId: ERROR_VID_HANDLER_NOT_PRESENT
#
# MessageText:
#
# No handler exists to handle the message for the virtualization infrastructure driver. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_HANDLER_NOT_PRESENT = 0xC0370004

#
# MessageId: ERROR_VID_INVALID_OBJECT_NAME
#
# MessageText:
#
# The name of the partition or message queue for the virtualization infrastructure driver is invalid. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_INVALID_OBJECT_NAME = 0xC0370005

#
# MessageId: ERROR_VID_PARTITION_NAME_TOO_LONG
#
# MessageText:
#
# The partition name of the virtualization infrastructure driver exceeds the maximum.
#
ERROR_VID_PARTITION_NAME_TOO_LONG = 0xC0370006

#
# MessageId: ERROR_VID_MESSAGE_QUEUE_NAME_TOO_LONG
#
# MessageText:
#
# The message queue name of the virtualization infrastructure driver exceeds the maximum.
#
ERROR_VID_MESSAGE_QUEUE_NAME_TOO_LONG = 0xC0370007

#
# MessageId: ERROR_VID_PARTITION_ALREADY_EXISTS
#
# MessageText:
#
# Cannot create the partition for the virtualization infrastructure driver because another partition with the same name already exists.
#
ERROR_VID_PARTITION_ALREADY_EXISTS = 0xC0370008

#
# MessageId: ERROR_VID_PARTITION_DOES_NOT_EXIST
#
# MessageText:
#
# The virtualization infrastructure driver has encountered an error. The requested partition does not exist. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_PARTITION_DOES_NOT_EXIST = 0xC0370009

#
# MessageId: ERROR_VID_PARTITION_NAME_NOT_FOUND
#
# MessageText:
#
# The virtualization infrastructure driver has encountered an error. Could not find the requested partition. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_PARTITION_NAME_NOT_FOUND = 0xC037000A

#
# MessageId: ERROR_VID_MESSAGE_QUEUE_ALREADY_EXISTS
#
# MessageText:
#
# A message queue with the same name already exists for the virtualization infrastructure driver.
#
ERROR_VID_MESSAGE_QUEUE_ALREADY_EXISTS = 0xC037000B

#
# MessageId: ERROR_VID_EXCEEDED_MBP_ENTRY_MAP_LIMIT
#
# MessageText:
#
# The memory block page for the virtualization infrastructure driver cannot be mapped because the page map limit has been reached. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_EXCEEDED_MBP_ENTRY_MAP_LIMIT = 0xC037000C

#
# MessageId: ERROR_VID_MB_STILL_REFERENCED
#
# MessageText:
#
# The memory block for the virtualization infrastructure driver is still being used and cannot be destroyed.
#
ERROR_VID_MB_STILL_REFERENCED = 0xC037000D

#
# MessageId: ERROR_VID_CHILD_GPA_PAGE_SET_CORRUPTED
#
# MessageText:
#
# Cannot unlock the page array for the guest operating system memory address because it does not match a previous lock request. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_CHILD_GPA_PAGE_SET_CORRUPTED = 0xC037000E

#
# MessageId: ERROR_VID_INVALID_NUMA_SETTINGS
#
# MessageText:
#
# The non-uniform memory access (NUMA) node settings do not match the system NUMA topology. In order to start the virtual machine, you will need to modify the NUMA configuration.
#
ERROR_VID_INVALID_NUMA_SETTINGS = 0xC037000F

#
# MessageId: ERROR_VID_INVALID_NUMA_NODE_INDEX
#
# MessageText:
#
# The non-uniform memory access (NUMA) node index does not match a valid index in the system NUMA topology.
#
ERROR_VID_INVALID_NUMA_NODE_INDEX = 0xC0370010

#
# MessageId: ERROR_VID_NOTIFICATION_QUEUE_ALREADY_ASSOCIATED
#
# MessageText:
#
# The memory block for the virtualization infrastructure driver is already associated with a message queue.
#
ERROR_VID_NOTIFICATION_QUEUE_ALREADY_ASSOCIATED = 0xC0370011

#
# MessageId: ERROR_VID_INVALID_MEMORY_BLOCK_HANDLE
#
# MessageText:
#
# The handle is not a valid memory block handle for the virtualization infrastructure driver.
#
ERROR_VID_INVALID_MEMORY_BLOCK_HANDLE = 0xC0370012

#
# MessageId: ERROR_VID_PAGE_RANGE_OVERFLOW
#
# MessageText:
#
# The request exceeded the memory block page limit for the virtualization infrastructure driver. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_PAGE_RANGE_OVERFLOW = 0xC0370013

#
# MessageId: ERROR_VID_INVALID_MESSAGE_QUEUE_HANDLE
#
# MessageText:
#
# The handle is not a valid message queue handle for the virtualization infrastructure driver.
#
ERROR_VID_INVALID_MESSAGE_QUEUE_HANDLE = 0xC0370014

#
# MessageId: ERROR_VID_INVALID_GPA_RANGE_HANDLE
#
# MessageText:
#
# The handle is not a valid page range handle for the virtualization infrastructure driver.
#
ERROR_VID_INVALID_GPA_RANGE_HANDLE = 0xC0370015

#
# MessageId: ERROR_VID_NO_MEMORY_BLOCK_NOTIFICATION_QUEUE
#
# MessageText:
#
# Cannot install client notifications because no message queue for the virtualization infrastructure driver is associated with the memory block.
#
ERROR_VID_NO_MEMORY_BLOCK_NOTIFICATION_QUEUE = 0xC0370016

#
# MessageId: ERROR_VID_MEMORY_BLOCK_LOCK_COUNT_EXCEEDED
#
# MessageText:
#
# The request to lock or map a memory block page failed because the virtualization infrastructure driver memory block limit has been reached. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_MEMORY_BLOCK_LOCK_COUNT_EXCEEDED = 0xC0370017

#
# MessageId: ERROR_VID_INVALID_PPM_HANDLE
#
# MessageText:
#
# The handle is not a valid parent partition mapping handle for the virtualization infrastructure driver.
#
ERROR_VID_INVALID_PPM_HANDLE = 0xC0370018

#
# MessageId: ERROR_VID_MBPS_ARE_LOCKED
#
# MessageText:
#
# Notifications cannot be created on the memory block because it is use.
#
ERROR_VID_MBPS_ARE_LOCKED = 0xC0370019

#
# MessageId: ERROR_VID_MESSAGE_QUEUE_CLOSED
#
# MessageText:
#
# The message queue for the virtualization infrastructure driver has been closed. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_MESSAGE_QUEUE_CLOSED = 0xC037001A

#
# MessageId: ERROR_VID_VIRTUAL_PROCESSOR_LIMIT_EXCEEDED
#
# MessageText:
#
# Cannot add a virtual processor to the partition because the maximum has been reached.
#
ERROR_VID_VIRTUAL_PROCESSOR_LIMIT_EXCEEDED = 0xC037001B

#
# MessageId: ERROR_VID_STOP_PENDING
#
# MessageText:
#
# Cannot stop the virtual processor immediately because of a pending intercept.
#
ERROR_VID_STOP_PENDING = 0xC037001C

#
# MessageId: ERROR_VID_INVALID_PROCESSOR_STATE
#
# MessageText:
#
# Invalid state for the virtual processor. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_INVALID_PROCESSOR_STATE = 0xC037001D

#
# MessageId: ERROR_VID_EXCEEDED_KM_CONTEXT_COUNT_LIMIT
#
# MessageText:
#
# The maximum number of kernel mode clients for the virtualization infrastructure driver has been reached. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_EXCEEDED_KM_CONTEXT_COUNT_LIMIT = 0xC037001E

#
# MessageId: ERROR_VID_KM_INTERFACE_ALREADY_INITIALIZED
#
# MessageText:
#
# This kernel mode interface for the virtualization infrastructure driver has already been initialized. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_KM_INTERFACE_ALREADY_INITIALIZED = 0xC037001F

#
# MessageId: ERROR_VID_MB_PROPERTY_ALREADY_SET_RESET
#
# MessageText:
#
# Cannot set or reset the memory block property more than once for the virtualization infrastructure driver. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_MB_PROPERTY_ALREADY_SET_RESET = 0xC0370020

#
# MessageId: ERROR_VID_MMIO_RANGE_DESTROYED
#
# MessageText:
#
# The memory mapped I/O for this page range no longer exists. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_MMIO_RANGE_DESTROYED = 0xC0370021

#
# MessageId: ERROR_VID_INVALID_CHILD_GPA_PAGE_SET
#
# MessageText:
#
# The lock or unlock request uses an invalid guest operating system memory address. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_INVALID_CHILD_GPA_PAGE_SET = 0xC0370022

#
# MessageId: ERROR_VID_RESERVE_PAGE_SET_IS_BEING_USED
#
# MessageText:
#
# Cannot destroy or reuse the reserve page set for the virtualization infrastructure driver because it is in use. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_RESERVE_PAGE_SET_IS_BEING_USED = 0xC0370023

#
# MessageId: ERROR_VID_RESERVE_PAGE_SET_TOO_SMALL
#
# MessageText:
#
# The reserve page set for the virtualization infrastructure driver is too small to use in the lock request. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_RESERVE_PAGE_SET_TOO_SMALL = 0xC0370024

#
# MessageId: ERROR_VID_MBP_ALREADY_LOCKED_USING_RESERVED_PAGE
#
# MessageText:
#
# Cannot lock or map the memory block page for the virtualization infrastructure driver because it has already been locked using a reserve page set page. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_MBP_ALREADY_LOCKED_USING_RESERVED_PAGE = 0xC0370025

#
# MessageId: ERROR_VID_MBP_COUNT_EXCEEDED_LIMIT
#
# MessageText:
#
# Cannot create the memory block for the virtualization infrastructure driver because the requested number of pages exceeded the limit. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.
#
ERROR_VID_MBP_COUNT_EXCEEDED_LIMIT = 0xC0370026

#
# MessageId: ERROR_VID_SAVED_STATE_CORRUPT
#
# MessageText:
#
# Cannot restore this virtual machine because the saved state data cannot be read. Delete the saved state data and then try to start the virtual machine.
#
ERROR_VID_SAVED_STATE_CORRUPT = 0xC0370027

#
# MessageId: ERROR_VID_SAVED_STATE_UNRECOGNIZED_ITEM
#
# MessageText:
#
# Cannot restore this virtual machine because an item read from the saved state data is not recognized. Delete the saved state data and then try to start the virtual machine.
#
ERROR_VID_SAVED_STATE_UNRECOGNIZED_ITEM = 0xC0370028

#
# MessageId: ERROR_VID_SAVED_STATE_INCOMPATIBLE
#
# MessageText:
#
# Cannot restore this virtual machine to the saved state because of hypervisor incompatibility. Delete the saved state data and then try to start the virtual machine.
#
ERROR_VID_SAVED_STATE_INCOMPATIBLE = 0xC0370029

#
# Warnings:
#
#
# MessageId: ERROR_VID_REMOTE_NODE_PARENT_GPA_PAGES_USED
#
# MessageText:
#
# A virtual machine is running with its memory allocated across multiple NUMA nodes. This does not indicate a problem unless the performance of your virtual machine is unusually slow. If you are experiencing performance problems, you may need to modify the NUMA configuration.
#
ERROR_VID_REMOTE_NODE_PARENT_GPA_PAGES_USED = 0x80370001


#
# Volume manager error codes mapped from status codes
#

#
# WARNINGS
#
#
# MessageId: ERROR_VOLMGR_INCOMPLETE_REGENERATION
#
# MessageText:
#
# The regeneration operation was not able to copy all data from the active plexes due to bad sectors.
#
ERROR_VOLMGR_INCOMPLETE_REGENERATION = 0x80380001

#
# MessageId: ERROR_VOLMGR_INCOMPLETE_DISK_MIGRATION
#
# MessageText:
#
# One or more disks were not fully migrated to the target pack. They may or may not require reimport after fixing the hardware problems.
#
ERROR_VOLMGR_INCOMPLETE_DISK_MIGRATION = 0x80380002

#
# ERRORS
#
#
# MessageId: ERROR_VOLMGR_DATABASE_FULL
#
# MessageText:
#
# The configuration database is full.
#
ERROR_VOLMGR_DATABASE_FULL = 0xC0380001

#
# MessageId: ERROR_VOLMGR_DISK_CONFIGURATION_CORRUPTED
#
# MessageText:
#
# The configuration data on the disk is corrupted.
#
ERROR_VOLMGR_DISK_CONFIGURATION_CORRUPTED = 0xC0380002

#
# MessageId: ERROR_VOLMGR_DISK_CONFIGURATION_NOT_IN_SYNC
#
# MessageText:
#
# The configuration on the disk is not insync with the in-memory configuration.
#
ERROR_VOLMGR_DISK_CONFIGURATION_NOT_IN_SYNC = 0xC0380003

#
# MessageId: ERROR_VOLMGR_PACK_CONFIG_UPDATE_FAILED
#
# MessageText:
#
# A majority of disks failed to be updated with the new configuration.
#
ERROR_VOLMGR_PACK_CONFIG_UPDATE_FAILED = 0xC0380004

#
# MessageId: ERROR_VOLMGR_DISK_CONTAINS_NON_SIMPLE_VOLUME
#
# MessageText:
#
# The disk contains non-simple volumes.
#
ERROR_VOLMGR_DISK_CONTAINS_NON_SIMPLE_VOLUME = 0xC0380005

#
# MessageId: ERROR_VOLMGR_DISK_DUPLICATE
#
# MessageText:
#
# The same disk was specified more than once in the migration list.
#
ERROR_VOLMGR_DISK_DUPLICATE = 0xC0380006

#
# MessageId: ERROR_VOLMGR_DISK_DYNAMIC
#
# MessageText:
#
# The disk is already dynamic.
#
ERROR_VOLMGR_DISK_DYNAMIC = 0xC0380007

#
# MessageId: ERROR_VOLMGR_DISK_ID_INVALID
#
# MessageText:
#
# The specified disk id is invalid. There are no disks with the specified disk id.
#
ERROR_VOLMGR_DISK_ID_INVALID = 0xC0380008

#
# MessageId: ERROR_VOLMGR_DISK_INVALID
#
# MessageText:
#
# The specified disk is an invalid disk. Operation cannot complete on an invalid disk.
#
ERROR_VOLMGR_DISK_INVALID = 0xC0380009

#
# MessageId: ERROR_VOLMGR_DISK_LAST_VOTER
#
# MessageText:
#
# The specified disk(s) cannot be removed since it is the last remaining voter.
#
ERROR_VOLMGR_DISK_LAST_VOTER = 0xC038000A

#
# MessageId: ERROR_VOLMGR_DISK_LAYOUT_INVALID
#
# MessageText:
#
# The specified disk has an invalid disk layout.
#
ERROR_VOLMGR_DISK_LAYOUT_INVALID = 0xC038000B

#
# MessageId: ERROR_VOLMGR_DISK_LAYOUT_NON_BASIC_BETWEEN_BASIC_PARTITIONS
#
# MessageText:
#
# The disk layout contains non-basic partitions which appear after basic paritions. This is an invalid disk layout.
#
ERROR_VOLMGR_DISK_LAYOUT_NON_BASIC_BETWEEN_BASIC_PARTITIONS = 0xC038000C

#
# MessageId: ERROR_VOLMGR_DISK_LAYOUT_NOT_CYLINDER_ALIGNED
#
# MessageText:
#
# The disk layout contains partitions which are not cylinder aligned.
#
ERROR_VOLMGR_DISK_LAYOUT_NOT_CYLINDER_ALIGNED = 0xC038000D

#
# MessageId: ERROR_VOLMGR_DISK_LAYOUT_PARTITIONS_TOO_SMALL
#
# MessageText:
#
# The disk layout contains partitions which are samller than the minimum size.
#
ERROR_VOLMGR_DISK_LAYOUT_PARTITIONS_TOO_SMALL = 0xC038000E

#
# MessageId: ERROR_VOLMGR_DISK_LAYOUT_PRIMARY_BETWEEN_LOGICAL_PARTITIONS
#
# MessageText:
#
# The disk layout contains primary partitions in between logical drives. This is an invalid disk layout.
#
ERROR_VOLMGR_DISK_LAYOUT_PRIMARY_BETWEEN_LOGICAL_PARTITIONS = 0xC038000F

#
# MessageId: ERROR_VOLMGR_DISK_LAYOUT_TOO_MANY_PARTITIONS
#
# MessageText:
#
# The disk layout contains more than the maximum number of supported partitions.
#
ERROR_VOLMGR_DISK_LAYOUT_TOO_MANY_PARTITIONS = 0xC0380010

#
# MessageId: ERROR_VOLMGR_DISK_MISSING
#
# MessageText:
#
# The specified disk is missing. The operation cannot complete on a missing disk.
#
ERROR_VOLMGR_DISK_MISSING = 0xC0380011

#
# MessageId: ERROR_VOLMGR_DISK_NOT_EMPTY
#
# MessageText:
#
# The specified disk is not empty.
#
ERROR_VOLMGR_DISK_NOT_EMPTY = 0xC0380012

#
# MessageId: ERROR_VOLMGR_DISK_NOT_ENOUGH_SPACE
#
# MessageText:
#
# There is not enough usable space for this operation.
#
ERROR_VOLMGR_DISK_NOT_ENOUGH_SPACE = 0xC0380013

#
# MessageId: ERROR_VOLMGR_DISK_REVECTORING_FAILED
#
# MessageText:
#
# The force revectoring of bad sectors failed.
#
ERROR_VOLMGR_DISK_REVECTORING_FAILED = 0xC0380014

#
# MessageId: ERROR_VOLMGR_DISK_SECTOR_SIZE_INVALID
#
# MessageText:
#
# The specified disk has an invalid sector size.
#
ERROR_VOLMGR_DISK_SECTOR_SIZE_INVALID = 0xC0380015

#
# MessageId: ERROR_VOLMGR_DISK_SET_NOT_CONTAINED
#
# MessageText:
#
# The specified disk set contains volumes which exist on disks outside of the set.
#
ERROR_VOLMGR_DISK_SET_NOT_CONTAINED = 0xC0380016

#
# MessageId: ERROR_VOLMGR_DISK_USED_BY_MULTIPLE_MEMBERS
#
# MessageText:
#
# A disk in the volume layout provides extents to more than one member of a plex.
#
ERROR_VOLMGR_DISK_USED_BY_MULTIPLE_MEMBERS = 0xC0380017

#
# MessageId: ERROR_VOLMGR_DISK_USED_BY_MULTIPLE_PLEXES
#
# MessageText:
#
# A disk in the volume layout provides extents to more than one plex.
#
ERROR_VOLMGR_DISK_USED_BY_MULTIPLE_PLEXES = 0xC0380018

#
# MessageId: ERROR_VOLMGR_DYNAMIC_DISK_NOT_SUPPORTED
#
# MessageText:
#
# Dynamic disks are not supported on this system.
#
ERROR_VOLMGR_DYNAMIC_DISK_NOT_SUPPORTED = 0xC0380019

#
# MessageId: ERROR_VOLMGR_EXTENT_ALREADY_USED
#
# MessageText:
#
# The specified extent is already used by other volumes.
#
ERROR_VOLMGR_EXTENT_ALREADY_USED = 0xC038001A

#
# MessageId: ERROR_VOLMGR_EXTENT_NOT_CONTIGUOUS
#
# MessageText:
#
# The specified volume is retained and can only be extended into a contiguous extent. The specified extent to grow the volume is not contiguous with the specified volume.
#
ERROR_VOLMGR_EXTENT_NOT_CONTIGUOUS = 0xC038001B

#
# MessageId: ERROR_VOLMGR_EXTENT_NOT_IN_PUBLIC_REGION
#
# MessageText:
#
# The specified volume extent is not within the public region of the disk.
#
ERROR_VOLMGR_EXTENT_NOT_IN_PUBLIC_REGION = 0xC038001C

#
# MessageId: ERROR_VOLMGR_EXTENT_NOT_SECTOR_ALIGNED
#
# MessageText:
#
# The specifed volume extent is not sector aligned.
#
ERROR_VOLMGR_EXTENT_NOT_SECTOR_ALIGNED = 0xC038001D

#
# MessageId: ERROR_VOLMGR_EXTENT_OVERLAPS_EBR_PARTITION
#
# MessageText:
#
# The specified parition overlaps an EBR (the first track of an extended partition on a MBR disks).
#
ERROR_VOLMGR_EXTENT_OVERLAPS_EBR_PARTITION = 0xC038001E

#
# MessageId: ERROR_VOLMGR_EXTENT_VOLUME_LENGTHS_DO_NOT_MATCH
#
# MessageText:
#
# The specified extent lengths cannot be used to construct a volume with specified length.
#
ERROR_VOLMGR_EXTENT_VOLUME_LENGTHS_DO_NOT_MATCH = 0xC038001F

#
# MessageId: ERROR_VOLMGR_FAULT_TOLERANT_NOT_SUPPORTED
#
# MessageText:
#
# The system does not support fault tolerant volumes.
#
ERROR_VOLMGR_FAULT_TOLERANT_NOT_SUPPORTED = 0xC0380020

#
# MessageId: ERROR_VOLMGR_INTERLEAVE_LENGTH_INVALID
#
# MessageText:
#
# The specified interleave length is invalid.
#
ERROR_VOLMGR_INTERLEAVE_LENGTH_INVALID = 0xC0380021

#
# MessageId: ERROR_VOLMGR_MAXIMUM_REGISTERED_USERS
#
# MessageText:
#
# There is already a maximum number of registered users.
#
ERROR_VOLMGR_MAXIMUM_REGISTERED_USERS = 0xC0380022

#
# MessageId: ERROR_VOLMGR_MEMBER_IN_SYNC
#
# MessageText:
#
# The specified member is already in-sync with the other active members. It does not need to be regenerated.
#
ERROR_VOLMGR_MEMBER_IN_SYNC = 0xC0380023

#
# MessageId: ERROR_VOLMGR_MEMBER_INDEX_DUPLICATE
#
# MessageText:
#
# The same member index was specified more than once.
#
ERROR_VOLMGR_MEMBER_INDEX_DUPLICATE = 0xC0380024

#
# MessageId: ERROR_VOLMGR_MEMBER_INDEX_INVALID
#
# MessageText:
#
# The specified member index is greater or equal than the number of members in the volume plex.
#
ERROR_VOLMGR_MEMBER_INDEX_INVALID = 0xC0380025

#
# MessageId: ERROR_VOLMGR_MEMBER_MISSING
#
# MessageText:
#
# The specified member is missing. It cannot be regenerated.
#
ERROR_VOLMGR_MEMBER_MISSING = 0xC0380026

#
# MessageId: ERROR_VOLMGR_MEMBER_NOT_DETACHED
#
# MessageText:
#
# The specified member is not detached. Cannot replace a member which is not detached.
#
ERROR_VOLMGR_MEMBER_NOT_DETACHED = 0xC0380027

#
# MessageId: ERROR_VOLMGR_MEMBER_REGENERATING
#
# MessageText:
#
# The specified member is already regenerating.
#
ERROR_VOLMGR_MEMBER_REGENERATING = 0xC0380028

#
# MessageId: ERROR_VOLMGR_ALL_DISKS_FAILED
#
# MessageText:
#
# All disks belonging to the pack failed.
#
ERROR_VOLMGR_ALL_DISKS_FAILED = 0xC0380029

#
# MessageId: ERROR_VOLMGR_NO_REGISTERED_USERS
#
# MessageText:
#
# There are currently no registered users for notifications. The task number is irrelevant unless there are registered users.
#
ERROR_VOLMGR_NO_REGISTERED_USERS = 0xC038002A

#
# MessageId: ERROR_VOLMGR_NO_SUCH_USER
#
# MessageText:
#
# The specified notification user does not exist. Failed to unregister user for notifications.
#
ERROR_VOLMGR_NO_SUCH_USER = 0xC038002B

#
# MessageId: ERROR_VOLMGR_NOTIFICATION_RESET
#
# MessageText:
#
# The notifications have been reset. Notifications for the current user are invalid. Unregister and re-register for notifications.
#
ERROR_VOLMGR_NOTIFICATION_RESET = 0xC038002C

#
# MessageId: ERROR_VOLMGR_NUMBER_OF_MEMBERS_INVALID
#
# MessageText:
#
# The specified number of members is invalid.
#
ERROR_VOLMGR_NUMBER_OF_MEMBERS_INVALID = 0xC038002D

#
# MessageId: ERROR_VOLMGR_NUMBER_OF_PLEXES_INVALID
#
# MessageText:
#
# The specified number of plexes is invalid.
#
ERROR_VOLMGR_NUMBER_OF_PLEXES_INVALID = 0xC038002E

#
# MessageId: ERROR_VOLMGR_PACK_DUPLICATE
#
# MessageText:
#
# The specified source and target packs are identical.
#
ERROR_VOLMGR_PACK_DUPLICATE = 0xC038002F

#
# MessageId: ERROR_VOLMGR_PACK_ID_INVALID
#
# MessageText:
#
# The specified pack id is invalid. There are no packs with the specified pack id.
#
ERROR_VOLMGR_PACK_ID_INVALID = 0xC0380030

#
# MessageId: ERROR_VOLMGR_PACK_INVALID
#
# MessageText:
#
# The specified pack is the invalid pack. The operation cannot complete with the invalid pack.
#
ERROR_VOLMGR_PACK_INVALID = 0xC0380031

#
# MessageId: ERROR_VOLMGR_PACK_NAME_INVALID
#
# MessageText:
#
# The specified pack name is invalid.
#
ERROR_VOLMGR_PACK_NAME_INVALID = 0xC0380032

#
# MessageId: ERROR_VOLMGR_PACK_OFFLINE
#
# MessageText:
#
# The specified pack is offline.
#
ERROR_VOLMGR_PACK_OFFLINE = 0xC0380033

#
# MessageId: ERROR_VOLMGR_PACK_HAS_QUORUM
#
# MessageText:
#
# The specified pack already has a quorum of healthy disks.
#
ERROR_VOLMGR_PACK_HAS_QUORUM = 0xC0380034

#
# MessageId: ERROR_VOLMGR_PACK_WITHOUT_QUORUM
#
# MessageText:
#
# The pack does not have a quorum of healthy disks.
#
ERROR_VOLMGR_PACK_WITHOUT_QUORUM = 0xC0380035

#
# MessageId: ERROR_VOLMGR_PARTITION_STYLE_INVALID
#
# MessageText:
#
# The specified disk has an unsupported partition style. Only MBR and GPT partition styles are supported.
#
ERROR_VOLMGR_PARTITION_STYLE_INVALID = 0xC0380036

#
# MessageId: ERROR_VOLMGR_PARTITION_UPDATE_FAILED
#
# MessageText:
#
# Failed to update the disk's partition layout.
#
ERROR_VOLMGR_PARTITION_UPDATE_FAILED = 0xC0380037

#
# MessageId: ERROR_VOLMGR_PLEX_IN_SYNC
#
# MessageText:
#
# The specified plex is already in-sync with the other active plexes. It does not need to be regenerated.
#
ERROR_VOLMGR_PLEX_IN_SYNC = 0xC0380038

#
# MessageId: ERROR_VOLMGR_PLEX_INDEX_DUPLICATE
#
# MessageText:
#
# The same plex index was specified more than once.
#
ERROR_VOLMGR_PLEX_INDEX_DUPLICATE = 0xC0380039

#
# MessageId: ERROR_VOLMGR_PLEX_INDEX_INVALID
#
# MessageText:
#
# The specified plex index is greater or equal than the number of plexes in the volume.
#
ERROR_VOLMGR_PLEX_INDEX_INVALID = 0xC038003A

#
# MessageId: ERROR_VOLMGR_PLEX_LAST_ACTIVE
#
# MessageText:
#
# The specified plex is the last active plex in the volume. The plex cannot be removed or else the volume will go offline.
#
ERROR_VOLMGR_PLEX_LAST_ACTIVE = 0xC038003B

#
# MessageId: ERROR_VOLMGR_PLEX_MISSING
#
# MessageText:
#
# The specified plex is missing.
#
ERROR_VOLMGR_PLEX_MISSING = 0xC038003C

#
# MessageId: ERROR_VOLMGR_PLEX_REGENERATING
#
# MessageText:
#
# The specified plex is currently regenerating.
#
ERROR_VOLMGR_PLEX_REGENERATING = 0xC038003D

#
# MessageId: ERROR_VOLMGR_PLEX_TYPE_INVALID
#
# MessageText:
#
# The specified plex type is invalid.
#
ERROR_VOLMGR_PLEX_TYPE_INVALID = 0xC038003E

#
# MessageId: ERROR_VOLMGR_PLEX_NOT_RAID5
#
# MessageText:
#
# The operation is only supported on RAID-5 plexes.
#
ERROR_VOLMGR_PLEX_NOT_RAID = 5

#
# MessageId: ERROR_VOLMGR_PLEX_NOT_SIMPLE
#
# MessageText:
#
# The operation is only supported on simple plexes.
#
ERROR_VOLMGR_PLEX_NOT_SIMPLE = 0xC0380040

#
# MessageId: ERROR_VOLMGR_STRUCTURE_SIZE_INVALID
#
# MessageText:
#
# The Size fields in the VM_VOLUME_LAYOUT input structure are incorrectly set.
#
ERROR_VOLMGR_STRUCTURE_SIZE_INVALID = 0xC0380041

#
# MessageId: ERROR_VOLMGR_TOO_MANY_NOTIFICATION_REQUESTS
#
# MessageText:
#
# There is already a pending request for notifications. Wait for the existing request to return before requesting for more notifications.
#
ERROR_VOLMGR_TOO_MANY_NOTIFICATION_REQUESTS = 0xC0380042

#
# MessageId: ERROR_VOLMGR_TRANSACTION_IN_PROGRESS
#
# MessageText:
#
# There is currently a transaction in process.
#
ERROR_VOLMGR_TRANSACTION_IN_PROGRESS = 0xC0380043

#
# MessageId: ERROR_VOLMGR_UNEXPECTED_DISK_LAYOUT_CHANGE
#
# MessageText:
#
# An unexpected layout change occurred outside of the volume manager.
#
ERROR_VOLMGR_UNEXPECTED_DISK_LAYOUT_CHANGE = 0xC0380044

#
# MessageId: ERROR_VOLMGR_VOLUME_CONTAINS_MISSING_DISK
#
# MessageText:
#
# The specified volume contains a missing disk.
#
ERROR_VOLMGR_VOLUME_CONTAINS_MISSING_DISK = 0xC0380045

#
# MessageId: ERROR_VOLMGR_VOLUME_ID_INVALID
#
# MessageText:
#
# The specified volume id is invalid. There are no volumes with the specified volume id.
#
ERROR_VOLMGR_VOLUME_ID_INVALID = 0xC0380046

#
# MessageId: ERROR_VOLMGR_VOLUME_LENGTH_INVALID
#
# MessageText:
#
# The specified volume length is invalid.
#
ERROR_VOLMGR_VOLUME_LENGTH_INVALID = 0xC0380047

#
# MessageId: ERROR_VOLMGR_VOLUME_LENGTH_NOT_SECTOR_SIZE_MULTIPLE
#
# MessageText:
#
# The specified size for the volume is not a multiple of the sector size.
#
ERROR_VOLMGR_VOLUME_LENGTH_NOT_SECTOR_SIZE_MULTIPLE = 0xC0380048

#
# MessageId: ERROR_VOLMGR_VOLUME_NOT_MIRRORED
#
# MessageText:
#
# The operation is only supported on mirrored volumes.
#
ERROR_VOLMGR_VOLUME_NOT_MIRRORED = 0xC0380049

#
# MessageId: ERROR_VOLMGR_VOLUME_NOT_RETAINED
#
# MessageText:
#
# The specified volume does not have a retain partition.
#
ERROR_VOLMGR_VOLUME_NOT_RETAINED = 0xC038004A

#
# MessageId: ERROR_VOLMGR_VOLUME_OFFLINE
#
# MessageText:
#
# The specified volume is offline.
#
ERROR_VOLMGR_VOLUME_OFFLINE = 0xC038004B

#
# MessageId: ERROR_VOLMGR_VOLUME_RETAINED
#
# MessageText:
#
# The specified volume already has a retain partition.
#
ERROR_VOLMGR_VOLUME_RETAINED = 0xC038004C

#
# MessageId: ERROR_VOLMGR_NUMBER_OF_EXTENTS_INVALID
#
# MessageText:
#
# The specified number of extents is invalid.
#
ERROR_VOLMGR_NUMBER_OF_EXTENTS_INVALID = 0xC038004D

#
# MessageId: ERROR_VOLMGR_DIFFERENT_SECTOR_SIZE
#
# MessageText:
#
# All disks participating to the volume must have the same sector size.
#
ERROR_VOLMGR_DIFFERENT_SECTOR_SIZE = 0xC038004E

#
# MessageId: ERROR_VOLMGR_BAD_BOOT_DISK
#
# MessageText:
#
# The boot disk experienced failures.
#
ERROR_VOLMGR_BAD_BOOT_DISK = 0xC038004F

#
# MessageId: ERROR_VOLMGR_PACK_CONFIG_OFFLINE
#
# MessageText:
#
# The configuration of the pack is offline.
#
ERROR_VOLMGR_PACK_CONFIG_OFFLINE = 0xC0380050

#
# MessageId: ERROR_VOLMGR_PACK_CONFIG_ONLINE
#
# MessageText:
#
# The configuration of the pack is online.
#
ERROR_VOLMGR_PACK_CONFIG_ONLINE = 0xC0380051

#
# MessageId: ERROR_VOLMGR_NOT_PRIMARY_PACK
#
# MessageText:
#
# The specified pack is not the primary pack.
#
ERROR_VOLMGR_NOT_PRIMARY_PACK = 0xC0380052

#
# MessageId: ERROR_VOLMGR_PACK_LOG_UPDATE_FAILED
#
# MessageText:
#
# All disks failed to be updated with the new content of the log.
#
ERROR_VOLMGR_PACK_LOG_UPDATE_FAILED = 0xC0380053

#
# MessageId: ERROR_VOLMGR_NUMBER_OF_DISKS_IN_PLEX_INVALID
#
# MessageText:
#
# The specified number of disks in a plex is invalid.
#
ERROR_VOLMGR_NUMBER_OF_DISKS_IN_PLEX_INVALID = 0xC0380054

#
# MessageId: ERROR_VOLMGR_NUMBER_OF_DISKS_IN_MEMBER_INVALID
#
# MessageText:
#
# The specified number of disks in a plex member is invalid.
#
ERROR_VOLMGR_NUMBER_OF_DISKS_IN_MEMBER_INVALID = 0xC0380055

#
# MessageId: ERROR_VOLMGR_VOLUME_MIRRORED
#
# MessageText:
#
# The operation is not supported on mirrored volumes.
#
ERROR_VOLMGR_VOLUME_MIRRORED = 0xC0380056

#
# MessageId: ERROR_VOLMGR_PLEX_NOT_SIMPLE_SPANNED
#
# MessageText:
#
# The operation is only supported on simple and spanned plexes.
#
ERROR_VOLMGR_PLEX_NOT_SIMPLE_SPANNED = 0xC0380057

#
# MessageId: ERROR_VOLMGR_NO_VALID_LOG_COPIES
#
# MessageText:
#
# The pack has no valid log copies.
#
ERROR_VOLMGR_NO_VALID_LOG_COPIES = 0xC0380058

#
# MessageId: ERROR_VOLMGR_PRIMARY_PACK_PRESENT
#
# MessageText:
#
# A primary pack is already present.
#
ERROR_VOLMGR_PRIMARY_PACK_PRESENT = 0xC0380059

#
# MessageId: ERROR_VOLMGR_NUMBER_OF_DISKS_INVALID
#
# MessageText:
#
# The specified number of disks is invalid.
#
ERROR_VOLMGR_NUMBER_OF_DISKS_INVALID = 0xC038005A

#
# MessageId: ERROR_VOLMGR_MIRROR_NOT_SUPPORTED
#
# MessageText:
#
# The system does not support mirrored volumes.
#
ERROR_VOLMGR_MIRROR_NOT_SUPPORTED = 0xC038005B

#
# MessageId: ERROR_VOLMGR_RAID5_NOT_SUPPORTED
#
# MessageText:
#
# The system does not support RAID-5 volumes.
#
ERROR_VOLMGR_RAID = 5


#
# Boot Code Data (BCD) error codes
#

#
# MessageId: ERROR_BCD_NOT_ALL_ENTRIES_IMPORTED
#
# MessageText:
#
# Some BCD entries were not imported correctly from the BCD store.
#
ERROR_BCD_NOT_ALL_ENTRIES_IMPORTED = 0x80390001

#
# MessageId: ERROR_BCD_TOO_MANY_ELEMENTS
#
# MessageText:
#
# Entries enumerated have exceeded the allowed threshold.
#
ERROR_BCD_TOO_MANY_ELEMENTS = 0xC0390002

#
# MessageId: ERROR_BCD_NOT_ALL_ENTRIES_SYNCHRONIZED
#
# MessageText:
#
# Some BCD entries were not synchronized correctly with the firmware.
#
ERROR_BCD_NOT_ALL_ENTRIES_SYNCHRONIZED = 0x80390003

#
# Vhd error codes - These codes are used by the virtual hard diskparser component.
#
#
# Errors:
#

#
# MessageId: ERROR_VHD_DRIVE_FOOTER_MISSING
#
# MessageText:
#
# The virtual hard disk is corrupted. The virtual hard disk drive footer is missing.
#
ERROR_VHD_DRIVE_FOOTER_MISSING = 0xC03A0001

#
# MessageId: ERROR_VHD_DRIVE_FOOTER_CHECKSUM_MISMATCH
#
# MessageText:
#
# The virtual hard disk is corrupted. The virtual hard disk drive footer checksum does not match the on-disk checksum.
#
ERROR_VHD_DRIVE_FOOTER_CHECKSUM_MISMATCH = 0xC03A0002

#
# MessageId: ERROR_VHD_DRIVE_FOOTER_CORRUPT
#
# MessageText:
#
# The virtual hard disk is corrupted. The virtual hard disk drive footer in the virtual hard disk is corrupted.
#
ERROR_VHD_DRIVE_FOOTER_CORRUPT = 0xC03A0003

#
# MessageId: ERROR_VHD_FORMAT_UNKNOWN
#
# MessageText:
#
# The system does not recognize the file format of this virtual hard disk.
#
ERROR_VHD_FORMAT_UNKNOWN = 0xC03A0004

#
# MessageId: ERROR_VHD_FORMAT_UNSUPPORTED_VERSION
#
# MessageText:
#
# The version does not support this version of the file format.
#
ERROR_VHD_FORMAT_UNSUPPORTED_VERSION = 0xC03A0005

#
# MessageId: ERROR_VHD_SPARSE_HEADER_CHECKSUM_MISMATCH
#
# MessageText:
#
# The virtual hard disk is corrupted. The sparse header checksum does not match the on-disk checksum.
#
ERROR_VHD_SPARSE_HEADER_CHECKSUM_MISMATCH = 0xC03A0006

#
# MessageId: ERROR_VHD_SPARSE_HEADER_UNSUPPORTED_VERSION
#
# MessageText:
#
# The system does not support this version of the virtual hard disk.This version of the sparse header is not supported.
#
ERROR_VHD_SPARSE_HEADER_UNSUPPORTED_VERSION = 0xC03A0007

#
# MessageId: ERROR_VHD_SPARSE_HEADER_CORRUPT
#
# MessageText:
#
# The virtual hard disk is corrupted. The sparse header in the virtual hard disk is corrupt.
#
ERROR_VHD_SPARSE_HEADER_CORRUPT = 0xC03A0008

#
# MessageId: ERROR_VHD_BLOCK_ALLOCATION_FAILURE
#
# MessageText:
#
# Failed to write to the virtual hard disk failed because the system failed to allocate a new block in the virtual hard disk.
#
ERROR_VHD_BLOCK_ALLOCATION_FAILURE = 0xC03A0009

#
# MessageId: ERROR_VHD_BLOCK_ALLOCATION_TABLE_CORRUPT
#
# MessageText:
#
# The virtual hard disk is corrupted. The block allocation table in the virtual hard disk is corrupt.
#
ERROR_VHD_BLOCK_ALLOCATION_TABLE_CORRUPT = 0xC03A000A

#
# MessageId: ERROR_VHD_INVALID_BLOCK_SIZE
#
# MessageText:
#
# The system does not support this version of the virtual hard disk. The block size is invalid.
#
ERROR_VHD_INVALID_BLOCK_SIZE = 0xC03A000B

#
# MessageId: ERROR_VHD_BITMAP_MISMATCH
#
# MessageText:
#
# The virtual hard disk is corrupted. The block bitmap does not match with the block data present in the virtual hard disk.
#
ERROR_VHD_BITMAP_MISMATCH = 0xC03A000C

#
# MessageId: ERROR_VHD_PARENT_VHD_NOT_FOUND
#
# MessageText:
#
# The chain of virtual hard disks is broken. The system cannot locate the parent virtual hard disk for the differencing disk.
#
ERROR_VHD_PARENT_VHD_NOT_FOUND = 0xC03A000D

#
# MessageId: ERROR_VHD_CHILD_PARENT_ID_MISMATCH
#
# MessageText:
#
# The chain of virtual hard disks is corrupted. There is a mismatch in the identifiers of the parent virtual hard disk and differencing disk.
#
ERROR_VHD_CHILD_PARENT_ID_MISMATCH = 0xC03A000E

#
# MessageId: ERROR_VHD_CHILD_PARENT_TIMESTAMP_MISMATCH
#
# MessageText:
#
# The chain of virtual hard disks is corrupted. The time stamp of the parent virtual hard disk does not match the time stamp of the differencing disk.
#
ERROR_VHD_CHILD_PARENT_TIMESTAMP_MISMATCH = 0xC03A000F

#
# MessageId: ERROR_VHD_METADATA_READ_FAILURE
#
# MessageText:
#
# Failed to read the metadata of the virtual hard disk.
#
ERROR_VHD_METADATA_READ_FAILURE = 0xC03A0010

#
# MessageId: ERROR_VHD_METADATA_WRITE_FAILURE
#
# MessageText:
#
# Failed to write to the metadata of the virtual hard disk.
#
ERROR_VHD_METADATA_WRITE_FAILURE = 0xC03A0011

#
# MessageId: ERROR_VHD_INVALID_SIZE
#
# MessageText:
#
# The size of the virtual hard disk is not valid.
#
ERROR_VHD_INVALID_SIZE = 0xC03A0012

#
# MessageId: ERROR_VHD_INVALID_FILE_SIZE
#
# MessageText:
#
# The file size of this virtual hard disk is not valid.
#
ERROR_VHD_INVALID_FILE_SIZE = 0xC03A0013

#
# MessageId: ERROR_VIRTDISK_PROVIDER_NOT_FOUND
#
# MessageText:
#
# A virtual disk support provider for the specified file was not found.
#
ERROR_VIRTDISK_PROVIDER_NOT_FOUND = 0xC03A0014

#
# MessageId: ERROR_VIRTDISK_NOT_VIRTUAL_DISK
#
# MessageText:
#
# The specified disk is not a virtual disk.
#
ERROR_VIRTDISK_NOT_VIRTUAL_DISK = 0xC03A0015

#
# MessageId: ERROR_VHD_PARENT_VHD_ACCESS_DENIED
#
# MessageText:
#
# The chain of virtual hard disks is inaccessible. The process has not been granted access rights to the parent virtual hard disk for the differencing disk.
#
ERROR_VHD_PARENT_VHD_ACCESS_DENIED = 0xC03A0016

#
# MessageId: ERROR_VHD_CHILD_PARENT_SIZE_MISMATCH
#
# MessageText:
#
# The chain of virtual hard disks is corrupted. There is a mismatch in the virtual sizes of the parent virtual hard disk and differencing disk.
#
ERROR_VHD_CHILD_PARENT_SIZE_MISMATCH = 0xC03A0017

#
# MessageId: ERROR_VHD_DIFFERENCING_CHAIN_CYCLE_DETECTED
#
# MessageText:
#
# The chain of virtual hard disks is corrupted. A differencing disk is indicated in its own parent chain.
#
ERROR_VHD_DIFFERENCING_CHAIN_CYCLE_DETECTED = 0xC03A0018

#
# MessageId: ERROR_VHD_DIFFERENCING_CHAIN_ERROR_IN_PARENT
#
# MessageText:
#
# The chain of virtual hard disks is inaccessible. There was an error opening a virtual hard disk further up the chain.
#
ERROR_VHD_DIFFERENCING_CHAIN_ERROR_IN_PARENT = 0xC03A0019

#
# MessageId: ERROR_VIRTUAL_DISK_LIMITATION
#
# MessageText:
#
# The requested operation could not be completed due to a virtual disk system limitation.  On NTFS, virtual hard disk files must be uncompressed and unencrypted. On ReFS, virtual hard disk files must not have the integrity bit set.
#
ERROR_VIRTUAL_DISK_LIMITATION = 0xC03A001A

#
# MessageId: ERROR_VHD_INVALID_TYPE
#
# MessageText:
#
# The requested operation cannot be performed on a virtual disk of this type.
#
ERROR_VHD_INVALID_TYPE = 0xC03A001B

#
# MessageId: ERROR_VHD_INVALID_STATE
#
# MessageText:
#
# The requested operation cannot be performed on the virtual disk in its current state.
#
ERROR_VHD_INVALID_STATE = 0xC03A001C

#
# MessageId: ERROR_VIRTDISK_UNSUPPORTED_DISK_SECTOR_SIZE
#
# MessageText:
#
# The sector size of the physical disk on which the virtual disk resides is not supported.
#
ERROR_VIRTDISK_UNSUPPORTED_DISK_SECTOR_SIZE = 0xC03A001D

#
# MessageId: ERROR_VIRTDISK_DISK_ALREADY_OWNED
#
# MessageText:
#
# The disk is already owned by a different owner.
#
ERROR_VIRTDISK_DISK_ALREADY_OWNED = 0xC03A001E

#
# MessageId: ERROR_VIRTDISK_DISK_ONLINE_AND_WRITABLE
#
# MessageText:
#
# The disk must be offline or read-only.
#
ERROR_VIRTDISK_DISK_ONLINE_AND_WRITABLE = 0xC03A001F

#
# MessageId: ERROR_CTLOG_TRACKING_NOT_INITIALIZED
#
# MessageText:
#
# Change Tracking is not initialized for this virtual disk.
#
ERROR_CTLOG_TRACKING_NOT_INITIALIZED = 0xC03A0020

#
# MessageId: ERROR_CTLOG_LOGFILE_SIZE_EXCEEDED_MAXSIZE
#
# MessageText:
#
# Size of change tracking file exceeded the maximum size limit.
#
ERROR_CTLOG_LOGFILE_SIZE_EXCEEDED_MAXSIZE = 0xC03A0021

#
# MessageId: ERROR_CTLOG_VHD_CHANGED_OFFLINE
#
# MessageText:
#
# VHD file is changed due to compaction, expansion, or offline updates.
#
ERROR_CTLOG_VHD_CHANGED_OFFLINE = 0xC03A0022

#
# MessageId: ERROR_CTLOG_INVALID_TRACKING_STATE
#
# MessageText:
#
# Change Tracking for the virtual disk is not in a valid state to perform this request.  Change tracking could be discontinued or already in the requested state.
#
ERROR_CTLOG_INVALID_TRACKING_STATE = 0xC03A0023

#
# MessageId: ERROR_CTLOG_INCONSISTENT_TRACKING_FILE
#
# MessageText:
#
# Change Tracking file for the virtual disk is not in a valid state.
#
ERROR_CTLOG_INCONSISTENT_TRACKING_FILE = 0xC03A0024

#
# MessageId: ERROR_VHD_RESIZE_WOULD_TRUNCATE_DATA
#
# MessageText:
#
# The requested resize operation could not be completed because it might truncate user data residing on the virtual disk.
#
ERROR_VHD_RESIZE_WOULD_TRUNCATE_DATA = 0xC03A0025

#
# MessageId: ERROR_VHD_COULD_NOT_COMPUTE_MINIMUM_VIRTUAL_SIZE
#
# MessageText:
#
# The requested operation could not be completed because the virtual disk's minimum safe size could not be determined.
# This may be due to a missing or corrupt partition table.
#
ERROR_VHD_COULD_NOT_COMPUTE_MINIMUM_VIRTUAL_SIZE = 0xC03A0026

#
# MessageId: ERROR_VHD_ALREADY_AT_OR_BELOW_MINIMUM_VIRTUAL_SIZE
#
# MessageText:
#
# The requested operation could not be completed because the virtual disk's size cannot be safely reduced further.
#
ERROR_VHD_ALREADY_AT_OR_BELOW_MINIMUM_VIRTUAL_SIZE = 0xC03A0027

#
# MessageId: ERROR_VHD_METADATA_FULL
#
# MessageText:
#
# There is not enough space in the virtual disk file for the provided metadata item.
#
ERROR_VHD_METADATA_FULL = 0xC03A0028

#
# Warnings:
#
#
# MessageId: ERROR_QUERY_STORAGE_ERROR
#
# MessageText:
#
# The virtualization storage subsystem has generated an error.
#
ERROR_QUERY_STORAGE_ERROR = 0x803A0001

#
# =======================================================
# Facility Scripted Diagnostics (SDIAG) Error Messages
# =======================================================
#
#
# MessageId: SDIAG_E_CANCELLED
#
# MessageText:
#
# The operation was cancelled.
#
SDIAG_E_CANCELLED = 0x803C0100

#
# MessageId: SDIAG_E_SCRIPT
#
# MessageText:
#
# An error occurred when running a PowerShell script.
#
SDIAG_E_SCRIPT = 0x803C0101

#
# MessageId: SDIAG_E_POWERSHELL
#
# MessageText:
#
# An error occurred when interacting with PowerShell runtime.
#
SDIAG_E_POWERSHELL = 0x803C0102

#
# MessageId: SDIAG_E_MANAGEDHOST
#
# MessageText:
#
# An error occurred in the Scripted Diagnostic Managed Host.
#
SDIAG_E_MANAGEDHOST = 0x803C0103

#
# MessageId: SDIAG_E_NOVERIFIER
#
# MessageText:
#
# The troubleshooting pack does not contain a required verifier to complete the verification.
#
SDIAG_E_NOVERIFIER = 0x803C0104

#
# MessageId: SDIAG_S_CANNOTRUN
#
# MessageText:
#
# The troubleshooting pack cannot be executed on this system.
#
SDIAG_S_CANNOTRUN = 0x003C0105

#
# MessageId: SDIAG_E_DISABLED
#
# MessageText:
#
# Scripted diagnostics is disabled by group policy.
#
SDIAG_E_DISABLED = 0x803C0106

#
# MessageId: SDIAG_E_TRUST
#
# MessageText:
#
# Trust validation of the troubleshooting pack failed.
#
SDIAG_E_TRUST = 0x803C0107

#
# MessageId: SDIAG_E_CANNOTRUN
#
# MessageText:
#
# The troubleshooting pack cannot be executed on this system.
#
SDIAG_E_CANNOTRUN = 0x803C0108

#
# MessageId: SDIAG_E_VERSION
#
# MessageText:
#
# This version of the troubleshooting pack is not supported.
#
SDIAG_E_VERSION = 0x803C0109

#
# MessageId: SDIAG_E_RESOURCE
#
# MessageText:
#
# A required resource cannot be loaded.
#
SDIAG_E_RESOURCE = 0x803C010A

#
# MessageId: SDIAG_E_ROOTCAUSE
#
# MessageText:
#
# The troubleshooting pack reported information for a root cause without adding the root cause.
#
SDIAG_E_ROOTCAUSE = 0x803C010B

#
# =======================================================
# Facility Windows Push Notifications (WPN) Error Messages
# =======================================================
#
#
# MessageId: WPN_E_CHANNEL_CLOSED
#
# MessageText:
#
# The notification channel has already been closed.
#
WPN_E_CHANNEL_CLOSED = 0x803E0100

#
# MessageId: WPN_E_CHANNEL_REQUEST_NOT_COMPLETE
#
# MessageText:
#
# The notification channel request did not complete successfully.
#
WPN_E_CHANNEL_REQUEST_NOT_COMPLETE = 0x803E0101

#
# MessageId: WPN_E_INVALID_APP
#
# MessageText:
#
# The application identifier provided is invalid.
#
WPN_E_INVALID_APP = 0x803E0102

#
# MessageId: WPN_E_OUTSTANDING_CHANNEL_REQUEST
#
# MessageText:
#
# A notification channel request for the provided application identifier is in progress.
#
WPN_E_OUTSTANDING_CHANNEL_REQUEST = 0x803E0103

#
# MessageId: WPN_E_DUPLICATE_CHANNEL
#
# MessageText:
#
# The channel identifier is already tied to another application endpoint.
#
WPN_E_DUPLICATE_CHANNEL = 0x803E0104

#
# MessageId: WPN_E_PLATFORM_UNAVAILABLE
#
# MessageText:
#
# The notification platform is unavailable.
#
WPN_E_PLATFORM_UNAVAILABLE = 0x803E0105

#
# MessageId: WPN_E_NOTIFICATION_POSTED
#
# MessageText:
#
# The notification has already been posted.
#
WPN_E_NOTIFICATION_POSTED = 0x803E0106

#
# MessageId: WPN_E_NOTIFICATION_HIDDEN
#
# MessageText:
#
# The notification has already been hidden.
#
WPN_E_NOTIFICATION_HIDDEN = 0x803E0107

#
# MessageId: WPN_E_NOTIFICATION_NOT_POSTED
#
# MessageText:
#
# The notification cannot be hidden until it has been shown.
#
WPN_E_NOTIFICATION_NOT_POSTED = 0x803E0108

#
# MessageId: WPN_E_CLOUD_DISABLED
#
# MessageText:
#
# Cloud notifications have been turned off.
#
WPN_E_CLOUD_DISABLED = 0x803E0109

#
# MessageId: WPN_E_CLOUD_INCAPABLE
#
# MessageText:
#
# The application does not have the cloud notification capability.
#
WPN_E_CLOUD_INCAPABLE = 0x803E0110

#
# MessageId: WPN_E_CLOUD_AUTH_UNAVAILABLE
#
# MessageText:
#
# The notification platform is unable to retrieve the authentication credentials required to connect to the cloud notification service.
#
WPN_E_CLOUD_AUTH_UNAVAILABLE = 0x803E011A

#
# MessageId: WPN_E_CLOUD_SERVICE_UNAVAILABLE
#
# MessageText:
#
# The notification platform is unable to connect to the cloud notification service.
#
WPN_E_CLOUD_SERVICE_UNAVAILABLE = 0x803E011B

#
# MessageId: WPN_E_FAILED_LOCK_SCREEN_UPDATE_INTIALIZATION
#
# MessageText:
#
# The notification platform is unable to initialize a callback for lock screen updates.
#
WPN_E_FAILED_LOCK_SCREEN_UPDATE_INTIALIZATION = 0x803E011C

#
# MessageId: WPN_E_NOTIFICATION_DISABLED
#
# MessageText:
#
# Settings prevent the notification from being delivered.
#
WPN_E_NOTIFICATION_DISABLED = 0x803E0111

#
# MessageId: WPN_E_NOTIFICATION_INCAPABLE
#
# MessageText:
#
# Application capabilities prevent the notification from being delivered.
#
WPN_E_NOTIFICATION_INCAPABLE = 0x803E0112

#
# MessageId: WPN_E_INTERNET_INCAPABLE
#
# MessageText:
#
# The application does not have the internet access capability.
#
WPN_E_INTERNET_INCAPABLE = 0x803E0113

#
# MessageId: WPN_E_NOTIFICATION_TYPE_DISABLED
#
# MessageText:
#
# Settings prevent the notification type from being delivered.
#
WPN_E_NOTIFICATION_TYPE_DISABLED = 0x803E0114

#
# MessageId: WPN_E_NOTIFICATION_SIZE
#
# MessageText:
#
# The size of the notification content is too large.
#
WPN_E_NOTIFICATION_SIZE = 0x803E0115

#
# MessageId: WPN_E_TAG_SIZE
#
# MessageText:
#
# The size of the notification tag is too large.
#
WPN_E_TAG_SIZE = 0x803E0116

#
# MessageId: WPN_E_ACCESS_DENIED
#
# MessageText:
#
# The notification platform doesn't have appropriate privilege on resources.
#
WPN_E_ACCESS_DENIED = 0x803E0117

#
# MessageId: WPN_E_DUPLICATE_REGISTRATION
#
# MessageText:
#
# The notification platform found application is already registered.
#
WPN_E_DUPLICATE_REGISTRATION = 0x803E0118

#
# MessageId: WPN_E_PUSH_NOTIFICATION_INCAPABLE
#
# MessageText:
#
# The application background task does not have the push notification capability.
#
WPN_E_PUSH_NOTIFICATION_INCAPABLE = 0x803E0119

#
# MessageId: WPN_E_DEV_ID_SIZE
#
# MessageText:
#
# The size of the developer id for scheduled notification is too large.
#
WPN_E_DEV_ID_SIZE = 0x803E0120

#
# MessageId: WPN_E_TAG_ALPHANUMERIC
#
# MessageText:
#
# The notification tag is not alphanumeric.
#
WPN_E_TAG_ALPHANUMERIC = 0x803E012A

#
# MessageId: WPN_E_INVALID_HTTP_STATUS_CODE
#
# MessageText:
#
# The notification platform has received invalid HTTP status code other than 2xx for polling.
#
WPN_E_INVALID_HTTP_STATUS_CODE = 0x803E012B

#
# MessageId: WPN_E_OUT_OF_SESSION
#
# MessageText:
#
# The notification platform has run out of presentation layer sessions.
#
WPN_E_OUT_OF_SESSION = 0x803E0200

#
# MessageId: WPN_E_POWER_SAVE
#
# MessageText:
#
# The notification platform rejects image download request due to system in power save mode.
#
WPN_E_POWER_SAVE = 0x803E0201

#
# MessageId: WPN_E_IMAGE_NOT_FOUND_IN_CACHE
#
# MessageText:
#
# The notification platform doesn't have the requested image in its cache.
#
WPN_E_IMAGE_NOT_FOUND_IN_CACHE = 0x803E0202

#
# MessageId: WPN_E_ALL_URL_NOT_COMPLETED
#
# MessageText:
#
# The notification platform cannot complete all of requested image.
#
WPN_E_ALL_URL_NOT_COMPLETED = 0x803E0203

#
# MessageId: WPN_E_INVALID_CLOUD_IMAGE
#
# MessageText:
#
# A cloud image downloaded from the notification platform is invalid.
#
WPN_E_INVALID_CLOUD_IMAGE = 0x803E0204

#
# MessageId: WPN_E_NOTIFICATION_ID_MATCHED
#
# MessageText:
#
# Notification Id provided as filter is matched with what the notification platform maintains.
#
WPN_E_NOTIFICATION_ID_MATCHED = 0x803E0205

#
# MessageId: WPN_E_CALLBACK_ALREADY_REGISTERED
#
# MessageText:
#
# Notification callback interface is already registered.
#
WPN_E_CALLBACK_ALREADY_REGISTERED = 0x803E0206

#
# MessageId: WPN_E_TOAST_NOTIFICATION_DROPPED
#
# MessageText:
#
# Toast Notification was dropped without being displayed to the user.
#
WPN_E_TOAST_NOTIFICATION_DROPPED = 0x803E0207

#
# MessageId: WPN_E_STORAGE_LOCKED
#
# MessageText:
#
# The notification platform does not have the proper privileges to complete the request.
#
WPN_E_STORAGE_LOCKED = 0x803E0208


#
# MBN error codes
#

#
# MessageId: E_MBN_CONTEXT_NOT_ACTIVATED
#
# MessageText:
#
# Context is not activated.
#
E_MBN_CONTEXT_NOT_ACTIVATED = 0x80548201

#
# MessageId: E_MBN_BAD_SIM
#
# MessageText:
#
# Bad SIM is inserted.
#
E_MBN_BAD_SIM = 0x80548202

#
# MessageId: E_MBN_DATA_CLASS_NOT_AVAILABLE
#
# MessageText:
#
# Requested data class is not avaialable.
#
E_MBN_DATA_CLASS_NOT_AVAILABLE = 0x80548203

#
# MessageId: E_MBN_INVALID_ACCESS_STRING
#
# MessageText:
#
# Access point name (APN) or Access string is incorrect.
#
E_MBN_INVALID_ACCESS_STRING = 0x80548204

#
# MessageId: E_MBN_MAX_ACTIVATED_CONTEXTS
#
# MessageText:
#
# Max activated contexts have reached.
#
E_MBN_MAX_ACTIVATED_CONTEXTS = 0x80548205

#
# MessageId: E_MBN_PACKET_SVC_DETACHED
#
# MessageText:
#
# Device is in packet detach state.
#
E_MBN_PACKET_SVC_DETACHED = 0x80548206

#
# MessageId: E_MBN_PROVIDER_NOT_VISIBLE
#
# MessageText:
#
# Provider is not visible.
#
E_MBN_PROVIDER_NOT_VISIBLE = 0x80548207

#
# MessageId: E_MBN_RADIO_POWER_OFF
#
# MessageText:
#
# Radio is powered off.
#
E_MBN_RADIO_POWER_OFF = 0x80548208

#
# MessageId: E_MBN_SERVICE_NOT_ACTIVATED
#
# MessageText:
#
# MBN subscription is not activated.
#
E_MBN_SERVICE_NOT_ACTIVATED = 0x80548209

#
# MessageId: E_MBN_SIM_NOT_INSERTED
#
# MessageText:
#
# SIM is not inserted.
#
E_MBN_SIM_NOT_INSERTED = 0x8054820A

#
# MessageId: E_MBN_VOICE_CALL_IN_PROGRESS
#
# MessageText:
#
# Voice call in progress.
#
E_MBN_VOICE_CALL_IN_PROGRESS = 0x8054820B

#
# MessageId: E_MBN_INVALID_CACHE
#
# MessageText:
#
# Visible provider cache is invalid.
#
E_MBN_INVALID_CACHE = 0x8054820C

#
# MessageId: E_MBN_NOT_REGISTERED
#
# MessageText:
#
# Device is not registered.
#
E_MBN_NOT_REGISTERED = 0x8054820D

#
# MessageId: E_MBN_PROVIDERS_NOT_FOUND
#
# MessageText:
#
# Providers not found.
#
E_MBN_PROVIDERS_NOT_FOUND = 0x8054820E

#
# MessageId: E_MBN_PIN_NOT_SUPPORTED
#
# MessageText:
#
# Pin is not supported.
#
E_MBN_PIN_NOT_SUPPORTED = 0x8054820F

#
# MessageId: E_MBN_PIN_REQUIRED
#
# MessageText:
#
# Pin is required.
#
E_MBN_PIN_REQUIRED = 0x80548210

#
# MessageId: E_MBN_PIN_DISABLED
#
# MessageText:
#
# PIN is disabled.
#
E_MBN_PIN_DISABLED = 0x80548211

#
# MessageId: E_MBN_FAILURE
#
# MessageText:
#
# Generic Failure.
#
E_MBN_FAILURE = 0x80548212

# Profile related error messages
#
# MessageId: E_MBN_INVALID_PROFILE
#
# MessageText:
#
# Profile is invalid.
#
E_MBN_INVALID_PROFILE = 0x80548218

#
# MessageId: E_MBN_DEFAULT_PROFILE_EXIST
#
# MessageText:
#
# Default profile exist.
#
E_MBN_DEFAULT_PROFILE_EXIST = 0x80548219

# SMS related error messages
#
# MessageId: E_MBN_SMS_ENCODING_NOT_SUPPORTED
#
# MessageText:
#
# SMS encoding is not supported.
#
E_MBN_SMS_ENCODING_NOT_SUPPORTED = 0x80548220

#
# MessageId: E_MBN_SMS_FILTER_NOT_SUPPORTED
#
# MessageText:
#
# SMS filter is not supported.
#
E_MBN_SMS_FILTER_NOT_SUPPORTED = 0x80548221

#
# MessageId: E_MBN_SMS_INVALID_MEMORY_INDEX
#
# MessageText:
#
# Invalid SMS memory index is used.
#
E_MBN_SMS_INVALID_MEMORY_INDEX = 0x80548222

#
# MessageId: E_MBN_SMS_LANG_NOT_SUPPORTED
#
# MessageText:
#
# SMS language is not supported.
#
E_MBN_SMS_LANG_NOT_SUPPORTED = 0x80548223

#
# MessageId: E_MBN_SMS_MEMORY_FAILURE
#
# MessageText:
#
# SMS memory failure occurred.
#
E_MBN_SMS_MEMORY_FAILURE = 0x80548224

#
# MessageId: E_MBN_SMS_NETWORK_TIMEOUT
#
# MessageText:
#
# SMS network timeout happened.
#
E_MBN_SMS_NETWORK_TIMEOUT = 0x80548225

#
# MessageId: E_MBN_SMS_UNKNOWN_SMSC_ADDRESS
#
# MessageText:
#
# Unknown SMSC address is used.
#
E_MBN_SMS_UNKNOWN_SMSC_ADDRESS = 0x80548226

#
# MessageId: E_MBN_SMS_FORMAT_NOT_SUPPORTED
#
# MessageText:
#
# SMS format is not supported.
#
E_MBN_SMS_FORMAT_NOT_SUPPORTED = 0x80548227

#
# MessageId: E_MBN_SMS_OPERATION_NOT_ALLOWED
#
# MessageText:
#
# SMS operation is not allowed.
#
E_MBN_SMS_OPERATION_NOT_ALLOWED = 0x80548228

#
# MessageId: E_MBN_SMS_MEMORY_FULL
#
# MessageText:
#
# Device SMS memory is full.
#
E_MBN_SMS_MEMORY_FULL = 0x80548229


#
# P2P error codes
#

#
# MessageId: PEER_E_IPV6_NOT_INSTALLED
#
# MessageText:
#
# The IPv6 protocol is not installed.
#
PEER_E_IPV = 6

#
# MessageId: PEER_E_NOT_INITIALIZED
#
# MessageText:
#
# The compoment has not been initialized.
#
PEER_E_NOT_INITIALIZED = 0x80630002

#
# MessageId: PEER_E_CANNOT_START_SERVICE
#
# MessageText:
#
# The required service canot be started.
#
PEER_E_CANNOT_START_SERVICE = 0x80630003

#
# MessageId: PEER_E_NOT_LICENSED
#
# MessageText:
#
# The P2P protocol is not licensed to run on this OS.
#
PEER_E_NOT_LICENSED = 0x80630004

#
# MessageId: PEER_E_INVALID_GRAPH
#
# MessageText:
#
# The graph handle is invalid.
#
PEER_E_INVALID_GRAPH = 0x80630010

#
# MessageId: PEER_E_DBNAME_CHANGED
#
# MessageText:
#
# The graph database name has changed.
#
PEER_E_DBNAME_CHANGED = 0x80630011

#
# MessageId: PEER_E_DUPLICATE_GRAPH
#
# MessageText:
#
# A graph with the same ID already exists.
#
PEER_E_DUPLICATE_GRAPH = 0x80630012

#
# MessageId: PEER_E_GRAPH_NOT_READY
#
# MessageText:
#
# The graph is not ready.
#
PEER_E_GRAPH_NOT_READY = 0x80630013

#
# MessageId: PEER_E_GRAPH_SHUTTING_DOWN
#
# MessageText:
#
# The graph is shutting down.
#
PEER_E_GRAPH_SHUTTING_DOWN = 0x80630014

#
# MessageId: PEER_E_GRAPH_IN_USE
#
# MessageText:
#
# The graph is still in use.
#
PEER_E_GRAPH_IN_USE = 0x80630015

#
# MessageId: PEER_E_INVALID_DATABASE
#
# MessageText:
#
# The graph database is corrupt.
#
PEER_E_INVALID_DATABASE = 0x80630016

#
# MessageId: PEER_E_TOO_MANY_ATTRIBUTES
#
# MessageText:
#
# Too many attributes have been used.
#
PEER_E_TOO_MANY_ATTRIBUTES = 0x80630017

#
# MessageId: PEER_E_CONNECTION_NOT_FOUND
#
# MessageText:
#
# The connection can not be found.
#
PEER_E_CONNECTION_NOT_FOUND = 0x80630103

#
# MessageId: PEER_E_CONNECT_SELF
#
# MessageText:
#
# The peer attempted to connect to itself.
#
PEER_E_CONNECT_SELF = 0x80630106

#
# MessageId: PEER_E_ALREADY_LISTENING
#
# MessageText:
#
# The peer is already listening for connections.
#
PEER_E_ALREADY_LISTENING = 0x80630107

#
# MessageId: PEER_E_NODE_NOT_FOUND
#
# MessageText:
#
# The node was not found.
#
PEER_E_NODE_NOT_FOUND = 0x80630108

#
# MessageId: PEER_E_CONNECTION_FAILED
#
# MessageText:
#
# The Connection attempt failed.
#
PEER_E_CONNECTION_FAILED = 0x80630109

#
# MessageId: PEER_E_CONNECTION_NOT_AUTHENTICATED
#
# MessageText:
#
# The peer connection could not be authenticated.
#
PEER_E_CONNECTION_NOT_AUTHENTICATED = 0x8063010A

#
# MessageId: PEER_E_CONNECTION_REFUSED
#
# MessageText:
#
# The connection was refused.
#
PEER_E_CONNECTION_REFUSED = 0x8063010B

#
# MessageId: PEER_E_CLASSIFIER_TOO_LONG
#
# MessageText:
#
# The peer name classifier is too long.
#
PEER_E_CLASSIFIER_TOO_LONG = 0x80630201

#
# MessageId: PEER_E_TOO_MANY_IDENTITIES
#
# MessageText:
#
# The maximum number of identities have been created.
#
PEER_E_TOO_MANY_IDENTITIES = 0x80630202

#
# MessageId: PEER_E_NO_KEY_ACCESS
#
# MessageText:
#
# Unable to access a key.
#
PEER_E_NO_KEY_ACCESS = 0x80630203

#
# MessageId: PEER_E_GROUPS_EXIST
#
# MessageText:
#
# The group already exists.
#
PEER_E_GROUPS_EXIST = 0x80630204

# record error codes
#
# MessageId: PEER_E_RECORD_NOT_FOUND
#
# MessageText:
#
# The requested record could not be found.
#
PEER_E_RECORD_NOT_FOUND = 0x80630301

#
# MessageId: PEER_E_DATABASE_ACCESSDENIED
#
# MessageText:
#
# Access to the database was denied.
#
PEER_E_DATABASE_ACCESSDENIED = 0x80630302

#
# MessageId: PEER_E_DBINITIALIZATION_FAILED
#
# MessageText:
#
# The Database could not be initialized.
#
PEER_E_DBINITIALIZATION_FAILED = 0x80630303

#
# MessageId: PEER_E_MAX_RECORD_SIZE_EXCEEDED
#
# MessageText:
#
# The record is too big.
#
PEER_E_MAX_RECORD_SIZE_EXCEEDED = 0x80630304

#
# MessageId: PEER_E_DATABASE_ALREADY_PRESENT
#
# MessageText:
#
# The database already exists.
#
PEER_E_DATABASE_ALREADY_PRESENT = 0x80630305

#
# MessageId: PEER_E_DATABASE_NOT_PRESENT
#
# MessageText:
#
# The database could not be found.
#
PEER_E_DATABASE_NOT_PRESENT = 0x80630306

#
# MessageId: PEER_E_IDENTITY_NOT_FOUND
#
# MessageText:
#
# The identity could not be found.
#
PEER_E_IDENTITY_NOT_FOUND = 0x80630401

# eventing error
#
# MessageId: PEER_E_EVENT_HANDLE_NOT_FOUND
#
# MessageText:
#
# The event handle could not be found.
#
PEER_E_EVENT_HANDLE_NOT_FOUND = 0x80630501

# searching error
#
# MessageId: PEER_E_INVALID_SEARCH
#
# MessageText:
#
# Invalid search.
#
PEER_E_INVALID_SEARCH = 0x80630601

#
# MessageId: PEER_E_INVALID_ATTRIBUTES
#
# MessageText:
#
# The search atributes are invalid.
#
PEER_E_INVALID_ATTRIBUTES = 0x80630602


# certificate verification error codes
#
# MessageId: PEER_E_INVITATION_NOT_TRUSTED
#
# MessageText:
#
# The invitiation is not trusted.
#
PEER_E_INVITATION_NOT_TRUSTED = 0x80630701

#
# MessageId: PEER_E_CHAIN_TOO_LONG
#
# MessageText:
#
# The certchain is too long.
#
PEER_E_CHAIN_TOO_LONG = 0x80630703

#
# MessageId: PEER_E_INVALID_TIME_PERIOD
#
# MessageText:
#
# The time period is invalid.
#
PEER_E_INVALID_TIME_PERIOD = 0x80630705

#
# MessageId: PEER_E_CIRCULAR_CHAIN_DETECTED
#
# MessageText:
#
# A circular cert chain was detected.
#
PEER_E_CIRCULAR_CHAIN_DETECTED = 0x80630706

#
# MessageId: PEER_E_CERT_STORE_CORRUPTED
#
# MessageText:
#
# The certstore is corrupted.
#
PEER_E_CERT_STORE_CORRUPTED = 0x80630801

#
# MessageId: PEER_E_NO_CLOUD
#
# MessageText:
#
# The specified PNRP cloud deos not exist.
#
PEER_E_NO_CLOUD = 0x80631001

#
# MessageId: PEER_E_CLOUD_NAME_AMBIGUOUS
#
# MessageText:
#
# The cloud name is ambiguous.
#
PEER_E_CLOUD_NAME_AMBIGUOUS = 0x80631005

#
# MessageId: PEER_E_INVALID_RECORD
#
# MessageText:
#
# The record is invlaid.
#
PEER_E_INVALID_RECORD = 0x80632010

#
# MessageId: PEER_E_NOT_AUTHORIZED
#
# MessageText:
#
# Not authorized.
#
PEER_E_NOT_AUTHORIZED = 0x80632020

#
# MessageId: PEER_E_PASSWORD_DOES_NOT_MEET_POLICY
#
# MessageText:
#
# The password does not meet policy requirements.
#
PEER_E_PASSWORD_DOES_NOT_MEET_POLICY = 0x80632021

#
# MessageId: PEER_E_DEFERRED_VALIDATION
#
# MessageText:
#
# The record validation has been defered.
#
PEER_E_DEFERRED_VALIDATION = 0x80632030

#
# MessageId: PEER_E_INVALID_GROUP_PROPERTIES
#
# MessageText:
#
# The group properies are invalid.
#
PEER_E_INVALID_GROUP_PROPERTIES = 0x80632040

#
# MessageId: PEER_E_INVALID_PEER_NAME
#
# MessageText:
#
# The peername is invalid.
#
PEER_E_INVALID_PEER_NAME = 0x80632050

#
# MessageId: PEER_E_INVALID_CLASSIFIER
#
# MessageText:
#
# The classifier is invalid.
#
PEER_E_INVALID_CLASSIFIER = 0x80632060

#
# MessageId: PEER_E_INVALID_FRIENDLY_NAME
#
# MessageText:
#
# The friendly name is invalid.
#
PEER_E_INVALID_FRIENDLY_NAME = 0x80632070

#
# MessageId: PEER_E_INVALID_ROLE_PROPERTY
#
# MessageText:
#
# Invalid role property.
#
PEER_E_INVALID_ROLE_PROPERTY = 0x80632071

#
# MessageId: PEER_E_INVALID_CLASSIFIER_PROPERTY
#
# MessageText:
#
# Invalid classifer property.
#
PEER_E_INVALID_CLASSIFIER_PROPERTY = 0x80632072

#
# MessageId: PEER_E_INVALID_RECORD_EXPIRATION
#
# MessageText:
#
# Invlaid record expiration.
#
PEER_E_INVALID_RECORD_EXPIRATION = 0x80632080

#
# MessageId: PEER_E_INVALID_CREDENTIAL_INFO
#
# MessageText:
#
# Invlaid credential info.
#
PEER_E_INVALID_CREDENTIAL_INFO = 0x80632081

#
# MessageId: PEER_E_INVALID_CREDENTIAL
#
# MessageText:
#
# Invalid credential.
#
PEER_E_INVALID_CREDENTIAL = 0x80632082

#
# MessageId: PEER_E_INVALID_RECORD_SIZE
#
# MessageText:
#
# Invalid record size.
#
PEER_E_INVALID_RECORD_SIZE = 0x80632083

#
# MessageId: PEER_E_UNSUPPORTED_VERSION
#
# MessageText:
#
# Unsupported version.
#
PEER_E_UNSUPPORTED_VERSION = 0x80632090

#
# MessageId: PEER_E_GROUP_NOT_READY
#
# MessageText:
#
# The group is not ready.
#
PEER_E_GROUP_NOT_READY = 0x80632091

#
# MessageId: PEER_E_GROUP_IN_USE
#
# MessageText:
#
# The group is still in use.
#
PEER_E_GROUP_IN_USE = 0x80632092

#
# MessageId: PEER_E_INVALID_GROUP
#
# MessageText:
#
# The group is invalid.
#
PEER_E_INVALID_GROUP = 0x80632093

#
# MessageId: PEER_E_NO_MEMBERS_FOUND
#
# MessageText:
#
# No members were found.
#
PEER_E_NO_MEMBERS_FOUND = 0x80632094

#
# MessageId: PEER_E_NO_MEMBER_CONNECTIONS
#
# MessageText:
#
# There are no member connections.
#
PEER_E_NO_MEMBER_CONNECTIONS = 0x80632095

#
# MessageId: PEER_E_UNABLE_TO_LISTEN
#
# MessageText:
#
# Unable to listen.
#
PEER_E_UNABLE_TO_LISTEN = 0x80632096

#
# MessageId: PEER_E_IDENTITY_DELETED
#
# MessageText:
#
# The identity does not exist.
#
PEER_E_IDENTITY_DELETED = 0x806320A0

#
# MessageId: PEER_E_SERVICE_NOT_AVAILABLE
#
# MessageText:
#
# The service is not availible.
#
PEER_E_SERVICE_NOT_AVAILABLE = 0x806320A1

# Contacts APIs error code
#
# MessageId: PEER_E_CONTACT_NOT_FOUND
#
# MessageText:
#
# THe contact could not be found.
#
PEER_E_CONTACT_NOT_FOUND = 0x80636001

# Special success codes
#
# MessageId: PEER_S_GRAPH_DATA_CREATED
#
# MessageText:
#
# The graph data was created.
#
PEER_S_GRAPH_DATA_CREATED = 0x00630001

#
# MessageId: PEER_S_NO_EVENT_DATA
#
# MessageText:
#
# There is not more event data.
#
PEER_S_NO_EVENT_DATA = 0x00630002

#
# MessageId: PEER_S_ALREADY_CONNECTED
#
# MessageText:
#
# The graph is already connect.
#
PEER_S_ALREADY_CONNECTED = 0x00632000

#
# MessageId: PEER_S_SUBSCRIPTION_EXISTS
#
# MessageText:
#
# The subscription already exists.
#
PEER_S_SUBSCRIPTION_EXISTS = 0x00636000

#
# MessageId: PEER_S_NO_CONNECTIVITY
#
# MessageText:
#
# No connectivity.
#
PEER_S_NO_CONNECTIVITY = 0x00630005

#
# MessageId: PEER_S_ALREADY_A_MEMBER
#
# MessageText:
#
# Already a member.
#
PEER_S_ALREADY_A_MEMBER = 0x00630006

# Pnrp helpers errors
#
# MessageId: PEER_E_CANNOT_CONVERT_PEER_NAME
#
# MessageText:
#
# The peername could not be converted to a DNS pnrp name.
#
PEER_E_CANNOT_CONVERT_PEER_NAME = 0x80634001

#
# MessageId: PEER_E_INVALID_PEER_HOST_NAME
#
# MessageText:
#
# Invalid peer host name.
#
PEER_E_INVALID_PEER_HOST_NAME = 0x80634002

#
# MessageId: PEER_E_NO_MORE
#
# MessageText:
#
# No more data could be found.
#
PEER_E_NO_MORE = 0x80634003

#
# MessageId: PEER_E_PNRP_DUPLICATE_PEER_NAME
#
# MessageText:
#
# The existing peer name is already registered.
#
PEER_E_PNRP_DUPLICATE_PEER_NAME = 0x80634005

# AppInvite APIs error code
#
# MessageId: PEER_E_INVITE_CANCELLED
#
# MessageText:
#
# The app invite request was cancelled by the user.
#
PEER_E_INVITE_CANCELLED = 0x80637000

#
# MessageId: PEER_E_INVITE_RESPONSE_NOT_AVAILABLE
#
# MessageText:
#
# No response of the invite was received.
#
PEER_E_INVITE_RESPONSE_NOT_AVAILABLE = 0x80637001

# Serverless presence error codes
#
# MessageId: PEER_E_NOT_SIGNED_IN
#
# MessageText:
#
# User is not signed into serverless presence.
#
PEER_E_NOT_SIGNED_IN = 0x80637003

#
# MessageId: PEER_E_PRIVACY_DECLINED
#
# MessageText:
#
# The user declined the privacy policy prompt.
#
PEER_E_PRIVACY_DECLINED = 0x80637004

#
# MessageId: PEER_E_TIMEOUT
#
# MessageText:
#
# A timeout occurred.
#
PEER_E_TIMEOUT = 0x80637005

#
# MessageId: PEER_E_INVALID_ADDRESS
#
# MessageText:
#
# The address is invalid.
#
PEER_E_INVALID_ADDRESS = 0x80637007

#
# MessageId: PEER_E_FW_EXCEPTION_DISABLED
#
# MessageText:
#
# A required firewall exception is disabled.
#
PEER_E_FW_EXCEPTION_DISABLED = 0x80637008

#
# MessageId: PEER_E_FW_BLOCKED_BY_POLICY
#
# MessageText:
#
# The service is blocked by a firewall policy.
#
PEER_E_FW_BLOCKED_BY_POLICY = 0x80637009

#
# MessageId: PEER_E_FW_BLOCKED_BY_SHIELDS_UP
#
# MessageText:
#
# Firewall exceptions are disabled.
#
PEER_E_FW_BLOCKED_BY_SHIELDS_UP = 0x8063700A

#
# MessageId: PEER_E_FW_DECLINED
#
# MessageText:
#
# The user declined to enable the firewall exceptions.
#
PEER_E_FW_DECLINED = 0x8063700B


#
# UI error codes
#

#
# MessageId: UI_E_CREATE_FAILED
#
# MessageText:
#
# The object could not be created.
#
UI_E_CREATE_FAILED = 0x802A0001

#
# MessageId: UI_E_SHUTDOWN_CALLED
#
# MessageText:
#
# Shutdown was already called on this object or the object that owns it.
#
UI_E_SHUTDOWN_CALLED = 0x802A0002

#
# MessageId: UI_E_ILLEGAL_REENTRANCY
#
# MessageText:
#
# This method cannot be called during this type of callback.
#
UI_E_ILLEGAL_REENTRANCY = 0x802A0003

#
# MessageId: UI_E_OBJECT_SEALED
#
# MessageText:
#
# This object has been sealed, so this change is no longer allowed.
#
UI_E_OBJECT_SEALED = 0x802A0004

#
# MessageId: UI_E_VALUE_NOT_SET
#
# MessageText:
#
# The requested value was never set.
#
UI_E_VALUE_NOT_SET = 0x802A0005

#
# MessageId: UI_E_VALUE_NOT_DETERMINED
#
# MessageText:
#
# The requested value cannot be determined.
#
UI_E_VALUE_NOT_DETERMINED = 0x802A0006

#
# MessageId: UI_E_INVALID_OUTPUT
#
# MessageText:
#
# A callback returned an invalid output parameter.
#
UI_E_INVALID_OUTPUT = 0x802A0007

#
# MessageId: UI_E_BOOLEAN_EXPECTED
#
# MessageText:
#
# A callback returned a success code other than S_OK or S_FALSE.
#
UI_E_BOOLEAN_EXPECTED = 0x802A0008

#
# MessageId: UI_E_DIFFERENT_OWNER
#
# MessageText:
#
# A parameter that should be owned by this object is owned by a different object.
#
UI_E_DIFFERENT_OWNER = 0x802A0009

#
# MessageId: UI_E_AMBIGUOUS_MATCH
#
# MessageText:
#
# More than one item matched the search criteria.
#
UI_E_AMBIGUOUS_MATCH = 0x802A000A

#
# MessageId: UI_E_FP_OVERFLOW
#
# MessageText:
#
# A floating-point overflow occurred.
#
UI_E_FP_OVERFLOW = 0x802A000B

#
# MessageId: UI_E_WRONG_THREAD
#
# MessageText:
#
# This method can only be called from the thread that created the object.
#
UI_E_WRONG_THREAD = 0x802A000C

#
# MessageId: UI_E_STORYBOARD_ACTIVE
#
# MessageText:
#
# The storyboard is currently in the schedule.
#
UI_E_STORYBOARD_ACTIVE = 0x802A0101

#
# MessageId: UI_E_STORYBOARD_NOT_PLAYING
#
# MessageText:
#
# The storyboard is not playing.
#
UI_E_STORYBOARD_NOT_PLAYING = 0x802A0102

#
# MessageId: UI_E_START_KEYFRAME_AFTER_END
#
# MessageText:
#
# The start keyframe might occur after the end keyframe.
#
UI_E_START_KEYFRAME_AFTER_END = 0x802A0103

#
# MessageId: UI_E_END_KEYFRAME_NOT_DETERMINED
#
# MessageText:
#
# It might not be possible to determine the end keyframe time when the start keyframe is reached.
#
UI_E_END_KEYFRAME_NOT_DETERMINED = 0x802A0104

#
# MessageId: UI_E_LOOPS_OVERLAP
#
# MessageText:
#
# Two repeated portions of a storyboard might overlap.
#
UI_E_LOOPS_OVERLAP = 0x802A0105

#
# MessageId: UI_E_TRANSITION_ALREADY_USED
#
# MessageText:
#
# The transition has already been added to a storyboard.
#
UI_E_TRANSITION_ALREADY_USED = 0x802A0106

#
# MessageId: UI_E_TRANSITION_NOT_IN_STORYBOARD
#
# MessageText:
#
# The transition has not been added to a storyboard.
#
UI_E_TRANSITION_NOT_IN_STORYBOARD = 0x802A0107

#
# MessageId: UI_E_TRANSITION_ECLIPSED
#
# MessageText:
#
# The transition might eclipse the beginning of another transition in the storyboard.
#
UI_E_TRANSITION_ECLIPSED = 0x802A0108

#
# MessageId: UI_E_TIME_BEFORE_LAST_UPDATE
#
# MessageText:
#
# The given time is earlier than the time passed to the last update.
#
UI_E_TIME_BEFORE_LAST_UPDATE = 0x802A0109

#
# MessageId: UI_E_TIMER_CLIENT_ALREADY_CONNECTED
#
# MessageText:
#
# This client is already connected to a timer.
#
UI_E_TIMER_CLIENT_ALREADY_CONNECTED = 0x802A010A

#
# MessageId: UI_E_INVALID_DIMENSION
#
# MessageText:
#
# The passed dimension is invalid or does not match the object's dimension.
#
UI_E_INVALID_DIMENSION = 0x802A010B

#
# MessageId: UI_E_PRIMITIVE_OUT_OF_BOUNDS
#
# MessageText:
#
# The added primitive begins at or beyond the duration of the interpolator.
#
UI_E_PRIMITIVE_OUT_OF_BOUNDS = 0x802A010C

#
# MessageId: UI_E_WINDOW_CLOSED
#
# MessageText:
#
# The operation cannot be completed because the window is being closed.
#
UI_E_WINDOW_CLOSED = 0x802A0201


#
# Bluetooth Attribute Protocol Warnings
#

#
# MessageId: E_BLUETOOTH_ATT_INVALID_HANDLE
#
# MessageText:
#
# The attribute handle given was not valid on this server.
#
E_BLUETOOTH_ATT_INVALID_HANDLE = 0x80650001

#
# MessageId: E_BLUETOOTH_ATT_READ_NOT_PERMITTED
#
# MessageText:
#
# The attribute cannot be read.
#
E_BLUETOOTH_ATT_READ_NOT_PERMITTED = 0x80650002

#
# MessageId: E_BLUETOOTH_ATT_WRITE_NOT_PERMITTED
#
# MessageText:
#
# The attribute cannot be written.
#
E_BLUETOOTH_ATT_WRITE_NOT_PERMITTED = 0x80650003

#
# MessageId: E_BLUETOOTH_ATT_INVALID_PDU
#
# MessageText:
#
# The attribute PDU was invalid.
#
E_BLUETOOTH_ATT_INVALID_PDU = 0x80650004

#
# MessageId: E_BLUETOOTH_ATT_INSUFFICIENT_AUTHENTICATION
#
# MessageText:
#
# The attribute requires authentication before it can be read or written.
#
E_BLUETOOTH_ATT_INSUFFICIENT_AUTHENTICATION = 0x80650005

#
# MessageId: E_BLUETOOTH_ATT_REQUEST_NOT_SUPPORTED
#
# MessageText:
#
# Attribute server does not support the request received from the client.
#
E_BLUETOOTH_ATT_REQUEST_NOT_SUPPORTED = 0x80650006

#
# MessageId: E_BLUETOOTH_ATT_INVALID_OFFSET
#
# MessageText:
#
# Offset specified was past the end of the attribute.
#
E_BLUETOOTH_ATT_INVALID_OFFSET = 0x80650007

#
# MessageId: E_BLUETOOTH_ATT_INSUFFICIENT_AUTHORIZATION
#
# MessageText:
#
# The attribute requires authorization before it can be read or written.
#
E_BLUETOOTH_ATT_INSUFFICIENT_AUTHORIZATION = 0x80650008

#
# MessageId: E_BLUETOOTH_ATT_PREPARE_QUEUE_FULL
#
# MessageText:
#
# Too many prepare writes have been queued.
#
E_BLUETOOTH_ATT_PREPARE_QUEUE_FULL = 0x80650009

#
# MessageId: E_BLUETOOTH_ATT_ATTRIBUTE_NOT_FOUND
#
# MessageText:
#
# No attribute found within the given attribute handle range.
#
E_BLUETOOTH_ATT_ATTRIBUTE_NOT_FOUND = 0x8065000A

#
# MessageId: E_BLUETOOTH_ATT_ATTRIBUTE_NOT_LONG
#
# MessageText:
#
# The attribute cannot be read or written using the Read Blob Request.
#
E_BLUETOOTH_ATT_ATTRIBUTE_NOT_LONG = 0x8065000B

#
# MessageId: E_BLUETOOTH_ATT_INSUFFICIENT_ENCRYPTION_KEY_SIZE
#
# MessageText:
#
# The Encryption Key Size used for encrypting this link is insufficient.
#
E_BLUETOOTH_ATT_INSUFFICIENT_ENCRYPTION_KEY_SIZE = 0x8065000C

#
# MessageId: E_BLUETOOTH_ATT_INVALID_ATTRIBUTE_VALUE_LENGTH
#
# MessageText:
#
# The attribute value length is invalid for the operation.
#
E_BLUETOOTH_ATT_INVALID_ATTRIBUTE_VALUE_LENGTH = 0x8065000D

#
# MessageId: E_BLUETOOTH_ATT_UNLIKELY
#
# MessageText:
#
# The attribute request that was requested has encountered an error that was unlikely, and therefore could not be completed as requested.
#
E_BLUETOOTH_ATT_UNLIKELY = 0x8065000E

#
# MessageId: E_BLUETOOTH_ATT_INSUFFICIENT_ENCRYPTION
#
# MessageText:
#
# The attribute requires encryption before it can be read or written.
#
E_BLUETOOTH_ATT_INSUFFICIENT_ENCRYPTION = 0x8065000F

#
# MessageId: E_BLUETOOTH_ATT_UNSUPPORTED_GROUP_TYPE
#
# MessageText:
#
# The attribute type is not a supported grouping attribute as defined by a higher layer specification.
#
E_BLUETOOTH_ATT_UNSUPPORTED_GROUP_TYPE = 0x80650010

#
# MessageId: E_BLUETOOTH_ATT_INSUFFICIENT_RESOURCES
#
# MessageText:
#
# Insufficient Resources to complete the request.
#
E_BLUETOOTH_ATT_INSUFFICIENT_RESOURCES = 0x80650011

#
# MessageId: E_BLUETOOTH_ATT_UNKNOWN_ERROR
#
# MessageText:
#
# An error that lies in the reserved range has been received.
#
E_BLUETOOTH_ATT_UNKNOWN_ERROR = 0x80651000


#
# Audio errors
#

#
# MessageId: E_AUDIO_ENGINE_NODE_NOT_FOUND
#
# MessageText:
#
# PortCls could not find an audio engine node exposed by a miniport driver claiming support for IMiniportAudioEngineNode.
#
E_AUDIO_ENGINE_NODE_NOT_FOUND = 0x80660001

#
# MessageId: E_HDAUDIO_EMPTY_CONNECTION_LIST
#
# MessageText:
#
# HD Audio widget encountered an unexpected empty connection list.
#
E_HDAUDIO_EMPTY_CONNECTION_LIST = 0x80660002

#
# MessageId: E_HDAUDIO_CONNECTION_LIST_NOT_SUPPORTED
#
# MessageText:
#
# HD Audio widget does not support the connection list parameter.
#
E_HDAUDIO_CONNECTION_LIST_NOT_SUPPORTED = 0x80660003

#
# MessageId: E_HDAUDIO_NO_LOGICAL_DEVICES_CREATED
#
# MessageText:
#
# No HD Audio subdevices were successfully created.
#
E_HDAUDIO_NO_LOGICAL_DEVICES_CREATED = 0x80660004

#
# MessageId: E_HDAUDIO_NULL_LINKED_LIST_ENTRY
#
# MessageText:
#
# An unexpected NULL pointer was encountered in a linked list.
#
E_HDAUDIO_NULL_LINKED_LIST_ENTRY = 0x80660005

#
# Spaceport errors
#
# Success
#
# MessageId: ERROR_SPACES_POOL_WAS_DELETED
#
# MessageText:
#
# The storage pool was deleted by the driver. The object cache should be updated.
#
ERROR_SPACES_POOL_WAS_DELETED = 0x00E70001

# Errors
#
# MessageId: ERROR_SPACES_RESILIENCY_TYPE_INVALID
#
# MessageText:
#
# The specified resiliency type is not valid.
#
ERROR_SPACES_RESILIENCY_TYPE_INVALID = 0x80E70003

#
# MessageId: ERROR_SPACES_DRIVE_SECTOR_SIZE_INVALID
#
# MessageText:
#
# The physical disk's sector size is not supported by the storage pool.
#
ERROR_SPACES_DRIVE_SECTOR_SIZE_INVALID = 0x80E70004

#
# MessageId: ERROR_SPACES_DRIVE_REDUNDANCY_INVALID
#
# MessageText:
#
# The requested redundancy is outside of the supported range of values.
#
ERROR_SPACES_DRIVE_REDUNDANCY_INVALID = 0x80E70006

#
# MessageId: ERROR_SPACES_NUMBER_OF_DATA_COPIES_INVALID
#
# MessageText:
#
# The number of data copies requested is outside of the supported range of values.
#
ERROR_SPACES_NUMBER_OF_DATA_COPIES_INVALID = 0x80E70007

#
# MessageId: ERROR_SPACES_PARITY_LAYOUT_INVALID
#
# MessageText:
#
# The value for ParityLayout is outside of the supported range of values.
#
ERROR_SPACES_PARITY_LAYOUT_INVALID = 0x80E70008

#
# MessageId: ERROR_SPACES_INTERLEAVE_LENGTH_INVALID
#
# MessageText:
#
# The value for interleave length is outside of the supported range of values.
#
ERROR_SPACES_INTERLEAVE_LENGTH_INVALID = 0x80E70009

#
# MessageId: ERROR_SPACES_NUMBER_OF_COLUMNS_INVALID
#
# MessageText:
#
# The number of columns specified is outside of the supported range of values.
#
ERROR_SPACES_NUMBER_OF_COLUMNS_INVALID = 0x80E7000A

#
# MessageId: ERROR_SPACES_NOT_ENOUGH_DRIVES
#
# MessageText:
#
# There were not enough physical disks to complete the requested operation.
#
ERROR_SPACES_NOT_ENOUGH_DRIVES = 0x80E7000B

#
# Volsnap errors
#
# Success
#
# MessageId: ERROR_VOLSNAP_BOOTFILE_NOT_VALID
#
# MessageText:
#
# The bootfile is too small to support persistent snapshots.
#
ERROR_VOLSNAP_BOOTFILE_NOT_VALID = 0x80820001

#
# Tiering errors
#
# Errors
#
# MessageId: ERROR_TIERING_NOT_SUPPORTED_ON_VOLUME
#
# MessageText:
#
# The specified volume does not support storage tiers.
#
ERROR_TIERING_NOT_SUPPORTED_ON_VOLUME = 0x80830001

#
# MessageId: ERROR_TIERING_VOLUME_DISMOUNT_IN_PROGRESS
#
# MessageText:
#
# The Storage Tiers Management service detected that the specified volume is in the process of being dismounted.
#
ERROR_TIERING_VOLUME_DISMOUNT_IN_PROGRESS = 0x80830002

#
# MessageId: ERROR_TIERING_STORAGE_TIER_NOT_FOUND
#
# MessageText:
#
# The specified storage tier could not be found on the volume. Confirm that the storage tier name is valid.
#
ERROR_TIERING_STORAGE_TIER_NOT_FOUND = 0x80830003

#
# MessageId: ERROR_TIERING_INVALID_FILE_ID
#
# MessageText:
#
# The file identifier specified is not valid on the volume.
#
ERROR_TIERING_INVALID_FILE_ID = 0x80830004

#
# MessageId: ERROR_TIERING_WRONG_CLUSTER_NODE
#
# MessageText:
#
# Storage tier operations must be called on the clustering node that owns the metadata volume.
#
ERROR_TIERING_WRONG_CLUSTER_NODE = 0x80830005

#
# MessageId: ERROR_TIERING_ALREADY_PROCESSING
#
# MessageText:
#
# The Storage Tiers Management service is already optimizing the storage tiers on the specified volume.
#
ERROR_TIERING_ALREADY_PROCESSING = 0x80830006

#
# MessageId: ERROR_TIERING_CANNOT_PIN_OBJECT
#
# MessageText:
#
# The requested object type cannot be assigned to a storage tier.
#
ERROR_TIERING_CANNOT_PIN_OBJECT = 0x80830007

#
# ===============================
# Facility Direct* Error Messages
# ===============================
#
#

#
# DXGI status (success) codes
#

#
# MessageId: DXGI_STATUS_OCCLUDED
#
# MessageText:
#
# The Present operation was invisible to the user.
#
DXGI_STATUS_OCCLUDED = 0x087A0001

#
# MessageId: DXGI_STATUS_CLIPPED
#
# MessageText:
#
# The Present operation was partially invisible to the user.
#
DXGI_STATUS_CLIPPED = 0x087A0002

#
# MessageId: DXGI_STATUS_NO_REDIRECTION
#
# MessageText:
#
# The driver is requesting that the DXGI runtime not use shared resources to communicate with the Desktop Window Manager.
#
DXGI_STATUS_NO_REDIRECTION = 0x087A0004

#
# MessageId: DXGI_STATUS_NO_DESKTOP_ACCESS
#
# MessageText:
#
# The Present operation was not visible because the Windows session has switched to another desktop (for example, ctrl-alt-del).
#
DXGI_STATUS_NO_DESKTOP_ACCESS = 0x087A0005

#
# MessageId: DXGI_STATUS_GRAPHICS_VIDPN_SOURCE_IN_USE
#
# MessageText:
#
# The Present operation was not visible because the target monitor was being used for some other purpose.
#
DXGI_STATUS_GRAPHICS_VIDPN_SOURCE_IN_USE = 0x087A0006

#
# MessageId: DXGI_STATUS_MODE_CHANGED
#
# MessageText:
#
# The Present operation was not visible because the display mode changed. DXGI will have re-attempted the presentation.
#
DXGI_STATUS_MODE_CHANGED = 0x087A0007

#
# MessageId: DXGI_STATUS_MODE_CHANGE_IN_PROGRESS
#
# MessageText:
#
# The Present operation was not visible because another Direct3D device was attempting to take fullscreen mode at the time.
#
DXGI_STATUS_MODE_CHANGE_IN_PROGRESS = 0x087A0008


#
# DXGI error codes
#

#
# MessageId: DXGI_ERROR_INVALID_CALL
#
# MessageText:
#
# The application made a call that is invalid. Either the parameters of the call or the state of some object was incorrect.
# Enable the D3D debug layer in order to see details via debug messages.
#
DXGI_ERROR_INVALID_CALL = 0x887A0001

#
# MessageId: DXGI_ERROR_NOT_FOUND
#
# MessageText:
#
# The object was not found. If calling IDXGIFactory::EnumAdaptes, there is no adapter with the specified ordinal.
#
DXGI_ERROR_NOT_FOUND = 0x887A0002

#
# MessageId: DXGI_ERROR_MORE_DATA
#
# MessageText:
#
# The caller did not supply a sufficiently large buffer.
#
DXGI_ERROR_MORE_DATA = 0x887A0003

#
# MessageId: DXGI_ERROR_UNSUPPORTED
#
# MessageText:
#
# The specified device interface or feature level is not supported on this system.
#
DXGI_ERROR_UNSUPPORTED = 0x887A0004

#
# MessageId: DXGI_ERROR_DEVICE_REMOVED
#
# MessageText:
#
# The GPU device instance has been suspended. Use GetDeviceRemovedReason to determine the appropriate action.
#
DXGI_ERROR_DEVICE_REMOVED = 0x887A0005

#
# MessageId: DXGI_ERROR_DEVICE_HUNG
#
# MessageText:
#
# The GPU will not respond to more commands, most likely because of an invalid command passed by the calling application.
#
DXGI_ERROR_DEVICE_HUNG = 0x887A0006

#
# MessageId: DXGI_ERROR_DEVICE_RESET
#
# MessageText:
#
# The GPU will not respond to more commands, most likely because some other application submitted invalid commands.
# The calling application should re-create the device and continue.
#
DXGI_ERROR_DEVICE_RESET = 0x887A0007

#
# MessageId: DXGI_ERROR_WAS_STILL_DRAWING
#
# MessageText:
#
# The GPU was busy at the moment when the call was made, and the call was neither executed nor scheduled.
#
DXGI_ERROR_WAS_STILL_DRAWING = 0x887A000A

#
# MessageId: DXGI_ERROR_FRAME_STATISTICS_DISJOINT
#
# MessageText:
#
# An event (such as power cycle) interrupted the gathering of presentation statistics. Any previous statistics should be
# considered invalid.
#
DXGI_ERROR_FRAME_STATISTICS_DISJOINT = 0x887A000B

#
# MessageId: DXGI_ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE
#
# MessageText:
#
# Fullscreen mode could not be achieved because the specified output was already in use.
#
DXGI_ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE = 0x887A000C

#
# MessageId: DXGI_ERROR_DRIVER_INTERNAL_ERROR
#
# MessageText:
#
# An internal issue prevented the driver from carrying out the specified operation. The driver's state is probably suspect,
# and the application should not continue.
#
DXGI_ERROR_DRIVER_INTERNAL_ERROR = 0x887A0020

#
# MessageId: DXGI_ERROR_NONEXCLUSIVE
#
# MessageText:
#
# A global counter resource was in use, and the specified counter cannot be used by this Direct3D device at this time.
#
DXGI_ERROR_NONEXCLUSIVE = 0x887A0021

#
# MessageId: DXGI_ERROR_NOT_CURRENTLY_AVAILABLE
#
# MessageText:
#
# A resource is not available at the time of the call, but may become available later.
#
DXGI_ERROR_NOT_CURRENTLY_AVAILABLE = 0x887A0022

#
# MessageId: DXGI_ERROR_REMOTE_CLIENT_DISCONNECTED
#
# MessageText:
#
# The application's remote device has been removed due to session disconnect or network disconnect.
# The application should call IDXGIFactory1::IsCurrent to find out when the remote device becomes available again.
#
DXGI_ERROR_REMOTE_CLIENT_DISCONNECTED = 0x887A0023

#
# MessageId: DXGI_ERROR_REMOTE_OUTOFMEMORY
#
# MessageText:
#
# The device has been removed during a remote session because the remote computer ran out of memory.
#
DXGI_ERROR_REMOTE_OUTOFMEMORY = 0x887A0024

#
# MessageId: DXGI_ERROR_ACCESS_LOST
#
# MessageText:
#
# The keyed mutex was abandoned.
#
DXGI_ERROR_ACCESS_LOST = 0x887A0026

#
# MessageId: DXGI_ERROR_WAIT_TIMEOUT
#
# MessageText:
#
# The timeout value has elapsed and the resource is not yet available.
#
DXGI_ERROR_WAIT_TIMEOUT = 0x887A0027

#
# MessageId: DXGI_ERROR_SESSION_DISCONNECTED
#
# MessageText:
#
# The output duplication has been turned off because the Windows session ended or was disconnected.
# This happens when a remote user disconnects, or when "switch user" is used locally.
#
DXGI_ERROR_SESSION_DISCONNECTED = 0x887A0028

#
# MessageId: DXGI_ERROR_RESTRICT_TO_OUTPUT_STALE
#
# MessageText:
#
# The DXGI outuput (monitor) to which the swapchain content was restricted, has been disconnected or changed.
#
DXGI_ERROR_RESTRICT_TO_OUTPUT_STALE = 0x887A0029

#
# MessageId: DXGI_ERROR_CANNOT_PROTECT_CONTENT
#
# MessageText:
#
# DXGI is unable to provide content protection on the swapchain. This is typically caused by an older driver,
# or by the application using a swapchain that is incompatible with content protection.
#
DXGI_ERROR_CANNOT_PROTECT_CONTENT = 0x887A002A

#
# MessageId: DXGI_ERROR_ACCESS_DENIED
#
# MessageText:
#
# The application is trying to use a resource to which it does not have the required access privileges.
# This is most commonly caused by writing to a shared resource with read-only access.
#
DXGI_ERROR_ACCESS_DENIED = 0x887A002B

#
# MessageId: DXGI_ERROR_NAME_ALREADY_EXISTS
#
# MessageText:
#
# The application is trying to create a shared handle using a name that is already associated with some other resource.
#
DXGI_ERROR_NAME_ALREADY_EXISTS = 0x887A002C

#
# MessageId: DXGI_ERROR_SDK_COMPONENT_MISSING
#
# MessageText:
#
# The application requested an operation that depends on an SDK component that is missing or mismatched.
#
DXGI_ERROR_SDK_COMPONENT_MISSING = 0x887A002D


#
# DXGI errors that are internal to the Desktop Window Manager
#

#
# MessageId: DXGI_STATUS_UNOCCLUDED
#
# MessageText:
#
# The swapchain has become unoccluded.
#
DXGI_STATUS_UNOCCLUDED = 0x087A0009

#
# MessageId: DXGI_STATUS_DDA_WAS_STILL_DRAWING
#
# MessageText:
#
# The adapter did not have access to the required resources to complete the Desktop Duplication Present() call, the Present() call needs to be made again
#
DXGI_STATUS_DDA_WAS_STILL_DRAWING = 0x087A000A

#
# MessageId: DXGI_ERROR_MODE_CHANGE_IN_PROGRESS
#
# MessageText:
#
# An on-going mode change prevented completion of the call. The call may succeed if attempted later.
#
DXGI_ERROR_MODE_CHANGE_IN_PROGRESS = 0x887A0025


#
# DXGI DDI
#

#
# MessageId: DXGI_DDI_ERR_WASSTILLDRAWING
#
# MessageText:
#
# The GPU was busy when the operation was requested.
#
DXGI_DDI_ERR_WASSTILLDRAWING = 0x887B0001

#
# MessageId: DXGI_DDI_ERR_UNSUPPORTED
#
# MessageText:
#
# The driver has rejected the creation of this resource.
#
DXGI_DDI_ERR_UNSUPPORTED = 0x887B0002

#
# MessageId: DXGI_DDI_ERR_NONEXCLUSIVE
#
# MessageText:
#
# The GPU counter was in use by another process or d3d device when application requested access to it.
#
DXGI_DDI_ERR_NONEXCLUSIVE = 0x887B0003


#
# Direct3D10
#

#
# MessageId: D3D10_ERROR_TOO_MANY_UNIQUE_STATE_OBJECTS
#
# MessageText:
#
# The application has exceeded the maximum number of unique state objects per Direct3D device.
# The limit is 4096 for feature levels up to 11.1.
#
D3D1 = 0

#
# MessageId: D3D10_ERROR_FILE_NOT_FOUND
#
# MessageText:
#
# The specified file was not found.
#
D3D1 = 0


#
# Direct3D11
#

#
# MessageId: D3D11_ERROR_TOO_MANY_UNIQUE_STATE_OBJECTS
#
# MessageText:
#
# The application has exceeded the maximum number of unique state objects per Direct3D device.
# The limit is 4096 for feature levels up to 11.1.
#
D3D1 = 1

#
# MessageId: D3D11_ERROR_FILE_NOT_FOUND
#
# MessageText:
#
# The specified file was not found.
#
D3D1 = 1

#
# MessageId: D3D11_ERROR_TOO_MANY_UNIQUE_VIEW_OBJECTS
#
# MessageText:
#
# The application has exceeded the maximum number of unique view objects per Direct3D device.
# The limit is 2^20 for feature levels up to 11.1.
#
D3D1 = 1

#
# MessageId: D3D11_ERROR_DEFERRED_CONTEXT_MAP_WITHOUT_INITIAL_DISCARD
#
# MessageText:
#
# The application's first call per command list to Map on a deferred context did not use D3D11_MAP_WRITE_DISCARD.
#
D3D1 = 1


#
# Direct2D
#

#
# MessageId: D2DERR_WRONG_STATE
#
# MessageText:
#
# The object was not in the correct state to process the method.
#
D = 2

#
# MessageId: D2DERR_NOT_INITIALIZED
#
# MessageText:
#
# The object has not yet been initialized.
#
D = 2

#
# MessageId: D2DERR_UNSUPPORTED_OPERATION
#
# MessageText:
#
# The requested operation is not supported.
#
D = 2

#
# MessageId: D2DERR_SCANNER_FAILED
#
# MessageText:
#
# The geometry scanner failed to process the data.
#
D = 2

#
# MessageId: D2DERR_SCREEN_ACCESS_DENIED
#
# MessageText:
#
# Direct2D could not access the screen.
#
D = 2

#
# MessageId: D2DERR_DISPLAY_STATE_INVALID
#
# MessageText:
#
# A valid display state could not be determined.
#
D = 2

#
# MessageId: D2DERR_ZERO_VECTOR
#
# MessageText:
#
# The supplied vector is zero.
#
D = 2

#
# MessageId: D2DERR_INTERNAL_ERROR
#
# MessageText:
#
# An internal error (Direct2D bug) occurred. On checked builds, we would assert. The application should close this instance of Direct2D and should consider restarting its process.
#
D = 2

#
# MessageId: D2DERR_DISPLAY_FORMAT_NOT_SUPPORTED
#
# MessageText:
#
# The display format Direct2D needs to render is not supported by the hardware device.
#
D = 2

#
# MessageId: D2DERR_INVALID_CALL
#
# MessageText:
#
# A call to this method is invalid.
#
D = 2

#
# MessageId: D2DERR_NO_HARDWARE_DEVICE
#
# MessageText:
#
# No hardware rendering device is available for this operation.
#
D = 2

#
# MessageId: D2DERR_RECREATE_TARGET
#
# MessageText:
#
# There has been a presentation error that may be recoverable. The caller needs to recreate, rerender the entire frame, and reattempt present.
#
D = 2

#
# MessageId: D2DERR_TOO_MANY_SHADER_ELEMENTS
#
# MessageText:
#
# Shader construction failed because it was too complex.
#
D = 2

#
# MessageId: D2DERR_SHADER_COMPILE_FAILED
#
# MessageText:
#
# Shader compilation failed.
#
D = 2

#
# MessageId: D2DERR_MAX_TEXTURE_SIZE_EXCEEDED
#
# MessageText:
#
# Requested DirectX surface size exceeded maximum texture size.
#
D = 2

#
# MessageId: D2DERR_UNSUPPORTED_VERSION
#
# MessageText:
#
# The requested Direct2D version is not supported.
#
D = 2

#
# MessageId: D2DERR_BAD_NUMBER
#
# MessageText:
#
# Invalid number.
#
D = 2

#
# MessageId: D2DERR_WRONG_FACTORY
#
# MessageText:
#
# Objects used together must be created from the same factory instance.
#
D = 2

#
# MessageId: D2DERR_LAYER_ALREADY_IN_USE
#
# MessageText:
#
# A layer resource can only be in use once at any point in time.
#
D = 2

#
# MessageId: D2DERR_POP_CALL_DID_NOT_MATCH_PUSH
#
# MessageText:
#
# The pop call did not match the corresponding push call.
#
D = 2

#
# MessageId: D2DERR_WRONG_RESOURCE_DOMAIN
#
# MessageText:
#
# The resource was realized on the wrong render target.
#
D = 2

#
# MessageId: D2DERR_PUSH_POP_UNBALANCED
#
# MessageText:
#
# The push and pop calls were unbalanced.
#
D = 2

#
# MessageId: D2DERR_RENDER_TARGET_HAS_LAYER_OR_CLIPRECT
#
# MessageText:
#
#
D = 2

#
# MessageId: D2DERR_INCOMPATIBLE_BRUSH_TYPES
#
#
#