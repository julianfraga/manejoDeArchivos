from especiales.BANCOS_2.apps.preguntasBANCOS_2 import filesBANCOS_2, preguntasQueNoVanBANCOS_2
from especiales.BANCOS_2.apps.txtBANCOS_2 import textosBANCOS_2
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.BANCOS_2.apps.txtBANCOS_2 import textosBANCOS_2
from config import *
from especiales.BANCOS_2.apps.configBANCOS_2 import *
from especiales.BANCOS_2.apps.bloquesBANCOS_2 import bloques_BANCOS_2
from graphs import *
from especiales.BANCOS_2.apps.preguntas import preguntas_df


preguntas = {}
for bloque in bloques_BANCOS_2.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosBANCOS_2["label" + pregunta]

orden_preguntas = []
for _ in bloques_BANCOS_2.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

layout = {}

encuesta = "BANCOS_2"

for i, row in preguntas_df.iterrows():
    pregunta = row.codigo
    ps[pregunta] = html.Div([
             html.H3(textosBANCOS_2['pregunta' + pregunta], className='subtituloBloque'),

             getBarplotWithPalette(filesBANCOS_2['csv' + pregunta][0], f'selectTarget{encuesta}', paletas[pregunta], f'{encuesta}-{pregunta}-1', showticklabels=False, reverse=False),

             html.H3(textosBANCOS_2['cruce'], className='subtituloBloque'),
             getCrucesStacked(filesBANCOS_2['csv' + pregunta][2], f'{encuesta}-{pregunta}-3', f'selectTarget{encuesta}', '', preguntasQueNoVan = preguntasQueNoVanBANCOS_2, reorder= False, crucesDict = crucesDictBANCOS_2)
    ])








