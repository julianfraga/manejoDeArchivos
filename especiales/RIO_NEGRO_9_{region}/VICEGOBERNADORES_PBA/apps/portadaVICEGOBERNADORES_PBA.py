import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from flask_login import logout_user, current_user
from login import login_failed
from config import *
from especiales.VICEGOBERNADORES_PBA.apps.config_VICEGOBERNADORES_PBA import *
from app import app
from txt import textos
from especiales.VICEGOBERNADORES_PBA.apps.txt_VICEGOBERNADORES_PBA import textos_VICEGOBERNADORES_PBA
from permisos import trackingSANTIAGOPreguntasDeshabilitadas as trackingVICEGOBERNADORES_PBAPreguntasDeshabilitadas
from permisos import trackingSANTIAGOBloquesDeshabilitados as trackingVICEGOBERNADORES_PBABloquesDeshabilitados
from especiales.VICEGOBERNADORES_PBA.apps.cuestionario_VICEGOBERNADORES_PBA import bloques
from especiales.VICEGOBERNADORES_PBA.apps.config_VICEGOBERNADORES_PBA import *
import pandas as pd



dropdown_tema = dcc.Dropdown( id='VICEGOBERNADORES_PBA_tema', searchable=False, clearable=False,
                                                                )
def dropwdownOpciones(id='selectOpciones'):
    opciones = [
        {'label': 'No disponible', 'value': '_4opc'}]
    return html.Div([
        html.Label(children='Cantidad de opciones en preguntas de opinión'),
        dcc.Dropdown(
            id=id,
            options=opciones,
            value='_4opc',
            searchable=False,
            clearable=False
        )
    ])

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
                html.H2(children=textos_VICEGOBERNADORES_PBA['encuesta_especial']),
                html.P(children=textos_VICEGOBERNADORES_PBA['bajada_encuesta_especial']),
                #html.P(children=textos_VICEGOBERNADORES_PBA['bajada_encuesta_especial2'], className="bold"),
                html.P(children=textos_VICEGOBERNADORES_PBA['bajada_encuesta_especial_fecha']),
            ]
        ),
        html.Div([ 
        
        dcc.Tabs(
            id="VICEGOBERNADORES_PBA-tabs-with-classes",
            value='tab-1',
            parent_className='custom-tabs',
            className='container custom-tabs-container',
            children=tabs),
        html.Div(id='VICEGOBERNADORES_PBA-tabs-content-classes')
    ]),
    html.Div(
        className='footer',
        children=[
            html.P(children=textos['footer'])
        ]

    )
]),
    
@app.callback(Output('VICEGOBERNADORES_PBA-tabs-content-classes', 'children'),
              [Input('VICEGOBERNADORES_PBA-tabs-with-classes', 'value')])
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
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato1']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato1']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato2']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato2']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato3']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato3']),
                                                    ]
                                                ),
                                                # html.Div(
                                                #     className='dato no-border-bottom',
                                                #     children=[
                                                #         html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato4']),
                                                #         html.P(children=textos_VICEGOBERNADORES_PBA['textoDato4']),
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
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato5']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato5']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato',
                                                    children=[
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato6']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato6']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato7']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato7']),
                                                    ]
                                                ),
                                                # html.Div(
                                                #     className='dato no-border-bottom',
                                                #     children=[
                                                #         html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato8']),
                                                #         html.P(children=textos_VICEGOBERNADORES_PBA['textoDato8']),
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
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato8']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato8']),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='dato no-border-bottom',
                                                    children=[
                                                        html.H3(children=textos_VICEGOBERNADORES_PBA['tituloDato9']),
                                                        html.P(children=textos_VICEGOBERNADORES_PBA['textoDato9']),
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
        preguntasDeshabilitadas = trackingVICEGOBERNADORES_PBABloquesDeshabilitados()
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
        #         opciones.append({'label': textos_VICEGOBERNADORES_PBA[key], 'value': textos_VICEGOBERNADORES_PBA[value]})
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
                                            id='VICEGOBERNADORES_PBA-bloques-dropdown',
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
                                        id='VICEGOBERNADORES_PBA-div-tema-dropdown-container',
                                        children=[dropdown_tema,
                                                 dropwdownOpciones("selectOpciones_VICEGOBERNADORES_PBA")
                                                  ])
                                    ]
                                ),
                                html.Div(
                                    className='col-12 col-sm-3',
                                    children=[
                                        html.Label(children=textos['labelTarget']),
                                        dropdownTarget('selectTargetVICEGOBERNADORES_PBA', cantidadDeOpciones =19)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div([
                    html.Div(
                        html.Div(id='VICEGOBERNADORES_PBA-bloque-content', className='content'),
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
    [dash.dependencies.Output('VICEGOBERNADORES_PBA_tema', 'options'), dash.dependencies.Output('VICEGOBERNADORES_PBA_tema', 'value')],
    [dash.dependencies.Input('VICEGOBERNADORES_PBA-bloques-dropdown', 'value')])
def update_output(pathname):
    # Callback para llenar el dropdown de los temas. Lee el bloque seleccionado desde del dropdown de bloques,
    # busca que preguntas contiene ese bloque y las pone como opciones del dropdown de preguntas.

    preguntasDeshabilitadas  = []#trackingVICEGOBERNADORES_PBAPreguntasDeshabilitadas()

    pregs = [p for p in bloques[pathname.replace('/apps/', '')]
             if p not in preguntasDeshabilitadas]

    salida = [{'label':"Bloque completo", 'value':'todo'}]
    default_value = 'todo'

    # if "imagen" in pathname.replace('/apps/', '').lower(): # imagen tiene el bloque todos diferente
    #     salida = []
    #     default_value = pregs[0]

    salida.extend([{'label': textos_VICEGOBERNADORES_PBA['label' + p], 'value': p } for p in pregs])



    return salida, default_value


@app.callback(
    dash.dependencies.Output('VICEGOBERNADORES_PBA-bloque-content', 'children'),
    [dash.dependencies.Input('VICEGOBERNADORES_PBA_tema', 'value'),dash.dependencies.Input('VICEGOBERNADORES_PBA-bloques-dropdown', 'value')])
def update_output(pregunta, pathname):
    # Devuelve el "layout" de la pregunta seleccionada en el dropdown tema, o un layout con todas las preguntas del bloque
    # si esta seleccionado Bloque completo
    # De esta forma nos evitamos la conversion esa de pregunta a las letras A B C etc que se repetian en los bloques

    if current_user.is_authenticated:
        preguntasDeshabilitadas = trackingVICEGOBERNADORES_PBAPreguntasDeshabilitadas()
        if pregunta != 'todo': # Si es una sola pregunta

            return ps[pregunta]
        else:
            return [html.Div(ps[preg]) for preg in bloques[pathname.replace('/apps/', '')]
                if preg not in preguntasDeshabilitadas]
    else:
        return login_failed.layout
