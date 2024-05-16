from config import colores, qualitative,votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong,ingresosColorDict

# comando:


paletas = {}

paletas['aysa_1'] = dict(zip(['Si', 'No'],  ['#4bb05c', '#ea5739']))

paletas['aysa_2'] = list2dictPalette([
            'A la empresa Aysa en forma directa',
            'Al Country, barrio, consorcio donde vivo y está conectada a la de la empresa Aysa',
            'Es una red desvinculada de la empresa Aysa',
            'No sabe'
            ],
            qualitative)


paletas['aysa_3'] = dict(zip(['No desmejoró', 'Si desmejoró'],  ['#4bb05c', '#ea5739']))


paletas['aysa_4'] = list2dictPalette([
            'Color',
            'Olor',
            'Gusto',
            'Presión',
            ],
            qualitative)


paletas['aysa_5'] =  list2dictPalette([
            'No',
            'Si. A la empresa AySA en forma directa',
            'Si. Al Country, barrio, consorcio donde vivo y está conectada a la de la empresa AySA',
            'Si. Es una red desvinculada de la empresa AySA',
            'No sabe',
            ],
            qualitative)

paletas['aysa_6'] = dict(zip(['No desmejoró', 'Si desmejoró'],  ['#4bb05c', '#ea5739']))

paletas['aysa_7'] = list2dictPalette([
            'Ningún aspecto ha desmejorado',
            'Tapa rota',
            'Boca de acceso rota',
            'Filtraciones en el sótano',
            'Olor químico en la cloaca',
            'Taponamiento',
            'Otro'
            ],
            qualitative)


paletas["P33"] = ingresosColorDict
# Bloque Imagen de dirigentes
paletas["P45"] = opinionColorDict
paletas["P48"] = opinionColorDict

paletas["P51"] = opinionColorDict

paletas["P56"] = opinionColorDict
