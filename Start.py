import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
df = pd.read_csv(r'/Users/xisun/Desktop/datasets/Iris.csv')


fig = px.scatter(df,x="SepalLengthCm",y="PetalLengthCm",size="SepalWidthCm",color="Species",hover_name="PetalWidthCm",log_x=False,size_max=60)


app.layout = html.Div([dcc.Graph(id = "life-exp-vs-gdp",figure=fig)])


if __name__=='__main__':
    app.run_server(debug=True)