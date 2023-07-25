#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:34:23 2023

@author: julian
"""

diccionario = {'labelTEMP_TEMP_Pborrar': 'Imagen de Alberto Fernández',
    'labelPborrar': 'Imagen de Cristina Fernández de Kirchner',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Mauricio Macri',
    'labelTEMP_Pborrar': 'Imagen de Horacio Rodríguez Larreta',
    'labelPborrar': 'Imagen de Sergio Massa',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de María Eugenia Vidal',
    'labelPborrar': 'Imagen de Axel Kicillof',
    'labelPborrar': 'Imagen de Martin Insaurralde',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Daniel Scioli',
    'labelPborrar': 'Imagen de Diego Santilli',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Néstor Grindeti',
    'labelPborrar': 'Imagen de Javier Milei',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Patricia Bullrich',
    'labelPborrar': 'Imagen de Facundo Manes',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Wado de Pedro',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Máximo Kirchner',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Malena Galmarini',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Elisa Carrio',
    'labelTEMP_TEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Martín Lousteau',
    'labelTEMP_TEMP_TEMP_TEMP_P78': 'Imagen de Gerardo Morales',
    'labelTEMP_TEMP_TEMP_P78': 'Imagen de Juan Schiaretti'}


mapa = {}
for label in diccionario.keys():
    codigo = label.strip('label')
    candidato = diccionario[label].replace('Imagen de ', '')
    mapa[codigo] = candidato

for codigo in mapa.keys():
    candidato = mapa[codigo]
    print(f"filesNacional['{candidato}'] = "+ "['{}"+f"cruce_pregunta_{codigo}_6opc.csv'.format(dataFolderNacional),"+"'{}"+f"cruce_pregunta_{codigo}_4opc.csv'.format(dataFolderNacional)]")