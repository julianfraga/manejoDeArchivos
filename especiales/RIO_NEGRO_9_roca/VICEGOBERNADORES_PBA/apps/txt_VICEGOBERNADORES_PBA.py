from especiales.VICEGOBERNADORES_PBA.apps.cuestionario_VICEGOBERNADORES_PBA import cuestionario

textos_VICEGOBERNADORES_PBA = {
    'encuesta_especial': "Preferencias electorales: candidatos a Vicegobernador de Provincia de Buenos Aires 2023 - Junio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "06/06/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Provincia de Buenos Aires',

	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos.',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': 'Muestreo aleatorio estratificado por localidad. La probabilidad de selección hacia el interior de cada estrato se definió de manera proporcional al tamaño de la localidad.',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo el 06/06/2023 abarcando 1536 encuestas efectivas.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 2.5%',

	'seleccioneFigura': 'Seleccione qué dirigentes o funcionarios políticos comparar:',
	'pregunta_imagen': '¿Qué imagen tiene de cada uno de estos políticos?',
	'labelimagen1': 'Imagen comparada, orden según imagen positiva',
	'labelimagen2': 'Imagen comparada, orden según ratio imagen positiva/negativa',
	'labelimagen3': 'Imagen comparada, orden según imagen negativa',

	'bloque1': 'Bloque Bloque Vicegobernadores',
	'bloque1href': '/apps/bloque1',

	'bloque2': 'Bloque Reach de candidatos a gobernador y vicegobernador',
	'bloque2href': '/apps/bloque2',
	}

for _,row in cuestionario.iterrows():


	aclaracion = row.fillna("").aclaracion

	sep = " "
	if aclaracion  and not aclaracion.startswith('('):

		sep= ", "
	texto = f'{row.texto}{sep}{aclaracion}'.strip()
	label = f'{row.label}{sep}{aclaracion}'.strip()


	textos_VICEGOBERNADORES_PBA["pregunta" + row.codigo] = texto
	textos_VICEGOBERNADORES_PBA["label" + row.codigo] = label
