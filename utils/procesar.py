#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:14:20 2022

@author: Julián Fraga

Una serie de funciones para manejar archivos png dispersos en distintos direc-
torios y agruparlos juntos dentro de uno nuevo llamado por default 'imgs_procesadas'

"""

import os

def recorrer_arbol(rutini):
    '''
    Recorre un directorio y devuelve una lista de tuplas con las carpetas y ar-
    chivos encontrados. El formato es el siguiente:
    elementos = [(dir_actual), (subdir_2, ... ,subdir_n), (arch_1, ..., arch_n)]
    '''
    elementos=[]
    
    if not type(rutini)==str:
        
        raise TypeError('El argumento debe ser una cadena')
        
    for directorio in os.walk(rutini):
        elementos.append(directorio)
    return(elementos)


def listaDeArchivos(rutini, formato = '.png'):
    '''
    Devuelve dos listas: uno con los nombres de los archivos .png encontrados
    y otra con las rutas completas
    '''
    elementos = recorrer_arbol(rutini)
    imagenes = []
    rutas = []
        
    for elemento in elementos:
        padre = elemento[0]
        lista_de_archivos = elemento[2]
        
        for archivo in lista_de_archivos:
            
            if archivo.endswith(formato):
                
                ruta = os.path.join(padre, archivo)
                imagenes.append(archivo)
                rutas.append(ruta)
    
    return (imagenes, rutas)            


def procesar(imagen,fname, nombreDirectorio = 'imgs_procesadas', formato = '.png'):
    '''
    Procesa una imagen dada y la mueve a la carpeta imgs_procesadas
    Si no existe la carpeta en el directorio actual, la crea
    '''
    if not nombreDirectorio in os.listdir():
        directorio = './' + nombreDirectorio
        os.mkdir(directorio)
    
    
    ruta_nueva = os.path.join( nombreDirectorio , imagen)
    ruta_vieja=fname

    os.rename(ruta_vieja, ruta_nueva)

    os.rename(ruta_nueva, ruta_nueva[:-4]+ formato)


def procesar_carpeta(directorio, formato = '.png', directorioDestino = 'imgs_procesadas'):
    '''
    Itera la función "procesar_imagenes()" sobre todas las subcarpetas de un
    directorio, incluído sí mismo.
    '''
    imagenes, rutas = listaDeArchivos(directorio, formato)
    for indice, imagen in enumerate(imagenes):
        ruta = rutas[indice]
        procesar(imagen,ruta, directorioDestino)



def borrar_carpetas_vacias(directorio):
    '''
    Autodescriptivo sobre un directorio y sus subcarpetas
    '''
    hubo_cambios=True
    while hubo_cambios:
        arbol = recorrer_arbol(directorio)
        hubo_cambios = False
        
        for rama in arbol:
            
            if len(rama[1]) == 0 and len(rama[2]) == 0:
                os.rmdir(rama[0])
                hubo_cambios = True

def main():
    directorio = input('Ingrese la ruta a procesar: ')
    formato = input('Especifique un formato de archivo buscado.' 
                    +'Si no especifica, se mostrarán todos: ')
    print('Estos son los archivos encontrados:')
    print(listaDeArchivos(directorio, formato)[0])
    decision = input('¿Desea extraer los archivos? [S/N] ').upper()
    
    if decision != 'S':
        return
    
    directorioDestino = input('Indique el nombre de la nueva carpeta ')
    
    decision = input('¿Desea cambiar el formato de archivo? [S/N] ').upper()
    if decision =='S':
        formato = input('Ingrese el nuevo formato')
        if not formato.startswith('.'):
            formato = '.'+formato
    else:
        formato = '.png'
    
    procesar_carpeta(directorio, formato, directorioDestino)
    
    decision = input('¿Desea borrar las carpetas vacías? [S/N] ').upper()
    if decision =='S':
        borrar_carpetas_vacias(directorio)

if __name__ == '__main__':
    import sys
    main()
