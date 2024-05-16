import pandas as pd
import aux
from especiales.NEUQUEN_5.apps.paletas_NEUQUEN_5 import paletas
from especiales.NEUQUEN_5.apps.cuestionario_NEUQUEN_5 import *
from especiales.NEUQUEN_5.apps.txt_NEUQUEN_5 import textos_NEUQUEN_5
from especiales.NEUQUEN_5.apps.files_NEUQUEN_5 import files_NEUQUEN_5
import dash_core_components as dcc
import dash_html_components as html
from graphs import getStackedBarplot
from config import opinionColorDict
from txt import textos
from graph_imagen import *


ps = {}


cruces_dict = {}

for pregunta, paleta in paletas.items():
    if pregunta not in preguntas_ocultas:
        cruces_dict[pregunta] = [textos_NEUQUEN_5 ['label' + pregunta], paleta]

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():


        pregunta = row.codigo
        if pregunta not in preguntas_ocultas:

            tiene_opciones = preguntas_con_opciones[pregunta]

            ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='NEUQUEN_5', textos=textos_NEUQUEN_5,
                                                   files=files_NEUQUEN_5, paletas=paletas, cruces_dict=cruces_dict,preguntas_ocultas=preguntas_ocultas,
                                                   opciones=tiene_opciones)


def dropdownTarget(id='selectTargetNEUQUEN_5', cantidadDeOpciones=17):
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
        {'label': 'Voto marzo 2019: Rolo Figueroa', 'value': 'Figueroa'},
        {'label': 'Voto marzo 2019: Marcos Koopmann', 'value': 'Koopmann'},
        {'label': 'Voto marzo 2019: Ramón Rioseco', 'value': 'Rioseco'},
        {'label': 'Voto marzo 2019: Carlos Eguía', 'value': 'Eguía'}
        ]




    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
        )
