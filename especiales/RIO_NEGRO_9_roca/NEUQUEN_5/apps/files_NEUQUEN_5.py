from especiales.NEUQUEN_5.apps.cuestionario_NEUQUEN_5 import cuestionario, path, opciones

files_NEUQUEN_5 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_NEUQUEN_5["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
