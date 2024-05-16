from graphs import *
import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from flask_login import logout_user, current_user
from login import login_failed
from especiales.PASO_BA_4.apps.config import *
from app import app
from txt import textos
from permisos import *
import dash_bootstrap_components as dbc
import pandas as pd
from especiales.PASO_BA_4.apps.txtPASO_BA_4 import textosPASO_BA_4
from especiales.PASO_BA_4.apps.layout import layouts, filesPASO_BA_4, preguntas, preguntas_provincias


# Esta pagina ademas de las tipicas paginas de la portada tiene toda una parte extra para cargar lo que sería el HOME
# este tracking (los links a las distintas sub encuestas)


# Dropdown con las distintas preguntas ( y transferencia en este caso)
_preguntas = ['P09_convoto','P09_sinvoto']
dropdown_tema = dcc.Dropdown(  searchable=False, clearable=False, id='PASO_BA_4_select_preguntas',
                                                                options= [{'label': 'Bloque completo', 'value': "todo"}] +
                                                                         [{'label': textosPASO_BA_4['label' + p],  'value':   p} for p in  _preguntas]
                               ,
                                                                value='todo')

layout = html.Div(
		children=[
			html.Div(
			id="content_PASO_BA_4",
            #className='slider',

		),
		html.Div(
	        className='footer m-t-0',
	        children=[
	            html.P(children=textos['footer']),  html.Div("start", id='collapse_tmp', style={'display':'none'})
	        ]
	    )
    ])




encuesta = html.Div(id='PASO_BA_4_encuestas')

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



@app.callback(Output('content_PASO_BA_4', 'children'),
              [Input('url', 'pathname')])
def display_slides(pathname):

    if current_user.is_authenticated:
        if pathname == '/especiales_PASO_BA_4/portada':

            provincias_habilitadas = [html.H1("Provincias")]
            for provincia in ['pba','INTERIOR','PRIMERA','TERCERA']:
                provincias_habilitadas.append(
                    html.Div(dcc.Link(
                                textosPASO_BA_4[provincia],
                                href="/especiales_PASO_BA_4/" + provincia
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
                            ),id="slider_PASO_BA_4",
                            className='slider',
                            )

        else:
            provincia = pathname.split('/')[-1]

        return encuesta

@app.callback(Output('PASO_BA_4_encuestas', 'children'),
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
                html.H2(children=textosPASO_BA_4.get("titulo")),
                html.P(children=textosPASO_BA_4.get("ambito_" + provincia)),
                # html.P(children=textosSANTIAGO['bajada_encuesta_especial2'], className="bold"),
                html.P(children=textosPASO_BA_4['fecha']),
            ]
        ),

        dcc.Tabs(
            id="PASO_BA_4-tabs-with-classes",
            value='tab-1',
            parent_className='custom-tabs',
            className='container custom-tabs-container',
            children=tabs),
        html.Div(id='PASO_BA_4-tabs-content-classes')
    ])


@app.callback(Output('PASO_BA_4-tabs-content-classes', 'children'),
              [Input('url', 'pathname') ,Input('PASO_BA_4-tabs-with-classes', 'value')])
def render_content(pathname, tab):
    provincia = pathname.split('/')[-1]

    if 'PASO_BA_4' in pathname:
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
                                                            html.H3(children=textosPASO_BA_4['tituloDato1']),
                                                            html.P(children=textosPASO_BA_4['textoDato1']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosPASO_BA_4['tituloDato2']),
                                                            html.P(children=textosPASO_BA_4['textoDato2']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosPASO_BA_4['tituloDato3']),
                                                            html.P(children=textosPASO_BA_4.get('ambito_' + provincia, '')),
                                                        ]
                                                    ),
                                                    #html.Div(
                                                    #    className='dato no-border-bottom',
                                                    #    children=[
                                                    #        html.H3(children=textosPASO_BA_4['tituloDato4']),
                                                    #        html.P(children=textosPASO_BA_4['textoDato4']),
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
                                                            html.H3(children=textosPASO_BA_4['tituloDato5']),
                                                            html.P(children=textosPASO_BA_4['textoDato5']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosPASO_BA_4['tituloDato6']),
                                                            html.P(children=textosPASO_BA_4['textoDato6']),
                                                        ]
                                                    )

                                                ]
                                            ),
                                            html.Div(
                                                className='col-12 col-sm-4',
                                                children=[html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosPASO_BA_4['tituloDato7']),
                                                            html.P(children=textosPASO_BA_4.get(provincia + '_tam', '')),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato no-border-bottom',
                                                        children=[
                                                            html.H3(children=textosPASO_BA_4['tituloDato8']),
                                                            html.P(children=textosPASO_BA_4['textoDato8']),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className='dato',
                                                        children=[
                                                            html.H3(children=textosPASO_BA_4['tituloDato9']),
                                                            html.P(children=textosPASO_BA_4.get(provincia + '_error', '')),
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
                                            id='PASO_BA_4-div-tema-dropdown-container',
                                            children=[dropdown_tema,
                                                     # dropwdownOpciones(),
                                                      dcc.Checklist(options= [{'label': ' Con voto', 'value':'convoto'}],  value=["convoto"],style={'display': 'none'}, id='PASO_BA_4_convoto_check')
                                                      ])
                                        ]
                                    ),
                                    html.Div(
                                        className='col-12 col-sm-3',
                                        children=[
                                            html.Label(children=textos['labelTarget']),
                                            dropdownTargetNacional('selectTargetPASO_BA_4', cantidadDeOpciones = 13)
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Div([
                        html.Div(
                            html.Div(id='PASO_BA_4_content'),


                            className='content-container'
                        ),
                    ], className='container'),
                ]
            )

@app.callback(Output('PASO_BA_4_select_preguntas', 'options'),
              [Input('url', 'pathname'),  Input('PASO_BA_4_convoto_check', 'value')]
              )
def update_options(pathname, convoto):
    if 'PASO_BA_4' in pathname and 'portada' not in pathname:
        provincia = pathname.split('/')[-1]

        cv = ['P09_sinvoto']
        if convoto:
            cv = ['P09_convoto']


        options = [{'label': 'Bloque completo', 'value': "todo"}] +  [{'label': textosPASO_BA_4['label' + p], 'value': p} for p in cv]
        return options
    return []




@app.callback( Output('PASO_BA_4_content', 'children'),
               [Input('url', 'pathname'), Input('PASO_BA_4_select_preguntas', 'value'), Input('PASO_BA_4_convoto_check', 'value')])
def update_content(pathname, pregunta, convoto):

    # Rellenar el contenido segun la pregunta seleccionada en el dropdown y si es con imputacion de indecisos o no

    if 'PASO_BA_4' in pathname and 'portada' not in pathname:



        provincia = pathname.split('/')[-1]

        cv = ['P09_sinvoto']
        if convoto:
            cv = ['P09_convoto']


        if pregunta == "todo":
            return html.Div([html.Div(p) for k, p in layouts[provincia].items() if k in cv])
        else:
            return html.Div(layouts[provincia][pregunta])



