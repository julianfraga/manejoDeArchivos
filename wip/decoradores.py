#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:04:21 2024

@author: julian
"""


import pandas as pd
usuario = 'JulianF'
textos = {
    'trackingDiarioNacional': 'Tracking Nacional',
    'trackingDiarioPBA': 'Tracking PBA'
}
def especiales_check(encuesta):
    usuario = 'JulianF'

    especiales_permisos = (pd.read_csv('./especiales/permisos_especiales.csv', index_col='user')
                           .T
                           .fillna(0)
                           .astype(bool)
                           .to_dict('index')
                           )

    if usuario in especiales_permisos.keys():
        return especiales_permisos[usuario].get(encuesta, False)
    else:
        return False
titulos =['NEUQUEN_18',
           'CORRIENTES_3',
           'RIOCUARTO_3',
           'NEUQUEN_17',
           'RIO_NEGRO_10_prov',
            'RIO_NEGRO_10_bariloche',
           'RIO_NEGRO_10_cipoletti',
           'RIO_NEGRO_10_roca',
           'RIO_NEGRO_10_viedma',
           'RIOCUARTO_2',
           'NEUQUEN_16',
           'CORRIENTES_2',
           'NEUQUEN_15',
           'RIO_NEGRO_9',
           'RIO_NEGRO_9_roca',
           'RIO_NEGRO_9_bariloche',
           'RIO_NEGRO_9_viedma',
           'RIO_NEGRO_9_cipoletti',
           'NEUQUEN_14',
           'RIO_NEGRO_8',
           'RIO_NEGRO_8_bariloche',
           'RIO_NEGRO_8_cipoletti',
            'RIO_NEGRO_8_roca',
           'RIO_NEGRO_8_viedma',
           'TRACKING_NACIONAL_237',
           'CORRIENTES',
           'NEUQUEN_13',
           'RIO_NEGRO_7',
           'RIO_NEGRO_7_bariloche',
           'RIO_NEGRO_7_roca',
           'NEUQUEN_12',
           'RIOCUARTO',
           'LEY_OMNIBUS_2_convoto',
           'LEY_OMNIBUS_2',
           'NEUQUEN_11',
           'LEY_OMNIBUS',
           'MEDICOS_01',
           'NEUQUEN_10',
           'NEUQUEN_9',
           'APOYO_LULA',
           'GRUPOS_BLANCOYNULO',
            'GRUPOS_BLANCOPASO',
            'GRUPOS_BULLRICH',
            'GRUPOS_GRABOIS','GRUPOS_LARRETA','GRUPOS_SCHIARETTI',
           'TRACKING_NACIONAL_F',
           'TRACKING_PBA_F','TRACKING_CABA_F',
           'TRACKING_NACIONAL_E','TRACKING_PBA_E','TRACKING_CABA_E',
           'TARIFAS',
           'TRACKING_NACIONAL_D','TRACKING_PBA_D','TRACKING_CABA_D',
           'TIGRE_16',
           'TRACKING_NACIONAL_C','TRACKING_PBA_C','TRACKING_CABA_C',
           'TRACKING_NACIONAL_B','TRACKING_PBA_B','TRACKING_CABA_B',
           'TRACKING_NACIONAL_A','TRACKING_PBA_A','TRACKING_CABA_A',
            'BASE_1', # template para futuras encuestas
            #  'TRACKING_NACIONAL',# Prueba para ir pasando los trackings a la misma logica de las nuevas encuestas
                        ]
especiales_encuestas = titulos[:25]
especiales_check('TRACKING_NACIONAL_C')
encuestas_habilitadas = [e for e in especiales_encuestas if especiales_check(e)]

#%%
from especiales.especiales_config import especiales_labels
from dash import html, dcc
from functools import wraps


def habilitar_menu(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        menues_habilitados = args[0]
        texto = args[1]
        href = args[2]

        other_args = args[3:]  # Los otros argumentos posicionales
        other_kwargs = kwargs  # Los argumentos de palabras clave

        if func(*other_args, **other_kwargs):
            menues_habilitados.append(html.Div(
                children=[
                    dcc.Link(
                        texto,
                        href=href
                    )
                ]
            ))
    return wrapper

@habilitar_menu
def habilitar_tracking_nacional():
    return trackingNacionalHabilitado()

@habilitar_menu
def habilitar_tracking_pba():
    return trackingPBAHabilitado()

def trackingNacionalHabilitado():
    return True

def trackingPBAHabilitado():
    return True


@habilitar_menu
def habilitar_encuesta_especial(encuesta_titulo:str) ->bool:
    return especiales_check(encuesta_titulo)

menues_habilitados = []
tracking_habilitados = []
habilitar_tracking_nacional(tracking_habilitados, textos['trackingDiarioNacional'], "/trackingNacional/portada#top")
habilitar_tracking_pba(tracking_habilitados, textos['trackingDiarioPBA'], "/trackingPBA/portada")
if len(tracking_habilitados)>0:
    menues_habilitados.append(html.H1('encuestasContinuas'))
    menues_habilitados+=tracking_habilitados