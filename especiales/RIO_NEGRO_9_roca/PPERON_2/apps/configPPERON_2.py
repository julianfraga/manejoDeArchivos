from config import *
from especiales.PPERON_2.apps.txtPPERON_2 import textosPPERON_2
from especiales.PPERON_2.apps.preguntasPPERON_2 import filesPPERON_2, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetPPERON_2(id='selectTargetPPERON_2', cantidadDeOpciones=13):
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


def dropwdownOpcionesPPERON_2(id='selectOpciones'):
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




paletas['P06'] =  {'Victoria Tolosa Paz para diputada nacional y Walter Enrique Acuña para concejal por el “Frente de todos”':  colores["peron1"],
 'Diego Santilli para diputado nacional y Guido Giana para concejal por “Juntos”': colores["cambiemos1"],
 'Facundo Manes para diputado nacional y Ruben Eduardo Mobilio para concejal por “Juntos”':   colores["cambiemos2"],
 'Florencio Randazzo para diputado nacional y Maico Müller para concejal por “Vamos con vos”': colores["peron_nok"],
 'A la lista de Anibal Regueiro para concejal por “Peronenses Primero”':  "#af8528",
 'A la lista de José Luis Espert para diputado nacional por “Avanza Libertad”':  colores["liberales"],
 'A los candidatos de la izquierda':  colores["izquierda"],
 'Otros Candidatos':  colores["otros"],
 'En blanco o anularía':  colores["blanco"],
 'Cortaría Boleta': "#933502"}

paletas['P10'] =  {'Toloza Paz por el Frente de todos':  colores["peron1"],
 'Diego Santilli dentro de la interna de Juntos por el cambio': colores["cambiemos1"],
 'Facundo Manes dentro de la interna de Juntos por el cambio': colores["cambiemos2"],
 'Florencio Randazzo por el frente "Vamos con vos."': colores["peron_nok"],
 'José Luis Espert por los liberales': colores["liberales"],
 'A los candidatos de la izquierda': colores["izquierda"],
 'Otros candidatos': colores["otros"],
 'Votaría en blanco o anularía': colores["blanco"]}

paletas['P11'] =  {'Walter Enrique Acuña por el “Frente de Todos”': colores["peron1"],
 'Guido Giana dentro de la interna “Juntos”':  colores["cambiemos1"],
 'Ruben Eduardo Mobilio dentro de la interna por “Juntos”':  colores["cambiemos2"],
 'Maico Müller dentro de la interna de “vamos con vos”':  colores["peron_nok"],
 'Anibal Regueiro por “Peronenses Primero”':  "#af8528",
 'Otro candidato': colores["otros"],
 'En blanco o anularía': colores["blanco"]}



paletas['P05'] = list2dictPalette(
    ["Si",
    "Puede ser",
    "No",
        ],
    diverging, noSabe=False
)

paletas['P18'] = siNoColorDict


paletas['P19'] = opinionColorDict
paletas['P20'] = opinionColorDict
paletas['P21'] = opinionColorDict
paletas['P22'] = opinionColorDict


crucesDictPPERON_2 = {}
for pregunta, paleta in paletas.items():

    crucesDictPPERON_2[pregunta] = [textosPPERON_2['label' + pregunta], paleta]


