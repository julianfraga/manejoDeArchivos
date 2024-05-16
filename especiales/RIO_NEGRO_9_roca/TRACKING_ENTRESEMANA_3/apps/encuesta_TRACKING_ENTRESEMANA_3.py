from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/TRACKING_ENTRESEMANA_3/'
preguntas_ocultas = ['P11', 'P11_imputada', 'P11_imputada_sinblanco']
encuesta = Encuesta('TRACKING_ENTRESEMANA_3', './especiales/TRACKING_ENTRESEMANA_3','cuestionario', preguntas_ocultas)

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
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'},
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Norte Grande', 'value': 'Norte'},
        {'label': 'Región: Patagonia', 'value': 'Sur'},
        {'label': 'Región: Buenos Aires', 'value': 'Buenos Aires'},
        {'label' : 'Voto Octubre 2023: S. Massa', 'value' : 'Massa'},
        {'label' : 'Voto Octubre 2023: P. Bullrich', 'value' : 'Bullrich'},
        {'label' : 'Voto Octubre 2023: J. Milei', 'value' : 'Milei'},
        {'label' : 'Voto Octubre 2023: M. Bregman', 'value' : 'Bregman'},
        {'label' : 'Voto Octubre 2023: J. Schiaretti', 'value' : 'Schiaretti'},
                                     ]
n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
