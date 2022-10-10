#libraries
import dash
from dash import Dash, html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import base64

# dash-labs plugin call, menu name and route
register_page(__name__, path='/Wordcloud')

IMAGE_WC_ALL = 'project/images/WC_all.png' # replace with your own image
ENCODED_IMAGE_WC_ALL = base64.b64encode(open(IMAGE_WC_ALL, 'rb').read())

IMAGE_WC_FEMALE = 'project/images/WC_female.png' # replace with your own image
ENCODED_IMAGE_WC_FEMALE = base64.b64encode(open(IMAGE_WC_FEMALE, 'rb').read())

IMAGE_WC_MALE = 'project/images/WC_male.png' # replace with your own image
ENCODED_IMAGE_WC_MALE = base64.b64encode(open(IMAGE_WC_MALE, 'rb').read())

layout= dbc.Container(children=[
    dbc.Row(children=[
        dbc.Col(children=[
            html.H1('WordCloud Male'),
            html.Img(src= "data:image/png;base64,{}".format(ENCODED_IMAGE_WC_MALE.decode()))
        ]),
        dbc.Col(children=[
            html.H1('WordCloud Female'),
            html.Img(src= "data:image/png;base64,{}".format(ENCODED_IMAGE_WC_FEMALE.decode()))
        ]),
        dbc.Col(children=[
            html.H1('WordCloud All'),
            html.Img(src= "data:image/png;base64,{}".format(ENCODED_IMAGE_WC_ALL.decode()))
        ])
    ])  
])



