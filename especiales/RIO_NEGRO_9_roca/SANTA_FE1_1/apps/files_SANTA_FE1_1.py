from especiales.SANTA_FE1_1.apps.cuestionario_SANTA_FE1_1 import cuestionario, path, opciones

files_SANTA_FE1_1 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_SANTA_FE1_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
