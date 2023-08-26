#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 14:06:17 2023

@author: julian
"""

import os
os.chdir('/home/julian/trabajo/opinionpublica')
from txt import textos
import csv
       
def cuestionarioTSV_especial(diccionario, rutaGuardado='/home/julian/trabajo/updates', nombreArchivo = ''):
    '''
    Lee las preguntas y bloques previamente pasados a diccionario y arma un csv
    completando código, bloque y texto
    '''
    preguntas = diccionario['preguntas']
    labels = diccionario['labels']
    bloques = ['Preferencias electorales']
    claves = diccionario['preguntas'].keys()
    campos =['codigo','bloque','paleta','texto','label','aclaracion']
    
    
    while len(nombreArchivo)<1:
        nombreArchivo = input('nombre del tsv: ')
    
    if '.tsv' not in nombreArchivo:
        nombreArchivo += '.tsv'
    
    rutaCompleta = rutaGuardado+'/'+nombreArchivo        
    with open(rutaCompleta, 'w', newline='') as archivoTSV:
        writer = csv.writer(archivoTSV, delimiter='\t')
        
        writer.writerow(campos)

        # Iterar sobre las claves y escribir los valores correspondientes en cada columna
        for clave in claves:
            
            pregunta = preguntas[clave]
            label = labels[clave]
            bloque = bloques[0]
            if 'BIS' in clave or 'bis' in clave:
                continue
            # Escribir una nueva fila en el archivo TSV
            writer.writerow([clave, bloque, '', pregunta, label, ''])
    
        print('Archivo TSV generado exitosamente.')
        
os.chdir('/home/julian/trabajo/manejoDeArchivos')

cuestionario= {'labels':{}, 'preguntas':{}}
for key in list(textos):
    if 'imagen' in key:
        continue
    if 'labelP' in key:
        label = key.lstrip('label')
        cuestionario['labels'][label] = textos[key]
    if 'pregunta' in key:
        pregunta = key.lstrip('pregunta')
        cuestionario['preguntas'][pregunta] = textos[key]
 
nombreArchivo = 'corte 207 (PASO)/cuestionario_reversion.tsv' 
cuestionarioTSV_especial(cuestionario, nombreArchivo= nombreArchivo)
# codigos_lab = list(cuestionario['labels'])
# codigos_preg = list(cuestionario['preguntas'])

# for codigo in codigos_preg:
#     if codigo not in codigos_lab:
#         print(codigo)