# https://stackoverflow.com/questions/42237761/how-to-call-linux-syscall-process-vm-readv-within-python
import ctypes # from ctypes import *

class iovec(ctypes.Structure):
    _fields_ = [("iov_base", ctypes.c_void_p),("iov_len", ctypes.c_size_t)]

local = (iovec*2)()             #create local iovec array
remote =  (iovec*1)()[0]        #create remote iovec
buf1 = (ctypes.c_char*10)()
buf2 = (ctypes.c_char*10)()
pid = 25117

local[0].iov_base = ctypes.cast(ctypes.byref(buf1),ctypes.c_void_p)
local[0].iov_len = 10
local[1].iov_base = ctypes.cast(ctypes.byref(buf2),ctypes.c_void_p)
local[1].iov_len = 10
remote.iov_base = ctypes.c_void_p(0x800005a9)      #pass valid readable address
remote.iov_len = 20


libc = ctypes.CDLL("libc.so.6")
vm = libc.process_vm_readv

vm.argtypes = [
	ctypes.c_int, ctypes.POINTER(iovec), 
	ctypes.c_ulong, ctypes.POINTER(iovec), 
	ctypes.c_ulong, ctypes.c_ulong]

nread = vm(pid,local,2,remote,1,0)

if nread != -1:
    bytes = "[+] "
    print "[+] received %s bytes" % (nread)
    for i in buf1: bytes += hex(ord(i)) + " "
    for i in buf2: bytes += hex(ord(i)) + " "
    print bytes 

