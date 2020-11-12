#! usr/bin/python

# Made by Snow cannon

import socket
import subprocess
import sys
from datetime import datetime

def banner(): 
	print """ *********************************
				Frozen Scanner | Port Scanner
			  ********************************* """


subprocess.call('clear', shell=True)

remoteServer	= rawinput("Enter a Remote host to scan: ")
remoteServerIP 	= socket.gethostbyname(remoteServer)

print "-" * 60
print " Please wait while frozen scanner scans the remote host:", + remoteServerIP
print "-" * 60 

t1 = datetime.now()

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "port {}: 	Open".format(port)
		sock.close()
		
except keyboardInterrupt: 
	print "You pressed Ctrl+C"
	sys.exit()
	
t2 = datetime.now()

total = t2 - t1

print 'Scanning Completed in: ', total
