dataFolderPPERON_2 = './especiales/PPERON_2/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPPERON_2):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPPERON_2 = {}

for pregunta in preguntas:
        filesPPERON_2["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPPERON_2),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPPERON_2),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPPERON_2)]

filesPPERON_2['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPPERON_2),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPPERON_2),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPPERON_2),
                           '{}serie_imagen.csv'.format(dataFolderPPERON_2)]


imagenes = ["Alberto Fernandez",
            'CFK',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta"]

for p, figura in enumerate(imagenes, 19):
    filesPPERON_2[figura] = ['{}cruce_pregunta_P{}_5opc.csv'.format(dataFolderPPERON_2, p),
                                       '{}cruce_pregunta_P{}_3opc.csv'.format(dataFolderPPERON_2,p)]

preguntasQueNoVanPPERON_2 = [] # control interno

