from utils.docx_parser import get_preguntas, getOpciones, getBloque
from utils.inferencias import infer_paleta
from utils.paletas import list2dictPalette
from utils.file_utils import cuestionarioTSV, getOpcionesFromData, printPaletas

def main():
    ruta_docx = "path/to/your/document.docx"
    ruta_trabajo = "path/to/working/directory"
    nombre_tsv = "output.tsv"

    # Ejemplos de uso
    preguntas = get_preguntas(ruta_docx)
    opciones = getOpciones(ruta_docx)
    bloques = getBloque(ruta_docx)

    cuestionarioTSV(ruta_docx, rutaGuardado=ruta_trabajo, nombreArchivo=nombre_tsv)
    opciones_data = getOpcionesFromData(ruta_trabajo)
    printPaletas("questionnaire.txt", nombre_tsv, ruta_trabajo)

if __name__ == "__main__":
    main()