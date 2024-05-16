from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/SANTA_FE_3/'
preguntas_ocultas = []
encuesta = Encuesta('SANTA_FE_3', './especiales/SANTA_FE_3','cuestionario', preguntas_ocultas)

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
        {'label' : 'Voto Agosto 2023: S. Massa', 'value' : 'Massa'},
        {'label' : 'Voto Agosto 2023: J. Grabois', 'value' : 'Grabois'},
        {'label' : 'Voto Agosto 2023: P. Bullrich', 'value' : 'Bullrich'},

        {'label' : 'Voto Gobernador PASO: M. Pullaro y G. Scaglia', 'value' : 'Pullaro'},
        {'label' : 'Voto Gobernador PASO: C. Losada y F. Angelini', 'value' : 'Losada'},
        {'label' : 'Voto Gobernador PASO: M. Féin y E. Fernández', 'value' : 'Fein'},
        {'label' : 'Voto Gobernador PASO: M. Lewandowski y S. Frana', 'value' : 'Lewandowski'},
        {'label' : 'Voto Gobernador PASO: M. Cleri y A. del Huerto Obeid', 'value' : 'Cleri'},
        {'label' : 'Voto Gobernador PASO: L. Bussato y A. Gómez Sáenz', 'value' : 'Busatto'},

        {'label' : 'Zona 1: Rosario', 'value' : 'Rosario'},
        {'label' : 'Zona 2: San lorenzo y Villa Constitución', 'value' : 'San lorenzo o Villa Constitución'},
        {'label' : 'Zona 3: San Martín, Belgrano, Iriondo, Caseros y Gral. López', 'value' : 'San Martín, Belgrano, Iriondo, Caseros o General López'},
        {'label' : 'Zona 4: Santa Fé Capital', 'value' : 'La Capital'},
        {'label' : 'Zona 5: San Jerónimo, Las Colonias, San Justo y Garay', 'value' : 'San Jerónimo, Las Colonias, San Justo o Garay'},
        {'label' : 'Zona 6: Castellano, San Cristóbal y Nueve de Julio', 'value' : 'Castellano, San Cristóbal o Nueve de Julio'},
        {'label' : 'Zona 7: Vera, Gral. Obligado y San Javier', 'value' : 'Vera, General Obligado o San Javier'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)
