from datetime import datetime
import DB_Data_Output
import time
import os
f=open("/tmp/TSN_Data.txt",'r')
f1=open("TSN_data.txt",'w')
def MakeData(str):
	if str = "Tooth" :
		data = [[0]*300 for i in range(9)]
		i=0
		last_read='0'
		now=datetime.now()
		
		
		f2=open("/tmp/TSN_Data_r.txt",'r')

		while True:
			read=f2.readline()
			if not read:
				break
			last_read=read
			
		count =int(last_read)
		lines = f.readlines()
		for line in lines:
			data[i]=line.split(',')
			data[i][1]=datetime.strptime(data[i][1].strip(),'%Y-%m-%d-%H-%M-%S')
			i+=1

		time=(data[i-1][1]-data[0][1]).seconds
		last=str(data[0][1])+'\t'+str(count+1)+'\t'+str(time)
		print(last)
		f1.write(last)
		f2.close()
f.close()
f1.close()

