from especiales.POSICIONAMIENTO_PBA_11.apps.cuestionario_POSICIONAMIENTO_PBA_11 import cuestionario, path, opciones

files_POSICIONAMIENTO_PBA_11 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_POSICIONAMIENTO_PBA_11["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]

files_POSICIONAMIENTO_PBA_11['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(data_folder),
                           '{}imagen_orden_ratio.csv'.format(data_folder),
                           '{}imagen_orden_negativa.csv'.format(data_folder),
                           '{}serie_imagen.csv'.format(data_folder)]


renombres = {}

for _, row in cuestionario.query('paleta == "imagen"').iterrows():

    figura = row.texto.replace('¿Qué imagen tiene de ', '').replace('?', '').strip()
    figura = renombres.get(figura, figura) # Por si hay que cambiar un nombre de lo que dice en el csv

    files_POSICIONAMIENTO_PBA_11[figura] = ['{}cruce_pregunta_{}{}.csv'.format(data_folder, row.codigo, opcion)
                               for opcion in opciones]