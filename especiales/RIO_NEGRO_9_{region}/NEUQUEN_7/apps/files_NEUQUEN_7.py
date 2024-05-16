from especiales.NEUQUEN_7.apps.encuesta_NEUQUEN_7 import encuesta, path, opciones

cuestionario = encuesta.cuestionario
files_NEUQUEN_7 = {}
data_folder = path + "data/"

# Para cada pregunta que no es imagen se agrega en el diccionario los 3 csvs (individual, serie, pregunta)
for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_NEUQUEN_7["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]

# ruta de los archivos de imagenes
files_NEUQUEN_7['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(data_folder),
                           '{}imagen_orden_ratio.csv'.format(data_folder),
                           '{}imagen_orden_negativa.csv'.format(data_folder),
                           '{}serie_imagen.csv'.format(data_folder)
                              ]


renombres = {}
# usar en caso de que no coincidan los nombres con los datos del CSV
# por ej {'Cristina Fernández de Kirchner', 'CFK'}


# Agregar al diccionario las rutas para los cruces de los candidatos, aca se genera el link entre los nombres y los
# codigos (los datos individuales salen del archivo imagen, y ahi estan por nombre no por codigo)
# Ejemplo de como tiene quedar:
# { 'Sergio Massa': ['./especiales/NEUQUEN_7/data/cruce_pregunta_P61_4opc.csv',
#                   './especiales/NEUQUEN_7/data/cruce_pregunta_P61_6opc.csv'], ...

for _, row in cuestionario.query('paleta == "imagen"').iterrows():


    prefijo = '¿Qué imagen tiene de ' # Es FUNDAMENTAL que esto coincida con como esta escrito en el cuestionario
                                      # Para que en la clave quede solo el nombre y nada mas.
    figura = row.texto.replace(prefijo, '').replace('?', '').strip()
    if row.texto == figura:
        print("Posible error en imagenes", figura ,path)


    figura = renombres.get(figura, figura) # Por si hay que cambiar un nombre de lo que dice en el csv

    files_NEUQUEN_7[figura] = ['{}cruce_pregunta_{}{}.csv'.format(data_folder, row.codigo, opcion)
                               for opcion in opciones]
