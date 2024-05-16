from especiales.MERLO_3.apps.preguntasMERLO_3 import filesMERLO_3, preguntasQueNoVanMERLO_3
from especiales.MERLO_3.apps.txtMERLO_3 import textosMERLO_3
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.MERLO_3.apps.txtMERLO_3 import textosMERLO_3
from config import *
from especiales.MERLO_3.apps.configMERLO_3 import *
from especiales.MERLO_3.apps.bloquesMERLO_3 import bloques_MERLO_3
from graphs import *
from especiales.MERLO_3.apps.txtMERLO_3 import textosMERLO_3 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_MERLO_3.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosMERLO_3["label" + pregunta]

orden_preguntas = []
for _ in bloques_MERLO_3.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

# ps['PXX'] = html.Div([
#         html.H3(textosMERLO_3['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_3['csvPXX'][0], 'selectTargetMERLO_3', paletas['PXX'], 'MERLO_3-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_3['csvPXX'][1], MERLO_3PXX, 'MERLO_3-PXX-2', 'selectTargetMERLO_3', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_3['csvPXX'][2], 'MERLO_3-PXX-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, crucesDict = crucesDictMERLO_3)
# ])


ps['P06'] = html.Div([

        html.H3(textosMERLO_3['preguntaP06'], className='subtituloBloque'),

        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP06'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P06'], 'MERLO_3-P06-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP06'][2], 'MERLO_3-P06-3', 'selectTargetMERLO_3', 'selectOpciones_Merlo2', preguntasQueNoVan = preguntasQueNoVanMERLO_3,reorder=False, crucesDict = crucesDictMERLO_3,  opcionesDePreguntasInicial = 4)
])

ps['P07'] = html.Div([
        html.H3(textosMERLO_3['preguntaP07'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP07'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P07'], 'MERLO_3-P07-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP07'][2], 'MERLO_3-P07-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False, crucesDict = crucesDictMERLO_3,  opcionesDePreguntasInicial = 4)
])

ps['P08'] = html.Div([
        html.H3(textosMERLO_3['preguntaP08'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP08'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P08'], 'MERLO_3-P08-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP08'][2], 'MERLO_3-P08-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P09'] = html.Div([
        html.H3(textosMERLO_3['preguntaP09'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP09'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P09'], 'MERLO_3-P09-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP09'][2], 'MERLO_3-P09-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P10'] = html.Div([
        html.H3(textosMERLO_3['preguntaP10'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP10'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P10'], 'MERLO_3-P10-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP10'][2], 'MERLO_3-P10-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P11'] = html.Div([
        html.H3(textosMERLO_3['preguntaP11'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP11'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P11'], 'MERLO_3-P11-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP11'][2], 'MERLO_3-P11-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P12'] = html.Div([
        html.H3(textosMERLO_3['preguntaP12'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP12'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P12'], 'MERLO_3-P12-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP12'][2], 'MERLO_3-P12-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P13'] = html.Div([
        html.H3(textosMERLO_3['preguntaP13'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP13'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P13'], 'MERLO_3-P13-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP13'][2], 'MERLO_3-P13-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])






ps['P14'] = html.Div([
        html.H3(textosMERLO_3['preguntaP14'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP14'][0], 'selectTargetMERLO_3', paletas['P14'], 'MERLO_3-P14-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP14'][2], 'MERLO_3-P14-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P15'] = html.Div([
        html.H3(textosMERLO_3['preguntaP15'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP15'][0], 'selectTargetMERLO_3', paletas['P15'], 'MERLO_3-P15-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP15'][2], 'MERLO_3-P15-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P16'] = html.Div([
        html.H3(textosMERLO_3['preguntaP16'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP16'][0], 'selectTargetMERLO_3', paletas['P16'], 'MERLO_3-P16-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP16'][2], 'MERLO_3-P16-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])
ps['P17'] = html.Div([
        html.H3(textosMERLO_3['preguntaP17'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP17'][0], 'selectTargetMERLO_3', paletas['P17'], 'MERLO_3-P17-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP17'][2], 'MERLO_3-P17-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P18'] = html.Div([
        html.H3(textosMERLO_3['preguntaP18'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP18'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P18'], 'MERLO_3-P18-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),

        getCrucesOpinionStacked(filesMERLO_3['csvP18'][2], 'MERLO_3-P18-3', 'selectTargetMERLO_3', "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P19'] = html.Div([
        html.H3(textosMERLO_3['preguntaP19'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_3['csvP19'][0], 'selectTargetMERLO_3','selectOpciones_Merlo2', paletas['P19'], 'MERLO_3-P19-1', showticklabels=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_3['csvP19'][2], 'MERLO_3-P19-3', 'selectTargetMERLO_3',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P20'] = html.Div([
        html.H3(textosMERLO_3['preguntaP20'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP20'][0], 'selectTargetMERLO_3', paletas['P20'], 'MERLO_3-P20-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP20'][2], 'MERLO_3-P20-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P21'] = html.Div([
        html.H3(textosMERLO_3['preguntaP21'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP21'][0], 'selectTargetMERLO_3', paletas['P21'], 'MERLO_3-P21-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP21'][2], 'MERLO_3-P21-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P22'] = html.Div([
        html.H3(textosMERLO_3['preguntaP22'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP22'][0], 'selectTargetMERLO_3', paletas['P22'], 'MERLO_3-P22-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP22'][2], 'MERLO_3-P22-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P24'] = html.Div([
        html.H3(textosMERLO_3['preguntaP24'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP24'][0], 'selectTargetMERLO_3', paletas['P24'], 'MERLO_3-P24-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP24'][2], 'MERLO_3-P24-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P25'] = html.Div([
        html.H3(textosMERLO_3['preguntaP25'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP25'][0], 'selectTargetMERLO_3', paletas['P25'], 'MERLO_3-P25-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP25'][2], 'MERLO_3-P25-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P26'] = html.Div([
        html.H3(textosMERLO_3['preguntaP26'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP26'][0], 'selectTargetMERLO_3', paletas['P26'], 'MERLO_3-P26-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP26'][2], 'MERLO_3-P26-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])

ps['P27'] = html.Div([
        html.H3(textosMERLO_3['preguntaP27'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_3['csvP27'][0], 'selectTargetMERLO_3', paletas['P27'], 'MERLO_3-P27-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_3['csvP27'][2], 'MERLO_3-P27-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, reorder=False,  crucesDict = crucesDictMERLO_3)
])



# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosMERLO_3['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_3['csvPXX'][0], 'selectTargetMERLO_3', paletas['PXX'], 'MERLO_3-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_3['csvPXX'][1], MERLO_3PXX, 'MERLO_3-PXX-2', 'selectTargetMERLO_3', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_3['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_3['csvPXX'][2], 'MERLO_3-PXX-3', 'selectTargetMERLO_3', '', preguntasQueNoVan = preguntasQueNoVanMERLO_3, crucesDict = crucesDictMERLO_3)
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


imagen = plots(filesMERLO_3['csv_imagen'][0],filesMERLO_3['csv_imagen'][3], filesMERLO_3['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetMERLO_3',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanMERLO_3, name='MERLO_3-Comparativo',crucesDict = crucesDictMERLO_3, files=filesMERLO_3, tracking='MERLO_3'),



ps['imagen1'] = html.Div([
                html.H3(textosMERLO_3['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_3['seleccioneFigura']),
                getStackedBarplot(filesMERLO_3['csv_imagen'][0], 'selectTargetMERLO_3', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_3-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosMERLO_3['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_3['seleccioneFigura']),
                getStackedBarplot(filesMERLO_3['csv_imagen'][1], 'selectTargetMERLO_3', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_3-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosMERLO_3['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_3['seleccioneFigura']),
                getStackedBarplot(filesMERLO_3['csv_imagen'][2], 'selectTargetMERLO_3', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_3-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





