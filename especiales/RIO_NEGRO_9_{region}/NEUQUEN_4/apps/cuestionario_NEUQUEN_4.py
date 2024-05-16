import pandas as pd
import aux

path='./especiales/NEUQUEN_4/'

cuestionario = pd.read_table(path + 'apps/cuestionario.tsv')

preguntas_efectivas = aux.get_preguntas(path + "/data/")
preguntas_imagenes = ['P10', 'P11', 'P12']
preguntas_efectivas.extend(preguntas_imagenes)
preguntas_ocultas= ['P13']

cuestionario = cuestionario[cuestionario.codigo.isin(preguntas_efectivas) ]


cuestionario = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)]

bloques = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)].groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

preguntas_con_opciones = aux.get_numero_de_opciones(path + 'data/')

opciones = ['_4opc', '_6opc', '_4opc_imputadas', '_6opc_imputadas']

bloques.update({'Gestión e imágenes': ['imagen1', 'imagen2', 'imagen3'] })

