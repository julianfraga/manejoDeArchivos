from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/MATANZA_1/'
encuesta = Encuesta('MATANZA_1', './especiales/MATANZA_1','cuestionario', [])

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
        {'label': 'Voto octubre 2019: F. Espinoza', 'value': 'Espinoza'},
        {'label': 'Voto octubre 2019: F. Finocchiaro', 'value': 'Finocchiaro'},
        {'label': 'Voto octubre 2019: J. C. Costieri', 'value': 'Costieri'},
        {'label': 'Voto octubre 2019: N. González Seligra', 'value': 'González Seligra'},
        {'label': 'Región Sudoeste', 'value': 'González Catan/Virrey del Pino'},
        {'label': 'Región Central', 'value': 'Rafael Castillo/Laferrere/Isidro Casanova'},
        {'label': 'Región Norte', 'value': ' San Justo/Ramos Mejía/Lomas del Mirador/Villa Luzuriaga Manzanares'},
        {'label': 'Región Este', 'value': 'La Tablada/Ciudad Evita/Aldo Bonzi/Villa Madero/Villa Celina/Tapiales'},
                                     ]
n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
