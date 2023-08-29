from typing import List
import dash
import dash_html_components as html
import dash_core_components as dcc


def create_content() -> List:
    """
    Функция создает список с компонентами страницы
    :return: component : list
    """
    content = []
    rangs = {'User1': 123,
             'User2': 13,
             'User3': 12, }

    for key, value in rangs.items():
        component = html.H1(f'{key} : {value}',
                            style={'fontSize': '40px',
                                   'color': 'blue'})

        content.append(component)
    return content


app = dash.Dash(__name__)
app.layout = html.Div(create_content())

if __name__ == '__main__':
  app.run_server()
