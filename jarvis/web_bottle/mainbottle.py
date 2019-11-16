from bottle import route, run
import run_def
from bottle import template
from bottle import *
import os
import bottle
import random
from bokeh.models import (HoverTool, FactorRange, Plot, LinearAxis, Grid, Range1d)
from bokeh.models.glyphs import VBar
from bokeh.plotting import figure
from bokeh.charts import Bar
from bokeh.embed import components
from bokeh.models.sources import ColumnDataSource
import TsnList_dbInput
import TsnList_dbOutput


app = bottle.default_app()

TEMPLATE_STRING = """
<html>
<head>
<link href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.css" 
rel="stylesheet">
<link href="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.css" 
rel="stylesheet">
<title>Bar charts with Bottle and Bokeh</title>
</head>
<body>
<h1>This is {{ bars_count }} graph</h1>
{{ !the_div }}
<script src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.js"></script>
<script src="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.js"></script>
{{ !the_script }}
</body>
</html>
"""


@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='/root/workbench/static')

@route('/')
def mainpage():
	return template('/root/workbench/templates/mainpage.html') 


@route('/ViewingData')
def ViewingData():
	return template('/root/workbench/templates/viewingdata.html')

@route('/ViewingTsnList')
def ViewingTsnList():
	f2 = open("/tmp/tsnlistdata.txt", 'r')
	lines2 = f2.readlines()

	return bottle.template('/root/workbench/templates/viewingtsnlist.tpl',lines=lines2)

@post('/data_process/graph')
def graph_processing():

	start = request.forms.get('data_min')
	end = request.forms.get('data_max')	

	TsnList_dbOutput.act(start, end)    # data pull module

	f1 = open("/tmp/graphdata.txt", 'r')
	lines = f1.readlines()

	data = {"date":[], "count":[]}

	i = 0
	for line in lines:
		tmp = line
		tmp = tmp.split(',')
		data["date"].append(tmp[0])
		tmp[0] = "0"
		tmp = [int (j) for j in tmp]
		data["count"].append(tmp[1])	#int로 형 변환
		i += 1

	os.remove("/tmp/graphdata.txt")

	#def week_graph():
		#if end-start==0

	#def week_graph():
		#if end-start >0 && end-start<30

	#def month_graph():
		#if end-start >0month 

	hover = create_hover_tool()
	exstr = "OTTO2019 Test Graph Page"
	plot = create_bar_chart(data, exstr, "date", "count", hover)
	script, div = components(plot)
	return template(TEMPLATE_STRING, bars_count="days", the_div=div, the_script=script)

def create_hover_tool():
	return None

def create_bar_chart(data, title, x_name, y_name, hover_tool=None, width=1200,  height=300):

	source = ColumnDataSource(data)
	xdr = FactorRange(factors=data[x_name])
	ydr = Range1d(start=0,end=max(data[y_name])*1.5)

	tools=[]
	if hover_tool:
		tools = [hover_tool,]

	plot = figure(title=title, x_range=xdr, y_range=ydr, plot_width=width, plot_height=height, h_symmetry=False, v_symmetry=False, min_border=10, toolbar_location="above", tools=tools, responsive=True, outline_line_color="#666666")

	glyph = VBar(x=x_name, top=y_name, bottom=0, width=.8, fill_color="#6599ed")
	plot.add_glyph(source,glyph)

	xaxis = LinearAxis()
	yaxis = LinearAxis()

	plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
	plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))
	plot.toolbar.logo = None
	plot.min_border_top = 0
	plot.xgrid.grid_line_color = None
	plot.ygrid.grid_line_color = "#999999"
	plot.yaxis.axis_label = "Data Count"
	plot.ygrid.grid_line_alpha = 1
	plot.xaxis.axis_label = "Date"
	plot.xaxis.major_label_orientation = 1
	return plot
		

run(host=run_def.host, port=run_def.port, degug=True)
