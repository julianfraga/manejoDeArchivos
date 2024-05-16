from config import *
from especiales.SAN_MARTIN_1.apps.txtSAN_MARTIN_1 import textosSAN_MARTIN_1
from especiales.SAN_MARTIN_1.apps.preguntasSAN_MARTIN_1 import filesSAN_MARTIN_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_SAN_MARTIN_1 = [
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
    ]

def dropdownTargetSAN_MARTIN_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_SAN_MARTIN_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesSAN_MARTIN_1(id='selectOpcionesSAN_MARTIN_1'):
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
    'liberales2': '#8ed689',
    'otro': "#b15928",
    'otros': "#b15928",
    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454",
    'nosabe': '#c9bebd',
    'nose': '#c9bebd',
}


paletas = {}

paletas["P06"] = {'En juntos por el Cambio, a Santiago López Medrano con el apoyo de María Eugenía Vidal': colores['cambiemos1'],
 'En Juntos por el cambio, A Andrés Petrillo con el apoyo de Jorge Macri': colores['cambiemos2'],
 'En juntos por el Cambio,a Mauricio D’alessandro': colores['cambiemos_ucr'],
 'En el frente de todos, a Gabriel Katopodis con el apoyo de Alberto Fernández': colores['peron1'],
 'En el frente de todos, a Juan Esleiman con el apoyo de Sergio Massa': colores['peron2'],
 'En el frente de todos, a Leonardo Grosso': colores['peron3'],
 'Al candidato de Javier Milei': colores['liberales'],
 'Al Candidato de la izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P08"] = {'En Juntos por el Cambio, a Santiago López Medrano con el apoyo de María Eugenía Vidal': colores["cambiemos2"],
 'En Juntos por el Cambio, a Andrés Petrillo con el apoyo de Jorge Macri': colores["cambiemos1"],
 'En Juntos por el Cambio, a Mauricio D’alessandro': colores["cambiemos_ucr"],
 'En el Frente de Todos, a Fernando Moreira con el apoyo de Alberto Fernández': colores['peron1'
 ],
 'En el Frente de Todos, a Juan Esleiman con el apoyo de Sergio Massa': colores['peron3'],
 'En el Frente de Todos, a Leonardo Grosso': colores["peron2"],
 'Al candidato de Javier Milei': colores["liberales"],
 'Al Candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]
}


paletas["P10"] = {'A Santiago López Medrano por Juntos por el Cambio': colores['cambiemos'],
 'A Gabriel Katopodis por el Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios': colores['liberales'],
 'Al candidato del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P12"] = {'A Santiago López Medrano por Juntos por el Cambio': colores['cambiemos'],
 'A Fernando Moreira por el Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios': colores['liberales'],
 'Al candidato del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P14"] = {'A Santiago López Medrano por Juntos por el Cambio': colores['cambiemos'],
 'A Juan Esleiman por el Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios': colores['liberales'],
 'Al candidato del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P16"] = {'A Andrés Petrillo por Juntos por el Cambio': colores['cambiemos'],
 'A Gabriel Katopodis por el Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]
}


paletas["P17"] = {'A Andrés Petrillo por Juntos por el Cambio': colores['cambiemos1'],
 'A Fernando Moreira por el Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]
}


paletas["P18"] = {'A Andrés Petrillo por Juntos por el Cambio': colores['cambiemos1'],
 'A Juan Esleiman por el Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]
}
votaria_paleta = list2dictPalette(['Lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)
votaria_paleta_mujer = list2dictPalette(['La votaría', 'Puede que la vote', 'Nunca la votaría', 'No sabe'], diverging)


paletas["P19"] = votaria_paleta


paletas["P20"] = votaria_paleta


paletas["P21"] = votaria_paleta


paletas["P22"] = votaria_paleta


paletas["P23"] = votaria_paleta


paletas["P24"] = votaria_paleta


paletas["P25"] = votaria_paleta


paletas["P26"] = {'En Juntos por el Cambio, a Horacio Rodríguez Larreta presidente con Diego Santilli de gobernador': colores['cambiemos1'],
 'En Juntos por el Cambio, a Patricia Bullrich presidenta con Joaquín De La Torre de gobernador': colores['cambiemos1'],
 'En el Frente de Todos, a Alberto Fernández presidente con Victoria Tolosa paz de gobernadora': colores['peron2'],
 'En el Frente de Todos, a Sergio Massa presidente con Axel Kicillof de gobernador': colores['peron1'],
 'Por los liberales, a  Javier Milei presidente con Carolina Píparo de gobernadora': colores['liberales'],
 'Solo como gobernador a José Luis Espert': colores['liberales2'],
 'A los candidatos a presidente y gobernador del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P27"] = {'En Juntos por el Cambio, a Mauricio Macri presidente con Cristian Ritondo de gobernador': colores['cambiemos1'],
 'En Juntos por el Cambio, a Horacio Rodríguez Larreta presidente con Diego Santilli de gobernador': colores['cambiemos2'],
 'En Juntos por el Cambio, a Patricia Bullrich presidenta con Joaquín De La Torre de gobernador': colores['cambiemos3'],
 'En el Frente de Todos, a Alberto Fernández presidente con Victoria Tolosa paz de gobernadora': colores['peron2'],
 'En el Frente de Todos, a Sergio Massa presidente con Axel Kicillof de gobernador': colores['peron1'],
 'Por los liberales, a Javier Milei presidente con Carolina Píparo de gobernadora': colores['liberales'],
 'Solo como gobernador a José Luis Espert': colores['liberales2'],
 'A los candidatos a presidente y gobernador del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P28"] = {'A Horacio Rodríguez Larreta presidente con Diego Santilli de gobernador por Juntos por el Cambio': colores['cambiemos1'],
 'A Sergio Massa presidente con Axel Kicillof de gobernador por el Frente de Todos': colores['peron1'],
 'A Javier Milei presidente con Carolina Píparo de gobernadora por la Libertad Avanza': colores['liberales'],
 'Solo como gobernador a José Luis Espert': colores['liberales2'],
 'A los candidatos a presidente y gobernador del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P29"] = {'A Patricia Bullrich presidenta con Joaquín De La Torre de gobernador por Juntos por el Cambio': colores['cambiemos1'],
 'A Sergio Massa presidente con Axel Kicillof de gobernador por el Frente de Todos': colores['peron1'],
 'A Javier Milei presidente con Carolina Píparo de gobernadora por la Libertad Avanza': colores['liberales'],
 'Solo como gobernador a José Luis Espert': colores['liberales2'],
 'A los candidatos a presidente y gobernador del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P30"] = {'A Mauricio Macri presidente con Cristian Ritondo de gobernador por Juntos por el Cambio': colores['cambiemos1'],
 'A Sergio Massa presidente con Axel Kicillof de gobernador por el Frente de Todos': colores['peron1'],
 'A Javier Milei presidente con Carolina Píparo de gobernadora por la Libertad Avanza': colores['liberales'],
 'Solo como gobernador a José Luis Espert': colores['liberales2'],
 'A los candidatos a presidente y gobernador del Frente de Izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]
}


paletas["P38"] = opinionColorDict

paletas["P39"] = list2dictPalette(['Que continúe el intendente Fernando Moreira',
 'Que continúe Fernando Moreira pero con mejoras',
 'Que cambie Fernando Moreira pero que se mantengan los avances',
 'Que cambie el intendente Fernando Moreira'], diverging, noSabe=False)



paletas["P40"] = list2dictPalette(['La seguridad',
 'El tránsito',
 'El arreglo de las calles',
 'Los parques y espacios públicos',
 'El sistema de salud',
 'La limpieza de las calles',
 'El deporte y la cultura',
 'La luminaria',
 'No sabe'], qualitative_strong
)


paletas["P41"] = list2dictPalette(['La seguridad',
 'El tránsito',
 'El arreglo de las calles',
 'Los parques y espacios públicos',
 'El sistema de salud',
 'La limpieza de las calles',
 'El deporte y la cultura',
 'La luminaria',
 'No sabe'], qualitative_strong)


paletas["P42"] = list2dictPalette(['Agua corriente y cloacas',
 'Energía eléctrica',
 'Red de gas natural',
 'Recolección de residuos',
 'Ninguno'], qualitative_strong)


paletas["P43"] = list2dictPalette(['Los robos', 'El narcotráfico',
 'La ausencia de patrulleros y personal policial',
 'Otro',
 'Ninguno'], qualitative_strong)




paletas['P31'] = opinionColorDict
paletas['P32'] = opinionColorDict
paletas['P33'] = opinionColorDict
paletas['P34'] = opinionColorDict
paletas['P35'] = opinionColorDict
paletas['P36'] = opinionColorDict
paletas['P37'] = opinionColorDict


crucesDictSAN_MARTIN_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictSAN_MARTIN_1[pregunta] = [textosSAN_MARTIN_1['label' + pregunta], paleta]


