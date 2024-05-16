dataFolderSAN_MARTIN_1 = './especiales/SAN_MARTIN_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderSAN_MARTIN_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesSAN_MARTIN_1 = {}

for pregunta in preguntas:
        filesSAN_MARTIN_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderSAN_MARTIN_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderSAN_MARTIN_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderSAN_MARTIN_1)]

filesSAN_MARTIN_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderSAN_MARTIN_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderSAN_MARTIN_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderSAN_MARTIN_1),
                           '{}serie_imagen.csv'.format(dataFolderSAN_MARTIN_1)]




filesSAN_MARTIN_1["Santiago López Medrano"] = ['{}cruce_pregunta_P31_4opc.csv'.format(dataFolderSAN_MARTIN_1),
                                       '{}cruce_pregunta_P31_6opc.csv'.format(dataFolderSAN_MARTIN_1)]

filesSAN_MARTIN_1["Fernando Moreira"] = ['{}cruce_pregunta_P32_4opc.csv'.format(dataFolderSAN_MARTIN_1),
                                       '{}cruce_pregunta_P32_6opc.csv'.format(dataFolderSAN_MARTIN_1)]

filesSAN_MARTIN_1["Andrés Petrillo"] = ['{}cruce_pregunta_P33_4opc.csv'.format(dataFolderSAN_MARTIN_1),
                                       '{}cruce_pregunta_P33_6opc.csv'.format(dataFolderSAN_MARTIN_1)]
filesSAN_MARTIN_1["Gabriel Katopodis"] = ['{}cruce_pregunta_P34_4opc.csv'.format(dataFolderSAN_MARTIN_1),
                                       '{}cruce_pregunta_P34_6opc.csv'.format(dataFolderSAN_MARTIN_1)]
filesSAN_MARTIN_1["Mauricio D’alessandro"] = ['{}cruce_pregunta_P35_4opc.csv'.format(dataFolderSAN_MARTIN_1),
                                       '{}cruce_pregunta_P35_6opc.csv'.format(dataFolderSAN_MARTIN_1)]

filesSAN_MARTIN_1["Juan Esleiman"] = ['{}cruce_pregunta_P36_4opc.csv'.format(dataFolderSAN_MARTIN_1),
                                       '{}cruce_pregunta_P36_6opc.csv'.format(dataFolderSAN_MARTIN_1)]

filesSAN_MARTIN_1["Leonardo Grosso"] = ['{}cruce_pregunta_P37_4opc.csv'.format(dataFolderSAN_MARTIN_1),
                                       '{}cruce_pregunta_P37_6opc.csv'.format(dataFolderSAN_MARTIN_1)]




imagenes = ["Santiago López Medrano",
            'Fernando Moreira',
            "Andrés Petrillo",
            "Gabriel Katopodis",
            'Mauricio D’alessandro',
            'Juan Esleiman',
            'Leonardo Grosso',

            ]

for p, figura in enumerate(imagenes, int("P31"[1:]) ):
    filesSAN_MARTIN_1[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderSAN_MARTIN_1, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderSAN_MARTIN_1,p)]

preguntasQueNoVanSAN_MARTIN_1 = ["P05"] # control interno

