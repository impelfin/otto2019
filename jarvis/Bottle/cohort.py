import os
from bottle import run, template, get, post, request

import plotly.plotly as py
from plotly.graph_objs import *

import json

# grab username and key from config/data file
with open('data.json') as config_file:
    config_data = json.load(config_file)
username = config_data["user"]
key = config_data["key"]

py.sign_in(username, key)


@get('/plot')
def form():
    return template('template', title='JARVIS')


@post('/plot')
def submit():
    # grab data from form
    Y01 = request.forms.get('Y01')
    Y02 = request.forms.get('Y02')
    Y03 = request.forms.get('Y03')
    Y11 = request.forms.get('Y11')
    Y12 = request.forms.get('Y12')
    Y13 = request.forms.get('Y13')
    Y21 = request.forms.get('Y21')
    Y22 = request.forms.get('Y22')
    Y23 = request.forms.get('Y23')
    Y31 = request.forms.get('Y31')
    Y32 = request.forms.get('Y32')
    Y33 = request.forms.get('Y33')


    trace1 = Scatter(
        x=[1, 2, 3],
        y=[Y01, Y02, Y03]
    )
    trace2 = Scatter(
        x=[1, 2, 3],
        y=[Y11, Y12, Y13]
    )
    trace3 = Scatter(
        x=[1, 2, 3],
        y=[Y21, Y22, Y23]
    )

    data = Data([trace1, trace2, trace3])

    ###
    ###
    ###

    data1 = Data([
        Bar(
            x=[1, 2, 3],
            y=[Y01, Y02, Y03]
        )
    ])

    # make api call
    response = py.plot(data1, filename='basic-bar')


    ###
    ###
    ###

    # api call
    plot_url = py.plot(data, filename='basic-line')

    
    return template('template2', title='JARVIS', plot_url=str(plot_url), response=str(response))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
