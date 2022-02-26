from turtle import width
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_extensions import Lottie

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

text = "industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."

#Config lottie files
#lottie_file = 'https://assets8.lottiefiles.com/packages/lf20_GZxjzF.json'
lottie_file = 'https://assets5.lottiefiles.com/packages/lf20_mkppywz7.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
                Lottie(options=options, width="77%", height="77%", url=lottie_file),
            ],
            width={'size':2, 'offset':2}
        ),
        dbc.Col(
            #[
            #    dbc.Card([
            #        dbc.CardBody(
            #            
            #        )
            #    ])
            #],
            [html.H2('CLASSIFICADOR DE VIDROS DO KAGGLE',style={'text-align':'center'}),
            html.P('Por Davi Santos', style={'text-align':'center'})],
            className='ml-5',
            width=6,
        ),
        ],
        #row parameters
        align='center',
        className='mt-3 ml-1 mb-2 center', 
    ),
    dbc.Row(
        [
            dbc.Col([
                    dbc.Card([
                            dbc.CardBody([
                                    html.H5('Sobre a base de dados', className='card-title'),
                                    #dbc.DropdownMenu([
                                    #        dbc.DropdownMenuItem('Item 1', header=True),
                                    #        dbc.DropdownMenuItem('Item 2'),
                                    #        dbc.DropdownMenuItem('Item 3')
                                    #    ],
                                    #    label='Base de dados',
                                    #    color='success',
                                    #    className='ml-1',
                                    #),

                                    html.P(text, className='card-text'),
                                ]
                            ),
                        ],
                        color=''
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
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5('insight graphs'),
                            dcc.Graph(id='another-graph', figure={})
                        ]
                    )
                )
                ],
                width=4
            ),
            dbc.Col([
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5('graphs about models'),
                                dcc.Graph(id='graph-graph', figure={})
                            ]
                        )
                    )

                ],
                width=4,
            ),
            dbc.Col([
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5('Get predictions'),
                                dcc.Graph(id='graph-233', figure={})
                            ]
                        )
                    )
                ],
                width=4,
            ),
        ],
        className='mt-3 mb-3'
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)