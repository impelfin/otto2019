from bottle import route, run
from bottle import template
from bottle import *
import TsnList

@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='/home/workbench/static')

@route('/')
def mainpage():
	return template('/home/workbench/templates/mainpage.html') 

run(host='localhost', port=8080, degug=True)
