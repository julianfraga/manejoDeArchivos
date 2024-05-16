from config import *
from especiales.GOB_PBA_1.apps.txtGOB_PBA_1 import textosGOB_PBA_1
from especiales.GOB_PBA_1.apps.preguntasGOB_PBA_1 import filesGOB_PBA_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_GOB_PBA_1 = [
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
        {'label': 'Voto octubre 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'},
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Norte Grande', 'value': 'Norte'},
        {'label': 'Región: Patagonia', 'value': 'Sur'},
        {'label': 'Región: Buenos Aires', 'value': 'Buenos Aires'},

    ]

def dropdownTargetGOB_PBA_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_GOB_PBA_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesGOB_PBA_1(id='selectOpciones'):
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
    'cambiemos': '#ffff5c',
    'cambiemos1': '#ffff5c',
    'cambiemos2': '#f5f59f',
    'cambiemos_ucr':  "#fc5d5d",
    'izquierda': '#e31a1c',
    'liberales': '#33a02c',
    'otro': "#b15928",
    'otros': "#b15928",
    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454",
    'nosabe': '#c9bebd',
    'nose': '#c9bebd',
}


paletas = {}

colores['color'] = 'blue'

paletas["P05"] = list2dictPalette(['Tengo trabajo estable',
 'Realizo changas o trabajos de vez en cuando',
 'No tengo trabajo',
 'Soy jubilado o pensionado'], diverging)

paletas["P06"] = list2dictPalette(
    [str(i) for i in range(1,10)], "coolwarm", noSabe=False
)

paletas["P07"] = list2dictPalette(
    [str(i) for i in range(1,10)], diverging_reverse, noSabe=False
)

paletas["P08"] = list2dictPalette(
     [str(i) for i in range(1,10)], reversed(sns.diverging_palette(250, 150, n=10, l=70, s=100)), noSabe=False
)



paletas["P10"] = {
    'Del Frente de Todos y el peronismo': colores["peron1"],
    'De Cambiemos': colores["cambiemos"],
    'De los Liberales libertarios': colores["liberales"],
    'De la Izquierda': colores["izquierda"],
    'No sabe': colores["nosabe"]
    }

paletas['P11']= {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}
paletas['P12'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
    }

paletas['P13'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros']
}

votaria_paleta = list2dictPalette(['Lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)
votaria_paleta_mujer = list2dictPalette(['La votaría', 'Puede que la vote', 'Nunca la votaría', 'No sabe'], diverging)

paletas["P14"] = list2dictPalette(['Seguro lo votaria', 'Quizás lo votaría', 'Nunca lo votaría', 'No sabe'], diverging)
paletas["P15"] = votaria_paleta
paletas["P16"] = votaria_paleta
paletas["P17"] = votaria_paleta
paletas["P18"] = votaria_paleta
paletas["P19"] = votaria_paleta
paletas["P20"] = votaria_paleta
paletas["P21"] = votaria_paleta
paletas["P22"] = votaria_paleta

paletas['P23'] = {

    'Mauricio Macri presidente – Cristian Ritondo gobernador por Juntos por el Cambio': colores["cambiemos"],
    'Horacio Rodríguez Larreta presidente – Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos2"],
    'Patricia Bullrich presidenta – Joaquín de la Torre gobernador por Juntos por el Cambio': colores["cambiemos1"],
    'Alberto Fernández presidente – Gabriel Katopodis gobernador por el Frente de Todos': colores["peron2"],
    'Cristina Fernández de Kirchner presidenta  - Axel Kicillof gobernador por el Frente de Todos': colores["peron1"],
    'Cristina Fernández de Kirchner presidenta  - Sergio Massa gobernador por el Frente de Todos': colores["peron2"],
    'Sergio Massa presidente – Axel Kicillof Gobernador': colores["peron3"],

    "Cristina Fernández de Kirchner presidenta – Sergio Massa gobernador por el Frente de Todos": colores["peron1"],
    "Javier Milei presidente – José Luis Espert gobernador por los liberales": colores["liberales"],
    'Javier Milei presidente - José Luis Espert gobernador por los liberales': colores["liberales"],
    "Javier Milei presidente – José Luis Espert  gobernador por los liberales": colores["liberales"],



    "A los candidatos de la izquierda":colores['izquierda'],
    'Otros candidatos': colores["otros"],"Otro candidato": colores["otros"],
}

paletas['P24'] = paletas['P23']




paletas['P26'] = paletas['P23']

paletas['P28'] = paletas['P23']

paletas['P30'] = paletas['P23']

paletas['P31'] ={

    'Mauricio Macri por Juntos por el Cambio': colores["cambiemos"],
    'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
    'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
    'Facundo Manes por Juntos por el Cambio': colores["cambiemos_ucr"],
    'Alberto Fernández por el Frente de Todos': colores["peron2"],
    'Cristina Fernández de Kirchner por el Frente de Todos': colores["peron1"],
    'Sergio Massa por el Frente de Todos': colores["peron1"],
    'Javier Milei por los liberales libertarios': colores["liberales"],
    "Nicolás del Caño por la izquierda":colores['izquierda'],
    'Otro candidato': colores["otros"],     'Otros candidatos': colores["otros"],
    'Aún no lo tengo decidido': colores['nose']
}
paletas['P33'] = paletas['P31']

paletas['P34'] = paletas['P31']

paletas['P35'] = paletas['P31']

paletas['P36'] = {
'Cristina Fernández de Kirchner por el Frente de Todos': colores["peron1"],
'Mauricio Macri por Juntos por el Cambio': colores["cambiemos"],
'No sabe': colores["nosabe"],
}
paletas['P37'] = {
'Alberto Fernández por el Frente de Todos': colores["peron1"],
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
'No sabe': colores["nosabe"],
}

paletas['P38'] = {
'Sergio Massa presidente por el Frente de Todos': colores["peron1"],
'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
'No sabe': colores["nosabe"],
}

paletas['P39'] = {
'Cristina Fernandez de Kirchner por el Frente de Todos': colores["peron1"],
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
'No sabe': colores["nosabe"],
}
paletas['P40'] ={
    'Sergio Massa presidente por el Frente de Todos': colores["peron1"],
    'Javier Milei por los liberales libertarios': colores["liberales"],
 "No sabe": colores['nosabe']
}

paletas['P41'] ={
    'Sergio Massa por el Frente de Todos': colores["peron1"],
     'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 "No sabe": colores['nosabe']
}

paletas['P42'] ={
    'Sergio Massa por el Frente de Todos': colores["peron1"],
    'Mauricio Macri por Juntos por el Cambio': colores["cambiemos"],
 "No sabe": colores['nosabe']
}


paletas['P43'] ={
"Horacio Rodríguez Larreta por Juntos por el Cambio": colores['cambiemos'],
 "Javier Milei por los liberales libertarios": colores['liberales'],
 "No sabe": colores['nosabe']
}


paletas['P44'] = opinionColorDict




for p in range(int('P44'[1:]), int("P56"[1:])):

    paletas['P' + str(p)] = opinionColorDict

crucesDictGOB_PBA_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictGOB_PBA_1[pregunta] = [textosGOB_PBA_1['label' + pregunta], paleta]


