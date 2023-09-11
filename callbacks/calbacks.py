from typing import List
from dash import Dash, html, dcc

external_stylesheets = ['assets/style.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div(id='left_panel_div', children=[
        html.Div(id='left_top_div', children=[
            html.P('top left DIV'),
            html.Label('dcc.Dropdown'),
            dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
            html.Label('dcc.RadioItem'),
            dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
            html.Label('dcc.CheckList'),
            dcc.Checklist(['1', '2', '3']),
            dcc.Clipboard(),
            html.Label('dcc.Slider'),
            dcc.Slider(
                min=0,
                max=10,
                marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 10)},
                value=5,
            ),

        ]),
        html.Div(id='left_bottom_div', children=[html.P('bottom left DIV')]),
    ]),
    html.Div(id='right_panel_div', children=[
      html.Div(id='right_top_div', children=[html.P('top right DIV')]),
      html.Div(id='right_bottom_div', children=[html.P('bottom right DIV')]),
  ])
], )

if __name__ == '__main__':
  app.run_server()