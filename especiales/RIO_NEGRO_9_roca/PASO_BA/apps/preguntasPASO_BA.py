dataFolderPASO_BA = './especiales/PASO_BA/data/'
import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPASO_BA):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPASO_BA = {}

for pregunta in preguntas:
        filesPASO_BA["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPASO_BA),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPASO_BA),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPASO_BA)]
