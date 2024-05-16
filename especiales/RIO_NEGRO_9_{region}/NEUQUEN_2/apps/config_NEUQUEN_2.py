import pandas as pd
import aux
from especiales.NEUQUEN_2.apps.paletas_NEUQUEN_2 import paletas
from especiales.NEUQUEN_2.apps.cuestionario_NEUQUEN_2 import *
from especiales.NEUQUEN_2.apps.txt_NEUQUEN_2 import textos_NEUQUEN_2
from especiales.NEUQUEN_2.apps.files_NEUQUEN_2 import files_NEUQUEN_2
import dash_core_components as dcc
import dash_html_components as html
from graph_imagen import plots_no_ts
from graphs import getStackedBarplot
from config import opinionColorDict
from txt import textos

preguntas_ocultas = []

ps = {}


cruces_dict = {}
for pregunta, paleta in paletas.items():

    cruces_dict[pregunta] = [textos_NEUQUEN_2['label' + pregunta], paleta]




for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():

    pregunta = row.codigo
    tiene_opciones = preguntas_con_opciones[pregunta]

    ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='NEUQUEN_2', textos=textos_NEUQUEN_2,
                                           files=files_NEUQUEN_2, paletas=paletas, cruces_dict=cruces_dict,
                                           opciones=tiene_opciones
                                           )






def dropdownTarget(id='selectTargetNEUQUEN_2', cantidadDeOpciones=17):
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
        {'label': 'Zona: Capital', 'value': 'Capital'},
        {'label': 'Zona: Interior', 'value': 'Interior'},

    ]
    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )


