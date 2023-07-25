#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:04:01 2023

@author: julian
"""

renombramientos = {}

lista = list(renombramientos.keys())
lista.reverse()
for codigo in range()
for viejo in lista:
    print (viejo+','+renombramientos[viejo])
#%%
import os
listaDeArchivos = os.listdir('/home/julian/trabajo/opinionpublica/trackingPBA/data')
orden_cruces = []
for archivo in listaDeArchivos:
    if archivo.startswith('pregunta_P'):
        orden_cruces.append(archivo.strip('.csv').replace('pregunta_', ''))
orden_cruces.sort()
repr(orden_cruces)
