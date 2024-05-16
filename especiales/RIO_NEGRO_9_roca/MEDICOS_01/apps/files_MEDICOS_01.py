from especiales.MEDICOS_01.apps.encuesta_MEDICOS_01 import encuesta, path, opciones

cuestionario = encuesta.cuestionario
files_MEDICOS_01 = {}
data_folder = path + "data/"

# Para cada pregunta que no es imagen se agrega en el diccionario los 3 csvs (individual, serie, pregunta)
for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_MEDICOS_01["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]

