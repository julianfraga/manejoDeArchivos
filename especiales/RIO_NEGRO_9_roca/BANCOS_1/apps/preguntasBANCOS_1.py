dataFolderBANCOS_1 = './especiales/BANCOS_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderBANCOS_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesBANCOS_1 = {}

for pregunta in preguntas:
        filesBANCOS_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderBANCOS_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderBANCOS_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderBANCOS_1)]

filesBANCOS_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderBANCOS_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderBANCOS_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderBANCOS_1),
                           '{}serie_imagen.csv'.format(dataFolderBANCOS_1)]


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

for p, figura in enumerate(imagenes, 47):
    filesBANCOS_1[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderBANCOS_1, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderBANCOS_1,p)]

preguntasQueNoVanBANCOS_1 = ['P59','P60'] # control interno

