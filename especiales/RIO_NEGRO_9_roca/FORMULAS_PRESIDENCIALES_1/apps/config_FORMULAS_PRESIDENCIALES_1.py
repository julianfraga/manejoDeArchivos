import pandas as pd
import aux
from especiales.FORMULAS_PRESIDENCIALES_1.apps.paletas_FORMULAS_PRESIDENCIALES_1 import paletas
from especiales.FORMULAS_PRESIDENCIALES_1.apps.cuestionario_FORMULAS_PRESIDENCIALES_1 import *
from especiales.FORMULAS_PRESIDENCIALES_1.apps.txt_FORMULAS_PRESIDENCIALES_1 import textos_FORMULAS_PRESIDENCIALES_1
from especiales.FORMULAS_PRESIDENCIALES_1.apps.files_FORMULAS_PRESIDENCIALES_1 import files_FORMULAS_PRESIDENCIALES_1
import dash_core_components as dcc
import dash_html_components as html
from graph_imagen import plots_no_ts
from graphs import getStackedBarplot
from config import siNoColorDict
from txt import textos


preguntas_ocultas = ["P21_todos", "P22_todos", "P23_todos", "P24"]
cruces_dict = {}
for pregunta, paleta in paletas.items():
    if pregunta not in preguntas_ocultas:

        cruces_dict[pregunta] = [textos_FORMULAS_PRESIDENCIALES_1['label' + pregunta], paleta]
ps = {}

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():

    pregunta = row.codigo
    tiene_opciones = preguntas_con_opciones[pregunta]

    ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='FORMULAS_PRESIDENCIALES_1', textos=textos_FORMULAS_PRESIDENCIALES_1,
                                           files=files_FORMULAS_PRESIDENCIALES_1, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=preguntas_ocultas,
                                           opciones=tiene_opciones
                                           )




def dropdownTarget(id='selectTargetFORMULAS_PRESIDENCIALES_1', cantidadDeOpciones=17):
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
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Norte Grande', 'value': 'Norte'},
        {'label': 'Región: Patagonia', 'value': 'Sur'},
        {'label': 'Región: Buenos Aires', 'value': 'Buenos Aires'},

    ]
    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )




