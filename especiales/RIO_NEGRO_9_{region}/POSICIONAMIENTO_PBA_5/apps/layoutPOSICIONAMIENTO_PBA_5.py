from especiales.POSICIONAMIENTO_PBA_5.apps.preguntasPOSICIONAMIENTO_PBA_5 import filesPOSICIONAMIENTO_PBA_5, preguntasQueNoVanPOSICIONAMIENTO_PBA_5
from especiales.POSICIONAMIENTO_PBA_5.apps.txtPOSICIONAMIENTO_PBA_5 import textosPOSICIONAMIENTO_PBA_5
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.POSICIONAMIENTO_PBA_5.apps.txtPOSICIONAMIENTO_PBA_5 import textosPOSICIONAMIENTO_PBA_5
from config import *
from especiales.POSICIONAMIENTO_PBA_5.apps.configPOSICIONAMIENTO_PBA_5 import *
from especiales.POSICIONAMIENTO_PBA_5.apps.bloquesPOSICIONAMIENTO_PBA_5 import bloques_POSICIONAMIENTO_PBA_5
from graphs import *
from especiales.POSICIONAMIENTO_PBA_5.apps.txtPOSICIONAMIENTO_PBA_5 import textosPOSICIONAMIENTO_PBA_5 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_POSICIONAMIENTO_PBA_5.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosPOSICIONAMIENTO_PBA_5["label" + pregunta]

orden_preguntas = []
for _ in bloques_POSICIONAMIENTO_PBA_5.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

ps['P04'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP04'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP04'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P04'], 'POSICIONAMIENTO_PBA_5-P04-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP04'][1], POSICIONAMIENTO_PBA_5P04, 'POSICIONAMIENTO_PBA_5-P04-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP04'][2], 'POSICIONAMIENTO_PBA_5-P04-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P05'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP05'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP05'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P05'], 'POSICIONAMIENTO_PBA_5-P05-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP05'][1], POSICIONAMIENTO_PBA_5P05, 'POSICIONAMIENTO_PBA_5-P05-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP05'][2], 'POSICIONAMIENTO_PBA_5-P05-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P06'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP06'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP06'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P06'], 'POSICIONAMIENTO_PBA_5-P06-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP06'][1], POSICIONAMIENTO_PBA_5P06, 'POSICIONAMIENTO_PBA_5-P06-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP06'][2], 'POSICIONAMIENTO_PBA_5-P06-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P07'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP07'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP07'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P07'], 'POSICIONAMIENTO_PBA_5-P07-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP07'][1], POSICIONAMIENTO_PBA_5P07, 'POSICIONAMIENTO_PBA_5-P07-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP07'][2], 'POSICIONAMIENTO_PBA_5-P07-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P09'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP09'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP09'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P09'], 'POSICIONAMIENTO_PBA_5-P09-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP09'][1], POSICIONAMIENTO_PBA_5P09, 'POSICIONAMIENTO_PBA_5-P09-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP09'][2], 'POSICIONAMIENTO_PBA_5-P09-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P10'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP10'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP10'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P10'], 'POSICIONAMIENTO_PBA_5-P10-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP10'][1], POSICIONAMIENTO_PBA_5P10, 'POSICIONAMIENTO_PBA_5-P10-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP10'][2], 'POSICIONAMIENTO_PBA_5-P10-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P11'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP11'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP11'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P11'], 'POSICIONAMIENTO_PBA_5-P11-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP11'][1], POSICIONAMIENTO_PBA_5P11, 'POSICIONAMIENTO_PBA_5-P11-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP11'][2], 'POSICIONAMIENTO_PBA_5-P11-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])
ps['P12'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP12'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP12'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P12'], 'POSICIONAMIENTO_PBA_5-P12-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP12'][1], POSICIONAMIENTO_PBA_5P12, 'POSICIONAMIENTO_PBA_5-P12-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP12'][2], 'POSICIONAMIENTO_PBA_5-P12-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])
ps['P13'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP13'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP13'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P13'], 'POSICIONAMIENTO_PBA_5-P13-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP13'][1], POSICIONAMIENTO_PBA_5P13, 'POSICIONAMIENTO_PBA_5-P13-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP13'][2], 'POSICIONAMIENTO_PBA_5-P13-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P14'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP14'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP14'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P14'], 'POSICIONAMIENTO_PBA_5-P14-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP14'][1], POSICIONAMIENTO_PBA_5P14, 'POSICIONAMIENTO_PBA_5-P14-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP14'][2], 'POSICIONAMIENTO_PBA_5-P14-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P15'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP15'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP15'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P15'], 'POSICIONAMIENTO_PBA_5-P15-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP15'][1], POSICIONAMIENTO_PBA_5P15, 'POSICIONAMIENTO_PBA_5-P15-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP15'][2], 'POSICIONAMIENTO_PBA_5-P15-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P16'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP16'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP16'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P16'], 'POSICIONAMIENTO_PBA_5-P16-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP16'][1], POSICIONAMIENTO_PBA_5P16, 'POSICIONAMIENTO_PBA_5-P16-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP16'][2], 'POSICIONAMIENTO_PBA_5-P16-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P17'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP17'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP17'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P17'], 'POSICIONAMIENTO_PBA_5-P17-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP17'][1], POSICIONAMIENTO_PBA_5P17, 'POSICIONAMIENTO_PBA_5-P17-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP17'][2], 'POSICIONAMIENTO_PBA_5-P17-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P18'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP18'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP18'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P18'], 'POSICIONAMIENTO_PBA_5-P18-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP18'][1], POSICIONAMIENTO_PBA_5P18, 'POSICIONAMIENTO_PBA_5-P18-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP18'][2], 'POSICIONAMIENTO_PBA_5-P18-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P19'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP19'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP19'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P19'], 'POSICIONAMIENTO_PBA_5-P19-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP19'][1], POSICIONAMIENTO_PBA_5P19, 'POSICIONAMIENTO_PBA_5-P19-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP19'][2], 'POSICIONAMIENTO_PBA_5-P19-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P20'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP20'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP20'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P20'], 'POSICIONAMIENTO_PBA_5-P20-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP20'][1], POSICIONAMIENTO_PBA_5P20, 'POSICIONAMIENTO_PBA_5-P20-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP20'][2], 'POSICIONAMIENTO_PBA_5-P20-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P21'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP21'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP21'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P21'], 'POSICIONAMIENTO_PBA_5-P21-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP21'][1], POSICIONAMIENTO_PBA_5P21, 'POSICIONAMIENTO_PBA_5-P21-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP21'][2], 'POSICIONAMIENTO_PBA_5-P21-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P22'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP22'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP22'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P22'], 'POSICIONAMIENTO_PBA_5-P22-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP22'][1], POSICIONAMIENTO_PBA_5P22, 'POSICIONAMIENTO_PBA_5-P22-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP22'][2], 'POSICIONAMIENTO_PBA_5-P22-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P23'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP23'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP23'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P23'], 'POSICIONAMIENTO_PBA_5-P23-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP23'][1], POSICIONAMIENTO_PBA_5P23, 'POSICIONAMIENTO_PBA_5-P23-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP23'][2], 'POSICIONAMIENTO_PBA_5-P23-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P24'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP24'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP24'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P24'], 'POSICIONAMIENTO_PBA_5-P24-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP24'][1], POSICIONAMIENTO_PBA_5P24, 'POSICIONAMIENTO_PBA_5-P24-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP24'][2], 'POSICIONAMIENTO_PBA_5-P24-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P25'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP25'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP25'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P25'], 'POSICIONAMIENTO_PBA_5-P25-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP25'][1], POSICIONAMIENTO_PBA_5P25, 'POSICIONAMIENTO_PBA_5-P25-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP25'][2], 'POSICIONAMIENTO_PBA_5-P25-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P29'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP29'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP29'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P29'], 'POSICIONAMIENTO_PBA_5-P29-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP29'][1], POSICIONAMIENTO_PBA_5P29, 'POSICIONAMIENTO_PBA_5-P29-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP29'][2], 'POSICIONAMIENTO_PBA_5-P29-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P31'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP31'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP31'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P31'], 'POSICIONAMIENTO_PBA_5-P31-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP31'][1], POSICIONAMIENTO_PBA_5P31, 'POSICIONAMIENTO_PBA_5-P31-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP31'][2], 'POSICIONAMIENTO_PBA_5-P31-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P33'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP33'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP33'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P33'], 'POSICIONAMIENTO_PBA_5-P33-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP33'][1], POSICIONAMIENTO_PBA_5P33, 'POSICIONAMIENTO_PBA_5-P33-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP33'][2], 'POSICIONAMIENTO_PBA_5-P33-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P35'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP35'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP35'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P35'], 'POSICIONAMIENTO_PBA_5-P35-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP35'][1], POSICIONAMIENTO_PBA_5P35, 'POSICIONAMIENTO_PBA_5-P35-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP35'][2], 'POSICIONAMIENTO_PBA_5-P35-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P37'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP37'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP37'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P37'], 'POSICIONAMIENTO_PBA_5-P37-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP37'][1], POSICIONAMIENTO_PBA_5P37, 'POSICIONAMIENTO_PBA_5-P37-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP37'][2], 'POSICIONAMIENTO_PBA_5-P37-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])
ps['P38'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP38'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP38'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P38'], 'POSICIONAMIENTO_PBA_5-P38-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP38'][1], POSICIONAMIENTO_PBA_5P38, 'POSICIONAMIENTO_PBA_5-P38-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP38'][2], 'POSICIONAMIENTO_PBA_5-P38-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P39'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP39'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP39'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P39'], 'POSICIONAMIENTO_PBA_5-P39-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP39'][1], POSICIONAMIENTO_PBA_5P39, 'POSICIONAMIENTO_PBA_5-P39-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP39'][2], 'POSICIONAMIENTO_PBA_5-P39-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P40'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP40'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP40'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P40'], 'POSICIONAMIENTO_PBA_5-P40-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP40'][1], POSICIONAMIENTO_PBA_5P40, 'POSICIONAMIENTO_PBA_5-P40-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP40'][2], 'POSICIONAMIENTO_PBA_5-P40-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P41'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP41'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP41'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P41'], 'POSICIONAMIENTO_PBA_5-P41-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP41'][1], POSICIONAMIENTO_PBA_5P41, 'POSICIONAMIENTO_PBA_5-P41-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP41'][2], 'POSICIONAMIENTO_PBA_5-P41-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])


ps['P42'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP42'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP42'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P42'], 'POSICIONAMIENTO_PBA_5-P42-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP42'][1], POSICIONAMIENTO_PBA_5P42, 'POSICIONAMIENTO_PBA_5-P42-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP42'][2], 'POSICIONAMIENTO_PBA_5-P42-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P43'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP43'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP43'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P43'], 'POSICIONAMIENTO_PBA_5-P43-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP43'][1], POSICIONAMIENTO_PBA_5P43, 'POSICIONAMIENTO_PBA_5-P43-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP43'][2], 'POSICIONAMIENTO_PBA_5-P43-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])

ps['P44'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP44'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP44'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P44'], 'POSICIONAMIENTO_PBA_5-P44-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP44'][1], POSICIONAMIENTO_PBA_5P44, 'POSICIONAMIENTO_PBA_5-P44-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP44'][2], 'POSICIONAMIENTO_PBA_5-P44-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])
ps['P45'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP45'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP45'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P45'], 'POSICIONAMIENTO_PBA_5-P45-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP45'][1], POSICIONAMIENTO_PBA_5P45, 'POSICIONAMIENTO_PBA_5-P45-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP45'][2], 'POSICIONAMIENTO_PBA_5-P45-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])
ps['P46'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP46'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP46'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', paletas['P46'], 'POSICIONAMIENTO_PBA_5-P46-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP46'][1], POSICIONAMIENTO_PBA_5P46, 'POSICIONAMIENTO_PBA_5-P46-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_5['csvP46'][2], 'POSICIONAMIENTO_PBA_5-P46-3', 'selectTargetPOSICIONAMIENTO_PBA_5', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])





ps['P47'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_5['preguntaP47'], className='subtituloBloque'),
         getHBarplotOpcionesWithPalette(filesPOSICIONAMIENTO_PBA_5['csvP47'][0], 'selectTargetPOSICIONAMIENTO_PBA_5','selectOpciones', paletas['P47'], 'POSICIONAMIENTO_PBA_5-P47-1', showticklabels=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_5['csvP47'][1], POSICIONAMIENTO_PBA_5P47, 'POSICIONAMIENTO_PBA_5-P47-2', 'selectTargetPOSICIONAMIENTO_PBA_5', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_5['cruce'], className='subtituloBloque'),
         getCrucesOpinionStacked(filesPOSICIONAMIENTO_PBA_5['csvP47'][2], 'POSICIONAMIENTO_PBA_5-P47-3', 'selectTargetPOSICIONAMIENTO_PBA_5', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_5, reorder= False , crucesDict = crucesDictPOSICIONAMIENTO_PBA_5)
])






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


imagen = plots(filesPOSICIONAMIENTO_PBA_5['csv_imagen'][0],filesPOSICIONAMIENTO_PBA_5['csv_imagen'][3], filesPOSICIONAMIENTO_PBA_5['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetPOSICIONAMIENTO_PBA_5',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanPOSICIONAMIENTO_PBA_5, name='POSICIONAMIENTO_PBA_5-Comparativo',crucesDict = crucesDictPOSICIONAMIENTO_PBA_5, files=filesPOSICIONAMIENTO_PBA_5, tracking='POSICIONAMIENTO_PBA_5'),



ps['imagen1'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_PBA_5['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_PBA_5['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_PBA_5['csv_imagen'][0], 'selectTargetPOSICIONAMIENTO_PBA_5', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_PBA_5-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_PBA_5['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_PBA_5['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_PBA_5['csv_imagen'][1], 'selectTargetPOSICIONAMIENTO_PBA_5', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_PBA_5-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_PBA_5['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_PBA_5['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_PBA_5['csv_imagen'][2], 'selectTargetPOSICIONAMIENTO_PBA_5', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_PBA_5-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





