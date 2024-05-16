import pandas as pd
import aux
from especiales.TIGRE_14.apps.paletas_TIGRE_14 import paletas
from especiales.TIGRE_14.apps.cuestionario_TIGRE_14 import *
from especiales.TIGRE_14.apps.txt_TIGRE_14 import textos_TIGRE_14
from especiales.TIGRE_14.apps.files_TIGRE_14 import files_TIGRE_14
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
        cruces_dict[pregunta] = [textos_TIGRE_14 ['label' + pregunta], paleta]

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():


        pregunta = row.codigo
        if pregunta not in preguntas_ocultas:

            tiene_opciones = preguntas_con_opciones[pregunta]

            ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='TIGRE_14', textos=textos_TIGRE_14,
                                                   files=files_TIGRE_14, paletas=paletas, cruces_dict=cruces_dict,preguntas_ocultas=preguntas_ocultas,
                                                   opciones=tiene_opciones)


def dropdownTarget(id='selectTargetTIGRE_14', cantidadDeOpciones=17):
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
        {'label': 'Voto octubre 2019: J. Zamora', 'value': 'Zamora'},
        {'label': 'Voto octubre 2019: S. Cernadas', 'value': 'Cernadas'},
        {'label': 'Voto octubre 2019: J. Laborde Rodríguez', 'value': 'Laborde Rodriguez'},
        {'label': 'Voto octubre 2019: P. Akerfeld', 'value': 'Akerfeld'},
        {'label': 'Región: zona Centro', 'value': 'Centro'},
        {'label': 'Región: zona Norte', 'value': 'Norte'},
        {'label': 'Región: zona Sur', 'value': 'Sur'},
        ]

    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
        )

