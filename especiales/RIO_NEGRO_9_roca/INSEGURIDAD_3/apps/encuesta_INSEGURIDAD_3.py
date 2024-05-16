from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/INSEGURIDAD_3/'
preguntas_ocultas = []
encuesta = Encuesta('INSEGURIDAD_3', './especiales/INSEGURIDAD_3','cuestionario', preguntas_ocultas)

if encuesta.preguntas_imagenes:
        encuesta.actualizar_bloque({'Gestión e imágenes': ['imagen1', 'imagen2', 'imagen3']})
        encuesta.set_bloque_imagen('Gestión e imágenes')

cuestionario = encuesta.cuestionario

##  CONFIG
opciones = ['_4opc', '_6opc']  # Opciones para preguntas con opciones, tiene que coincidir con los csvs

#   Los Values tienen que coincidir con las columnas de los csv (targets)
opciones_target = opciones_target = [
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
        {'label': 'Región: CABA', 'value': 'CABA'},
        {'label': 'Región: 1er Cordón GBA', 'value': '1 cordón GBA'},
        {'label': 'Región: 2do Cordón GBA', 'value': '2 cordón GBA'},
        {'label': 'Región: 3er Cordón GBA', 'value': '3 cordón GBA'},
        {'label': 'Región: Interior GBA', 'value': 'Interior GBA'},
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Cuyo', 'value': 'Cuyo'},
        {'label': 'Región: NEA', 'value': 'NEA'},
        {'label': 'Región: NOA', 'value': 'NOA'},
        {'label': 'Región: Patagonia', 'value': 'Patagonia'}
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
