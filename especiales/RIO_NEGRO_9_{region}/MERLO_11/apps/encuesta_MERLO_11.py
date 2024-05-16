from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/MERLO_11/'
preguntas_ocultas = ['CORTA_PRESIDENTE', 'CORTA_INTENDENTE', 'CORTA_GOBERNADOR', 'P16', 'P19', 'P22','P16_imputada', 'P19_imputada', 'P22_imputada']
encuesta = Encuesta('MERLO_11', './especiales/MERLO_11','cuestionario', preguntas_ocultas)

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
        {'label': 'Pontevedra', 'value': '654'},
        {'label': 'Mariano Acosta', 'value': '0655A'},
        {'label': 'Libertad', 'value': '653'},
        {'label': 'Parque Gral. San Martín', 'value': '0652A'},
        {'label': 'San Antonio de Padua', 'value': '655'},
        {'label': 'Merlo', 'value': '652'},
        {'label': 'Voto Agosto 2023: G. Menéndez', 'value': "Menéndez"},
        {'label': 'Voto Agosto 2023: P. Cocuzza', 'value': "Cocuzza"},
        {'label': 'Voto Agosto 2023: D. Zencich', 'value': "Zencich"},
        {'label': 'Voto Agosto 2023: E. Varela', 'value': "Varela"},
        {'label': 'Voto Agosto 2023: R. Othacehé', 'value': "Othacehé"},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
