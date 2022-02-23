from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])


df = pd.read_csv('./data/glass.csv')
#Fist figure
fig = px.pie(df, names='Type', title='Tipos de Vidro')

fig2 = px.scatter(df, x='Si', y='RI', trendline="ols")


app.layout = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(
            [
                html.H1(
                        'Classificação de Vidros', 
                        style={'text-align':'center'}
                    ),
                html.P(
                        'Posso escrever algo como (Disponível no Kaggle)', 
                        style={'text-align':'center'}
                    )
            ],
            width={'size':6, 'offset':3},
        )],
        #align='center',
        #justify='center'
    ),

    dbc.Row(children=[
        dbc.Col([
                html.H3('Projeto'),
                html.P('Esta é uma base de dados obtida no Kaggle. A base \
                    consiste em dados sobre 7 tipos de vidro, sendo estes:'),
               dbc.ListGroupItem("Tipo 1: construção de janelas flutuante processado"),
               dbc.ListGroupItem("Tipo 2: building_windows_non_float_processed "),
               dbc.ListGroupItem("Tipo 3: vehicle_windows_float_processed"),
               dbc.ListGroupItem("Tipo 4: vehicle_windows_non_float_processed"),
               dbc.ListGroupItem("Tipo 5: containers "),
               dbc.ListGroupItem("Tipo 6: tableware"),
               dbc.ListGroupItem("Tipo 7: headlamps"),
            ], 
        ),
        dbc.Col([
                dcc.Graph(
                    id='something',
                    figure=fig
                )
            ], 
        ),
    ]),

    dbc.Row(children=[
        dbc.Col([
            html.H4('Blá blá bla')            
            
        ]),

        dbc.Col([
            dcc.Graph(
                id='Figure-1',
                figure=fig2
            )

        ])


    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)