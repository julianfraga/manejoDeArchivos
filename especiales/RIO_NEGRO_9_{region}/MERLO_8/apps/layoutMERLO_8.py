from especiales.MERLO_8.apps.preguntasMERLO_8 import filesMERLO_8, preguntasQueNoVanMERLO_8
from especiales.MERLO_8.apps.txtMERLO_8 import textosMERLO_8
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.MERLO_8.apps.txtMERLO_8 import textosMERLO_8
from config import *
from especiales.MERLO_8.apps.configMERLO_8 import *
from especiales.MERLO_8.apps.bloquesMERLO_8 import bloques_MERLO_8
from graphs import *
from especiales.MERLO_8.apps.txtMERLO_8 import textosMERLO_8 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
ps = {}
tiene_opciones = {'P27': False, 'P41': False, 'P31': False, 'P37': False, 'P19': False, 'P29': False, 'P30': False,
                  'P36': True, 'P11': False, 'P35': True, 'P32': False, 'P18': False, 'P09': False, 'P39': False, 'P07': False, 'P33': False, 'P34': False, 'P28': False, 'P40': False, 'P26': False, 'P20': False}
PS = ['P27', 'P41', 'P31', 'P37', 'P19', 'P29', 'P30', 'P36', 'P11', 'P35', 'P32', 'P18', 'P09', 'P39', 'P07', 'P33', 'P34', 'P28', 'P40', 'P26', 'P20']

for bloque in bloques_MERLO_8.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosMERLO_8["label" + pregunta]
        p = pregunta
        if p in PS:
            if not tiene_opciones.get(p, True):
                ps[p] = html.Div([
                    html.H3(textosMERLO_8['pregunta' + p], className='subtituloBloque'),
                    getBarplotWithPalette(filesMERLO_8['csv' + p][0], 'selectTargetMERLO_8',
                                          paletas[p], f'MERLO_8-{p}-1', showticklabels=False, reverse=False),

                    html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
                    getCrucesStacked(filesMERLO_8['csv' + p][2], f'MERLO_8-{p}-3',
                                     'selectTargetMERLO_8', '',
                                     preguntasQueNoVan=preguntasQueNoVanMERLO_8, reorder=False,
                                     crucesDict=crucesDictMERLO_8)
                ])
            else:
                ps[p] = html.Div([

                    html.H3(textosMERLO_8['pregunta' + p], className='subtituloBloque'),

                    getHBarplotOpcionesWithPalette(filesMERLO_8['csv' + p][0], 'selectTargetMERLO_8',
                                                   'selectOpciones_Merlo2', paletas[p], f'MERLO_8-{p}-1',
                                                   showticklabels=False),
                    html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
                    getCrucesOpinionStacked(filesMERLO_8['csv' + p][2], f'MERLO_8-P{p}-3', 'selectTargetMERLO_8',
                                            'selectOpciones_Merlo2', preguntasQueNoVan=preguntasQueNoVanMERLO_8,
                                            reorder=False, crucesDict=crucesDictMERLO_8, opcionesDePreguntasInicial=4)
                ])


orden_preguntas = []
for _ in bloques_MERLO_8.values():
    orden_preguntas.extend(_)


# Layout






#
#
# # ps['PXX'] = html.Div([
# #         html.H3(textosMERLO_8['preguntaPXX'], className='subtituloBloque'),
# #         getBarplotWithPalette(filesMERLO_8['csvPXX'][0], 'selectTargetMERLO_8', paletas['PXX'], 'MERLO_8-PXX-1', showticklabels=False, reverse=False),
# #         #html.H3(),
# #         #getTimeSeriesLineplot(filesMERLO_8['csvPXX'][1], MERLO_8PXX, 'MERLO_8-PXX-2', 'selectTargetMERLO_8', opcionesDePreguntasInicial=3),
# #         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
# #         getCrucesStacked(filesMERLO_8['csvPXX'][2], 'MERLO_8-PXX-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, crucesDict = crucesDictMERLO_8)
# # ])
#
# ps[p] = html.Div([
#         html.H3(textosMERLO_8['preguntaP07'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP07'][0], 'selectTargetMERLO_8', paletas[p], 'MERLO_8-P07-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_8['csvP07'][1], MERLO_8P07, 'MERLO_8-P07-2', 'selectTargetMERLO_8', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP07'][2], 'MERLO_8-P07-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False, crucesDict = crucesDictMERLO_8)
# ])
# ps['P09'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP09'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP09'][0], 'selectTargetMERLO_8', paletas['P09'], 'MERLO_8-P09-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_8['csvP09'][1], MERLO_8P09, 'MERLO_8-P09-2', 'selectTargetMERLO_8', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP09'][2], 'MERLO_8-P09-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False, crucesDict = crucesDictMERLO_8)
# ])
# ps['P11'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP11'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP11'][0], 'selectTargetMERLO_8', paletas['P11'], 'MERLO_8-P11-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_8['csvP11'][1], MERLO_8P11, 'MERLO_8-P11-2', 'selectTargetMERLO_8', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP11'][2], 'MERLO_8-P11-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False, crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P13'] = html.Div([
#
#         html.H3(textosMERLO_8['preguntaP13'], className='subtituloBloque'),
#
#         getHBarplotOpcionesWithPalette(filesMERLO_8['csvP13'][0], 'selectTargetMERLO_8','selectOpciones_Merlo2', paletas['P13'], 'MERLO_8-P13-1', showticklabels=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesMERLO_8['csvP13'][2], 'MERLO_8-P13-3', 'selectTargetMERLO_8', 'selectOpciones_Merlo2', preguntasQueNoVan = preguntasQueNoVanMERLO_8,reorder=False, crucesDict = crucesDictMERLO_8,  opcionesDePreguntasInicial = 4)
# ])
#
# ps['P14'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP14'], className='subtituloBloque'),
#         getHBarplotOpcionesWithPalette(filesMERLO_8['csvP14'][0], 'selectTargetMERLO_8','selectOpciones_Merlo2', paletas['P14'], 'MERLO_8-P14-1', showticklabels=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesMERLO_8['csvP14'][2], 'MERLO_8-P14-3', 'selectTargetMERLO_8',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False, crucesDict = crucesDictMERLO_8,  opcionesDePreguntasInicial = 4)
# ])
#
#
#
# ps['P15'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP15'], className='subtituloBloque'),
#         getHBarplotOpcionesWithPalette(filesMERLO_8['csvP15'][0], 'selectTargetMERLO_8','selectOpciones_Merlo2', paletas['P15'], 'MERLO_8-P15-1', showticklabels=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesMERLO_8['csvP15'][2], 'MERLO_8-P15-3', 'selectTargetMERLO_8',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P15'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP15'], className='subtituloBloque'),
#         getHBarplotOpcionesWithPalette(filesMERLO_8['csvP15'][0], 'selectTargetMERLO_8','selectOpciones_Merlo2', paletas['P15'], 'MERLO_8-P15-1', showticklabels=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesMERLO_8['csvP15'][2], 'MERLO_8-P15-3', 'selectTargetMERLO_8',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
#
#
#
#
#
# ps['P31'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP31'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP31'][0], 'selectTargetMERLO_8', paletas['P31'], 'MERLO_8-P31-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP31'][2], 'MERLO_8-P31-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P32'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP32'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP32'][0], 'selectTargetMERLO_8', paletas['P32'], 'MERLO_8-P32-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP32'][2], 'MERLO_8-P32-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P33'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP33'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP33'][0], 'selectTargetMERLO_8', paletas['P33'], 'MERLO_8-P33-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP33'][2], 'MERLO_8-P33-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
# ps['P34'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP34'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP34'][0], 'selectTargetMERLO_8', paletas['P34'], 'MERLO_8-P34-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP34'][2], 'MERLO_8-P34-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P35'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP35'], className='subtituloBloque'),
#         getHBarplotOpcionesWithPalette(filesMERLO_8['csvP35'][0], 'selectTargetMERLO_8','selectOpciones_Merlo2', paletas['P35'], 'MERLO_8-P35-1', showticklabels=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#
#         getCrucesOpinionStacked(filesMERLO_8['csvP35'][2], 'MERLO_8-P35-3', 'selectTargetMERLO_8', "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P36'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP36'], className='subtituloBloque'),
#         getHBarplotOpcionesWithPalette(filesMERLO_8['csvP36'][0], 'selectTargetMERLO_8','selectOpciones_Merlo2', paletas['P36'], 'MERLO_8-P36-1', showticklabels=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesMERLO_8['csvP36'][2], 'MERLO_8-P36-3', 'selectTargetMERLO_8',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
#
#
# ps['P37'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP37'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP37'][0], 'selectTargetMERLO_8', paletas['P37'], 'MERLO_8-P37-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP37'][2], 'MERLO_8-P37-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P39'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP39'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP39'][0], 'selectTargetMERLO_8', paletas['P39'], 'MERLO_8-P39-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP39'][2], 'MERLO_8-P39-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P40'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP40'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP40'][0], 'selectTargetMERLO_8', paletas['P40'], 'MERLO_8-P40-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP40'][2], 'MERLO_8-P40-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['P41'] = html.Div([
#         html.H3(textosMERLO_8['preguntaP41'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvP41'][0], 'selectTargetMERLO_8', paletas['P41'], 'MERLO_8-P41-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvP41'][2], 'MERLO_8-P41-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])
#
# ps['PSACAR_32'] = html.Div([
#         html.H3(textosMERLO_8['preguntaPSACAR_32'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvPSACAR_32'][0], 'selectTargetMERLO_8', paletas['PSACAR_32'], 'MERLO_8-PSACAR_32-1', showticklabels=False, reverse=False),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvPSACAR_32'][2], 'MERLO_8-PSACAR_32-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, reorder=False,  crucesDict = crucesDictMERLO_8)
# ])



# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosMERLO_8['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_8['csvPXX'][0], 'selectTargetMERLO_8', paletas['PXX'], 'MERLO_8-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_8['csvPXX'][1], MERLO_8PXX, 'MERLO_8-PXX-2', 'selectTargetMERLO_8', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_8['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_8['csvPXX'][2], 'MERLO_8-PXX-3', 'selectTargetMERLO_8', '', preguntasQueNoVan = preguntasQueNoVanMERLO_8, crucesDict = crucesDictMERLO_8)
# ])




# Parche del grafico de imagenes por no haber time series
from graph_imagen import *



def plot_cruces(candidato,df_cruces,files, name, preguntasQueNoVan, callbackInputTarget, crucesDict = crucesDict,opcionesDePreguntasInicial='', reorder=True):
    filesCandidato = files

    tracking = get_tracking(list(files.values())[0][0])


    if reorder:
        orden_cruces = orden[tracking]
    else:
        orden_cruces = df_cruces['var'].unique().tolist()

    xaxisTitle = ''
    yaxisTitle = ''
    opciones = {'_6opc': 0, '_4opc': 1, '_5opc': 0, '_3opc': 1}
    cruces_graph_id = 'enhanced-graph-cruces-'+ name + candidato.replace(" ", '_')
    layout = go.Layout(
        xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
               'showticklabels': False, 'visible': False},
        yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
               'showticklabels': False, },
        barmode='stack', template="plotly_white")



    cruces_component = html.Div([
        dcc.Dropdown(
            id='selectCruce' + name + candidato,
            options=[{'label': crucesDict[i][0], 'value': i} for i in reorder_cruces(df_cruces['var'].unique(), orden_cruces)],
            placeholder='Seleccioná una pregunta para ver el cruce',
            clearable=False,
            searchable=False,
            optionHeight=50,
        ),
        dcc.Graph(
            figure=go.Figure(layout=layout),
            # style={'height': crucesHeight},
            id=cruces_graph_id
            ),
        ])


    @app.callback(
        Output(cruces_graph_id, 'figure'),
        [Input('selectCruce' + name + candidato, 'value'),
         Input(callbackInputTarget, 'value'),
         Input("selectOpciones_Merlo2", 'value'), ])
    def update_figure(selected_cruce, selected_target, selected_opciones):

        if selected_target != 'Todos':
            layout = go.Layout(
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
                       'showticklabels': False},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
                       'showticklabels': False},
                barmode='stack',
                annotations=[{
                    'x': 0,
                    'y': -100,
                    'xref': 'x',
                    'yref': 'y',
                    'text': 'Por favor seleccione "Todos"<br>los targets para visualizar el cruce',
                    'showarrow': False,
                    'ax': 0,
                    'ay': -100,
                    'font': dict(size=25),
                }]
            )
            return {'data': [go.Bar()], 'layout': layout}
        if selected_opciones == '_2opc':
            layout = go.Layout(
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
                       'showticklabels': False},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
                       'showticklabels': False},
                barmode='stack',
                annotations=[{
                    'x': 0,
                    'y': -100,
                    'xref': 'x',
                    'yref': 'y',
                    'text': 'Seleccioná 4 o 6 opciones<br>para visualizar el cruce',
                    'showarrow': False,
                    'ax': 0,
                    'ay': -100,
                    'font': dict(size=25),
                }]
            )
            return {'data': [go.Bar()], 'layout': layout}

        if selected_cruce:
            # Update dropdown dinamically
            if not opcionesDePreguntasInicial is None:
                df = pd.read_csv(filesCandidato[candidato][opciones[selected_opciones]])
            else:
                df = pd.read_csv(filesCandidato[candidato][0])
            df = df[~df['var'].isin(preguntasQueNoVan)]
            layout = go.Layout(
                height=800,
                legend=dict(orientation='h', x=0, y=-0.2),
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle},
                barmode='stack',
                # margin=go.layout.Margin(b=200),
            )

            palette = crucesDict[selected_cruce][1]
            dfloc = df.loc[df['var'] == selected_cruce].drop('var', axis=1).set_index('categoria').iloc[::-1]
            data = []
            # Fix for variable ammount of categories.
            if palette is None:
                clases = dfloc.index.tolist()
                if "No sabe" in clases:  # Si No sabe está presente lo ponemos al final
                    clases.remove("No sabe")
                    clases.append("No sabe")

                palette = list2dictPalette([clase for clase in clases], diverging)

            iclase = 0
            for i in dfloc.index:
                # Fix for variable ammount of categories.
                if type(palette).__name__ == "_ColorPalette":
                    color = palette[iclase]
                    iclase = iclase + 1
                else:
                    color = palette[i]

                trace = go.Bar(x=dfloc.columns,
                               y=dfloc.loc[i],
                               name='<br>'.join(textwrap.wrap(i, width=wrapWidht)),
                               marker={'color': color})
                data.append(trace)

            return {'data': data, 'layout': layout}
        else:
            layout = go.Layout(
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
                       'showticklabels': False},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
                       'showticklabels': False},
                barmode='stack',
            )
            return {'data': [go.Bar()], 'layout': layout}
    return cruces_component



# def get_tracking(csv):
#     if "tracking" in csv:
#         return csv.split("/")[1]
#     else:
#         return csv.split("/")[2]

def plots(csv_hbp,csv_ts, csv_cruces, callbackInputTarget = '', crucesDict = crucesDict, opcionesDePreguntasInicial = 4, preguntasQueNoVan = "", preguntasDeshabilitadas = '', name = '', tracking='Nacional', files=''):
    tracking = get_tracking(csv_hbp)


    suf = 'conGalmarini' if 'conGalmarini' in csv_hbp else ''

    if not opcionesDePreguntasInicial is None:
        df_hbp = pd.read_csv(insertString(csv_hbp, '_' + str(opcionesDePreguntasInicial) + 'opc', -4))
    else:
        df_hbp = pd.read_csv(csv_hbp)




    df_cruces = pd.read_csv(csv_cruces)
    # removemos las variables de control interno: cuan frecuente es que responda / esá interesado en que lo contactemos
    df_cruces = df_cruces[~df_cruces['var'].isin(preguntasQueNoVan)]


    candidatos = df_hbp.clase.unique().tolist()

    selector_candidato = dcc.Dropdown(
        options=[{'label':'Todos', 'value':'todos'}] + [{'value':candidato, 'label':candidato} for candidato in candidatos],
        value='todos',
        #placeholder="Selección por target",
        id=tracking + 'select_candidato',
        clearable=False,
        searchable=False
    )

    candidatos_plots = {}
    for candidato in candidatos:
        df_cruces = pd.read_csv(files[candidato][-1])
        df_cruces = df_cruces[~df_cruces['var'].isin(preguntasQueNoVan)]
        plots = []

        hbarplot  = plot_hbarplot(csv_hbp, df_hbp, candidato, callbackInputTarget, 'selectOpciones_Merlo2', opinionColorDict, name, opcionesDePreguntasInicial = opcionesDePreguntasInicial)
        cruces_component = plot_cruces(candidato, df_cruces, files, name, callbackInputTarget = callbackInputTarget, crucesDict = crucesDict,  preguntasQueNoVan = preguntasQueNoVan,opcionesDePreguntasInicial = opcionesDePreguntasInicial, reorder=False)
        plots.append(
            html.Div(id = tracking + candidato + "_imagen_div"+ suf,
            children = [html.H4(candidato), hbarplot, html.H3(), html.H3(), cruces_component]
                     )
        )
        candidatos_plots[candidato] = html.Div(plots)
        componentes = html.Div(children=[selector_candidato,html.H3(),
                                         html.Div(
                                         html.Div(list(candidatos_plots.values())
                                             , id=tracking + 'plots_candidatos_div_ss' + suf), id='plots_candidatos_div')])

    @app.callback(
        [Output(tracking + candidato + "_imagen_div" + suf, 'style') for candidato in candidatos]
        ,[Input(tracking + 'select_candidato', 'value')])
    def update_candidato(candidato):
        c = candidato
        uid = {candidato: i for i, candidato in enumerate(candidatos)}
        if candidato == 'todos':
           salida = html.Div(list(candidatos_plots.values()))
           estilo = [{'display':'inline'}] * len(candidatos)
        else:
           salida = html.Div(candidatos_plots[candidato])
           estilo = [{'display': 'none'}] * len(candidatos)
           estilo[uid[c]] = {'visible': 'inline'}
        return estilo
    return componentes


imagen = plots(filesMERLO_8['csv_imagen'][0],filesMERLO_8['csv_imagen'][3], filesMERLO_8['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetMERLO_8',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanMERLO_8, name='MERLO_8-Comparativo',crucesDict = crucesDictMERLO_8, files=filesMERLO_8, tracking='MERLO_8'),



ps['imagen1'] = html.Div([
                html.H3(textosMERLO_8['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_8['seleccioneFigura']),
                getStackedBarplot(filesMERLO_8['csv_imagen'][0], 'selectTargetMERLO_8', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_8-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosMERLO_8['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_8['seleccioneFigura']),
                getStackedBarplot(filesMERLO_8['csv_imagen'][1], 'selectTargetMERLO_8', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_8-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosMERLO_8['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_8['seleccioneFigura']),
                getStackedBarplot(filesMERLO_8['csv_imagen'][2], 'selectTargetMERLO_8', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_8-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





