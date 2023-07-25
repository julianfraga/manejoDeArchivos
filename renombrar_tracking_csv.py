#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:41:03 2023

@author: julian
"""
import os
import csv
import pandas as pd
os.chdir('/home/julian/trabajo/manejoDeArchivos')

ruta_trabajo = '/home/julian/trabajo/updates/corte 202/tracking/'
ruta_csv = ruta_trabajo + 'test.csv'

codigos = pd.read_table(ruta_csv)
codigos.fillna('', inplace=True)

renombramientos = {}
for i, fila in codigos.iterrows():
    if type(fila.nuevos) == float:
        fila.nuevos = int(fila.nuevos)
    fila.nuevos = str(fila.nuevos)
    fila.viejos = str(fila.viejos)
    renombramientos[f'P{fila.viejos}'] = f'P{fila.nuevos}'



# Crear renombramientos temporales
renombramientos_temporales = {}
for cod_viejo, cod_nuevo in renombramientos.items():
    if cod_nuevo != list(renombramientos.keys())[-1]:
        renombramientos_temporales[cod_viejo] = f"TEMP_{cod_nuevo.replace('P','preg')}"

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

with open(ruta_trabajo+'comandos.txt', 'w') as file:
    for comando in comandos_sed_etapa1:
        output = os.popen(comando).read()
        print(comando, file=file)
        # print(output, file=file)
    for comando in comandos_sed_etapa2:
        output = os.popen(comando).read()
        print(comando, file=file)
        # print(output, file=file)
#%%
root = '/home/julian/trabajo/opinionpublica'
carpetas = [root, root+'/trackingNacional/apps', root+'/trackingCABA/apps', root+'/trackingPBA/apps', root+'/trackingAYSA/apps']  # Lista de carpetas
archivo_comandos = ruta_trabajo +'comandos.txt'  # Archivo de texto con los comandos

respuesta = input(f'¿Renombrar según {archivo_comandos}? [S/N]').lower()

if respuesta == 's':
    with open(archivo_comandos, 'r') as file: 
        # Lee el archivo de comandos
        comandos = file.readlines()
       
        for carpeta in carpetas:
            # Cambia al directorio de la carpeta actual
            os.chdir(carpeta)
            print(carpeta)
            
            # Ejecuta los comandos uno por uno
            for comando in comandos:
                comando = comando.strip()  # Elimina los espacios en blanco al inicio y final
                os.system(comando)
else:
    print('Abortadín')
    