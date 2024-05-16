import pandas as pd
import aux
from especiales.HURLINGHAM_1.apps.paletas_HURLINGHAM_1 import paletas
from especiales.HURLINGHAM_1.apps.cuestionario_HURLINGHAM_1 import *
from especiales.HURLINGHAM_1.apps.txt_HURLINGHAM_1 import textos_HURLINGHAM_1
from especiales.HURLINGHAM_1.apps.files_HURLINGHAM_1 import files_HURLINGHAM_1
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
        cruces_dict[pregunta] = [textos_HURLINGHAM_1 ['label' + pregunta], paleta]

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():


        pregunta = row.codigo
        if pregunta not in preguntas_ocultas:

            tiene_opciones = preguntas_con_opciones[pregunta]

            ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='HURLINGHAM_1', textos=textos_HURLINGHAM_1,
                                                   files=files_HURLINGHAM_1, paletas=paletas, cruces_dict=cruces_dict,preguntas_ocultas=preguntas_ocultas,
                                                   opciones=tiene_opciones)


def dropdownTarget(id='selectTargetHURLINGHAM_1', cantidadDeOpciones=17):
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
        {'label': 'Voto octubre 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'},
        ]




    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
        )




