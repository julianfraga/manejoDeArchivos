from config import *
from especiales.SANTIAGO.apps.txtSANTIAGO import textosSANTIAGO
from especiales.SANTIAGO.apps.preguntasSANTIAGO import filesSANTIAGO, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetSANTIAGO(id='selectTargetSANTIAGO', cantidadDeOpciones=13):
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


def dropwdownOpcionesSANTIAGO(id='selectOpciones'):
    opciones = [
        {'label': '3 opciones', 'value': '_3opc'},
        {'label': '5 opciones', 'value': '_5opc'},
        {'label': 'Imputación no lineal de neutros', 'value': '_2opc'}]
    return html.Div([
        html.Label(children='Cantidad de opciones en preguntas de opinión'),
        dcc.Dropdown(
            id=id,
            options=opciones,
            value='_5opc',
            searchable=False,
            clearable=False
        , style={'display': 'none'}
        )
    ])


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

colores['P05'] = [ "#1f78b4",'#ffff5c', "#fdbf6f", "#d6c99b"]
colores['P06'] = [ "#1f78b4","#619bc2", '#ffff5c', "#d6c99b", "#fdbf6f", "#d6c99b"]

colores['P08'] = [ "#1f78b4","#619bc2", '#f5f59f',"#fff480", "#f1f100",  '#ffff5c', "#d6c99b", "#fdbf6f", "#d6c99b"]
colores['P09'] = colores['P08']  # Mismas opciones
colores['P10'] = ["#619bc2","#1f78b4", '#ffff5c', "#fdbf6f"]

paletas = {}
for pregunta in preguntas:


    if pregunta in preguntas_con_opciones:
        paletas[pregunta] = opinionColorDict
    else:
        archivo_cruces = filesSANTIAGO['csv' + pregunta][-1]
        opciones = pd.read_csv(archivo_cruces, nrows=5).columns.tolist()[2:]
        paletas[pregunta] = list2dictPalette(opciones, colores[pregunta])

crucesDictSANTIAGO = {}
for pregunta, paleta in paletas.items():
    crucesDictSANTIAGO[pregunta] = [textosSANTIAGO['label' + pregunta], paleta]


