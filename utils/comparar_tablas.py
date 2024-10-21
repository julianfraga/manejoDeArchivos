#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:43:52 2024

@author: julian
"""

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Rutas a los archivos TSV
ruta_A = '/home/julian/trabajo/opinionpublica/especiales/NEUQUEN_22/tablas/cuestionario.tsv'
ruta_B = "/home/julian/trabajo/updates/corte 266/neuquen/cuestionario.tsv"

# Cargar los archivos TSV en DataFrames
df_A = pd.read_csv(ruta_A, sep='\t')
df_B = pd.read_csv(ruta_B, sep='\t')

# Columnas a copiar
columnas_a_copiar = ['bloque', 'paleta', 'label', 'aclaracion']

# Función para buscar coincidencias aproximadas entre textos
def encontrar_coincidencia(texto_A, lista_textos_B):
    # Usamos el proceso de fuzzy matching para buscar el texto más similar
    resultado = process.extractOne(texto_A, lista_textos_B, scorer=fuzz.token_sort_ratio)
    # Retornamos el texto coincidente y la puntuación de similitud
    return resultado[0], resultado[1]

# Recorremos la tabla A y buscamos coincidencias con la tabla B
for idx_A, row_A in df_A.iterrows():
    texto_A = row_A['texto']
    
    # Buscamos la mejor coincidencia en la columna 'texto' de B
    mejor_texto_B, puntuacion = encontrar_coincidencia(texto_A, df_B['texto'])
    
    # Si la similitud es suficientemente alta (umbral del 90%)
    if puntuacion > 90:
        # Encontrar el índice de la coincidencia en B
        idx_B = df_B[df_B['texto'] == mejor_texto_B].index[0]
        
        # Copiar las columnas correspondientes de A a B
        df_B.loc[idx_B, columnas_a_copiar] = df_A.loc[idx_A, columnas_a_copiar]

# Guardar los cambios en el archivo B
df_B.to_csv(ruta_B, sep='\t', index=False)
