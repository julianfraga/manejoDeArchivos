import pandas as pd
import aux

path='./especiales/RIO_NEGRO_2/'

cuestionario = pd.read_table(path + 'apps/cuestionario.tsv')

preguntas_efectivas = aux.get_preguntas(path + "/data/")
preguntas_imagenes = cuestionario[cuestionario.paleta == "imagen"].codigo.tolist()
preguntas_efectivas.extend(preguntas_imagenes)
preguntas_ocultas = ['P06','P31']


cuestionario = cuestionario[cuestionario.codigo.isin(preguntas_efectivas) ]


cuestionario = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)]

bloques = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)].groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

preguntas_con_opciones = aux.get_numero_de_opciones(path + 'data/')

opciones = ['_4opc', '_6opc']


# bloques.update({'Imagen de dirigentes': ['imagen1', 'imagen2', 'imagen3'] })

