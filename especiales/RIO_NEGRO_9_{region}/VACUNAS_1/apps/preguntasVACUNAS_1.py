dataFolderVACUNAS_1 = './especiales/VACUNAS_1/data/'
import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderVACUNAS_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesVACUNAS_1 = {}

for pregunta in preguntas:
        filesVACUNAS_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderVACUNAS_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderVACUNAS_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderVACUNAS_1)]
