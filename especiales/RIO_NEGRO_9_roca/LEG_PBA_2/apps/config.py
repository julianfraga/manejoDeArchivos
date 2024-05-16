import dash_core_components as dcc
import dash_html_components as html
import seaborn as sns
from config import *
from especiales.LEG_PBA_2.apps.txtLEG_PBA_2 import textosLEG_PBA_2


opciones_LEGISLATIVAS = [
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
        {'label': 'Voto PASO 2021: Juntos', 'value': 'Juntos'},
        {'label': 'Voto PASO 2021: Frente de Todos', 'value': 'FdT'},
        {'label': 'Voto PASO 2021: Frente de Izquierda', 'value': 'Izquierda'},
        {'label': 'Voto PASO 2021: Liberales', 'value': 'Liberales'},
        {'label': 'Voto PASO 2021: Otro partido', 'value': 'Otro'},
        {'label': 'Voto PASO 2021: En blanco', 'value': 'Blanco'},
        {'label': 'Voto PASO 2021: No fue a votar', 'value': 'No fue a votar'},
    ]

def dropdownTargetLEGISLATIVAS(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_LEGISLATIVAS
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )


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
    'cristianos': "#4dc2ff",
    'blanco':"#666666"
}

paletas = {}


paletas['P11'] =  {'A Tolosa Paz por el Frente de todos':  colores["peron1"],
 'A Santilli y Manes por Juntos': colores["cambiemos1"],
 'A Randazo por “Vamos con vos"': colores["peron_nok"],
 'A Espert por Avanza libertad': colores["liberales"],
 "A Del Caño por el Frente de Izquierda": colores["izquierda"],
 'Otros candidatos': colores["otros"],
'A Hotton por “+Valores”': colores['cristianos'],
 'Votaría en blanco o anularía': colores["blanco"]}


paletas['P08'] = list2dictPalette(
    ["Si",
    "Puede ser",
    "No",
        ],
    diverging, noSabe=False
)


paletas['P34'] = ingresosColorDict
paletas['P35'] = opinionColorDict
paletas['P36'] = comparacionColorDict
paletas['P37'] = comparacionColorDict
paletas['P46'] = opinionColorDict
paletas['P47'] = opinionColorDict
paletas['P48'] = opinionColorDict
paletas['P49'] = opinionColorDict
paletas['P50'] = opinionColorDict
paletas['P59'] = opinionColorDict
paletas['P61'] = opinionColorDict

cruces_dic_LEG_PBA_2 = {}
for pregunta, paleta in paletas.items():

    cruces_dic_LEG_PBA_2[pregunta] = [textosLEG_PBA_2['label' + pregunta], paleta]

