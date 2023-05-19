# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from docx import Document

def getOpciones(ruta):
    ''' 
    Genera un diccionario con el siguiente formato
    {'P01':['opcion_1', ... ,'opcion_N'],
     'P02':['opcion_1', ... ,'opcion_N'],
     etc}
    '''
    archivo = Document(ruta)
    opciones = {}
    for parrafo in archivo.paragraphs:
        texto = parrafo.text
        if not texto:
            continue
        
        if 'Pregunta' in texto:
            codigo = texto.strip('Pregunta ')
            codigo = 'P'+str.zfill(codigo, 2)
            opciones[codigo] = []
        
        if 'Presione' in texto or 'presione' in texto:
            opciones[codigo].append(texto)
    
    opciones_limpias = {}
    for pregunta in opciones:
        opciones_limpias[pregunta] = []
        if pregunta == "P1":
            opciones_limpias["P1"] = opciones["P1"]
        
        for indice, opcion in enumerate(opciones[pregunta]):
            texto_limpio = opcion.replace(" Presione ", "")[:-2]
            opciones_limpias[pregunta].append(texto_limpio)

    return(opciones_limpias)

def getPreguntas(ruta):
    ''' 
    Genera un diccionario con el siguiente formato
    {'P01':' se deja en blanco, TO:DO',
     'P02': 'texto 2',
     'P03': 'texto 3',
     etc} 
    '''
    
    archivo = Document(ruta)
    preguntas = {}
    codigo = 0

    banderin_apertura = False
    for parrafo in archivo.paragraphs:

        texto = parrafo.text
        
        if not texto:
            continue

        if 'pregunta' in texto.lower() and 'ahora' not in texto.lower():
            numero = texto.strip('Pregunta ')
            codigo = 'P'+str.zfill(numero, 2)
            preguntas[codigo] = ''
            
            banderin_apertura = True
            continue
        
        elif codigo in preguntas.keys() and banderin_apertura == True:
            
            if 'Presione' not in texto:
                preguntas[codigo]= texto
                banderin_apertura = False
    return preguntas
#
# ejemplo de uso
# ruta = '/home/julian/trabajo/updates/corte 195/Encuesta politica y elecciones_Mayo 2023 (1).docx'
# opciones = getOpciones(ruta)
# preguntas = getPreguntas(ruta)
