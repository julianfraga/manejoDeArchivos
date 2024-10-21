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

def generarCarpetas(nombreEncuesta, nombrePlantilla, rutaInsercion = './especiales/'):
    if not rutaInsercion.endswith('/'):
        rutaInsercion+='/'
    # Ruta donde se crearán las carpetas modificadas
    rutaDestino = rutaInsercion + nombreEncuesta

    # Copiar la carpeta plantilla a la ubicación de destino
    shutil.copytree(f"/home/julian/trabajo/opinionpublica/especiales/{nombrePlantilla}", rutaDestino)
    
    rutaData = os.path.join(rutaDestino, "data")
    
    # Eliminar contenido de la carpeta "data" sin borrar la carpeta en sí
    for elemento in os.listdir(rutaData):
        elementoRuta = os.path.join(rutaData, elemento)
        if os.path.isfile(elementoRuta):
            os.remove(elementoRuta)
        elif os.path.isdir(elementoRuta):
            shutil.rmtree(elementoRuta)


def renombrarArchivos(nombreEncuesta, nombrePlantilla, rutaInsercion = "/home/julian/trabajo/opinionpublica/especiales/"):
    if not rutaInsercion.endswith('/'):
        rutaInsercion+='/'

    rutaDestino = f"{rutaInsercion}{nombreEncuesta}/apps"
    if not os.path.exists(rutaDestino):
        raise OSError("La ruta de destino no es válida.")
        
    # Expresión regular para buscar cualquier nombre de archivo con "BASE_1"
    patronArchivo = re.compile(r'(.*{}.py)'.format(nombrePlantilla))

    for rutaActual, carpetas, archivos in os.walk(rutaDestino):
        if '/__pycache__' in rutaActual:
            continue
        
        for archivo in archivos:
            # Buscar coincidencias con el patrón 
            match = patronArchivo.match(archivo)
            if match:
                nuevoNombre = match.group(1).replace(nombrePlantilla, nombreEncuesta)
                os.rename(os.path.join(rutaActual, archivo), os.path.join(rutaActual, nuevoNombre))


def renombreInterno(nombreEncuesta, nombrePlantilla, rutaInsercion = "/home/julian/trabajo/opinionpublica/especiales/"):
    if not rutaInsercion.endswith('/'):
        rutaInsercion+='/'

    rutaDestino = f"{rutaInsercion}{nombreEncuesta}/apps"
    if not os.path.exists(rutaDestino):
        raise OSError("La ruta de destino no es válida.")
    
    archivosModificados = []
    # Recorrer todos los archivos en la carpeta de destino y reemplazar "nombrePlantilla" por "nombreEncuesta"
    for rutaActual, carpetas, archivos in os.walk(rutaDestino):
        if '/__pycache__' in rutaActual:
            continue
        for archivo in archivos:
            rutaArchivo = os.path.join(rutaActual, archivo)
            with fileinput.FileInput(rutaArchivo, inplace=True) as archivoInplace:
                for linea in archivoInplace:
                    nuevaLinea = linea.replace(nombrePlantilla, nombreEncuesta)
                    print(nuevaLinea, end='')
                    if nuevaLinea != linea:
                        if rutaArchivo not in archivosModificados:
                            archivosModificados.append(rutaArchivo)

    # Imprimir los nombres de los archivos modificados
    print("Archivos modificados:")
    for archivo_modificado in archivosModificados:
        print(archivo_modificado)


def armarEncuesta(nombreEncuesta, rutaInsercion="/home/julian/trabajo/opinionpublica/especiales/", nombrePlantilla = "BASE_1" ):
    # Llamamos a las funciones para generar carpetas y renombrar internamente
    print(f'Generando encuesta en {rutaInsercion}/{nombreEncuesta}')
    try:
        generarCarpetas(nombreEncuesta, nombrePlantilla, rutaInsercion)
        renombrarArchivos(nombreEncuesta, nombrePlantilla, rutaInsercion)
        renombreInterno(nombreEncuesta, nombrePlantilla, rutaInsercion)
        
        # # Ruta del archivo especiales_config.py
        # rutaConfig = "/home/julian/trabajo/opinionpublica/especiales/especiales_config.py"
        
        # # Agregar nombreEncuesta a la lista titulos
        # with fileinput.FileInput(rutaConfig, inplace=True) as archivoInplace:
        #     for linea in archivoInplace:
        #         if "titulos =" in linea:
        #             nuevaLinea =  f"['{nombreEncuesta}',\n" + linea.lstrip()[:-1]
        #         else:
        #             nuevaLinea = linea
        #         print(nuevaLinea, end='')
        
        # # Agregar nombreEncuesta al diccionario especiales_label
        # with fileinput.FileInput(rutaConfig, inplace=True) as archivoInplace:
        #     for linea in archivoInplace:
        #         if "especiales_labels =" in linea:
        #             nuevaLinea = linea.rstrip()[:-1] + f", '{nombreEncuesta}': '{nombreEncuesta}',\n"
        #         else:
        #             nuevaLinea = linea
        #         print(nuevaLinea, end='')
        
    except(FileExistsError):
        print('YA EXISTE UNA ENCUESTA CON ESE NOMBRE')