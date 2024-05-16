from especiales.VACUNAS_1.apps.preguntasVACUNAS_1 import filesVACUNAS_1
from especiales.VACUNAS_1.apps.txtVACUNAS_1 import textosVACUNAS_1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.VACUNAS_1.apps.txtVACUNAS_1 import textosVACUNAS_1
from config import *
from especiales.VACUNAS_1.apps.configVACUNAS_1 import *

from graphs import *
from especiales.VACUNAS_1.apps.txtVACUNAS_1 import textosVACUNAS_1 as textos
from graph_imagen import plots

preguntas = {}
for pregunta in ['P'+str(i).zfill(2) for i in range(6, 36)]:
        preguntas[pregunta] = textosVACUNAS_1["label" + pregunta]

# orden_preguntas = []
# for _ in bloques_VACUNAS_1.values():
#     orden_preguntas.extend(_)


# Layout

ps = {}
reversed = ["x"]
for __pregunta in preguntas:
        if __pregunta  not in reversed:
                ps[__pregunta] = html.Div([
                        html.H3(textosVACUNAS_1['pregunta' + __pregunta], className='subtituloBloque'),
                        getBarplotWithPalette(filesVACUNAS_1['csv' + __pregunta][0], 'selectTargetVACUNAS_1',
                                              paleta_vacunas[__pregunta], 'VACUNAS_1-' + __pregunta + '-1',
                                              showticklabels=False, reverse=False),
                        html.H3(textosVACUNAS_1['cruce'], className='subtituloBloque'),
                        getCrucesStacked(filesVACUNAS_1['csv' + __pregunta][2], 'VACUNAS_1-' + __pregunta + '-3',
                                         'selectTargetVACUNAS_1', '', reorder=False, crucesDict=crucesDictVACUNAS_1)
                ])
        else:
                ps[__pregunta] = html.Div([
                        html.H3(textosVACUNAS_1['pregunta' + __pregunta], className='subtituloBloque'),
                        getBarplotWithPalette(filesVACUNAS_1['csv' + __pregunta][0], 'selectTargetVACUNAS_1',
                                              paleta_vacunas[__pregunta], 'VACUNAS_1-' + __pregunta + '-1',
                                              showticklabels=False, reverse=True),
                        html.H3(textosVACUNAS_1['cruce'], className='subtituloBloque'),
                        getCrucesStackedReverse(filesVACUNAS_1['csv' + __pregunta][2], 'VACUNAS_1-' + __pregunta + '-3',
                                                'selectTargetVACUNAS_1', '', crucesDict=crucesDictVACUNAS_1)
                ])


