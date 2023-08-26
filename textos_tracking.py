#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:32:19 2023

@author: julian
"""

textos_base = {
    'target': 'Seleccioná un target para ver su distribución:',
    'seleccioneFigura': 'Seleccione qué dirigentes o funcionarios políticos comparar:',
    'cruce': 'Cruce con otras preguntas:',
    'label-usuario': 'Usuario',
    'label-password': 'Contraseña',

    'ingresaCredenciales': 'Ingresar',
    'wrongPassword': 'Nombre de usuario o password incorrecto',
    'usuarioNoAutentificado': 'Usuario no autentificado. Ingresá tus credenciales.',
    'contenidoNoDisponible': 'El contenido solicitado no está disponible para su usuario.',

    'menuInicio': "Inicio",
    'menuQuienesSomos': "Quiénes Somos",
    'menuProductos': "Productos",
    'menuOpinionPublica': "OPINIÓN PÚBLICA",
    'menuEncuestasContinuas': "Encuestas continuas",
    'menuEncuestasEspeciales': "Encuestas especiales",
    'menuTrackingNacional': "Tracking Nacional",
    'menuTrackingPBA': "Tracking PBA",
    'menuTrackingCOVID': "Tracking COVID-19",
    'menuTrackingAYSA': "Tracking AYSA",
    'menuTrackingSANTIAGO': "Santiago del Estero 16/02/21",
    'menuTrackingSANTIAGO2': "Santiago del Estero  17/07/21",
    'menuTrackingSANTIAGO_3': "Santiago del Estero  12/08/21",
    'menuTrackingPASO_PBA': "Provincia de Buenos Aires 06/07/21",
    'menuTrackingPASO2_PBA': "Provincia de Buenos Aires 10/07/21",
    'menuTrackingPASO3_PBA': "Provincia de Buenos Aires 18/08/21",
    'menuTrackingPASO4_PBA': "Provincia de Buenos Aires 23/08/21",
    'menuTrackingControl': "Tracking Control",
    'menuTrackingLEGISLATIVAS': "PASO Legislativas 2021",
    'menuInformesAnteriores': "Informes Anteriores",
    'menuBigData': "BIG DATA",
    'menuContacto': "Contacto",
    'menuSalir': "Salir",

    'enConstruccion': "En construcción",
    'actualizando': 'Estamos actualizando la información, volvé a intentarlo más tarde',

    'qs': 'Quiénes somos',
    'qsBajada': 'Inteligencia Analítica - Consultores Asociados',
    'qsIntro': 'Realizamos investigación política y electoral de todo tipo. Encuestas permanentes (tracking), sondeos de opinión, grupos focales, simulación electoral, boca de urna, sentiment de redes, análisis de datos (big data). También realizamos desarrollos tecnológicos aplicados y estudios experimentales.',
    'hacemos': 'Esto es lo que hacemos',

    'ea': 'EA - Encuesta Automática (IVR)',
    'eaBajada': 'a teléfonos móviles',
    'eaBajada2': 'Imagen diagnóstica',
    'eaTexto1': 'Nuestra Encuesta Automática (EA) trabaja sobre una base completa y optimizada de teléfonos celulares argentinos garantizando resultados sólidos, dinámicos y actualizados.',
    'eaTexto2': '¿Cuáles son sus ventajas?',
    'eaTexto3': 'Permite:',
    'eaTexto4': 'Sondeos estables de corto plazo, con gran variación socioeconómica y etaria.',
    'eaTexto5': 'Cobertura geográfica completa y proporcional de localidades, aún con población dispersa.',
    'eaTexto6': 'Focalización micro regional, ya que cada número telefónico se encuentra clasificado localmente.',
    'eaTexto7': 'Obtención de información cualitativa sobre comportamiento y opinión individualizados.',

    'eca': 'ECA - Encuesta Continua Automática (IVR)',
    'ecaBajada': 'a teléfonos móviles',
    'ecaBajada2': 'Tracking y Monitoreo',
    'ecaTexto1': 'Para hacer un seguimiento permanente de fenómenos volátiles a corto plazo, ofrecemos nuestra Encuesta Continua Automática (ECA), un ensamble (tracking) de encuestas de corte transversal. Este estudio de IVR evolutivo posibilita mediciones constantes de alta precisión y permite segmentar las poblaciones-objetivo geográficamente, por targets determinados o según el resultado de sus respuestas.',
    'ecaTexto2': 'La metodología de la ECA se alimenta del proceso en tiempo real para optimizar sus resultados mediante mecanismos de corrección automática, variables latentes dinámicas y machine-learning, entre otras técnicas.',
    'ecaTexto3': 'Este tipo de encuesta ofrece dos módulos complementarios:',
    'ecaTexto4': 'Módulo base: Se efectúan estimaciones de muy corto plazo para un conjunto de variables básicas para el tema de estudio, que permiten observar de manera inmediata el comportamiento de la población y su evolución constante en el tiempo.',
    'ecaTexto5': 'Módulos de apertura: Incorpora variables específicas para producir estimaciones más robustas segmentadas por unidades geográficas (provincias, ciudades, regiones), Targets (Segmento de edad o instrucción, sexo etc) y tipo de respuestas (imagen positiva o negativa, problema principal, expectativa positiva, etc). Se potencia al efectuar cruces significativos con los datos del módulo base.',

    'acr': 'ACR - Social Listening',
    'acrBajada': 'Análisis Big Data de contenido en redes',
    'acrTexto1': 'El ACR realiza un análisis semántico y emocional partiendo de un proceso de clasificación de términos aislados, como las menciones a usuarios o el uso de hashtags. En abordajes más complejos, nuestro motor de análisis utiliza categorías, patrones y registros lingüísticos para medir el sentimiento o polaridad emocional (sentiment analysis) de un conjunto segmentado de información.',
    'acrTexto2': 'A estos procedimientos estándar, el ACR incorpora un análisis Big Data con métricas compuestas, caracterización de posturas - Stance detection- y procedimientos de descubrimiento de información que procesan de forma inteligente grandes volúmenes de datos no estructurados para llegar directo a lo relevante, detectando incidencias, alertas y oportunidades no previstas inicialmente.',
    'acrTexto3': 'Nuestra metodología de avanzada en la industria se basa en un abordaje híbrido lingüísticamente motivado. Aplica machine learning tanto para un caso supervisado que permite la caracterización de aspectos predeterminados del discurso como uno no supervisado en el que lo relevante es promover el descubrimiento de factores no previstos.',
    'acrTexto4': 'El ACR permite:',
    'acrTexto5': 'Caracterizar posturas como favorables o contrarias respecto de una temática. Dichas temáticas pueden ser tan diversas como la imagen de una figura pública o política, la filiación de los usuarios a un club deportivo o el interés por un determinado producto de consumo.',
    'acrTexto6': 'Identificar términos, hashtags y menciones a usuarios en función de variables complejas como las polaridades emocionales y/o posturas frente a un tópico.',
    'acrTexto7': 'Descubrir nuevas temáticas prevalentes en la conversación y clasificar los tweets según las mismas. Implica un análisis de conjuntos de vocablos relacionados entre sí de manera sistemática.',

    'srs': 'SRS - Sensor de redes sociales',
    'srsBajada': 'Topología y análisis dinámico en Twitter',
    'srsTexto1': 'Nuestro motor de análisis de Twitter, gracias a una metodología de avanzada en la industria, identifica conjuntos de interés en los contenidos y los caracteriza por patrones.',
    'srsTexto2': 'La metodología empleada supone la construcción de grafos sobre los que se implementan técnicas de análisis de redes, como algoritmos de community detection, caracterización mediante análisis de flujo de información e implementación de modelos estadísticos predictivos.',
    'srsTexto3': 'El SRS permite:',
    'srsTexto4': 'Inferencia topológica: caracterizar la estructura de grupos de usuarios de acuerdo con su conectividad dentro de un campo de análisis como la discusión política, el consumo, el fútbol, etc.',
    'srsTexto5': 'Perfil de contenido: identificar diferencias semánticas de actividad entre grupos, caracterizar la distribución de temáticas y las diferencias entre posturas.',
    'srsTexto6': 'Análisis dinámico: evaluar la velocidad y dirección de propagación de diferentes tipos de actividad en la red y determinar sus parámetros más relevantes.',

    'aas': 'AAS - Análisis de adecuación semántica',
    'aasBajada': 'Procesamiento automático de discursos',
    'aasTexto1': 'El Análisis de Adecuación Semántica es un tipo de Procesamiento del Lenguaje Natural (PLN) que trabaja sobre discursos orales y escritos para obtener métricas de interrelación, basándose en la representación formal de los textos y su posterior comparación en base a similitudes semánticas.',
    'aasTexto2': 'El AAS permite:',
    'aasTexto3': 'Comparación y entrecruzamiento: Medir cuán relacionados están dos o más discursos y cuánto se adaptan unos a los lineamientos de otros. (cosine similarity, word2vec, etc.)',
    'aasTexto4': 'Clasificación: Agrupar discursos en categorías, en base a la similitud del contenido.',
    'aasTexto5': 'Reconocimiento de referentes: Identificar las entidades (personas, lugares, organizaciones, etc.) a las que los discursos hacen referencia (Named Entity Recognition), además de desplegar estos datos en series temporales.',

    'contacto': "Contacto",
    'direccion': "Zapiola 4248 Piso 3. Dpto D. CABA",
    'email': "info@inteligenciaanalitica.com.ar",
    'telefono': "+54 (011) 6346-9861",

    'encuestasContinuas': "Encuestas continuas",
    'encuestasSincrónicas': "Encuestas sincrónicas",
    'economiaPoliticaSocial': "",  # "Economía, política y social",
    'trackingDiarioNacional': "Tracking diario Nacional",
    'trackingDiarioPBA': "Tracking diario Provincia de Buenos Aires",
    'trackingDiarioCOVID': "Tracking diario COVID-19",
    'trackingDiarioAYSA': "Tracking diario AYSA",
    'encuestaSANTIAGO': "Encuesta Santiago del Estero 16/02/2021",
    'encuestaSANTIAGO2': "Encuesta Santiago del Estero 17/07/2021",
    'acceder': "Acceder",

    'footer': '© 2020. Inteligencia Analítica. Todos los derechos reservados',

    'breadcrumb': "Productos | Opinión Pública",

    'labelBloque': 'Bloque',
    'labelTema': 'Tema',
    'labelTarget': 'Target',
    'txtNorte': 'La Región del __“Norte Grande”__ está integrada por las provincias Corrientes, Misiones, Chaco, Santiago del Estero, Formosa, Tucumán, Salta, Jujuy, Catamarca, La Rioja y San Juan.',
    'txtCentro': 'La Región __“Central Transversal” + CABA__ está integrada por las provincias Entre Ríos, Santa Fé, Córdoba, San Luis, Mendoza y la Ciudad Autónoma de Buenos Aires.',
    'txtPatagonia': 'La Región __Patagonica__ está integrada por las provincias La Pampa, Neuquén, Río Negro, Chubut, Santa Cruz y Tierra del Fuego.',
    'txtBuenosAires': 'La región de __Buenos Aires__ está integrada por la Provincia de Buenos Aires.',

    'bloque1': 'Bloque Política y Gestión',
    'bloque1href': '/apps/bloquePolitico',
    'bloque2': 'Bloque Socioeconómico',
    'bloque2href': '/apps/bloqueSocioeconomico',
    'bloque3': 'Bloque Imagen Comparada de Dirigentes y Funcionarios Políticos',
    'bloque3href': '/apps/bloqueImagenComparada',
    'bloque3Bis': 'Bloque Imagen Individual de Dirigentes y Funcionarios Políticos',
    'bloque3Bishref': '/apps/bloqueImagenIndividual',
    'bloque4': 'Bloque Consumo de Medios y Poderes Legislativo y Judicial',
    'bloque4href': '/apps/bloqueMedios',
    'bloque5': 'Bloque COVID19',
    'bloque5href': '/apps/bloqueCOVID19',
    'bloque7': 'Bloque Temas de Coyuntura',
    'bloque7href': '/apps/bloqueCoyuntura',
    'bloque6': 'Bloque Evaluación de Políticas PBA',
    'bloque6href': '/apps/bloqueEvaluacionPBA',
    'bloque8': 'Bloque Electoral',
    'bloque8href': '/apps/bloqueElectoral',
    'bloque9': 'Bloque Consumo de tabaco',
    'bloque9href': '/apps/bloqueTabaco',
    'bloque10': 'Bloque Reach de candidatos',
    'bloque10href': '/apps/bloqueReach',

    'pregunta_imagen': '¿Qué imagen tiene de cada uno de estos políticos?',

    'labelimagen1': 'Imágen comparada, orden según imagen positiva',
    'labelimagen2': 'Imágen comparada, orden según ratio imagen positiva/negativa',
    'labelimagen3': 'Imágen comparada, orden según imagen negativa',
    
    'labelimagenComparada1': 'Imágen comparada, orden según imagen positiva',
    'labelimagenComparada2': 'Imágen comparada, orden según diferencial enter imagen positiva/negativa',
    'labelimagenComparada3': 'Imágen comparada, orden según imagen negativa',
    'labelimagenComparada1_conGalmarini': 'Imágen comparada, orden según imagen positiva',
    'labelimagenComparada2_conGalmarini': 'Imágen comparada, orden según diferencial imagen positiva/negativa',
    'labelimagenComparada3_conGalmarini': 'Imágen comparada, orden según imagen negativa',

    #'labelimagen': 'Imágen individual de dirigentes',
    'labelimagen_conGalmarini': 'Imágen individual de dirigentes',
    'labelimagen_sinGalmarini': 'Imágen individual de dirigentes'}
#%%
ruta_trabajo = '/home/julian/trabajo/updates/corte 208/tracking/'
nombre_tsv =   'labeleadocuestionario_tracking.tsv'
cuestionario = pd.read_table(ruta_trabajo + nombre_tsv)
textos = textos_base.copy()
for index, row in cuestionario.iterrows():
    codigo = row.codigo
    label = row.label
    

    textos_actualizados.update({f'pregunta{codigo}' : f'{row.texto}', f'label{codigo}' : f'{row.label}'})
    # extos_actualizados.update({f'label{codigo}' : f'{row.label}'})