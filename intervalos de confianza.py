# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from app import app
import pandas as pd
import numpy as np
import textwrap
from txt import *
from config import *
import seaborn as sns
import os.path
from plotly.offline import plot

from especiales.src.Encuesta import Encuesta

##  Generar encuesta y cuestionario
path='./especiales/TRACKING_NACIONAL/'
encuesta = Encuesta('TRACKING_NACIONAL', './especiales/TRACKING_NACIONAL','cuestionario', [])

if encuesta.preguntas_imagenes:
        encuesta.actualizar_bloque({'Imagen Comparada de dirigentes': ['imagen1', 'imagen2', 'imagen3']})
        encuesta.set_bloque_imagen('Imagen Comparada de dirigentes')

encuesta.cargar_cuestionario()
cuestionario = encuesta.cuestionario

##  CONFIG
opciones = ['_4opc', '_6opc']  # Opciones para preguntas con opciones, tiene que coincidir con los csvs

#   Los Values tienen que coincidir con las columnas de los csv (targets)
opciones_target = [
        {'label': 'Todos', 'value': 'Todos'},
        {'label': 'Hombres', 'value': 'Hombres'},
        {'label': 'Mujeres', 'value': 'Mujeres'},
        {'label': '16-29 años', 'value': '16-29 años'},
        {'label': '30-49 años', 'value': '30-49 años'},
        {'label': '50-64 años', 'value': '50-64 años'},
        {'label': '65+ años', 'value': '65+ años'},
        {'label': 'Hasta primario completo', 'value': 'Hasta primario completo'},
        {'label': 'Secundario completo/incompleto', 'value': 'Secundario completo/incompleto'},
        {'label': 'Terciario completo/incompleto', 'value': 'Terciario completo/incompleto'},
        {'label': 'Voto octubre 2019: A. Fernandez', 'value': 'Fernandez'},
        {'label': 'Voto octubre 2019: M. Macri', 'value': 'Macri'},
        {'label': 'Voto octubre 2019: R. Lavagna', 'value': 'Lavagna'},
        {'label': 'Región: Central Transversal', 'value': 'Centro'},
        {'label': 'Región: Norte Grande', 'value': 'Norte'},
        {'label': 'Región: Patagonia', 'value': 'Sur'},
        {'label': 'Región: Buenos Aires', 'value': 'Buenos Aires'},
                                     ]

n_opciones_target = len(opciones_target) # Cambiar de ser neceario, habria que deprecarlo

encuesta.set_opciones_target(opciones_target)

files_TRACKING_NACIONAL = {}
data_folder = path + "data/"

# Para cada pregunta que no es imagen se agrega en el diccionario los 3 csvs (individual, serie, pregunta)
for pregunta in cuestionario.query('bloque != "imagen"').codigo:
    files_TRACKING_NACIONAL["csv" + pregunta] = [('{}pregunta_' + pregunta + '.csv').format(data_folder),
                                      ('{}serie_' + pregunta + '.csv').format(data_folder),
                                      ('{}cruce_pregunta_' + pregunta + '.csv').format(data_folder)]



#%%
from especiales.TRACKING_NACIONAL.apps.paletas_TRACKING_NACIONAL import paletas

titleDict = dict(size = 26, color='black', family='Arial, sans-serif')

def insertString (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

#%%
p = 'P19'
csv = files_TRACKING_NACIONAL['csv'+p][1]

palette =  paletas[p]
name =  f'{encuesta.codigo}-{p}-2'

callbackInput,callbackOpciones = f'selectTarget{encuesta.codigo}', 'selectOpciones'
opcionesDePreguntasInicial=4
xaxisTitle=''
yaxisTitle=''
yLegendPosition=-0.5
dias = 0

graph_id = 'enhanced-graph-' + name
if not opcionesDePreguntasInicial is None:
    df = pd.read_csv(csv)
else:
    df = pd.read_csv(csv, index_col='clase')
    
df['fecha'] = pd.to_datetime(df['fecha'])
seleted_opciones = '_4opc'
selected_target = 'Todos'
filtered_df = df
cols = [col.replace('t1 ', '').lstrip('ls ').lstrip('li ') for  col in df.columns.values.tolist()]
cols = list(dict.fromkeys(cols))
maxRange = max(df.select_dtypes(include=[np.number]).max() * 100 + 5)
selected_cand = [i for i in cols if i != 'fecha']
data = []
if len(selected_cand) == 0:
    data.append(go.Scatter())

# shade_color = {7:'rgba(194, 186, 184, 0.5)', 0:'rgba(194, 186, 184, 0.05)'}

# columnas = df.columns[ df.columns.str.startswith('t1')]

# Lista vacía en donde se almacenan los traces

layout = go.Layout(
                yaxis={'fixedrange': True, 'autorange': False, 'range': [0, maxRange]},
                xaxis={'fixedrange': True, 'autorange': False,
                    'range': [filtered_df.fecha.min(), filtered_df.fecha.max()]},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                showlegend=True,
                legend=dict(orientation="h", x=0, y=yLegendPosition),
                hovermode='closest',
                template='plotly_white',
                transition={'duration': 500},
                shapes=[{'type': 'line',
                        'x0': pd.to_datetime('2019-12-10 00:00:00'),
                        'x1': pd.to_datetime('2019-12-10 00:00:00'),
                        'y0': 0,
                        'y1': maxRange,
                        'line': dict(color="RoyalBlue", width=2)},
                        {'type': "rect",
                        'x0': df.fecha.max() - np.timedelta64(7, 'D'),  # pd.to_datetime('2019-12-15 00:00:00'),
                        'y0': 0,
                        'x1': df.fecha.max(),
                        'y1': maxRange,
                        'fillcolor': shade_color[dias],
                        'line': {'color': '#b3abaa'}
                        }
                        ],
                annotations=[{
                    'x': pd.to_datetime('2019-12-10 00:00:00'),
                    'y': maxRange - 5,
                    'xref': 'x',
                    'yref': 'y',
                    'text': 'Asunción de<br>Alberto<br>Fernández',
                    'showarrow': True,
                    'ax': 80,
                    'ay': 0
                },
                    {
                        'x': df.fecha.max() - np.timedelta64(7, 'D'),
                        'y': maxRange - 5,
                        'xref': 'x',
                        'yref': 'y',
                        'text': 'Último<br>Corte',
                        'showarrow': True,
                        'ax': -40,
                        'ay': 0
                    }
                ]
            )
graph_id = 'enhanced-graph-' + name
fig = go.Figure(layout=layout)
data = []
for index, candidato in enumerate(cols[1:]):
    
    x_values=filtered_df.fecha
    y_values=filtered_df['t1 '+candidato].values * 100
    trace = go.Scatter(x=x_values,
                       y=y_values,
                       name= candidato,
                       line={'shape': 'spline', 'smoothing': lineSmooth},
                       marker=dict(color=palette[candidato])
                       )
    data.append(trace)
    
    # y_values = data[index]['y']
    upper_values = filtered_df[f"ls {candidato}"].values * 100
    lower_values = filtered_df[f"li {candidato}"].values * 100
    
    fig.add_trace(go.Scatter(data[index],legendgroup = candidato))
    
    
    # Agregar las barras de error al objeto Scatter correspondiente
    x_error = x_values.tolist()+x_values.tolist()[::-1] # x, then x reversed
    y_error = upper_values.tolist()+lower_values.tolist()[::-1]# upper, then lower reversed
    fig.add_trace(go.Scatter(
        x=x_error,
        y=y_error, 
        fill='toself',
        fillcolor='rgba(20,20,80,0.05)',
        line={'dash': 'dot', 'smoothing': lineSmooth},
        hoverinfo="skip",
        marker = {'color':palette[candidato]},
        name = 'Intervalo de confianza',
        showlegend=False,
        legendgroup = candidato
        )
    )
# lineSmooth = 1.3


num_candidatos = len(cols)-1 # El número de candidatos en el DataFrame (cols incluye fecha)

# for index, opcion in enumerate(cols[1:]):
#     y_values = data[index]['y']
#     upper_values = filtered_df[f"ls {opcion}"].values * 100
#     lower_values = filtered_df[f"li {opcion}"].values * 100
    
#     fig.add_trace(go.Scatter(data[index],legendgroup = opcion))
#     # Agregar las barras de error al objeto Scatter correspondiente
    
#     x_error = data[index]['x'].tolist()+data[index]['x'].tolist()[::-1] # x, then x reversed
#     y_error = upper_values.tolist()+lower_values.tolist()[::-1]# upper, then lower reversed
#     fig.add_trace(go.Scatter(
#         x=x_error,
#         y=y_error, 
#         fill='toself',
#         fillcolor='rgba(20,20,80,0.05)',
#         line={'dash': 'dot', 'smoothing': lineSmooth},
#         hoverinfo="skip",
#         marker = {'color':palette[opcion]},
#         name = 'Intervalo de confianza',
#         showlegend=False,
#         legendgroup = opcion
#         )
#     )

# Mostrar el gráfico interactivo
plot(fig)
#%%
# =============================================================================
# 
# =============================================================================
data = []
for index, i in enumerate(columnas):

    trace = go.Scatter(x=filtered_df.fecha,
                       y=filtered_df[i].values * 100,
                       name=i,
                       line={'shape': 'spline', 'smoothing': lineSmooth},
                       marker=dict(color=palette[i.split(" ",1)[-1]])
                       )
    data.append(trace)
    
    # Extraer el nombre del candidato/fórmula/opción del título
    
    # candidato = i.replace('t1 ', '')
    candidato = cols[index+1]
    # Agregar el intervalo de confianza como área sombreada para el candidato actual
    trace_upper = go.Scatter(
        x=filtered_df.fecha,
        y=(filtered_df[i].values + filtered_df[f"ls {candidato}"].values) * 100,
        name=f"ls {candidato}",
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0),
        hoverinfo='skip'
    )

    trace_lower = go.Scatter(
        x=filtered_df.fecha,
        y=(filtered_df[i].values - filtered_df[f"li {candidato}"].values) * 100,
        name=f"li {candidato}",
        fill='tonexty',
        mode='lines',
        line=dict(width=0),
        marker=dict(color='rgba(0,0,0,0)'),  # Color transparente
        hoverinfo='skip'
)

    data.append(trace_upper)
    data.append(trace_lower)
#%%
from plotly.subplots import make_subplots

lineSmooth = 1.3

num_candidatos = len(cols) - 1  # El número de candidatos en el DataFrame (cols incluye fecha)

fig = make_subplots(rows=num_candidatos, cols=1, shared_xaxes=True, vertical_spacing=0.02)

for index, opcion in enumerate(cols[1:]):
    y_values = data[index]['y']
    upper_values = filtered_df[f"ls {opcion}"].values * 100
    lower_values = filtered_df[f"li {opcion}"].values * 100

    # Agregar las barras de error al objeto Scatter correspondiente
    fig.add_trace(go.Scatter(
        x=data[index]['x'].tolist()+data[index]['x'].tolist()[::-1],  # x, then x reversed
        y=upper_values.tolist()+lower_values.tolist()[::-1],  # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(20,20,80,0.05)',
        line={'dash': 'dot', 'smoothing': lineSmooth},
        hoverinfo="skip",
        marker={'color': palette[opcion]},
        showlegend=False,
    ), row=index+1, col=1)

    # Agregar el spline correspondiente
    fig.add_trace(go.Scatter(
        x=data[index]['x'],
        y=y_values * 100,
        name=opcion,
        line={'shape': 'spline', 'smoothing': lineSmooth},
        marker=dict(color=palette[opcion]),
        error_y=dict(
            type='data',  # Tipo de error basado en datos
            array=upper_values,
            arrayminus=lower_values,
            visible=True,
        ),
        showlegend=False,
    ), row=index+1, col=1)

    # Ocultar la banda de error y el spline al iniciar el gráfico
    fig.data[2*index+1].visible = 'legendonly'
    fig.data[2*index+2].visible = 'legendonly'

# Actualizar el layout para agregar el título y ajustar los márgenes
fig.update_layout(
    title='Gráfico de series temporales con intervalo de confianza',
    xaxis=dict(title='Fecha'),
    yaxis=dict(title='Valor (%)'),
    height=800,
    width=1000,
    showlegend=True,
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
)

# Mostrar el gráfico interactivo
plot(fig)