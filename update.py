# -*- coding: utf-8 -*-
"""
Este programa es un script que realiza las siguientes tareas:
1. Crea un archivo "changelog.txt" en la carpeta "update".
2. Registra todo el contenido de la carpeta "destino/data" en "changelog.txt", 
   incluyendo la ubicación original, el nombre del archivo, el tamaño (en MB) y
   la fecha de modificación.
3. Elimina todo el contenido de la carpeta "destino/data".
4. Copia todo el contenido de la carpeta "update" a la carpeta "destino/data".
5. Registra el contenido copiado en "changelog.txt", incluyendo la ubicación 
   original, el nombre del archivo, el tamaño (en MB) y la fecha de 
   modificación.

El programa puede ser ejecutado desde la línea de comandos y toma dos argumentos:
- La ruta hacia la carpeta "update".
- La ruta hacia la carpeta "destino".

Ejemplo de uso: python programa.py /ruta/hacia/update /ruta/hacia/destino
"""


import os
import shutil
from datetime import datetime


def create_changelog_file(update_folder):
    """
    Crea un archivo "changelog.txt" en la carpeta especificada.
    
    Argumentos:
    folder -- La ruta hacia la carpeta donde se creará el archivo.
    
    Retorna:
    None
    """
    
    changelog_file = os.path.join(update_folder, 'changelog.txt')
    with open(changelog_file, 'w') as f:
        f.write('ubicación original, nombre del archivo, tamaño (MB), fecha de modificación\n')
    return changelog_file


def add_to_changelog_file(changelog_file, folder_path, header):
    """
    Registra información sobre un archivo en el archivo "changelog.txt".
    
    Argumentos:
    changelog_file -- La ruta hacia la carpeta donde se encuentra el archivo 
    "changelog.txt".   
    folder_path -- La ubicación original del archivo.
    header -- Explicativo.
    
    Retorna:
    None
    """
    
    with open(changelog_file, 'a') as f:
        f.write(f'\n #Contenido de la carpeta "{folder_path}" {header}:\n')
        f.write('# --------------------------------------------------------------------\n')
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for file_name in filenames:
                file_path = os.path.join(dirpath, file_name)
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                mod_time = os.path.getmtime(file_path)
                mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
                f.write(f'{dirpath}, {file_name}, {file_size:.2f}, {mod_time_str}\n')


def remove_csv_files(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.csv'):
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)


def copy_csv_files(update_folder, data_folder):
    """
    Copia todos los archivos con formato ".csv" desde la carpeta de origen a la
    carpeta de destino.
    
    Argumentos:
    update_folder -- La ruta hacia la carpeta de origen.
    data_folder -- La ruta hacia la carpeta de destino.
    
    Retorna:
    archivos -- Lista de archivos contenido en update_folder y sus ramas
    """
    archivos = []
    for dirpath, dirnames, filenames in os.walk(update_folder):
        for file_name in filenames:
            if file_name.endswith('.csv'):
                source_file_path = os.path.join(dirpath, file_name)
                destination_file_path = os.path.join(data_folder, file_name)
                shutil.copy2(source_file_path, destination_file_path)
                
                archivos.append(file_name) 
    return(archivos) #guardo la lista de archivos en el árbol

def update_data(update_folder, data_folder):
    """
    Función principal que crea "changelog.txt" en la carpeta especificada
    como primer argumento 'update_folder', elimina todo los archivos de 
    'data_folder/data' y copia el contenido de 'update_folder' a la carpeta
    aterior
    
    Argumentos:
    update_folder -- La ruta hacia la carpeta de origen.
    data_folder -- La ruta hacia la carpeta de destino.
    
    Retorna:
    archivos -- Lista de archivos contenido en update_folder y sus ramas
    """
    changelog_file = create_changelog_file(update_folder)
    
    add_to_changelog_file(changelog_file, data_folder, 'antes de ser eliminado')
    remove_csv_files(data_folder)
    
    add_to_changelog_file(changelog_file, update_folder, 'antes de ser copiado')
    archivos_update = copy_csv_files(update_folder, data_folder) #guardo la lista de archivos en el árbol
    
    add_to_changelog_file(changelog_file, data_folder, 'después de ser actualizado')
    
    archivos_data = os.listdir(data_folder)

    if archivos_update==archivos_data:
        print(f'Archivos en {update_folder} copiados con éxito a {data_folder}')
    else:
        print('ADVERTENCIA: la lista de archivos en {archivos_update} no coincide con la de {archivos_data}')

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print('Debe proporcionar dos rutas: la ruta a la carpeta "update" y la ruta a la carpeta "destino"')
        sys.exit(1)
    
    update_folder = sys.argv[1]
    data_folder = os.path.join(sys.argv[2], 'data')
    update_data(update_folder, data_folder)
    
