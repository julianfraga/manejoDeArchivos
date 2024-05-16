from especiales.FORMULAS_PRESIDENCIALES_1.apps.cuestionario_FORMULAS_PRESIDENCIALES_1 import cuestionario, path, opciones

files_FORMULAS_PRESIDENCIALES_1 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_FORMULAS_PRESIDENCIALES_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]
