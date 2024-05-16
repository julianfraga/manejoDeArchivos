from config import *
from especiales.VACUNAS_1.apps.txtVACUNAS_1 import textosVACUNAS_1
from especiales.VACUNAS_1.apps.preguntasVACUNAS_1 import filesVACUNAS_1, preguntas, preguntas_con_opciones
import pandas as pd


def dropdownTargetVACUNAS(id='selectTargetVACUNAS', cantidadDeOpciones=17):
    opciones = [
        {'label': 'Todos', 'value': 'Todos'},
        {'label': 'Hombres', 'value': 'Hombres'},
        {'label': 'Mujeres', 'value': 'Mujeres'},
        {'label': '16-29 años', 'value': '16-29 años'},
        {'label': '30-49 años', 'value': '30-49 años'},
        {'label': '50 o más años', 'value': '50+ años'},
        {'label': 'Hasta primario completo', 'value': 'Hasta primario completo'},
        {'label': 'Secundario completo/incompleto', 'value': 'Secundario completo/incompleto'},
        {'label': 'Terciario completo/incompleto', 'value': 'Terciario completo/incompleto'},
        {'label': 'CABA', 'value': 'CABA'},
        {'label': 'GBA', 'value': 'GBA'},
        {'label': 'Interior', 'value': 'INTERIOR'},
        {'label': 'Región: Central Transversal', 'value': 'CENTRO'},
        {'label': 'Región: Cuyo', 'value': 'CUYO'},
        {'label': 'Región: NEA', 'value': 'NEA'},
        {'label': 'Región: NOA', 'value': 'NOA'},
        {'label': 'Región: Patagonia', 'value': 'PATAGONIA'},

    ]
    return dcc.Dropdown(
        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )


qualitative2 = [(0.12156862745098039, 0.47058823529411764, 0.7058823529411765), (0.2, 0.6274509803921569, 0.17254901960784313), (0.8901960784313725, 0.10196078431372549, 0.10980392156862745), (1.0, 0.4980392156862745, 0.0), (0.41568627450980394, 0.23921568627450981, 0.6039215686274509), (0.6941176470588235, 0.34901960784313724, 0.1568627450980392), (0.6509803921568628, 0.807843137254902, 0.8901960784313725), (0.6980392156862745, 0.8745098039215686, 0.5411764705882353), (0.984313725490196, 0.6039215686274509, 0.6), (0.9921568627450981, 0.7490196078431373, 0.43529411764705883), (0.792156862745098, 0.6980392156862745, 0.8392156862745098), (1.0, 1.0, 0.6)]
si_no  = ['#87cb67', '#f88c51','#c9bebd']
si_maso_no  = ['#87cb67', '#fffd5e','#f88c51','#c9bebd']
si_no_maso  = ['#87cb67','#f88c51', '#fffd5e','#c9bebd']
si_no_dict = {'Si': '#87cb67', 'No': '#f88c51'}

paleta_vacunas = {}

paleta_vacunas['P06'] = list2dictPalette(["1 hijo","2 hijos","3 hijos","4 o más hijos"], secuencial  , noSabe=False)
paleta_vacunas['P07'] = list2dictPalette(['Con hijos de 3 años y menos','Con hijos mayores de 3 años'], secuencial  , noSabe=False)

paleta_vacunas['P08'] = list2dictPalette(['En un Centro de Salud', 'En un hospital', 'En un sanatorio', 'En un Consultorio Privado', 'En un vacunatorio'], qualitative2  , noSabe=False)
paleta_vacunas['P09'] = si_no_dict
paleta_vacunas['P10'] = dict(zip(['Si, son efectivas', 'No, no son efectivas'], si_no))
paleta_vacunas['P11'] = si_no_dict
paleta_vacunas['P12'] = dict(zip([ 'Si','No'], si_no))
paleta_vacunas['P13'] = list2dictPalette(['La quíntuple', 'La triple viral (Sarampión, rubeola y paperas)', 'La Neumococo', 'La BCG', 'Otra', 'No recuerda'], qualitative2  , noSabe=False)
paleta_vacunas['P14'] = si_no_dict
paleta_vacunas['P15'] = list2dictPalette(['Si, las conozco', 'No, no las conozco', 'Algunas'], si_no_maso  , noSabe=False)
paleta_vacunas['P16'] = list2dictPalette(['Si', 'A veces', 'No'], si_maso_no  , noSabe=False)
paleta_vacunas['P17'] = dict(zip(['Sí, hay suficiente información', 'No, no hay suficiente información'], si_no))
paleta_vacunas['P18'] = list2dictPalette(['Si', 'Sí, pero es necesario', 'No'], si_maso_no, noSabe=False)
paleta_vacunas['P19'] = list2dictPalette(['Sí, mucho', 'Si, un poco', 'No'], si_maso_no[:3], noSabe=False)
paleta_vacunas['P20'] = list2dictPalette([ 'Si', 'No recuerda','No'], si_maso_no[:3] , noSabe=False)
paleta_vacunas['P21'] = list2dictPalette(['La quíntuple', 'La triple viral (Sarampión, rubeola y paperas)', 'La Neumococo', 'La BCG', 'Otra', 'No recuerda'], qualitative2  , noSabe=False)
paleta_vacunas['P22'] = list2dictPalette(['Si', 'No recuerda','No'], si_maso_no  , noSabe=False)
paleta_vacunas['P23'] = list2dictPalette(['La quíntuple', 'La triple viral (Sarampión, rubeola y paperas)', 'La Neumococo', 'La BCG', 'Otra', 'No recuerda'], qualitative2  , noSabe=False)
paleta_vacunas['P24'] = list2dictPalette(['Sí, una vez', 'Si varias veces', 'No', 'No recuerdo'], qualitative2  , noSabe=False)
paleta_vacunas['P25'] = si_no_dict
paleta_vacunas['P26'] = si_no_dict
paleta_vacunas['P27'] = list2dictPalette(['Si, la Polio y la quíntuple', 'Si, la triple viral y la BCG', 'Otras', 'No recuerdo'], qualitative2  , noSabe=False)
paleta_vacunas['P28'] = si_no_dict
paleta_vacunas['P29'] = si_no_dict
paleta_vacunas['P30'] = list2dictPalette(['Si, Infanrix', 'Si, Hexaxim', 'No recuerdo'], qualitative2  , noSabe=False)
paleta_vacunas['P31'] = si_no_dict
paleta_vacunas['P32'] = si_no_dict
paleta_vacunas['P33'] = list2dictPalette(['Miedo al contagio', 'Porque el lugar donde vacuno a mis hijos se encontraba cerrado', 'Porque el lugar donde vacuno a mi hijo atendía en horario reducido', 'Porque era costoso el viaje'], qualitative2  , noSabe=False)
paleta_vacunas['P34'] = list2dictPalette(['Si, una dosis', 'Si, dos dosis', 'Ninguna'], qualitative2  , noSabe=False)
paleta_vacunas['P35'] = list2dictPalette(['Sputnik V', 'Sinopharm', 'AstraZeneca', 'Johnson', 'Phizer', 'Moderna', 'Otra'], qualitative2  , noSabe=False)


crucesDictVACUNAS_1 = {}
for pregunta, paleta in paleta_vacunas.items():
    crucesDictVACUNAS_1[pregunta] = [textosVACUNAS_1['label' + pregunta], paleta]


