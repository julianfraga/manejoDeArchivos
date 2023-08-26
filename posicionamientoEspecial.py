#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:58:42 2023

@author: julian
"""

import os
import pandas as pd
from manejoDeArchivos.preguntas_opciones import *

ruta_trabajo = '/home/julian/trabajo/updates/corte 208/posicionamiento_especial/'
cuestionario_raw = pd.read_table(ruta_trabajo + 'cuestionario.tsv')
cuestionario = cuestionario_raw.copy()
cuestionario.nacion = 0
cuestionario.pba = 0
cuestionario.caba = 0

ambito = '/nacional'

ruta_actual = ruta_trabajo+'/web'+ambito+'/individuales'
listaDeArchivos = [codigo.strip('pregunta_').strip('.csv') for codigo in os.listdir(ruta_actual)]

for pregunta in listaDeArchivos:
    cuestionario.loc[cuestionario['codigo'] == pregunta, 'nacion'] = 1
        
ambito = '/caba'

ruta_actual = ruta_trabajo+'/web'+ambito+'/individuales'
listaDeArchivos = [codigo.strip('pregunta_').strip('.csv') for codigo in os.listdir(ruta_actual)]

for pregunta in listaDeArchivos:
    cuestionario.loc[cuestionario['codigo'] == pregunta, 'caba'] = 1
        
ambito = '/pba'

ruta_actual = ruta_trabajo+'/web'+ambito+'/individuales'
listaDeArchivos = [codigo.strip('pregunta_').strip('.csv') for codigo in os.listdir(ruta_actual)]

for pregunta in listaDeArchivos:
    cuestionario.loc[cuestionario['codigo'] == pregunta, 'pba'] = 1

cuestionario.to_csv(ruta_trabajo+'cuestionario_corregido.csv',index=False)       
#%%


cuestionario = pd.read_csv(ruta_trabajo+'cuestionario_corregido.csv')

cuestionario_caba = cuestionario[cuestionario.caba == 1]
cuestionario_nacional = cuestionario[cuestionario.nacion == 1]
cuestionario_pba = cuestionario[cuestionario.pba == 1]

cuestionario_caba.to_csv(ruta_trabajo+'cuestionario_caba.csv',index=False) 
cuestionario_nacional.to_csv(ruta_trabajo+'cuestionario_nacional.csv',index=False) 
cuestionario_pba.to_csv(ruta_trabajo+'cuestionario_pba.csv',index=False) 
#%%
ruta_cuestionario = ruta_trabajo + 'Encuesta de posicionamiento y preferencias electorales - corte 5.docx'
opciones = limpiarKeys(getOpciones(ruta_cuestionario))

nombre_csv = 'cuestionario_nacional.csv'
cuestionario = pd.read_csv(ruta_trabajo + nombre_csv)


bloques = cuestionario.groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

infer_paleta(opciones, cuestionario)
