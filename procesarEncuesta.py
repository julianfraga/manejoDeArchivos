#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 00:48:41 2023

@author: julian
"""

from docx import Document
import pandas as pd
import os
import csv
os.chdir('/home/julian/trabajo/manejoDeArchivos')
from preguntas_opciones import *
# ejemplo de uso
ruta_trabajo = '/home/julian/trabajo/updates/corte 208/transporte/'
ruta_cuestionario = ruta_trabajo + 'Cuestionario_Transporte.docx'
opciones = limpiarKeys(getOpciones(ruta_cuestionario))
preguntas = getPreguntas(ruta_cuestionario)
bloques = getBloque(ruta_cuestionario)

nombre_tsv =   'cuestionario.tsv'
cuestionarioTSV(ruta_cuestionario, ruta_trabajo, nombre_tsv)
#%%
'''
Una vez guardados los diccionarios Opciones, Preguntas y Bloques, este bloque
printea los labels de las preguntas de imagen y reach
'''
cuestionario = pd.read_table(ruta_trabajo + nombre_tsv)

for codigo in preguntas.keys():
    gen = ''

    if 'imagen' in preguntas[codigo]:
        candidato = preguntas[codigo].lstrip('¿Qué imagen tiene de ').strip('?')
        print('Imagen de '+candidato)
    elif ', ud.' in preguntas[codigo] or 'Votaría' in preguntas[codigo]:
        
        if 'candidato' in preguntas[codigo]:
            gen = 'm'
        elif 'candidata' in preguntas[codigo]:
            gen = 'f'
        
        if 'presiden' in preguntas[codigo]:
            if gen == 'f':
                puesto = 'presidenta'
            else:
                puesto = 'presidente'
                
        elif 'intenden' in preguntas[codigo]:
            if gen == 'f':
                puesto = 'intendenta'
            elif gen == 'm':
                puesto = 'intendente'
                
        elif 'goberna' in preguntas[codigo] and 'vice' in preguntas[codigo]:
            if gen == 'f':
                puesto = 'vicegobernadora'
            elif gen == 'm':
                puesto = 'vicegobernador'
                
        elif 'goberna' in preguntas[codigo] and 'vice' not in preguntas[codigo]:
            if gen == 'f':
                puesto = 'gobernadora'
            elif gen == 'm':
                puesto = 'gobernador'
                
        elif 'diputa' in preguntas[codigo] :
            if gen == 'f':
                puesto = 'diputada'
            elif gen == 'm':
                puesto = 'diputado'
                
        candidato = ' '.join(preguntas[codigo].split()[3:5])


        print('Intención de voto por '+candidato +' para ' + puesto)

#%%
'''Una vez agregadas las paletas a mano en el cuestionario, este bloque 
levanta el csv e imprime las paletas de cada pregunta (faltan agregar algunas como
Frecuencia, muchoPoco, siNo, etc, una plantilla)'''
# archivo = path + 'Encuesta_Merlo_2023_05_16.docx'
# opciones = getOpciones(archivo)
def printPaletas(texto, nombre_tsv, ruta_trabajo):
    ruta_cuestionario = ruta_trabajo + texto
    cuestionario = pd.read_table(ruta_trabajo + nombre_tsv)
    opciones = limpiarKeys(getOpciones(ruta_cuestionario))

    opciones_limpias = {}
    for key in opciones:
        codigo_limpio = key[:3]
        if codigo_limpio in cuestionario.codigo.to_list():
            opciones_limpias[codigo_limpio] = opciones[key]
    
    
    
    bloques = cuestionario.groupby('bloque', sort=False).agg(list)['codigo'].to_dict()
    
    infer_paleta(opciones, cuestionario)
    return(opciones_limpias)
#%%
bloque = ''
for i, linea in cuestionario.iterrows():
    codigo = linea.codigo
    label = linea.label
    if bloque != linea.bloque:
        bloque = linea.bloque
        print(f'# Bloque {bloque}')
    # print(f"'pregunta{codigo}' : '{preguntas[codigo]}'")

    print(f"'pregunta{codigo}' : '{linea.texto}',")
    print(f"'label{codigo}' : '{label}',")
    print()
#%%
import os
preguntas_ocultas = []
carpeta_data = '/home/julian/trabajo/updates/corte 200/pos especial/web/caba'
individuales = [s.strip('pregunta_').strip('.csv') for s in os.listdir(carpeta_data+'/individuales')]
cruces = [s.strip('cruce_pregunta_').strip('.csv') for s in os.listdir(carpeta_data+'/cruces')]

for codigo in preguntas.keys():
    if 'BIS' in codigo:
        continue
    if codigo not in individuales:
        preguntas_ocultas.append(codigo)
print(repr(preguntas_ocultas))
