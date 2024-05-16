from config import *
from especiales.TIGRE_6.apps.txtTIGRE_6 import textosTIGRE_6
from especiales.TIGRE_6.apps.preguntasTIGRE_6 import filesTIGRE_6, preguntas, preguntas_con_opciones
import pandas as pd


opciones_TIGRE_6 = [
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
        {'label': 'Centro', 'value': 'Centro'},
        {'label': 'Norte', 'value': 'Norte'},
        {'label': 'Sur', 'value': 'Sur'},
    ]

def dropdownTargetTIGRE_6(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_TIGRE_6
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesTIGRE_6(id='selectOpcionesTIGRE_6'):
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

#
# colores = {
#     'peron1': '#1f78b4',
#     'peron2':  "#619bc2",
#     'peron3': "#a6cee3",
#     'peron_nok': "#a6cee3",
#     'cambiemos1': '#ffff5c',
#     'cambiemos2': '#f5f59f',
#     'cambiemos_ucr':  "#fc5d5d",
#     'izquierda': '#e31a1c',
#     'liberales': '#33a02c',
#     'otros': "#b15928",
#     'blanco':'#8a8a8a',
#     'cristianos': "#4dc2ff",
#     'nofue':"#545454"
# }


paletas = {}



paletas["P06"] = {
"Al candidato del Frente de Todos": colores['peron1'],
"Al candidato de Juntos por el Cambio":colores['cambiemos1'],
"Al candidato de los liberales - libertarios":colores['liberales'],
"Al candidato de la Izquierda":colores['izquierda'],
"A otro candidato": colores['otros'],
"No sabe": colores['nosabe']
}

paletas["P07"] = {
"A Malena Galmarini": colores['peron1'],
"A Julio Zamora": colores['peron2'],
"No sabe": colores['nosabe']
}




paletas["P13"] = list2dictPalette(
    [
    "La seguridad",
    "El tránsito",
    "El arreglo de las calles",
    "El estado de las escuelas y la educación",
    "El sistema de salud",
    "El deporte y la cultura",
    "La obra pública",
    "La luminaria",
    "No sabe",
    ]
    , qualitative_strong
)
paletas["P14"] = paletas["P13"]

paletas["P15"] = list2dictPalette(
    [
        "Agua corriente y cloacas",
        "Energía eléctrica",
        "Red de gas natural",
        "Recolección de residuos",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P16"] = list2dictPalette(
    [
        "Los robos",
        "El narcotráfico",
        "La ausencia de patrulleros y personal policial",
        "Otro",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P17"] = {
"Frente de Todos y el peronismo": colores['peron1'],
"Cambiemos":colores['cambiemos1'],
"Liberales Libertarios":colores['liberales'],
"Izquierda":colores['izquierda'],
"No sabe": colores['nosabe'],
}

paletas["P17"] = {
"Frente de Todos y el peronismo": colores['peron1'],
"Cambiemos":colores['cambiemos1'],
"Liberales Libertarios":colores['liberales'],
"Izquierda":colores['izquierda'],
"No sabe": colores['nosabe'],
}

paletas['P19'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}
paletas['P20'] = list2dictPalette(['Seguro la votaria', 'Quizás la votaría', 'Nunca la votaría'], diverging, noSabe=False)

paletas['P22']  = list2dictPalette(['Seguro lo votaria', 'Quizás lo votaría', 'Nunca lo votaría'], diverging, noSabe=False)

paletas['P21'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Martín Lousteau": colores['otros']
}


paletas['P08'] = opinionColorDict
paletas['P09'] = opinionColorDict
paletas['P10'] = opinionColorDict
paletas['P11'] = opinionColorDict
paletas['P12'] = opinionColorDict
paletas['P23'] = opinionColorDict
paletas['P24'] = opinionColorDict
paletas['P25'] = opinionColorDict
paletas['P26'] = opinionColorDict
paletas['P27'] = opinionColorDict
paletas['P28'] = opinionColorDict
paletas['P29'] = opinionColorDict

crucesDictTIGRE_6 = {}
for pregunta, paleta in paletas.items():

    crucesDictTIGRE_6[pregunta] = [textosTIGRE_6['label' + pregunta], paleta]


