import os
import csv
import pandas as pd
from utils.docx_parser import get_preguntas, getOpciones, getBloque

def limpiarKeys(diccionario):
    diccionarioLimpio = {}
    for key, value in diccionario.items():
        keyLimpia = key.replace('?', '')
        diccionarioLimpio[keyLimpia] = value
    return diccionarioLimpio

def cuestionarioTSV(ruta, rutaGuardado='.', nombreArchivo='cuestionario.tsv', ruta_individuales='web/individuales/', check_carpeta=True ):
    """
    Generate a TSV file containing the questionnaire data.
    Parameters:
    - ruta (str): The path to the input file.
    - rutaGuardado (str): The path to the directory where the output file will be saved. Default is the current directory.
    - nombreArchivo (str): The name of the output file. Default is 'cuestionario.tsv'.
    - ruta_individuales (str): ruta de preguntas individuales. Default 'web/individuales'
    - check_carpeta (bool): compara las preguntas extraídas del documento de texto con los csv contenidos en ruta_individuales. Default True
    Returns:
    None
    Raises:
    None
    """
    preguntas = get_preguntas(ruta)
    opciones = getOpciones(ruta)
    bloques = getBloque(ruta)
    
    # Filtrar las preguntas para que solo incluyan las que están en la carpeta de preguntas individuales
    if check_carpeta:
        preguntas_existentes = sorted([key.lstrip('pregunta_').rstrip('.csv') for key in os.listdir(os.path.join(rutaGuardado, ruta_individuales))])
        preguntas_filtradas = {k: v for k, v in preguntas.items() if k in preguntas_existentes}
    
    # Añadir preguntas que están en preguntas_existentes pero no en preguntas
    for pregunta in preguntas_existentes:
        if pregunta not in preguntas_filtradas:
            base_key = pregunta.split('_')[0]  # Obtener la clave base sin sufijo
            if base_key in preguntas:
                preguntas_filtradas[pregunta] = preguntas[base_key]
    
    header = ['codigo', 'bloque', 'paleta','texto','label', 'aclaracion']
    rutaSalida = os.path.join(rutaGuardado, nombreArchivo)
    
    with open(rutaSalida, 'w', newline='') as archivo_tsv:
        escritor = csv.writer(archivo_tsv, delimiter='\t')
        escritor.writerow(header)
        
        for pregunta, texto in preguntas_filtradas.items():
            bloque = bloques.get(pregunta.split('_')[0], '')
            paleta = 'qualitative_strong' if len(opciones.get(pregunta.split('_')[0], [])) <= 5 else 'diverging'
            
            if '_imputada' in pregunta:
                aclaracion = "(Imputación no lineal de indecisos)"
            elif '_repregunta' in pregunta:
                aclaracion = "(Repregunta)"
            else:
                aclaracion = ''

            label = ''
            escritor.writerow([pregunta, bloque, paleta, texto, label, aclaracion])
    
    print(f"Archivo '{nombreArchivo}' guardado en '{rutaGuardado}'.")

