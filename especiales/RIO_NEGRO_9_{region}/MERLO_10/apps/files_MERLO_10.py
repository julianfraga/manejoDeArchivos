from especiales.MERLO_10.apps.cuestionario_MERLO_10 import cuestionario, path, opciones

files_MERLO_10 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_MERLO_10["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]

files_MERLO_10['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(data_folder),
                           '{}imagen_orden_ratio.csv'.format(data_folder),
                           '{}imagen_orden_negativa.csv'.format(data_folder),
                           '{}serie_imagen.csv'.format(data_folder)]


