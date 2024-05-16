from especiales.POSICIONAMIENTO_PBA_12.apps.cuestionario_POSICIONAMIENTO_PBA_12 import cuestionario, path, opciones

files_POSICIONAMIENTO_PBA_12 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_POSICIONAMIENTO_PBA_12["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
