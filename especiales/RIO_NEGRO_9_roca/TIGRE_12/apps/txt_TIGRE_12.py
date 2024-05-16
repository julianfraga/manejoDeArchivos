from especiales.TIGRE_12.apps.cuestionario_TIGRE_12 import cuestionario

textos_TIGRE_12 = {
    'encuesta_especial': "Preferencias electorales y evaluación de la gestión municipal. Municipio de Tigre, corte 12 - Junio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "06/06/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Municipio de Tigre',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos.',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': 'Muestreo aleatorio estratificado por localidad. La probabilidad de selección hacia el interior de cada estrato se definió de manera proporcional al tamaño de la localidad.',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 03/06/2023 al 06/06/2023 abarcando 829 encuestas efectivas.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 3.32%',

	'seleccioneFigura': 'Seleccione qué dirigentes o funcionarios políticos comparar:',
	'pregunta_imagen': '¿Qué imagen tiene de cada uno de estos políticos?',
	'labelimagen1': 'Imagen comparada, orden según imagen positiva',
	'labelimagen2': 'Imagen comparada, orden según ratio imagen positiva/negativa',
	'labelimagen3': 'Imagen comparada, orden según imagen negativa',

	'bloque1': 'Bloque Intención de voto por espacio político',
	'bloque1href': '/apps/bloque1',

	'bloque2': 'Bloque Escenarios políticos municipales en elecciones unificadas',
	'bloque2href': '/apps/bloque2',
	
	'bloque3': 'Bloque Escenarios políticos municipales en elecciones desdobladas',
	'bloque3href': '/apps/bloque3',

	'bloque4': 'Bloque Imagen de dirigentes',
	'bloque4href': '/apps/bloque4',

	'bloque5': 'Bloque Gestión municipal',
	'bloque4href': '/apps/bloque4',
	}

for _,row in cuestionario.iterrows():


	aclaracion = row.fillna("").aclaracion

	sep = " "
	if aclaracion  and not aclaracion.startswith('('):

		sep= ", "
	texto = f'{row.texto}{sep}{aclaracion}'.strip()
	label = f'{row.label}{sep}{aclaracion}'.strip()


	textos_TIGRE_12["pregunta" + row.codigo] = texto
	textos_TIGRE_12["label" + row.codigo] = label
