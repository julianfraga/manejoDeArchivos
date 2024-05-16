dataFolderTIGRE = './especiales/TIGRE/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderTIGRE):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesTIGRE = {}

for pregunta in preguntas:
        filesTIGRE["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderTIGRE),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderTIGRE),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderTIGRE)]

filesTIGRE['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderTIGRE),
                           '{}imagen_orden_ratio.csv'.format(dataFolderTIGRE),
                           '{}imagen_orden_negativa.csv'.format(dataFolderTIGRE),
                           '{}serie_imagen.csv'.format(dataFolderTIGRE)]
#
filesTIGRE["csvP06_imputados"] = [('{}pregunta_P06__imputada.csv').format(dataFolderTIGRE),
                                      ('{}cruce_pregunta_P06__imputada.csv').format(dataFolderTIGRE)]
filesTIGRE["csvP08_imputados"] = [('{}pregunta_P08__imputada.csv').format(dataFolderTIGRE),
                                      ('{}cruce_pregunta_P08__imputada.csv').format(dataFolderTIGRE)
                                      ]

imagenes = ["Alberto Fernandez",
            "Mauricio Macri",
            "Cristina Fernández de Kirchner",
            "María Eugenia Vidal",
            "Axel Kicillof",
            "Horacio Rodriguez Larreta",
            "Malena Galmarini",
            "Sergio Massa",
            "Julio Zamora",
            "Segundo Cernadas"]

for p, figura in enumerate(imagenes, 18):
    filesTIGRE[figura] = ['{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderTIGRE, p),
                                       '{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderTIGRE,p)]

#
# filesTIGRE['Alberto Fernandez']        = ['{}cruce_pregunta_P15_5opc.csv'.format(dataFolderTIGRE),
#                                   '{}cruce_pregunta_P15_3opc.csv'.format(dataFolderTIGRE)]
# filesTIGRE['CFK']                      = ['{}cruce_pregunta_P17_5opc.csv'.format(dataFolderTIGRE),
#                                   '{}cruce_pregunta_P17_3opc.csv'.format(dataFolderTIGRE)]
# filesTIGRE['Mauricio Macri']           = ['{}cruce_pregunta_P16_5opc.csv'.format(dataFolderTIGRE),
#                                   '{}cruce_pregunta_P16_3opc.csv'.format(dataFolderTIGRE)]
# filesTIGRE['Horacio Rodriguez Larreta']= ['{}cruce_pregunta_P18_5opc.csv'.format(dataFolderTIGRE),
#                                   '{}cruce_pregunta_P18_3opc.csv'.format(dataFolderTIGRE)]
# filesTIGRE['Sergio Massa']             = ['{}cruce_pregunta_P19_5opc.csv'.format(dataFolderTIGRE),
#                                   '{}cruce_pregunta_P19_3opc.csv'.format(dataFolderTIGRE)]
#
#

preguntasQueNoVanTIGRE = ["P06", 'P17',"P28"] # control interno

