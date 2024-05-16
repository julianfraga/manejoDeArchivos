import pandas as pd
import aux
from txt import textos as textos_base


class Encuesta():
    """
    Carga y procesamiento del cuestionario de la encuesta y de la ficha tenica.
    Para eso:
        - con pandas carga el cuestionario desde ./tablas/cuestionario.tsv
        - obtiene las preguntas que tienen opciones, las de imagenes, la que tienen efectivamente archivos csv
        - obtiene los bloques con sus respectivas preguntas asociadas
        - carga los textos desde el archivo ./tablas/textos.tsv, de textos_base (que viene de /txt.py)

    Tiene metodos para personalizar datos, actualizar y/o sobreescribir bloques (Importante para bloques de imagenes)
    Además tiene getters y setters para actualizar u obtener el cuestionario en dataframe, bloques, textos, opciones
    y targets.

    En caso de necesidad los atributos se pueden soobrescribir a mano.


    """

    def __init__(self, codigo:str, path: str, cuestionario: str, preguntas_ocultas:[str]):
        """
        Constructor de la clase Encuesta.
        :param codigo: Código de la encuesta.
        :param path: Ruta del directorio de la encuesta.
        :param cuestionario: Nombre del archivo de cuestionario.
        :param preguntas_ocultas: Lista de preguntas ocultas.
        """

        self.codigo = codigo
        self.preguntas_ocultas = preguntas_ocultas
        self.path = path
        self.cuestionario_file = cuestionario

        self.bloque_imagen = None
     
        if 'especiales' not in self.path:
            self.cargar_cuestionario_tracking()
        else:
            self.cargar_cuestionario()

        self.cargar_preguntas_imagenes()
        self.cargar_preguntas_opciones()
        self.cargar_preguntas_series()
        self.cargar_preguntas_efectivas()

        self.procesar_cuestionario()
        self.cargar_bloques()

        self.load_textos()

        

    def cargar_cuestionario(self):
        """
        Carga el cuestionario desde un archivo tsv.
        """
        self.cuestionario =  pd.read_table(f'{self.path}/tablas/{self.cuestionario_file}.tsv')

    def cargar_cuestionario_tracking(self):
                """
                Carga el cuestionario desde tracking.csv hardcodeado.
                """
                self.cuestionario =  pd.read_table('./tracking.tsv')

    def set_bloque_imagen(self, bloque_imagen):
        """
        Establece el bloque de imagen de la encuesta.
        :param bloque_imagen: Nombre del bloque de imagen.
        Importante para que en la portada se devuelva todas las preguntas de un bloque (si no es imagen) o solo la
        primera que es imagen orden positiva (si es bloque imagen)
        """
        self.bloque_imagen = bloque_imagen
    


    def cargar_preguntas_efectivas(self):
        """
        Carga las preguntas efectivas desde un archivo y las añade a las preguntas de imágenes.
        Estas preguntas son las que tienen archivo csv en ./data/
        """
        preguntas_efectivas = aux.get_preguntas(f'{self.path}/data/')
        preguntas_efectivas.extend(self.preguntas_imagenes)
        self.preguntas_efectivas = preguntas_efectivas

    def cargar_preguntas_imagenes(self):
        """
        Carga las preguntas de imagen desde el cuestionario.
        Las preguntas de imagen son aquellas que tienen la paleta "imagen".
        """
        self.preguntas_imagenes = self.cuestionario[self.cuestionario.paleta == "imagen"].codigo.tolist()

    def cargar_preguntas_opciones(self):
        """
        Carga las preguntas con opciones desde un archivo.
        """
        self.preguntas_con_opciones = aux.get_numero_de_opciones(f'{self.path}/data/')
    
    def cargar_preguntas_series(self):
        self.preguntas_con_series = aux.get_series(f'{self.path}/data/')

    def procesar_cuestionario(self):
        """
        Filtra y procesa el cuestionario basado en las preguntas efectivas y ocultas.
        """

        cuestionario = self.cuestionario

        preguntas_imagenes = self.preguntas_imagenes
        preguntas_efectivas = self.preguntas_efectivas
        preguntas_ocultas = self.preguntas_ocultas
        preguntas_efectivas.extend(preguntas_imagenes)
        cuestionario = cuestionario[cuestionario.codigo.isin(preguntas_efectivas)]
        cuestionario = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)]
        cuestionario.bloque = cuestionario.bloque.astype(str) # Por si se utilizan numeros en lugar de nombres
        self.cuestionario = cuestionario

    def cargar_bloques(self):
        """
        Carga los bloques de la encuesta basados en el cuestionario.
        """
        self.bloques = self.cuestionario[~self.cuestionario.codigo.isin(self.preguntas_ocultas)].groupby('bloque', sort=False).agg(list)[
            'codigo'].to_dict()

    def actualizar_bloque(self, nuevo_bloque):
        """
        Actualiza los bloques de la encuesta con nuevos valores y verifica si hay bloques no presentes en el cuestionario original.
        :param nuevo_bloque: Nuevo bloque de la encuesta.
        """
        self.bloques.update(nuevo_bloque)
        for key in nuevo_bloque.keys():
            if key not in self.bloques.keys():
                print(f"Bloque {key} no estaba presente en el cuestionario")
    @property
    def get_bloques(self):
        """
        Obtiene los bloques de la encuesta.
        return Dict con nombre de codigo como key y lista de preguntas como value
        """
        return self.bloques

    @property
    def get_cuestionario(self):
        """
        Obtiene el cuestionario de la encuesta.
        return pandas.DataFrame
        """
        return self.cuestionario

    def set_opciones_target(self, opciones_target):
        """
        Establece las opciones objetivo de la encuesta.
        :param opciones_target: Opciones objetivo.
        """
        self.opciones_target = opciones_target

    # def load_textos(self):
    #     """
    #     Carga los textos de la encuesta desde el archivo base y la tabla de textos y los asigna a las preguntas y etiquetas correspondientes.

    #     """
    #     textos = textos_base# {k:v for k,v in textos_base.items() if not (k.startswith('pregunta') | k.startswith('label') )}

    #     textos_desde_table = pd.read_table(f'{self.path}/tablas/textos.tsv').set_index('clave')['texto'].to_dict() 
    #     textos.update(textos_desde_table)
        
    #     for _, row in self.cuestionario.iterrows():

    #         aclaracion = row.fillna("").aclaracion

    #         sep = " "
    #         if aclaracion and not aclaracion.startswith('('):
    #             sep = ", "
    #         texto = f'{row.texto}{sep}{aclaracion}'.strip()
    #         label = f'{row.label}{sep}{aclaracion}'.strip()

    #         textos["pregunta" + row.codigo] = texto
    #         textos["label" + row.codigo] = label


    #     self.textos_dict = textos

    def load_textos(self):
        """
        Carga los textos de la encuesta desde el archivo base y la tabla de textos y los asigna a las preguntas y etiquetas correspondientes.
        """
        textos = textos_base.copy()  # Copia el diccionario base para no modificarlo directamente
        textos_desde_table = pd.read_table(f'{self.path}/tablas/textos.tsv').set_index('clave')['texto'].to_dict()
        textos.update(textos_desde_table)

        for _, row in self.cuestionario.iterrows():
            aclaracion = row.fillna("").aclaracion
            sep = " "
            if aclaracion and not aclaracion.startswith('('):
                sep = ", "
            texto = f'{row.texto}{sep}{aclaracion}'.strip()
            label = f'{row.label}{sep}{aclaracion}'.strip()
            textos["pregunta" + row.codigo] = texto
            textos["label" + row.codigo] = label

        self.textos_dict = textos


    @property
    def get_textos(self):
        """
        Obtiene los textos de la encuesta.
        return Dict con textos
        """
        return self.textos_dict
    @property
    def opciones(self):
        pass

    def set_opciones(self):
        pass




