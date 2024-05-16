dataFolderSANTIAGO_3 = './especiales/SANTIAGO_3/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderSANTIAGO_3):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesSANTIAGO_3 = {}

for pregunta in preguntas:
        filesSANTIAGO_3["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderSANTIAGO_3),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderSANTIAGO_3),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderSANTIAGO_3)]

filesSANTIAGO_3['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderSANTIAGO_3),
                           '{}imagen_orden_ratio.csv'.format(dataFolderSANTIAGO_3),
                           '{}imagen_orden_negativa.csv'.format(dataFolderSANTIAGO_3),
                           '{}serie_imagen.csv'.format(dataFolderSANTIAGO_3)]


imagenes = ["Alberto Fernandez",
            'CFK',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta"]

for p, figura in enumerate(imagenes, 9):
    filesSANTIAGO_3[figura] = ['{}cruce_pregunta_P{}_5opc.csv'.format(dataFolderSANTIAGO_3, str(p).zfill(2)),
                                       '{}cruce_pregunta_P{}_3opc.csv'.format(dataFolderSANTIAGO_3,str(p).zfill(2))]

preguntasQueNoVanSANTIAGO_3 = ["P05"] # control interno

