dataFolderPOSICIONAMIENTO_CABA_1 = './especiales/POSICIONAMIENTO_CABA_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_CABA_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_CABA_1 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_CABA_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_CABA_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_CABA_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_CABA_1)]

filesPOSICIONAMIENTO_CABA_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_CABA_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_CABA_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_CABA_1),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_CABA_1)]


imagenes = [
    "Jorge Macri",
    "Leandro Santoro",
    "María Eugenia Vidal",
    "Soledad Acuña",
    "Martín Lousteau",
    "Matías Lammens",
    "Ricardo López Murphy",
    "Fernán Quirós",
    'Mariano Recalde',
    'Lucía Cámpora',
    "Gobierno Nacional",
    "Alberto Fernandez",
    'CFK',
    "Mauricio Macri",
    "Horacio Rodriguez Larreta",
    'Sergio Massa',
    'Patricia Bullrich',
    'Javier Milei',
    "Facundo Manes",
            ]

for p, figura in enumerate(imagenes, int("P52"[1:])):
    filesPOSICIONAMIENTO_CABA_1[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_CABA_1, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_CABA_1,p)]

preguntasQueNoVanPOSICIONAMIENTO_CABA_1 = ['P04', 'P71','P72'] # control interno

