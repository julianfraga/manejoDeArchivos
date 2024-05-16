import dash_core_components as dcc
import dash_html_components as html
import seaborn as sns
from config import *
from especiales.PASO_BA_5.apps.txtPASO_BA_5 import textosPASO_BA_5

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
    'blanco':"#666666"
}
#
# PASO_BA_5P09 = {
#     "Toloza Paz": colores['peron1'],
#     "Diego Santilli": colores['cambiemos1'],
#     "Facundo Manes": colores['cambiemos2'],
#     "Florencio Randazzo": colores['peron_nok'],
#     "A los candidatos de la izquierda": colores['izquierda'],
#     "Jose Luis Espert": colores['liberales'],
#     "Otros candidatos": colores['otros'],
#     "Votaría en blanco o anularía": colores['blanco'],
# }
#
# cruces_dic_PASO_BA_5 = crucesDict.copy()
#
# cruces_dic_PASO_BA_5.update({
#     # 'P06': [textos['labelP06'], NacionalP06],
#     # 'P28': [textos['labelP28'], NacionalP28],
#     #'P08': [textos['labelP08'], p08],
#     'P09_convoto': [textosPASO_BA_5['labelP09_convoto'], PASO_BA_5P09],
#     'P09_sinvoto': [textosPASO_BA_5['labelP09_sinvoto'], PASO_BA_5P09],
# })
#

paletas = {}


paletas['P11'] =  {'Al Frente de todos':  colores["peron1"],
 'A Juntos': colores["cambiemos1"],
 'A “Vamos con vos"': colores["peron_nok"],
 'Al Partido Avanza libertad': colores["liberales"],
 'Al Frente de Izquierda': colores["izquierda"],
 'Otros candidatos': colores["otros"],
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

cruces_dic_PASO_BA_5 = {}
for pregunta, paleta in paletas.items():

    cruces_dic_PASO_BA_5[pregunta] = [textosPASO_BA_5['label' + pregunta], paleta]

