from config import *
from especiales.MERLO_3.apps.txtMERLO_3 import textosMERLO_3
from especiales.MERLO_3.apps.preguntasMERLO_3 import filesMERLO_3, preguntas, preguntas_con_opciones
import pandas as pd


opciones_MERLO_3 = [
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
    ]

def dropdownTargetMERLO_3(id='selectTarget', cantidadDeOpciones=10):
    opciones = opciones_MERLO_3
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesMERLO_3(id='selectOpciones_Merlo2'):
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



paletas['P06'] = opinionColorDict
paletas['P07'] = opinionColorDict
paletas['P08'] = opinionColorDict
paletas['P09'] = opinionColorDict
paletas['P10'] = opinionColorDict
paletas['P11'] = opinionColorDict
paletas['P12'] = opinionColorDict
paletas['P13'] = opinionColorDict



paletas["P14"] = list2dictPalette(
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
paletas["P15"] = paletas["P14"]

paletas["P16"] = list2dictPalette(
    [
        "Agua corriente y cloacas",
        "Energía eléctrica",
        "Red de gas natural",
        "Recolección de residuos",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P17"] = list2dictPalette(
    [
        "Los robos",
        "El narcotráfico",
        "La ausencia de patrulleros y personal policial",
        "Otro",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P18"] = opinionColorDict
paletas["P19"] = opinionColorDict


paletas["P20"] = {
    "Al candidato del Frente de Todos": colores["peron1"],
    "Al candidato de Juntos por el Cambio": colores["cambiemos1"],
    "Al candidato de la Izquierda": colores["izquierda"],
    "A otro candidato": colores["otros"],
    'No sabe':colores['nosabe'],

}

paletas["P21"] = {
    "A Gustavo Menéndez": colores["peron1"],
    "A Karina Menéndez": colores["peron3"],
    "A Florencia Lizaraso": colores["peron2"],
    "A otro candidato": colores["otros"],
    'No sabe':colores['nosabe'],

}


paletas['P22'] = {
    "Frente de Todos y el peronismo": colores['peron1'],
    "Cambiemos": colores['cambiemos1'],
    "Liberales": colores['liberales'],
    "Izquierda": colores['izquierda'],
    'No sabe': colores['nose']
}

paletas['P24']  = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}

paletas['P25'] = list2dictPalette([
    "Seguro la votaria",
    "Quizás la votaría",
    "Nunca la votaría",
    ],
    diverging, noSabe=False)

paletas['P26'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Martín Lousteau": colores['otros']
}

paletas['P27']  = list2dictPalette([
    "Seguro lo votaria",
    "Quizás lo votaría",
    "Nunca lo votaría",
    ],
    diverging, noSabe=False)



paletas['P28'] = opinionColorDict
paletas['P29'] = opinionColorDict
paletas['P30'] = opinionColorDict
paletas['P32'] = opinionColorDict
paletas['P31'] = opinionColorDict
paletas['P33'] = opinionColorDict
paletas['P34'] = opinionColorDict


crucesDictMERLO_3 = {}
for pregunta, paleta in paletas.items():

    crucesDictMERLO_3[pregunta] = [textosMERLO_3['label' + pregunta], paleta]


