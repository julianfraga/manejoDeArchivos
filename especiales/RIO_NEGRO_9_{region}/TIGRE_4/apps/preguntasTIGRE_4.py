dataFolderTIGRE_4 = './especiales/TIGRE_4/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderTIGRE_4):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesTIGRE_4 = {}

for pregunta in preguntas:
        filesTIGRE_4["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_4),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderTIGRE_4),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_4)]

filesTIGRE_4['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderTIGRE_4),
                           '{}imagen_orden_ratio.csv'.format(dataFolderTIGRE_4),
                           '{}imagen_orden_negativa.csv'.format(dataFolderTIGRE_4),
                           '{}serie_imagen.csv'.format(dataFolderTIGRE_4)]


imagenes = ["Alberto Fernandez",
            'CFK',
            'Sergio Massa',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta",
            'Malena Galmarini']

for p, figura in enumerate(imagenes, 22):
    filesTIGRE_4[figura] = ['{}cruce_pregunta_P{}_5opc.csv'.format(dataFolderTIGRE_4, p),
                                       '{}cruce_pregunta_P{}_3opc.csv'.format(dataFolderTIGRE_4,p)]

preguntasQueNoVanTIGRE_4 = ["P05"] # control interno

