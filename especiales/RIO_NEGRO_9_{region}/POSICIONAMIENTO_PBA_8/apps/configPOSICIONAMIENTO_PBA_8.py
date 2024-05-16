from config import *
from especiales.POSICIONAMIENTO_PBA_8.apps.txtPOSICIONAMIENTO_PBA_8 import textosPOSICIONAMIENTO_PBA_8
from especiales.POSICIONAMIENTO_PBA_8.apps.preguntasPOSICIONAMIENTO_PBA_8 import filesPOSICIONAMIENTO_PBA_8, preguntas, preguntas_con_opciones
import pandas as pd


opciones_POSICIONAMIENTO_PBA_8 = [
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

def dropdownTargetPOSICIONAMIENTO_PBA_8(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_POSICIONAMIENTO_PBA_8
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesPOSICIONAMIENTO_PBA_8(id='selectOpciones'):
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
    'cambiemos3': "#dbdb12",
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

paletas["P04"] = list2dictPalette(['Tengo trabajo estable',
 'Realizo changas o trabajos de vez en cuando',
 'No tengo trabajo',
 'Soy jubilado o pensionado'], diverging)

paletas["P05"] = list2dictPalette(
    [str(i) for i in range(1,10)], "coolwarm", noSabe=False
)

paletas["P06"] = list2dictPalette(
    [str(i) for i in range(1,10)], diverging_reverse, noSabe=False
)

paletas["P07"] = list2dictPalette(
     [str(i) for i in range(1,10)], reversed(sns.diverging_palette(250, 150, n=10, l=70, s=100)), noSabe=False
)



paletas["P09"] = {
    'Del Frente de Todos y el peronismo': colores["peron1"],
    'De Juntos por el cambio': colores["cambiemos"],
    'De los Liberales libertarios': colores["liberales"],
    'De la Izquierda': colores["izquierda"],
    'No sabe': colores["nosabe"]
    }

paletas['P10']= {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}
paletas['P11'] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
    }

paletas['P12'] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos1'],
    "A Mauricio Macri": colores['cambiemos'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros']
}
paletas['P13'] = list2dictPalette(['Seguro lo votaria', 'Quizás lo votaría', 'Nunca lo votaría', 'No sabe'], diverging)

votaria_paleta = list2dictPalette(['Lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)
votaria_paleta_mujer = list2dictPalette(['La votaría', 'Puede que la vote', 'Nunca la votaría', 'No sabe'], diverging)

paletas["P14"] = votaria_paleta
paletas["P15"] = votaria_paleta
paletas["P16"] =votaria_paleta
paletas["P17"] = votaria_paleta_mujer
paletas["P18"] = votaria_paleta
paletas["P19"] = votaria_paleta
paletas["P20"] = votaria_paleta_mujer
paletas["P21"] = votaria_paleta
paletas["P22"] = votaria_paleta_mujer


paletas['P23'] = {
"Mauricio Macri por Juntos por el Cambio": colores['cambiemos'],
"Horacio Rodríguez Larreta por Juntos por el Cambio": colores['cambiemos2'],
"Patricia Bullrich por Juntos por el Cambio": colores['cambiemos3'],
"María Eugenia Vidal por Juntos por el Cambio": "#fce279",
"Facundo Manes por Juntos por el Cambio": colores['cambiemos_ucr'],

"Alberto Fernández por el Frente de Todos": colores['peron1'],
"Sergio Massa por el Frente de Todos": colores['peron2'],
"Javier Milei por los liberales libertarios": colores['liberales'],
"Al candidato del Frente de Izquierda": colores['izquierda'],
"No sabe": colores['nosabe'],
}





paletas['P24'] = {
"Horacio Rodríguez Larreta por Juntos por el Cambio": colores['cambiemos'],
"Mauricio Macri por Juntos por el Cambio": colores['cambiemos2'],
"Alberto Fernández por el Frente de Todos": colores['peron1'],
"Sergio Massa por el Frente de Todos": colores['peron2'],
"Javier Milei por los liberales libertarios": colores['liberales'],
"Al candidato del Frente de Izquierda": colores['izquierda'],
"No sabe": colores['nosabe'],
}



paletas['P25'] =  {
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores['cambiemos'],
'Patricia Bullrich por Juntos por el Cambio': colores['cambiemos2'],
'Alberto Fernández por el Frente de Todos': colores['peron1'],
'Sergio Massa por el Frente de Todos': colores['peron2'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'Al candidato del Frente de Izquierda': colores['izquierda'],
'No sabe': colores['nosabe']}




paletas["P26"] = {

'Sergio Massa por el Frente de Todos': colores['peron1'],
'Mauricio Macri por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'Al candidato del Frente de Izquierda': colores['izquierda'],
'No sabe': colores['nosabe'],
}


paletas['P27'] = {
'Alberto Fernández por el Frente de Todos': colores['peron1'],
'Mauricio Macri por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'Al candidato del Frente de Izquierda': colores['izquierda'],
'No sabe': colores['nosabe']}




paletas['P28'] = {

'Alberto Fernández por el Frente de Todos': colores['peron1'],
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'Al candidato del Frente de Izquierda': colores['izquierda'],
'No sabe': colores['nosabe'],
}


paletas['P29'] = {
'Sergio Massa por el Frente de Todos': colores['peron1'],
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'Al candidato del Frente de Izquierda': colores['izquierda'],
'No sabe': colores['nosabe'],
}





paletas['P30'] = {'Sergio Massa por el Frente de Todos': colores['peron1'],
'Patricia Bullrich por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'Al candidato del Frente de Izquierda': colores['izquierda'],
'No sabe': colores['nosabe'],
}




paletas['P32'] = {'Alberto Fernández por el Frente de Todos': colores['peron1'],
'Patricia Bullrich por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'Al candidato del Frente de Izquierda': colores['izquierda'],
'No sabe': colores['nosabe'],
}



paletas['P34'] = {'Sergio Massa por el Frente de Todos': colores['peron1'],
'Mauricio Macri por Juntos por el Cambio': colores['cambiemos'],
'No sabe': colores['nosabe']}




paletas['P35'] = {'Sergio Massa': colores['peron1'],
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores['cambiemos'],
'No sabe': colores['nosabe']
}


paletas['P36'] = {
'Alberto Fernández por el Frente de Todos': colores['peron1'],
'Mauricio Macri por Juntos por el Cambio': colores['cambiemos'],
'No sabe': colores['nosabe']
}



paletas['P37'] = {'Alberto Fernández': colores['peron1'],
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores['cambiemos'],
'No sabe': colores['nosabe']
                  }



paletas['P38'] = {
'Sergio Massa por el Frente de Todos': colores['peron1'],
'Patricia Bullrich por Juntos por el Cambio': colores['cambiemos'],
'No sabe': colores['nosabe']}



paletas['P39'] = {
    'Alberto Fernández por el Frente de Todos': colores['peron1'],
'Patricia Bullrich por Juntos por el Cambio': colores['cambiemos'],
'No sabe': colores['nosabe']
     }



paletas['P40'] = {
'Mauricio Macri por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'No sabe': colores['nosabe']
}



paletas['P41'] = {
'Horacio Rodríguez Larreta por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'No sabe': colores['nosabe']}



paletas['P42'] = {'Patricia Bullrich por Juntos por el Cambio': colores['cambiemos'],
'Javier Milei por los liberales libertarios': colores['liberales'],
'No sabe': colores['nosabe']
                  }





for p in range(int('P43'[1:]), int("P53"[1:])):

    paletas['P' + str(p)] = opinionColorDict

crucesDictPOSICIONAMIENTO_PBA_8 = {}
for pregunta, paleta in paletas.items():

    crucesDictPOSICIONAMIENTO_PBA_8[pregunta] = [textosPOSICIONAMIENTO_PBA_8['label' + pregunta], paleta]


