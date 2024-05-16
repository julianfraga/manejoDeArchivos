from especiales.SAN_MARTIN_3.apps.cuestionario_SAN_MARTIN_3 import cuestionario, path, opciones

files_SAN_MARTIN_3 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_SAN_MARTIN_3["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
