from bottle import *
import TsnList

@route('/')
def set_category():
	return template('/home/workbench/templates/set_category.html') 

@post('/data_process/category')
def category_processing():
	#web input or system input

	#Tcode = request.forms.get('Tcode_info')
	Tcode = "A004"
	if(Tcode == None or Tcode==""):
		return template('/home/workbench/templates/errorpage_tsn.html')
	

	category = request.forms.get('category_info')
	if(category == None or category==""):
		return template('/home/workbench/templates/errorpage_cate.html')
	TsnList.TsnList_sql(Tcode, category)
	return template('/home/workbench/templates/success_cate.html')

	

run(host='192.168.1.3', port=8080, degug=True)
