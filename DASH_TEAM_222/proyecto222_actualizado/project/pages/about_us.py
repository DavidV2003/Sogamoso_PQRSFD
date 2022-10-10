import dash
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/about_us")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

layout= dbc.Container(children=[
    dbc.Row(children=[
        dbc.Col(children=[
            html.H1('Business problem')
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.H2('OVERVIEW') 
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.P("""Sogamoso is a city located in
            Boyacá, Colombia, which according
            to DANE projections, in 2022 has
            132,985 inhabitants. Its economy is
            mainly based on the steel industry,
            construction materials production,
            coal mining, and agriculture. The
            hospital infrastructure of Sogamoso
            has three levels of attention through
            eight institutions.""")
        ]),
        dbc.Col(children=[
            html.H4('132985 inhabitants & 8 hospital') ]
        )
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.H4('Reception of PQRSDF through Orfeo') 
            ]),
        dbc.Col(children=[
            html.P("""One of the branches of the Municipal
            Government is the SMS, which has 
            implemented SIAU. Its main 
            objective is the reception of
            PQRSDF, especially those related to
            the EAPB operation. This is done
            through Orfeo, which is a digital
            platform that handles all the
            PQRSDF of the city, including those
            directed to the SMS. Requests are
            submitted either virtually or in
            person. In the second case, the
            physical document is digitalized and
            attached to an online requirement,
            so Orfeo handles both methods.""")
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.P("""The mission of SIAU is to address
            complaints and requirements filed by
            affiliates of the Subsidized and
            Contributory Regime, so the risk of
            diseases is mitigated and health
            prevention is performed. The
            implementation of the system
            follows the Quality Management
            System, governed by guidelines of
            MinSalud and UNDP.
            """)
        ]),
        dbc.Col(children=[
            html.H4('Mitigation of diseases and health prevention') ]
        )
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.H2('OPPORTUNITY') 
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.P("""The SMS has detected that some of
            the EAPB do not guarantee proper
            attention to their affiliates, and thus
            users constantly fill PQRSDF.
            Currently, the city does not have a
            tool that can be used to prioritize the
            urgency and relevance of these
            petitions. Also, there is no analysis
            or study on this data at all.
            """)
        ]),
        dbc.Col(children=[
            html.H4('User fill PQRSDF about EAPB attention') ]
        )
    ]),
     dbc.Row(children=[
        dbc.Col(children=[
            html.H4('Detect, model and predict') 
            ]),
        dbc.Col(children=[
            html.P("""Hence, the main purpose of our
            Team is to use Data Science
            techniques to analyze the PQRSDF of
            Sogamoso in order to detect, model
            and predict the aspects of the Health
            System (procedures, medical
            dependencies, prevention, diseases,
            EAPB, etc.) that most affect the
            population of the city and that
            therefore require greater attention
            from the institutions. User
            satisfaction and the main reasons
            that lead them to file PQRSDF shall
            also be explored.
            """)
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.H2('IMPACT') 
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.P("""Healthcare is a Fundamental Right
            regulated by Colombian Law 1751 of
            2015. Its objective is to regulate the
            Health System, and establish its
            protection mechanisms, via
            prevention of diseases, promotion of
            healthcare, and improvement of
            health indicators. Hence, raising the
            efficiency of the PQRSDF resolution
            process could deeply impact the
            quality of life of the population.
            """)
        ]),
        dbc.Col(children=[
            html.H4('Healthcare is a Fundamental Right') ]
        )
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            html.H4('Improving the Health System') 
            ]),
        dbc.Col(children=[
            html.P("""These improvements also impact the
            trust of the people in public
            institutions, the Health System, the
            health management indicators, the
            quality of health services, and the
            efficiency of the institutional
            procedures of the quality system.
            """)
        ])
    ])                                                                                                                                                                
])