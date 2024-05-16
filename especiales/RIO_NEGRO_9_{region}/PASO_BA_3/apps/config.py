import dash_core_components as dcc
import dash_html_components as html
import seaborn as sns
from config import *
from especiales.PASO_BA_3.apps.txtPASO_BA_3 import textosPASO_BA_3

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

PASO_BA_3P09 = {
    "Toloza Paz": colores['peron1'],
    "Diego Santilli": colores['cambiemos1'],
    "Facundo Manes": colores['cambiemos2'],
    "Florencio Randazzo": colores['peron_nok'],
    "A la izquierda": colores['izquierda'],
    "Jose Luis Espert": colores['liberales'],
    "Otros candidatos": colores['otros'],
    "Votaría en blanco o anularía": colores['blanco'],
}

cruces_dic_PASO_BA_3 = crucesDict.copy()

cruces_dic_PASO_BA_3.update({
    # 'P06': [textos['labelP06'], NacionalP06],
    # 'P28': [textos['labelP28'], NacionalP28],
    #'P08': [textos['labelP08'], p08],
    'P09_convoto': [textosPASO_BA_3['labelP09_convoto'], PASO_BA_3P09],
    'P09_sinvoto': [textosPASO_BA_3['labelP09_sinvoto'], PASO_BA_3P09],
})