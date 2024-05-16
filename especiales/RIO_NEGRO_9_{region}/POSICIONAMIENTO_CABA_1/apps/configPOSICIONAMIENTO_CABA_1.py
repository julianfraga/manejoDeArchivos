from config import *
from especiales.POSICIONAMIENTO_CABA_1.apps.txtPOSICIONAMIENTO_CABA_1 import textosPOSICIONAMIENTO_CABA_1
from especiales.POSICIONAMIENTO_CABA_1.apps.preguntasPOSICIONAMIENTO_CABA_1 import filesPOSICIONAMIENTO_CABA_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_POSICIONAMIENTO_CABA_1 = [
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


    ]

def dropdownTargetPOSICIONAMIENTO_CABA_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_POSICIONAMIENTO_CABA_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesPOSICIONAMIENTO_CABA_1(id='selectOpciones'):
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


paletas["P05"] = list2dictPalette(['Tengo trabajo estable',
 'Realizo changas o trabajos de vez en cuando',
 'No tengo trabajo',
 'Soy jubilado o pensionado'], diverging)


paletas["P06"] = list2dictPalette(
    [str(i) for i in range(1,10)], "coolwarm", noSabe=False
)
paletas["P07"] = list2dictPalette(
    [str(i) for i in range(1,10)], diverging_reverse, noSabe=False
)

paletas["P08"] = list2dictPalette(
     [str(i) for i in range(1,10)], reversed(sns.diverging_palette(250, 150, n=10, l=70, s=100)), noSabe=False
)



paletas["P10"] = {'Del Frente de Todos y el peronismo': colores['peron1'], 'De Cambiemos': colores['cambiemos1'], 'De los Liberales libertarios': colores['liberales'],
 'De la Izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P11"] = {'A Alberto Fernández': colores['peron2'],
 'A Sergio Massa': colores['peron3'],
 'A algún candidato del peronismo': "#7794a3",
 'A algún candidato del kirchnerismo': colores['peron1']}


paletas["P12"] = {'A Alberto Fernández': colores['peron2'],
 'A Sergio Massa': colores['peron3'],
 'A algún candidato del peronismo':  "#7794a3",
 'A Cristina Fernández de Kirchner': colores['peron1']}


paletas["P13"] = {'A Horacio Rodriguez Larreta': colores['cambiemos2'],
 'A Mauricio Macri': colores['cambiemos1'],
 'A Patricia Bullrich': colores['cambiemos3'],
 'A Facundo Manes': colores['cambiemos_ucr'],
 'A Gerardo Morales': colores['otros']}


paletas["P14"] = {'Del Frente de Todos y el peronismo': colores['peron1'],
 'A Juntos por el Cambio': colores['cambiemos1'],
 'De los Liberales libertarios': colores['liberales'],
 'De la Izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P16"] = {'A Leandro Santoro': colores['peron1'],
 'A Matias Lammens': colores['peron2'],
 'A Mariano Recalde': colores['peron3']}


paletas["P17"] = {'A Soledad Acuña': colores['cambiemos1'],
 'A Jorge Macri': colores['cambiemos2'],
 'A Martín Lousteau': colores['cambiemos_ucr'],
 'A Fernan Quirós': colores['cambiemos3'],
 'A Ricardo López Murphy': colores['otros']}

votaria_paleta = list2dictPalette(['Lo votaría', 'Puede que lo vote', 'Nunca lo votaría', 'No sabe'], diverging)


paletas["P18"] = votaria_paleta


paletas["P19"] = votaria_paleta


paletas["P20"] = votaria_paleta


paletas["P21"] = votaria_paleta


paletas["P22"] = votaria_paleta


paletas["P23"] = votaria_paleta

paletas["P24"] = votaria_paleta


paletas["P25"] = votaria_paleta


paletas["P26"] = {'Patricia Bullrich presidenta – Jorge Macri Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos1'],
 'Patricia Bullrich presidenta – Ricardo López Murphy Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos2'],
 'Horacio Rodríguez Larreta presidente – Soledad Acuña jefa de gobierno por Juntos por el Cambio': colores['cambiemos3'],
 'Horacio Rodríguez Larreta presidente– Fernán Quirós Jefe de Gobierno por Juntos por el Cambio': colores['otros'],
 'Horacio Rodríguez Larreta presidente – Martín Lousteau Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos_ucr'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Sergio Massa presidente – Matías Lammens Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron2'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['nosabe'],
 'No sabe': colores['nosabe']}


paletas["P27"] = {'Patricia Bullrich presidenta – Jorge Macri Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos1'],
 'Patricia Bullrich presidenta – Ricardo López Murphy Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos2'],
 'Horacio Rodríguez Larreta presidente – Soledad Acuña jefa de gobierno por Juntos por el Cambio': colores['cambiemos3'],
 'Horacio Rodríguez Larreta presidente– Fernán Quirós Jefe de Gobierno por Juntos por el Cambio': colores['otros'],
 'Horacio Rodríguez Larreta presidente – Martín Lousteau Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos_ucr'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron1'],
 'Alberto Fernández presidente – Matías Lammens Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron2'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertario': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P28"] = {'Patricia Bullrich presidenta – Jorge Macri Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos1'],
 'Horacio Rodríguez Larreta presidente – Soledad Acuña jefa de gobierno por Juntos por el Cambio': colores['cambiemos2'],
 'A Martín Lousteau como Jefe de Gobierno': colores['cambiemos3'],
 'A Ricardo López Murphy como Jefe de Gobierno': colores['cambiemos_ucr'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Sergio Massa presidente – Matías Lammens Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron2'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P29"] = {'Patricia Bullrich presidenta – Jorge Macri Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos1"],
 'Horacio Rodríguez Larreta presidente – Soledad Acuña jefa de gobierno por Juntos por el Cambio': colores['cambiemos2'],
 'A Martín Lousteau como Jefe de Gobierno': colores['cambiemos3'],
 'A Ricardo López Murphy como Jefe de Gobierno': colores['cambiemos_ucr'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron1'],
 'Alberto Fernández presidente – Matías Lammens Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron2'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertario': colores['liberales'],
 'A los candidatos de izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P30"] = {'Horacio Rodríguez Larreta presidente - Jorge Macri Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos1'],
 'Patricia Bullrich presidenta – Ricardo López Murphy Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos2'],
 'A Martín Lousteau como Jefe de Gobierno': colores['cambiemos3'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Sergio Massa presidente – Matias Lammens Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron2'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P31"] = {'Horacio Rodríguez Larreta presidente - Jorge Macri Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos1'],
 'Patricia Bullrich presidenta – Ricardo López Murphy Jefe de Gobierno por Juntos por el Cambio': colores['cambiemos2'],
 'A Martín Lousteau como Jefe de Gobierno': colores['cambiemos3'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron1'],
 'Alberto Fernández presidente – Matias Lammens Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron2'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P32"] = {'Patricia Bullrich presidenta – Jorge Macri Jefe de Gobierno por Juntos por el Cambio con el apoyo de Horacio Rodríguez Larreta, Mauricio Macri y la UCR': colores['cambiemos1'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P33"] = {'Patricia Bullrich presidenta – Jorge Macri Jefe de Gobierno por Juntos por el Cambio con el apoyo de Horacio Rodríguez Larreta, Mauricio Macri y la UCR': colores['cambiemos1'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores["peron1"],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P34"] = {'Horacio Rodríguez Larreta presidente – Soledad Acuña jefa de gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos1'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores["izquierda"],
 'No sabe': colores['otros']}


paletas["P35"] = {'Horacio Rodríguez Larreta presidente – Soledad Acuña jefa de gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos1'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P36"] = {'Horacio Rodríguez Larreta presidente – Martín Lousteau Jefe de Gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P37"] = {'Horacio Rodríguez Larreta presidente – Martín Lousteau Jefe de Gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P38"] = {'Horacio Rodríguez Larreta presidente – Jorge Macri Jefe de Gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos1'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P40"] = {'Horacio Rodríguez Larreta presidente – Jorge Macri Jefe de Gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P42"] = {'Horacio Rodríguez Larreta presidente – María Eugenia Vidal jefa de gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos'],
 'Sergio Massa presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernández': colores['peron1'],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores["nosabe"]}


paletas["P44"] = {'Horacio Rodríguez Larreta presidente – María Eugenia Vidal jefa de gobierno por Juntos por el Cambio con el apoyo de Patricia Bullrich, Mauricio Macri y la UCR': colores['cambiemos1'],
 'Alberto Fernández presidente – Leandro Santoro Jefe de Gobierno por el Frente de Todos con el apoyo de Cristina Kirchner y Sergio Massa': colores["peron1"],
 'Javier Milei presidente – Ramiro Marra Jefe de Gobierno por los liberales libertarios': colores['liberales'],
 'A los candidatos de la izquierda': colores['izquierda'],
 'No sabe': colores['nosabe']}


paletas["P46"] = {'Jorge Macri por Juntos por el Cambio': colores['cambiemos1'],
 'Leandro Santoro por el Frente de Todos': colores['peron1'],
 'No sabe': colores['nosabe']}


paletas["P47"] = {'Soledad Acuña por Juntos por el Cambio': colores['cambiemos1'],
 'Leandro Santoro por el Frente de Todos': colores['peron1'],
 'No sabe': colores["nosabe"]}


paletas["P48"] = {'Fernán Quirós por Juntos por el Cambio': colores['cambiemos1'],
 'Leandro Santoro por el Frente de Todos': colores['peron1'],
 'No sabe': colores['nosabe']}


paletas["P49"] = {'Martín Lousteau por Juntos por el Cambio': colores['cambiemos1'],
 'Leandro Santoro por el Frente de Todos': colores['peron1'],
 'No sabe': colores['nosabe']}


paletas["P50"] = {'María Eugenia Vidal por Juntos por el Cambio': colores['cambiemos1'],
 'Leandro Santoro por el Frente de Todos': colores['peron1'],
 'No sabe': colores['nosabe']}







for p in range(int('P51'[1:]), int("P71"[1:])):

    paletas['P' + str(p)] = opinionColorDict

crucesDictPOSICIONAMIENTO_CABA_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictPOSICIONAMIENTO_CABA_1[pregunta] = [textosPOSICIONAMIENTO_CABA_1['label' + pregunta], paleta]


