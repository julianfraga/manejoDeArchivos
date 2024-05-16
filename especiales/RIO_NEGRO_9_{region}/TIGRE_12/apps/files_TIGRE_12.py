from especiales.TIGRE_12.apps.cuestionario_TIGRE_12 import cuestionario, path, opciones

files_TIGRE_12 = {}
data_folder = path + "data/"

for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_TIGRE_12["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]

files_TIGRE_12['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(data_folder),
                           '{}imagen_orden_ratio.csv'.format(data_folder),
                           '{}imagen_orden_negativa.csv'.format(data_folder),
                           '{}serie_imagen.csv'.format(data_folder)]


renombres = {'Cristina Fernández de Kirchner': 'CFK'}

for _, row in cuestionario.query('paleta == "imagen"').iterrows():

    if 'tiene de ' in str(row.texto):
        figura = row.texto.replace('¿Qué imagen tiene de ', '').replace('?', '').strip()
    
    
    elif 'tiene sobre' in str(row.texto):
        figura = row.texto.replace('¿Qué imagen tiene sobre ', '').replace('?', '').strip()
    
    figura = renombres.get(figura, figura)   
    
    files_TIGRE_12[figura] = ['{}cruce_pregunta_{}{}.csv'.format(data_folder, row.codigo, opcion)
                           for opcion in opciones]