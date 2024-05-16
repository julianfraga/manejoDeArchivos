from config import *
from especiales.BANCOS_2.apps.txtBANCOS_2 import textosBANCOS_2
from especiales.BANCOS_2.apps.preguntasBANCOS_2 import filesBANCOS_2, preguntas, preguntas_con_opciones
import pandas as pd


opciones_BANCOS_2 = [
        {'label': 'Todos', 'value': 'Todos'},
        {'label': 'Masculino', 'value': 'Masculino'},
        {'label': 'Femenino', 'value': 'Femenino'},
        {'label': 'No binario', 'value': 'No binario'},
        {'label': '16-29 años', 'value': '16-29 años'},
        {'label': '30-49 años', 'value': '30-49 años'},
        {'label': '50-64 años', 'value': '50-64 años'},
        {'label': '65+ años', 'value': '65+ años'},
        {'label': 'Hasta primario completo', 'value': 'Hasta primario completo'},
        {'label': 'Secundario completo/incompleto', 'value': 'Secundario completo/incompleto'},
        {'label': 'Terciario completo/incompleto', 'value': 'Terciario completo/incompleto'},
        {'label': 'Región: CABA', 'value': 'CABA'},
        {'label': 'Región: 1er Cordón GBA', 'value': '1 cordón GBA'},
        {'label': 'Región: 2do Cordón GBA', 'value': '2 cordón GBA'},
        {'label': 'Región: 3er Cordón GBA', 'value': '3 cordón GBA'},
        {'label': 'Región: Interior GBA', 'value': 'Interior GBA'},
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Cuyo', 'value': 'Cuyo'},
        {'label': 'Región: Patagonia', 'value': 'Sur'},
        {'label': 'Región: NEA', 'value': 'NEA'},
        {'label': 'Región: NOA', 'value': 'NOA'},
        {'label': 'Región: Patagonia', 'value': 'Patagonia'},
    ]

def dropdownTargetBANCOS_2(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_BANCOS_2
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesBANCOS_2(id='selectOpciones'):
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

paletas = {}

paletas["P02"] = list2dictPalette(['Masculino', 'Femenino', 'No binario'], ["#6eaff4", "#f06a77","#50b367" ], noSabe=False)
paletas["P03"] = list2dictPalette(['Soltero o soltera', 'Casado o casada', 'En concubinato'], qualitative_strong, noSabe=False)
paletas["P04"] = list2dictPalette(['No tengo hijos', 'Tengo 1 hijo', 'Tengo 2 hijos', 'Tengo 3 o más hijos'], qualitative_strong, noSabe=False)
paletas["P06"] = list2dictPalette(['Tengo trabajo estable', 'Realizo changas o trabajos de vez en cuando', 'No tengo trabajo', 'Soy jubilado o pensionado'], qualitative_strong, noSabe=False)
paletas["P07"] = list2dictPalette(['Si, tengo un emprendimiento', 'No, no tengo ningún emprendimiento'], diverging_mini, noSabe=False)
paletas["P08"] = list2dictPalette(['Hasta $70.000', 'De $70.000 a $140.000', 'De $140.000 a $210.000', 'De $210.000 a $280.000', 'De $280.000 a $350.000', 'De $350.000 a $420.000', 'De $420.000 a $490.000', 'Más de $490.000'], diverging_reverse, noSabe=False)
paletas["P09"] = list2dictPalette(['Si, solicité', 'No, no solicité'], diverging_mini, noSabe=False)
paletas["P10"] = list2dictPalette(['No necesité un préstamo', 'Ya sabía que no cumplia las condiciones', 'Porque la tasa de interés es muy alta', 'Es un proceso engorroso con mucha burocrácia', 'Otro motivo'], qualitative_strong, noSabe=False)
paletas["P11"] = list2dictPalette(['En un banco', 'En una financiera', 'En una fintech', 'En una red de finanzas colaborativas', 'Otro'], qualitative_strong, noSabe=False)
paletas["P12"] = list2dictPalette(['De $25.000 a $300.000', 'De $300.000 a $500.000', 'De $500.000 a $800.000', 'De $800.000 a $1.500.000', 'De $1.500.000 a $3.000.000', 'De $3.000.000 a $5.000.000', 'Más de $5.000.000'], secuencial, noSabe=False)
paletas["P13"] = list2dictPalette(['No, no tuve ningún problema', 'Si, tuve scoring insuficiente', 'Si, porque estaba en el veraz', 'Si, porque la tasa de interés era muy alta', 'Si, porque no cumplía con la documentación solicitada', 'Otro problema'], qualitative_strong, noSabe=False)
paletas["P14"] = list2dictPalette(['No, no sentí ningún trato diferencial', 'Si, sentí desconfianza', 'Si, sentí que hubo maltrato', 'Si, sentí que hubo una mala atención', 'Si, sentí que me subestimaron', 'Otro problema'], qualitative_strong, noSabe=False)
paletas["P15"] = list2dictPalette(['Si', 'No'], diverging_mini, noSabe=False)
paletas["P16"] = list2dictPalette(['Si', 'No'], diverging_mini, noSabe=False)
paletas["P17"] = list2dictPalette(['Si, recibí apoyo financiero', 'No, nunca recibí apoyo financiero'], diverging_mini, noSabe=False)
paletas["P18"] = list2dictPalette(['Menos de $1.500.000', 'de $1.500.000 a $3.000.000', 'de $3.000.000 a $5.000.000', 'Más de $5.000.000'], qualitative_strong, noSabe=False)


crucesDictBANCOS_2 = {}
for pregunta, paleta in paletas.items():

    crucesDictBANCOS_2[pregunta] = [textosBANCOS_2['label' + pregunta], paleta]


