from config import *
from especiales.POSICIONAMIENTO_CBA_1.apps.txtPOSICIONAMIENTO_CBA_1 import textosPOSICIONAMIENTO_CBA_1
from especiales.POSICIONAMIENTO_CBA_1.apps.preguntasPOSICIONAMIENTO_CBA_1 import filesPOSICIONAMIENTO_CBA_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_POSICIONAMIENTO_CBA_1 = [
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
        {'label': 'Zona Capital', 'value': 'Capital'},
        {'label': 'Zona Interior', 'value': 'Interior'},
        {'label': 'Voto octubre 2019: Schiaretti', 'value': 'Schiaretti'},
        {'label': 'Voto octubre 2019: Negri', 'value': 'Negri'},
        {'label': 'Voto octubre 2019: Mestre', 'value': 'Mestre'},
        {'label': 'Voto octubre 2019: García Elorrio', 'value': 'García Elorrio'},
        {'label': 'Voto octubre 2019: Olivero', 'value': 'Olivero'}]





def dropdownTargetPOSICIONAMIENTO_CBA_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_POSICIONAMIENTO_CBA_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesPOSICIONAMIENTO_CBA_1(id='selectOpciones'):
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

preguntas_CABA_1 = ['P07', 'P08', 'P09', 'P10', 'P11', 'P12', 'P13', 'P15', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P42', 'P44', 'P46', 'P47', 'P48', 'P49', 'P50', 'P51', 'P52']

colores = {
    'peron1': '#1f78b4',
    'peron2':  "#619bc2",
    'peron3': "#a6cee3",
    'peron_nok': "#a6cee3",


    'cambiemos': '#ffff5c',
    'cambiemos1': '#ffff5c',
    'cambiemos2': '#f5f59f',
    'cambiemos3': "#dbdb12",
    'cambiemos_ucr':  "#fc5d5d",



    'izquierda': '#e31a1c',

    'liberales': '#33a02c',

    'otro': "#b15928",
    'otros': "#b15928",

    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454",
    'nosabe': '#c9bebd',
    'nose': '#c9bebd',

}


paletas = {}

colores['color'] = 'blue'

#
# paletas["P05"] = list2dictPalette(['Tengo trabajo estable',
#  'Realizo changas o trabajos de vez en cuando',
#  'No tengo trabajo',
#  'Soy jubilado o pensionado'], diverging)
#
#
# paletas["P06"] = list2dictPalette(
#     [str(i) for i in range(1,10)], "coolwarm", noSabe=False
# )
# paletas["P07"] = list2dictPalette(
#     [str(i) for i in range(1,10)], diverging_reverse, noSabe=False
# )
#
# paletas["P08"] = list2dictPalette(
#      [str(i) for i in range(1,10)], reversed(sns.diverging_palette(250, 150, n=10, l=70, s=100)), noSabe=False
# )
#


votaria = list2dictPalette(['Lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)
votaria = votaria.update(list2dictPalette(['La votaría', 'Puede que la vote', 'Nunca la votaría', 'No sabe'], diverging))





paletas["P07"] = {'Del Frente de Todos y el peronismo': colores['peron1'],
 'De Cambiemos': colores['cambiemos'],
 'De los Liberales libertarios': colores['liberales'],
 'De la Izquierda': colores['izquierda'],
 'Otros': colores['otros'],
 'No sabe': colores['nosabe']}

paletas["P08"] = {'A Alberto Fernández': colores['peron2'],
 'A Sergio Massa': colores['peron3'],
 'A algún candidato del peronismo': colores['peron3'],
 'A algún candidato del kirchnerismo': colores['peron1']}

paletas["P09"] = {'A Alberto Fernández': colores['peron2'],
 'A Sergio Massa': colores['peron3'],
 'A algún candidato del peronismo': colores['peron_nok'],
 'A Cristina Fernández de Kirchner': colores['peron1']}

paletas["P10"] = {'A Horacio Rodriguez Larreta': colores['cambiemos2'],
 'A Mauricio Macri': colores['cambiemos1'],
 'A Patricia Bullrich': colores['cambiemos3'],
 'A Facundo Manes': colores['cambiemos_ucr'],
 'A Gerardo Morales': colores['otros']}

paletas["P11"] = {'A Juntos por el Cambio': colores['cambiemos'],
 'Al Frente de Todos': colores['peron1'],
 'A Hacemos por Córdoba': colores['peron3'],
 'A los liberales libertarios de Milei': colores['liberales'],
 'A Encuentro Vecinal Córdoba': colores['otros'],
 'Al Frente de Izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}

paletas["P12"] = {'A Rodrigo De Loredo con el apoyo de Mauricio Macri, Patricia Bullrich, Martín Lousteau y el radicalismo': colores['cambiemos1'],
 'A Luis Juez con el apoyo de Horacio Rodríguez Larreta': colores['cambiemos_ucr'],
 'No sabe': colores['nosabe']}

paletas["P13"] = {'A Rodrigo De Loredo por Juntos por el Cambio': colores['cambiemos1'],
 'A Martín Llaryora por Hacemos por Córdoba': colores['peron3'],
 'Al candidato del Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A Aurelio Garcia Elorrio por Encuentro Vecinal Cordoba': colores['otros'],
 'Al candidato del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P15"] = {'A Luis Juez por Juntos por el Cambio': colores['cambiemos'],
 'A Martín Llaryora por Hacemos por Córdoba': colores['peron3'],
 'Al candidato del Frente de Todos': colores['peron1'],
 'Al candidato de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A Aurelio García Elorrio por Encuentro Vecinal Córdoba': colores['otros'],
 'Al candidato del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P17"] = {'Luis Juez gobernador – Rodrigo De Loredo vicegobernador por Juntos por el Cambio': colores['cambiemos'],
 'Martín Llaryora gobernador – Alejandra Vigo vicegobernadora por Hacemos por Córdoba': colores['peron3'],
 'A los candidatos  a gobernador y vicegobernador del Frente de Todos': colores['peron1'],
 'A los candidatos de gobernador y vicegobernador de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A los candidatos a gobernador y vicegobernador de Encuentro Vecinal Córdoba': colores['otros'],
 'A los candidatos a gobernador y vicegobernador del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P18"] = {'Rodrigo De Loredo gobernador – Luis Juez vicegobernador por Juntos por el Cambio': colores['cambiemos'],
 'Martín Llaryora gobernador – Alejandra Vigo vicegobernadora por Hacemos por Córdoba': colores['peron3'],
 'A los candidatos  a gobernador y vicegobernador del Frente de Todos': colores['peron1'],
 'A los candidatos de gobernador y vicegobernador de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A los candidatos a gobernador y vicegobernador de Encuentro Vecinal Córdoba': colores['otros'],
 'A los candidatos a gobernador y vicegobernador del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P19"] = {'Luis Juez gobernador – Rodrigo De Loredo vicegobernador por Juntos por el Cambio': colores['cambiemos'],
 'Martín Llaryora gobernador – Natalia de la Sota vicegobernadora por Hacemos por Córdoba': colores['peron3'],
 'A los candidatos  a gobernador y vicegobernador del Frente de Todos': colores['peron1'],
 'A los candidatos de gobernador y vicegobernador de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A los candidatos a gobernador y vicegobernador de Encuentro Vecinal Córdoba': colores['otros'],
 'A los candidatos a gobernador y vicegobernador del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P20"] = {'Rodrigo De Loredo gobernador – Luis Juez vicegobernador por Juntos por el Cambio': colores['cambiemos'],
 'Martín Llaryora gobernador – Natalia de la Sota vicegobernadora por Hacemos por Córdo-ba': colores['peron3'],
 'A los candidatos  a gobernador y vicegobernador del Frente de Todos': colores['peron1'],
 'A los candidatos de gobernador y vicegobernador de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A los candidatos a gobernador y vicegobernador de Encuentro Vecinal Córdoba': colores['otros'],
 'A los candidatos a gobernador y vicegobernador del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P21"] = votaria

paletas["P22"] = votaria

paletas["P23"] = votaria

paletas["P24"] = votaria

paletas["P42"] = {'A Rodrigo De Loredo por Juntos por el Cambio': colores['cambiemos'],
 'A Daniel Passerini por Hacemos por Cordoba': colores['peron3'],
 'Al candidato del frente de todos': colores['peron1'],
 'Al candidato de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A  Juan Pablo Quinteros por Encuentro Vecinal': colores['otros'],
 'Al candidato del frente de izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P44"] = {'A Luis Juez por Juntos por el Cambio': colores['cambiemos'],
 'A Daniel Passerini por Hacemos por Cordoba': colores['peron3'],
 'Al candidato del frente de todos': colores['peron1'],
 'Al candidato de los liberales libertarios con el apoyo de Javier Milei': colores['liberales'],
 'A  Juan Pablo Quinteros por Encuentro Vecinal': colores['otros'],
 'Al candidato del frente de izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P46"] = votaria

paletas["P47"] = votaria

paletas["P48"] = votaria

paletas["P49"] = votaria

paletas["P50"] = votaria

paletas["P51"] = {'Luis Juez gobernador – Rodrigo De Loredo intendente por Juntos por el Cambio': colores['cambiemos'],
 'Martín Llaryora gobernador – Daniel Passerini intendente por Hacemos por Córdoba': colores['peron3'],
 'A los candidatos a gobernador e intendente del Frente de Todos': colores['peron1'],
 'A los candidatos a gobernador e intendente de los liberales libertarios con el apoyo de Ja-vier Milei': colores['liberales'],
 'A Aurelio García Elorrio gobernador – Juan Pablo Quinteros intendente por Encuentro Veci-nal Córdoba': colores['otros'],
 'A los candidatos a gobernador e intendente del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}

paletas["P52"] = {'Rodrigo De Loredo gobernador – Luis Juez intendente por Juntos por el Cambio': colores['cambiemos'],
 'Martín Llaryora gobernador – Daniel Passerini intendente por Hacemos por Córdoba': colores['peron3'],
 'A los candidatos a gobernador e intendente del Frente de Todos': colores['peron1'],
 'A los candidatos a gobernador e intendente de los liberales libertarios con el apoyo de Ja-vier Milei': colores['liberales'],
 'A Aurelio García Elorrio gobernador – Juan Pablo Quinteros intendente por Encuentro Veci-nal Córdoba': colores['otros'],
 'A los candidatos a gobernador e intendente del Frente de Izquierda': colores['izquierda'],
 'Votaría en blanco': colores['blanco'],
 'No sabe': colores['nosabe']}






for p in range(int('P25'[1:]), int("P40"[1:])):

    paletas['P' + str(p)] = opinionColorDict

crucesDictPOSICIONAMIENTO_CBA_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictPOSICIONAMIENTO_CBA_1[pregunta] = [textosPOSICIONAMIENTO_CBA_1['label' + pregunta], paleta]


