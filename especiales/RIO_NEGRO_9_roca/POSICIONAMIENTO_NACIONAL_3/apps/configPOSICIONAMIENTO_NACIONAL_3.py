from config import *
from especiales.POSICIONAMIENTO_NACIONAL_3.apps.txtPOSICIONAMIENTO_NACIONAL_3 import textosPOSICIONAMIENTO_NACIONAL_3
from especiales.POSICIONAMIENTO_NACIONAL_3.apps.preguntasPOSICIONAMIENTO_NACIONAL_3 import filesPOSICIONAMIENTO_NACIONAL_3, preguntas, preguntas_con_opciones
import pandas as pd


opinionCoyunturaP66 = list2dictPalette([
    'Creo que es inocente y está siendo perseguida',
    "No sé si cometió delitos, pero están aprovechando para perseguirla",
    "Creo que es culpable y debe ser condenada",
    "No sabe"
], qualitative_strong)


opinionCoyunturaP67 = list2dictPalette([
    'Disminuiría su confianza en el juicio contra Cristina',
    "Es irrelevante que existan vínculos",
    "Aumentaría su confianza en el juicio contra Cristina",
    "No sabe"
], qualitative_strong)


opinionCoyunturaP64 = list2dictPalette(
    [
        'Muy de acuerdo',
        'De acuerdo',
        'Ni de acuerdo ni en desacuerdo',
        'En desacuerdo',
        'Muy en desacuerdo',
        'No sabe'
     ], diverging
)

opinionCoyunturaP65 = opinionCoyunturaP64
opinionCoyunturaP66 = opinionCoyunturaP64
opinionCoyunturaP67 = opinionCoyunturaP64

opciones_POSICIONAMIENTO_NACIONAL_3 = [
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

def dropdownTargetPOSICIONAMIENTO_NACIONAL_3(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_POSICIONAMIENTO_NACIONAL_3
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesPOSICIONAMIENTO_NACIONAL_3(id='selectOpciones'):
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

paletas["P05"] = list2dictPalette(
    [str(i) for i in range(1,10)], "coolwarm", noSabe=False
)

paletas["P06"] = list2dictPalette(
    [str(i) for i in range(1,10)], diverging_reverse, noSabe=False
)

paletas["P07"] = list2dictPalette(
     [str(i) for i in range(1,10)], reversed(sns.diverging_palette(250, 150, n=10, l=70, s=100)), noSabe=False
)



paletas["P09"] = {
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
'Sergio Massa – Wado de Pedro por el Frente de Todos': colores["peron1"],
'Horacio Rodríguez Larreta - Gerardo Morales, por Cambiemos': colores["cambiemos1"],
'Javier Milei – José Luis Espert por los liberales': colores["liberales"],
'Nicolás del Caño – Myriam Bregman por la izquierda': colores["izquierda"],
'Otro candidato': colores["otros"],
}

paletas['P37'] = {
'Cristina Fernández de Kirchner – Sergio Massa por el Frente de Todos': colores["peron1"],
'Horacio Rodríguez Larreta- Gerardo Morales por Cambiemos': colores["cambiemos1"],
'Javier Milei – José Luis Espert por los liberales': colores["liberales"],
'Nicolás del Caño – Myriam Bregman por la izquierda': colores["izquierda"],
'Otro candidato': colores["otros"],
}




paletas['P38'] = {
'Cristina Fernández de Kirchner presidenta – Sergio Massa vice': colores["peron1"],
'Mauricio Macri presidente – María Eugenia Vidal vice': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}
paletas['P39'] = {
'Alberto Fernández presidente – Daniel Scioli vice': colores["peron1"],
'Horacio Rodríguez Larreta presidente – Gerardo Morales vice': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}
paletas['P40'] = {
'Sergio Massa presidente – Wado de Pedro vice por el Frente de Todos': colores["peron1"],
'Patricia Bullrich presidenta – María Eugenia Vidal vice por Cambiemos': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}


paletas['P41'] = {
'Cristina Fernández de Kirchner presidenta – Sergio Massa vice': colores["peron1"],
'Horacio Rodríguez Larreta presidente – Gerardo Morales vice': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}


paletas['P42'] = {
'Sergio Massa presidente – Wado de Pedro vice por el Frente de Todos': colores["peron1"],
'Horacio Rodríguez Larreta presidente – Gerardo Morales vice': colores["cambiemos1"],
'No sabe': colores["nosabe"],
}

paletas['P43'] = opinionColorDict

paletas['P44'] = list2dictPalette(
    [
    "Muy de acuerdo",
    "De acuerdo",
    "Ni de acuerdo ni en desacuerdo",
    "En desacuerdo",
    "Muy en desacuerdo",
    'No sabe'
     ],diverging
)

paletas['P45']  = opinionCoyunturaP62

paletas['P46'] = siNoNoSabeColorDict




for p in range(47, 58):
    paletas['P' + str(p)] = opinionColorDict

crucesDictPOSICIONAMIENTO_NACIONAL_3 = {}
for pregunta, paleta in paletas.items():

    crucesDictPOSICIONAMIENTO_NACIONAL_3[pregunta] = [textosPOSICIONAMIENTO_NACIONAL_3['label' + pregunta], paleta]


