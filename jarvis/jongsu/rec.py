import pymysql
from datetime import datetime, timedelta


def rec_sql() :
	con = pymysql.connect(host='localhost',user='dgbs',password='1234',db='TSN_Tooth1',charset='utf8',local_infile=1)

	con.autocommit(True)
	curs = con.cursor()

	sql2="select Count from tooth where Date > curdate() into outfile \"/tmp/TSN_data_r.txt\" fields terminated by '' lines terminated by '\n';" 
	curs.execute(sql2)
	print(sql2)

	
	con.close()

if __name__=="__main__":
	rec_sql()
