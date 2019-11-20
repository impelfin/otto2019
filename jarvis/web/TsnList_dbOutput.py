import pymysql

def act(start, end) :
	con = pymysql.connect(host='localhost', user='testbot', password='1234', db='hello', charset='utf8', local_infile = 1)
	con.autocommit(True)

	curs = con.cursor()

	sql2=("select * from User_profile where Date(date) between '" + start + "' AND '" + end + "' into outfile \"/tmp/graphdata.txt\" fields terminated by ',' lines terminated by '\n';")
	curs.execute(sql2)

	con.close()




def act2(tablename):
	con = pymysql.connect(host='localhost', user='testbot', password='1234', db='hello', charset='utf8', local_infile = 1)
	con.autocommit(True)

	curs = con.cursor()

	sql1=("select * from " + tablename + " into outfile \"/tmp/tsnlist.txt\" fields terminated by ',' lines terminated by '\n';")

	curs.execute(sql1)

	con.close()
if __name__ =="__main__":
	act2("2019-11-11")
