from especiales.RIO_NEGRO_2.apps.cuestionario_RIO_NEGRO_2 import cuestionario

textos_RIO_NEGRO_2 = {
	'encuesta_especial': "Encuesta Electoral Bariloche - Junio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "06/06/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos particulares del tejido urbano de la Ciudad de Bariloche. Teléfonos celulares de la Ciudad de Bariloche de las empresas Personal, Movistar y Claro complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Ciudad de Bariloche',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos. Con rotación de respuestas',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo el 05/06/2023 abarcando 846 encuestas efectivas',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 3.37%',
	'tituloDato10': 'Nivel de confianza',
	'textoDato10': '95%',

	'bloque1': 'Bloque General',
	'bloque1href': '/apps/bloque1',
	'bloque1': 'Bloque Reach de intención de voto',
	'bloque1href': '/apps/bloque2',
	}

for _,row in cuestionario.iterrows():


	aclaracion = row.fillna("").aclaracion

	sep = " "
	if aclaracion  and not aclaracion.startswith('('):

		sep= ", "
	texto = f'{row.texto}{sep}{aclaracion}'.strip()
	label = f'{row.label}{sep}{aclaracion}'.strip()

	
	textos_RIO_NEGRO_2["pregunta" + row.codigo] = texto
	textos_RIO_NEGRO_2["label" + row.codigo] = label
