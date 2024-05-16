dataFolderMERLO_7 = './especiales/MERLO_7/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderMERLO_7):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesMERLO_7 = {}

for pregunta in preguntas:
        filesMERLO_7["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderMERLO_7),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderMERLO_7),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderMERLO_7)]

filesMERLO_7['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderMERLO_7),
                           '{}imagen_orden_ratio.csv'.format(dataFolderMERLO_7),
                           '{}imagen_orden_negativa.csv'.format(dataFolderMERLO_7),
                           '{}serie_imagen.csv'.format(dataFolderMERLO_7)]



imagenes = ["Gustavo Menendez",
            "David Zencich",
            'Karina Menendez',
            "Pablo Cocuzza",
            'Raúl Othacehé',
            'María Luján Rey',
            'Florencia Lizaraso',
            'Flavia Luz Tesone',
           ]
for p, figura in enumerate(imagenes, int('P13'[1:])):
    filesMERLO_7[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_7, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_7,p)]


imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',

           ]

for p, figura in enumerate(imagenes, int('P33'[1:])):
    filesMERLO_7[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderMERLO_7, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderMERLO_7,p)]

preguntasQueNoVanMERLO_7 = ["P06"] # control interno

