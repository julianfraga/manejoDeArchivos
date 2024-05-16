from config import *
from especiales.TIGRE_2.apps.txtTIGRE_2 import textosTIGRE_2
from especiales.TIGRE_2.apps.preguntasTIGRE_2 import filesTIGRE_2, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetTIGRE_2(id='selectTargetTIGRE_2', cantidadDeOpciones=13):
    #opciones = ['Todos', 'Hombres', 'Mujeres', '16-29 años', '30-49 años', '50-64 años', '65+ años', 'Hasta primario completo', 'Secundario completo/incompleto', 'Terciario completo/incompleto', 'Fernandez', 'Macri', 'Lavagna']
    #opciones = [{'label': col, 'value':col} for col in opciones]
    opciones = [{'label': 'Todos', 'value': 'Todos'},
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
    {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'}]

    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )


def dropwdownOpcionesTIGRE_2(id='selectOpciones'):
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


opinionBienMalColorDict = list2dictPalette([
    'Mucho mejor',
    'Mejor',
    'Peor',
    'Mucho peor',
    'No sabe'],
    diverging)

opinionMinusculaColorDict = list2dictPalette([
    'Muy buena',
    'Buena',
    'Mala',
    'Muy mala',
    'No sabe'],
    diverging)

opinionAmpliadaColorDict = list2dictPalette([
    'Muy Buena',
    'Buena',
    'Ni buena ni mala',
    'Mala',
    'Muy mala',
    'No sabe'],
    diverging)

opinionColorDict = {**opinionBienMalColorDict, **opinionMinusculaColorDict, **opinionAmpliadaColorDict, **opinionReducidaColorDict}

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
    'blanco':"#666666"
}


paletas = {}

paletas['P06'] = list2dictPalette(["Julio Zamora","Segundo Cernadas","Otro candidato","En blanco","No sabe"], diverging)

paletas['P07'] ={
    "Victoria Tolosa Paz para diputada nacional y Gisela Zamora para concejal por el frente de todos": colores["peron1"],
    "Santilli para diputado nacional y Segundo cernadas para concejal por Juntos": colores["cambiemos1"],
    "Manes para diputado nacional y Nicolas massot para concejal por juntos":  colores["cambiemos2"],
    "Espert para diputado nacional y Juan José Cervetto para concejal por avanza libertad": colores["liberales"],
    "Espert para diputado nacional y Martin Liserre Moreno para concejal por Republicanos unidos": colores["liberales"],
    "Randazzo para diputado nacional y Matias Orfo para concejal por Vamos con vos": colores["peron3"],
    "Randazzo para diputado nacional y Oscar Hurtado para concejal por vamos con vos": colores["peron3"],
    "Guillermo Moreno para diputado nacional y Andrés “Pichon” Flores para concejal por principios y valores": colores["peron3"],
    "En blanco o anularía": colores["blanco"],
    "A los candidatos de la izquierda": colores["izquierda"],
    "Cortaría Boleta": colores["otros"],
}

paletas['P08'] ={
    "Victoria Tolosa Paz por el frente de todos": colores["peron1"],
    "Santilli dentro de la interna de Juntos": colores["cambiemos1"],
    "Manes dentro de la interna de juntos": colores["cambiemos2"],
    "Espert por avanza libertad": colores["liberales"],
    'Randazzo por Vamos con vos': colores["peron3"],
    "Guillermo Moreno por principios y valores": colores["peron3"],
    "A los candidatos de la izquierda": colores["izquierda"],
    "En blanco o anularía": colores["blanco"],
}

paletas['P09'] = {
    "Gisela Zamora por el frente de todos": colores["peron1"],
    "Segundo cernadas dentro de la interna Juntos": colores["cambiemos1"],
    "Nicolas massot dentro de la interna por juntos":colores["cambiemos2"],
    "Juan José Cervetto dentro de la interna de avanza libertad": colores["liberales"],
    "Matias Orfo dentro de la interna de vamos con vos": colores["peron_nok"],
    "Martin Liserre Moreno por Republicanos unidos dentro de la interna de Avanza libertad": colores["liberales"],
    "Oscar Hurtado dentro de la interna de vamos con vos": colores["peron_nok"],
    "Andrés “Pichon” Flores por principios y valores": colores["peron_nok"],
    "A los candidatos de la izquierda": colores["izquierda"],
    "En blanco o anularía": colores["blanco"],

}


paletas['P10'] = list2dictPalette(
    ["Si",
    "Puede ser",
    "No",
        ],
    diverging, noSabe=False
)

paletas['P11'] = siNoColorDict


paletas['P12'] = opinionColorDict
paletas['P13'] = opinionColorDict
paletas['P14'] = opinionColorDict
paletas['P15'] = opinionColorDict


crucesDictTIGRE_2 = {}
for pregunta, paleta in paletas.items():

    crucesDictTIGRE_2[pregunta] = [textosTIGRE_2['label' + pregunta], paleta]


