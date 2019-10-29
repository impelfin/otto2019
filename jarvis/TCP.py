import socket
import threading
import sys
import time
import sub1
import sub2
import sub3


HOST = "192.168.0.7"
PORT = 80
fcount = 1

def handler(conn,addr) :
	global fcount
	b=0
	if fcount==3:
		key = fcount
		f3 = open("/usr/local/mysql/bin/mysqltest3.txt", 'w')
		fcount = 1
	if fcount==2:
		key = fcount
		f2 = open("/usr/local/mysql/bin/mysqltest2.txt", 'w')
		fcount +=1
	if fcount==1:
		key = fcount
		f1 = open("/usr/local/mysql/bin/mysqltest1.txt", 'w')
		fcount +=1
	while 1:
		time.sleep(0.1)
		if b==0:
			tsn = conn.recv(1024)
			tsn = tsn[:-1] + "\t"
			reply = '\r'
			conn.sendall(reply)
			b +=1
			time.sleep(0.1)
		data = conn.recv(1024)
		reply = '\r'
		if data == "Stop\r" :
			conn.close()
			if key ==1:
				sub1.sub1_sql()
				f1.close()
			if key ==2:
				sub2.sub2_sql()
				f2.close()
			if key==3:
				sub3.sub3_sql()
				f3.close()
			print 'disconnected from : ', addr
			break
		else:
			data = data[:-1] + "\n"
			data = tsn + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))+ '\t'  + data
			print data
			if key ==1:
				f1.write(data)
			if key ==2:
				f2.write(data)
			if key ==3:
				f3.write(data)
			conn.sendall(reply)

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

