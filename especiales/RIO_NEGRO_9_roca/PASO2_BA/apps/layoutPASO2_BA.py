from especiales.PASO2_BA.apps.preguntasPASO2_BA import filesPASO2_BA
from especiales.PASO2_BA.apps.txtPASO2_BA import textosPASO2_BA
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.PASO2_BA.apps.txtPASO2_BA import textosPASO2_BA
from config import *
from especiales.PASO2_BA.apps.configPASO2_BA import *

from graphs import *
from especiales.PASO2_BA.apps.txtPASO2_BA import textosPASO2_BA as textos
from graph_imagen import plots

preguntas = {}
for pregunta in['P08', 'P09','P15', 'P13','P11']:
        preguntas[pregunta] = textosPASO2_BA["label" + pregunta]

# orden_preguntas = []
# for _ in bloques_PASO2_BA.values():
#     orden_preguntas.extend(_)


# Layout

ps = {}



ps['P08'] = html.Div([
        html.H3(textosPASO2_BA['preguntaP08'], className='subtituloBloque'),
        getBarplotWithPalette(filesPASO2_BA['csvP08'][0], 'selectTargetPASO2_BA', paletas['P08'], 'PASO2_BA-P08-1', showticklabels=False, reverse=False),
        html.H3(textosPASO2_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO2_BA['csvP08'][2], 'PASO2_BA-P08-3', 'selectTargetPASO2_BA', '',reorder=True,  crucesDict = crucesDictPASO2_BA)
])

ps['P09'] = html.Div([
        html.H3(textosPASO2_BA['preguntaP09'], className='subtituloBloque'),
        html.H4("Escenario 1, Massa - Macri.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO2_BA['csvP09'][0], 'selectTargetPASO2_BA', paletas['P09'], 'PASO2_BA-P09-1', showticklabels=False, reverse=False),

        html.H3(textosPASO2_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO2_BA['csvP09'][2], 'PASO2_BA-P09-3', 'selectTargetPASO2_BA', '',reorder=True,  crucesDict = crucesDictPASO2_BA)
])

ps['P15'] = html.Div([
        html.H3(textosPASO2_BA['preguntaP15'], className='subtituloBloque'),
        html.H4("Escenario 2, Kirchner - Macri.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO2_BA['csvP15'][0], 'selectTargetPASO2_BA', paletas['P15'], 'PASO2_BA-P15-1', showticklabels=False, reverse=False),
        html.H3(textosPASO2_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO2_BA['csvP15'][2], 'PASO2_BA-P15-3', 'selectTargetPASO2_BA', '',reorder=True, crucesDict = crucesDictPASO2_BA)
])


ps['P11'] = html.Div([
        html.H3(textosPASO2_BA['preguntaP11'], className='subtituloBloque'),
        html.H4("Escenario 4, Kirchner - Manes.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO2_BA['csvP11'][0], 'selectTargetPASO2_BA', paletas['P11'], 'PASO2_BA-P11-1', showticklabels=False, reverse=False),
        html.H3(textosPASO2_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO2_BA['csvP11'][2], 'PASO2_BA-P11-3', 'selectTargetPASO2_BA', '',reorder=True, crucesDict = crucesDictPASO2_BA)
])
ps['P13'] = html.Div([
        html.H3(textosPASO2_BA['preguntaP13'], className='subtituloBloque'),
        html.H4("Escenario 3, Massa - Manes.", className='subtituloBloque'),
        getBarplotWithPalette(filesPASO2_BA['csvP13'][0], 'selectTargetPASO2_BA', paletas['P13'], 'PASO2_BA-P13-1', showticklabels=False, reverse=False),

        html.H3(textosPASO2_BA['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPASO2_BA['csvP13'][2], 'PASO2_BA-P13-3', 'selectTargetPASO2_BA', '',reorder=True, crucesDict = crucesDictPASO2_BA)
])



