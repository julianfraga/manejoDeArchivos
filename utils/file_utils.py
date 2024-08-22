import os
import csv
import pandas as pd

def limpiarKeys(diccionario):
    diccionarioLimpio = {}
    for key, value in diccionario.items():
        keyLimpia = key.replace('?', '')
        diccionarioLimpio[keyLimpia] = value
    return diccionarioLimpio

def cuestionarioTSV(ruta, rutaGuardado='.', nombreArchivo='cuestionario.tsv'):
    """
    Generate a TSV file containing the questionnaire data.
    Parameters:
    - ruta (str): The path to the input file.
    - rutaGuardado (str): The path to the directory where the output file will be saved. Default is the current directory.
    - nombreArchivo (str): The name of the output file. Default is 'cuestionario.tsv'.
    Returns:
    None
    Raises:
    None
    """
    preguntas = get_preguntas(ruta)
    opciones = getOpciones(ruta)
    bloques = getBloque(ruta)
    
    header = ['codigo', 'pregunta', 'bloque', 'paleta']
    rutaSalida = os.path.join(rutaGuardado, nombreArchivo)
    
    with open(rutaSalida, 'w', newline='') as archivo_tsv:
        escritor = csv.writer(archivo_tsv, delimiter='\t')
        escritor.writerow(header)
        
        for pregunta, pregunta_texto in preguntas.items():
            bloque = bloques.get(pregunta, '')
            paleta = 'qualitative' if len(opciones.get(pregunta, [])) <= 5 else 'diverging'
            escritor.writerow([pregunta, pregunta_texto, bloque, paleta])
    
    print(f"Archivo '{nombreArchivo}' guardado en '{rutaGuardado}'.")

def getOpcionesFromData(ruta):
    opciones = pd.read_csv(ruta, delimiter='\t')
    opciones_dict = {}
    for _, row in opciones.iterrows():
        opciones_dict[row['codigo']] = row['opciones']
    return opciones_dict

def printPaletas(file_name, cuestionario_name, rutaGuardado='.'):
    """
    Prints the lines from the file specified by `file_name` that start with any of the lines from the file specified by `cuestionario_name`.
    Parameters:
    - file_name (str): The name of the file to read the lines from.
    - cuestionario_name (str): The name of the file containing the lines to match against.
    - rutaGuardado (str, optional): The path where the files are located. Defaults to the current directory.
    Returns:
    None
    """
    with open(os.path.join(rutaGuardado, file_name), 'r') as file:
        paletas = file.readlines()
        
    with open(os.path.join(rutaGuardado, cuestionario_name), 'r') as file:
        data = file.readlines()
        
    for line in paletas:
        if any(line.startswith(pregunta) for pregunta in data):
            print(line)
