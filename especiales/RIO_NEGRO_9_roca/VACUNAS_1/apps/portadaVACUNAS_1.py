import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from flask_login import logout_user, current_user
from login import login_failed
from config import *
from especiales.VACUNAS_1.apps.configVACUNAS_1 import *
from app import app
from txt import textos
from especiales.VACUNAS_1.apps.txtVACUNAS_1 import textosVACUNAS_1
import dash_bootstrap_components as dbc
#from permisos import trackingVACUNAS_1PreguntasDeshabilitadas, trackingVACUNAS_1BloquesDeshabilitados

trackingVACUNAS_1PreguntasDeshabilitadas, trackingVACUNAS_1BloquesDeshabilitados = "",""
from especiales.VACUNAS_1.apps.bloquesVACUNAS_1 import bloques_VACUNAS_1
from especiales.VACUNAS_1.apps.layoutVACUNAS_1 import ps, preguntas
import pandas as pd



dropdown_tema = dcc.Dropdown( id='VACUNAS_1_tema', searchable=False, clearable=False,
                                                                options= [{'label':'Todo', "value":'todo'}] + [{'label': v, 'value': k} for k,v in preguntas.items()],
                                                                value='todo')

tabs = [
    dcc.Tab(
        label='Ficha Técnica',
        value='tab-1',
        className='custom-tab',
        selected_className='custom-tab--selected'
    ),
    dcc.Tab(
        label='Encuesta',
        value='tab-2',
        className='custom-tab',
        selected_className='custom-tab--selected'
    ),
    dcc.Tab(
        label='Informe',
        value='tab-3',
        className='custom-tab',
        selected_className='custom-tab--selected'
    )                
]

if informe==False:
    tabs = tabs[:2]

layout = html.Div( 
    children=[
        #dcc.Store(id='session', storage_type='session'),        
        html.Div( 
            className='section-header pba',
            children=[
                html.Div(
                    className='section-breadcrumb',
                    children=[
                        html.P(children=textos['breadcrumb']),
                    ]
                ),
                html.H2(children=textosVACUNAS_1['encuesta_especial']),
                html.P(children=textosVACUNAS_1['bajada_encuesta_especial']),
                #html.P(children=textosVACUNAS_1['bajada_encuesta_especial2'], className="bold"),
                html.P(children=textosVACUNAS_1['bajada_encuesta_especial_fecha']),
            ]
        ),
        html.Div([ 
        
        dcc.Tabs(
            id="VACUNAS_1-tabs-with-classes",
            value='tab-1',
            parent_className='custom-tabs',
            className='container custom-tabs-container',
            children=tabs),
        html.Div(id='VACUNAS_1-tabs-content-classes')
    ]),
    html.Div(
        className='footer',
        children=[
            html.P(children=textos['footer'])
        ]

    )
]),
    
@app.callback(Output('VACUNAS_1-tabs-content-classes', 'children'),
              [Input('VACUNAS_1-tabs-with-classes', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div(
                children=[
                    html.Div(
                        className='ficha',
                        children=[
                        html.Div(
                            className='container',
                            children=[
                                html.Div(
                                    className='row',
                                    children=[
                                        html.Div(
                                            className='col-12 col-sm-4',
                                            children=[
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato1']),
                                                        html.P(children=textosVACUNAS_1['textoDato1']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato2']),
                                                        html.P(children=textosVACUNAS_1['textoDato2']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato3']),
                                                        html.P(children=textosVACUNAS_1['textoDato3']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato4']),
                                                        html.P(children=textosVACUNAS_1['textoDato4']),
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className='col-12 col-sm-4',
                                            children=[
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato5']),
                                                        html.P(children=textosVACUNAS_1['textoDato5']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato6']),
                                                        html.P(children=textosVACUNAS_1['textoDato6']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato  no-border-bottom',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato7']),
                                                        html.P(children=textosVACUNAS_1['textoDato7']),
                                                    ]
                                                ),

                                            ]
                                        ),
                                        html.Div(
                                            className='col-12 col-sm-4',
                                            children=[
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato8']),
                                                        html.P(children=textosVACUNAS_1['textoDato8']),
                                                    ]
                                                ),

                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosVACUNAS_1['tituloDato9']),
                                                        html.P(children=textosVACUNAS_1['textoDato9']),
                                                    ]
                                                )



                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            ]            
        )
    elif tab == 'tab-2':
        preguntaPorDefecto = ''    
        opciones=[]
        preguntasDeshabilitadas = ""#, trackingVACUNAS_1BloquesDeshabilitados()
        #preguntas = pr
        for key, value in preguntas.items():
            if not key in preguntasDeshabilitadas:
                opciones.append({'label': value, 'value': key})
                if len(preguntaPorDefecto) == 0:
                    preguntaPorDefecto = value

        return html.Div(
            className='encuesta',
            children=[
                html.Div(
                    className='container filtros',
                    children=[
                        html.Div(
                            className='row',
                            children=[
                                html.Div(
                                    className='col-12 col-sm-9',
                                    children=[
                                    ]
                                )
                            ]
                        ),
                         html.Div(
                            className='row',
                            children=[                                
                                html.Div(
                                    className='col-12 col-sm-9',
                                    children=[
                                        html.Label(children=textos['labelTema']),
                                        html.Div(
                                        id='VACUNAS_1-div-tema-dropdown-container',
                                        children=[dropdown_tema,

                                                  ])
                                    ]
                                ),
                                html.Div(
                                    className='col-12 col-sm-3',
                                    children=[
                                        html.Label(children=textos['labelTarget']),
                                        dropdownTargetVACUNAS('selectTargetVACUNAS_1', cantidadDeOpciones=17)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div([html.Div([html.H3('Cargando Gráficos'),
                                    dbc.Spinner(color="primary", type="grow"),
                                    dbc.Spinner(color="primary", type="grow"),
                                    dbc.Spinner(color="primary", type="grow")
                                    ], style={'text-align':'center'}, id='VACUNAS_1-loading_content'),
                    html.Div(
                        html.Div(id='VACUNAS_1-bloque-content', style={'display':'none'}, className='content'),
                        className='content-container'
                    ),
                ], className='container'),
            ]
        )
    elif tab == 'tab-3':
        return html.Div(
            className='encuesta',
            children=[
                html.Div(
                    html.H3('Acá va el informe')
                    )
                ]
            )
        

def showImage(filename):
    encoded_image = base64.b64encode(open(filename, 'rb').read())
    layout = html.Div(children=[
             html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
             ])
    return layout


@app.callback(
    dash.dependencies.Output('VACUNAS_1-bloque-content', 'children'),
    [dash.dependencies.Input('VACUNAS_1_tema', 'value')])
def update_output(pregunta):
    # Devuelve el "layout" de la pregunta seleccionada en el dropdown tema, o un layout con todas las preguntas del bloque
    # si esta seleccionado Bloque completo
    # De esta forma nos evitamos la conversion esa de pregunta a las letras A B C etc que se repetian en los bloques

    if current_user.is_authenticated:
        preguntasDeshabilitadas = ""#,trackingVACUNAS_1PreguntasDeshabilitadas()
        if pregunta != 'todo': # Si es una sola pregunta

            return ps[pregunta]

        else:  # si es el bloque completo

            return [html.Div(ps[preg]) for preg in preguntas
                if preg not in preguntasDeshabilitadas]
    else:
        return login_failed.layout


@app.callback(
    [dash.dependencies.Output('VACUNAS_1-loading_content', 'style'),
     dash.dependencies.Output('VACUNAS_1-bloque-content', 'style')],
    [dash.dependencies.Input('enhanced-graph-VACUNAS_1-P35-1', 'loading_state')],
    [dash.dependencies.State('enhanced-graph-VACUNAS_1-P35-1', 'loading_state')]
)
def update_output(_,__):
    return {'display':'none'},{'display':'inline'}
