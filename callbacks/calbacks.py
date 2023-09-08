from typing import List
from dash import Dash, html, dcc
main_div_style_css = {'display': 'block',
                      'border': '5px',
                      'background-color': 'blue',
                      'text-align': 'center'}

inner_div = {'display': 'inline',
             'border': '5px',
             'background-color': 'gray',
             'text-align': 'center',
             'width': '100px',
             'height': '100px'}

app = Dash(__name__)
app.layout = html.Div(children=[
    html.Div(children=[
        html.Div(id='left_top_div', style=inner_div, children=[html.P('left DIV')]),
        html.Div(id='left_bottom_div', style=inner_div, children=[html.P('right DIV')]),
    ]),
    html.Div(children=[
      html.Div(id='right_top_div', style=inner_div, children=[html.P('left DIV')]),
      html.Div(id='right_bottom_div', style=inner_div, children=[html.P('right DIV')]),
  ])
], style=main_div_style_css)

if __name__ == '__main__':
  app.run_server()