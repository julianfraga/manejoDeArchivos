#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:52:19 2023

@author: julian
"""
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
from PIL import ImageColor
import pandas as pd

# Obtener opciones únicas para OPCION1 y OPCION2
ruta = '/home/julian/trabajo/updates/corte 205/tigre/drive-download-20230806T210651Z-001/alluvial/tabla_INTENDENTE_CORTA_1_INTENDENTE_CORTA_2.csv'
# df = pd.read_csv(archivo)
paleta = {'Galmarini': colores["peronismo"],
                    'Zamora': colores["peronismo2"], 
                    'Cufré': colores["cambiemos"],
                    'Cernadas': colores["cambiemos2"],
                    'Baumgarten': colores["liberales"],
                    'Izquierda': colores["izquierda"], 
                    'Otros': colores["otros"], 
                    'No sabe': colores["nosabe"]}

titleDict = dict(size = 26, color='black', family='Arial, sans-serif')
def getColor(candidato: str, diccionario: dict):
    color = diccionario[candidato]
    return(color)

def procesarDFAlluvial(ruta:str, paleta: dict):
    
    ### Tratamiento del DF
    # Asumo que el dataframe tiene el siguiente formato: candidato - candidato - frecuencia
    df = pd.read_csv(archivo)
    df['color'] = ''
    columna_1, columna_2, frecuencia = list(df)[0:3]
    for index, row in df.iterrows():
        candidato = row[columna_1]
        #paso paletas a RGBA
        df.at[index, 'color'] =  ImageColor.getcolor(getColor(candidato, paletas), "RGBA")
    
    opciones1 = df[columna_1].unique()
    opciones2 = df[columna_2].unique()
    
    # Crear listas para los nodos y las fuentes de flujo
    nodos = opciones1.tolist() + opciones2.tolist()
    colores_nodos = [paletas[candidato] for candidato in nodos]

    fuentes = []

    # Crear una lista de tuplas (fuente, destino, valor) para representar los flujos
    for i, opcion1 in enumerate(opciones1):
        for j, opcion2 in enumerate(opciones2):
            valor = df[(df["OPCION1"] == opcion1) & (df["OPCION2"] == opcion2)]["Freq"].sum()
            RGBA = df[(df["OPCION1"] == opcion1) & (df["OPCION2"] == opcion2)]["color"].sum()
            if valor > 0:
                fuentes.append((i, len(opciones1) + j, valor, RGBA))

    x_pos_ = [0]*len(opciones1)+[1]*len(opciones2)
    y_pos_ = list(np.linspace(0,1, num = len(opciones1), endpoint = True))+list(np.linspace(0,1, num = len(opciones2), endpoint = True))
    x_pos = [.001 if v==0 else .999 if v==1 else v for v in x_pos_]
    y_pos = [.001 if v==0 else .999 if v==1 else v for v in y_pos_]
    
    posiciones = {'x_pos' : x_pos, 'y_pos' : y_pos}
    opciones = {'opciones1': opciones1, 'opciones2' : opciones2}
    
    salida = {
        'posiciones' : posiciones, 
        'opciones': opciones, 
        'fuentes': fuentes, 
        'nodos': nodos, 
        'colores_nodos':colores_nodos
                }
    
    return salida



def getDefaultLayout(xaxisTitle = 'HOLDER X',yaxisTitle = 'HOLDER Y'):
    layout = go.Layout(xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'showticklabels': False},
                        yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'showticklabels': False},
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        #gridcolor='grey',
                        #showgrid=True,
                        legend={'traceorder': 'reversed'},
                        title='Target: ',
                        titlefont=titleDict,
                        annotations=[{
                            'x': 35,
                            'y': -100,
                            'xref': 'x',
                            'text': '',
                            'yref': 'y',
                            'showarrow': False,
                            'ax': 0,
                            'ay': -100,
                            'font': dict(size=25),
                        }]
                    )
    return layout

def alluvialPlotComponent(ruta:str, paleta: dict):
    opacidad = 0.3
    atributos = procesarDFAlluvial(ruta, paleta)
    mynode = dict(
                thickness = 20,
                line = dict(color="black", width=0.5),
                label = atributos['nodos'],
                color = atributos['colores_nodos'],
                x = atributos['posiciones']['x_pos'],
                y = atributos['posiciones']['y_pos']
                )
    opacidad = 0.3
    mylinks = dict(
                source=[x[0] for x in atributos['fuentes']],
                target = [x[1] for x in atributos['fuentes']],
                value=[x[2] for x in atributos['fuentes']],
                color = [f'rgba{(*x[3][0:3],opacidad)}' for x in atributos['fuentes']]
                )
    
    # Crear el diagrama Alluvial
    default_layout = getDefaultLayout()
    fig = go.Figure(
        data = [go.Sankey(
        arrangement="snap",                                
        node= mynode,
        link=mylinks)],
        layout = default_layout
        )
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')

    return fig

def getAlluvialPlot(ruta : str, paleta : str, name, callbackInput, axisRange=None, xaxisTitle='', yaxisTitle='', showticklabels=True, reverse=True, yLegendPosition=-0.2):
    graph_id = 'enhanced-graph-' + name

    fig = alluvialPlotComponent(ruta, paleta)

    component = html.Div(
        dcc.Graph(id=graph_id, figure=fig)
        )
    return component
#%%
# plot(fig)
plot(plotAlluvial(ruta, paleta))
getAlluvialPlot(ruta, paleta, 'alluvial', 'callback')
