import pandas as pd
import aux

path='./especiales/POSICIONAMIENTO_PBA_12/'

cuestionario = pd.read_table(path + 'apps/cuestionario.tsv')

preguntas_efectivas = aux.get_preguntas(path + "/data/")
preguntas_imagenes = cuestionario[cuestionario.paleta == "imagen"].codigo.tolist()
preguntas_efectivas.extend(preguntas_imagenes)

cuestionario = cuestionario[cuestionario.codigo.isin(preguntas_efectivas) ]
preguntas_ocultas = ['P01', 'P02', 'P03', 'P04', 'P07', 'P09', 'P10', 'P11', 
                     'P12', 'P13', 'P14', 'P16', 'P17', 'P18', 'P19', 'P20', 
                     'P21', 'P22', 'P23', 'P27', 'P28', 'P29', 'P30', 'P38', 
                     'P39', 'P40', 'P41', 'P42', 'P43', 'P44', 'P52']

cuestionario = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)]

bloques = cuestionario[~cuestionario.codigo.isin(preguntas_ocultas)].groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

preguntas_con_opciones = aux.get_numero_de_opciones(path + 'data/')

opciones = ['_4opc', '_6opc']


