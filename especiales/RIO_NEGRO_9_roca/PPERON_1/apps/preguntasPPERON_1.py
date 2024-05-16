dataFolderPPERON_1 = './especiales/PPERON_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPPERON_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPPERON_1 = {}

for pregunta in preguntas:
        filesPPERON_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPPERON_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPPERON_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPPERON_1)]

filesPPERON_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPPERON_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPPERON_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPPERON_1),
                           '{}serie_imagen.csv'.format(dataFolderPPERON_1)]


imagenes = ["Alberto Fernandez",
            'CFK',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta"]

for p, figura in enumerate(imagenes, 10):
    filesPPERON_1[figura] = ['{}cruce_pregunta_P{}_5opc.csv'.format(dataFolderPPERON_1, p),
                                       '{}cruce_pregunta_P{}_3opc.csv'.format(dataFolderPPERON_1,p)]

preguntasQueNoVanPPERON_1 = [] # control interno

