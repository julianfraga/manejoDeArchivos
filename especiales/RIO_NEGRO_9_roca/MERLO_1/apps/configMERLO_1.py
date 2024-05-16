from config import *
from especiales.MERLO_1.apps.txtMERLO_1 import textosMERLO_1
from especiales.MERLO_1.apps.preguntasMERLO_1 import filesMERLO_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_MERLO_1 = [
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
        {'label': 'Estrato 1', 'value': 'Estrato 1'},
        {'label': 'Estrato 2', 'value': 'Estrato 2'},
        {'label': 'Voto octubre 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'},
        {'label': 'Voto PASO 2021: Frente de Todos', 'value': 'FdT'},
        {'label': 'Voto PASO 2021: Santilli', 'value': 'Santilli'},
        {'label': 'Voto PASO 2021: Manes', 'value': 'Manes'},
        {'label': 'Voto PASO 2021: Randazzo', 'value': 'Randazzo'},
        {'label': 'Voto PASO 2021: Del Caño', 'value': 'Del Caño'},
        {'label': 'Voto PASO 2021: Espert', 'value': 'Espert'},
        {'label': 'Voto PASO 2021: Otro partido', 'value': 'Otros'},
        {'label': 'Voto PASO 2021: En blanco', 'value': 'Blanco'},
        {'label': 'Voto PASO 2021: No fue a votar', 'value': 'No fue a votar'},
    ]

def dropdownTargetMERLO_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_MERLO_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesMERLO_1(id='selectOpciones'):
    opciones = [
        {'label': '3 opciones', 'value': '_3opc'},
        {'label': '5 opciones', 'value': '_5opc'},
        #{'label': 'Imputación no lineal de neutros', 'value': '_2opc'}
     ]
    return html.Div([
        html.Label(children='Cantidad de opciones en preguntas de opinión'),
        dcc.Dropdown(
            id=id,
            options=opciones,
            value='_3opc',
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
    'cambiemos1': '#ffff5c',
    'cambiemos2': '#f5f59f',
    'cambiemos_ucr':  "#fc5d5d",
    'izquierda': '#e31a1c',
    'liberales': '#33a02c',
    'otros': "#b15928",
    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454"
}


paletas = {}

paletas["P09"] = list2dictPalette(
    ['Porque me siento desanimado con la realidad del país', 'Porque estoy en desacuerdo con el gobierno, pero la oposición no me representa', 'Nunca voy a votar', 'Por miedo a la pandemia', 'Porque las PASO no son elecciones importantes']
    , qualitative_strong, noSabe=False
)
paletas["P14"] = {
    "A Tolosa Paz por el Frente de Todos": colores["peron1"],
    "A Santilli y Manes por Juntos": colores["cambiemos1"],
    "A del Caño por el Frente de Izquierda": colores["izquierda"],
    "A Espert por Avanza libertad": colores["liberales"],
    'A Randazzo por "Vamos con vos"': colores["peron_nok"],
    "A Hotton por “+Valores”": colores["cristianos"],
    "Votaría en blanco o anularía": colores["blanco"],

}

paletas["P16"] = {
"A Karina Isabel Menendez por el Frente de todos": colores["peron1"],
"A David Mauricio Zencich por Juntos": colores["cambiemos1"],
"A Flavia Luz Tesone por el Frente de Izquierda": colores["izquierda"],
"A Martín Maximiliano Diaz por Avanza libertad": colores["liberales"],
'A Domingo Palma por “Vamos con vos"': colores["peron_nok"],
"A Juan Domingo Ochoa por Union Celeste y Blanco": colores["cambiemos_ucr"],
"A Gustavo Javier Marchesani por Vocación Social": colores["cristianos"],
"A Claudio Alejandro Ferrari por Republicano Federal": colores["otros"],
"Votaría en blanco o anularía": colores["blanco"],

}
paletas["P18"] = {
    "Diego Santilli y Facundo Manes por “Juntos”": colores["cambiemos1"],
    "Victoria Tolosa Paz por el Frente de todos": colores["peron1"],
    "Nicolás del Caño por el Frente de Izquierda": colores["izquierda"],
    "José Luis Espert por “Avanza Libertad”": colores["liberales"],
    "Florencio Randazzo por “Vamos con vos”": colores["peron_nok"],
    "Cynthia Hotton por “+Valores”": colores["cristianos"],
    "Ninguna en particular": colores["nofue"],
    "No sabe": '#c9bebd',
}
paletas["P19"] = {
    "Diego Santilli y Facundo Manes por “Juntos”": colores["cambiemos1"],
    "Victoria Tolosa Paz por el Frente de todos": colores["peron1"],
    "Nicolás del Caño por el Frente de Izquierda": colores["izquierda"],
    "José Luis Espert por “Avanza Libertad”": colores["liberales"],
    "Florencio Randazzo por “Vamos con vos”": colores["peron_nok"],
    "Cynthia Hotton por “+Valores”": colores["cristianos"],
    "Ninguna en particular": colores["nofue"],
    "No sabe":'#c9bebd',
}

paletas["P20"] = list2dictPalette(
    ['No alcanzan para cubrir las necesidades básicas familiares', 'Solo alcanzan para cubrir las necesidades básicas familiares', 'No alcanzan para cubrir los gastos totales de la familia', 'Alcanzan para cubrir los gastos totales de la familia', 'Tenemos un pequeño excedente, pero es excepcional', 'Tenemos un pequeño excedente habitual que ahorramos o invertimos', 'Tenemos un gran excedente pero es excepcional', 'Tenemos un gran excedente habitual que ahorramos o invertimos', 'No sabe']
, diverging_reverse
)

#paletas['P11'] = siNoColorDict


paletas['P21'] = opinionColorDict
paletas['P22'] = opinionColorDict
paletas['P23'] = opinionColorDict
paletas['P24'] = opinionColorDict
paletas['P25'] = opinionColorDict


crucesDictMERLO_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictMERLO_1[pregunta] = [textosMERLO_1['label' + pregunta], paleta]


