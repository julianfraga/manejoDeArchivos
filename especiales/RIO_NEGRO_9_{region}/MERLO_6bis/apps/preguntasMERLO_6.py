dataFolderMERLO_6 = './especiales/MERLO_6/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderMERLO_6):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesMERLO_6 = {}

for pregunta in preguntas:
        filesMERLO_6["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderMERLO_6),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderMERLO_6),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderMERLO_6)]

filesMERLO_6['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderMERLO_6),
                           '{}imagen_orden_ratio.csv'.format(dataFolderMERLO_6),
                           '{}imagen_orden_negativa.csv'.format(dataFolderMERLO_6),
                           '{}serie_imagen.csv'.format(dataFolderMERLO_6)]


imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',

           ]

for p, figura in enumerate(imagenes, int('P31'[1:])):
    filesMERLO_6[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_6, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_6,p)]

preguntasQueNoVanMERLO_6 = ["P06"] # control interno

