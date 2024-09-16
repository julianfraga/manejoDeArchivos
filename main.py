from utils.docx_parser import get_preguntas, getOpciones, getBloque
from utils.inferencias import infer_paleta
from utils.paletas import list2dictPalette
from utils.file_utils import cuestionarioTSV
from utils.generarEspeciales import armarEncuesta
from depr.preguntas_opciones import printPaletas
import os
import pandas as pd
ruta_trabajo = "/home/julian/trabajo/updates/corte 262/entre rios/"

for archivo in os.listdir(ruta_trabajo):
    if archivo.endswith('.docx'):
        ruta_docx = ruta_trabajo+archivo
        break
# ruta_docx = "path/to/your/document.docx"
nombre_tsv = "cuestionario.tsv"

# cuestionario
cuestionarioTSV(ruta_docx, rutaGuardado=ruta_trabajo, nombreArchivo=nombre_tsv)
tabla = pd.read_table(ruta_trabajo+nombre_tsv)
print(tabla)

#armado de encuesta
armarEncuesta(nombreEncuesta = 'ENTRE_RIOS_1', nombrePlantilla='BASE_1')
#PALETAS
opciones_limpias = printPaletas(ruta_docx, nombre_tsv, ruta_trabajo, subcarpeta = 'web/individuales')
