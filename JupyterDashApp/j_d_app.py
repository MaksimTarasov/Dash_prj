from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html

app = JupyterDash(__name__)

if __name__ == '__main__':
    app.run_server(mode='inline')
