import pandas as pd
import aux

path='./especiales/ALQUILERES_NACIONAL_1/'

cuestionario = pd.read_table(path + 'apps/cuestionario.tsv')

bloques = cuestionario.groupby('bloque', sort=False).agg(list)['codigo'].to_dict()

preguntas_imagenes = cuestionario[cuestionario.paleta == "imagen"].codigo.tolist()

preguntas_con_opciones = aux.get_numero_de_opciones(path + 'data/')

opciones = ['_4opc', '_6opc']



#bloques.update({'Imagen': ['imagen1', 'imagen2', 'imagen3'] })



