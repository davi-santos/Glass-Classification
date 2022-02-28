from turtle import width
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash_extensions import Lottie
import joblib

text = "industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."

#Reading dataframe
df = pd.read_csv('./data/glass.csv')

#Config logo picture
logo_image = 'https://assets5.lottiefiles.com/packages/lf20_mkppywz7.json'
options_image = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

app.layout = dbc.Container([
    # dbc.Row([
    #     dbc.Col([
    #             Lottie(options=options_image, url=logo_image),
    #             #Lottie(options=options_image, width="97%", height="97%", url=logo_image),
    #         ],
    #         width={'size':2},
    #         align='center',
    #     ),
    #     dbc.Col(
    #         #[
    #         #    dbc.Card([
    #         #        dbc.CardBody(
    #         #            
    #         #        )
    #         #    ])
    #         #],
    #         [
    #         html.H1('CLASSIFICADOR DE VIDROS DO KAGGLE',style={'text-align':'center'}),
    #         html.P('Por Davi Santos', style={'text-align':'center'})],
    #         className='',
    #         width=8,
    #     ),
    #     ],
    #     #row parameters
    #     align='center',
    #     className='mt-3 mb-2 center', 
    # ),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.Div([
                        html.H1('Classificador de Vidros',style={'text-align':'center'}),
                        Lottie(options=options_image, width="30%", height="30%", url=logo_image),
                    ],
                    className='border-0'
                )
                ]),
            ],
            className=''
            ),
            dbc.Card([
                dbc.CardHeader(
                    html.H4('Sobre a Base de Dados', className='card-title'),
                    className='bg-dark text-center text-light'
                ),

                dbc.CardBody([
                    html.H3('214 amostras', className='ml-5 text-center'),
                    html.H3('9 atributos', className='ml-5 text-center'),

                    html.Div([
                        dbc.Button("Ver Atributos",color="secondary", id="left", outline=True,className="me-1", n_clicks=0,),  
                        dbc.Button("Ver Tipos de Vidro",id="right",color="secondary", outline=True,className="me-1",n_clicks=0,),
                        dbc.Button("Ver todos os dados", color="secondary",outline=True, id="both", n_clicks=0),
                        ],
                        className='d-grid gap-2 d-md-flex justify-content-md-center mb-2'
                    )],
                    className='bg-light'
                ),
            ]),
            
            dbc.Collapse(
                dbc.Card(
                    [
                        html.H5('Atributos:', className='font-weight-bold'),
                        html.Ul([
                            html.Li('RI - Índice de Refração;'),
                            html.Li('Na - Sódio;'),
                            html.Li('Mg - Magnésio;'),
                            html.Li('Al - Alumínio;'),
                            html.Li('Si - Silício;'),
                            html.Li('K - Potássio;'),
                            html.Li('Ca - Cálcio;'),
                            html.Li('Ba - Bário;'),
                            html.Li('Fe - Ferro.'),
                        ],
                        className='ml-5 text-justify')
                    ], 
                    body=True,
                    className='bg-light'
                ),
                id="left-collapse",
                is_open=False,
                className='bg-light'
            ),

            dbc.Collapse(
                dbc.Card([
                        html.H5('Tipos de Vidro:', className='font-weight-bold'),
                        html.Ul([
                            html.Li('Tipo 1 - Construção de Janela Flutuante Processado;'),
                            html.Li('Tipo 2 - Construção de Janela Não-flutuante processado;'),
                            html.Li('Tipo 3 - Janela de Veículo Flutuante Processado;'),
                            html.Li('Tipo 4 - Janela de Veículo Não-flutuante processado'),
                            html.Li('Tipo 5 - Vidros para recipientes'),
                            html.Li('Tipo 6 - Vidro de Louças;'),
                            html.Li('Tipo 7 - Vidro para Faróis'),
                        ],
                        className='ml-5 text-justify')                    
                ], body=True, className='bg-light',),
                    id="right-collapse",
                    is_open=False,
            ),
            
            dbc.Card([
                dbc.CardHeader(
                    html.H4('Achados', className='card-title', style={'text-align':'center','color':'#FFFFFF'}),
                    className='bg-dark'
                ),
                dbc.CardBody(html.P('Oi')                        )
            ]),
            
            dbc.Card([
                dbc.CardHeader(
                    html.H4('Avaliação do Modelo', className='card-title'),
                    className='text-center text-light bg-dark'
                ),
                
                dbc.CardBody(
                    html.P('Oi')
                )
            ])
            ],
            align='top',
            width=5,
            className='mt-3',
            ),
            dbc.Col(
                [
                    #dbc.Card(
                    #    [
                            #dbc.CardBody(
                              #  [
                                    dbc.Card(
                                        dbc.CardHeader([
                                           html.H4('Opções Gráficas:', className=''),
                                            dbc.RadioItems(
                                                options=[
                                                    {"label": "Gráfico em Pizza", "value": 1},
                                                    {"label": "Gráfico de Barras", "value": 2},
                                                    {"label": "Mapa de Calor", "value": 3},
                                                    {"label": "Importância de Atributos do Modelo", "value": 4},
                                                ],
                                                value=1,
                                                id="graphic-option",
                                                inline=True,
                                            ),
                                        ],
                                        className='bg-dark text-light'
                                        )
                                    ),
                                    dcc.Graph(id='first-image', figure={}),
                                    dbc.Card([
                                        dbc.CardHeader([
                                            html.H4('Fazer Predições:'),
                                        ], className='bg-dark text-light'),
                                        dbc.CardBody([
                                          dbc.Row([
                                              dbc.Col([
                                                   dbc.Label("Índice de Refração", html_for="slider"),
                                                    dcc.Slider(id="RI", min=1.510, max=1.533, step=0.006, value=1.516),
                                              ], width=4),
                                              dbc.Col([
                                                   dbc.Label("Sódio", html_for="slider"),
                                                    dcc.Slider(id="Na", min=10.7, max=17.4, step=1.4, value=12.1),
                                              ], width=4),
                                              dbc.Col([
                                                   dbc.Label("Magnésio", html_for="slider"),
                                                    dcc.Slider(id="Mg", min=0, max=4.5, step=0.75, value=0.75),
                                              ], width=4)
                                          ], className='text-center'),
                                          dbc.Row([
                                              dbc.Col([
                                                   dbc.Label("Alumínio", html_for="slider"),
                                                    dcc.Slider(id="Al", min=0, max=4, step=0.7, value=0.7),
                                              ], width=4),
                                              dbc.Col([
                                                   dbc.Label("Silício", html_for="slider"),
                                                    dcc.Slider(id="Si", min=68, max=76, step=1, value=69),
                                              ], width=4),
                                              dbc.Col([
                                                   dbc.Label("Potássio", html_for="slider"),
                                                    dcc.Slider(id="K", min=0, max=6.5, step=1.25, value=1.25),
                                              ], width=4)
                                          ], className='text-center'),
                                          dbc.Row([
                                              dbc.Col([
                                                dbc.Label("Cálcio", html_for="slider"),
                                                dcc.Slider(id="Ca", min=5.4, max=16.2, step=2, value=7.4),
                                              ], width=4),
                                              dbc.Col([
                                                   dbc.Label("Bário", html_for="slider"),
                                                    dcc.Slider(id="Ba", min=0, max=3.2, step=0.8, value=0.8),
                                              ], width=4),
                                              dbc.Col([
                                                   dbc.Label("Ferro", html_for="slider"),
                                                    dcc.Slider(id="Fe", min=0, max=0.6, step=0.1, value=0.1),
                                              ], width=4),
                                          ], className='text-center', justify='center'),
                                            dbc.Row([
                                                dbc.Col([
                                                    dbc.Button("Fazer Predição", color="secondary", outline=True)
                                                ], width=3),
                                                dbc.Col([
                                                    dbc.Card([
                                                        html.H4('Resultado: ', id='result')
                                                    ],
                                                    className='bg-dark text-light text-center font-weight-lighter',
                                                    ),
                                                ], width=4),
                                            ], justify='center', align='center', className='mt-4')
                                        ])
                                    ]
                                    ),  
                             #   ]
                            #)
                    #    ]
                    #)
                ],
                className='justify-content-center mt-3',
                align='top',
                width={'size':7},
                style={'color':'#000000'}
            ),
        ]
    ),
],fluid=True)

@app.callback(
    Output('first-image', 'figure'),
    Input('graphic-option', 'value')
)
def image_top(option):
    
    fig = {}
    if option==1:
        fig = px.pie(df, values='Type',names='Type', title='Categorias de Vidro')
    elif option==2:
        df_auxiliar = df['Type'].value_counts()
        fig = px.bar(df_auxiliar, y='Type')
    elif option==3:
        matrix_corr = df.drop('Type', axis=1).corr()
        fig = px.imshow(matrix_corr)
    elif option==4:
        dt = joblib.load('./models/DecisionTree.joblib')
        df_decisionTree = pd.Series(dt.feature_importances_, index=df.columns.values[0:-1])
        fig = px.bar(df_decisionTree)

    return fig

@app.callback(
    Output("left-collapse", "is_open"),
    [Input("left", "n_clicks"), Input("both", "n_clicks")],
    [State("left-collapse", "is_open")],
)
def toggle_left(n_left, n_both, is_open):
    if n_left or n_both:
        return not is_open
    return is_open


@app.callback(
    Output("right-collapse", "is_open"),
    [Input("right", "n_clicks"), Input("both", "n_clicks")],
    [State("right-collapse", "is_open")],
)
def toggle_left(n_right, n_both, is_open):
    if n_right or n_both:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)