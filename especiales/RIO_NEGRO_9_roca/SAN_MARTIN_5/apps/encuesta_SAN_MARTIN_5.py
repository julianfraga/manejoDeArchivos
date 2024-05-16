from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/SAN_MARTIN_5/'
preguntas_ocultas = ['P17', 'P17_imputada', 'P20', 'P20_imputada', 'P23', 'P23_imputada','CORTA_PRESIDENTE', 'CORTA_INTENDENTE', 'CORTA_GOBERNADOR',]
encuesta = Encuesta('SAN_MARTIN_5', './especiales/SAN_MARTIN_5','cuestionario', preguntas_ocultas)

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
        {'label': 'Voto PASO 2023: F. Moreira', 'value': 'Moreira'},
        {'label': 'Voto PASO 2023: L. Grosso', 'value': 'Grosso'},
        {'label': 'Voto PASO 2023: S. López Medrano', 'value': 'López Medrano'},
        {'label': "Voto PASO 2023: M. D'Alessandro", 'value': 'D Alessandro'},
        {'label': 'Voto PASO 2023: H. Sardella', 'value': 'Sardella'},
        {'label': 'Región: Zona 1', 'value': 'Zona 1'},
        {'label': 'Región: Zona 2', 'value': 'Zona 2'},
        {'label': 'Región: Zona 3', 'value': 'Zona 3'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
