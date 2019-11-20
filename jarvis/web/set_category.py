from bottle import *
import run_def
import TsnList_dbInput

@route('/')
def set_category():
	return template('/root/workbench/templates/set_category.html') 

@post('/data_process/category')
def category_processing():
	#web input or system input

	#Tcode = request.forms.get('Tcode_info') # Tcode process
	Tcode = "A004"
	if(Tcode == None or Tcode==""):
		return template('/root/workbench/templates/errorpage_tsn.html')
	

	category = request.forms.get('category_info')
	if(category == None or category==""):
		return template('/root/workbench/templates/errorpage_cate.html')
	TsnList_dbInput.act(Tcode, category)
	return template('/root/workbench/templates/success_cate.html')

	

run(host=run_def.host, port=run_def.port, degug=True)
