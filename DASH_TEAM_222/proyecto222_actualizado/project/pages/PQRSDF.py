#libraries
import dash
from dash import Dash, html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import plotly.graph_objects as go
import pandas as pd

# dash-labs plugin call, menu name and route
register_page(__name__, path='/PQRSDF')


df = pd.read_csv('project/pages/all_data_enhanced.csv',encoding='utf-8')

print('Haciendo el grafico del total del tipo de las pqrs')
graph_tipo_PQRS= df.groupby(['TIPO_DE_PQRSDF']).size()
graph_1= go.Bar(x=graph_tipo_PQRS.index, y=graph_tipo_PQRS.values,marker={'color': ['violet', 'pink', 'orange']})

print('Haciendo el grafico de la muestra de los canales de comunicacion')
print(df.columns)
graph_tipo_PQRS= df.groupby(['CANAL_DE_COMUNICACIÓN']).size()
graph_2= go.Bar(x=graph_tipo_PQRS.index, y=graph_tipo_PQRS.values,marker={'color': ['yellow ','green','gray']})

print('Haciendo el grafico de la muestra de los estados')
graph_tipo_PQRS= df.groupby(['ESTADO']).size()
graph_3= go.Bar(x=graph_tipo_PQRS.index, y=graph_tipo_PQRS.values,marker={'color': ['purple','orange','black', 'pink']})

print('Haciendo el grafico de la muestra de los generos')
graph_tipo_PQRS= df.groupby(['GENERO']).size()
graph_4= go.Bar(x=graph_tipo_PQRS.index, y=graph_tipo_PQRS.values,marker={'color': ['purple','yellow','pink']})

print('Haciendo el grafico de la muestra de las afiliaciones')
graph_tipo_PQRS= df.groupby(['EAPB']).size()
graph_5= go.Bar(x=graph_tipo_PQRS.index, y=graph_tipo_PQRS.values,marker={'color': ['purple','yellow','pink', 'orange','black', 'red','blue','green','gray', 'brown', 'purple', 'violet', 'green', 'orange', 'yellow','pink', 'green','gray', 'fuchsia', 'green', 'blue', 'brown','orange','violet','pink']})

print('Haciendo el grafico de la muestra de las afiliaciones segregados por el tipo de pqrs')
graph_tipo_PQRS= df.groupby(['EAPB','TIPO_DE_PQRSDF']).size().reset_index()
graph_tipo_PQRS=graph_tipo_PQRS.rename(columns={'TIPO_DE_PQRSDF':'TIPO'})
pqr = graph_tipo_PQRS.pivot_table(index=['TIPO'],columns=['EAPB']).fillna(0)
graph_P= go.Bar(x=pqr.iloc[0].reset_index()['EAPB'], y=pqr.iloc[0],name="P")
graph_Q= go.Bar(x=pqr.iloc[1].reset_index()['EAPB'], y=pqr.iloc[1], name="Q")
graph_S= go.Bar(x=pqr.iloc[2].reset_index()['EAPB'], y=pqr.iloc[2], name="S")

df_orfeo = pd.read_csv('project/components/maps/geo_data.csv',encoding='latin-1')

layout = html.Div(children=[
html.H1(children='Dashboard de los hospitales'),
    html.Div(children='''
    '''),
    dcc.Graph(
        id= 'Tipo_PQRSDF_Graph',
        figure={
            'data': [graph_1],
            'layout': 
            go.Layout(title= 'Type of PQRSDF')
        }),
    dcc.Graph(
        id='Canal_Comunicacion_Graph',
        figure={
            'data': [graph_2],
            'layout': 
            go.Layout(title= 'Communication Channel')
        }),
    dcc.Graph(
        id='Genero_Graph',
        figure={
            'data': [graph_4],
            'layout': 
            go.Layout(title= 'Genre')
        }),
    dcc.Graph(
        id='EAPB_Graph',
        figure={
            'data': [graph_5],
            'layout': 
            go.Layout(title= 'EAPB')
        }),
    dcc.Graph(
        id='PQRSDFs_EAPB_Graph',
        figure={
            'data': [graph_P, graph_Q, graph_S],
            'layout': 
            go.Layout(title= 'PQRSDFs by EAPB')
        })
])