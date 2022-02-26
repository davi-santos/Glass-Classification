from turtle import width
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
                dbc.Card([
                        dbc.CardBody(html.P('Some image in here'))
                    ],
                )
            ],
            width=2
        ),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody(
                        html.H2('CLASSIFICADOR DE VIDROS DO KAGGLE',),
                        className='ml-5'
                    )
                ])
            ],
            width=10,
        ),
        ],
        #row parameters
        align='center',
        className='mt-3 ml-1 mb-2'    
    ),
    dbc.Row(
        [
            dbc.Col([
                    dbc.Card([
                            dbc.CardBody([
                                    dbc.DropdownMenu([
                                            dbc.DropdownMenuItem('Item 1', header=True),
                                            dbc.DropdownMenuItem('Item 2'),
                                            dbc.DropdownMenuItem('Item 3')
                                        ],
                                        label='Base de dados',
                                        color='success',
                                        className='ml-1',
                                    ),
                                    html.P('Some text in here', className='mt-2')
                                ]
                            ),
                        ]
                    ),
                ],
                width=5
            ),
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H3('Graphics'),
                                    dcc.Graph(id='first-image', figure={})
                                ]
                            )
                        ]
                    )
                ],
                align='center',
                width=7
            ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col([
                    html.H5('insight graphs'),
                    dcc.Graph(id='another-graph', figure={})
                ],
                width=4
            ),
            dbc.Col([
                    html.H5('graphs about models'),
                    dcc.Graph(id='graph-graph', figure={})
                ],
                width=4,
            ),
            dbc.Col([
                    html.H5('Get predictions'),
                    dcc.Graph(id='graph-233', figure={})
                ],
                width=4,
            ),
        ],
        className='mt-3'
    ),
    dbc.Row(

    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)