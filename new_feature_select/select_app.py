"""

"""
from typing import List
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

def get_data_from_csv(filename:str):
    """

    :param filename:str имя файла.
    :return: датфрейм пандас.
    """
    #TODO проверку наличия файла
    data_rangs = pd.read_csv(filename)
    return data_rangs

app = dash.Dash(__name__)
color_list = ['red', 'blue', 'white']
app.layout = html.Div([
                        dcc.Dropdown(
                            id='color_dropdown',
                            options=[{'label': color, 'value': color} for color in color_list]),
                        html.Div(id='color_output',)
])
"""
Input - указывается элемент который будет служить вводом для 
        функции обратного вывода.
        Input(component_id='color_dropdown', component_property='value')
        
Output - указывается элемент который будет изменяться
        Output(component_id='color_output', component_property='children')    
"""
@app.callback(Output('color_output', 'children'),
                     Input('color_dropdown', 'value'))
def display_selected_color(color):
    """

    :param color:
    :return:
    """
    if color is None:
        color = 'nothing'
    return [html.H3('You selected '), f'{color}']

if __name__ == '__main__':
    print(get_data_from_csv('data/rangs.csv')['Unnamed: 2'])
    #app.run_server()
