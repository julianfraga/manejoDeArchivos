from especiales.PASO_BA_4.apps.txtPASO_BA_4 import textosPASO_BA_4
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.PASO_BA_4.apps.txtPASO_BA_4 import textosPASO_BA_4
from config import *
from graphs import *
from graph_imagen import plots
from config import *
from especiales.PASO_BA_4.apps.config import  cruces_dic_PASO_BA_4
from especiales.PASO_BA_4.apps.txtPASO_BA_4 import textosPASO_BA_4
import os
# Layout
from especiales.PASO_BA_4.apps.plots import getTimeSeries2



# Un par de cosas que irian en un config, pero que son pocas como para crearlo
provincias = [filename for filename in os.listdir("./especiales/PASO_BA_4/data/") if os.path.isdir("./especiales/PASO_BA_4/data/" + filename)]
filesPASO_BA_4 = {}

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

    ruta = f"./especiales/PASO_BA_4/data/{provincia}"
    layout = {}
    _preguntas_provincia = []
    for _pregunta in [i for i in sorted(os.listdir(ruta + "/individuales")) if not i.startswith('.')]:


        if _pregunta != 'pregunta_P29__imputada.csv':
            n_preg = _pregunta.replace('pregunta_', '')[:-4]
            _preguntas_provincia.append(n_preg)

            layout[n_preg] = [

                html.Div([
                    html.H3(textosPASO_BA_4['pregunta' + n_preg], className='subtituloBloque'),
                    dcc.Loading(getBarplotWithPalette("/".join([ruta, "individuales", _pregunta]), 'selectTargetPASO_BA_4', cruces_dic_PASO_BA_4[n_preg][-1],
                                                      'PASO_BA_4-{}-1-{}'.format(n_preg, provincia),
                                                      showticklabels=False, reverse=False), color="#EC7030"),
                    #html.H3(),
                    #__add_serie(n_preg, _pregunta,provincia),

                    html.H3(textos['cruce'], className='subtituloBloque'),
                    getCrucesStacked("/".join([ruta, "cruces","cruce_" + _pregunta]), 'PASO_BA_4-cruces-{}-1-{}'.format(n_preg, provincia),
                                     'selectTargetPASO_BA_4',
                                     reorder=False, crucesDict = cruces_dic_PASO_BA_4
                                     ),
                ])
            ]

    layouts[provincia] = layout
    preguntas_provincias[provincia] = _preguntas_provincia
