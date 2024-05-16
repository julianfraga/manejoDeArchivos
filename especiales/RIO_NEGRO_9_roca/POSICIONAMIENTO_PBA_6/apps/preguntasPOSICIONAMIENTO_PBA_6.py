dataFolderPOSICIONAMIENTO_PBA_6 = './especiales/POSICIONAMIENTO_PBA_6/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_PBA_6):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_PBA_6 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_PBA_6["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_6),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_6),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_PBA_6)]

filesPOSICIONAMIENTO_PBA_6['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_PBA_6),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_PBA_6),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_PBA_6),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_PBA_6)]


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
    filesPOSICIONAMIENTO_PBA_6[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_6, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_PBA_6,p)]

preguntasQueNoVanPOSICIONAMIENTO_PBA_6 = ['P57','P58'] # control interno

