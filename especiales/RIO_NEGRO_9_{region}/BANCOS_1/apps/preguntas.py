import pandas as pd
from config import list2dictPalette, qualitative_strong
preguntas_df = pd.read_csv('especiales/BANCOS_1/apps/preguntas.tsv', sep='\t')

dic = {}

for i, row in preguntas_df.iterrows():
    dic["pregunta" + row.codigo] = row.texto
    dic["label" + row.codigo] = row.label


# layout = {}
#
# encuesta = "BANCOS_1"
#
# for i, row in preguntas_df.iterrows():
#     pregunta = row.codigo
#     layout[pregunta] = html.Div([
#              html.H3(textosBANCOS_1['pregunta' + pregunta], className='subtituloBloque'),
#
#              getBarplotWithPalette(filesBANCOS_1['csv' + pregunta][0], f'selectTarget{encuesta}', paletas[pregunta], f'{encuesta}-{pregunta}-1', showticklabels=False, reverse=False),
#
#              html.H3(textosBANCOS_1['cruce'], className='subtituloBloque'),
#              getCrucesStacked(filesBANCOS_1['csv' + pregunta][2], f'{encuesta}-{pregunta}-3', f'selectTarget{encuesta}', '', preguntasQueNoVan = preguntasQueNoVanBANCOS_1, reorder= False, crucesDict = crucesDictBANCOS_1)
#     ])

paleta_df = pd.read_csv('especiales/BANCOS_1/apps/paleta.tsv', sep='\t')

paletas = {}

paletas_2 = {}

for pregunta, row in paleta_df.groupby('codigo'):
    #paletas[pregunta] = list2dictPalette( row.texto.to_list(), qualitative_strong)
    paletas_2[pregunta] = f"list2dictPalette({ row.texto.to_list()}, diverging)"