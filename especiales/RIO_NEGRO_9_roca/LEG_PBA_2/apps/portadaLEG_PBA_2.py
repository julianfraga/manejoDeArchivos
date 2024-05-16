from graphs import *
import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from flask_login import logout_user, current_user
from login import login_failed
from especiales.LEG_PBA_2.apps.config import *
from app import app
from txt import textos
from permisos import *
import dash_bootstrap_components as dbc
import pandas as pd
from especiales.LEG_PBA_2.apps.txtLEG_PBA_2 import textosLEG_PBA_2
from especiales.LEG_PBA_2.apps.layout import layouts, filesLEG_PBA_2, preguntas, preguntas_provincias


# Esta pagina ademas de las tipicas paginas de la portada tiene toda una parte extra para cargar lo que sería el HOME
# este tracking (los links a las distintas sub encuestas)


# Dropdown con las distintas preguntas ( y transferencia en este caso)
_preguntas = ['P11']
dropdown_tema = dcc.Dropdown(  searchable=False, clearable=False, id='LEG_PBA_2_select_preguntas',
                                                                options= [{'label': 'Bloque completo', 'value': "todo"}] +
                                                                         [{'label': textosLEG_PBA_2['label' + p],  'value':   p} for p in  _preguntas]
                               ,
                                                                value='todo')

layout = html.Div(
		children=[
			html.Div(
			id="content_LEG_PBA_2",
            #className='slider',

		),
		html.Div(
	        className='footer m-t-0',
	        children=[
	            html.P(children=textos['footer']),  html.Div("start", id='collapse_tmp', style={'display':'none'})
	        ]
	    )
    ])




encuesta = html.Div(id='LEG_PBA_2_encuestas')

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
    )
]



@app.callback(Output('content_LEG_PBA_2', 'children'),
              [Input('url', 'pathname')])
def display_slides(pathname):

    if current_user.is_authenticated:
        if pathname == '/especiales_LEG_PBA_2/portada':

            provincias_habilitadas = [html.H1("Provincias")]
            for provincia in ['pba','INTERIOR','PRIMERA','TERCERA']:
                provincias_habilitadas.append(
                    html.Div(dcc.Link(
                                textosLEG_PBA_2[provincia],
                                href="/especiales_LEG_PBA_2/" + provincia
                                     )
                            )
                )


            return html.Div( children  = html.Div(#className="slides movimiento slider slider-1 content slides movimiento",
                            className="slides slider-1 slider slider-1",
                                    children=[
                                        html.Div(
                                            className="content-txt",
                                            children=provincias_habilitadas,
                                            style={'margin-top':'20%', 'margin-bottom':'10%'}
                                        )
                                    ]
                            ),id="slider_LEG_PBA_2",
                            className='slider',
                            )

        else:
            provincia = pathname.split('/')[-1]

        return encuesta

@app.callback(Output('LEG_PBA_2_encuestas', 'children'),
    [Input('url', 'pathname')])
def update_encuesta(pathname):
    provincia = pathname.split('/')[-1]

    return html.Div([
        html.Div(
            className='section-header pba',
            children=[
                html.Div(
                    className='section-breadcrumb',
                    children=[
                        html.P(children=textos['breadcrumb']),
                    ]
                ),
                html.H2(children=textosLEG_PBA_2.get("titulo")),
                html.P(children=textosLEG_PBA_2.get("ambito_" + provincia)),
                # html.P(children=textosSANTIAGO['bajada_encuesta_especial2'], className="bold"),
                html.P(children=textosLEG_PBA_2['fecha']),
            ]
        ),

        dcc.Tabs(
            id="LEG_PBA_2-tabs-with-classes",
            value='tab-1',
            parent_className='custom-tabs',
            className='container custom-tabs-container',
            children=tabs),
        html.Div(id='LEG_PBA_2-tabs-content-classes')
    ])


@app.callback(Output('LEG_PBA_2-tabs-content-classes', 'children'),
              [Input('url', 'pathname') ,Input('LEG_PBA_2-tabs-with-classes', 'value')])
def render_content(pathname, tab):
    provincia = pathname.split('/')[-1]

    if 'LEG_PBA_2' in pathname:
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
                                                            html.H3(children=textosLEG_PBA_2['tituloDato1']),
                                                            html.P(children=textosLEG_PBA_2['textoDato1']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosLEG_PBA_2['tituloDato2']),
                                                            html.P(children=textosLEG_PBA_2['textoDato2']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosLEG_PBA_2['tituloDato3']),
                                                            html.P(children=textosLEG_PBA_2.get('ambito_' + provincia, '')),
                                                        ]
                                                    ),
                                                    #html.Div(
                                                    #    className='dato no-border-bottom',
                                                    #    children=[
                                                    #        html.H3(children=textosLEG_PBA_2['tituloDato4']),
                                                    #        html.P(children=textosLEG_PBA_2['textoDato4']),
                                                    #    ]
                                                    #)
                                                ]
                                            ),
                                            html.Div(
                                                className='col-12 col-sm-4',
                                                children=[
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosLEG_PBA_2['tituloDato5']),
                                                            html.P(children=textosLEG_PBA_2['textoDato5']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosLEG_PBA_2['tituloDato6']),
                                                            html.P(children=textosLEG_PBA_2['textoDato6']),
                                                        ]
                                                    )

                                                ]
                                            ),
                                            html.Div(
                                                className='col-12 col-sm-4',
                                                children=[html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosLEG_PBA_2['tituloDato7']),
                                                            html.P(children=textosLEG_PBA_2.get(provincia + '_frase_tam', '')),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato ',
                                                        children=[
                                                            html.H3(children=textosLEG_PBA_2['tituloDato8']),
                                                            html.P(children=textosLEG_PBA_2['textoDato8']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato no-border-bottom',
                                                        children=[
                                                            html.H3(children=textosLEG_PBA_2['tituloDato9']),
                                                            html.P(children=textosLEG_PBA_2.get(provincia + '_error', '')),
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
                                            html.Label(children=textos['labelTema']),
                                            html.Div(
                                            id='LEG_PBA_2-div-tema-dropdown-container',
                                            children=[dropdown_tema,
                                                     # dropwdownOpciones(),
                                                      dcc.Checklist(options= [{'label': ' Con voto', 'value':'convoto'}],  value=["convoto"],style={'display': 'none'}, id='LEG_PBA_2_convoto_check')
                                                      ])
                                        ]
                                    ),
                                    html.Div(
                                        className='col-12 col-sm-3',
                                        children=[
                                            html.Label(children=textos['labelTarget']),
                                            dropdownTargetLEGISLATIVAS('selectTargetLEG_PBA_2')
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Div([
                        html.Div(
                            html.Div(id='LEG_PBA_2_content'),


                            className='content-container'
                        ),
                    ], className='container'),
                ]
            )

@app.callback(Output('selectTargetLEG_PBA_2', 'options'),
              [Input('url', 'pathname')]
              )
def update_options(pathname):
    if 'LEG_PBA_2' in pathname and 'portada' not in pathname:
        if pathname == "/especiales_LEG_PBA_2/pba":
            return opciones_LEGISLATIVAS
        else:
            return opciones_LEGISLATIVAS[:-7]




@app.callback(Output('LEG_PBA_2_select_preguntas', 'options'),
              [Input('url', 'pathname'),  Input('LEG_PBA_2_convoto_check', 'value')]
              )
def update_options(pathname, convoto):
    if 'LEG_PBA_2' in pathname and 'portada' not in pathname:
        provincia = pathname.split('/')[-1]

        cv = ['P11']
        if convoto:
            cv = ['P11']


        options = [{'label': 'Bloque completo', 'value': "todo"}] +  [{'label': textosLEG_PBA_2['label' + p], 'value': p} for p in cv]
        return options
    return []




@app.callback( Output('LEG_PBA_2_content', 'children'),
               [Input('url', 'pathname'), Input('LEG_PBA_2_select_preguntas', 'value'), Input('LEG_PBA_2_convoto_check', 'value')])
def update_content(pathname, pregunta, convoto):

    # Rellenar el contenido segun la pregunta seleccionada en el dropdown y si es con imputacion de indecisos o no

    if 'LEG_PBA_2' in pathname and 'portada' not in pathname:



        provincia = pathname.split('/')[-1]

        cv = ['P11']
        if convoto:
            cv = ['P11']


        if pregunta == "todo":
            return html.Div([html.Div(p) for k, p in layouts[provincia].items() if k in cv])
        else:
            return html.Div(layouts[provincia][pregunta])



