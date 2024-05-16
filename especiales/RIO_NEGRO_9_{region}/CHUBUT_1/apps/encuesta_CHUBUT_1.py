from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/CHUBUT_1/'
encuesta = Encuesta('CHUBUT_1', './especiales/CHUBUT_1','cuestionario', ["P70"])

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
        {'label': 'Voto Gobernador 2019: M. Arcioni', 'value': 'Arcioni'},
        {'label': 'Voto Gobernador 2019: C. Linares', 'value': 'Linares'},
        {'label': 'Voto Gobernador 2019: G. Menna', 'value': 'Menna'},
        {'label': 'Voto Gobernador 2019: G. Sáez', 'value': 'Sáez'},
        {'label': 'Región Valle Inferior de Río Chubut', 'value': 'Trelew/Rawson/Valle inferior Rio Chubut'},
        {'label': 'Región C. Rivadavia y aledaños', 'value': 'Comodoro Rivadavia/Rada Tilly/Sarmiento'},
        {'label': 'Región Puerto Madryn', 'value': 'Puerto Madryn'},
        {'label': 'Región Andina', 'value': 'Esquel/Trevelin/Alto Rio Senguer/Región Andina'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
