dataFolderTIGRE_3 = './especiales/TIGRE_3/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderTIGRE_3):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesTIGRE_3 = {}

for pregunta in preguntas:
        filesTIGRE_3["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_3),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderTIGRE_3),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_3)]

filesTIGRE_3['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderTIGRE_3),
                           '{}imagen_orden_ratio.csv'.format(dataFolderTIGRE_3),
                           '{}imagen_orden_negativa.csv'.format(dataFolderTIGRE_3),
                           '{}serie_imagen.csv'.format(dataFolderTIGRE_3)]


imagenes = ["Alberto Fernandez",
            'CFK',
            'Sergio Massa',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta"]

for p, figura in enumerate(imagenes, 15):
    filesTIGRE_3[figura] = ['{}cruce_pregunta_P{}_5opc.csv'.format(dataFolderTIGRE_3, p),
                                       '{}cruce_pregunta_P{}_3opc.csv'.format(dataFolderTIGRE_3,p)]

preguntasQueNoVanTIGRE_3 = ["P05"] # control interno

