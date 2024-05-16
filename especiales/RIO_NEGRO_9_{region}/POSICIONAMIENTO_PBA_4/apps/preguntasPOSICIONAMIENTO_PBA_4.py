dataFolderPOSICIONAMIENTO_PBA_4 = './especiales/POSICIONAMIENTO_PBA_4/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_PBA_4):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_PBA_4 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_PBA_4["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_4),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_4),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_4)]

filesPOSICIONAMIENTO_PBA_4['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_PBA_4),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_PBA_4),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_PBA_4),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_PBA_4)]


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
    filesPOSICIONAMIENTO_PBA_4[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_4, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_4,p)]

preguntasQueNoVanPOSICIONAMIENTO_PBA_4 = ['P59','P60'] # control interno

