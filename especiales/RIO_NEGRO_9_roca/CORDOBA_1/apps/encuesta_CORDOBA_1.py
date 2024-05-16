from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/CORDOBA_1/'
preguntas_ocultas = []
encuesta = Encuesta('CORDOBA_1', './especiales/CORDOBA_1','cuestionario', preguntas_ocultas)

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
        {'label' : 'Voto Presidente PASO: S. Massa', 'value' : 'Massa'},
        {'label' : 'Voto Presidente PASO: J. Grabois', 'value' : 'Grabois'},
        {'label' : 'Voto Presidente PASO: P. Bullrich', 'value' : 'Bullrich'},
        {'label' : 'Voto Presidente PASO: H. Rodriguez Larreta', 'value' : 'Rodriguez Larreta'},
        {'label' : 'Voto Presidente PASO: J. Milei', 'value' : 'Milei'},
        {'label' : 'Voto Gobernador PASO: M. Llaryora', 'value' : 'Llaryora'},
        {'label' : 'Voto Gobernador PASO: L. Juez', 'value' : 'Juez'},
        {'label' : 'Voto Gobernador PASO: A. García Elorrio', 'value' : 'García Elorrio'},
        {'label' : 'Voto Gobernador PASO: A. Spaccesi', 'value' : 'Spaccesi'},
        {'label' : 'Voto Gobernador PASO: L. Olivero', 'value' : 'Olivero'},
        {'label': 'Región: Ciudad de Córdoba', 'value': 'Córdoba'},
        {'label': 'Región: Otras localidades de la Provincia', 'value': 'Otra localidad'},
        {'label': 'Cobertura: Obra social', 'value': 'Obra social'},
        {'label': 'Cobertura: Prepaga por O. S.', 'value': 'Prepaga por obra social'},
        {'label': 'Cobertura: Prepaga voluntaria', 'value': 'Prepaga voluntaria'},
        {'label': 'Cobertura: Plan estatal', 'value': 'Plan estatal'},
        {'label': 'Cobertura: Sin cobertura de salud', 'value': 'No tiene'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
