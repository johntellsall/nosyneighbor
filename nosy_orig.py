# https://stackoverflow.com/questions/42237761/how-to-call-linux-syscall-process-vm-readv-within-python
import ctypes
import errno
import sys


class iovec(ctypes.Structure):
    _fields_ = [
	    ("iov_base", ctypes.c_void_p),
	    ("iov_len", ctypes.c_size_t)]

proc_pid = int(sys.argv[1])
assert sys.argv[2].startswith('0x')
proc_addr = int(sys.argv[2], 16)

local = (iovec*2)()             #create local iovec array
remote =  (iovec*1)()[0]        #create remote iovec
buf1 = (ctypes.c_char*10)()
buf2 = (ctypes.c_char*10)()

local[0].iov_base = ctypes.cast(ctypes.byref(buf1), ctypes.c_void_p)
local[0].iov_len = 10
local[1].iov_base = ctypes.cast(ctypes.byref(buf2), ctypes.c_void_p)
local[1].iov_len = 10
remote.iov_base = ctypes.c_void_p(proc_addr)
remote.iov_len = 20 # XXXXX


libc = ctypes.CDLL("libc.so.6", use_errno=True)
vm_readv = libc.process_vm_readv

vm_readv.argtypes = [
	ctypes.c_int, ctypes.POINTER(iovec), 
	ctypes.c_ulong, ctypes.POINTER(iovec), 
	ctypes.c_ulong, ctypes.c_ulong]

nread = vm_readv(proc_pid,local,2,remote,1,0)

if nread != -1:
    bytes = "[+] "
    print("[+] received %s bytes" % (nread))
    for i in buf1: bytes += hex(ord(i)) + " "
    for i in buf2: bytes += hex(ord(i)) + " "
    print(bytes)
else:
	# import ipdb ; ipdb.set_trace()
	errnum = ctypes.get_errno()
	errname = errno.errorcode[errnum]
	print("read error: {errname}({errnum})".format(**locals()))


