import pandas as pd
import aux
from especiales.POSICIONAMIENTO_ESPECIAL_PBA_2.apps.paletas_POSICIONAMIENTO_ESPECIAL_PBA_2 import paletas
from especiales.POSICIONAMIENTO_ESPECIAL_PBA_2.apps.cuestionario_POSICIONAMIENTO_ESPECIAL_PBA_2 import *
from especiales.POSICIONAMIENTO_ESPECIAL_PBA_2.apps.txt_POSICIONAMIENTO_ESPECIAL_PBA_2 import textos_POSICIONAMIENTO_ESPECIAL_PBA_2
from especiales.POSICIONAMIENTO_ESPECIAL_PBA_2.apps.files_POSICIONAMIENTO_ESPECIAL_PBA_2 import files_POSICIONAMIENTO_ESPECIAL_PBA_2
import dash_core_components as dcc
import dash_html_components as html
from graph_imagen import plots_no_ts
from graphs import getStackedBarplot
from config import opinionColorDict
from txt import textos



ps = {}


cruces_dict = {}
for pregunta, paleta in paletas.items():
    if pregunta not in preguntas_ocultas:

        cruces_dict[pregunta] = [textos_POSICIONAMIENTO_ESPECIAL_PBA_2['label' + pregunta], paleta]




for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():

    pregunta = row.codigo

    tiene_opciones = preguntas_con_opciones[pregunta]

    ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='POSICIONAMIENTO_ESPECIAL_PBA_2', textos=textos_POSICIONAMIENTO_ESPECIAL_PBA_2,
                                           files=files_POSICIONAMIENTO_ESPECIAL_PBA_2, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=preguntas_ocultas,
                                           opciones=tiene_opciones
                                           )






def dropdownTarget(id='selectTargetPOSICIONAMIENTO_ESPECIAL_PBA_2', cantidadDeOpciones=17):
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
        {'label': 'Gran Buenos Aires', 'value': 'GBA'},
        {'label': 'Interior de la Provincia de Buenos Aires', 'value': 'Interior'},
    ]
    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )
