from especiales.ESCOBAR_1.apps.preguntasESCOBAR_1 import filesESCOBAR_1, preguntasQueNoVanESCOBAR_1
from especiales.ESCOBAR_1.apps.txtESCOBAR_1 import textosESCOBAR_1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.ESCOBAR_1.apps.txtESCOBAR_1 import textosESCOBAR_1
from config import *
from especiales.ESCOBAR_1.apps.configESCOBAR_1 import *
from especiales.ESCOBAR_1.apps.bloquesESCOBAR_1 import bloques_ESCOBAR_1
from graphs import *
from especiales.ESCOBAR_1.apps.txtESCOBAR_1 import textosESCOBAR_1 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_ESCOBAR_1.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosESCOBAR_1["label" + pregunta]

orden_preguntas = []
for _ in bloques_ESCOBAR_1.values():
    orden_preguntas.extend(_)




# Layout

ps = {}

ps['P07'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP07'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP07'][0], 'selectTargetESCOBAR_1', paletas['P07'], 'ESCOBAR_1-P07-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP07'][1], ESCOBAR_1P07, 'ESCOBAR_1-P07-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP07'][2], 'ESCOBAR_1-P07-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P08'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP08'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP08'][0], 'selectTargetESCOBAR_1', paletas['P08'], 'ESCOBAR_1-P08-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP08'][1], ESCOBAR_1P08, 'ESCOBAR_1-P08-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP08'][2], 'ESCOBAR_1-P08-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P09'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP09'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP09'][0], 'selectTargetESCOBAR_1', paletas['P09'], 'ESCOBAR_1-P09-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP09'][1], ESCOBAR_1P09, 'ESCOBAR_1-P09-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP09'][2], 'ESCOBAR_1-P09-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P10'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP10'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP10'][0], 'selectTargetESCOBAR_1', paletas['P10'], 'ESCOBAR_1-P10-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP10'][1], ESCOBAR_1P10, 'ESCOBAR_1-P10-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP10'][2], 'ESCOBAR_1-P10-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])


ps['P12'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP12'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP12'][0], 'selectTargetESCOBAR_1', paletas['P12'], 'ESCOBAR_1-P12-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP12'][1], ESCOBAR_1P12, 'ESCOBAR_1-P12-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP12'][2], 'ESCOBAR_1-P12-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P13'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP13'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP13'][0], 'selectTargetESCOBAR_1', paletas['P13'], 'ESCOBAR_1-P13-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP13'][1], ESCOBAR_1P13, 'ESCOBAR_1-P13-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP13'][2], 'ESCOBAR_1-P13-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P14'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP14'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP14'][0], 'selectTargetESCOBAR_1', paletas['P14'], 'ESCOBAR_1-P14-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP14'][1], ESCOBAR_1P14, 'ESCOBAR_1-P14-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP14'][2], 'ESCOBAR_1-P14-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P15'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP15'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP15'][0], 'selectTargetESCOBAR_1', paletas['P15'], 'ESCOBAR_1-P15-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP15'][1], ESCOBAR_1P15, 'ESCOBAR_1-P15-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP15'][2], 'ESCOBAR_1-P15-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P16'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP16'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP16'][0], 'selectTargetESCOBAR_1', paletas['P16'], 'ESCOBAR_1-P16-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP16'][1], ESCOBAR_1P16, 'ESCOBAR_1-P16-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP16'][2], 'ESCOBAR_1-P16-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P17'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP17'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP17'][0], 'selectTargetESCOBAR_1', paletas['P17'], 'ESCOBAR_1-P17-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP17'][1], ESCOBAR_1P17, 'ESCOBAR_1-P17-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP17'][2], 'ESCOBAR_1-P17-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P18'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP18'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP18'][0], 'selectTargetESCOBAR_1', paletas['P18'], 'ESCOBAR_1-P18-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP18'][1], ESCOBAR_1P18, 'ESCOBAR_1-P18-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP18'][2], 'ESCOBAR_1-P18-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P19'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP19'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP19'][0], 'selectTargetESCOBAR_1', paletas['P19'], 'ESCOBAR_1-P19-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP19'][1], ESCOBAR_1P19, 'ESCOBAR_1-P19-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP19'][2], 'ESCOBAR_1-P19-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P20'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP20'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP20'][0], 'selectTargetESCOBAR_1', paletas['P20'], 'ESCOBAR_1-P20-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP20'][1], ESCOBAR_1P20, 'ESCOBAR_1-P20-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP20'][2], 'ESCOBAR_1-P20-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])


ps['P21'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP21'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesESCOBAR_1['csvP21'][0], 'selectTargetESCOBAR_1','selectOpciones',  paletas['P21'], 'ESCOBAR_1-P21-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP21'][1], ESCOBAR_1P21, 'ESCOBAR_1-P21-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesESCOBAR_1['csvP21'][2], 'ESCOBAR_1-P21-3', 'selectTargetESCOBAR_1', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1, opcionesDePreguntasInicial=6),
])

ps['P22'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP22'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP22'][0], 'selectTargetESCOBAR_1', paletas['P22'], 'ESCOBAR_1-P22-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP22'][1], ESCOBAR_1P22, 'ESCOBAR_1-P22-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP22'][2], 'ESCOBAR_1-P22-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P23'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP23'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP23'][0], 'selectTargetESCOBAR_1', paletas['P23'], 'ESCOBAR_1-P23-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP23'][1], ESCOBAR_1P23, 'ESCOBAR_1-P23-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP23'][2], 'ESCOBAR_1-P23-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P24'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP24'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP24'][0], 'selectTargetESCOBAR_1', paletas['P24'], 'ESCOBAR_1-P24-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP24'][1], ESCOBAR_1P24, 'ESCOBAR_1-P24-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP24'][2], 'ESCOBAR_1-P24-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P25'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP25'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP25'][0], 'selectTargetESCOBAR_1', paletas['P25'], 'ESCOBAR_1-P25-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP25'][1], ESCOBAR_1P25, 'ESCOBAR_1-P25-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP25'][2], 'ESCOBAR_1-P25-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P26'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP26'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP26'][0], 'selectTargetESCOBAR_1', paletas['P26'], 'ESCOBAR_1-P26-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP26'][1], ESCOBAR_1P26, 'ESCOBAR_1-P26-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP26'][2], 'ESCOBAR_1-P26-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])



ps['P35'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP35'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP35'][0], 'selectTargetESCOBAR_1', paletas['P35'], 'ESCOBAR_1-P35-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP35'][1], ESCOBAR_1P35, 'ESCOBAR_1-P35-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesESCOBAR_1['csvP35'][2], 'ESCOBAR_1-P35-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])


ps['P37'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP37'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP37'][0], 'selectTargetESCOBAR_1', paletas['P37'], 'ESCOBAR_1-P37-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP37'][1], ESCOBAR_1P37, 'ESCOBAR_1-P37-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        #html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        #getCrucesStacked(filesESCOBAR_1['csvP37'][2], 'ESCOBAR_1-P37-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P38'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP38'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP38'][0], 'selectTargetESCOBAR_1', paletas['P38'], 'ESCOBAR_1-P38-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP38'][1], ESCOBAR_1P38, 'ESCOBAR_1-P38-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        #html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        #getCrucesStacked(filesESCOBAR_1['csvP38'][2], 'ESCOBAR_1-P38-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P39'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP39'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP39'][0], 'selectTargetESCOBAR_1', paletas['P39'], 'ESCOBAR_1-P39-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP39'][1], ESCOBAR_1P39, 'ESCOBAR_1-P39-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        #html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        #getCrucesStacked(filesESCOBAR_1['csvP39'][2], 'ESCOBAR_1-P39-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])

ps['P40'] = html.Div([
        html.H3(textosESCOBAR_1['preguntaP40'], className='subtituloBloque'),
        getBarplotWithPalette(filesESCOBAR_1['csvP40'][0], 'selectTargetESCOBAR_1', paletas['P40'], 'ESCOBAR_1-P40-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesESCOBAR_1['csvP40'][1], ESCOBAR_1P40, 'ESCOBAR_1-P40-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
        #html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
        #getCrucesStacked(filesESCOBAR_1['csvP40'][2], 'ESCOBAR_1-P40-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
])










# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosESCOBAR_1['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesESCOBAR_1['csvPXX'][0], 'selectTargetESCOBAR_1', paletas['PXX'], 'ESCOBAR_1-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesESCOBAR_1['csvPXX'][1], ESCOBAR_1PXX, 'ESCOBAR_1-PXX-2', 'selectTargetESCOBAR_1', opcionesDePreguntasInicial=3),
#         html.H3(textosESCOBAR_1['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesESCOBAR_1['csvPXX'][2], 'ESCOBAR_1-PXX-3', 'selectTargetESCOBAR_1', '', preguntasQueNoVan = preguntasQueNoVanESCOBAR_1, reorder=True, crucesDict = crucesDictESCOBAR_1)
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


imagen = plots(filesESCOBAR_1['csv_imagen'][0],filesESCOBAR_1['csv_imagen'][3], filesESCOBAR_1['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetESCOBAR_1',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanESCOBAR_1, name='ESCOBAR_1-Comparativo', crucesDict = crucesDictESCOBAR_1, files=filesESCOBAR_1, tracking='ESCOBAR_1'),



ps['imagen1'] = html.Div([
                html.H3(textosESCOBAR_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosESCOBAR_1['seleccioneFigura']),
                getStackedBarplot(filesESCOBAR_1['csv_imagen'][0], 'selectTargetESCOBAR_1', 'selectOpciones', opinionColorDict, 'ESCOBAR_1-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosESCOBAR_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosESCOBAR_1['seleccioneFigura']),
                getStackedBarplot(filesESCOBAR_1['csv_imagen'][1], 'selectTargetESCOBAR_1', 'selectOpciones', opinionColorDict, 'ESCOBAR_1-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosESCOBAR_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosESCOBAR_1['seleccioneFigura']),
                getStackedBarplot(filesESCOBAR_1['csv_imagen'][2], 'selectTargetESCOBAR_1', 'selectOpciones', opinionColorDict, 'ESCOBAR_1-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





