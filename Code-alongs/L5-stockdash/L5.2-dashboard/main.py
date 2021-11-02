import pandas as pd
from dash import dcc, html
import dash


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stocks viewer"),
    html.H2("This is a cool app")

])

if __name__ == "__main__":
    app.run(debug=True)