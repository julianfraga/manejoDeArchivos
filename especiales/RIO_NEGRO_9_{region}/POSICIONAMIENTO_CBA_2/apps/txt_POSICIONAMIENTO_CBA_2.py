from especiales.POSICIONAMIENTO_CBA_2.apps.cuestionario_POSICIONAMIENTO_CBA_2 import cuestionario

textos_POSICIONAMIENTO_CBA_2 ={
	'encuesta_especial': "Posicionamiento politico y preferencias electorales: Elecciones 2023 Córdoba. Junio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
	'bajada_encuesta_especial_fecha': "15/06/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
	'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Provincia de Córdoba / Ciudad de Córdoba',
	'tituloDato4': 'Estratificación',
	'textoDato4': 'Departamental',	
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'ES - Encuesta Sincrónica (IVR) a teléfonos móviles y fijos',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': 'Muestreo aleatorio a teléfonos móviles y fijos del la Provincia de Córdoba y  departamento Capital.',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 14/06/2023 al 15/06/2023 abarcando 3.049 casos efectivos en la provincia y 1.555 en la Capital.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': 'Provincia: +/- 1.77 %;  Capital : +/- 2.49 % ',

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


	textos_POSICIONAMIENTO_CBA_2["pregunta" + row.codigo] = texto
	textos_POSICIONAMIENTO_CBA_2["label" + row.codigo] = label

