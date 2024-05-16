from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/SAN_ISIDRO_2/'
preguntas_ocultas = ['P16',
'P16_imputada',
'P19',
'P19_imputada',
'P22',
'P22_imputada',
'CORTA_GOBERNADOR','CORTA_INTENDENTE', 'CORTA_PRESIDENTE']
encuesta = Encuesta('SAN_ISIDRO_2', './especiales/SAN_ISIDRO_2','cuestionario', preguntas_ocultas)

if encuesta.preguntas_imagenes:
        encuesta.actualizar_bloque({'Gestión e imágenes': ['imagen1', 'imagen2', 'imagen3']})
        encuesta.set_bloque_imagen('Gestión e imágenes')

cuestionario = encuesta.cuestionario

##  CONFIG
opciones = ['_4opc', '_6opc']  # Opciones para preguntas con opciones, tiene que coincidir con los csvs

#   Los Values tienen que coincidir con las columnas de los csv (targets)
opciones_target = [
        {'label': 'Todos', 'value': 'Todos'},
        {'label': 'Hombres', 'value': 'Hombres'},
        {'label': 'Mujeres', 'value': 'Mujeres'},
        {'label': '16-29 años', 'value': '16-29 años'},
        {'label': '30-49 años', 'value': '30-49 años'},
        {'label': '50-64 años', 'value': '50-64 años'},
        {'label': '65+ años', 'value': '65+ años'},
        {'label': 'Hasta primario completo', 'value': 'Hasta primario completo'},
        {'label': 'Secundario completo/incompleto', 'value': 'Secundario completo/incompleto'},
        {'label': 'Terciario completo/incompleto', 'value': 'Terciario completo/incompleto'},

        # {'label' : 'Voto Agosto 2023: S. Massa', 'value' : 'Massa'},
        # {'label' : 'Voto Agosto 2023: J. Grabois', 'value' : 'Grabois'},
        # {'label' : 'Voto Agosto 2023: P. Bullrich', 'value' : 'Bullrich'},
        # {'label' : 'Voto Agosto 2023: H. Rodriguez Larreta', 'value' : 'Rodriguez Larreta'},
        # {'label' : 'Voto Agosto 2023: J. Milei', 'value' : 'Milei'},
        {'label': 'Voto intendente PASO 2023: F. Meca', 'value': 'Meca'},
        {'label': 'Voto intendente PASO 2023: R. Lanús', 'value': 'Lanús'},
        {'label': 'Voto intendente PASO 2023: R. Paolucci', 'value': 'Paolucci'},
        {'label': 'Voto intendente PASO 2023: candidatos de Izquierda', 'value': 'Izquierda'},
        
        {'label': 'Región: Villa Adelina', 'value': 'Villa Adelina'},
        {'label': 'Región: Boulogne', 'value': 'Boulogne'},
        {'label': 'Región: Martínez', 'value': 'Martínez'},
        {'label': 'Región: San Isidro', 'value': 'San Isidro'},
        {'label': 'Región: Beccar', 'value': 'Beccar'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
