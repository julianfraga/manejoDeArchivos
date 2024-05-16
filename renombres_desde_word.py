#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:58:23 2023

@author: julian
"""

from docx import Document
import pandas as pd
import os
import csv
os.chdir('/home/julian/trabajo/manejoDeArchivos')
from preguntas_opciones import *


ruta_trabajo = '/home/julian/trabajo/updates/corte 236/tracking/'
ruta_cuestionario = ruta_trabajo + 'Encuenta de tracking 236.docx'
nombre_tsv =   'cuestionario_tracking.tsv'
cuestionarioTSV(ruta_cuestionario, ruta_trabajo, nombre_tsv)
cuestionario = pd.read_table(ruta_trabajo + nombre_tsv)
#%%
import os
os.chdir('/home/julian/trabajo/opinionpublica/')
from txt import textos

for index, row in cuestionario.iterrows():
    codigo = row.codigo
    texto = row.texto.strip()
    if texto in textos:
        
        if f'pregunta{codigo}' in textos:
            cuestionario.at[index, 'label'] = textos[f'label{codigo}']

cuestionario.to_csv(ruta_trabajo +'labeleado_'+ nombre_tsv, sep= '\t', index = False)


#%%
# renombres
ruta_trabajo = '/home/julian/trabajo/updates/corte 236/tracking/'
ruta_cuestionario = ruta_trabajo + 'Encuenta de tracking 236.docx'
archivo = Document(ruta_cuestionario)
opciones = {}
for parrafo in archivo.paragraphs:
    texto = parrafo.text
    if not texto:
        continue
    if 'rotada' in texto.lower() or 'rotadas' in texto.lower():
        continue
    if 'Pregunta' in texto:
        codigo = texto.strip('Pregunta ')
        codigo = 'P'+str.zfill(codigo, 2)
        opciones[codigo] = []
    
    if 'Presione' in texto or 'presione' in texto:
        opciones[codigo].append(texto)

opciones_limpias = {}
for pregunta in opciones:
    opciones_limpias[pregunta] = []
    if pregunta == "P1":
        opciones_limpias["P1"] = opciones["P1"]
    
    for indice, opcion in enumerate(opciones[pregunta]):
        texto_limpio = opcion.replace(" Presione ", "")[:-2]
        texto_limpio = texto_limpio.replace('.','')
        opciones_limpias[pregunta].append(texto_limpio)
        
keys = []
for key in opciones_limpias:
    if 'BIS' not in str(key):
        print(f"'{key}' : ", opciones_limpias[key])
        print()
        keys.append(key)

renombres = {}

for key in keys:
    if 'EX' in key.upper():
        nuevo, viejo = key.upper().replace(' ','').replace('(','').strip(')').split('EX')
        renombres[viejo]= nuevo
        
renombres_df = pd.DataFrame.from_dict(renombres, orient='index',columns = ['nuevos'])
renombres_df.to_csv(f'{ruta_trabajo}renombres.csv')
