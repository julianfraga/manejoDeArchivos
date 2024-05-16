import pandas as pd
import aux
from especiales.POSICIONAMIENTO_CABA_14.apps.paletas_POSICIONAMIENTO_CABA_14 import paletas
from especiales.POSICIONAMIENTO_CABA_14.apps.cuestionario_POSICIONAMIENTO_CABA_14 import *
from especiales.POSICIONAMIENTO_CABA_14.apps.txt_POSICIONAMIENTO_CABA_14 import textos_POSICIONAMIENTO_CABA_14
from especiales.POSICIONAMIENTO_CABA_14.apps.files_POSICIONAMIENTO_CABA_14 import files_POSICIONAMIENTO_CABA_14
import dash_core_components as dcc



ps = {}


cruces_dict = {}
for pregunta, paleta in paletas.items():
    if pregunta not in preguntas_ocultas:

        cruces_dict[pregunta] = [textos_POSICIONAMIENTO_CABA_14['label' + pregunta], paleta]




for _,row in cuestionario[~cuestionario.codigo.isin(preguntas_imagenes)].iterrows():

    pregunta = row.codigo
    tiene_opciones = preguntas_con_opciones[pregunta]

    ps[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='POSICIONAMIENTO_CABA_14', textos=textos_POSICIONAMIENTO_CABA_14,
                                           files=files_POSICIONAMIENTO_CABA_14, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=preguntas_ocultas,
                                           opciones=tiene_opciones
                                           )






def dropdownTarget(id='selectTargetPOSICIONAMIENTO_CABA_14', cantidadDeOpciones=17):
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
        {'label': 'Voto octubre 2019: H. R. Larreta y D. Santilli', 'value': "Rodriguez Larreta/Santilli"},
        {'label': 'Voto octubre 2019: M. Lammens y G. Marziotta', 'value': "Lammens/Marziotta"},
        {'label': 'Voto octubre 2019: M. Tombolini y D. Gasparini', 'value': "Tombolini/Gasparini"},
        {'label': 'Voto octubre 2019: G. Solano y V. Gagliardi', 'value': "Solano/Gagliardi"},

    ]
    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )
