import pandas as pd
import aux
from especiales.HURLINGHAM_2.apps.paletas_HURLINGHAM_2 import paletas
from especiales.HURLINGHAM_2.apps.cuestionario_HURLINGHAM_2 import *
from especiales.HURLINGHAM_2.apps.txt_HURLINGHAM_2 import textos_HURLINGHAM_2
from especiales.HURLINGHAM_2.apps.files_HURLINGHAM_2 import files_HURLINGHAM_2
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
        cruces_dict[pregunta] = [textos_HURLINGHAM_2 ['label' + pregunta], paleta]

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():


        pregunta = row.codigo
        if pregunta not in preguntas_ocultas:

            tiene_opciones = preguntas_con_opciones[pregunta]

            ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='HURLINGHAM_2', textos=textos_HURLINGHAM_2,
                                                   files=files_HURLINGHAM_2, paletas=paletas, cruces_dict=cruces_dict,preguntas_ocultas=preguntas_ocultas,
                                                   opciones=tiene_opciones)


def dropdownTarget(id='selectTargetHURLINGHAM_2', cantidadDeOpciones=17):
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
        {'label': 'Voto Presidente 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto Presidente 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto Presidente 2019: R. Lavagna', 'value': 'Lavagna'},
        {'label': 'Voto Intendente 2019: J. Zabaleta', 'value': 'Zabaleta'},
        {'label': 'Voto Intendente 2019: L. Delfino', 'value': 'Delfino'},
        {'label': 'Voto Intendente 2019: R. De Francesco', 'value': 'De Francesco'},
        {'label': 'Voto Intendente 2019: Leandro Chayan', 'value': 'Chayan'},
        {'label': 'Voto Intendente 2019: J. E. Argüello', 'value': 'Arguello'},
        ]




    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
        )




