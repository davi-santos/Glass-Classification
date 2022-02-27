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
    dbc.Row([
        dbc.Col([
                Lottie(options=options_image, url=logo_image),
                #Lottie(options=options_image, width="97%", height="97%", url=logo_image),
            ],
            width={'size':2},
            align='center',
        ),
        dbc.Col(
            #[
            #    dbc.Card([
            #        dbc.CardBody(
            #            
            #        )
            #    ])
            #],
            [
            html.H1('CLASSIFICADOR DE VIDROS DO KAGGLE',style={'text-align':'center'}),
            html.P('Por Davi Santos', style={'text-align':'center'})],
            className='',
            width=8,
        ),
        ],
        #row parameters
        align='center',
        className='mt-3 mb-2 center', 
    ),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    html.H5('Base de Dados', className='card-title', style={'text-align':'center'}),
                ),
                
                #dbc.CardBody([
                html.P('Sobre a Base de Dados:', className='ml-5',style={'text-align':'center'}),
                html.H3('214 amostras', className='ml-5', style={'text-align':'center', 'text-color':'#379aa3'}, ),
                html.H3('9 atributos', className='ml-5', style={'text-align':'center'}),

                html.Div([
                dbc.Button(
                    "Ver Atributos",
                    color="success",
                        id="left",
                        className="me-1",
                        n_clicks=0,
                    ),
                    
                dbc.Button(
                        "Ver Tipos de Vidro",
                        color="info",
                        id="right",
                        className="me-1",
                        n_clicks=0,
                ),

            dbc.Button("Ver todos os dados", color="primary", outline=True,id="both", n_clicks=0),
            
            ],
            className='d-grid gap-2 d-md-flex justify-content-md-center mb-2'
            ),
                

                ],
                
            ),
            


                    

                    dbc.Collapse(
                    dbc.Card("This is the left card!", body=True),
                                id="left-collapse",
                                is_open=False,
                ),

                dbc.Collapse(
                    dbc.Card("This is the right card!", body=True),
                        id="right-collapse",
                        is_open=False,
                ),


                    dbc.Card([
                        dbc.CardHeader(
                            html.H5('Achados', className='card-title', style={'text-align':'center'})
                        ),
                        dbc.CardBody(
                            html.P('Oi')
                        )

                    ]),
                    dbc.Card([
                        dbc.CardHeader(
                            html.H5('Predições', className='card-title', style={'text-align':'center'})
                        ),
                        dbc.CardBody(
                            html.P('Oi')
                        )

                    ])
                ],
                align='top',
                width=5,
                className='mt-3'
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