from dash.dependencies import Input, Output
import plotly.graph_objs as go
from app import app
import pandas as pd
import numpy as np

from config import *


def getTimeSeries2(csv, palette, name, callbackInput, callbackOpciones='selectOpciones',
                          opcionesDePreguntasInicial=4,
                          xaxisTitle='', yaxisTitle='', yLegendPosition=-0.5, dias = 7):

    # Cree esta funcion temporal, es la misma que getTimeSeriesLineplot pero en vez de cargar al principio un
    # Graph vacio, carga los datos del dataframe de T1. (Para covid y aysa habria que hacerle un arreglo a las opciones)

    graph_id = 'enhanced-graph-' + name
    df = pd.read_csv(csv)
    df['fecha'] = pd.to_datetime(df['fecha'])

    filtered_df = df
    cols = [col.replace('t1 ', '').replace('s1 ', '').replace('s2 ', '').replace('e1 ', '').replace('e2 ', '').replace(
        'e3 ', '').replace('e4 ', '').replace('ed1 ', '').replace('ed2 ', '').replace('ed3 ', '').replace('dom1 ',
                                                                                                          '').replace(
        'dom2 ', '').replace('sa1 ', '').replace('sa2 ', '').replace('v1 ', '').replace('v2 ', '').replace('v3 ',
                                                                                                           '').replace(
        'zpba1 ', '').replace('zpba2 ', '').replace('z1', '').replace('z2', '').replace('z3', '').replace('z4', '') for
            col in df.columns.values.tolist()]
    cols = list(dict.fromkeys(cols))
    maxRange = max(df.select_dtypes(include=[np.number]).max() * 100 + 5)
    selected_cand = [i for i in cols if i != 'fecha']
    data = []
    if len(selected_cand) == 0:
        data.append(go.Scatter())

    shade_color = {7:'rgba(194, 186, 184, 0.5)', 0:'rgba(194, 186, 184, 0.05)'}

    columnas = df.columns[ df.columns.str.startswith('t1')]
    for i in columnas:

        trace = go.Scatter(x=filtered_df.fecha,
                           y=filtered_df[i].values * 100,
                           name=i,
                           line={'shape': 'spline', 'smoothing': lineSmooth},
                           marker=dict(color=palette[i.split(" ",1)[-1]])
                           )
        data.append(trace)

    component = html.Div([
        dcc.Graph(
            figure=go.Figure(data=data,
                             layout=dict(
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

                             ),
            style={'height': '90vmin'},
            id=graph_id,
        ),
        dcc.DatePickerRange(
            id='date-picker-range' + name,
            display_format='DD/MM/YYYY',
            min_date_allowed=df['fecha'].min(),
            max_date_allowed=df['fecha'].max(),
            start_date=df['fecha'].min(),
            end_date=df['fecha'].max(),
        )
    ])

    @app.callback(
        Output(graph_id, 'figure'),
        [Input('date-picker-range' + name, 'start_date'),
         Input('date-picker-range' + name, 'end_date'),
         # Input('checklist' + name, 'value'),
         Input(callbackInput, 'value'),
         #Input(callbackOpciones, 'value')
         ])
    def update_figure(start_date, end_date, selected_target):


        df = pd.read_csv(csv)
        df['fecha'] = pd.to_datetime(df['fecha'])
        cols = [
            col.replace('t1 ', '').replace('s1 ', '').replace('s2 ', '').replace('e1 ', '').replace('e2 ', '').replace(
                'e3 ', '').replace('e4 ', '').replace('ed1 ', '').replace('ed2 ', '').replace('ed3 ', '').replace(
                'dom1 ', '').replace('dom2 ', '').replace('sa1 ', '').replace('sa2 ', '').replace('v1 ', '').replace(
                'v2 ', '').replace('v3 ', '').replace('zpba1 ', '').replace('zpba2 ', '').replace('z1 ', '').replace(
                'z2 ', '').replace('z3 ', '').replace('z4 ', '') for col in df.columns.values.tolist()]
        cols = list(dict.fromkeys(cols))
        selected_cand = [i for i in cols if i != 'fecha']
        maxRange = max(df.select_dtypes(include=[np.number]).max() * 100 + 5)
        filtered_df = df.loc[(df.fecha >= start_date) & (df.fecha <= end_date)]
        data = []
        if len(selected_cand) == 0:
            data.append(go.Scatter())
        for i in selected_cand:
            trace = go.Scatter(x=filtered_df.fecha,
                               y=filtered_df[filtered_df.columns[1:]][
                                     traduccionSeries[selected_target] + ' ' + i].values * 100,
                               name=i,
                               line={'shape': 'spline', 'smoothing': lineSmooth},
                               marker=dict(color=palette[i])
                               )
            data.append(trace)

        return {
            'data': data,
            'layout': dict(
                yaxis={'fixedrange': True, 'autorange': False, 'range': [0, maxRange]},
                xaxis={'fixedrange': True, 'autorange': False,
                       'range': [filtered_df.fecha.min(), filtered_df.fecha.max()]},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                showlegend=True,
                gridcolor='grey',
                legend=dict(orientation="h", x=0, y=yLegendPosition),
                hovermode='closest',
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
        }
    return component