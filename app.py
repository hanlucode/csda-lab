import dash
import dash_bootstrap_components as dbc
from lab1.movies import Recommender


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True

# Lab 1
rec = Recommender()
df = rec.get_sample_df()