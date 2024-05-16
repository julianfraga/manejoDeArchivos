import pandas as pd
import aux

path='./especiales/POSICIONAMIENTO_NACIONAL_12/'

cuestionario = pd.read_table(path + 'apps/cuestionario.tsv')

preguntas_efectivas = aux.get_preguntas(path + "/data/")
preguntas_imagenes = cuestionario[cuestionario.paleta == "imagen"].codigo.tolist()
preguntas_efectivas.extend(preguntas_imagenes)

cuestionario = cuestionario[cuestionario.codigo.isin(preguntas_efectivas) ]
preguntas_ocultas = ['P01', 'P02', 'P03', 'P04', 'P07', 'P10', 'P11', 'P12', 
                     'P13', 'P14', 'P15', 'P16', 'P17', 'P19', 'P20', 'P21', 'P22', 
                     'P23', 'P24', 'P29', 'P30', 'P31', 'P32', 'P45', 'P46', 'P47', 
                     'P48', 'P49', 'P50', 'P51', 'P52']

cuestionario = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)]

bloques = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)].groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

preguntas_con_opciones = aux.get_numero_de_opciones(path + 'data/')

opciones = ['_4opc', '_6opc']


