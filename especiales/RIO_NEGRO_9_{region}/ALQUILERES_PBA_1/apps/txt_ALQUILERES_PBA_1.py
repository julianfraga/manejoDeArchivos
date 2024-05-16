from especiales.ALQUILERES_PBA_1.apps.cuestionario_ALQUILERES_PBA_1 import cuestionario

textos_ALQUILERES_PBA_1 ={
     'encuesta_especial': "Encuesta Nueva Ley de Alquileres PBA",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "07/04/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Provincia de Buenos Aires',
	'tituloDato4': 'Estratificación',
	'textoDato4': '',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'ES - Encuesta Sincrónica (IVR) a teléfonos móviles y fijos',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': '',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 06/04/2023 al 07/04/2023 abarcando 1.532 casos efectivos.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 2.5%',

	 'labelimagen1': 'Imágen comparada, orden según imagen positiva',
	 'labelimagen2': 'Imágen comparada, orden según ratio imagen positiva/negativa',
	 'labelimagen3': 'Imágen comparada, orden según imagen negativa',


}

for _,row in cuestionario.iterrows():


	aclaracion = row.fillna("").aclaracion

	sep = " "
	if aclaracion  and not aclaracion.startswith('('):

		sep= ", "
	texto = f'{row.texto}{sep}{aclaracion}'.strip()
	label = f'{row.label}{sep}{aclaracion}'.strip()


	textos_ALQUILERES_PBA_1["pregunta" + row.codigo] = texto
	textos_ALQUILERES_PBA_1["label" + row.codigo] = label

