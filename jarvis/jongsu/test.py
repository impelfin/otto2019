from datetime import datetime
f=open("text.txt",'r')
f1=open("TSN_data.txt",'w')
f2=open("/tmp/TSN_data_r.txt",'r')

data = [[0]*100 for i in range(9)]
i=0
last_read='0'

while True:
	read=f2.readline()
	if not read:
#		last_read='0'
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
f.close()
f1.close()
f2.close()

