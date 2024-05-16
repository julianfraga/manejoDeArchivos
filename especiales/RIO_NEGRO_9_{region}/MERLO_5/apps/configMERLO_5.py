from config import *
from especiales.MERLO_5.apps.txtMERLO_5 import textosMERLO_5
from especiales.MERLO_5.apps.preguntasMERLO_5 import filesMERLO_5, preguntas, preguntas_con_opciones
import pandas as pd


opciones_MERLO_5 = [
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
        {'label': 'Pontevedra', 'value': '654'},
        {'label': 'Mariano Acosta', 'value': '655A'},
        {'label': 'Libertad', 'value': '653'},
        {'label': 'Parque Gral. San Martín', 'value': '652A'},
        {'label': 'San Antonio de Padua', 'value': '655'},
        {'label': 'Merlo', 'value': '652'},
        {'label': 'Voto octubre 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'},
    ]

def dropdownTargetMERLO_5(id='selectTarget', cantidadDeOpciones=10):
    opciones = opciones_MERLO_5
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesMERLO_5(id='selectOpciones_Merlo2'):
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
    'cambiemos1': '#ffff5c',
    'cambiemos2': '#f5f59f',
    'cambiemos_ucr':  "#fc5d5d",
    'izquierda': '#e31a1c',
    'liberales': '#33a02c',
    'otros': "#b15928",
    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454",
    'nosabe':"#c9bebd",
    'nose':"#c9bebd",
}


paletas = {}



paletas['P07'] = opinionColorDict
paletas['P08'] = opinionColorDict
paletas['P09'] = opinionColorDict
paletas['P10'] = opinionColorDict
paletas['P11'] = opinionColorDict
paletas['P12'] = opinionColorDict
paletas['P13'] = opinionColorDict
paletas['P14'] = opinionColorDict



paletas["P15"] = list2dictPalette(
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
paletas["P16"] = paletas["P15"]

paletas["P17"] = list2dictPalette(
    [
        "Agua corriente y cloacas",
        "Energía eléctrica",
        "Red de gas natural",
        "Recolección de residuos",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P18"] = list2dictPalette(
    [
        "Los robos",
        "El narcotráfico",
        "La ausencia de patrulleros y personal policial",
        "Otro",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P19"] = list2dictPalette(
    [
        "Muy buena",
        "Buena",
        "Ni buena ni mala",
        "Mala",
        "Muy mala",
        'No sabe'
    ]
    , diverging
)

paletas["P20"] = list2dictPalette(
    [
        "Que continúe el intendente Julio Zamora",
        "Que continúe Julio Zamora pero con mejoras",
        "Que cambie Julio Zamora pero que se mantengan los avances",
        "Que cambie el intendente Julio Zamora",
    ]
    , diverging,    noSabe=False
)

paletas["P21"] = opinionColorDict
paletas["P22"] = opinionColorDict


paletas["P23"] = {
    "Al candidato del Frente de Todos": colores["peron1"],
    "Al candidato de Juntos por el Cambio": colores["cambiemos1"],
    "Al candidato de la Izquierda": colores["izquierda"],
    "A otro candidato": colores["otros"],
    'No sabe':colores['nosabe'],

}

paletas["P24"] = {
    "A Gustavo Menéndez": colores["peron1"],
    "A Karina Menéndez": colores["peron3"],
    "A Florencia Lizaraso": colores["peron2"],
    "A Raúl Otahacé": colores["otros"],
    'No sabe':colores['nosabe'],

}


paletas['P25'] = {
    "Frente de Todos y el peronismo": colores['peron1'],
    "Cambiemos": colores['cambiemos1'],
    "Liberales": colores['liberales'],
    "Izquierda": colores['izquierda'],
    'No sabe': colores['nose']
}

paletas['P27']  = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}

paletas['P28'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
}

paletas['P29'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Martín Lousteau": colores['otros']
}

paletas['P30']  = list2dictPalette([
    "Seguro lo votaria",
    "Quizás lo votaría",
    "Nunca lo votaría",
    ],
    diverging, noSabe=False)



paletas['P31'] = opinionColorDict
paletas['P32'] = opinionColorDict
paletas['P33'] = opinionColorDict
paletas['P35'] = opinionColorDict
paletas['P34'] = opinionColorDict
paletas['P36'] = opinionColorDict
paletas['P37'] = opinionColorDict


crucesDictMERLO_5 = {}
for pregunta, paleta in paletas.items():

    crucesDictMERLO_5[pregunta] = [textosMERLO_5['label' + pregunta], paleta]


