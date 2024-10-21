#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:47:47 2024

@author: julian
"""

import csv
import os
import pandas as pd
os.chdir('/home/julian/trabajo/manejoDeArchivos')

ruta_trabajo = '/home/julian/trabajo/updates/corte 266/neuquen/'
nombre_tsv = 'cuestionario.tsv'

cuestionario = pd.read_table(ruta_trabajo + nombre_tsv)
# Lista de códigos
codigos = list(cuestionario.codigo)

# Directorio donde se guardarán los archivos resultantes
output_dir = ruta_trabajo + 'data faltante'
os.makedirs(output_dir, exist_ok=True)

input_dir = ruta_trabajo+'web/cruces'

# Función para procesar cada archivo
def procesar_codigo(codigo):
    # Determinar el sufijo y la base del nombre del archivo
    if "_repregunta" in codigo:
        base_codigo = codigo.replace("_repregunta", "")
        sufijo = "_repregunta"
    elif "_imputada" in codigo:
        base_codigo = codigo.replace("_imputada", "")
        sufijo = "_imputada"
    else:
        return

    # Posibles nombres de archivos de entrada
    input_filenames = [
        f'cruce_pregunta_{base_codigo}.csv',
        f'cruce_pregunta_{base_codigo}_4opc.csv',
        f'cruce_pregunta_{base_codigo}_6opc.csv'
    ]

    # Procesar cada archivo de entrada si existe
    for input_filename in input_filenames:
        input_filepath = os.path.join(input_dir, input_filename)
        if os.path.exists(input_filepath):
            # Leer la primera fila (encabezados) del archivo de entrada
            with open(input_filepath, mode='r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                headers = next(reader)  # Leer la primera fila

            # Determinar el nombre del archivo de salida
            output_filename = input_filename.replace(f'{base_codigo}', f'{base_codigo}{sufijo}')
            output_filepath = os.path.join(output_dir, output_filename)

            # Escribir los encabezados en el archivo de salida
            with open(output_filepath, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
                writer.writerow(headers)

            print(f"Archivo procesado y guardado: {output_filepath}")

#

# Procesar todos los códigos
for codigo in codigos:
    procesar_codigo(codigo)