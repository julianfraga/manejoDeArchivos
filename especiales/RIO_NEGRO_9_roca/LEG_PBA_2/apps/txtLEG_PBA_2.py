textosLEG_PBA_2 =     {

        'fecha': '11/10/21 al 17/10/21',
        'titulo': "Encuesta Legislativa PBA",
        'PBA': 'Buenos Aires',
        'pba':'Toda la Provincia',
        'INTERIOR': 'Interior de la Provincia',


        'PRIMERA': 'Primera Sección',
        'TERCERA': 'Tercera Sección',

        'ambito_pba': 'Provincia de Buenos Aires.',
        'ambito_PRIMERA': 'Provincia de Buenos Aires, primera sección.',
        'ambito_TERCERA': 'Provincia de Buenos Aires, tercera sección.',
        'ambito_INTERIOR': 'Provincia de Buenos Aires, interior.',


        'pba_corte':'1.593',
        'pba_tam': "14.560",
        "pba_error": "2.92%",

        'PRIMERA_corte': '530',
        'PRIMERA_tam': "4.837",
        'PRIMERA_error': "5.03%",

        'TERCERA_corte': '622',
        "TERCERA_tam": "5.653",
        'TERCERA_error': "4.74%",

        'INTERIOR_corte': '441',
        'INTERIOR_tam': "4.070",
        'INTERIOR_error': "5.47%",


        'target': 'Seleccioná un target para ver su distribución:',
        'seleccioneFigura': 'Seleccione qué dirigentes o funcionarios políticos comparar:',
        'cruce': 'Cruce con otras preguntas:',

        'encuestaContinua': "Encuesta Continua",
        'bajadaEncuestaContinua': "---",
        'bajadaEncuestaContinua2': "---",
        'bajadaEncuestaContinua3': "---",

        'tituloDato1': 'Población objeto de estudio',
        'textoDato1': 'Población mayor de 16 años.',
        'tituloDato2': 'Unidad de muestreo',
        'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
        'tituloDato3': 'Ámbito',
        'textoDato3': '---',
        'tituloDato4': 'Estratificación',
        'textoDato4': '---',
        'tituloDato5': 'Técnicas de recolección de información',
        'textoDato5': 'ECA - Encuesta Contínua Automática (IVR) a teléfonos móviles.',
        'tituloDato6': 'Diseño muestral',
        'textoDato6': 'Muestreo aleatorio dinámico estratificado por Cordones I, II; III e interior de la Provincia de Buenos Aires. Con captura datos en tiempo real y de manera contínua. La probabilidad de selección hacia el interior de cada estrato se definió de manera proporcional al tamaño del departamento/partido.',
        'tituloDato7': 'Tamaño muestral',

        'tituloDato8': 'Calibración de la muestra',
        'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
        'tituloDato9': 'Margen de error',


        'preguntaP08': "Suponiendo que las elecciones generales de este año fuesen hoy, ¿iría a votar?",
        'labelP08': "Suponiendo que las elecciones generales de este año fuesen hoy, ¿iría a votar?",

        'preguntaP11': 'Pensando en las elecciones generales legislativas del 14 de noviembre de este año, ¿A cuál de los siguientes espacios políticos votaría?',
        'labelP11': "Intención de voto",

        'preguntaP34': "Ingresos familiares",
        'labelP34': "Ingresos familiares",

        'preguntaP35': 'Situación económica personal actual',
        'labelP35': 'Percepción de la situación económica personal',

        'preguntaP36': 'Situación económica personal en comparación con seis meses atrás',
        'labelP36': 'Percepción de la situación económica personal en comparación con seis meses atrás',

        'preguntaP37': 'Expectativa económica personal para dentro de seis meses',
        'labelP37': 'Expectativa económica personal para dentro de seis meses',

        'preguntaP46': '¿Qué imagen tiene de Alberto Fernandez',
        'labelP46': 'Imágen de Alberto Fernandez',

        'preguntaP47': '¿Qué imagen tiene de Cristina Fernández de Kirchner?',
        'labelP47': 'Imágen de Cristina Fernández de Kirchner',

        'labelP48': 'Imágen de Mauricio Macri',
        'preguntaP48': '¿Qué imagen tiene de Mauricio Macri?',

        'preguntaP49': '¿Qué imagen tiene de Horacio Rodriguez Larreta?',
        'labelP49': 'Imágen de Horacio Rodriguez Larreta',

        'preguntaP50': '¿Qué imagen tiene de Sergio Massa?',
        'labelP50': 'Imágen de Sergio Massa',

        'preguntaP59': '¿Qué imagen tiene de Martin Lousteau?',
        'labelP59': 'Imágen de Martin Lousteau',

        'preguntaP61': '¿Qué imagen tiene de Alfredo Cornejo?',
        'labelP61': 'Imágen de Alfredo Cornejo',

}
for prov in ['pba', 'PRIMERA', 'TERCERA', 'INTERIOR']:
        textosLEG_PBA_2.update({
        prov + "_frase_tam": 'La serie electoral corrió del día {} abarcando {} casos totales y acumulando {} estimaciones implicando una ventana móvil de 3 días.'.format(
                textosLEG_PBA_2["fecha"], textosLEG_PBA_2[prov + "_corte"], textosLEG_PBA_2[prov + "_tam"],
        )
})