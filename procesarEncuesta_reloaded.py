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

ruta_trabajo = '/home/julian/trabajo/updates/corte 208/rionegro/'
ruta_cuestionario = ruta_trabajo + 'Rio_Negro_Agosto.docx'
nombre_tsv =   'cuestionario.tsv'
nombreEncuesta = 'RIO_NEGRO_5'
#%%
armarEncuesta(nombreEncuesta)
cuestionarioTSV(ruta_cuestionario, ruta_trabajo, nombre_tsv)
opcionesLimpias = printPaletas('Cuestionario_Transporte.docx', nombre_tsv, ruta_trabajo)
