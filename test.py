import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import joblib

#figures

df = pd.read_csv('./data/glass.csv')

dt = joblib.load('./models/DecisionTree.joblib')

df_decisionTree = pd.Series(dt.feature_importances_, index=df.columns.values[0:-1])

fig = px.bar(df_decisionTree)

fig.show()