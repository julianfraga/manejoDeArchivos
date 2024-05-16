from especiales.HURLINGHAM_1.apps.cuestionario_HURLINGHAM_1 import cuestionario

textos_HURLINGHAM_1 = {
    'encuesta_especial': "Preferencias electorales. Municipio de Hurlingham - Junio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "24/06/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Municipio de Hurlingham',

	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos.',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': 'Muestreo aleatorio estratificado por localidad. La probabilidad de selección hacia el interior de cada estrato se definió de manera proporcional al tamaño de la localidad.',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo el 24/06/2023 abarcando 716 encuestas efectivas.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 3.66%',
	}

for _,row in cuestionario.iterrows():


	aclaracion = row.fillna("").aclaracion

	sep = " "
	if aclaracion  and not aclaracion.startswith('('):

		sep= ", "
	texto = f'{row.texto}{sep}{aclaracion}'.strip()
	label = f'{row.label}{sep}{aclaracion}'.strip()


	textos_HURLINGHAM_1["pregunta" + row.codigo] = texto
	textos_HURLINGHAM_1["label" + row.codigo] = label
