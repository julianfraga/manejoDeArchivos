dataFolderPOSICIONAMIENTO_CBA_1 = './especiales/POSICIONAMIENTO_CBA_1/data/'

import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderPOSICIONAMIENTO_CBA_1):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesPOSICIONAMIENTO_CBA_1 = {}

for pregunta in preguntas:
        filesPOSICIONAMIENTO_CBA_1["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_CBA_1),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_CBA_1),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderPOSICIONAMIENTO_CBA_1)]

filesPOSICIONAMIENTO_CBA_1['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderPOSICIONAMIENTO_CBA_1),
                           '{}imagen_orden_ratio.csv'.format(dataFolderPOSICIONAMIENTO_CBA_1),
                           '{}imagen_orden_negativa.csv'.format(dataFolderPOSICIONAMIENTO_CBA_1),
                           '{}serie_imagen.csv'.format(dataFolderPOSICIONAMIENTO_CBA_1)]


imagenes = [
    'Rodrigo de Loredo',
    'Luis Juez',
    'Martín Llaryora',
    'Aurelio García Elorrio',
    'Alberto Fernandez',
    'CFK',
    'Mauricio Macri',
    'Horacio Rodriguez Larreta',
    'Sergio Massa',
    'Patricia Bullrich',
    'Juan Schiaretti',
    'Javier Milei',
    'Martín Lousteau',
    'Gerardo Morales',
    'Facundo Manes',

]

for p, figura in enumerate(imagenes, int("P25"[1:])):
    filesPOSICIONAMIENTO_CBA_1[figura] = ['{}cruce_pregunta_P{}_4opc.csv'.format(dataFolderPOSICIONAMIENTO_CBA_1, p),
                                       '{}cruce_pregunta_P{}_6opc.csv'.format(dataFolderPOSICIONAMIENTO_CBA_1,p)]

preguntasQueNoVanPOSICIONAMIENTO_CBA_1 = ['P05', 'P71','P72'] # control interno

