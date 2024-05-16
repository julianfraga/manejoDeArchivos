from especiales.PLOTTIER_1.apps.cuestionario_PLOTTIER_1 import cuestionario, path, opciones

files_PLOTTIER_1 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_PLOTTIER_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
