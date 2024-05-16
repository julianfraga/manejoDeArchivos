dataFolderPOSICIONAMIENTO_PBA_3 = './especiales/POSICIONAMIENTO_PBA_3/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_PBA_3):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_PBA_3 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_PBA_3["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_3),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_3),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_3)]

filesPOSICIONAMIENTO_PBA_3['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_PBA_3),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_PBA_3),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_PBA_3),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_PBA_3)]


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
    filesPOSICIONAMIENTO_PBA_3[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_3, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_3,p)]

preguntasQueNoVanPOSICIONAMIENTO_PBA_3 = [] # control interno

