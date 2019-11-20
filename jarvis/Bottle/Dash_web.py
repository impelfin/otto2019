import dash
import dash_html_components as html
import dash_core_components as dcc
from random import *
import numpy

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
t = [numpy.random.randint(0,100) for r in range(24)]#24시간
w = [numpy.random.randint(0,100) for r in range(7)]#7일
m = [numpy.random.randint(0,100) for r in range(31)]#31일
y = [numpy.random.randint(0,100) for r in range(12)]#365일// 12달?

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Today', 'value': 'Today'},
            {'label': 'Weekly', 'value': 'Weekly'},
            {'label': 'Monthly', 'value': 'Monthly'},
            {'label': 'Yearly', 'value': 'Yearly'}
        ],
        value='Today'
    ),
    dcc.Graph(
        id='graph',
        config={
            'showSendToCloud': True,
            'plotlyServerURL': 'https://plot.ly'
        }
    )
    
])

@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    y_array_dict = {
        'Today': t,
        'Weekly': w,
        'Monthly': m,
        'Yearly': y
    }

    return {
        'data': [{
            'type': 'bar',
            'y': y_array_dict[value]
            
        }],
        'layout': {
            'title': value
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
