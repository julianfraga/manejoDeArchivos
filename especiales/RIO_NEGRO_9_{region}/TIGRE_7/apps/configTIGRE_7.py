from config import *
from especiales.TIGRE_7.apps.txtTIGRE_7 import textosTIGRE_7
from especiales.TIGRE_7.apps.preguntasTIGRE_7 import filesTIGRE_7, preguntas, preguntas_con_opciones
import pandas as pd


opciones_TIGRE_7 = [
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
        {'label': 'Voto octubre 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'},
    ]

def dropdownTargetTIGRE_7(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_TIGRE_7
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesTIGRE_7(id='selectOpcionesTIGRE_7'):
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



paletas["P07"] = {
"Al candidato del Frente de Todos": colores['peron1'],
"Al candidato de Juntos por el Cambio":colores['cambiemos1'],
"Al candidato de los liberales - libertarios":colores['liberales'],
"Al candidato de la Izquierda":colores['izquierda'],
"A otro candidato": colores['otros'],
"No sabe": colores['nosabe']
}

paletas["P08"] = {
"A Julio Zamora por el Frente de Todos": colores['peron2'],
"A Malena Galmarini por el Frente de Todos": colores['peron1'],
"A Segundo Cernadas por Cambiemos": colores['cambiemos1'],
"A Nicolás Massot por Cambiemos": colores['cambiemos2'],
"Al candidato de los liberales libertarios": colores['liberales'],
"A Paula Akerfeld por el Frente de Izquierda": colores['izquierda'],
"No sabe": colores['nosabe']
}


paletas["P10"] = {
    "A Julio Zamora por el Frente de Todos": colores['peron1'],
    "A Segundo Cernadas por Cambiemos": colores['cambiemos1'],
    "A Nicolás Massot por Cambiemos": colores['cambiemos2'],
    "Al candidato de los liberales libertarios": colores['liberales'],
    "A Paula Akerfeld por el Frente de Izquierda": colores['izquierda'],
    "No sabe": colores['nosabe']
}


paletas["P12"] = {
    "A Malena Galmarini por el Frente de Todos": colores['peron1'],
    "A Segundo Cernadas por Cambiemos": colores['cambiemos1'],
    "A Nicolás Massot por Cambiemos": colores['cambiemos2'],
    "Al candidato de los liberales libertarios": colores['liberales'],
    "A Paula Akerfeld por el Frente de Izquierda": colores['izquierda'],
    "No sabe": colores['nosabe']
}






paletas["P19"] = list2dictPalette(
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
paletas["P20"] = paletas["P19"]

paletas["P21"] = list2dictPalette(
    [
        "Agua corriente y cloacas",
        "Energía eléctrica",
        "Red de gas natural",
        "Recolección de residuos",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P22"] = list2dictPalette(
    [
        "Los robos",
        "El narcotráfico",
        "La ausencia de patrulleros y personal policial",
        "Otro",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P23"] = {
"Frente de Todos y el peronismo": colores['peron1'],
"Cambiemos":colores['cambiemos1'],
"Liberales Libertarios":colores['liberales'],
"Izquierda":colores['izquierda'],
"No sabe": colores['nosabe'],
}

paletas["P23"] = {
"Frente de Todos y el peronismo": colores['peron1'],
"Cambiemos":colores['cambiemos1'],
"Liberales Libertarios":colores['liberales'],
"Izquierda":colores['izquierda'],
"No sabe": colores['nosabe'],
}

paletas['P25'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}
paletas['P26'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
}

paletas['P28']  = list2dictPalette(['Seguro lo votaria', 'Quizás lo votaría', 'Nunca lo votaría'], diverging, noSabe=False)

paletas['P27'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros']
}


paletas['P14'] = opinionColorDict
paletas['P15'] = opinionColorDict
paletas['P16'] = opinionColorDict
paletas['P17'] = opinionColorDict
paletas['P18'] = opinionColorDict
paletas['P29'] = opinionColorDict
paletas['P30'] = opinionColorDict
paletas['P31'] = opinionColorDict
paletas['P32'] = opinionColorDict
paletas['P33'] = opinionColorDict
paletas['P34'] = opinionColorDict
paletas['P35'] = opinionColorDict

crucesDictTIGRE_7 = {}
for pregunta, paleta in paletas.items():

    crucesDictTIGRE_7[pregunta] = [textosTIGRE_7['label' + pregunta], paleta]


