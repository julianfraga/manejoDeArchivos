dataFolderESCOBAR_1 = './especiales/ESCOBAR_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderESCOBAR_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesESCOBAR_1 = {}

for pregunta in preguntas:
        filesESCOBAR_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderESCOBAR_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderESCOBAR_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderESCOBAR_1)]

filesESCOBAR_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderESCOBAR_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderESCOBAR_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderESCOBAR_1),
                           '{}serie_imagen.csv'.format(dataFolderESCOBAR_1)]



filesESCOBAR_1["Ariel Sujarchuk"] = ['{}cruce_pregunta_P27_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P27_6opc.csv'.format(dataFolderESCOBAR_1)]

filesESCOBAR_1["Roberto Costa"] = ['{}cruce_pregunta_P28_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P28_6opc.csv'.format(dataFolderESCOBAR_1)]

filesESCOBAR_1["Mariano Castagnaro"] = ['{}cruce_pregunta_P29_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P29_6opc.csv'.format(dataFolderESCOBAR_1)]

filesESCOBAR_1["Ricardo Choffi"] = ['{}cruce_pregunta_P30_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P30_6opc.csv'.format(dataFolderESCOBAR_1)]

filesESCOBAR_1["Jesica Avejera"] = ['{}cruce_pregunta_P31_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P31_6opc.csv'.format(dataFolderESCOBAR_1)]

filesESCOBAR_1["Carlos “Beto” Ramil"] = ['{}cruce_pregunta_P32_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P32_6opc.csv'.format(dataFolderESCOBAR_1)]


filesESCOBAR_1["Griselda Romariz"] = ['{}cruce_pregunta_P33_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P33_6opc.csv'.format(dataFolderESCOBAR_1)]


filesESCOBAR_1["Leandro Costa"] = ['{}cruce_pregunta_P34_4opc.csv'.format(dataFolderESCOBAR_1),
                                       '{}cruce_pregunta_P34_6opc.csv'.format(dataFolderESCOBAR_1)]






imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',
            ]

for p, figura in enumerate(imagenes, int("P41"[1:]) ):
    filesESCOBAR_1[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderESCOBAR_1, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderESCOBAR_1,p)]

preguntasQueNoVanESCOBAR_1 = ["P05"] # control interno

