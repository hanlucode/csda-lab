import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

# from comp.navbar import Navbar
# nav = Navbar()

from layouts import navbar

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

body = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Lab 3 Page',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash App for Lab3', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2],
                 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])


def App():
    layout = html.Div([
        navbar,
        body
    ])
    return layout


if __name__ == "__main__":
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
    app.layout = App()
    app.run_server()
