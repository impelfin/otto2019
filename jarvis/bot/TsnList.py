import pymysql

def TsnList_sql(Tcode, category) :
	con = pymysql.connect(host='localhost', user='testbot', password='1234', db='hello', charset='utf8', local_infile = 1)
	con.autocommit(True)

	curs = con.cursor()

	sql2=('insert into TsnList(Tcode, Category) values('
+ "\"" + Tcode + "\"" + ", " + "\"" + category + "\"" + ");")
	curs.execute(sql2)

	con.close()

if __name__ =="__main__":
	TsnList_sql("test","test")
