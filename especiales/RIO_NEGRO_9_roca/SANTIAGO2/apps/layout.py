from especiales.SANTIAGO2.apps.preguntasSANTIAGO2 import filesSANTIAGO2, preguntasQueNoVanSANTIAGO2
from especiales.SANTIAGO2.apps.txtSANTIAGO2 import textosSANTIAGO2
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.SANTIAGO2.apps.txtSANTIAGO2 import textosSANTIAGO2
from config import *
from especiales.SANTIAGO2.apps.configSANTIAGO2 import *
from especiales.SANTIAGO2.apps.bloques import bloques_SANTIAGO2
from graphs import *
from especiales.SANTIAGO2.apps.txtSANTIAGO2 import textosSANTIAGO2 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_SANTIAGO2.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosSANTIAGO2["label" + pregunta]

orden_preguntas = []
for _ in bloques_SANTIAGO2.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

# Bloque 1

# ps['P05'] = html.Div([
#         html.H3(textosSANTIAGO2['preguntaP05'], className='subtituloBloque'),
#         getBarplotWithPalette(filesSANTIAGO2['csvP05'][0], 'selectTargetSANTIAGO2', paletas['P05'], 'SANTIAGO2-P05-1', showticklabels=False, reverse=False ),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesSANTIAGO2['csvP05'][1], SANTIAGO2P05, 'SANTIAGO2-P05-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
#         html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesSANTIAGO2['csvP05'][2], 'SANTIAGO2-P05-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
# ])
#
#
# ps['P06'] = html.Div([
#         html.H3(textosSANTIAGO2['preguntaP06'], className='subtituloBloque'),
#         getBarplotWithPalette(filesSANTIAGO2['csvP06'][0], 'selectTargetSANTIAGO2', paletas['P06'], 'SANTIAGO2-P06-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesSANTIAGO2['csvP06'][1], SANTIAGO2P06, 'SANTIAGO2-P06-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
#         html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesSANTIAGO2['csvP06'][2], 'SANTIAGO2-P06-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
# ])

ps['P05'] = html.Div([
        html.H3(textosSANTIAGO2['preguntaP05'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO2['csvP05'][0], 'selectTargetSANTIAGO2', paletas['P05'], 'SANTIAGO2-P05-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO2['csvP05'][1], SANTIAGO2P05, 'SANTIAGO2-P05-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO2['csvP05'][2], 'SANTIAGO2-P05-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
])

ps['P06'] = html.Div([
        html.H3(textosSANTIAGO2['preguntaP06'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO2['csvP06'][0], 'selectTargetSANTIAGO2', paletas['P06'], 'SANTIAGO2-P06-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO2['csvP06'][1], SANTIAGO2P06, 'SANTIAGO2-P06-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO2['csvP06'][2], 'SANTIAGO2-P06-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
])
# ps['P06_imputados'] = html.Div([
#         html.H3(textosSANTIAGO2['preguntaP06_imputados'], className='subtituloBloque'),
#         getBarplotWithPalette(filesSANTIAGO2['csvP06_imputados'][0], 'selectTargetSANTIAGO2', paletas['P06'], 'SANTIAGO2-P06_imputados-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesSANTIAGO2['csvP06_imputados'][1], SANTIAGO2P06_imputados, 'SANTIAGO2-P06_imputados-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
#         html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesSANTIAGO2['csvP06_imputados'][1], 'SANTIAGO2-P06_imputados-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
# ])
#
#

ps['P08'] = html.Div([
        html.H3(textosSANTIAGO2['preguntaP08'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO2['csvP08'][0], 'selectTargetSANTIAGO2', paletas['P08'], 'SANTIAGO2-P08-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO2['csvP08'][1], SANTIAGO2P08, 'SANTIAGO2-P08-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO2['csvP08'][2], 'SANTIAGO2-P08-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
])

# ps['P08_imputados'] = html.Div([
#         html.H3(textosSANTIAGO2['preguntaP08_imputados'], className='subtituloBloque'),
#         getBarplotWithPalette(filesSANTIAGO2['csvP08_imputados'][0], 'selectTargetSANTIAGO2', paletas['P08'], 'SANTIAGO2-P08_imputados-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesSANTIAGO2['csvP08_imputados'][1], SANTIAGO2P08_imputados, 'SANTIAGO2-P08_imputados-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
#         html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesSANTIAGO2['csvP08_imputados'][1], 'SANTIAGO2-P08_imputados-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
# ])


ps['P10'] = html.Div([
        html.H3(textosSANTIAGO2['preguntaP10'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO2['csvP10'][0], 'selectTargetSANTIAGO2', paletas['P10'], 'SANTIAGO2-P10-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO2['csvP10'][1], SANTIAGO2P10, 'SANTIAGO2-P10-2', 'selectTargetSANTIAGO2', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO2['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO2['csvP10'][2], 'SANTIAGO2-P10-3', 'selectTargetSANTIAGO2', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO2, crucesDict = crucesDictSANTIAGO2)
])



# Parche del grafico de imagenes por no haber time series
from graph_imagen import *

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
        plots = []

        hbarplot  = plot_hbarplot(csv_hbp, df_hbp, candidato, callbackInputTarget, 'selectOpciones', opinionColorDict, name, opcionesDePreguntasInicial = opcionesDePreguntasInicial)
        cruces_component = plot_cruces(candidato, df_cruces, files, name, callbackInputTarget = callbackInputTarget, crucesDict = crucesDict,  preguntasQueNoVan = preguntasQueNoVan,opcionesDePreguntasInicial = opcionesDePreguntasInicial)
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


imagen = plots(filesSANTIAGO2['csv_imagen'][0],filesSANTIAGO2['csv_imagen'][3], filesSANTIAGO2['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetSANTIAGO2',opcionesDePreguntasInicial = 3,
                            preguntasQueNoVan= preguntasQueNoVanSANTIAGO2, name='SANTIAGO2-Comparativo',crucesDict = crucesDictSANTIAGO2, files=filesSANTIAGO2, tracking='SANTIAGO2'),



#
#
#
#
# # Bloque 17
#
# imagen = plots(filesSANTIAGO2['csv_imagen'][0],filesSANTIAGO2['csv_imagen'][3], filesSANTIAGO2['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetSANTIAGO2',opcionesDePreguntasInicial = 3,
#                            preguntasQueNoVan= preguntasQueNoVanSANTIAGO2, name='SANTIAGO2-Comparativo',crucesDict = crucesDictSANTIAGO2, files=filesSANTIAGO2, tracking='SANTIAGO2'),
#
#
ps['imagen1'] = html.Div([
                html.H3(textosSANTIAGO2['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSANTIAGO2['seleccioneFigura']),
                getStackedBarplot(filesSANTIAGO2['csv_imagen'][0], 'selectTargetSANTIAGO2', 'selectOpciones', opinionColorDict, 'SANTIAGO2-1D1A', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosSANTIAGO2['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSANTIAGO2['seleccioneFigura']),
                getStackedBarplot(filesSANTIAGO2['csv_imagen'][1], 'selectTargetSANTIAGO2', 'selectOpciones', opinionColorDict, 'SANTIAGO2-1D1B', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosSANTIAGO2['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSANTIAGO2['seleccioneFigura']),
                getStackedBarplot(filesSANTIAGO2['csv_imagen'][2], 'selectTargetSANTIAGO2', 'selectOpciones', opinionColorDict, 'SANTIAGO2-1D1C', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





