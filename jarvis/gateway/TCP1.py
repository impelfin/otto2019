import socket
import threading
import sys
import time
<<<<<<< HEAD
import sub1
import sub2
import sub3
import os
impott DB_Data_Output
import DB_Data_Input
=======

>>>>>>> a4ad404a842bd219e41d4873f14ab3c2c34abca3

HOST = "192.168.0.20"
PORT = 80
fcount = 1


def handler(conn,addr) :
<<<<<<< HEAD
	time1 = time.strptime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
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
=======
>>>>>>> a4ad404a842bd219e41d4873f14ab3c2c34abca3
	while 1:
		data = conn.recv(1024)
		reply = '\r'
<<<<<<< HEAD
		
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
			arg=["TSN_Info","TSN_Info"]
			DB_Data_Output.rec1(arg)		
			file_I = open("/tmp/TSN_Info","r")
			os.system('rm /tmp/TSN_Info')
			tsn[:-1]=""
			tsncategory=file_I.readlines()
			category=""
			for i in tsncategory:
				if tsn == i[0]:
					if i[1] == "Sleep": category="Sleep"
					elif i[1] == "Tooth": category="Tooth"
					elif i[1] == "Water": category="Water"
			str=["Datetime",category,time1,time.strftime('%Y-%m-%d',time.localtime(time.time())),"TSN_Data"]	
			DB_Data_Output.rec(str)
			Make_TSNData.MakeData(category)
			os.system(rm /tmp/TSN_Data.txt)
			str1=["TSN_data.txt",category]
			DB_Data_Input.send(str1)

		
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

=======
		conn.sendall(reply)
		time.sleep(0.8)
		print data
>>>>>>> a4ad404a842bd219e41d4873f14ab3c2c34abca3
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

