from config import *
from especiales.TIGRE_3.apps.txtTIGRE_3 import textosTIGRE_3
from especiales.TIGRE_3.apps.preguntasTIGRE_3 import filesTIGRE_3, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetTIGRE_3(id='selectTargetTIGRE_3', cantidadDeOpciones=13):
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


def dropwdownOpcionesTIGRE_3(id='selectOpciones'):
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
    'blanco':'#8a8a8a',
    'nofue':"#545454"
}


paletas = {}
paletas['P06'] =  {'A Santilli y Manes por Juntos': colores["cambiemos1"],
 'A Tolosa Paz por el Frente de Todos': colores["peron1"],
 'A del Caño por el Frente de Izquierda': colores["izquierda"],
 'A Espert por Avanza libertad': colores["liberales"],
 'A Randazzo "Vamos con vos"': colores["peron_nok"],
 'Votaría en blanco o anularía': colores["blanco"]}


paletas['P08'] =  {'A Segundo cernadas por Juntos': colores["cambiemos1"],
 'A Gisela Zamora por el frente de todos': colores["peron1"],
 'A Juan José Cervetto por avanza libertad': colores["liberales"],
 'A Paula Yamila Akerfeld por el Frente de Izquierda': colores["izquierda"],
 'A Matias Orfo por Vamos con vos': colores["peron_nok"],
 'A Nicolás Viera Dutra por el Partido Unión Celeste y Blanco': colores["cambiemos_ucr"],
 'En blanco o anularía': colores["blanco"]}



paletas['P10'] = {"Victoria Tolosa Paz por el frente de todos": colores['peron1'],
                    "Santilli dentro de la interna de Juntos": colores['cambiemos1'],
                    "Manes dentro de la interna de juntos": colores['cambiemos2'],
                     'A los candidatos de la izquierda': colores["izquierda"],
                     'Espert por avanza libertad': colores["liberales"],
                     'Randazzo por Vamos con vos': colores["peron_nok"],
                    'Otra lista': colores['otros'],
                    'Votó en blanco o anuló': colores["blanco"],
                     'No fue a votar': colores["nofue"]}

paletas['P12'] = {
"Gisela Zamora por el frente de todos": colores["peron1"],
"Segundo cernadas dentro de la interna Juntos": colores["cambiemos1"],
"Nicolas Massot dentro de la interna por juntos": colores["cambiemos2"],
"A los candidatos de avanza libertad": colores["liberales"],
"A los candidatos de vamos con vos": colores["peron_nok"],
"A los candidatos de la izquierda": colores["izquierda"],
"A los candidatos de unión celeste y blanco": colores["cambiemos_ucr"],
"Otra lista": colores["otros"],
"Votó en blanco o anuló": colores["blanco"],
"No fue a votar":  colores["nofue"],
}



paletas['P14'] = list2dictPalette(
    ["Si",
    "Puede ser",
    "No",
        ],
    diverging, noSabe=False
)

#paletas['P11'] = siNoColorDict


paletas['P15'] = opinionColorDict
paletas['P16'] = opinionColorDict
paletas['P17'] = opinionColorDict
paletas['P18'] = opinionColorDict
paletas['P19'] = opinionColorDict


crucesDictTIGRE_3 = {}
for pregunta, paleta in paletas.items():

    crucesDictTIGRE_3[pregunta] = [textosTIGRE_3['label' + pregunta], paleta]


