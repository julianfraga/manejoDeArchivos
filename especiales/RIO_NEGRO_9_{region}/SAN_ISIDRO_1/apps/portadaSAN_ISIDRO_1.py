import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from flask_login import logout_user, current_user
from login import login_failed
from config import *
from especiales.SAN_ISIDRO_1.apps.configSAN_ISIDRO_1 import *
from app import app
from txt import textos
from especiales.SAN_ISIDRO_1.apps.txtSAN_ISIDRO_1 import textosSAN_ISIDRO_1
from permisos import trackingSANTIAGOPreguntasDeshabilitadas as trackingSAN_ISIDRO_1PreguntasDeshabilitadas
from permisos import trackingSANTIAGOBloquesDeshabilitados as trackingSAN_ISIDRO_1BloquesDeshabilitados
from especiales.SAN_ISIDRO_1.apps.layoutSAN_ISIDRO_1 import ps, preguntas, orden_preguntas
from especiales.SAN_ISIDRO_1.apps.bloquesSAN_ISIDRO_1 import bloques_SAN_ISIDRO_1

import pandas as pd



dropdown_tema = dcc.Dropdown( id='SAN_ISIDRO_1_tema', searchable=False, clearable=False,
                                                                options= [{'label': v, 'value': k} for k,v in preguntas.items()],
                                                                value='todo')

bloques = {}
for b in range(1, 4):
    bloques['bloque' + str(b)] = 'bloque' + str(b) + 'href'
    
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
                html.H2(children=textosSAN_ISIDRO_1['encuesta_especial']),
                html.P(children=textosSAN_ISIDRO_1['bajada_encuesta_especial']),
                #html.P(children=textosSAN_ISIDRO_1['bajada_encuesta_especial2'], className="bold"),
                html.P(children=textosSAN_ISIDRO_1['bajada_encuesta_especial_fecha']),
            ]
        ),
        html.Div([ 
        
        dcc.Tabs(
            id="SAN_ISIDRO_1-tabs-with-classes",
            value='tab-1',
            parent_className='custom-tabs',
            className='container custom-tabs-container',
            children=tabs),
        html.Div(id='SAN_ISIDRO_1-tabs-content-classes')
    ]),
    html.Div(
        className='footer',
        children=[
            html.P(children=textos['footer'])
        ]

    )
]),
    
@app.callback(Output('SAN_ISIDRO_1-tabs-content-classes', 'children'),
              [Input('SAN_ISIDRO_1-tabs-with-classes', 'value')])
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
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato1']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato1']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato2']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato2']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato3']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato3']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato4']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato4']),
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
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato5']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato5']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato6']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato6']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato7']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato7']),
                                                    ]
                                                ),
                                                # html.Div(
                                                #     className='dato no-border-bottom',
                                                #     children=[
                                                #         html.H3(children=textosSAN_ISIDRO_1['tituloDato8']),
                                                #         html.P(children=textosSAN_ISIDRO_1['textoDato8']),
                                                #     ]
                                                # )
                                            ]
                                        ),
                                        html.Div(
                                            className='col-12 col-sm-4',
                                            children=[
                                                # html.Div(
                                                #     className='dato',
                                                #     children=[
                                                #         html.H3(children=textosSAN_ISIDRO_1['tituloDato9']),
                                                #         html.P(children=textosSAN_ISIDRO_1['textoDato9']),
                                                #     ]
                                                # ),
                                                # html.Div(
                                                #     className='dato',
                                                #     children=[
                                                #         html.H3(children=textosSAN_ISIDRO_1['tituloDato10']),
                                                #         html.P(children=textosSAN_ISIDRO_1['textoDato10']),
                                                #     ]
                                                # ),
                                                # html.Div(
                                                #     className='dato',
                                                #     children=[
                                                #         html.H3(children=textosSAN_ISIDRO_1['tituloDato11']),
                                                #         html.P(children=textosSAN_ISIDRO_1['textoDato11']),
                                                #     ]
                                                # ),
                                                # html.Div(
                                                #     className='dato',
                                                #     children=[
                                                #         html.H3(children=textosSAN_ISIDRO_1['tituloDato12']),
                                                #         html.P(children=textosSAN_ISIDRO_1['textoDato12']),
                                                #     ]
                                                # ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato8']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato8']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textosSAN_ISIDRO_1['tituloDato9']),
                                                        html.P(children=textosSAN_ISIDRO_1['textoDato9']),
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
        preguntasDeshabilitadas = trackingSAN_ISIDRO_1BloquesDeshabilitados()
        preguntas = bloques
        for key, value in  {"bloque1":"bloque1href", "bloque3":"bloque3href"}.items():
            if not key in preguntasDeshabilitadas:
                opciones.append({'label': textosSAN_ISIDRO_1[key], 'value': textosSAN_ISIDRO_1[value]})
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
                                    html.Label(children=textos['labelBloque']),
                                        dcc.Dropdown(
                                            id='SAN_ISIDRO_1-bloques-dropdown',
                                            options=opciones,
                                            value=textosSAN_ISIDRO_1['bloque1href'],
                                            searchable=False,
                                            clearable=False
                                        ),
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
                                        id='SAN_ISIDRO_1-div-tema-dropdown-container',
                                        children=[dropdown_tema,
                                                 dropwdownOpcionesSAN_ISIDRO_1(id='selectOpciones')
                                                  ])
                                    ]
                                ),
                                html.Div(
                                    className='col-12 col-sm-3',
                                    children=[
                                        html.Label(children=textos['labelTarget']),
                                        dropdownTargetSAN_ISIDRO_1('selectTargetSAN_ISIDRO_1', cantidadDeOpciones =20)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div([
                    html.Div(
                        html.Div(id='SAN_ISIDRO_1-bloque-content', className='content'),
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
    [dash.dependencies.Output('SAN_ISIDRO_1_tema', 'options'), dash.dependencies.Output('SAN_ISIDRO_1_tema', 'value')],
    [dash.dependencies.Input('SAN_ISIDRO_1-bloques-dropdown', 'value')])
def update_output(pathname):
    # Callback para llenar el dropdown de los temas. Lee el bloque seleccionado desde del dropdown de bloques,
    # busca que preguntas contiene ese bloque y las pone como opciones del dropdown de preguntas.

    preguntasDeshabilitadas  = trackingSAN_ISIDRO_1PreguntasDeshabilitadas()

    pregs = [p for p in bloques_SAN_ISIDRO_1[pathname.replace('/apps/', '')]
             if p not in preguntasDeshabilitadas]
    salida = [{'label':"Bloque completo", 'value':'todo'}]
    default_value = 'todo'

    if pathname.replace('/apps/', '') == "bloque3": # imagen tiene el bloque todos diferente
        salida = []
        default_value = pregs[0]

    salida.extend([{'label': v, 'value': k} for k, v in preguntas.items() if k in pregs])

    return salida, default_value


@app.callback(
    dash.dependencies.Output('SAN_ISIDRO_1-bloque-content', 'children'),
    [dash.dependencies.Input('SAN_ISIDRO_1_tema', 'value'),dash.dependencies.Input('SAN_ISIDRO_1-bloques-dropdown', 'value')])
def update_output(pregunta, pathname):
    # Devuelve el "layout" de la pregunta seleccionada en el dropdown tema, o un layout con todas las preguntas del bloque
    # si esta seleccionado Bloque completo
    # De esta forma nos evitamos la conversion esa de pregunta a las letras A B C etc que se repetian en los bloques

    if current_user.is_authenticated:
        preguntasDeshabilitadas = trackingSAN_ISIDRO_1PreguntasDeshabilitadas()
        if pregunta != 'todo': # Si es una sola pregunta

            return ps[pregunta]
        else:
            if pathname.replace('/apps/', '') == "bloque3":  # Parche para el layout de imagen completo

                return ps['imagen1']

            else:  # si es el bloque completo

                return [html.Div(ps[preg]) for preg in bloques_SAN_ISIDRO_1[pathname.replace('/apps/', '')]
                    if preg not in preguntasDeshabilitadas]
    else:
        return login_failed.layout
