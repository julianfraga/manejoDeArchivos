from especiales.POSICIONAMIENTO_ESPECIAL_PBA_2.apps.cuestionario_POSICIONAMIENTO_ESPECIAL_PBA_2 import cuestionario, path, opciones

files_POSICIONAMIENTO_ESPECIAL_PBA_2 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_POSICIONAMIENTO_ESPECIAL_PBA_2["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
