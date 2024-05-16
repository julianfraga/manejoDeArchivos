from config import *
from especiales.TIGRE.apps.txtTIGRE import textosTIGRE
from especiales.TIGRE.apps.preguntasTIGRE import filesTIGRE, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetTIGRE(id='selectTargetTIGRE', cantidadDeOpciones=13):
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


def dropwdownOpcionesTIGRE(id='selectOpciones'):
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
    'otros': "#b15928"
}


paletas = {}

paletas['P07'] ={
    "A los candidatos del Frente de todos": colores["peron1"],
    "A los candidatos de Juntos por el cambio": colores["cambiemos1"],
    "A los candidatos del Peronismo no kirchnerista, Lavagnismo o randazismo": colores["peron_nok"],
    "A los candidatos de la Izquierda": colores["izquierda"],
    "A los candidatos Liberales": colores["liberales"],
}

paletas['P08'] ={
    "Diego Santilli por el PRO en Juntos por el Cambio": colores["cambiemos1"],
    "Facundo Manes por el radicalismo en Juntos por el Cambio": colores["cambiemos_ucr"],
}

paletas['P09'] = {
    "A los candidatos del Frente de todos": colores["peron1"],
    "A los candidatos de Juntos por el cambio": colores["cambiemos1"],
    "A los candidatos del frente unidos por tigre": colores["peron2"],
    "A los candidatos del Peronismo no kirchnerista, Lavagnismo o randazismo": colores["peron_nok"],
    "A los candidatos de la Izquierda": colores["izquierda"],
    "A los candidatos Liberales": colores["liberales"],
}

paletas['P10'] = list2dictPalette(
    [
     "Luis Samyn Duco",

    "Gonzalo Meschengieser",
    "Micaela Ferraro",
    "Javier Forlenza",
    "Jose Paesani",
"Malena Galmarini",
"Pipo Gorosito",
        ],
    'Blues_r', noSabe=False
)

paletas['P11'] ={
    "Segundo Cernadas": colores["cambiemos1"],
    "Nicolas Massot": colores["cambiemos2"],
}

paletas['P12'] ={
    "Malena Galmarini por el Frente de todos": colores["peron1"],
    "Gisela Zamora por Frente vecinal unidos": colores["peron2"],
    'Segundo cernadas por Juntos por el Cambio': colores["cambiemos1"],
    "Rodriguez Laborde por el Frente de Randazzo": colores["peron_nok"],
    "A los candidatos del frente de izquierda": colores["izquierda"],
    "Cervetto por los liberales": colores["liberales"]
}

paletas['P13'] ={
    "Pipo Gorosito por el Frente de todos": colores["peron1"],
    "Gisela Zamora por Frente vecinal unidos": colores["peron2"],
    'Segundo cernadas por Juntos por el cambio': colores["cambiemos1"],
    "Rodriguez Laborde por el Frente de Randazzo": colores["peron_nok"],
    "A los candidatos del frente de izquierda": colores["izquierda"],
    "Cervetto por los liberales": colores["liberales"]
}

paletas['P14'] ={
    "Micaela Ferraro por el Frente de todos": colores["peron1"],
    "Gisela Zamora por Frente vecinal unidos": colores["peron2"],
    "Segundo cernadas por juntos por el cambio": colores["cambiemos1"],
    "Rodriguez Laborde por el Frente de Randazzo": colores["peron_nok"],
    "A los candidatos del frente de izquierda": colores["izquierda"],
    "Cervetto por los liberales": colores["liberales"]
}

paletas['P15'] ={
    "Luis Samin Duco por el Frente de todos": colores["peron1"],
    "Gisela Zamora por Frente vecinal unidos": colores["peron2"],
    "Segundo cernadas por juntos por el cambio": colores["cambiemos1"],
    "Rodriguez Laborde por el Frente de Randazzo": colores["peron_nok"],
    "A los candidatos del frente de izquierda": colores["izquierda"],
    "Cervetto por los liberales": colores["liberales"]
}


paletas['P16'] = list2dictPalette(
    ["Muy bueno",
    "Bueno",
    "Ni bueno ni malo",
    "Malo",
    "Muy malo",
    "No sabe"],
    diverging
)

for p in range(18,28):
    paletas[f'P{p}'] = opinionColorDict


crucesDictTIGRE = {}
for pregunta, paleta in paletas.items():

    crucesDictTIGRE[pregunta] = [textosTIGRE['label' + pregunta], paleta]


