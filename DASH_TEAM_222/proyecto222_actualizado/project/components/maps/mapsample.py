from dash import dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL #, ClientsideFunction
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px 
import pandas as pd

class mapsample:    
    """A class to represent a samplemap of Montreal Elections"""        
    def __init__(self,map_title:str,ID:str):
        """__init__
        Construct all the attributes for the sample map

        Args:
            map_title (str): _Title for the map_
            ID (str): _div id to specify unique #id with callbacks and css_

        Methods:

        display()
            Function to display a sample map with no arguments, uses plotly express data.

            Arguments:
                None

            Returns:
                html.Div : A Div container with a dash core component dcc.Graph() inside
        """

        self.map_title = map_title
        self.id = ID

    @staticmethod
    def figura():
        df = pd.read_csv('project/components/maps/geo_data.csv', encoding='latin-1')
        df['FECHA']=pd.to_datetime(df['FECHA'])
        df['MONTH'] = df['FECHA'].dt.month
        df_pivot = df.pivot_table(index=['DIRECCION_COMPLETA'],columns='MONTH', aggfunc='size', fill_value=0)
        
        fig = px.scatter_mapbox(
        lon=df['LONGITUD'],
        lat=df['LATITUD'],
        text=df['DIRECCION_COMPLETA'],
        #mode='markers',
        zoom=9
        #marker_color= 'RED'
        )

        fig.update_layout(
            autosize=True,
            hovermode='closest',
            mapbox_style="open-street-map",
            
            )
        
        return fig

    def display(self):

        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=self.figura())
                ])

            ],id=self.id
        )
        return layout