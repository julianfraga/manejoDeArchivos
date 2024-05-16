from especiales.TIGRE_6.apps.preguntasTIGRE_6 import filesTIGRE_6, preguntasQueNoVanTIGRE_6
from especiales.TIGRE_6.apps.txtTIGRE_6 import textosTIGRE_6
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.TIGRE_6.apps.txtTIGRE_6 import textosTIGRE_6
from config import *
from especiales.TIGRE_6.apps.configTIGRE_6 import *
from especiales.TIGRE_6.apps.bloquesTIGRE_6 import bloques_TIGRE_6
from graphs import *
from especiales.TIGRE_6.apps.txtTIGRE_6 import textosTIGRE_6 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_TIGRE_6.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosTIGRE_6["label" + pregunta]

orden_preguntas = []
for _ in bloques_TIGRE_6.values():
    orden_preguntas.extend(_)




# Layout

ps = {}

ps['P06'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP06'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP06'][0], 'selectTargetTIGRE_6', paletas['P06'], 'TIGRE_6-P06-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP06'][1], TIGRE_6P06, 'TIGRE_6-P06-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP06'][2], 'TIGRE_6-P06-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])

ps['P07'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP07'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP07'][0], 'selectTargetTIGRE_6', paletas['P07'], 'TIGRE_6-P07-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP07'][1], TIGRE_6P07, 'TIGRE_6-P07-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP07'][2], 'TIGRE_6-P07-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])
#
# ps['P08'] = html.Div([
#         html.H3(textosTIGRE_6['preguntaP08'], className='subtituloBloque'),
#         getBarplotOpcionesWithPalette(filesTIGRE_6['csvP08'][0], 'selectTargetTIGRE_6','selectOpcionesTIGRE_6',  paletas['P08'], 'TIGRE_6-P08-1', showticklabels=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesTIGRE_6['csvP08'][1], TIGRE_6P08, 'TIGRE_6-P08-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
#         html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesTIGRE_6['csvP08'][2], 'TIGRE_6-P08-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6),
# ])
#
# ps['P09'] = html.Div([
#         html.H3(textosTIGRE_6['preguntaP09'], className='subtituloBloque'),
#         getBarplotOpcionesWithPalette(filesTIGRE_6['csvP09'][0], 'selectTargetTIGRE_6','selectOpcionesTIGRE_6',  paletas['P09'], 'TIGRE_6-P09-1', showticklabels=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesTIGRE_6['csvP09'][1], TIGRE_6P09, 'TIGRE_6-P09-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
#         html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesTIGRE_6['csvP09'][2], 'TIGRE_6-P09-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6),
# ])
#
# ps['P10'] = html.Div([
#         html.H3(textosTIGRE_6['preguntaP10'], className='subtituloBloque'),
#         getBarplotOpcionesWithPalette(filesTIGRE_6['csvP10'][0], 'selectTargetTIGRE_6','selectOpcionesTIGRE_6',  paletas['P10'],'', 'TIGRE_6-P10-1', showticklabels=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesTIGRE_6['csvP10'][1], TIGRE_6P10, 'TIGRE_6-P10-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
#         html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesTIGRE_6['csvP10'][2], 'TIGRE_6-P10-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6),
# ])
#
# ps['P11'] = html.Div([
#         html.H3(textosTIGRE_6['preguntaP11'], className='subtituloBloque'),
#         getBarplotOpcionesWithPalette(filesTIGRE_6['csvP11'][0], 'selectTargetTIGRE_6','selectOpcionesTIGRE_6',  paletas['P11'], 'TIGRE_6-P11-1', showticklabels=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesTIGRE_6['csvP11'][1], TIGRE_6P11, 'TIGRE_6-P11-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
#         html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesTIGRE_6['csvP11'][2], 'TIGRE_6-P11-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6),
# ])
#
# ps['P12'] = html.Div([
#         html.H3(textosTIGRE_6['preguntaP12'], className='subtituloBloque'),
#         getBarplotOpcionesWithPalette(filesTIGRE_6['csvP12'][0], 'selectTargetTIGRE_6','selectOpcionesTIGRE_6',  paletas['P12'], 'TIGRE_6-P12-1', showticklabels=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesTIGRE_6['csvP12'][1], TIGRE_6P12, 'TIGRE_6-P12-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
#         html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesTIGRE_6['csvP12'][2], 'TIGRE_6-P12-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6),
# ])





ps['P13'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP13'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP13'][0], 'selectTargetTIGRE_6', paletas['P13'], 'TIGRE_6-P13-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP13'][1], TIGRE_6P13, 'TIGRE_6-P13-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP13'][2], 'TIGRE_6-P13-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])

ps['P14'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP14'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP14'][0], 'selectTargetTIGRE_6', paletas['P14'], 'TIGRE_6-P14-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP14'][1], TIGRE_6P14, 'TIGRE_6-P14-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP14'][2], 'TIGRE_6-P14-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])

ps['P15'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP15'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP15'][0], 'selectTargetTIGRE_6', paletas['P15'], 'TIGRE_6-P15-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP15'][1], TIGRE_6P15, 'TIGRE_6-P15-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP15'][2], 'TIGRE_6-P15-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])
ps['P16'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP16'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP16'][0], 'selectTargetTIGRE_6', paletas['P16'], 'TIGRE_6-P16-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP16'][1], TIGRE_6P16, 'TIGRE_6-P16-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP16'][2], 'TIGRE_6-P16-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])





ps['P17'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP17'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP17'][0], 'selectTargetTIGRE_6', paletas['P17'], 'TIGRE_6-P17-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP17'][1], TIGRE_6P17, 'TIGRE_6-P17-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP17'][2], 'TIGRE_6-P17-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])

ps['P19'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP19'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP19'][0], 'selectTargetTIGRE_6', paletas['P19'], 'TIGRE_6-P19-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP19'][1], TIGRE_6P19, 'TIGRE_6-P19-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP19'][2], 'TIGRE_6-P19-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])
ps['P20'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP20'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP20'][0], 'selectTargetTIGRE_6', paletas['P20'], 'TIGRE_6-P20-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP20'][1], TIGRE_6P20, 'TIGRE_6-P20-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP20'][2], 'TIGRE_6-P20-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])
ps['P21'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP21'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP21'][0], 'selectTargetTIGRE_6', paletas['P21'], 'TIGRE_6-P21-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP21'][1], TIGRE_6P21, 'TIGRE_6-P21-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP21'][2], 'TIGRE_6-P21-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])
ps['P22'] = html.Div([
        html.H3(textosTIGRE_6['preguntaP22'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE_6['csvP22'][0], 'selectTargetTIGRE_6', paletas['P22'], 'TIGRE_6-P22-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE_6['csvP22'][1], TIGRE_6P22, 'TIGRE_6-P22-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE_6['csvP22'][2], 'TIGRE_6-P22-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
])





# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosTIGRE_6['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesTIGRE_6['csvPXX'][0], 'selectTargetTIGRE_6', paletas['PXX'], 'TIGRE_6-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesTIGRE_6['csvPXX'][1], TIGRE_6PXX, 'TIGRE_6-PXX-2', 'selectTargetTIGRE_6', opcionesDePreguntasInicial=3),
#         html.H3(textosTIGRE_6['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesTIGRE_6['csvPXX'][2], 'TIGRE_6-PXX-3', 'selectTargetTIGRE_6', '', preguntasQueNoVan = preguntasQueNoVanTIGRE_6, reorder=True, crucesDict = crucesDictTIGRE_6)
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
         Input("selectOpciones", 'value'), ])
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

        hbarplot  = plot_hbarplot(csv_hbp, df_hbp, candidato, callbackInputTarget, 'selectOpciones', opinionColorDict, name, opcionesDePreguntasInicial = opcionesDePreguntasInicial)
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


imagen = plots(filesTIGRE_6['csv_imagen'][0],filesTIGRE_6['csv_imagen'][3], filesTIGRE_6['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetTIGRE_6',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanTIGRE_6, name='TIGRE_6-Comparativo', crucesDict = crucesDictTIGRE_6, files=filesTIGRE_6, tracking='TIGRE_6'),



ps['imagen1'] = html.Div([
                html.H3(textosTIGRE_6['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosTIGRE_6['seleccioneFigura']),
                getStackedBarplot(filesTIGRE_6['csv_imagen'][0], 'selectTargetTIGRE_6', 'selectOpciones', opinionColorDict, 'TIGRE_6-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosTIGRE_6['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosTIGRE_6['seleccioneFigura']),
                getStackedBarplot(filesTIGRE_6['csv_imagen'][1], 'selectTargetTIGRE_6', 'selectOpciones', opinionColorDict, 'TIGRE_6-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosTIGRE_6['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosTIGRE_6['seleccioneFigura']),
                getStackedBarplot(filesTIGRE_6['csv_imagen'][2], 'selectTargetTIGRE_6', 'selectOpciones', opinionColorDict, 'TIGRE_6-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





