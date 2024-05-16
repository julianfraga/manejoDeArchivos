import pandas as pd
import aux
from especiales.SAN_MARTIN_3.apps.paletas_SAN_MARTIN_3 import paletas
from especiales.SAN_MARTIN_3.apps.cuestionario_SAN_MARTIN_3 import *
from especiales.SAN_MARTIN_3.apps.txt_SAN_MARTIN_3 import textos_SAN_MARTIN_3
from especiales.SAN_MARTIN_3.apps.files_SAN_MARTIN_3 import files_SAN_MARTIN_3
import dash_core_components as dcc
import dash_html_components as html
from graphs import getStackedBarplot
from config import opinionColorDict
from txt import textos
from graph_imagen import *
from permisos import getUser
import configparser

ps = {}


cruces_dict = {}

for pregunta, paleta in paletas.items():
    if pregunta not in preguntas_ocultas:
        cruces_dict[pregunta] = [textos_SAN_MARTIN_3 ['label' + pregunta], paleta]

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():


        pregunta = row.codigo
        if pregunta not in preguntas_ocultas:

            tiene_opciones = preguntas_con_opciones[pregunta]

            ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='SAN_MARTIN_3', textos=textos_SAN_MARTIN_3,
                                                   files=files_SAN_MARTIN_3, paletas=paletas, cruces_dict=cruces_dict,preguntas_ocultas=preguntas_ocultas,
                                                   opciones=tiene_opciones)


def dropdownTarget(id='selectTargetSAN_MARTIN_3', cantidadDeOpciones=17):
    opciones = [
        {'label': 'Todos', 'value': 'Todos'},
        {'label': 'Hombres', 'value': 'Hombres'},
        {'label': 'Mujeres', 'value': 'Mujeres'},
        {'label': '16-29 años', 'value': '16-29 años'},
        {'label': '30-49 años', 'value': '30-49 años'},
        {'label': '50-64 años', 'value': '50-64 años'},
        {'label': '65+ años', 'value': '65+ años'},
        {'label': 'Hasta primario completo', 'value': 'Hasta primario completo'},
        {'label': 'Secundario completo/incompleto', 'value': 'Secundario completo/incompleto'},
        {'label': 'Terciario completo/incompleto', 'value': 'Terciario completo/incompleto'},
        {'label': 'Voto octubre 2019: G. Katopodis', 'value': 'Katopodis'},
        {'label': 'Voto octubre 2019: S. López Medrano', 'value': 'López Medrano'},
        {'label': 'Voto octubre 2019: H. García', 'value': 'García'},
        {'label': 'Voto octubre 2019: G. La Spina', 'value': 'La Spina'},
        {'label': 'Voto octubre 2019: J. Suárez', 'value': 'Suarez'},
        ]




    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
        )
