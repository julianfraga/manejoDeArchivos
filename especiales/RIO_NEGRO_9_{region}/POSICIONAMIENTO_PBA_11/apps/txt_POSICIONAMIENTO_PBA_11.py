from especiales.POSICIONAMIENTO_PBA_11.apps.cuestionario_POSICIONAMIENTO_PBA_11 import cuestionario

textos_POSICIONAMIENTO_PBA_11 ={
	'encuesta_especial': "Posicionamiento politico y preferencias electorales. Elecciones presidenciales y a Gobernador. PBA Junio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
	'bajada_encuesta_especial_fecha': "19/06/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
	'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Provincia de Buenos Aires',
	'tituloDato4': 'Estratificación',
	'textoDato4': 'Cordones I,II y III de la RMBA e interior PBA.',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'ECA - Encuesta Contínua Automática (IVR) a teléfonos móviles.',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': 'Muestreo aleatorio estratificado por cordones 1, 2 y 3 de la RMBA e interior PBA con captura de datos en tiempo real y de manera continua. La probabilidad de selección hacia el interior de cada estrato se definió de manera proporcional al tamaño del departamento.',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 16/06/2023 al 19/06/2023 abarcando 3.027 casos efectivos.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 1.78%',

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


	textos_POSICIONAMIENTO_PBA_11["pregunta" + row.codigo] = texto
	textos_POSICIONAMIENTO_PBA_11["label" + row.codigo] = label

