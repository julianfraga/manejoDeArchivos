#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:33:56 2024

@author: julian
"""
import shutil
import os

def borrar_contenido_carpeta(carpeta):
    # Borra todo el contenido de la carpeta
    for filename in os.listdir(carpeta):
        file_path = os.path.join(carpeta, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Borra archivos
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Borra carpetas
        except Exception as e:
            print(f'Error al borrar {file_path}: {e}')

def copiar_contenido(origen, destino):
    # Copia el contenido de una carpeta origen a la carpeta destino
    for item in os.listdir(origen):
        origen_item = os.path.join(origen, item)
        destino_item = os.path.join(destino, item)
        try:
            if os.path.isdir(origen_item):
                shutil.copytree(origen_item, destino_item, dirs_exist_ok=True)  # Copia directorios
            else:
                shutil.copy2(origen_item, destino_item)  # Copia archivos
        except Exception as e:
            print(f'Error al copiar {origen_item} a {destino_item}: {e}')

def actualizar_carpeta(carpeta_principal, carpeta_updates):
    # Borra el contenido de la carpeta principal
    borrar_contenido_carpeta(carpeta_principal)
    
    # Copia el contenido de los parches
    for subcarpeta in ['individuales', 'cruces', 'series']:
        ruta_subcarpeta = os.path.join(carpeta_updates, subcarpeta)
        copiar_contenido(ruta_subcarpeta, carpeta_principal)

def actualizar_proyecto(corte):
    base_dir_trabajo = '/home/julian/trabajo/opinionpublica'
    base_dir_updates = f'/home/julian/trabajo/updates/corte {corte}/tracking/web'

    carpetas = {
        'nacional': 'trackingNacional/data',
        'pba': 'trackingPBA/data',  # Ajusta esta ruta según corresponda
        'caba': 'trackingCABA/data'   # Ajusta esta ruta según corresponda
    }
    
    for key, ruta_carpeta in carpetas.items():
        carpeta_principal = os.path.join(base_dir_trabajo, ruta_carpeta)
        carpeta_updates = os.path.join(base_dir_updates, key)
        
        print(f'Actualizando carpeta {ruta_carpeta} con el corte {corte}...')
        actualizar_carpeta(carpeta_principal, carpeta_updates)
        print(f'Actualización de {ruta_carpeta} completada.')

# Uso del script
corte_actual = 264  # Cambia esto por el número de corte actual
actualizar_proyecto(corte_actual)

