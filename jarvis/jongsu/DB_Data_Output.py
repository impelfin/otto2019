import pymysql
import sys
from datetime import datetime, timedelta


def rec(argv) :
	con = pymysql.connect(host='localhost',user='dgbs',password='1234',db='TSN_Tooth1',charset='utf8',local_infile=1)

	con.autocommit(True)
	curs = con.cursor()

	sql2="select "+argv[0]+" from "+argv[1]+" where Date between '"+argv[2]+"' AND '"+argv[3]+"' into outfile \"/tmp/"+argv[4]+"\" fields terminated by '\t' lines terminated by '\n';" 
	curs.execute(sql2)
	print(sql2)

	
	con.close()

def rec1(argv) :
	con = pymysql.connect(host='localhost',user='dgbs',password='1234',db='TSN_Tooth1',charset='utf8',local_infile=1)

	con.autocommit(True)
	curs = con.cursor()

	sql2="select * from "+argv[0]+" into outfile \"/tmp/"+argv[4]+"\" fields terminated by '\t' lines terminated by '\n';" 
	curs.execute(sql2)
	print(sql2)

	
	con.close()
