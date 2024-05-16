import pandas as pd
import aux
from especiales.MERLO_10.apps.paletas_MERLO_10 import paletas
from especiales.MERLO_10.apps.cuestionario_MERLO_10 import *
from especiales.MERLO_10.apps.txt_MERLO_10 import textos_MERLO_10
from especiales.MERLO_10.apps.files_MERLO_10 import files_MERLO_10
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
        cruces_dict[pregunta] = [textos_MERLO_10 ['label' + pregunta], paleta]

for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():


        pregunta = row.codigo
        if pregunta not in preguntas_ocultas:

            tiene_opciones = preguntas_con_opciones[pregunta]

            ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='MERLO_10', textos=textos_MERLO_10,
                                                   files=files_MERLO_10, paletas=paletas, cruces_dict=cruces_dict,preguntas_ocultas=preguntas_ocultas,
                                                   opciones=tiene_opciones)


def dropdownTarget(id='selectTargetMERLO_10', cantidadDeOpciones=17):
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
        {'label': 'Pontevedra', 'value': '654'},
        {'label': 'Mariano Acosta', 'value': '655A'},
        {'label': 'Libertad', 'value': '653'},
        {'label': 'Parque Gral. San Martín', 'value': '652A'},
        {'label': 'San Antonio de Padua', 'value': '655'},
        {'label': 'Merlo', 'value': '652'},
        #{'label': 'Voto octubre 2019: A. Fernández', 'value': 'Fernández'},
        #{'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        #{'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'}
        ]

    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
        )




