from config import *
from especiales.POSICIONAMIENTO_NACIONAL_2.apps.txtPOSICIONAMIENTO_NACIONAL_2 import textosPOSICIONAMIENTO_NACIONAL_2
from especiales.POSICIONAMIENTO_NACIONAL_2.apps.preguntasPOSICIONAMIENTO_NACIONAL_2 import filesPOSICIONAMIENTO_NACIONAL_2, preguntas, preguntas_con_opciones
import pandas as pd


opciones_POSICIONAMIENTO_NACIONAL_2 = [
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
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Norte Grande', 'value': 'Norte'},
        {'label': 'Región: Patagonia', 'value': 'Sur'},
        {'label': 'Región: Buenos Aires', 'value': 'Buenos Aires'},

    ]

def dropdownTargetPOSICIONAMIENTO_NACIONAL_2(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_POSICIONAMIENTO_NACIONAL_2
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesPOSICIONAMIENTO_NACIONAL_2(id='selectOpciones'):
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

paletas["P06"] = list2dictPalette(['Alta','Media','Baja'], diverging)

paletas["P07"] = list2dictPalette([
    'Estoy de acuerdo',
    'Debería realizarse solo en caso de violación o riesgo de vida de la madre',
    'No estoy de acuerdo',
    'No sabe',
], diverging)



paletas["P08"] = {
    'Del Frente de Todos y el peronismo': colores["peron1"],
    'De Cambiemos': colores["cambiemos"],
    'De los Liberales libertarios': colores["liberales"],
    'De la Izquierda': colores["izquierda"],
    'No sabe': colores["nosabe"]
    }

paletas['P10']= {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}
paletas['P11'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
    }

paletas['P12'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros']
}
paletas['P13'] = list2dictPalette(['Seguro lo votaria', 'Quizás lo votaría', 'Nunca lo votaría', 'No sabe'], diverging)

votaria_paleta = list2dictPalette(['Lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)
votaria_paleta_mujer = list2dictPalette(['La votaría', 'Puede que la vote', 'Nunca la votaría', 'No sabe'], diverging)

paletas["P14"] = votaria_paleta
paletas["P15"] = votaria_paleta
paletas["P16"] =votaria_paleta
paletas["P17"] = votaria_paleta_mujer
paletas["P18"] = votaria_paleta
paletas["P19"] = votaria_paleta
paletas["P20"] = votaria_paleta_mujer
paletas["P21"] = votaria_paleta
paletas["P22"] = votaria_paleta_mujer
paletas["P23"] = votaria_paleta
paletas["P24"] = votaria_paleta


paletas['P25'] = {
'Mauricio Macri presidente – María Eugenia Vidal vice por Cambiemos': colores["cambiemos1"],
'Horacio Rodríguez Larreta presidente - Gerardo Morales vice por Cambiemos': colores["cambiemos2"],
'Alberto Fernández presidente – Daniel Scioli vice por el Frente de Todos': colores["peron2"],
'Cristina Fernández de Kirchner presidenta  - Sergio Massa vice por el Frente de Todos': colores["peron1"],
'Javier Milei presidente - José Luis Espert vice por los liberales': colores["liberales"],
'Otros candidatos': colores["otros"],
}

paletas['P29'] = {
'Cristina Fernández de Kirchner – Sergio Massa por el Frente de Todos': colores["peron1"],
'Mauricio Macri – María Eugenia Vidal por Cambiemos': colores["cambiemos1"],
'Javier Milei – José Luis Espert por los liberales': colores["liberales"],
'Nicolás del Caño – Myriam Bregman por la izquierda': colores["izquierda"],
'Otro candidato': colores["otros"],
}

paletas['P31']= {
'Horacio Rodríguez Larreta presidente – Gerardo Morales vice por Cambiemos': colores["cambiemos1"],
'Alberto Fernández presidente – Daniel Scioli vice por el Frente de Todos': colores["peron1"],
'Javier Milei presidente – José Luis Espert por los liberales': colores["liberales"],
'Nicolás del Caño presidente – Myriam Bregman vice por la izquierda': colores["izquierda"],
'Otro candidato': colores["otros"],
}
paletas['P33'] = {
'Sergio Massa presidente – Wado de Pedro vice por el Frente de Todos': colores["peron1"],
'Patricia Bullrich presidenta – María Eugenia Vidal vice por Cambiemos': colores["cambiemos1"],
'Javier Milei presidente – José Luis Espert vice por los liberales': colores["liberales"],
'Nicolás del Caño presidente – Myriam Bregman vice por la izquierda': colores["izquierda"],
'Otro candidato': colores["otros"],
}


paletas['P35'] = {
'Cristina Fernández de Kirchner presidenta – Sergio Massa vice': colores["peron1"],
'Mauricio Macri presidente – María Eugenia Vidal vice': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}
paletas['P36'] = {
'Alberto Fernández presidente – Daniel Scioli vice': colores["peron1"],
'Horacio Rodríguez Larreta presidente – Gerardo Morales vice': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}
paletas['P37'] = {
'Sergio Massa presidente – Wado de Pedro vice por el Frente de Todos': colores["peron1"],
'Patricia Bullrich presidenta – María Eugenia Vidal vice por Cambiemos': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}





for p in range(38, 48):
    paletas['P' + str(p)] = opinionColorDict

crucesDictPOSICIONAMIENTO_NACIONAL_2 = {}
for pregunta, paleta in paletas.items():

    crucesDictPOSICIONAMIENTO_NACIONAL_2[pregunta] = [textosPOSICIONAMIENTO_NACIONAL_2['label' + pregunta], paleta]


