#libraries
import dash
from dash import Dash, html , dcc
import dash_labs as dl
import dash_bootstrap_components as dbc
import os
import dash_auth
from users import USERNAME_PASSWORD_PAIRS
#from callbacks import register_callbacks
import base64

request_path_prefix = None

#only for workspace in DS4A
workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

print(request_path_prefix)
# Dash instance declaration
app = dash.Dash(__name__, plugins=[dl.plugins.pages], requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.FLATLY],)
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS) 
page = {'name': ['geolocalization','Wordcloud','Institutions','PQRSDF'], 'path': ['pages/geolocalization.py','pages/Wordcloud.py','pages/Institutions.py','pages/PQRSDF.py']}

print(page['name'])
image_filename = 'project/images/logo.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([
    html.Img(src="data:image/png;base64,{}".format(encoded_image.decode()),style={'width':'10%','height':'0.5%','margin-left':'20%','margin-right':'40%'}),
    dbc.NavItem(dbc.NavLink( "Inicio", href=request_path_prefix)),
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="PQRS Secretaria de Salud - Sogamoso",
    ),
    dbc.NavItem(dbc.NavLink("Nosotros", href="/about_us")),
    ],
    brand="DS4A Project - Team 222",
    color="primary",
    dark=True,
    className="mb-2",
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)


# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(port=8050, debug=True)