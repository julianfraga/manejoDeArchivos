from especiales.LEG_PBA_2.apps.txtLEG_PBA_2 import textosLEG_PBA_2
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.LEG_PBA_2.apps.txtLEG_PBA_2 import textosLEG_PBA_2
from config import *
from graphs import *
from graph_imagen import plots
from config import *
from especiales.LEG_PBA_2.apps.config import  cruces_dic_LEG_PBA_2
from especiales.LEG_PBA_2.apps.txtLEG_PBA_2 import textosLEG_PBA_2
import os
# Layout
from trackingLEGISLATIVAS.apps.plots import getTimeSeries2


# Un par de cosas que irian en un config, pero que son pocas como para crearlo
provincias = [filename for filename in os.listdir("./especiales/LEG_PBA_2/data/") if os.path.isdir("./especiales/LEG_PBA_2/data/" + filename)]
filesLEG_PBA_2 = {}

_listas = []
preguntas = {}
opciones = {}
layout = {}

politica = [
    '#1f78b4',
    "#619bc2",
    "#a6cee3",
    '#ffff5c',
    '#f5f59f',
    '#e31a1c',
    "#33a02c",
    '#b15928']


layouts = {}
preguntas_provincias = {}
for provincia in provincias:

    ruta = f"./especiales/LEG_PBA_2/data/{provincia}"
    layout = {}
    _preguntas_provincia = []
    for _pregunta in [i for i in ["pregunta_P11.csv"]]:#sorted(os.listdir(ruta + "/individuales")) if not i.startswith('.')]:


        if _pregunta != 'pregunta_P29__imputada.csv':
            n_preg = _pregunta.replace('pregunta_', '')[:-4]
            _preguntas_provincia.append(n_preg)

            layout[n_preg] = [

                html.Div([
                    html.H3(textosLEG_PBA_2['pregunta' + n_preg], className='subtituloBloque'),
                    dcc.Loading(getBarplotWithPalette("/".join([ruta, "individuales", _pregunta]), 'selectTargetLEG_PBA_2', cruces_dic_LEG_PBA_2[n_preg][-1],
                                                      'LEG_PBA_2-{}-1-{}'.format(n_preg, provincia),
                                                      showticklabels=False, reverse=False), color="#EC7030"),
                    html.H3(),
                    getTimeSeries2("/".join([ruta, "series", _pregunta]).replace('pregunta', 'serie'),
                                   cruces_dic_LEG_PBA_2[n_preg][-1],
                                   'LEG_PBA_2-serie-{}-{}-1'.format(n_preg, provincia),
                                   'selectTargetLEG_PBA_2', restar_dias = 6),

                    html.H3(textos['cruce'], className='subtituloBloque'),
                    getCrucesStacked("/".join([ruta, "cruces","cruce_" + _pregunta]), 'LEG_PBA_2-cruces-{}-1-{}'.format(n_preg, provincia),
                                     'selectTargetLEG_PBA_2',
                                     reorder=False, crucesDict = cruces_dic_LEG_PBA_2
                                     ),
                ])
            ]

    layouts[provincia] = layout
    preguntas_provincias[provincia] = _preguntas_provincia
