from config import *
from especiales.POSICIONAMIENTO_PBA_1.apps.txtPOSICIONAMIENTO_PBA_1 import textosPOSICIONAMIENTO_PBA_1
from especiales.POSICIONAMIENTO_PBA_1.apps.preguntasPOSICIONAMIENTO_PBA_1 import filesPOSICIONAMIENTO_PBA_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_POSICIONAMIENTO_PBA_1 = [
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
        {'label': 'GBA', 'value': 'GBA'},
        {'label': 'Interior', 'value': 'Interior'},

    ]

def dropdownTargetPOSICIONAMIENTO_PBA_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_POSICIONAMIENTO_PBA_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesPOSICIONAMIENTO_PBA_1(id='selectOpciones'):
    opciones = [
        {'label': '4 opciones', 'value': '_4opc'},
        {'label': '6 opciones', 'value': '_6opc'},
        #{'label': 'Imputación no lineal de neutros', 'value': '_2opc'}
     ]
    return html.Div([
        html.Label(children='Cantidad de opciones en preguntas de opinión'),
        dcc.Dropdown(
            id=id,
            options=opciones,
            value='_4opc',
            searchable=False,
            clearable=False
        #, style={'display': 'none'}
        )
    ])


colores = {
    'peron1': '#1f78b4',
    'peron2':  "#619bc2",
    'peron3': "#a6cee3",
    'peron_nok': "#a6cee3",
    'cambiemos': '#ffff5c',
    'cambiemos1': '#ffff5c',
    'cambiemos2': '#f5f59f',
    'cambiemos_ucr':  "#fc5d5d",
    'izquierda': '#e31a1c',
    'liberales': '#33a02c',
    'otro': "#b15928",
    'otros': "#b15928",
    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454",
    'nosabe': '#c9bebd',
}


paletas = {}

colores['color'] = 'blue'

paletas["P04"] = list2dictPalette(['Tengo trabajo estable',
 'Realizo changas o trabajos de vez en cuando',
 'No tengo trabajo',
 'Soy jubilado o pensionado'], diverging)

paletas["P05"] = {'Derecha': "#1f78b4",
 'Centro derecha': "#a6cee3",
 'Centro izquierda': "#fb9a99",
 'Izquierda': "#e31a1c",
 'No sabe': colores["nosabe"]}

paletas["P06"] = list2dictPalette(['Muy importante',
 'Algo importante',
 'Nada importante',
 'No sabe'], diverging)

paletas["P07"] = list2dictPalette(['Estoy de acuerdo',
 'Debería realizarse solo en caso de violación o riesgo de vida de la madre',
 'No estoy de acuerdo',
 'No sabe'], diverging)



paletas["P08"] = {'Frente de Todos y el peronismo': colores["peron1"],
 'Cambiemos': colores["cambiemos"],
 'Liberales': colores["liberales"],
 'Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

votaria_paleta = list2dictPalette(['Lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)
votaria_paleta_mujer = list2dictPalette(['La votaría', 'Puede que la vote', 'Nunca la votaría', 'No sabe'], diverging)

paletas["P10"] = votaria_paleta
paletas["P11"] = votaria_paleta
paletas["P12"] =votaria_paleta
paletas["P13"] = votaria_paleta
paletas["P14"] = votaria_paleta_mujer
paletas["P15"] = votaria_paleta

paletas["P16"] = list2dictPalette(['Sí, lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)
paletas["P17"] = list2dictPalette(['Sí, la votaría', 'Puede que la vote', 'Nunca la votaría', 'No sabe'], diverging)


paletas["P18"] = {'Cristina Fernández de Kirchner por el Frente de Todos': colores["peron1"],
 'Mauricio Macri por Cambiemos': colores["cambiemos1"],
 'Javier Milei por los liberales': colores["liberales"],
 'Nicolás del Caño por la izquierda': colores["izquierda"],
 'Otro candidato': colores["otro"]}

paletas["P19"] = {'Horacio Rodríguez Larreta por Cambiemos': colores["cambiemos1"],
 'Alberto Fernández por el Frente de Todos': colores["peron1"],
 'Javier Milei por los liberales': colores["liberales"],
 'Nicolás del Caño por la izquierda': colores["izquierda"],
 'Otro candidato': colores["otros"]}

paletas["P20"] = {'Mauricio Macri presidente Javier Milei vice': colores["cambiemos1"],
 'Sergio Massa presidente Gerardo Morales vice': colores["peron_nok"],
 'Nicolas del Caño presidente Myriam Bregman vice': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P21"] = {'Mauricio Macri presidente Patricia Bullrich vice': colores["cambiemos1"],
 'Alberto Fernández presidente Sergio Massa vice': colores["peron2"],
 'Javier Milei presidente José Luis Espert vice': colores["liberales"],
 'Horacio Rodríguez Larreta presidente Gerardo Morales vice': colores["cambiemos_ucr"],
 'Cristina Fernández de Kirchner presidenta Jorge Capitanich vice': colores["peron1"],
 'Otros candidatos': colores["otros"]}

paletas["P22"] = opinionColorDict

paletas["P23"] = siNoNoSabeColorDict

paletas["P24"] = list2dictPalette([
        'El kirchnerismo',
        'Cambiemos',
        'Los medios de comunicación',
        'Otros',
        'No sabe'
        ], qualitative_strong)


paletas["P25"] = deudasColorDict
paletas["P26"] = ingresosColorDict
paletas["P27"] = opinionColorDict
paletas["P28"] =comparacionColorDict
paletas["P29"] = comparacionColorDict

paletas["P30"] = opinionColorDict
paletas["P40"] = opinionColorDict
paletas["P41"] = opinionColorDict

for p in range(31, 42):
    paletas['P' + str(p)] = opinionColorDict




crucesDictPOSICIONAMIENTO_PBA_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictPOSICIONAMIENTO_PBA_1[pregunta] = [textosPOSICIONAMIENTO_PBA_1['label' + pregunta], paleta]


