dataFolderSANTIAGO2 = './especiales/SANTIAGO2/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderSANTIAGO2):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesSANTIAGO2 = {}

for pregunta in preguntas:
        filesSANTIAGO2["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderSANTIAGO2),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderSANTIAGO2),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderSANTIAGO2)]

filesSANTIAGO2['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderSANTIAGO2),
                           '{}imagen_orden_ratio.csv'.format(dataFolderSANTIAGO2),
                           '{}imagen_orden_negativa.csv'.format(dataFolderSANTIAGO2),
                           '{}serie_imagen.csv'.format(dataFolderSANTIAGO2)]
#
filesSANTIAGO2["csvP06_imputados"] = [('{}pregunta_P06__imputada.csv').format(dataFolderSANTIAGO2),
                                      ('{}cruce_pregunta_P06__imputada.csv').format(dataFolderSANTIAGO2)]
filesSANTIAGO2["csvP08_imputados"] = [('{}pregunta_P08__imputada.csv').format(dataFolderSANTIAGO2),
                                      ('{}cruce_pregunta_P08__imputada.csv').format(dataFolderSANTIAGO2)
                                      ]



filesSANTIAGO2['Alberto Fernandez']        = ['{}cruce_pregunta_P15_5opc.csv'.format(dataFolderSANTIAGO2),
                                  '{}cruce_pregunta_P15_3opc.csv'.format(dataFolderSANTIAGO2)]
filesSANTIAGO2['CFK']                      = ['{}cruce_pregunta_P17_5opc.csv'.format(dataFolderSANTIAGO2),
                                  '{}cruce_pregunta_P17_3opc.csv'.format(dataFolderSANTIAGO2)]
filesSANTIAGO2['Mauricio Macri']           = ['{}cruce_pregunta_P16_5opc.csv'.format(dataFolderSANTIAGO2),
                                  '{}cruce_pregunta_P16_3opc.csv'.format(dataFolderSANTIAGO2)]
filesSANTIAGO2['Horacio Rodriguez Larreta']= ['{}cruce_pregunta_P18_5opc.csv'.format(dataFolderSANTIAGO2),
                                  '{}cruce_pregunta_P18_3opc.csv'.format(dataFolderSANTIAGO2)]
filesSANTIAGO2['Sergio Massa']             = ['{}cruce_pregunta_P19_5opc.csv'.format(dataFolderSANTIAGO2),
                                  '{}cruce_pregunta_P19_3opc.csv'.format(dataFolderSANTIAGO2)]



preguntasQueNoVanSANTIAGO2 = ["P20"] # control interno

