import pandas as pd
import aux
from especiales.INSEGURIDAD.apps.paletas_INSEGURIDAD import paletas
from especiales.INSEGURIDAD.apps.cuestionario_INSEGURIDAD import *
from especiales.INSEGURIDAD.apps.txt_INSEGURIDAD import textos_INSEGURIDAD
from especiales.INSEGURIDAD.apps.files_INSEGURIDAD import files_INSEGURIDAD
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
        cruces_dict[pregunta] = [textos_INSEGURIDAD ['label' + pregunta], paleta]

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():


        pregunta = row.codigo
        if pregunta not in preguntas_ocultas:

            tiene_opciones = preguntas_con_opciones[pregunta]

            ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='INSEGURIDAD', textos=textos_INSEGURIDAD,
                                                   files=files_INSEGURIDAD, paletas=paletas, cruces_dict=cruces_dict,preguntas_ocultas=preguntas_ocultas,
                                                   opciones=tiene_opciones)


def dropdownTarget(id='selectTargetINSEGURIDAD', cantidadDeOpciones=20):
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
        {'label': 'Región: CABA', 'value': 'CABA'},
        {'label': 'Región: 1er Cordón GBA', 'value': '1 cordón GBA'},
        {'label': 'Región: 2do Cordón GBA', 'value': '2 cordón GBA'},
        {'label': 'Región: 3er Cordón GBA', 'value': '3 cordón GBA'},
        {'label': 'Región: Interior GBA', 'value': 'Interior GBA'},
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Cuyo', 'value': 'Cuyo'},
        {'label': 'Región: NEA', 'value': 'NEA'},
        {'label': 'Región: NOA', 'value': 'NOA'},
        {'label': 'Región: Patagonia', 'value': 'Patagonia'}]

    return dcc.Dropdown(
        options=opciones,
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
        )


