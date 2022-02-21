from turtle import width
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

app.layout = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(
            [
                html.H1('Classificação de Vidros', style={'text-align':'center'}),
                html.P('Posso escrever algo como (Disponível no Kaggle)', style={'text-align':'center'})
            ],
            width={'size':6, 'offset':3},
        )],
        #align='center',
        justify='center'
    ),

    dbc.Row(children=[
        dbc.Col([
                html.H3('Coluna 1'),
                html.P('Aqui vou colocar conteúdo sobre a base de dados')
            ], 
            md=6
        ),
        dbc.Col([
                html.H3('Coluna 2')
            ], 
            md=6
        ),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)