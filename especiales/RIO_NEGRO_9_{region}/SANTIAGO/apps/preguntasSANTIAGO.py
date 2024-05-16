dataFolderSANTIAGO = './especiales/SANTIAGO/data/'
import os
import re
pat = 'P[0-9]{2}'
preguntas = []
archivos_con_opciones = []
preguntas_con_opciones = []
for csv in os.listdir(dataFolderSANTIAGO):
    pregunta = re.findall(pat, csv)
    preguntas.extend(pregunta)

    if 'opc' in csv:
        preguntas_con_opciones.extend(pregunta)

preguntas = list(sorted(set(preguntas)))
preguntas_con_opciones = list(sorted(set(preguntas_con_opciones)))



filesSANTIAGO = {}

for pregunta in preguntas:
        filesSANTIAGO["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(dataFolderSANTIAGO),
                                  ('{}serie_' + pregunta + '.csv').format(dataFolderSANTIAGO),
                                  ('{}cruce_pregunta_' + pregunta + '.csv').format(dataFolderSANTIAGO)]

filesSANTIAGO['csv_imagen'] = ['{}imagen_orden_positiva.csv'.format(dataFolderSANTIAGO),
                           '{}imagen_orden_ratio.csv'.format(dataFolderSANTIAGO),
                           '{}imagen_orden_negativa.csv'.format(dataFolderSANTIAGO),
                           '{}serie_imagen.csv'.format(dataFolderSANTIAGO)]

filesSANTIAGO["csvP08_imputados"] = [('{}pregunta_P08__imputada.csv').format(dataFolderSANTIAGO)]
filesSANTIAGO["csvP10_imputados"] = [('{}pregunta_P10__imputada.csv').format(dataFolderSANTIAGO)]
filesSANTIAGO["TransferenciaP08-P09"] = [('{}transferencia_P8_P9.csv').format(dataFolderSANTIAGO)]


preguntas_imagen = {'Mauricio Macri': 'P19',
                    'Alberto Fernandez': 'P20',
                    'Cristina Fernández de Kirchner': 'P21',
                    'CFK': 'P21',
                    'Horacio Rodriguez Larreta': 'P22',
                    'Sergio Massa': 'P23',
                    'Patricia Bullrich': 'P24',
                    'María Eugenia Vidal': 'P25',
                    'Gerardo Zamora': 'P26',
                    'Pablo Mirolo': 'P27',
                    'Ricardo Rodrigo Posse': 'P28',
                    'Natalia Neme': 'P29',
                    'Emilio Rached': 'P30',
                    'Marcelo Lugones': 'P31',
                    'Facundo Perez Carletti': 'P32',
                    'Hector Chabay Ruiz': 'P33',
                    'Claudia Zamora': 'P34',
                    'Emilio Pichon Neder': 'P35'}

for figura, pregunta in preguntas_imagen.items():
    filesSANTIAGO[figura] = ['{}cruce_pregunta_{}_5opc.csv'.format(dataFolderSANTIAGO, pregunta),
                                   '{}cruce_pregunta_{}_3opc.csv'.format(dataFolderSANTIAGO, pregunta)]

preguntasQueNoVanSANTIAGO = ["P18"] # control interno

