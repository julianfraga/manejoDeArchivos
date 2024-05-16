from config import *
from especiales.PASO_BA.apps.txtPASO_BA import textosPASO_BA
from especiales.PASO_BA.apps.preguntasPASO_BA import filesPASO_BA, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetPASO_BA(id='selectTargetPASO_BA', cantidadDeOpciones=13):
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
colores['P13'] = [ "#1f78b4", '#F7C775', "#ffff5c",'#a6cee3',"#33a02c", "#e31a1c"]
colores['P15'] = [ "#1f78b4", '#F7C775', "#ffff5c",'#a6cee3',"#33a02c", "#e31a1c"]



paletas = {}
for pregunta in preguntas:
    archivo_cruces = filesPASO_BA['csv' + pregunta][-1]
    opciones = pd.read_csv(archivo_cruces, nrows=5).columns.tolist()[2:]
    paletas[pregunta] = list2dictPalette(opciones, colores[pregunta], noSabe=False)

crucesDictPASO_BA = {}
for pregunta, paleta in paletas.items():
    crucesDictPASO_BA[pregunta] = [textosPASO_BA['label' + pregunta], paleta]


