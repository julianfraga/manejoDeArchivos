import pandas as pd
import aux
from config import *
from especiales.RIOCUARTO.apps.encuesta_RIOCUARTO import encuesta
from especiales.RIOCUARTO.apps.paletas_RIOCUARTO import paletas
from especiales.RIOCUARTO.apps.files_RIOCUARTO import files_RIOCUARTO
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

    layout_preguntas[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='RIOCUARTO', textos=encuesta.get_textos,
                                           files=files_RIOCUARTO, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=encuesta.preguntas_ocultas,
                                           opciones=tiene_opciones
                                           )

if encuesta.preguntas_imagenes:
    encuesta.actualizar_bloque({'Imagen de dirigentes': ['imagen1', 'imagen2', 'imagen3']})
    encuesta.set_bloque_imagen('Imagen de dirigentes')

    # Graficos de preguntas de imagen indiviaules para cada candidato
    imagen = plots(files_RIOCUARTO['csv_imagen'][0],files_RIOCUARTO['csv_imagen'][3], files_RIOCUARTO["Sergio Massa"][0], callbackInputTarget= 'selectTargetRIOCUARTO',opcionesDePreguntasInicial = 4,
                                preguntasQueNoVan= encuesta.preguntas_ocultas, name='RIOCUARTO-Comparativo',crucesDict = cruces_dict, files=files_RIOCUARTO, codigo='RIOCUARTO')

    # Layouts imagenes

    #   imagen orden positiva
    layout_preguntas['imagen1'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_RIOCUARTO['csv_imagen'][0], 'selectTargetRIOCUARTO', 'selectOpciones_RIOCUARTO',
                                      opinionColorDict, 'RIOCUARTO-1D1A', opcionesDePreguntasInicial = 4), # Grafico comparado positiva
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen # Imagen
                    ])

    #   imagen orden negativa
    layout_preguntas['imagen2'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_RIOCUARTO['csv_imagen'][1], 'selectTargetRIOCUARTO', 'selectOpciones_RIOCUARTO',
                                      opinionColorDict, 'RIOCUARTO-1D1B', opcionesDePreguntasInicial = 4), # Grafico compardo Negativa
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])

    #   imagen orden ratio
    layout_preguntas['imagen3'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_RIOCUARTO['csv_imagen'][2], 'selectTargetRIOCUARTO', 'selectOpciones_RIOCUARTO',
                                      opinionColorDict, 'RIOCUARTO-1D1C', opcionesDePreguntasInicial = 4), # Grafico comparado Ratio
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])