import dash_core_components as dcc
import dash_html_components as html
import seaborn as sns
from config import *
from especiales.PASO_BA_4.apps.txtPASO_BA_4 import textosPASO_BA_4


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

PASO_BA_4P09 = {
    "Toloza Paz": colores['peron1'],
    "Diego Santilli": colores['cambiemos1'],
    "Facundo Manes": colores['cambiemos2'],
    "Florencio Randazzo": colores['peron_nok'],
    "A los candidatos de la izquierda": colores['izquierda'],
    "Jose Luis Espert": colores['liberales'],
    "Otros candidatos": colores['otros'],
    "Votaría en blanco o anularía": colores['blanco'],
}


siNoColorDict = dict(zip(['Si', 'No'], diverging_mini))

siNoNoSabeColorDict = dict(zip(['Si', 'No', 'No sabe'], diverging_mini))


politica = [
    '#1f78b4',
    "#619bc2",
    "#a6cee3",
    '#ffff5c',
    '#f5f59f',

    '#e31a1c',
    "#33a02c",
    '#b15928']

NacionalP23 = siNoColorDict

opinionCoyunturaP68 = list2dictPalette([
    'Totalmente de acuerdo',
    'Bastante de acuerdo',
    'Poco de acuerdo',
    'Nada de acuerdo',
    'No sabe'],
    diverging)


opinionCoyunturaP67 = list2dictPalette([
    'Si, hay mucha información en los medios y comprendo las medidas preventivas',
    'Si, hay mucha información, aunque muchas veces es contradictoria',
    'Mas o menos. Es difícil creerle a los que informan',
    'No, la información es escasa y difícil de entender',
    'No, la información no es confiable y es imposible de entender',
    'No sabe'],
    diverging)


opinionCoyunturaP74 = list2dictPalette([
    "La Pfizer, fabricada en Estados Unidos",
    "La Sputnik, fabricada en Rusia",
    "La vacuna de Oxford, fabricada por AstraZeneca en Argentina y México",
    "La vacuna de Oxford, fabricada por AstraZeneca en India",
    'La vacuna China fabricada en China',
    "Me resultan todas confiables",
    "No sabe"],
    qualitative)


traduccionSeries = {
    'Todos': 't1',
    'Hombres': 's1',
    'Mujeres': 's2',
    '16-29 años': 'e1',
    '30-49 años': 'e2',
    '50-64 años': 'e3',
    '65+ años': 'e4',
    'Hasta primario completo': 'ed1',
    'Secundario completo/incompleto': 'ed2',
    'Terciario completo/incompleto': 'ed3',
    'Con enfermedad preexistente': 'sa1',
    'Sin enfermedad Preexistente': 'sa2',
    'GBA2': 'dom1',  # Trick 'GBA2'
    'CABA': 'dom2',
    'Fernandez': 'v1',
    'Macri': 'v2',
    'Lavagna': 'v3',
    'GBA': 'zpba1',
    'Interior': 'zpba2',
    'Centro': 'z1',
    'Norte': 'z2',
    'Sur': 'z3',
    'Buenos Aires': 'z4'
}
opinionCoyunturaP64 = list2dictPalette([
    'Totalmente de acuerdo',
    'Bastante de acuerdo',
    'Poco de acuerdo',
    'Nada de acuerdo',
    'No sabe'],
    diverging)

NacionalP07 = list2dictPalette([
    'Si',
    'Puede ser',
    'No'],
    diverging)

cruces_dic_PASO_BA_4 = {
    'P09_convoto': [textosPASO_BA_4['labelP09_convoto'], PASO_BA_4P09],
    'P09_sinvoto': [textosPASO_BA_4['labelP09_sinvoto'], PASO_BA_4P09],
    'P07': [textosPASO_BA_4 ['labelP08'], NacionalP07],
    'P23': [textosPASO_BA_4['labelP23'], siNoColorDict],
    'P24': [textosPASO_BA_4['labelP24'], problemaColorDict],
    'P30': [textosPASO_BA_4 ['labelP30'], ingresosColorDict],
    #'P33': [textosPASO_BA_4 ['labelP33'], opinionColorDict],
    'P36': [textosPASO_BA_4 ['labelP36'], comparacionColorDict],
    'P33': [textosPASO_BA_4 ['labelP33'], comparacionColorDict],
    'P42': [textosPASO_BA_4 ['labelP42'], opinionColorDict],
    'P43': [textosPASO_BA_4 ['labelP43'], opinionColorDict],
    'P44': [textosPASO_BA_4 ['labelP44'], opinionColorDict],
    'P45': [textosPASO_BA_4 ['labelP45'], opinionColorDict],
    'P64': [textosPASO_BA_4['labelP64'], opinionCoyunturaP64],
    'P67': [textosPASO_BA_4 ['labelP67'], opinionCoyunturaP67],
    'P74': [textosPASO_BA_4 ['labelP74'], opinionCoyunturaP74],
}
