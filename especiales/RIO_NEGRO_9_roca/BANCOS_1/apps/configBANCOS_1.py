from config import *
from especiales.BANCOS_1.apps.txtBANCOS_1 import textosBANCOS_1
from especiales.BANCOS_1.apps.preguntasBANCOS_1 import filesBANCOS_1, preguntas, preguntas_con_opciones
import pandas as pd


opciones_BANCOS_1 = [
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

def dropdownTargetBANCOS_1(id='selectTarget', cantidadDeOpciones=20):
    opciones = opciones_BANCOS_1
    return dcc.Dropdown(

        options=opciones[0:cantidadDeOpciones],
        value='Todos',
        placeholder="Selección por target",
        id=id,
        clearable=False,
        searchable=False
    )



def dropwdownOpcionesBANCOS_1(id='selectOpciones'):
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
    'cambiemos_ucr':  "#fc5d5d",
    'izquierda': '#e31a1c',
    'liberales': '#33a02c',
    'otro': "#b15928",
    'otros': "#b15928",
    'blanco':'#8a8a8a',
    'cristianos': "#4dc2ff",
    'nofue':"#545454",
    'nosabe': '#c9bebd',
}


#paletas = {'P01': {'Empleado en relación de dependencia': '#1f78b4', 'Jubilado o pensionado': '#33a02c', 'Desempleado': '#e31a1c', 'Monotributista o autónomo': '#ff7f00', 'Empresario': '#6a3d67', 'Estudiante': '#b15928', 'Otro': '#c9bebd'}, 'P02': {'Menos de 50 mil': '#1f78b4', 'Entre 50 y 100 mil': '#33a02c', 'Entre 100 y 150 mil': '#e31a1c', 'Entre 150 y 200 mil': '#ff7f00', 'Entre 200 y 250 mil': '#6a3d67', 'Entre 250 y 300 mil': '#b15928', 'Mas de 300 mil': '#c9bebd'}, 'P03': {'Si, tengo': '#1f78b4', 'No, no tengo': '#c9bebd'}, 'P04': {'Si ': '#1f78b4', 'No ': '#c9bebd'}, 'P05': {'Si ': '#1f78b4', 'No ': '#c9bebd'}, 'P06': {'Si ': '#1f78b4', 'No ': '#c9bebd'}, 'P07': {'Si, lo tomaría': '#1f78b4', 'Probablemente si': '#33a02c', 'Probablemente no': '#e31a1c', 'No, no lo tomaría': '#ff7f00', 'No sabe': '#c9bebd'}, 'P08': {'Si ': '#1f78b4', 'No ': '#c9bebd'}, 'P09': {'1': '#1f78b4', '2': '#33a02c', '3': '#e31a1c', '4': '#ff7f00', '5': '#6a3d67', '6': '#b15928', '7': '#a6cee3', '8': '#b2df8a', '9': '#c9bebd'}, 'P10': {'Muy conveniente': '#1f78b4', 'Bastante conveniente': '#33a02c', 'Algo convenientes': '#e31a1c', 'Poco convenientes': '#ff7f00', 'Nada convenientes': '#6a3d67', 'No sabe': '#c9bebd'}, 'P11': {'No intervenir y quien tomó el crédito debe hacerse cargo': '#1f78b4', 'Intervenir para asegurar que quien tomó el crédito pueda afrontar los pagos.': '#33a02c', 'No sabe': '#c9bebd'}, 'P12': {'Si': '#1f78b4', 'No': '#c9bebd'}, 'P13': {'Banco público o cooperativo': '#1f78b4', 'Banco privado': '#33a02c', 'No sabe': '#c9bebd'}, 'P14': {'Nación': '#1f78b4', 'Provincia': '#33a02c', 'Ciudad': '#e31a1c', 'Banco de Córdoba': '#ff7f00', 'Nuevo Banco de Santa Fé': '#6a3d67', 'Otro': '#c9bebd'}, 'P15': {'Santander': '#1f78b4', 'Galicia': '#33a02c', 'Macro': '#e31a1c', 'Francés': '#ff7f00', 'ICBC': '#6a3d67', 'Patagonia': '#b15928', 'No sabe': '#c9bebd'}, 'P16': {'Las billeteras virtuales ofertadas por entidades bancarias como MODO o Cuenta DNI': '#1f78b4', 'Las billeteras virtuales ofertadas por entidades no bancarias como Mercado Pago o Ualá': '#33a02c', 'No sabe': '#c9bebd'}, 'P17': {'Porque son más seguras': '#1f78b4', 'Porque tienen más clientes adheridos': '#33a02c', 'Porque la calidad de la aplicación es mejor': '#e31a1c', 'Por la calidad de la atención al cliente': '#ff7f00', 'Por la eficiencia en la solución de reclamos': '#6a3d67', 'No sabe': '#c9bebd'}, 'P18': {'Si, las conozco': '#1f78b4', 'No, no las conozco': '#c9bebd'}, 'P19': {'Si': '#1f78b4', 'No': '#c9bebd'}, 'P20': {'MODO': '#1f78b4', 'Cuenta DNI': '#33a02c', 'Mercado Pago': '#e31a1c', 'Ualá': '#ff7f00', 'Brubank': '#6a3d67', 'Naranja X': '#b15928', 'Otra': '#c9bebd'}, 'P21': {'Para pagar en comercios con el celular': '#1f78b4', 'Para transferir / enviar o recibir dinero de terceros': '#33a02c', 'Para usarla para trabajar / cobrar / vender': '#e31a1c', 'Para pagar servicios': '#ff7f00', 'Para extraer dinero sin tarjeta': '#6a3d67', 'Para recargar el celular / tarjeta de transporte': '#c9bebd'}, 'P22': {'Usás más efectivo que antes': '#1f78b4', 'Usas la misma cantidad de efectivo que antes': '#33a02c', 'Usas menos efectivo que antes': '#c9bebd'}, 'P23': {'Tener mayor control de tus gastos': '#1f78b4', 'Tener igual control de tus gastos': '#33a02c', 'Tener menor control de tus gastos': '#c9bebd'}, 'P24': {'Muy de acuerdo': '#1f78b4', 'De acuerdo': '#33a02c', 'Algo de acuerdo': '#e31a1c', 'Poco de acuerdo': '#ff7f00', 'Nada de acuerdo': '#c9bebd'}, 'P25': {'Deberían mantenerse y ampliarse aún mas': '#1f78b4', 'Deberían mantenerse pero garantizando también la calidad de los servicios presenciales': '#33a02c', 'Deberian limitarse a los estrictamente necesarios': '#e31a1c', 'Deberian eliminarse y volverse a la situación anterior': '#c9bebd'}, 'P26': {'Si, compraría': '#1f78b4', 'No, no tengo suficiente información': '#33a02c', 'No, me resulta una inversión riesgosa': '#e31a1c', 'No, me parece una inversión poco confiable': '#ff7f00', 'No me interesa': '#c9bebd'}, 'P27': {'Si': '#1f78b4', 'No': '#c9bebd'}, 'P28': {'Muy seguro': '#1f78b4', 'Bastante seguro': '#33a02c', 'Seguro': '#e31a1c', 'Poco seguro': '#ff7f00', 'Nada seguro': '#6a3d67', 'No hago operaciones online': '#c9bebd'}, 'P29': {'Si, he sido víctima': '#1f78b4', 'No, no he sido víctima': '#33a02c', 'No sabe': '#c9bebd'}, 'P30': {'Estafa por redes sociales': '#1f78b4', 'Estafa telefónica': '#33a02c', 'Correos electrónicos falsos que dirigían a un sitio web fraudulento': '#e31a1c', 'Virus': '#ff7f00', 'Otros': '#c9bebd'}, 'P31': {'Informar y asesorar a los usuarios/as sobre esta temática': '#1f78b4', 'Incentivar a clientes a desarrollar habilidades para la verificación de la información virtual': '#33a02c', 'Generar productos bancarios que aseguren a los clientes ante estas situaciones': '#e31a1c', 'No sabe': '#c9bebd'}, 'P32': {'Si, he limitado las operaciones': '#1f78b4', 'He limitado parcialmente': '#33a02c', 'No, continúo operando igual que siempre': '#c9bebd'}, 'P33': {'1': '#1f78b4', '2': '#33a02c', '3': '#e31a1c', '4': '#ff7f00', '5': '#6a3d67', '6': '#b15928', '7': '#a6cee3', '8': '#b2df8a', '9': '#c9bebd'}, 'P34': {'1': '#1f78b4', '2': '#33a02c', '3': '#e31a1c', '4': '#ff7f00', '5': '#6a3d67', '6': '#b15928', '7': '#a6cee3', '8': '#b2df8a', '9': '#c9bebd'}, 'P35': {'1': '#1f78b4', '2': '#33a02c', '3': '#e31a1c', '4': '#ff7f00', '5': '#6a3d67', '6': '#b15928', '7': '#a6cee3', '8': '#b2df8a', '9': '#c9bebd'}, 'P36': {'La falta de visión de largo plazo para el desarrollo productivo regional': '#1f78b4', 'Insuficiente coordinación entre los distintos actores que son parte de un proyecto productivo regional': '#33a02c', 'La ausencia de evaluaciones de impacto productivo de los programas a implementar.': '#e31a1c', 'No sabe': '#c9bebd'}}

paletas ={'P01': list2dictPalette(['Empleado en relación de dependencia', 'Jubilado o pensionado', 'Desempleado', 'Monotributista o autónomo', 'Empresario', 'Estudiante', 'Otro'], diverging)
, 'P02':
list2dictPalette([
"Menos de $50.000 mensuales",
"Entre $50.000 y $100.000 mensuales",
"Entre $100.000 y $150.000 mensuales",
"Entre $150.000 y $200.000 mensuales",
"Entre $200.000 y $250.000 mensuales",
"Entre $250.000 y $300.000 mensuales",
"Más de $300.000",

], diverging)
, 'P03':
list2dictPalette(["Si, tengo",
"No, no tengo"
], diverging, noSabe=False)
, 'P04':
list2dictPalette(['Si', 'No'], diverging, noSabe=False)
, 'P05':
list2dictPalette(['Si', 'No'],diverging, noSabe=False)
, 'P06':
list2dictPalette(['Si', 'No'],diverging, noSabe=False)
, 'P07':
list2dictPalette(['Si, lo tomaría', 'Probablemente si', 'Probablemente no', 'No. no lo tomaría', 'No sabe'], diverging)
, 'P08':
list2dictPalette(['Si', 'No'], diverging, noSabe=False)
, 'P09':
list2dictPalette(['1', '2', '3', '4', '5', '6', '7', '8', '9'],  noSabe=False)
, 'P10':
list2dictPalette(['Muy convenientes', 'Bastante convenientes', 'Algo convenientes', 'Poco convenientes', 'Nada convenientes', 'No sabe'], diverging)
, 'P11':
list2dictPalette(['No intervenir y quien tomó el crédito debe hacerse cargo',
                  'Intervenir para asegurar que quien tomó el crédito pueda afrontar los pagos',
                  'No sabe'], qualitative_strong)
, 'P12':
list2dictPalette(['Si', 'No'], diverging, noSabe=False)
, 'P13':
list2dictPalette(['Banco Publico o cooperativo', 'Banco privado', 'No sabe'], qualitative_strong)
, 'P14':
list2dictPalette(["Banco Nacion",
"Banco Provincia",
"Banco Ciudad",
"Bancor, Banco de Cordoba",
"Nuevo Banco de Santa Fe",
"Credicoop",
"Otro",], qualitative_strong, noSabe=False)
, 'P15':
list2dictPalette(['Santander', 'Galicia', 'Macro', 'Frances', 'ICBC', 'Patagonia', 'No sabe'], qualitative_strong)
, 'P16':
list2dictPalette(['Las billeteras virtuales ofertadas por entidades bancarias como MODO o Cuenta DNI', 'Las billeteras virtuales ofertadas por entidades no bancarias como Mercado Pago o Ualá', 'No sabe'], qualitative)
, 'P17':
list2dictPalette([
"Porque son mas seguras",
"Porque los costos del servicio son menores",
"Porque tienen mas clientes adheridos",
"Porque la calidad de la aplicación",
"Por la calidad de la atención al cliente",
"Por la eficiencia en la solución de reclamos",
"No sabe",
], qualitative_strong)
, 'P18':
list2dictPalette(['Si, las conozco', 'No, no las conozco'], diverging, noSabe=False)
, 'P19':
list2dictPalette(['Si', 'No'], diverging, noSabe=False)
, 'P20':
list2dictPalette(['MODO', 'Cuenta DNI', 'Mercado de Pago', 'Ualá', 'Brubank', 'Naranja X', 'Otra'], qualitative_strong, noSabe=False)
, 'P21':
list2dictPalette(['Para pagar en comercios con el celular', 'Para transferir / enviar o recibir dinero de terceros', 'Para usarla para trabajar / cobrar / vender', 'Para pagar servicios', 'Para extraer dinero sin tarjeta', 'Para recargar el celular / tarjeta de transporte'], qualitative_strong, noSabe=False)
, 'P22':
list2dictPalette(['Usas más efectivo que antes', 'Usas la misma cantidad de efectivo que antes', 'Usas menos efectivo que antes'], qualitative_strong, noSabe=False)
, 'P23':
list2dictPalette(['Tener mayor control de tus gastos', 'Tener igual control de tus gastos', 'Tener menor control de tus gastos'], qualitative_strong, noSabe=False)
, 'P24':
list2dictPalette(['Muy de acuerdo', 'De acuerdo', 'Algo de acuerdo', 'Poco de acuerdo', 'Nada de acuerdo'], diverging, noSabe=False)
, 'P25':
list2dictPalette([
"Deberían mantenerse y ampliarse aún mas",
"Deberían  mantenerse pero garantizando también la calidad de los servicios presenciales",
"Deberian limitarse a los estrictamente necesarios",
"Deberian eliminarse y volverse a la situación anterior"

], qualitative_strong, noSabe=False)
, 'P26':
list2dictPalette(['Sí, compraría', 'No, no tengo suficiente información', 'No, me resulta una inversión riesgosa', 'No, me parece una inversión poco confiable', 'No me interesa'], diverging, noSabe=False)
, 'P27':
list2dictPalette(['Si', 'No'], diverging, noSabe=False)
, 'P28':
list2dictPalette(['Muy seguro', 'Bastante seguro', 'Seguro', 'Poco seguro', 'Nada seguro', 'No hago operaciones online'], diverging)
, 'P29':
list2dictPalette(['Sí, he sido víctima', 'No, no he sido víctima', 'No sabe'], diverging_reverse)
, 'P30':
list2dictPalette(['Estafa por redes sociales', 'Estafa telefónica', 'Correos electrónicos falsos que dirigían a un sitio web fraudulento', 'Virus', 'Otros'], qualitative_strong)
, 'P31':
list2dictPalette(['Informar y asesorar a los usuarios/as sobre esta temática', 'Incentivar a clientes a desarrollar habilidades para la verificación de la información virtual', 'Generar productos bancarios que aseguren a los clientes ante estas situaciones', 'No sabe'], qualitative_strong)
, 'P32':
list2dictPalette(['Si, he limitado las operaciones', 'He limitado parcialmente', 'No, continúo operando igual que siempre'], diverging, noSabe=False)
, 'P33':
list2dictPalette(['1', '2', '3', '4', '5', '6', '7', '8', '9'], diverging_reverse, noSabe=False)
, 'P34':
list2dictPalette(['1', '2', '3', '4', '5', '6', '7', '8', '9'], diverging_reverse, noSabe=False)
, 'P35':
list2dictPalette(['1', '2', '3', '4', '5', '6', '7', '8', '9'], diverging_reverse, noSabe=False)
, 'P36':
list2dictPalette(['La falta de visión de largo plazo para el desarrollo productivo regional', 'Insuficiente coordinación entre los distintos actores que son parte de un proyecto productivo regional', 'La ausencia de evaluaciones de impacto productivo de los programas a implementar', 'No sabe'], qualitative_strong)
,
'P37':opinionColorDict ,

'P38': ingresosColorDict,

'P39': comparacionColorDict

}



crucesDictBANCOS_1 = {}
for pregunta, paleta in paletas.items():

    crucesDictBANCOS_1[pregunta] = [textosBANCOS_1['label' + pregunta], paleta]


