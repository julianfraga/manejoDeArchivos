dataFolderPOSICIONAMIENTO_PBA_1 = './especiales/POSICIONAMIENTO_PBA_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_PBA_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_PBA_1 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_PBA_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_1)]

filesPOSICIONAMIENTO_PBA_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_PBA_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_PBA_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_PBA_1),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_PBA_1)]


imagenes = ['CFK',
            "Alberto Fernandez",
            'Sergio Massa',
            'Axel Kicillof',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta",
            "Maria Eugenia Vidal",
            'Javier Milei',
            'Patricia Bullrich']

for p, figura in enumerate(imagenes, 31):
    filesPOSICIONAMIENTO_PBA_1[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_1, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_1,p)]

preguntasQueNoVanPOSICIONAMIENTO_PBA_1 = [] # control interno

