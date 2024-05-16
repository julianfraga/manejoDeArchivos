import pandas as pd
import aux

path='./especiales/POSICIONAMIENTO_CABA_13/'

cuestionario = pd.read_table(path + 'apps/cuestionario.tsv')

preguntas_efectivas = aux.get_preguntas(path + "/data/")
preguntas_imagenes = cuestionario[cuestionario.paleta == "imagen"].codigo.tolist()
preguntas_efectivas.extend(preguntas_imagenes)

cuestionario = cuestionario[cuestionario.codigo.isin(preguntas_efectivas) ]
preguntas_ocultas = ['P36']

cuestionario = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)]

bloques = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)].groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

preguntas_con_opciones = aux.get_numero_de_opciones(path + 'data/')

opciones = ['_4opc', '_6opc']

