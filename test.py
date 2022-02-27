import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

#figures

df = pd.read_csv('./data/glass.csv')

fig = px.pie(df, values='Type', names='Type')

aux_df = df['Type'].value_counts()

fig2 = px.bar(df, x='Type', y='Al', barmode='group')

fig.show()

#print(df['Type'].value_counts())

#app = Dash(__name__)

#app.layout = html.Div(
    #dcc.Graph(id='pie-graph', figure=fig),
#    dcc.Graph(id='bar-graph', figure=fig2)
#)

#if __name__ == ('__main__'):
#    app.run_server(debug=True)