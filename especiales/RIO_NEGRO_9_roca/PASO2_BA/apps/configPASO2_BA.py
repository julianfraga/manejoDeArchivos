from config import *
from especiales.PASO2_BA.apps.txtPASO2_BA import textosPASO2_BA
from especiales.PASO2_BA.apps.preguntasPASO2_BA import filesPASO2_BA, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetPASO2_BA(id='selectTargetPASO2_BA', cantidadDeOpciones=13):
    opciones = ['Todos', 'Hombres', 'Mujeres', '16-29 años', '30-49 años', '50-64 años', '65+ años', 'Hasta primario completo', 'Secundario completo/incompleto', 'Terciario completo/incompleto', 'Santiago del Estero', 'La Banda', 'Resto']
    opciones = [{'label': col, 'value':col} for col in opciones]
    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )


opinionBienMalColorDict = list2dictPalette([
    'Mucho mejor',
    'Mejor',
    'Peor',
    'Mucho peor',
    'No sabe'],
    diverging)

opinionMinusculaColorDict = list2dictPalette([
    'Muy buena',
    'Buena',
    'Mala',
    'Muy mala',
    'No sabe'],
    diverging)

opinionAmpliadaColorDict = list2dictPalette([
    'Muy Buena',
    'Buena',
    'Ni buena ni mala',
    'Mala',
    'Muy mala',
    'No sabe'],
    diverging)

opinionColorDict = {**opinionBienMalColorDict, **opinionMinusculaColorDict, **opinionAmpliadaColorDict, **opinionReducidaColorDict}

politica = [
    '#1f78b4',
    "#619bc2",
    "#a6cee3",
    '#ffff5c',
    '#f5f59f',
    '#e31a1c',
    "#33a02c",
    '#b15928']

colores = { p: qualitative for p in preguntas}

colores['P08'] =[ "#87cb67",'#fffd5e', "#f88c51"]

colores['P09'] = [ "#1f78b4","#ffff5c", '#a6cee3', "#33a02c", "#e31a1c"]
colores['P11'] = colores['P09']
colores['P13'] = colores['P09']
colores['P15'] = colores['P09']



paletas = {}
for pregunta in preguntas:
    archivo_cruces = filesPASO2_BA['csv' + pregunta][-1]
    opciones = pd.read_csv(archivo_cruces, nrows=5).columns.tolist()[2:]
    paletas[pregunta] = list2dictPalette(opciones, colores[pregunta], noSabe=False)

crucesDictPASO2_BA = {}
for pregunta, paleta in paletas.items():
    crucesDictPASO2_BA[pregunta] = [textosPASO2_BA['label' + pregunta], paleta]


