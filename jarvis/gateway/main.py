import pymysql
import sub

#pymysql.install_as_MySQLdb()

def main_sql():
	con = pymysql.connect(host='localhost', user='testbot', password='1234', db='hello', charset='utf8')

	curs = con.cursor(pymysql.cursors.DictCursor)

	sql=open("test.sql").read()
	curs.execute(sql)

	curs.fetchall()
	con.close()
	
	sub.sub_sql()


