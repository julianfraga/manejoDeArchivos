dataFolderTIGRE_10 = './especiales/TIGRE_10/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderTIGRE_10):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesTIGRE_10 = {}

for pregunta in preguntas:
        filesTIGRE_10["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_10),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderTIGRE_10),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderTIGRE_10)]

filesTIGRE_10['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderTIGRE_10),
                           '{}imagen_orden_ratio.csv'.format(dataFolderTIGRE_10),
                           '{}imagen_orden_negativa.csv'.format(dataFolderTIGRE_10),
                           '{}serie_imagen.csv'.format(dataFolderTIGRE_10)]



filesTIGRE_10["Malena Galmarini"] = ['{}cruce_pregunta_P14_4opc.csv'.format(dataFolderTIGRE_10),
                                       '{}cruce_pregunta_P14_6opc.csv'.format(dataFolderTIGRE_10)]

filesTIGRE_10["Julio Zamora"] = ['{}cruce_pregunta_P15_4opc.csv'.format(dataFolderTIGRE_10),
                                       '{}cruce_pregunta_P15_6opc.csv'.format(dataFolderTIGRE_10)]

filesTIGRE_10["Segundo Cernadas"] = ['{}cruce_pregunta_P15_4opc.csv'.format(dataFolderTIGRE_10),
                                       '{}cruce_pregunta_P15_6opc.csv'.format(dataFolderTIGRE_10)]
filesTIGRE_10["Juan Laborde Rodríguez"] = ['{}cruce_pregunta_P16_4opc.csv'.format(dataFolderTIGRE_10),
                                       '{}cruce_pregunta_P16_6opc.csv'.format(dataFolderTIGRE_10)]
filesTIGRE_10["Nicolás Massot"] = ['{}cruce_pregunta_P17_4opc.csv'.format(dataFolderTIGRE_10),
                                       '{}cruce_pregunta_P18_6opc.csv'.format(dataFolderTIGRE_10)]


imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            'CFK',
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',
            ]

for p, figura in enumerate(imagenes, int("P34"[1:]) ):
    filesTIGRE_10[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderTIGRE_10, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderTIGRE_10,p)]

preguntasQueNoVanTIGRE_10 = ["P05"] # control interno

