dataFolderBANCOS_2 = './especiales/BANCOS_2/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderBANCOS_2):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesBANCOS_2 = {}

for pregunta in preguntas:
        filesBANCOS_2["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderBANCOS_2),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderBANCOS_2),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderBANCOS_2)]


preguntasQueNoVanBANCOS_2 = ['P59','P60'] # control interno

