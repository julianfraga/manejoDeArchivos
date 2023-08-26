#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:38:33 2023

@author: julian
"""

import os
import shutil
import fileinput
import re

def generarCarpetas(nombreEncuesta, rutaInsercion = './especiales/', rutaPlantilla = "/home/julian/trabajo/opinionpublica/especiales/BASE_1"):
    if not rutaInsercion.endswith('/'):
        rutaInsercion+='/'
    # Ruta donde se crearán las carpetas modificadas
    rutaDestino = rutaInsercion + nombreEncuesta

    # Copiar la carpeta plantilla a la ubicación de destino
    shutil.copytree(rutaPlantilla, rutaDestino)


def renombrarArchivos(nombreEncuesta, rutaInsercion = './especiales/'):
    if not rutaInsercion.endswith('/'):
        rutaInsercion+='/'

    rutaDestino = f"{rutaInsercion}{nombreEncuesta}/apps"
    if not os.path.exists(rutaDestino):
        raise OSError("La ruta de destino no es válida.")
        
    # Expresión regular para buscar cualquier nombre de archivo con "BASE_1"
    patron_archivo = re.compile(r'(.*BASE_1.py)')

    for ruta_actual, carpetas, archivos in os.walk(rutaDestino):
        if ruta_actual.endswith('/__pycache__'):
            continue
        
        for archivo in archivos:
            # Buscar coincidencias con el patrón 
            match = patron_archivo.match(archivo)
            if match:
                nuevo_nombre = match.group(1).replace('BASE_1', nombreEncuesta)
                os.rename(os.path.join(ruta_actual, archivo), os.path.join(ruta_actual, nuevo_nombre))


def renombreInterno(nombreEncuesta):
    # Ruta de la carpeta donde se copiaron las carpetas modificadas
    rutaDestino = "./especiales/" + nombreEncuesta

    # Recorrer todos los archivos en la carpeta de destino y reemplazar "BASE_1" por "nombreEncuesta"
    for rutaActual, carpetas, archivos in os.walk(rutaDestino):
        for archivo in archivos:
            rutaArchivo = os.path.join(rutaActual, archivo)
            with fileinput.FileInput(rutaArchivo, inplace=True) as archivo_inplace:
                for linea in archivo_inplace:
                    print(linea.replace("BASE_1", nombreEncuesta), end='')

# Nombre que deseas para la encuesta
nombre_encuesta = "nombreEncuesta"

# Llamamos a las funciones para generar carpetas y renombrar internamente
generarCarpetas(nombre_encuesta, rutaInsercion= '/home/julian/trabajo/manejoDeArchivos')
renombrarArchivos(nombre_encuesta, rutaInsercion= '/home/julian/trabajo/manejoDeArchivos')
renombreInterno(nombre_encuesta)
