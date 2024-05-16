dataFolderTIGRE_5 = './especiales/TIGRE_5/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderTIGRE_5):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesTIGRE_5 = {}

for pregunta in preguntas:
        filesTIGRE_5["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_5),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderTIGRE_5),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_5)]

filesTIGRE_5['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderTIGRE_5),
                           '{}imagen_orden_ratio.csv'.format(dataFolderTIGRE_5),
                           '{}imagen_orden_negativa.csv'.format(dataFolderTIGRE_5),
                           '{}serie_imagen.csv'.format(dataFolderTIGRE_5)]


imagenes = ["Alberto Fernandez",
            'CFK',
            'Sergio Massa',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta",
            'Malena Galmarini']

for p, figura in enumerate(imagenes, 22):
    filesTIGRE_5[figura] = ['{}cruce_pregunta_P{}_5opc.csv'.format(dataFolderTIGRE_5, p),
                                       '{}cruce_pregunta_P{}_3opc.csv'.format(dataFolderTIGRE_5,p)]

preguntasQueNoVanTIGRE_5 = ["P05"] # control interno

