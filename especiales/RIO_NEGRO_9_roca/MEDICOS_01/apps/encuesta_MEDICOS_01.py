from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/MEDICOS_01/'
preguntas_ocultas = []
encuesta = Encuesta('MEDICOS_01', './especiales/MEDICOS_01','cuestionario', preguntas_ocultas)

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


        {'label' : 'Región: CABA', 'value' : 'CABA'},
        {'label': 'Región: Central Transversal', 'value': 'Centro'},   
        {'label' : 'Región: GBA 1er Cordón', 'value' : '1 cordón GBA'},
        {'label' : 'Región: GBA 2do Cordón', 'value' : '2 cordón GBA'},
        {'label' : 'Región: GBA 3er Cordón', 'value' : '3 cordón GBA'},
        {'label' : 'Región: Interior de PBA', 'value' : 'Interior GBA'},
        {'label' : 'Región: Cuyo', 'value' : 'Cuyo'},
        {'label' : 'Región: NEA', 'value' : 'NEA'},
        {'label' : 'Región: NOA', 'value' : 'NOA'},
        {'label': 'Región: Patagonia', 'value': 'Patagonia'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
