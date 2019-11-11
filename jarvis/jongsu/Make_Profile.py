from datetime import datetime,timedelta
import sys

f=open("profile.txt",'r')
f4=open("DB_Profile.txt",'w')

now=datetime.now()

point = 0
last = ''
for input in sys.argv:
	read=f.readline()
	data = read.split('\t')
	if data[0] == input:
		if input== 'Tooth' :
			f1=open("/tmp/Tooth_Data_r.txt",'r')
			TSN_data = f1.readlines()
		elif input == 'Sleep' : 
			f2=open("/tmp/Sleep_Data_r.txt",'r')
			TSN_data=f2.readlines()
		elif input == 'Water' : 
			f3=open("/tmp/Water_Data_r.txt",'r')
			TSN_data=f3.readlines()

		flag=0		
		for j in range(0,int(data[1])):
			i=j
			if flag==1 : i=j-1
			flag=0
			read=f.readline()
			read=read.strip('\n')
			line=read.split('\t')
			datetime_str=str(now.date())+line[0]
			time=datetime.strptime(datetime_str,'%Y-%m-%d%H:%M:%S')

			TSN_data_u = TSN_data[i].split('\t')
			if TSN_data_u[1] != line[5] : 
				flag=1
				continue
			time1=datetime.strptime(TSN_data_u[0],'%Y-%m-%d %H:%M:%S')
			if time1>time : 
				time2=time1-time
			else :	time2=time-time1

			time3=int(time2.seconds/3600)
			print(time3)
			if time3 < int(line[1])+1 and time3 >=0:point += int(line[2]) 
			else :
				time3-=int(line[1])
				if time3>int(line[2]) : time3=int(line[2])
				point+=int(line[2]) - time3
			print(point)

			usetime=int(line[3])
			if usetime-usetime/10<int(TSN_data_u[2]) and usetime+usetime/10>int(TSN_data_u[2]):
				point+=int(line[4])
			else :
				count = 0
				while True :
					if usetime-usetime/10<int(TSN_data_u[2]) and usetime+usetime/10>int(TSN_data_u[2]):
						break
					elif uestime<int(TSN_data_u[1]):
						TSN_data_u[1]=int(TSN_data_u[1])-usetime/10
						count+=1
					else  :
						TSN_data_u[1]=int(TSN_data_u[1])+usetime/10
						count+=1
				if count > 10 : count=10
				point+=int(line[4])-count
			print(point)
		if input == 'Tooth' : 
				f1.close()
				last += str(now.date())+'\tTooth\t'+str(point)+'\n'
		elif input == 'Sleep' : 
				f2.close()
				last += str(now.date())+'\tSleep\t'+str(point)+'\n'	
		elif input == 'Water' : 
				f3.close()
				last += str(now.date())+'\tWater\t'+str(point)+'\n'
f4.write(last)
f.close()
f4.close()

