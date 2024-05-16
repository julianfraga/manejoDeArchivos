from config import *
from especiales.MERLO_8.apps.txtMERLO_8 import textosMERLO_8
from especiales.MERLO_8.apps.preguntasMERLO_8 import filesMERLO_8, preguntas, preguntas_con_opciones
import pandas as pd


opciones_MERLO_8 = [
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

def dropdownTargetMERLO_8(id='selectTarget', cantidadDeOpciones=10):
    opciones = opciones_MERLO_8
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesMERLO_8(id='selectOpciones_Merlo2'):
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
    'otros': "#b15928",
    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454",
    'nosabe':"#c9bebd",
    'nose':"#c9bebd",
}


paletas = {}

paletas["P07"] = {'A Gustavo Menendez por el Frente de Todos con el apoyo de Cristina Kirchner, Sergio Massa y Alberto Fernández': colores["peron1"], 'A David Zencich por Juntos por el Cambio con el apoyo de Horacio Rodríguez Larreta y santilli': colores["cambiemos"], 'A Pablo Cocuzza por Juntos por el Cambio con el apoyo de Patricia Bullrich y joaquin de la torre ': colores["cambiemos2"], 'Al candidato de Milei en el municipio de Merlo': colores["liberales"], 'Al candidato de Espert en la boleta de Espert gobernador': colores["otros"], 'A Cristian Franco por el Frente de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}
paletas["P09"] = {'A Gustavo Menendez por el Frente de Todos con el apoyo de Cristina Kirchner, Sergio Massa y Alberto Fernández': colores["peron1"], 'A David Zencich por Juntos por el Cambio con el apoyo de Horacio Rodríguez Larreta, Patricia Bullrich y Mauricio Macri': colores["cambiemos"], 'Al candidato de Javier Milei en el municipio de Merlo': colores["liberales"], 'Al candidato de José Luis Espert en la boleta de Espert gobernador': colores["otros"], 'A Cristian Franco por el Frente de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}
paletas["P11"] = {'A Gustavo Menendez por el Frente de Todos con el apoyo de Cristina Kirchner, Sergio Massa y Alberto Fernández': colores["peron1"], 'A Pablo Cocuzza por Juntos por el Cambio con el apoyo de Patricia Bullrich, Horacio Rodríguez Larreta y Mauricio Macri': colores["cambiemos"], 'Al candidato de Javier Milei en el municipio de Merlo': colores["liberales"], 'Al candidato de José Luis Espert en la boleta de Espert gobernador': colores["otros"], 'A Cristian Franco por el Frente de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}
paletas['P13'] = opinionColorDict
paletas['P14'] = opinionColorDict
paletas['P15'] = opinionColorDict
paletas['P16'] = opinionColorDict
paletas['P17'] = opinionColorDict



paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria

paletas['P21'] = opinionColorDict
paletas['P22'] = opinionColorDict
paletas['P23'] = opinionColorDict
paletas['P24'] = opinionColorDict
paletas['P25'] = opinionColorDict

paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = list2dictPalette(['La seguridad', 'El tránsito', 'El arreglo de las calles', 'Los parques y espacios públicos', 'El sistema de salud', 'La limpieza de las calles', 'El deporte y la cultura', 'La luminaria', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P32"] = list2dictPalette(['La seguridad', 'El tránsito', 'El arreglo de las calles', 'Los parques y espacios públicos', 'El sistema de salud', 'La limpieza de las calles', 'El deporte y la cultura', 'La luminaria', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P33"] = list2dictPalette(['Agua corriente y cloacas', 'Energía eléctrica', 'Red de gas natural', 'Recolección de residuos', 'Ninguno'], qualitative_strong, noSabe=False)
paletas["P34"] = list2dictPalette(['Los robos', 'El narcotráfico', 'La ausencia de patrulleros y personal policial', 'Otro', 'Ninguno'], qualitative_strong, noSabe=False)
paletas["P35"] = opinionColorDict
paletas["P36"] = opinionColorDict
paletas["P37"] = {'Frente de Todos y el peronismo': colores["peron1"], 'Cambiemos': colores["cambiemos"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}
paletas["P39"] = list2dictPalette(['A Alberto Fernández', 'A Sergio Massa', 'A algún candidato del peronismo', 'A algún candidato del kirchnerismo'], ['#619bc2', '#a6cee3', '#7794a3', '#1f78b4'], noSabe=False)
paletas["P40"] = list2dictPalette(['A Alberto Fernández', 'A Sergio Massa', 'A algún candidato del peronismo', 'A Cristina Fernández de Kirchner'], ['#619bc2', '#a6cee3', '#7794a3', '#1f78b4'], noSabe=False)
paletas["P41"] = list2dictPalette(['A Horacio Rodriguez Larreta', 'A Mauricio Macri', 'A Patricia Bullrich', 'A Facundo Manes', 'A Gerardo Morales'], ['#f5f59f', '#ffff5c', '#edd464', '#fc5d5d', '#b15928', ' #e0976e']
, noSabe=False)

paletas['P42'] = opinionColorDict
paletas['P43'] = opinionColorDict
paletas['P44'] = opinionColorDict
paletas['P45'] = opinionColorDict
paletas['P46'] = opinionColorDict
paletas['P47'] = opinionColorDict
paletas['P48'] = opinionColorDict


crucesDictMERLO_8 = {}
for pregunta, paleta in paletas.items():

    crucesDictMERLO_8[pregunta] = [textosMERLO_8['label' + pregunta], paleta]


