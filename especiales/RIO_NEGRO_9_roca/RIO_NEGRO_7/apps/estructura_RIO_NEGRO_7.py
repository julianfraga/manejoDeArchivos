import pandas as pd
import aux
from config import *
from especiales.RIO_NEGRO_7.apps.encuesta_RIO_NEGRO_7 import encuesta
from especiales.RIO_NEGRO_7.apps.paletas_RIO_NEGRO_7 import paletas
from especiales.RIO_NEGRO_7.apps.files_RIO_NEGRO_7 import files_RIO_NEGRO_7
import dash_html_components as html
from txt import textos as textos_base
from graph_imagen import *
from especiales.src.plots import plots



# En cruces_dict se almacenan paletas y etiquetas de cada pregunta, cuando grafican los cruces para una pregunta,
# paleta y label de la pregunta con la que se quiere cruzar sale de cruces_dict
cruces_dict = {}
for pregunta, paleta in paletas.items():
    if pregunta not in encuesta.preguntas_ocultas:
        cruces_dict[pregunta] = [encuesta.get_textos['label' + pregunta], paleta]

## Estructura del layout

layout_preguntas = {}  # Aca va el layout de cada pregunta, que luego va a usar portada.py para mostrarlo segun correponda
for _,row in encuesta.cuestionario[~encuesta.cuestionario.codigo.isin(encuesta.preguntas_imagenes)].iterrows():

    pregunta = row.codigo
    tiene_opciones = encuesta.preguntas_con_opciones[pregunta]

    layout_preguntas[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='RIO_NEGRO_7', textos=encuesta.get_textos,
                                           files=files_RIO_NEGRO_7, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=encuesta.preguntas_ocultas,
                                           opciones=tiene_opciones
                                           )

if encuesta.preguntas_imagenes:
    encuesta.actualizar_bloque({'Imagen de dirigentes': ['imagen1', 'imagen2', 'imagen3']})
    encuesta.set_bloque_imagen('Imagen de dirigentes')

    # Graficos de preguntas de imagen indiviaules para cada candidato
    imagen = plots(files_RIO_NEGRO_7['csv_imagen'][0],files_RIO_NEGRO_7['csv_imagen'][3], files_RIO_NEGRO_7["Sergio Massa"][0], callbackInputTarget= 'selectTargetRIO_NEGRO_7',opcionesDePreguntasInicial = 4,
                                preguntasQueNoVan= encuesta.preguntas_ocultas, name='RIO_NEGRO_7-Comparativo',crucesDict = cruces_dict, files=files_RIO_NEGRO_7, codigo='RIO_NEGRO_7')

    # Layouts imagenes

    #   imagen orden positiva
    layout_preguntas['imagen1'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_RIO_NEGRO_7['csv_imagen'][0], 'selectTargetRIO_NEGRO_7', 'selectOpciones_RIO_NEGRO_7',
                                      opinionColorDict, 'RIO_NEGRO_7-1D1A', opcionesDePreguntasInicial = 4), # Grafico comparado positiva
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen # Imagen
                    ])

    #   imagen orden negativa
    layout_preguntas['imagen2'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_RIO_NEGRO_7['csv_imagen'][1], 'selectTargetRIO_NEGRO_7', 'selectOpciones_RIO_NEGRO_7',
                                      opinionColorDict, 'RIO_NEGRO_7-1D1B', opcionesDePreguntasInicial = 4), # Grafico compardo Negativa
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])

    #   imagen orden ratio
    layout_preguntas['imagen3'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_RIO_NEGRO_7['csv_imagen'][2], 'selectTargetRIO_NEGRO_7', 'selectOpciones_RIO_NEGRO_7',
                                      opinionColorDict, 'RIO_NEGRO_7-1D1C', opcionesDePreguntasInicial = 4), # Grafico comparado Ratio
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])