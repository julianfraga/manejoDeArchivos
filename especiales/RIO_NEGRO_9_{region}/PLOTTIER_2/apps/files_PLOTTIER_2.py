from especiales.PLOTTIER_2.apps.cuestionario_PLOTTIER_2 import cuestionario, path, opciones

files_PLOTTIER_2 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_PLOTTIER_2["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
