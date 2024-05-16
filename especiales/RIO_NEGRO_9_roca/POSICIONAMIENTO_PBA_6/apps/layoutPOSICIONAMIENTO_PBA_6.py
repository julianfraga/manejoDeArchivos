from especiales.POSICIONAMIENTO_PBA_6.apps.preguntasPOSICIONAMIENTO_PBA_6 import filesPOSICIONAMIENTO_PBA_6, preguntasQueNoVanPOSICIONAMIENTO_PBA_6
from especiales.POSICIONAMIENTO_PBA_6.apps.txtPOSICIONAMIENTO_PBA_6 import textosPOSICIONAMIENTO_PBA_6
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.POSICIONAMIENTO_PBA_6.apps.txtPOSICIONAMIENTO_PBA_6 import textosPOSICIONAMIENTO_PBA_6
from config import *
from especiales.POSICIONAMIENTO_PBA_6.apps.configPOSICIONAMIENTO_PBA_6 import *
from especiales.POSICIONAMIENTO_PBA_6.apps.bloquesPOSICIONAMIENTO_PBA_6 import bloques_POSICIONAMIENTO_PBA_6
from graphs import *
from especiales.POSICIONAMIENTO_PBA_6.apps.txtPOSICIONAMIENTO_PBA_6 import textosPOSICIONAMIENTO_PBA_6 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_POSICIONAMIENTO_PBA_6.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosPOSICIONAMIENTO_PBA_6["label" + pregunta]

orden_preguntas = []
for _ in bloques_POSICIONAMIENTO_PBA_6.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

ps['P04'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP04'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP04'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P04'], 'POSICIONAMIENTO_PBA_6-P04-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP04'][1], POSICIONAMIENTO_PBA_6P04, 'POSICIONAMIENTO_PBA_6-P04-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP04'][2], 'POSICIONAMIENTO_PBA_6-P04-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P05'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP05'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP05'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P05'], 'POSICIONAMIENTO_PBA_6-P05-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP05'][1], POSICIONAMIENTO_PBA_6P05, 'POSICIONAMIENTO_PBA_6-P05-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP05'][2], 'POSICIONAMIENTO_PBA_6-P05-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P06'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP06'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP06'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P06'], 'POSICIONAMIENTO_PBA_6-P06-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP06'][1], POSICIONAMIENTO_PBA_6P06, 'POSICIONAMIENTO_PBA_6-P06-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP06'][2], 'POSICIONAMIENTO_PBA_6-P06-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P07'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP07'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP07'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P07'], 'POSICIONAMIENTO_PBA_6-P07-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP07'][1], POSICIONAMIENTO_PBA_6P07, 'POSICIONAMIENTO_PBA_6-P07-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP07'][2], 'POSICIONAMIENTO_PBA_6-P07-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P09'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP09'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP09'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P09'], 'POSICIONAMIENTO_PBA_6-P09-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP09'][1], POSICIONAMIENTO_PBA_6P09, 'POSICIONAMIENTO_PBA_6-P09-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP09'][2], 'POSICIONAMIENTO_PBA_6-P09-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P10'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP10'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP10'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P10'], 'POSICIONAMIENTO_PBA_6-P10-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP10'][1], POSICIONAMIENTO_PBA_6P10, 'POSICIONAMIENTO_PBA_6-P10-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP10'][2], 'POSICIONAMIENTO_PBA_6-P10-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P11'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP11'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP11'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P11'], 'POSICIONAMIENTO_PBA_6-P11-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP11'][1], POSICIONAMIENTO_PBA_6P11, 'POSICIONAMIENTO_PBA_6-P11-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP11'][2], 'POSICIONAMIENTO_PBA_6-P11-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])
ps['P12'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP12'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP12'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P12'], 'POSICIONAMIENTO_PBA_6-P12-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP12'][1], POSICIONAMIENTO_PBA_6P12, 'POSICIONAMIENTO_PBA_6-P12-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP12'][2], 'POSICIONAMIENTO_PBA_6-P12-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])
ps['P13'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP13'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP13'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P13'], 'POSICIONAMIENTO_PBA_6-P13-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP13'][1], POSICIONAMIENTO_PBA_6P13, 'POSICIONAMIENTO_PBA_6-P13-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP13'][2], 'POSICIONAMIENTO_PBA_6-P13-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P14'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP14'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP14'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P14'], 'POSICIONAMIENTO_PBA_6-P14-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP14'][1], POSICIONAMIENTO_PBA_6P14, 'POSICIONAMIENTO_PBA_6-P14-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP14'][2], 'POSICIONAMIENTO_PBA_6-P14-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P15'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP15'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP15'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P15'], 'POSICIONAMIENTO_PBA_6-P15-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP15'][1], POSICIONAMIENTO_PBA_6P15, 'POSICIONAMIENTO_PBA_6-P15-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP15'][2], 'POSICIONAMIENTO_PBA_6-P15-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P16'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP16'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP16'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P16'], 'POSICIONAMIENTO_PBA_6-P16-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP16'][1], POSICIONAMIENTO_PBA_6P16, 'POSICIONAMIENTO_PBA_6-P16-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP16'][2], 'POSICIONAMIENTO_PBA_6-P16-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P17'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP17'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP17'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P17'], 'POSICIONAMIENTO_PBA_6-P17-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP17'][1], POSICIONAMIENTO_PBA_6P17, 'POSICIONAMIENTO_PBA_6-P17-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP17'][2], 'POSICIONAMIENTO_PBA_6-P17-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P18'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP18'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP18'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P18'], 'POSICIONAMIENTO_PBA_6-P18-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP18'][1], POSICIONAMIENTO_PBA_6P18, 'POSICIONAMIENTO_PBA_6-P18-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP18'][2], 'POSICIONAMIENTO_PBA_6-P18-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P19'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP19'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP19'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P19'], 'POSICIONAMIENTO_PBA_6-P19-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP19'][1], POSICIONAMIENTO_PBA_6P19, 'POSICIONAMIENTO_PBA_6-P19-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP19'][2], 'POSICIONAMIENTO_PBA_6-P19-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P20'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP20'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP20'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P20'], 'POSICIONAMIENTO_PBA_6-P20-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP20'][1], POSICIONAMIENTO_PBA_6P20, 'POSICIONAMIENTO_PBA_6-P20-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP20'][2], 'POSICIONAMIENTO_PBA_6-P20-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P21'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP21'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP21'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P21'], 'POSICIONAMIENTO_PBA_6-P21-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP21'][1], POSICIONAMIENTO_PBA_6P21, 'POSICIONAMIENTO_PBA_6-P21-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP21'][2], 'POSICIONAMIENTO_PBA_6-P21-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P22'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP22'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP22'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P22'], 'POSICIONAMIENTO_PBA_6-P22-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP22'][1], POSICIONAMIENTO_PBA_6P22, 'POSICIONAMIENTO_PBA_6-P22-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP22'][2], 'POSICIONAMIENTO_PBA_6-P22-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P23'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP23'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP23'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P23'], 'POSICIONAMIENTO_PBA_6-P23-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP23'][1], POSICIONAMIENTO_PBA_6P23, 'POSICIONAMIENTO_PBA_6-P23-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP23'][2], 'POSICIONAMIENTO_PBA_6-P23-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P24'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP24'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP24'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P24'], 'POSICIONAMIENTO_PBA_6-P24-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP24'][1], POSICIONAMIENTO_PBA_6P24, 'POSICIONAMIENTO_PBA_6-P24-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP24'][2], 'POSICIONAMIENTO_PBA_6-P24-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])
#
# ps['P25'] = html.Div([
#          html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP25'], className='subtituloBloque'),
#          getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP25'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P25'], 'POSICIONAMIENTO_PBA_6-P25-1', showticklabels=False, reverse=False),
#          #html.H3(),
#         #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP25'][1], POSICIONAMIENTO_PBA_6P25, 'POSICIONAMIENTO_PBA_6-P25-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
#          html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
#          getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP25'][2], 'POSICIONAMIENTO_PBA_6-P25-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
# ])

ps['P26'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP26'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP26'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P26'], 'POSICIONAMIENTO_PBA_6-P26-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP26'][1], POSICIONAMIENTO_PBA_6P26, 'POSICIONAMIENTO_PBA_6-P26-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP26'][2], 'POSICIONAMIENTO_PBA_6-P26-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])
ps['P27'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP27'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP27'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P27'], 'POSICIONAMIENTO_PBA_6-P27-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP27'][1], POSICIONAMIENTO_PBA_6P27, 'POSICIONAMIENTO_PBA_6-P27-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP27'][2], 'POSICIONAMIENTO_PBA_6-P27-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P28'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP28'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP28'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P28'], 'POSICIONAMIENTO_PBA_6-P28-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP28'][1], POSICIONAMIENTO_PBA_6P28, 'POSICIONAMIENTO_PBA_6-P28-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP28'][2], 'POSICIONAMIENTO_PBA_6-P28-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])



ps['P30'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP30'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP30'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P30'], 'POSICIONAMIENTO_PBA_6-P30-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP30'][1], POSICIONAMIENTO_PBA_6P30, 'POSICIONAMIENTO_PBA_6-P30-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP30'][2], 'POSICIONAMIENTO_PBA_6-P30-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P32'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP32'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP32'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P32'], 'POSICIONAMIENTO_PBA_6-P32-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP32'][1], POSICIONAMIENTO_PBA_6P32, 'POSICIONAMIENTO_PBA_6-P32-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP32'][2], 'POSICIONAMIENTO_PBA_6-P32-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P34'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP34'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP34'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P34'], 'POSICIONAMIENTO_PBA_6-P34-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP34'][1], POSICIONAMIENTO_PBA_6P34, 'POSICIONAMIENTO_PBA_6-P34-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP34'][2], 'POSICIONAMIENTO_PBA_6-P34-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P36'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP36'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP36'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P36'], 'POSICIONAMIENTO_PBA_6-P36-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP36'][1], POSICIONAMIENTO_PBA_6P36, 'POSICIONAMIENTO_PBA_6-P36-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP36'][2], 'POSICIONAMIENTO_PBA_6-P36-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])
ps['P37'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP37'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP37'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P37'], 'POSICIONAMIENTO_PBA_6-P37-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP37'][1], POSICIONAMIENTO_PBA_6P37, 'POSICIONAMIENTO_PBA_6-P37-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP37'][2], 'POSICIONAMIENTO_PBA_6-P37-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])


ps['P38'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP38'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP38'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P38'], 'POSICIONAMIENTO_PBA_6-P38-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP38'][1], POSICIONAMIENTO_PBA_6P38, 'POSICIONAMIENTO_PBA_6-P38-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP38'][2], 'POSICIONAMIENTO_PBA_6-P38-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P39'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP39'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP39'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P39'], 'POSICIONAMIENTO_PBA_6-P39-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP39'][1], POSICIONAMIENTO_PBA_6P39, 'POSICIONAMIENTO_PBA_6-P39-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP39'][2], 'POSICIONAMIENTO_PBA_6-P39-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P40'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP40'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP40'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P40'], 'POSICIONAMIENTO_PBA_6-P40-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP40'][1], POSICIONAMIENTO_PBA_6P40, 'POSICIONAMIENTO_PBA_6-P40-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP40'][2], 'POSICIONAMIENTO_PBA_6-P40-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])

ps['P41'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP41'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP41'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P41'], 'POSICIONAMIENTO_PBA_6-P41-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP41'][1], POSICIONAMIENTO_PBA_6P41, 'POSICIONAMIENTO_PBA_6-P41-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP41'][2], 'POSICIONAMIENTO_PBA_6-P41-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])



ps['P42'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP42'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP42'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P42'], 'POSICIONAMIENTO_PBA_6-P42-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP42'][1], POSICIONAMIENTO_PBA_6P42, 'POSICIONAMIENTO_PBA_6-P42-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP42'][2], 'POSICIONAMIENTO_PBA_6-P42-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])
ps['P43'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP43'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP43'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P43'], 'POSICIONAMIENTO_PBA_6-P43-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP43'][1], POSICIONAMIENTO_PBA_6P43, 'POSICIONAMIENTO_PBA_6-P43-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP43'][2], 'POSICIONAMIENTO_PBA_6-P43-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])
ps['P44'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP44'], className='subtituloBloque'),
         getBarplotWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP44'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', paletas['P44'], 'POSICIONAMIENTO_PBA_6-P44-1', showticklabels=False, reverse=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP44'][1], POSICIONAMIENTO_PBA_6P44, 'POSICIONAMIENTO_PBA_6-P44-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesStacked(filesPOSICIONAMIENTO_PBA_6['csvP44'][2], 'POSICIONAMIENTO_PBA_6-P44-3', 'selectTargetPOSICIONAMIENTO_PBA_6', '', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False, crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
])





ps['P45'] = html.Div([
         html.H3(textosPOSICIONAMIENTO_PBA_6['preguntaP45'], className='subtituloBloque'),
         getHBarplotOpcionesWithPalette(filesPOSICIONAMIENTO_PBA_6['csvP45'][0], 'selectTargetPOSICIONAMIENTO_PBA_6','selectOpciones', paletas['P45'], 'POSICIONAMIENTO_PBA_6-P45-1', showticklabels=False),
         #html.H3(),
        #getTimeSeriesLineplot(filesPOSICIONAMIENTO_PBA_6['csvP45'][1], POSICIONAMIENTO_PBA_6P45, 'POSICIONAMIENTO_PBA_6-P45-2', 'selectTargetPOSICIONAMIENTO_PBA_6', opcionesDePreguntasInicial=3),
         html.H3(textosPOSICIONAMIENTO_PBA_6['cruce'], className='subtituloBloque'),
         getCrucesOpinionStacked(filesPOSICIONAMIENTO_PBA_6['csvP45'][2], 'POSICIONAMIENTO_PBA_6-P45-3', 'selectTargetPOSICIONAMIENTO_PBA_6', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanPOSICIONAMIENTO_PBA_6, reorder= False , crucesDict = crucesDictPOSICIONAMIENTO_PBA_6)
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


imagen = plots(filesPOSICIONAMIENTO_PBA_6['csv_imagen'][0],filesPOSICIONAMIENTO_PBA_6['csv_imagen'][3], filesPOSICIONAMIENTO_PBA_6['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetPOSICIONAMIENTO_PBA_6',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanPOSICIONAMIENTO_PBA_6, name='POSICIONAMIENTO_PBA_6-Comparativo',crucesDict = crucesDictPOSICIONAMIENTO_PBA_6, files=filesPOSICIONAMIENTO_PBA_6, tracking='POSICIONAMIENTO_PBA_6'),



ps['imagen1'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_PBA_6['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_PBA_6['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_PBA_6['csv_imagen'][0], 'selectTargetPOSICIONAMIENTO_PBA_6', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_PBA_6-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_PBA_6['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_PBA_6['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_PBA_6['csv_imagen'][1], 'selectTargetPOSICIONAMIENTO_PBA_6', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_PBA_6-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosPOSICIONAMIENTO_PBA_6['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPOSICIONAMIENTO_PBA_6['seleccioneFigura']),
                getStackedBarplot(filesPOSICIONAMIENTO_PBA_6['csv_imagen'][2], 'selectTargetPOSICIONAMIENTO_PBA_6', 'selectOpciones', opinionColorDict, 'POSICIONAMIENTO_PBA_6-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





