#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 18:47:35 2023

@author: julian
"""
import os
os.chdir('/home/julian/trabajo/manejoDeArchivos')
from preguntas_opciones import *
from generarEspeciales import armarEncuesta

ruta_trabajo = '/home/julian/trabajo/updates/corte 246/corrientes/'
# region = 'cipoletti'
nombreEncuesta = 'CORRIENTES_2'

for archivo in os.listdir(ruta_trabajo):
    if archivo.endswith('.docx'):
        nombre_docx = archivo
        break
ruta_cuestionario = ruta_trabajo + nombre_docx
nombre_tsv =   'cuestionario.tsv'

armarEncuesta(nombreEncuesta, nombrePlantilla="NEUQUEN_14")

cuestionarioTSV(ruta_cuestionario, ruta_trabajo, nombre_tsv,rutaData = 'web/individuales',checkCarpeta = True)


# opcionesLimpias = printPaletas(nombre_docx, nombre_tsv, ruta_trabajo, subcarpeta = f'web/{region}/individuales')
opcionesLimpias = printPaletas(nombre_docx, nombre_tsv, ruta_trabajo, subcarpeta = f'web/individuales')

#%%
zonas = ["Rosario","San lorenzo o Villa Constitución","San Martín, Belgrano, Iriondo, Caseros o General López","La Capital","San Jerónimo, Las Colonias, San Justo o Garay","Castellano, San Cristóbal o Nueve de Julio","Vera, General Obligado o San Javier"]
strings = []
for i, zona in enumerate(zonas):
    # print(f"'label' : 'Zona {i+1}: {zona}', 'value' : '{zona}'")
    # strings.append(f'Zona {i+1} ({zona.replace(" o ", " y ")})')
    
    print(f'Zona {i+1} ({zona.replace(" o ", " y ")})')