from especiales.MERLO_5.apps.preguntasMERLO_5 import filesMERLO_5, preguntasQueNoVanMERLO_5
from especiales.MERLO_5.apps.txtMERLO_5 import textosMERLO_5
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.MERLO_5.apps.txtMERLO_5 import textosMERLO_5
from config import *
from especiales.MERLO_5.apps.configMERLO_5 import *
from especiales.MERLO_5.apps.bloquesMERLO_5 import bloques_MERLO_5
from graphs import *
from especiales.MERLO_5.apps.txtMERLO_5 import textosMERLO_5 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_MERLO_5.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosMERLO_5["label" + pregunta]

orden_preguntas = []
for _ in bloques_MERLO_5.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

# ps['PXX'] = html.Div([
#         html.H3(textosMERLO_5['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_5['csvPXX'][0], 'selectTargetMERLO_5', paletas['PXX'], 'MERLO_5-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_5['csvPXX'][1], MERLO_5PXX, 'MERLO_5-PXX-2', 'selectTargetMERLO_5', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_5['csvPXX'][2], 'MERLO_5-PXX-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, crucesDict = crucesDictMERLO_5)
# ])


ps['P07'] = html.Div([

        html.H3(textosMERLO_5['preguntaP07'], className='subtituloBloque'),

        getHBarploWithPalette(filesMERLO_5['csvP07'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P07'], 'MERLO_5-P07-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP07'][2], 'MERLO_5-P07-3', 'selectTargetMERLO_5', 'selectOpciones_Merlo2', preguntasQueNoVan = preguntasQueNoVanMERLO_5,reorder=False, crucesDict = crucesDictMERLO_5,  opcionesDePreguntasInicial = 4)
])

ps['P08'] = html.Div([
        html.H3(textosMERLO_5['preguntaP08'], className='subtituloBloque'),
        getHBarplotWithPalette(filesMERLO_5['csvP08'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P08'], 'MERLO_5-P08-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP08'][2], 'MERLO_5-P08-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False, crucesDict = crucesDictMERLO_5,  opcionesDePreguntasInicial = 4)
])

ps['P09'] = html.Div([
        html.H3(textosMERLO_5['preguntaP09'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP09'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P09'], 'MERLO_5-P09-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP09'][2], 'MERLO_5-P09-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P10'] = html.Div([
        html.H3(textosMERLO_5['preguntaP10'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP10'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P10'], 'MERLO_5-P10-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP10'][2], 'MERLO_5-P10-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P11'] = html.Div([
        html.H3(textosMERLO_5['preguntaP11'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP11'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P11'], 'MERLO_5-P11-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP11'][2], 'MERLO_5-P11-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P12'] = html.Div([
        html.H3(textosMERLO_5['preguntaP12'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP12'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P12'], 'MERLO_5-P12-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP12'][2], 'MERLO_5-P12-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P13'] = html.Div([
        html.H3(textosMERLO_5['preguntaP13'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP13'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P13'], 'MERLO_5-P13-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP13'][2], 'MERLO_5-P13-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P14'] = html.Div([
        html.H3(textosMERLO_5['preguntaP14'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP14'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P14'], 'MERLO_5-P14-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP14'][2], 'MERLO_5-P14-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])






ps['P15'] = html.Div([
        html.H3(textosMERLO_5['preguntaP15'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP15'][0], 'selectTargetMERLO_5', paletas['P15'], 'MERLO_5-P15-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP15'][2], 'MERLO_5-P15-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P16'] = html.Div([
        html.H3(textosMERLO_5['preguntaP16'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP16'][0], 'selectTargetMERLO_5', paletas['P16'], 'MERLO_5-P16-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP16'][2], 'MERLO_5-P16-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P17'] = html.Div([
        html.H3(textosMERLO_5['preguntaP17'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP17'][0], 'selectTargetMERLO_5', paletas['P17'], 'MERLO_5-P17-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP17'][2], 'MERLO_5-P17-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])
ps['P18'] = html.Div([
        html.H3(textosMERLO_5['preguntaP18'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP18'][0], 'selectTargetMERLO_5', paletas['P18'], 'MERLO_5-P18-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP18'][2], 'MERLO_5-P18-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P19'] = html.Div([
        html.H3(textosMERLO_5['preguntaP19'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP19'][0], 'selectTargetMERLO_5', paletas['P19'], 'MERLO_5-P19-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP19'][2], 'MERLO_5-P19-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P20'] = html.Div([
        html.H3(textosMERLO_5['preguntaP20'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP20'][0], 'selectTargetMERLO_5', paletas['P20'], 'MERLO_5-P20-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP20'][2], 'MERLO_5-P20-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])



ps['P21'] = html.Div([
        html.H3(textosMERLO_5['preguntaP21'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP21'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P21'], 'MERLO_5-P21-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),

        getCrucesOpinionStacked(filesMERLO_5['csvP21'][2], 'MERLO_5-P21-3', 'selectTargetMERLO_5', "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P22'] = html.Div([
        html.H3(textosMERLO_5['preguntaP22'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesMERLO_5['csvP22'][0], 'selectTargetMERLO_5','selectOpciones_Merlo2', paletas['P22'], 'MERLO_5-P22-1', showticklabels=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesMERLO_5['csvP22'][2], 'MERLO_5-P22-3', 'selectTargetMERLO_5',  "selectOpciones_Merlo2", preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P23'] = html.Div([
        html.H3(textosMERLO_5['preguntaP23'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP23'][0], 'selectTargetMERLO_5', paletas['P23'], 'MERLO_5-P23-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP23'][2], 'MERLO_5-P23-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P24'] = html.Div([
        html.H3(textosMERLO_5['preguntaP24'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP24'][0], 'selectTargetMERLO_5', paletas['P24'], 'MERLO_5-P24-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP24'][2], 'MERLO_5-P24-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P25'] = html.Div([
        html.H3(textosMERLO_5['preguntaP25'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP25'][0], 'selectTargetMERLO_5', paletas['P25'], 'MERLO_5-P25-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP25'][2], 'MERLO_5-P25-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P27'] = html.Div([
        html.H3(textosMERLO_5['preguntaP27'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP27'][0], 'selectTargetMERLO_5', paletas['P27'], 'MERLO_5-P27-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP27'][2], 'MERLO_5-P27-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P28'] = html.Div([
        html.H3(textosMERLO_5['preguntaP28'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP28'][0], 'selectTargetMERLO_5', paletas['P28'], 'MERLO_5-P28-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP28'][2], 'MERLO_5-P28-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P29'] = html.Div([
        html.H3(textosMERLO_5['preguntaP29'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP29'][0], 'selectTargetMERLO_5', paletas['P29'], 'MERLO_5-P29-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP29'][2], 'MERLO_5-P29-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])

ps['P30'] = html.Div([
        html.H3(textosMERLO_5['preguntaP30'], className='subtituloBloque'),
        getBarplotWithPalette(filesMERLO_5['csvP30'][0], 'selectTargetMERLO_5', paletas['P30'], 'MERLO_5-P30-1', showticklabels=False, reverse=False),
        html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesMERLO_5['csvP30'][2], 'MERLO_5-P30-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, reorder=False,  crucesDict = crucesDictMERLO_5)
])



# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosMERLO_5['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesMERLO_5['csvPXX'][0], 'selectTargetMERLO_5', paletas['PXX'], 'MERLO_5-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesMERLO_5['csvPXX'][1], MERLO_5PXX, 'MERLO_5-PXX-2', 'selectTargetMERLO_5', opcionesDePreguntasInicial=3),
#         html.H3(textosMERLO_5['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesMERLO_5['csvPXX'][2], 'MERLO_5-PXX-3', 'selectTargetMERLO_5', '', preguntasQueNoVan = preguntasQueNoVanMERLO_5, crucesDict = crucesDictMERLO_5)
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


imagen = plots(filesMERLO_5['csv_imagen'][0],filesMERLO_5['csv_imagen'][3], filesMERLO_5['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetMERLO_5',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanMERLO_5, name='MERLO_5-Comparativo',crucesDict = crucesDictMERLO_5, files=filesMERLO_5, tracking='MERLO_5'),



ps['imagen1'] = html.Div([
                html.H3(textosMERLO_5['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_5['seleccioneFigura']),
                getStackedBarplot(filesMERLO_5['csv_imagen'][0], 'selectTargetMERLO_5', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_5-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosMERLO_5['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_5['seleccioneFigura']),
                getStackedBarplot(filesMERLO_5['csv_imagen'][1], 'selectTargetMERLO_5', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_5-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosMERLO_5['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosMERLO_5['seleccioneFigura']),
                getStackedBarplot(filesMERLO_5['csv_imagen'][2], 'selectTargetMERLO_5', 'selectOpciones_Merlo2', opinionColorDict, 'MERLO_5-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





