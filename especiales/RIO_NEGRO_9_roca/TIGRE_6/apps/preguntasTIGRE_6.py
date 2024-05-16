dataFolderTIGRE_6 = './especiales/TIGRE_6/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderTIGRE_6):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesTIGRE_6 = {}

for pregunta in preguntas:
        filesTIGRE_6["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_6),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderTIGRE_6),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_6)]

filesTIGRE_6['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderTIGRE_6),
                           '{}imagen_orden_ratio.csv'.format(dataFolderTIGRE_6),
                           '{}imagen_orden_negativa.csv'.format(dataFolderTIGRE_6),
                           '{}serie_imagen.csv'.format(dataFolderTIGRE_6)]



filesTIGRE_6["Malena Galmarini"] = ['{}cruce_pregunta_P08_4opc.csv'.format(dataFolderTIGRE_6),
                                       '{}cruce_pregunta_P08_6opc.csv'.format(dataFolderTIGRE_6)]

filesTIGRE_6["Julio Zamora"] = ['{}cruce_pregunta_P09_4opc.csv'.format(dataFolderTIGRE_6),
                                       '{}cruce_pregunta_P09_6opc.csv'.format(dataFolderTIGRE_6)]

filesTIGRE_6["Segundo Cernadas"] = ['{}cruce_pregunta_P09_4opc.csv'.format(dataFolderTIGRE_6),
                                       '{}cruce_pregunta_P09_6opc.csv'.format(dataFolderTIGRE_6)]
filesTIGRE_6["Juan Laborde Rodríguez"] = ['{}cruce_pregunta_P10_4opc.csv'.format(dataFolderTIGRE_6),
                                       '{}cruce_pregunta_P10_6opc.csv'.format(dataFolderTIGRE_6)]
filesTIGRE_6["Nicolás Massot"] = ['{}cruce_pregunta_P11_4opc.csv'.format(dataFolderTIGRE_6),
                                       '{}cruce_pregunta_P12_6opc.csv'.format(dataFolderTIGRE_6)]


imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',
            ]

for p, figura in enumerate(imagenes, 23):
    filesTIGRE_6[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderTIGRE_6, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderTIGRE_6,p)]

preguntasQueNoVanTIGRE_6 = ["P05"] # control interno

