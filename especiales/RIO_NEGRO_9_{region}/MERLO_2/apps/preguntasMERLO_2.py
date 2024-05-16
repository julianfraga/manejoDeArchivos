dataFolderMERLO_2 = './especiales/MERLO_2/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderMERLO_2):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesMERLO_2 = {}

for pregunta in preguntas:
        filesMERLO_2["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderMERLO_2),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderMERLO_2),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderMERLO_2)]

filesMERLO_2['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderMERLO_2),
                           '{}imagen_orden_ratio.csv'.format(dataFolderMERLO_2),
                           '{}imagen_orden_negativa.csv'.format(dataFolderMERLO_2),
                           '{}serie_imagen.csv'.format(dataFolderMERLO_2)]


imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            'Sergio Massa',
            "Horacio Rodriguez Larreta",
            'Patricia Bullrich',
            'Javier Milei',

           ]

for p, figura in enumerate(imagenes, 22):
    filesMERLO_2[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_2, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_2,p)]

preguntasQueNoVanMERLO_2 = ["P05"] # control interno

