# Average monthly arrival delay time over the year. Year range is from 2010 to 2020.

# Import required libraries and read the dataset
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

airline_data = pd.read_csv(r'C:\Users\krzys\Desktop\Python\Projekty\02-Airline Reporting\airline_data.csv')

# Layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Performance Dashboard', style={'textAlign':'center', 'color':'#503D36', 'font-size':40}),
                                html.Div(['Input year ', dcc.Input(id='input-year', value='2010', type='number',
                                style={'height':'50px', 'font-size':35}),],
                                style={'font-size':40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='bar-plot')),
                                ])

# Callback function
@app.callback(Output(component_id='bar-plot', component_property='figure'), 
                Input(component_id='input-year', component_property='value'))

def get_graph(entered_year):
    df = airline_data[airline_data['Year']==int(entered_year)]
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()