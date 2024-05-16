from especiales.RIO_NEGRO_3.apps.cuestionario_RIO_NEGRO_3 import cuestionario

textos_RIO_NEGRO_3 = {
	'encuesta_especial': "Posicionamiento político y preferencias electorales Río Negro - Julio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "06/07/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Teléfonos celulares delas empresas Personal, Movistar y Claro complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Provincia de Río Negro',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos. Con rotación de respuestas',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 04/07/2023 al 06/07/2023 abarcando 948 encuestas efectivas',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 3.18%',
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

	
	textos_RIO_NEGRO_3["pregunta" + row.codigo] = texto
	textos_RIO_NEGRO_3["label" + row.codigo] = label
