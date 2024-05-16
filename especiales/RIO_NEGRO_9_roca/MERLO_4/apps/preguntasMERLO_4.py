dataFolderMERLO_4 = './especiales/MERLO_4/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderMERLO_4):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesMERLO_4 = {}

for pregunta in preguntas:
        filesMERLO_4["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderMERLO_4),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderMERLO_4),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderMERLO_4)]

filesMERLO_4['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderMERLO_4),
                           '{}imagen_orden_ratio.csv'.format(dataFolderMERLO_4),
                           '{}imagen_orden_negativa.csv'.format(dataFolderMERLO_4),
                           '{}serie_imagen.csv'.format(dataFolderMERLO_4)]


imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',

           ]

for p, figura in enumerate(imagenes, 29):
    filesMERLO_4[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_4, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_4,p)]

preguntasQueNoVanMERLO_4 = ["P06"] # control interno

