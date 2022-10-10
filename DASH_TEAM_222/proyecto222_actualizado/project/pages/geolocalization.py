import dash
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/geolocalization")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px


from components.maps.mapsample import mapsample
mapa_ejemplo = mapsample('This is my custom map', 'div_samplemap')

# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['PQRS in Sogamoso'],id="div_title_maps"),
                 mapa_ejemplo.display()
                 
            ], lg=12), 

        ]),
        ]
) 