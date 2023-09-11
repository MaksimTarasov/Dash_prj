from typing import List
from dash import Dash, html, dcc

# left_panel_div = {
#     'position': 'absolute',
#     'background-color': 'green',
#     'width': '50%',
#     'height': '50%',
#     'left': '0px',
#     'top': '0px'
# }
# right_panel_div = {
#     'position': 'absolute',
#     'background-color': 'blue',
#     'width': '50%',
#     'height': '50%',
#     'left': '50%',
#     'top': '0px'
# }
# inner_div = {
#     'position': 'relative',
#     'background-color': 'gray',
#     'width': '50%',
#     'height': '50%',
# }
external_stylesheets = ['assets/style.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div(id='left_panel_div', children=[
        html.Div(id='left_top_div', children=[html.P('left DIV')]),
        html.Div(id='left_bottom_div', children=[html.P('right DIV')]),
    ]),
    html.Div(id='right_panel_div', children=[
      html.Div(id='right_top_div', children=[html.P('left DIV')]),
      html.Div(id='right_bottom_div', children=[html.P('right DIV')]),
  ])
], )

if __name__ == '__main__':
  app.run_server()