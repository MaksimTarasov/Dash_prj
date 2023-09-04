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

def drop_down_list(data_rangs) -> List:
    user_list = data_rangs['Unnamed: 2'].tolist()[3:]
    return user_list



data_rangs = get_data_from_csv('data/rangs.csv')
user_list = drop_down_list(data_rangs)

app = dash.Dash(__name__)
app.layout = html.Div([
                        dcc.Dropdown(
                            id='color_dropdown',
                            options=[{'label': user, 'value': user} for user in user_list]),
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
def display_selected_color(user):
    """

    :param user:
    :return:
    """
    if user is None:
        user = 'nothing'
    answer = data_rangs[data_rangs["Unnamed: 2"]==user]
    return [html.H3('You selected '), f'{answer.values[0][2]}',
                                      f'{answer.values[0][3]}',
                                      f'{answer.values[0][5]}'

            ]

if __name__ == '__main__':
    app.run_server()
