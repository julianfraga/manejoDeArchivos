from especiales.INSEGURIDAD.apps.cuestionario_INSEGURIDAD import cuestionario, path, opciones

files_INSEGURIDAD = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_INSEGURIDAD["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]

