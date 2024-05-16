dataFolderMERLO_8 = './especiales/MERLO_8/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderMERLO_8):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesMERLO_8 = {}

for pregunta in preguntas:
        filesMERLO_8["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderMERLO_8),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderMERLO_8),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderMERLO_8)]

filesMERLO_8['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderMERLO_8),
                           '{}imagen_orden_ratio.csv'.format(dataFolderMERLO_8),
                           '{}imagen_orden_negativa.csv'.format(dataFolderMERLO_8),
                           '{}serie_imagen.csv'.format(dataFolderMERLO_8)]



imagenes = ["Gustavo Menendez",
            "David Zencich",
            "Pablo Cocuzza",
            'Raúl Othacehé',
            'Cristian Franco',
           ]
for p, figura in enumerate(imagenes, int('P13'[1:])):
    filesMERLO_8[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_8, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_8,p)]




imagenes = ["Axel Kicillof",
            "Diego Santilli",
            'Cristian Ritondo',
            "José Luis Espert",
            'Carolina Píparo',
           ]

for p, figura in enumerate(imagenes, int('P21'[1:])):
    filesMERLO_8[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_8, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_8,p)]



imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',

           ]

for p, figura in enumerate(imagenes, int('P42'[1:])):
    filesMERLO_8[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_8, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_8,p)]

preguntasQueNoVanMERLO_8 = ["P06"] # control interno

