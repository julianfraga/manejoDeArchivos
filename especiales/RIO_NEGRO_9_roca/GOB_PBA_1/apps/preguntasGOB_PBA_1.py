dataFolderGOB_PBA_1 = './especiales/GOB_PBA_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderGOB_PBA_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))


filesGOB_PBA_1 = {}

for pregunta in preguntas:
        filesGOB_PBA_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderGOB_PBA_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderGOB_PBA_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderGOB_PBA_1)]

filesGOB_PBA_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderGOB_PBA_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderGOB_PBA_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderGOB_PBA_1),
                           '{}serie_imagen.csv'.format(dataFolderGOB_PBA_1)]


imagenes = [
            "Alberto Fernandez",
            'CFK',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',
            "Maria Eugenia Vidal",
            "Daniel Scioli",
            "Facundo Manes",
            "Gerardo Morales"]

for p, figura in enumerate(imagenes, int("P45"[1:])):
    filesGOB_PBA_1[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderGOB_PBA_1, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderGOB_PBA_1,p)]

preguntasQueNoVanGOB_PBA_1 = ['P56','P57','P22'] # control interno

