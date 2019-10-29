import pymysql

def sub_sql() :
	con = pymysql.connect(host='localhost', user='testbot', password='1234', db='hello', charset='utf8', local_infile = 1)
	con.autocommit(True)

	curs = con.cursor()

	sql2=open("test2.sql").read()
	curs.execute(sql2)

	con.close()

if __name__ =="__main__":
	sub_sql()
