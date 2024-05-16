from especiales.VICEGOBERNADORES_PBA.apps.cuestionario_VICEGOBERNADORES_PBA import cuestionario, path, opciones

files_VICEGOBERNADORES_PBA = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_VICEGOBERNADORES_PBA["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
