from especiales.PASO_BA.apps.preguntasPASO_BA import filesPASO_BA
from especiales.PASO_BA.apps.txtPASO_BA import textosPASO_BA
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.PASO_BA.apps.txtPASO_BA import textosPASO_BA
from config import *
from especiales.PASO_BA.apps.configPASO_BA import *

from graphs import *
from especiales.PASO_BA.apps.txtPASO_BA import textosPASO_BA as textos
from graph_imagen import plots

preguntas = {}
for pregunta in['P08', 'P09', 'P11','P13','P15']:
        preguntas[pregunta] = textosPASO_BA["label" + pregunta]

# orden_preguntas = []
# for _ in bloques_PASO_BA.values():
#     orden_preguntas.extend(_)


# Layout

ps = {}



ps['P08'] = html.Div([
        html.H3(textosPASO_BA['preguntaP08'], className='subtituloBloque'),
        getBarplotWithPalette(filesPASO_BA['csvP08'][0], 'selectTargetPASO_BA', paletas['P08'], 'PASO_BA-P08-1', showticklabels=False, reverse=False),
        html.H3(textosPASO_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO_BA['csvP08'][2], 'PASO_BA-P08-3', 'selectTargetPASO_BA', '',reorder=False,  crucesDict = crucesDictPASO_BA)
])

ps['P09'] = html.Div([
        html.H3(textosPASO_BA['preguntaP09'], className='subtituloBloque'),
        html.H4("Escenario 1, Massa - Macri.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO_BA['csvP09'][0], 'selectTargetPASO_BA', paletas['P09'], 'PASO_BA-P09-1', showticklabels=False, reverse=False),

        html.H3(textosPASO_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO_BA['csvP09'][2], 'PASO_BA-P09-3', 'selectTargetPASO_BA', '',reorder=False,  crucesDict = crucesDictPASO_BA)
])
ps['P11'] = html.Div([
        html.H3(textosPASO_BA['preguntaP11'], className='subtituloBloque'),
        html.H4("Escenario 2, Cafiero - Macri.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO_BA['csvP11'][0], 'selectTargetPASO_BA', paletas['P11'], 'PASO_BA-P11-1', showticklabels=False, reverse=False),
        html.H3(textosPASO_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO_BA['csvP11'][2], 'PASO_BA-P11-3', 'selectTargetPASO_BA', '',reorder=False, crucesDict = crucesDictPASO_BA)
])
ps['P13'] = html.Div([
        html.H3(textosPASO_BA['preguntaP13'], className='subtituloBloque'),
        html.H4("Escenario 3, Massa - Santilli/Manes.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO_BA['csvP13'][0], 'selectTargetPASO_BA', paletas['P13'], 'PASO_BA-P13-1', showticklabels=False, reverse=False),

        html.H3(textosPASO_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO_BA['csvP13'][2], 'PASO_BA-P13-3', 'selectTargetPASO_BA', '',reorder=False, crucesDict = crucesDictPASO_BA)
])
ps['P15'] = html.Div([
        html.H3(textosPASO_BA['preguntaP15'], className='subtituloBloque'),
        html.H4("Escenario 4, Cafiero - Santilli/Manes.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO_BA['csvP15'][0], 'selectTargetPASO_BA', paletas['P15'], 'PASO_BA-P15-1', showticklabels=False, reverse=False),
        html.H3(textosPASO_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO_BA['csvP15'][2], 'PASO_BA-P15-3', 'selectTargetPASO_BA', '',reorder=False, crucesDict = crucesDictPASO_BA)
])



