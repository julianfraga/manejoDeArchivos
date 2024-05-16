import pandas as pd
import aux

path='./especiales/POSICIONAMIENTO_ESPECIAL_NACIONAL_2/'

cuestionario = pd.read_table(path + 'apps/cuestionario.tsv')

preguntas_efectivas = aux.get_preguntas(path + "/data/")
preguntas_imagenes = cuestionario[cuestionario.paleta == "imagen"].codigo.tolist()
preguntas_efectivas.extend(preguntas_imagenes)

cuestionario = cuestionario[cuestionario.codigo.isin(preguntas_efectivas) ]
preguntas_ocultas = ['P12','P15','P21','P24', 'P29', 'P30', 'P31', 'P32', 'P38',
 'P39', 'P47', 'P48', 'P49', 'P50', 'P51', 'P52', 'P53','P54', 'P55', 'P56']
cuestionario = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)]

bloques = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)].groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

preguntas_con_opciones = aux.get_numero_de_opciones(path + 'data/')

opciones = ['_4opc', '_6opc']


