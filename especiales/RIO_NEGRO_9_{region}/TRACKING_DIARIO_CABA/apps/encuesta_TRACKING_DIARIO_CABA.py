from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/TRACKING_DIARIO_CABA/'

##### fix ocultar votan
from especiales.TRACKING_DIARIO_CABA.apps.paletas_TRACKING_DIARIO_CABA import paletas
preguntas_ocultas = ['P19', 'P19_imputada']
for pregunta, paleta in paletas.items():
    if 'votan' in pregunta:
          preguntas_ocultas.append(pregunta)
##### fix ocultar votan


encuesta = Encuesta('TRACKING_DIARIO_CABA', './especiales/TRACKING_DIARIO_CABA','cuestionario', preguntas_ocultas)

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
        {'label': 'Voto octubre 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'}
                                     ]


n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
