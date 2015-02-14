#!usr/bin/env python
# -*- coding:utf-8-*-

__author__ = "yejc"

import socket
import time
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9999))

s.listen(5)

print "waiting for connecting..."

def tcplink(sock, addr):
	print "accepting new connecting..."
	sock.send("welcome!")
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == "exit" or not data:
			break
		sock.send("hello, %s"%data)
	sock.close()
	print "connecting %s:%s close..."%addr

while True:
	sock, addr = s.accept()
	tre = threading.Thread(target=tcplink, args=(sock, addr))
	tre.start()
