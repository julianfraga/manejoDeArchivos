import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from flask_login import logout_user, current_user
from login import login_failed
from config import *
from especiales.MERLO_9.apps.config_MERLO_9 import *
from app import app
from txt import textos
from especiales.MERLO_9.apps.txt_MERLO_9 import textos_MERLO_9
from permisos import trackingSANTIAGOPreguntasDeshabilitadas as trackingMERLO_9PreguntasDeshabilitadas
from permisos import trackingSANTIAGOBloquesDeshabilitados as trackingMERLO_9BloquesDeshabilitados
from especiales.MERLO_9.apps.cuestionario_MERLO_9 import bloques
from especiales.MERLO_9.apps.config_MERLO_9 import *
import pandas as pd



dropdown_tema = dcc.Dropdown( id='MERLO_9_tema', searchable=False, clearable=False,
                                                                )


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
                html.H2(children=textos_MERLO_9['encuesta_especial']),
                html.P(children=textos_MERLO_9['bajada_encuesta_especial']),
                #html.P(children=textos_MERLO_9['bajada_encuesta_especial2'], className="bold"),
                html.P(children=textos_MERLO_9['bajada_encuesta_especial_fecha']),
            ]
        ),
        html.Div([ 
        
        dcc.Tabs(
            id="MERLO_9-tabs-with-classes",
            value='tab-1',
            parent_className='custom-tabs',
            className='container custom-tabs-container',
            children=tabs),
        html.Div(id='MERLO_9-tabs-content-classes')
    ]),
    html.Div(
        className='footer',
        children=[
            html.P(children=textos['footer'])
        ]

    )
]),
    
@app.callback(Output('MERLO_9-tabs-content-classes', 'children'),
              [Input('MERLO_9-tabs-with-classes', 'value')])
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
                                                        html.H3(children=textos_MERLO_9['tituloDato1']),
                                                        html.P(children=textos_MERLO_9['textoDato1']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textos_MERLO_9['tituloDato2']),
                                                        html.P(children=textos_MERLO_9['textoDato2']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textos_MERLO_9['tituloDato3']),
                                                        html.P(children=textos_MERLO_9['textoDato3']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textos_MERLO_9['tituloDato4']),
                                                        html.P(children=textos_MERLO_9['textoDato4']),
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
                                                        html.H3(children=textos_MERLO_9['tituloDato5']),
                                                        html.P(children=textos_MERLO_9['textoDato5']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textos_MERLO_9['tituloDato6']),
                                                        html.P(children=textos_MERLO_9['textoDato6']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textos_MERLO_9['tituloDato7']),
                                                        html.P(children=textos_MERLO_9['textoDato7']),
                                                    ]
                                                ),
                                                # html.Div(
                                                #     className='dato no-border-bottom',
                                                #     children=[
                                                #         html.H3(children=textos_MERLO_9['tituloDato8']),
                                                #         html.P(children=textos_MERLO_9['textoDato8']),
                                                #     ]
                                                # )
                                            ]
                                        ),
                                        html.Div(
                                            className='col-12 col-sm-4',
                                            children=[
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textos_MERLO_9['tituloDato8']),
                                                        html.P(children=textos_MERLO_9['textoDato8']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textos_MERLO_9['tituloDato9']),
                                                        html.P(children=textos_MERLO_9['textoDato9']),
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
        preguntasDeshabilitadas = trackingMERLO_9BloquesDeshabilitados()
        preguntas = bloques
        # for key, value in  {"bloque1":"bloque1href",
        #                     "bloque2":"bloque2href",
        #                     "bloque3":"bloque3href",
        #                     "bloque4":"bloque4href",
        #                     "bloque6": "bloque6href",
        #                     "bloque5": "bloque5href",
        #
        #                 }.items():
        #     if not key in preguntasDeshabilitadas:
        #         opciones.append({'label': textos_MERLO_9[key], 'value': textos_MERLO_9[value]})
        #         if len(preguntaPorDefecto) == 0:
        #             preguntaPorDefecto = value

        for bloque in bloques.keys():

            if not bloque in preguntasDeshabilitadas:
                opciones.append({'label': bloque, 'value': bloque})
                if len(preguntaPorDefecto) == 0:
                    preguntaPorDefecto = bloque




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
                                            id='MERLO_9-bloques-dropdown',
                                            options=opciones,
                                            value=list(bloques.keys())[0],
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
                                        id='MERLO_9-div-tema-dropdown-container',
                                        children=[dropdown_tema,
                                                 dropwdownOpciones("selectOpciones_MERLO_9")
                                                  ])
                                    ]
                                ),
                                html.Div(
                                    className='col-12 col-sm-3',
                                    children=[
                                        html.Label(children=textos['labelTarget']),
                                        dropdownTarget('selectTargetMERLO_9', cantidadDeOpciones =19)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div([
                    html.Div(
                        html.Div(id='MERLO_9-bloque-content', className='content'),
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
    [dash.dependencies.Output('MERLO_9_tema', 'options'), dash.dependencies.Output('MERLO_9_tema', 'value')],
    [dash.dependencies.Input('MERLO_9-bloques-dropdown', 'value')])
def update_output(pathname):
    # Callback para llenar el dropdown de los temas. Lee el bloque seleccionado desde del dropdown de bloques,
    # busca que preguntas contiene ese bloque y las pone como opciones del dropdown de preguntas.

    preguntasDeshabilitadas  = []#trackingMERLO_9PreguntasDeshabilitadas()

    pregs = [p for p in bloques[pathname.replace('/apps/', '')]
             if p not in preguntasDeshabilitadas]

    salida = [{'label':"Bloque completo", 'value':'todo'}]
    default_value = 'todo'

    if "imagen" in pathname.replace('/apps/', '').lower(): # imagen tiene el bloque todos diferente
        salida = []
        default_value = pregs[0]

    salida.extend([{'label': textos_MERLO_9['label' + p], 'value': p } for p in pregs])



    return salida, default_value


@app.callback(
    dash.dependencies.Output('MERLO_9-bloque-content', 'children'),
    [dash.dependencies.Input('MERLO_9_tema', 'value'),dash.dependencies.Input('MERLO_9-bloques-dropdown', 'value')])
def update_output(pregunta, pathname):
    # Devuelve el "layout" de la pregunta seleccionada en el dropdown tema, o un layout con todas las preguntas del bloque
    # si esta seleccionado Bloque completo
    # De esta forma nos evitamos la conversion esa de pregunta a las letras A B C etc que se repetian en los bloques

    if current_user.is_authenticated:
        preguntasDeshabilitadas = trackingMERLO_9PreguntasDeshabilitadas()
        if pregunta != 'todo': # Si es una sola pregunta

            return ps[pregunta]
        else:
            if "imagen" in pathname.replace('/apps/', '').lower():  # Parche para el layout de imagen completo

                return ps['imagen1']

            else:  # si es el bloque completo

                return [html.Div(ps[preg]) for preg in bloques[pathname.replace('/apps/', '')]
                    if preg not in preguntasDeshabilitadas]
    else:
        return login_failed.layout
