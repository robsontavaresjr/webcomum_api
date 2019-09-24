# -*- coding: utf-8 -*-
import dash
import logging
import os
import pandas as pd
import numpy as np
import datetime as dt
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_auth
import plotly.graph_objs as go
from dash.dependencies import Input, Output


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1(children='Hello, Maria'),
    html.H2(children='Esse é o seu dashboard')])

if __name__ == '__main__':
    app.run_server(debug=True)
