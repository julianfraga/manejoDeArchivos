dataFolderMERLO_3 = './especiales/MERLO_3/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderMERLO_3):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesMERLO_3 = {}

for pregunta in preguntas:
        filesMERLO_3["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderMERLO_3),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderMERLO_3),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderMERLO_3)]

filesMERLO_3['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderMERLO_3),
                           '{}imagen_orden_ratio.csv'.format(dataFolderMERLO_3),
                           '{}imagen_orden_negativa.csv'.format(dataFolderMERLO_3),
                           '{}serie_imagen.csv'.format(dataFolderMERLO_3)]


imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',

           ]

for p, figura in enumerate(imagenes, 28):
    filesMERLO_3[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_3, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_3,p)]

preguntasQueNoVanMERLO_3 = ["P05"] # control interno

