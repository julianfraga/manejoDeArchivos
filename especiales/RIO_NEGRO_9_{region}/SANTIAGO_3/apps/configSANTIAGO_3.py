from config import *
from especiales.SANTIAGO_3.apps.txtSANTIAGO_3 import textosSANTIAGO_3
from especiales.SANTIAGO_3.apps.preguntasSANTIAGO_3 import filesSANTIAGO_3, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetSANTIAGO_3(id='selectTargetSANTIAGO_3', cantidadDeOpciones=13):
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


def dropwdownOpcionesSANTIAGO_3(id='selectOpciones'):
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
    'liberales2':'#78c673',
    'otros': "#b15928",
    'blanco':"#666666"
}


paletas = {}

# paletas['P06'] = list2dictPalette(["Julio Zamora","Segundo Cernadas","Otro candidato","En blanco","No sabe"], diverging)

paletas['P05'] ={"Pablo Guillermo Mirolo por el Partido Frente Renovador “Hay Alternativa”": colores["peron3"],
                 "Silvia Noemí Sayago por el Frente Cívico": colores["peron2"],
                 "Facundo José Perez Carletti por Juntos, dentro de la interna de juntos por el cambio": colores["cambiemos1"],
                 "Marcelo Lugones por Cambia Santiago, dentro de la interna de juntos por el cambio": colores["cambiemos2"],
                 "José María Robledo por Voces Libertarias, dentro de la interna de Unite por la libertad y la dignidad": colores[
                     "liberales"],
                 "Luciano Antonio Pavan por Cruzada Santiagueña dentro de la interna de Unite por la libertad y la dignidad": colores[
                     "liberales2"],
                 "Marianella Lezama Hid por Libres del Sur": "#e2b058",
                 "Guillermo Daniel Suarez Melean por el Frente Patriótico Laborista": colores["otros"],
                 "Alguno de los candidatos de la izquierda": colores["izquierda"],
                 "En blanco o anularía": colores["blanco"]}


paletas['P07'] = list2dictPalette(
    ["Si",
    "Puede ser",
    "No",
        ],
    diverging, noSabe=False
)

paletas['P08'] = siNoColorDict


paletas['P09'] = opinionColorDict
paletas['P10'] = opinionColorDict
paletas['P11'] = opinionColorDict
paletas['P12'] = opinionColorDict


crucesDictSANTIAGO_3 = {}
for pregunta, paleta in paletas.items():

    crucesDictSANTIAGO_3[pregunta] = [textosSANTIAGO_3['label' + pregunta], paleta]


