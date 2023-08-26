#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 00:09:35 2023

@author: julian
"""
from docx import Document
import pandas as pd
import os
import csv
os.chdir('/home/julian/trabajo/manejoDeArchivos')
from preguntas_opciones import *
ruta_trabajo = '/home/julian/trabajo/updates/corte 201/tracking/'
ruta_cuestionario = ruta_trabajo + 'Encuesta Trackeo version 201.docx'

opciones = getOpciones(ruta_cuestionario)
preguntas = getPreguntas(ruta_cuestionario)

codigos_borrar = []
for codigo in preguntas.keys():
    if codigo not in opciones.keys():
        continue
    elif len(opciones[codigo]) == 0:
        codigos_borrar.append(codigo)
for codigo in codigos_borrar:
    del opciones[codigo]
    del preguntas[codigo]

renombramientos = {}
for codigo in preguntas.keys():
    if 'ex' in codigo:
        cadena = codigo.translate({ord(i): None for i in '() '})
        cod_viejo, cod_nuevo = cadena.split('ex')
        renombramientos[cod_viejo] = cod_nuevo


# Crear renombramientos temporales
renombramientos_temporales = {}
for cod_viejo, cod_nuevo in renombramientos.items():
    if cod_nuevo != list(renombramientos.keys())[-1]:
        renombramientos_temporales[cod_viejo] = f"TEMP_{cod_nuevo}"

# Generar los comandos sed en la primera etapa (renombramientos temporales)
comandos_sed_etapa1 = []
for cod_viejo, cod_temp in renombramientos_temporales.items():
    comando_sed = f"sed -i 's/{cod_viejo}/{cod_temp}/g' *.py"
    comandos_sed_etapa1.append(comando_sed)

# Generar los comandos sed en la segunda etapa (renombramientos finales)
comandos_sed_etapa2 = []
for cod_viejo, cod_nuevo in renombramientos.items():
    if cod_nuevo != list(renombramientos.keys())[-1]:
        cod_temp = renombramientos_temporales[cod_viejo]
        comando_sed = f"sed -i 's/{cod_temp}/{cod_nuevo}/g' *.py"
        comandos_sed_etapa2.append(comando_sed)

# Imprimir los comandos sed en pantalla
for comando in comandos_sed_etapa1:
    print(comando)
for comando in comandos_sed_etapa2:
    print(comando)
