from especiales.ALIMENTACION_2.apps.cuestionario_ALIMENTACION_2 import cuestionario

textos_ALIMENTACION_2 = {
    'encuesta_especial': "Alimentación y hábitos de consumo - Junio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "01/07/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'República Argentina',
	'tituloDato4': 'Estratificación',
	'textoDato4': 'Cinco estratos regionales (NEA, NOA, Cuyo, Centro y Patagonia) y Cordones I,II y III de la RMBA e interior PBA.',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos.',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': 'Muestreo aleatorio estratificado por provincias, CABA, Cordones I, II y III de la RMBA e interior PBA. La probabilidad de selección hacia el interior de cada estrato se definió de manera proporcional al tamaño del departamento.',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 21/06/2023 al 01/07/2023 abarcando 3672 encuestas efectivas.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 1.62%',

	# 'seleccioneFigura': 'Seleccione qué dirigentes o funcionarios políticos comparar:',
	# 'pregunta_imagen': '¿Qué imagen tiene de cada uno de estos políticos?',
	# 'labelimagen1': 'Imagen comparada, orden según imagen positiva',
	# 'labelimagen2': 'Imagen comparada, orden según ratio imagen positiva/negativa',
	# 'labelimagen3': 'Imagen comparada, orden según imagen negativa',

	'bloque1': 'Bloque Sociodemografico',
	'bloque1href': '/apps/bloque1',
	'bloque2': 'Bloque Hábitos alimentarios y consumos regulares',
	'bloque2href': '/apps/bloque2',
	'bloque3': 'Bloque Salud Alimentaria',
	'bloque3href': '/apps/bloque3',
	'bloque4': 'Bloque Cotidianidad',
	'bloque4href': '/apps/bloque4',
	'bloque5': 'Bloque Ley de Etiquetado Frontal',
	'bloque5href': '/apps/bloque5',
	 'bloque6': 'Bloque Hábitos de compra y planificación de comidas',
	 'bloque6href': '/apps/bloque6'
	}

for _,row in cuestionario.iterrows():


	aclaracion = row.fillna("").aclaracion

	sep = " "
	if aclaracion  and not aclaracion.startswith('('):

		sep= ", "
	texto = f'{row.texto}{sep}{aclaracion}'.strip()
	label = f'{row.label}{sep}{aclaracion}'.strip()


	textos_ALIMENTACION_2["pregunta" + row.codigo] = texto
	textos_ALIMENTACION_2["label" + row.codigo] = label
