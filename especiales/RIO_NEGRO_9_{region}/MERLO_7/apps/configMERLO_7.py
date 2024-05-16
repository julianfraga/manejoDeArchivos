from config import *
from especiales.MERLO_7.apps.txtMERLO_7 import textosMERLO_7
from especiales.MERLO_7.apps.preguntasMERLO_7 import filesMERLO_7, preguntas, preguntas_con_opciones
import pandas as pd


opciones_MERLO_7 = [
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

def dropdownTargetMERLO_7(id='selectTarget', cantidadDeOpciones=10):
    opciones = opciones_MERLO_7
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesMERLO_7(id='selectOpciones_Merlo2'):
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


paletas['P07'] = {
    "A Gustavo Menendez por el Frente de Todos": colores['peron1'],
    "A David Zencich por Juntos por el Cambio": colores['cambiemos1'],
    "A Pablo Cocuzza por Juntos por el Cambio": colores['cambiemos2'],
    "Al candidato de Javier Milei": colores['liberales'],
    "A Cristian Franco por el Frente de Izquierda": colores['izquierda'],
    'A otro candidato': colores['otros']
}

paletas['P09'] = {
    "A Gustavo Menendez por el Frente de Todos": colores['peron1'],
    "A David Zencich por Juntos por el Cambio": colores['cambiemos1'],
    "A Pablo Cocuzza por Juntos por el Cambio": colores['cambiemos2'],
    "Al candidato de Javier Milei": colores['liberales'],
    "A Cristian Franco por el Frente de Izquierda": colores['izquierda'],
    'A otro candidato': colores['otros']
}

paletas['P11'] = {
    "A Gustavo Menendez por el Frente de Todos": colores['peron1'],
    "A David Zencich por Juntos por el Cambio": colores['cambiemos1'],
    "A Pablo Cocuzza por Juntos por el Cambio": colores['cambiemos2'],
    "Al candidato de Javier Milei": colores['liberales'],
    "A Cristian Franco por el Frente de Izquierda": colores['izquierda'],
    'A otro candidato': colores['otros']
}



paletas['P13'] = opinionColorDict
paletas['P14'] = opinionColorDict
paletas['P15'] = opinionColorDict
paletas['P16'] = opinionColorDict
paletas['P17'] = opinionColorDict
paletas['P18'] = opinionColorDict
paletas['P19'] = opinionColorDict
paletas['P20'] = opinionColorDict



paletas["P21"] = list2dictPalette(
    [
    "La seguridad",
    "El tránsito",
    "El arreglo de las calles",
    "El estado de las escuelas y la educación",
    'Los parques y espacios públicos',
    'La limpieza de las calles',
    "El sistema de salud",
    "El deporte y la cultura",
    "La obra pública",
    "La luminaria",
    "No sabe",
    ]
    , qualitative_strong
)

paletas["P22"] = paletas["P21"]

paletas["P23"] = list2dictPalette(
    [
        "Agua corriente y cloacas",
        "Energía eléctrica",
        "Red de gas natural",
        "Recolección de residuos",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P24"] = list2dictPalette(
    [
        "Los robos",
        "El narcotráfico",
        "La ausencia de patrulleros y personal policial",
        "Otro",
        "Ninguno",
    ]
    , qualitative_strong, noSabe=False
)

paletas["P25"] = opinionColorDict
paletas["P26"] = opinionColorDict



paletas['P27'] = {
    "Frente de Todos y el peronismo": colores['peron1'],
    "Cambiemos": colores['cambiemos1'],
    "Liberales": colores['liberales'],
    "Izquierda": colores['izquierda'],
    'No sabe': colores['nose']
}

paletas['P29']  = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}

paletas['P30'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
}

paletas['P31'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Martín Lousteau": colores['otros']
}

paletas['P32']  = list2dictPalette([
    "Seguro lo votaria",
    "Quizás lo votaría",
    "Nunca lo votaría",
    ],
    diverging, noSabe=False)



paletas['P33'] = opinionColorDict
paletas['P34'] = opinionColorDict
paletas['P35'] = opinionColorDict
paletas['P37'] = opinionColorDict
paletas['P36'] = opinionColorDict
paletas['P38'] = opinionColorDict
paletas['P39'] = opinionColorDict


crucesDictMERLO_7 = {}
for pregunta, paleta in paletas.items():

    crucesDictMERLO_7[pregunta] = [textosMERLO_7['label' + pregunta], paleta]


