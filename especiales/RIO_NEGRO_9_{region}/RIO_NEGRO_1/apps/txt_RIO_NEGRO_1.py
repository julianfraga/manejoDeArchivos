from especiales.RIO_NEGRO_1.apps.cuestionario_RIO_NEGRO_1 import cuestionario

textos_RIO_NEGRO_1 = {
	'encuesta_especial': "Encuesta Electoral Cinco Saltos - Mayo 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "28/05/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos particulares del tejido urbano de la Ciudad de Cinco Saltos. Teléfonos celulares de la Ciudad de Cinco Saltos de las empresas Personal, Movistar y Claro complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Municipio de Cinco Saltos',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta presencial domiciliaria a individuos, con lectura de cuestionario y rotación de respuestas (cuotas por áreas de muestra significativa).\n Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos. Con rotación de respuestas',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 26/05/2023 al 28/05/2023 abarcando 725 casos efectivos de los cuales 405 pertenecen a encuestas presenciales y 320 a encuestas telefónicas  ',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 3.64%',
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

	
	textos_RIO_NEGRO_1["pregunta" + row.codigo] = texto
	textos_RIO_NEGRO_1["label" + row.codigo] = label
