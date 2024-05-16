from especiales.MERLO_10.apps.cuestionario_MERLO_10 import cuestionario

textos_MERLO_10 = {
    'encuesta_especial': "Encuesta Electoral Merlo - Julio 2023",
	'bajada_encuesta_especial': "Encuesta Sincrónica",
    'bajada_encuesta_especial_fecha': "10/07/2023",
	'cruce': 'Cruce con otras preguntas:',
	'tituloDato1': 'Población objeto de estudio',
	'textoDato1': 'Población mayor de 16 años.',
	'tituloDato2': 'Unidad de muestreo',
    'textoDato2': 'Télefonos celulares de empresas Personal, Movistar y Claro, complementados con un 13% de teléfonos fijos para optimizar cobertura geográfica.',
	'tituloDato3': 'Ámbito',
	'textoDato3': 'Municipio de Merlo',
	'tituloDato4': 'Estratificación',
	'textoDato4': 'Parque Gral. San Martín, Merlo y San Antonio de Padua, Mariano Acosta, Libertad y Pontevedra.',
	'tituloDato5': 'Técnicas de recolección de información',
	'textoDato5': 'Encuesta Automática (IVR) a teléfonos móviles y complementariamente a fijos.',
	'tituloDato6': 'Diseño muestral',
	'textoDato6': 'Muestreo aleatorio estratificado por localidad. La probabilidad de selección hacia el interior de cada estrato se definió de manera proporcional al tamaño de la localidad.',
	'tituloDato7': 'Tamaño muestral',
	'textoDato7': 'La captura de datos se llevó a cabo del 06/07/2023 al 10/07/2023 abarcando 689 casos efectivos.',
	'tituloDato8': 'Calibración de la muestra',
	'textoDato8': 'En función de datos paramétricos censales de sexo, edad y nivel educativo.',
	'tituloDato9': 'Margen de error',
	'textoDato9': '+/- 3.73%',

	'seleccioneFigura': 'Seleccione qué dirigentes o funcionarios políticos comparar:',
	'pregunta_imagen': '¿Qué imagen tiene de cada uno de estos políticos?',
	'labelimagen1': 'Imagen comparada, orden según imagen positiva',
	'labelimagen2': 'Imagen comparada, orden según ratio imagen positiva/negativa',
	'labelimagen3': 'Imagen comparada, orden según imagen negativa',

	'bloque1': 'Bloque Intención de voto intendente',
	'bloque1href': '/apps/bloque1',
	'bloque2': 'Reach de candidatos a intendente',
	'bloque2href': '/apps/bloque2',
	'bloque3': 'Reach de candidatos a gobernador',
	'bloque3href': '/apps/bloque3',
	'bloque4': 'Bloque Gestion municipal',
	'bloque4href': '/apps/bloque4',
	'bloque5': 'Bloque Imagen de dirigentes',
	'bloque5href': '/apps/bloque5',
	'bloque6': 'Bloque Intención de voto',
	'bloque6href': '/apps/bloque6'
	}

for _,row in cuestionario.iterrows():


	aclaracion = row.fillna("").aclaracion

	sep = " "
	if aclaracion  and not aclaracion.startswith('('):

		sep= ", "
	texto = f'{row.texto}{sep}{aclaracion}'.strip()
	label = f'{row.label}{sep}{aclaracion}'.strip()


	textos_MERLO_10["pregunta" + row.codigo] = texto
	textos_MERLO_10["label" + row.codigo] = label
