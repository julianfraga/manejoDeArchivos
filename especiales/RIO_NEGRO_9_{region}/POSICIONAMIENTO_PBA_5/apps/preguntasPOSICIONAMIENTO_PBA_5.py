dataFolderPOSICIONAMIENTO_PBA_5 = './especiales/POSICIONAMIENTO_PBA_5/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_PBA_5):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_PBA_5 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_PBA_5["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_5),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_5),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_5)]

filesPOSICIONAMIENTO_PBA_5['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_PBA_5),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_PBA_5),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_PBA_5),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_PBA_5)]


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
    filesPOSICIONAMIENTO_PBA_5[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_5, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_5,p)]

preguntasQueNoVanPOSICIONAMIENTO_PBA_5 = ['P59','P60'] # control interno

