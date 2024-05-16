from especiales.BANCOS_1.apps.preguntasBANCOS_1 import filesBANCOS_1, preguntasQueNoVanBANCOS_1
from especiales.BANCOS_1.apps.txtBANCOS_1 import textosBANCOS_1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.BANCOS_1.apps.txtBANCOS_1 import textosBANCOS_1
from config import *
from especiales.BANCOS_1.apps.configBANCOS_1 import *
from especiales.BANCOS_1.apps.bloquesBANCOS_1 import bloques_BANCOS_1
from graphs import *
from especiales.BANCOS_1.apps.preguntas import preguntas_df


preguntas = {}
for bloque in bloques_BANCOS_1.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosBANCOS_1["label" + pregunta]

orden_preguntas = []
for _ in bloques_BANCOS_1.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

layout = {}

encuesta = "BANCOS_1"

for i, row in preguntas_df.iterrows():
    pregunta = row.codigo
    ps[pregunta] = html.Div([
             html.H3(textosBANCOS_1['pregunta' + pregunta], className='subtituloBloque'),

             getBarplotWithPalette(filesBANCOS_1['csv' + pregunta][0], f'selectTarget{encuesta}', paletas[pregunta], f'{encuesta}-{pregunta}-1', showticklabels=False, reverse=False),

             html.H3(textosBANCOS_1['cruce'], className='subtituloBloque'),
             getCrucesStacked(filesBANCOS_1['csv' + pregunta][2], f'{encuesta}-{pregunta}-3', f'selectTarget{encuesta}', '', preguntasQueNoVan = preguntasQueNoVanBANCOS_1, reorder= True, crucesDict = crucesDictBANCOS_1)
    ])








