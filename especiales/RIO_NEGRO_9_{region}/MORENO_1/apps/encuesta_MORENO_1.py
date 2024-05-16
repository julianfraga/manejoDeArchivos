from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/MORENO_1/'
ocultas = ['P14','P15', 'P18', 'CORTA_INTENDENTE', 'CORTA_PRESIDENTE']
encuesta = Encuesta('MORENO_1', './especiales/MORENO_1','cuestionario', ocultas)

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
        {'label': 'Voto Intendente 2019: Mariel Fernández', 'value': 'Fernández'},
        {'label': 'Voto Intendente 2019: Aníbal Asseff', 'value': 'Asseff'},
        {'label': 'Voto Intendente 2019: Karina Álvarez', 'value': 'Álvarez'},
        {'label': 'Voto Intendente 2019: Belén Gómez', 'value': 'Gómez'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
