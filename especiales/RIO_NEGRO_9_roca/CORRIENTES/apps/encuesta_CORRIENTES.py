from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/CORRIENTES/'
preguntas_ocultas = []
encuesta = Encuesta('CORRIENTES', './especiales/CORRIENTES','cuestionario', preguntas_ocultas)

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
        {'label' : 'Voto Presidencial 2023: S. Massa', 'value' : 'Massa'},
        {'label' : 'Voto Presidencial 2023: J. Milei', 'value' : 'Milei'},

        {'label' : 'Voto Gobernador 2021 : G. Valdés', 'value' : 'Valdés'},
        {'label' : 'Voto Gobernador 2021 : F. Ríos', 'value' : 'Ríos'},

        {'label': 'Región: Ciudad de Corrientes', 'value': 'Ciudad de Corrientes'},
        {'label': 'Región: Otras localidades', 'value': 'Otra localidad'},

                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
