import pymysql

def send_sql() :
	con = pymysql.connect(host='localhost',user='dgbs',password='1234',db='TSN_Tooth1',charset='utf8',local_infile=1)

	con.autocommit(True)
	curs = con.cursor()

	sql2=open("send.sql").read()
	curs.execute(sql2)

	con.close()

if __name__=="__main__":
	send_sql()
