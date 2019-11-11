import pymysql

def send_sql(str) :
	con = pymysql.connect(host='localhost',user='dgbs',password='1234',db='TSN_Tooth1',charset='utf8',local_infile=1)

	con.autocommit(True)
	curs = con.cursor()

	sql2="load data local infile '"+str[0]+"' into table "+str[1]+";"
	curs.execute(sql2)

	con.close()

