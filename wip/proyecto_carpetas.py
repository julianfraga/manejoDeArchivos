#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:14:55 2023

@author: julian
"""
import os
os.chdir('/home/julian/trabajo/opinionpublica')

from especiales.TRACKING_DIARIO_NACIONAL.apps.paletas_TRACKING_DIARIO_NACIONAL import paletas
archivos = (sorted(os.listdir('./especiales/TRACKING_DIARIO_NACIONAL/data/individuales'), key=len))
for archivo in archivos:
    if not 'pregunta' in archivo:
        continue
    
    nombre = archivo.lstrip('pregunta_').rstrip('.csv')
    codigo = nombre[0:3]

os.listdir('./especiales/TRACKING_DIARIO_NACIONAL/data/')
#%%
path = './especiales/TRACKING_DIARIO_NACIONAL/data/'
import pandas as pd
import os
path = path[:-1] if path.endswith('/') else path
preguntas = []
contenido = os.listdir(path)
carpetas_posibles = ['series', 'cruces', 'individuales']
if any(carpeta in contenido for carpeta in carpetas_posibles):
    archivos_csv = []
    for carpeta in contenido:
        archivos_csv+=os.listdir(f'{path}/{carpeta}')
    
for archivo in archivos_csv:
    if archivo.startswith('pregunta'):
        preguntas.append(archivo.split('pregunta_')[1][:-4])
        #%%
        
def get_preguntas(path='./'):
    import pandas as pd
    import os
    path = path[:-1] if path.endswith('/') else path
    preguntas = []
    contenido = os.listdir(path)
    carpetas_posibles = ['series', 'cruces', 'individuales']
    if any(carpeta in contenido for carpeta in carpetas_posibles):
        archivos_csv = []
        for carpeta in contenido:
            archivos_csv+=os.listdir(f'{path}/{carpeta}')
        
    for archivo in archivos_csv:
        if archivo.startswith('pregunta'):
            preguntas.append(archivo.split('pregunta_')[1][:-4])