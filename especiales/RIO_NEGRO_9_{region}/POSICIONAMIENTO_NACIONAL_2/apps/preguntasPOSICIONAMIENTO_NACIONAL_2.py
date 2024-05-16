dataFolderPOSICIONAMIENTO_NACIONAL_2 = './especiales/POSICIONAMIENTO_NACIONAL_2/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_NACIONAL_2):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_NACIONAL_2 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_NACIONAL_2["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_NACIONAL_2),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_NACIONAL_2),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_NACIONAL_2)]

filesPOSICIONAMIENTO_NACIONAL_2['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_2),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_2),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_2),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_2)]


imagenes = [
            "Alberto Fernandez",
            'CFK',
            "Mauricio Macri",
            "Horacio Rodriguez Larreta",
            'Sergio Massa',
            'Javier Milei',
            "Maria Eugenia Vidal",
            "Daniel Scioli",
            "Gerardo Morales"]

for p, figura in enumerate(imagenes, 39):
    filesPOSICIONAMIENTO_NACIONAL_2[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_2, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_NACIONAL_2,p)]

preguntasQueNoVanPOSICIONAMIENTO_NACIONAL_2 = [] # control interno

