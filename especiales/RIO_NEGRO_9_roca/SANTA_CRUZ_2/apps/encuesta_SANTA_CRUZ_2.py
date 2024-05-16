from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/SANTA_CRUZ_2/'

"""
Constructor de la clase Encuesta.
:param codigo: Código de la encuesta.
:param path: Ruta del directorio de la encuesta.
:param cuestionario: Nombre del archivo de cuestionario.
:param preguntas_ocultas: Lista de preguntas ocultas.
"""
preguntas_ocultas = []

encuesta = Encuesta('SANTA_CRUZ_2', './especiales/SANTA_CRUZ_2','cuestionario', preguntas_ocultas)

if encuesta.preguntas_imagenes:
        encuesta.actualizar_bloque({'Gestión e imágenes': ['imagen1', 'imagen2', 'imagen3']})
        encuesta.set_bloque_imagen('Gestión e imágenes')

cuestionario = encuesta.cuestionario

##  CONFIG
opciones = ['_4opc']  # Opciones para preguntas con opciones, tiene que coincidir con los csvs

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
        {'label': 'Voto 2019: Alicia Kirchner', 'value': 'A.Kirchner'},
        {'label': 'Voto 2019: Florencia Saintout', 'value': 'Belloni'},
        {'label': 'Voto 2019: Eduardo Costa', 'value': 'Costa'},
        {'label': 'Voto 2019: Claudio Vidal', 'value': 'Vidal'},
        {'label': 'Voto 2019: Daniel Peralta', 'value': 'Peralta'}
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
