from especiales.ALQUILERES_PBA_1.apps.cuestionario_ALQUILERES_PBA_1 import cuestionario, path, opciones

files_ALQUILERES_PBA_1 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_ALQUILERES_PBA_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]


renombres = {}

for _, row in cuestionario.query('paleta == "imagen"').iterrows():

    figura = row.texto.replace('¿Qué imagen tiene de ', '').replace('?', '').strip()
    figura = renombres.get(figura, figura) # Por si hay que cambiar un nombre de lo que dice en el csv

    files_ALQUILERES_PBA_1[figura] = ['{}cruce_pregunta_{}{}.csv'.format(data_folder, row.codigo, opcion)
                               for opcion in opciones]