from config import *
from especiales.ESCOBAR_1.apps.txtESCOBAR_1 import textosESCOBAR_1
from especiales.ESCOBAR_1.apps.preguntasESCOBAR_1 import filesESCOBAR_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_ESCOBAR_1 = [
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

def dropdownTargetESCOBAR_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_ESCOBAR_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesESCOBAR_1(id='selectOpcionesESCOBAR_1'):
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


paletas['P38'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
}

paletas['P20'] = list2dictPalette([
'Lo votaria',
'Puede que lo vote',
'Nunca lo votaría',
'No sabe',
], diverging
)
paletas['P12'] = list2dictPalette([
'A  Carlos “Beto” Ramil por el Frente de Todos',
'A Roberto Costa por Juntos por el Cambio',
'A Ricardo Choffi por Consenso Federal',
'A Griselda Romariz por los liberales libertarios',
'A Sandro Salazar por el Frente de Izquierda',
'No sabe',
], [
    colores['peron1'], colores['cambiemos1'], colores['otros'], colores['liberales'], colores['izquierda']
]

)
paletas['P15'] = list2dictPalette([
'Lo votaria',
'Puede que lo vote',
'Nunca lo votaría',
'No sabe',
], diverging
)
paletas['P39'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros']
}

paletas['P37'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}


paletas['P14'] = list2dictPalette([
'Lo votaria',
'Puede que lo vote',
'Nunca lo votaría',
'No sabe',
], diverging
)
paletas['P13'] = list2dictPalette([
'A Carlos “Beto” Ramil por el Frente de Todos',
'A Mariano Castagnaro por Juntos por el Cambio',
'A Ricardo Choffi por Consenso Federal',
'A Griselda Romariz por los liberales libertarios',
'A Sandro Salazar por el Frente de Izquierda',
'No sabe',
], [
    colores['peron1'], colores['cambiemos1'], colores['otros'], colores['liberales'], colores['izquierda']
]
)
paletas['P26'] = list2dictPalette([
'Los robos',
'El narcotráfico',
'La ausencia de patrulleros y personal policial',
'Otro',
'Ninguno',
], qualitative_strong
)
paletas['P19'] = list2dictPalette([
'Lo votaria',
'Puede que lo vote',
'Nunca lo votaría',
'No sabe',
], diverging
)
paletas['P10'] = list2dictPalette([
'A Ariel Sujarchuk por el Frente de Todos',
'A Roberto Costa por Juntos por el Cambio',
'A Ricardo Choffi por Consenso Federal',
'A Griselda Romariz por los liberales libertarios',
'A Sandro Salazar por el Frente de Izquierda',
'No sabe',
],  [
    colores['peron1'], colores['cambiemos1'], colores['otros'], colores['liberales'], colores['izquierda']
]
)
paletas['P17'] = list2dictPalette([
'Lo votaria',
'Puede que lo vote',
'Nunca lo votaría',
'No sabe',
], diverging
)
paletas['P22'] = list2dictPalette([
'Que continúe el intendente Ariel Sujarchuk',
'Que continúe Ariel Sujarchuk  pero con mejoras',
'Que cambie Ariel Sujarchuk pero que se mantengan los avances',
'Que cambie el intendente Ariel Sujarchuk',
], diverging, noSabe=False
)
paletas['P25'] = list2dictPalette([
'Agua corriente y cloacas',
'Energía eléctrica',
'Red de gas natural',
'Recolección de residuos',
'Ninguno',
], qualitative_strong
)
paletas['P08'] = list2dictPalette([
'A Ariel Sujarchuk por el Frente de Todos',
'A Roberto Costa por Juntos por el cambio',
'A Mariano Castagnaro por Juntos por el Cambio',
'A Jesica Avejera por Juntos por el Cambio',
'A Ricardo Choffi por  Consenso Federal',
'A Griselda Romariz por los liberales libertarios',
'A Sandro Salazar por el Frente de Izquierda',
'No sabe',
],  [
    colores['peron1'], colores['cambiemos1'], colores['cambiemos2'], colores['cambiemos1'], colores['otros'], colores['liberales'], colores['izquierda']
]
)
paletas['P24'] = list2dictPalette([
'La seguridad',
'El tránsito',
'El arreglo de las calles',
'Los parques y los espacios públicos',
'El sistema de salud',
'La limpieza de las calles',
'El deporte y la cultura',
'La luminaria',
'No sabe',
], qualitative_strong
)
paletas['P23'] = list2dictPalette([
'La seguridad',
'El tránsito',
'El arreglo de las calles',
'Los parques y los espacios públicos',
'El sistema de salud',
'La limpieza de las calles',
'El deporte y la cultura',
'La luminaria',
'No sabe',
], qualitative_strong
)
paletas['P16'] = list2dictPalette([
'Lo votaria',
'Puede que lo vote',
'Nunca lo votaría',
'No sabe',
], diverging
)
paletas['P18'] = list2dictPalette([
'Lo votaria',
'Puede que lo vote',
'Nunca lo votaría',
'No sabe',
], diverging
)
paletas['P09'] = list2dictPalette([
'A Carlos “Beto” Ramil por el Frente de Todos',
'A Roberto Costa por Juntos por el cambio',
'A Mariano Castagnaro por Juntos por el Cambio',
'A Jesica Avejera por Juntos por el Cambio',
'A Ricardo Choffi por Consenso Federal',
'A Griselda Romariz por los liberales libertarios',
'A Sandro Salazar por el Frente de Izquierda',
'No sabe',
],  [
    colores['peron1'], colores['cambiemos1'], colores['cambiemos2'], colores['cambiemos1'], colores['otros'], colores['liberales'], colores['izquierda']
]
)
paletas['P07'] = list2dictPalette([
'Al candidato del Frente de Todos',
'Al candidato de Juntos por el Cambio',
'Al candidato de los liberales - libertarios',
'Al candidato de Consenso Federal',
'Al candidato de la Izquierda',
'A otro candidato',
'No sabe',
],  [
    colores['peron1'], colores['cambiemos1'], colores['liberales'], colores['otros'], colores['izquierda'], colores['peron2']
]
)
paletas['P35'] = list2dictPalette([
'Frente de Todos y el peronismo',
'Cambiemos',
'Liberales Libertarios',
'Izquierda',
'No sabe',
],  [
    colores['peron1'], colores['cambiemos1'], colores['liberales'], colores['izquierda']
]
)
paletas['P40'] = list2dictPalette([
'Seguro lo votaria',
'Quizás lo votaría',
'Nunca lo votaría',
], diverging
)

paletas["P21"] = opinionColorDict

for p in range(27, 35):
    paletas[f"P{p}"] = opinionColorDict

for p in range(41, 48):
    paletas[f"P{p}"] = opinionColorDict

crucesDictESCOBAR_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictESCOBAR_1[pregunta] = [textosESCOBAR_1['label' + pregunta], paleta]


