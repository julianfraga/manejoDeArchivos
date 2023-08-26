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
    
    rutaData = os.path.join(rutaDestino, "data")
    
    # Eliminar contenido de la carpeta "data" sin borrar la carpeta en sí
    for elemento in os.listdir(rutaData):
        elementoRuta = os.path.join(rutaData, elemento)
        if os.path.isfile(elementoRuta):
            os.remove(elementoRuta)
        elif os.path.isdir(elementoRuta):
            shutil.rmtree(elementoRuta)


def renombrarArchivos(nombreEncuesta, rutaInsercion = "/home/julian/trabajo/opinionpublica/especiales/"):
    if not rutaInsercion.endswith('/'):
        rutaInsercion+='/'

    rutaDestino = f"{rutaInsercion}{nombreEncuesta}/apps"
    if not os.path.exists(rutaDestino):
        raise OSError("La ruta de destino no es válida.")
        
    # Expresión regular para buscar cualquier nombre de archivo con "BASE_1"
    patronArchivo = re.compile(r'(.*BASE_1.py)')

    for rutaActual, carpetas, archivos in os.walk(rutaDestino):
        if '/__pycache__' in rutaActual:
            continue
        
        for archivo in archivos:
            # Buscar coincidencias con el patrón 
            match = patronArchivo.match(archivo)
            if match:
                nuevoNombre = match.group(1).replace('BASE_1', nombreEncuesta)
                os.rename(os.path.join(rutaActual, archivo), os.path.join(rutaActual, nuevoNombre))


def renombreInterno(nombreEncuesta, rutaInsercion = "/home/julian/trabajo/opinionpublica/especiales/"):
    if not rutaInsercion.endswith('/'):
        rutaInsercion+='/'

    rutaDestino = f"{rutaInsercion}{nombreEncuesta}/apps"
    if not os.path.exists(rutaDestino):
        raise OSError("La ruta de destino no es válida.")
    
    archivosModificados = []
    # Recorrer todos los archivos en la carpeta de destino y reemplazar "BASE_1" por "nombreEncuesta"
    for rutaActual, carpetas, archivos in os.walk(rutaDestino):
        if '/__pycache__' in rutaActual:
            continue
        for archivo in archivos:
            rutaArchivo = os.path.join(rutaActual, archivo)
            with fileinput.FileInput(rutaArchivo, inplace=True) as archivoInplace:
                for linea in archivoInplace:
                    nuevaLinea = linea.replace("BASE_1", nombreEncuesta)
                    print(nuevaLinea, end='')
                    if nuevaLinea != linea:
                        if rutaArchivo not in archivosModificados:
                            archivosModificados.append(rutaArchivo)

    # Imprimir los nombres de los archivos modificados
    print("Archivos modificados:")
    for archivo_modificado in archivosModificados:
        print(archivo_modificado)

def armarEncuesta(nombreEncuesta, rutaInsercion = "/home/julian/trabajo/opinionpublica/especiales/"):
    # Llamamos a las funciones para generar carpetas y renombrar internamente
    print('Generando encuesta en {rutaInsercion}/{nombreEncuesta}')
    generarCarpetas(nombreEncuesta, rutaInsercion)
    renombrarArchivos(nombreEncuesta, rutaInsercion)
    renombreInterno(nombreEncuesta,  rutaInsercion)
