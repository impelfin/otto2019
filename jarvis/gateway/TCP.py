import socket
import threading
import sys
import time


HOST = "192.168.0.20"
PORT = 80
fcount = 1

def handler(conn,addr) :
	while 1:
		data = conn.recv(1024)
		reply = '\r'
		conn.sendall(reply)
		time.sleep(0.8)
		print data
while True:
	a=0
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print 'socket created'
		a=0
		s.bind((HOST, PORT))
	except socket.error:a=1
	if a==0: break
	time.sleep(0.5)
	print 'bind error'

s.listen(5)
while 1: 
	print 'socket awiting messages'
	(conn, addr) = s.accept()
	print 'Connected from : ', addr
	t = threading.Thread(target=handler, args=(conn,addr))
	t.start()

