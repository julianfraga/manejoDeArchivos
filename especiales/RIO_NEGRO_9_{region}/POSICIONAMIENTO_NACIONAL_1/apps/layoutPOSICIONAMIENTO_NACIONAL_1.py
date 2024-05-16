from especiales.POSICIONAMIENTO_NACIONAL_1.apps.preguntasPOSICIONAMIENTO_NACIONAL_1 import filesPOSICIONAMIENTO_NACIONAL_1, preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1
from especiales.POSICIONAMIENTO_NACIONAL_1.apps.txtPOSICIONAMIENTO_NACIONAL_1 import textosPOSICIONAMIENTO_NACIONAL_1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.POSICIONAMIENTO_NACIONAL_1.apps.txtPOSICIONAMIENTO_NACIONAL_1 import textosPOSICIONAMIENTO_NACIONAL_1
from config import *
from especiales.POSICIONAMIENTO_NACIONAL_1.apps.configPOSICIONAMIENTO_NACIONAL_1 import *
from especiales.POSICIONAMIENTO_NACIONAL_1.apps.bloquesPOSICIONAMIENTO_NACIONAL_1 import bloques_POSICIONAMIENTO_NACIONAL_1
from graphs import *
from especiales.POSICIONAMIENTO_NACIONAL_1.apps.txtPOSICIONAMIENTO_NACIONAL_1 import textosPOSICIONAMIENTO_NACIONAL_1 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_POSICIONAMIENTO_NACIONAL_1.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosPOSICIONAMIENTO_NACIONAL_1["label" + pregunta]

orden_preguntas = []
for _ in bloques_POSICIONAMIENTO_NACIONAL_1.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

ps['P04'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP04'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP04'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P04'], 'POSICIONAMIENTO_NACIONAL_1-P04-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP04'][1], POSICIONAMIENTO_NACIONAL_1P04, 'POSICIONAMIENTO_NACIONAL_1-P04-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP04'][2], 'POSICIONAMIENTO_NACIONAL_1-P04-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])


ps['P05'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP05'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP05'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P05'], 'POSICIONAMIENTO_NACIONAL_1-P05-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP05'][1], POSICIONAMIENTO_NACIONAL_1P05, 'POSICIONAMIENTO_NACIONAL_1-P05-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP05'][2], 'POSICIONAMIENTO_NACIONAL_1-P05-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P06'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP06'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP06'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P06'], 'POSICIONAMIENTO_NACIONAL_1-P06-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP06'][1], POSICIONAMIENTO_NACIONAL_1P06, 'POSICIONAMIENTO_NACIONAL_1-P06-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP06'][2], 'POSICIONAMIENTO_NACIONAL_1-P06-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P07'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP07'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP07'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P07'], 'POSICIONAMIENTO_NACIONAL_1-P07-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP07'][1], POSICIONAMIENTO_NACIONAL_1P07, 'POSICIONAMIENTO_NACIONAL_1-P07-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP07'][2], 'POSICIONAMIENTO_NACIONAL_1-P07-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P08'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP08'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP08'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P08'], 'POSICIONAMIENTO_NACIONAL_1-P08-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP08'][1], POSICIONAMIENTO_NACIONAL_1P08, 'POSICIONAMIENTO_NACIONAL_1-P08-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP08'][2], 'POSICIONAMIENTO_NACIONAL_1-P08-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P10'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP10'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP10'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P10'], 'POSICIONAMIENTO_NACIONAL_1-P10-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP10'][1], POSICIONAMIENTO_NACIONAL_1P10, 'POSICIONAMIENTO_NACIONAL_1-P10-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP10'][2], 'POSICIONAMIENTO_NACIONAL_1-P10-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P11'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP11'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP11'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P11'], 'POSICIONAMIENTO_NACIONAL_1-P11-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP11'][1], POSICIONAMIENTO_NACIONAL_1P11, 'POSICIONAMIENTO_NACIONAL_1-P11-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP11'][2], 'POSICIONAMIENTO_NACIONAL_1-P11-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P12'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP12'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP12'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P12'], 'POSICIONAMIENTO_NACIONAL_1-P12-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP12'][1], POSICIONAMIENTO_NACIONAL_1P12, 'POSICIONAMIENTO_NACIONAL_1-P12-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP12'][2], 'POSICIONAMIENTO_NACIONAL_1-P12-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P13'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP13'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP13'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P13'], 'POSICIONAMIENTO_NACIONAL_1-P13-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP13'][1], POSICIONAMIENTO_NACIONAL_1P13, 'POSICIONAMIENTO_NACIONAL_1-P13-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP13'][2], 'POSICIONAMIENTO_NACIONAL_1-P13-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P14'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP14'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP14'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P14'], 'POSICIONAMIENTO_NACIONAL_1-P14-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP14'][1], POSICIONAMIENTO_NACIONAL_1P14, 'POSICIONAMIENTO_NACIONAL_1-P14-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP14'][2], 'POSICIONAMIENTO_NACIONAL_1-P14-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P15'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP15'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP15'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P15'], 'POSICIONAMIENTO_NACIONAL_1-P15-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP15'][1], POSICIONAMIENTO_NACIONAL_1P15, 'POSICIONAMIENTO_NACIONAL_1-P15-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP15'][2], 'POSICIONAMIENTO_NACIONAL_1-P15-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P16'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP16'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP16'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P16'], 'POSICIONAMIENTO_NACIONAL_1-P16-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP16'][1], POSICIONAMIENTO_NACIONAL_1P16, 'POSICIONAMIENTO_NACIONAL_1-P16-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP16'][2], 'POSICIONAMIENTO_NACIONAL_1-P16-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P17'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP17'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP17'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P17'], 'POSICIONAMIENTO_NACIONAL_1-P17-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP17'][1], POSICIONAMIENTO_NACIONAL_1P17, 'POSICIONAMIENTO_NACIONAL_1-P17-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP17'][2], 'POSICIONAMIENTO_NACIONAL_1-P17-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P18'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP18'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP18'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P18'], 'POSICIONAMIENTO_NACIONAL_1-P18-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP18'][1], POSICIONAMIENTO_NACIONAL_1P18, 'POSICIONAMIENTO_NACIONAL_1-P18-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP18'][2], 'POSICIONAMIENTO_NACIONAL_1-P18-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P19'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP19'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP19'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P19'], 'POSICIONAMIENTO_NACIONAL_1-P19-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP19'][1], POSICIONAMIENTO_NACIONAL_1P19, 'POSICIONAMIENTO_NACIONAL_1-P19-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP19'][2], 'POSICIONAMIENTO_NACIONAL_1-P19-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P20'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP20'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP20'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P20'], 'POSICIONAMIENTO_NACIONAL_1-P20-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP20'][1], POSICIONAMIENTO_NACIONAL_1P20, 'POSICIONAMIENTO_NACIONAL_1-P20-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP20'][2], 'POSICIONAMIENTO_NACIONAL_1-P20-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P21'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP21'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP21'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P21'], 'POSICIONAMIENTO_NACIONAL_1-P21-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP21'][1], POSICIONAMIENTO_NACIONAL_1P21, 'POSICIONAMIENTO_NACIONAL_1-P21-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP21'][2], 'POSICIONAMIENTO_NACIONAL_1-P21-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])



# ps['P20'] = html.Div([
#         html.H3(textos['preguntaP20'], className='subtituloBloque'),
#         getHBarplotOpcionesWithPalette(filesNacional['csvP20'][0], 'selectTarget', 'selectOpciones', opinionColorDict, 'Nacional-P20-1'),
#         html.H3(),
#         getTimeSeriesLineplot(filesNacional['csvP20'][1], imagenColorDict, 'Nacional-P20-2', 'selectTarget'),
#         html.H3(textos['cruce'], className='subtituloBloque'),
#         getCrucesOpinionStacked(filesNacional['csvP20'][2], 'Nacional-P20-3', 'selectTarget', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanNacional)
# ])

ps['P22'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP22'], className='subtituloBloque'),
         getHBarplotOpcionesWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP22'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1','selectOpciones', paletas['P22'], 'POSICIONAMIENTO_NACIONAL_1-P22-1', showticklabels=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP22'][1], POSICIONAMIENTO_NACIONAL_1P22, 'POSICIONAMIENTO_NACIONAL_1-P22-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesOpinionStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP22'][2], 'POSICIONAMIENTO_NACIONAL_1-P22-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False , crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P23'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP23'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP23'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P23'], 'POSICIONAMIENTO_NACIONAL_1-P23-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP23'][1], POSICIONAMIENTO_NACIONAL_1P23, 'POSICIONAMIENTO_NACIONAL_1-P23-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP23'][2], 'POSICIONAMIENTO_NACIONAL_1-P23-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P24'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP24'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP24'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P24'], 'POSICIONAMIENTO_NACIONAL_1-P24-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP24'][1], POSICIONAMIENTO_NACIONAL_1P24, 'POSICIONAMIENTO_NACIONAL_1-P24-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP24'][2], 'POSICIONAMIENTO_NACIONAL_1-P24-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P25'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP25'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP25'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P25'], 'POSICIONAMIENTO_NACIONAL_1-P25-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP25'][1], POSICIONAMIENTO_NACIONAL_1P25, 'POSICIONAMIENTO_NACIONAL_1-P25-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP25'][2], 'POSICIONAMIENTO_NACIONAL_1-P25-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P26'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP26'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP26'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P26'], 'POSICIONAMIENTO_NACIONAL_1-P26-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP26'][1], POSICIONAMIENTO_NACIONAL_1P26, 'POSICIONAMIENTO_NACIONAL_1-P26-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP26'][2], 'POSICIONAMIENTO_NACIONAL_1-P26-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P27'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP27'], className='subtituloBloque'),
         getHBarplotOpcionesWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP27'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1','selectOpciones', paletas['P27'], 'POSICIONAMIENTO_NACIONAL_1-P27-1', showticklabels=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP27'][1], POSICIONAMIENTO_NACIONAL_1P27, 'POSICIONAMIENTO_NACIONAL_1-P27-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesOpinionStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP27'][2], 'POSICIONAMIENTO_NACIONAL_1-P27-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False , crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P28'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP28'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP28'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P28'], 'POSICIONAMIENTO_NACIONAL_1-P28-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP28'][1], POSICIONAMIENTO_NACIONAL_1P28, 'POSICIONAMIENTO_NACIONAL_1-P28-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP28'][2], 'POSICIONAMIENTO_NACIONAL_1-P28-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P29'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP29'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP29'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['P29'], 'POSICIONAMIENTO_NACIONAL_1-P29-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP29'][1], POSICIONAMIENTO_NACIONAL_1P29, 'POSICIONAMIENTO_NACIONAL_1-P29-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP29'][2], 'POSICIONAMIENTO_NACIONAL_1-P29-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P30'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP30'], className='subtituloBloque'),
         getHBarplotOpcionesWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP30'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1','selectOpciones', paletas['P30'], 'POSICIONAMIENTO_NACIONAL_1-P30-1', showticklabels=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP30'][1], POSICIONAMIENTO_NACIONAL_1P30, 'POSICIONAMIENTO_NACIONAL_1-P30-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesOpinionStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP30'][2], 'POSICIONAMIENTO_NACIONAL_1-P30-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False , crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P40'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP40'], className='subtituloBloque'),
         getHBarplotOpcionesWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP40'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1','selectOpciones', paletas['P40'], 'POSICIONAMIENTO_NACIONAL_1-P40-1', showticklabels=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP40'][1], POSICIONAMIENTO_NACIONAL_1P40, 'POSICIONAMIENTO_NACIONAL_1-P40-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesOpinionStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP40'][2], 'POSICIONAMIENTO_NACIONAL_1-P40-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False , crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])

ps['P41'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaP41'], className='subtituloBloque'),
         getHBarplotOpcionesWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvP41'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1','selectOpciones', paletas['P41'], 'POSICIONAMIENTO_NACIONAL_1-P41-1', showticklabels=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvP41'][1], POSICIONAMIENTO_NACIONAL_1P41, 'POSICIONAMIENTO_NACIONAL_1-P41-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
         getCrucesOpinionStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvP41'][2], 'POSICIONAMIENTO_NACIONAL_1-P41-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False , crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
])





# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesPOSICIONAMIENTO_NACIONAL_1['csvPXX'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', paletas['PXX'], 'POSICIONAMIENTO_NACIONAL_1-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesPOSICIONAMIENTO_NACIONAL_1['csvPXX'][1], POSICIONAMIENTO_NACIONAL_1PXX, 'POSICIONAMIENTO_NACIONAL_1-PXX-2', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', opcionesDePreguntasInicial=3),
#         html.H3(textosPOSICIONAMIENTO_NACIONAL_1['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesPOSICIONAMIENTO_NACIONAL_1['csvPXX'][2], 'POSICIONAMIENTO_NACIONAL_1-PXX-3', 'selectTargetPOSICIONAMIENTO_NACIONAL_1', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, reorder= False ,crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1)
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


imagen = plots(filesPOSICIONAMIENTO_NACIONAL_1['csv_imagen'][0],filesPOSICIONAMIENTO_NACIONAL_1['csv_imagen'][3], filesPOSICIONAMIENTO_NACIONAL_1['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetPOSICIONAMIENTO_NACIONAL_1',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_1, name='POSICIONAMIENTO_NACIONAL_1-Comparativo',crucesDict = crucesDictPOSICIONAMIENTO_NACIONAL_1, files=filesPOSICIONAMIENTO_NACIONAL_1, tracking='POSICIONAMIENTO_NACIONAL_1'),



ps['imagen1'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_NACIONAL_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_NACIONAL_1['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_NACIONAL_1['csv_imagen'][0], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_NACIONAL_1-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_NACIONAL_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_NACIONAL_1['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_NACIONAL_1['csv_imagen'][1], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_NACIONAL_1-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_NACIONAL_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_NACIONAL_1['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_NACIONAL_1['csv_imagen'][2], 'selectTargetPOSICIONAMIENTO_NACIONAL_1', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_NACIONAL_1-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





