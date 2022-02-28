from turtle import width
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash_extensions import Lottie



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
                        Lottie(options=options_image, width="40%", height="40%", url=logo_image),
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
                    html.H4('Fazer Predições', className='card-title'),
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
                                    html.H3('Gráficos', style={'text-align':'center'}),
                                    dbc.RadioItems(
                                        options=[
                                            {"label": "Gráfico em Pizza", "value": 1},
                                            {"label": "Gráfico de Barras", "value": 2},
                                            {"label": "Mapa de Calor", "value": 3},
                                        ],
                                        value=1,
                                        id="graphic-option",
                                        inline=True,
                                        style={'text-align':'center'}
                                    ),
                                    dcc.Graph(id='first-image', figure={}),
                                    dbc.Card('Model Evaluation')
                             #   ]
                            #)
                    #    ]
                    #)
                ],
                className='justify-content-center',
                align='top',
                width={'size':7},
                style={'color':'#000000'}
            ),
        ]
    ),
],fluid=False)

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


#@app.callback(
#    Output('insight-graphs-image', 'figure'),
#    Input('insight-graphs-option', 'value')
#)
#def set_analysis_graphs(option):
#    
#    if option==1:
#        matrix_corr = df.drop('Type', axis=1).corr()
#        fig = px.imshow(matrix_corr)
#
#    return fig

if __name__ == '__main__':
    app.run_server(debug=True)