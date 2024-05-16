from especiales.TIGRE_14.apps.cuestionario_TIGRE_14 import cuestionario, path, opciones

files_TIGRE_14 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_TIGRE_14["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]

