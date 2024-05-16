dataFolderPOSICIONAMIENTO_NACIONAL_8 = './especiales/POSICIONAMIENTO_NACIONAL_8/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_NACIONAL_8):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_NACIONAL_8 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_NACIONAL_8["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_NACIONAL_8),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_NACIONAL_8),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_NACIONAL_8)]

filesPOSICIONAMIENTO_NACIONAL_8['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_8),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_8),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_8),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_8)]


imagenes = [
            "Alberto Fernandez",
            'CFK',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Patricia Bullrich',
            'Javier Milei',
            "Maria Eugenia Vidal",
            "Wado de Pedro",
            "Facundo Manes",
            ]

for p, figura in enumerate(imagenes, int("P43"[1:])):
    filesPOSICIONAMIENTO_NACIONAL_8[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_8, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_8,p)]

preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_8 = ['P53','P54'] # control interno

