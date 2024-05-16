dataFolderSAN_ISIDRO_1 = './especiales/SAN_ISIDRO_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderSAN_ISIDRO_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesSAN_ISIDRO_1 = {}

for pregunta in preguntas:
        filesSAN_ISIDRO_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderSAN_ISIDRO_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderSAN_ISIDRO_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderSAN_ISIDRO_1)]

filesSAN_ISIDRO_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderSAN_ISIDRO_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderSAN_ISIDRO_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderSAN_ISIDRO_1),
                           '{}serie_imagen.csv'.format(dataFolderSAN_ISIDRO_1)]


imagenes = ["Alberto Fernandez",
            'CFK',
            'Sergio Massa',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta"]

for p, figura in enumerate(imagenes, 21):
    filesSAN_ISIDRO_1[figura] = ['{}cruce_pregunta_P{}_5opc.csv'.format(dataFolderSAN_ISIDRO_1, p),
                                       '{}cruce_pregunta_P{}_3opc.csv'.format(dataFolderSAN_ISIDRO_1,p)]

preguntasQueNoVanSAN_ISIDRO_1 = ["P05"] # control interno

