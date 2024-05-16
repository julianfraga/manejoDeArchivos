import pandas as pd
import aux
from config import *
from especiales.MENDOZA_2.apps.encuesta_MENDOZA_2 import encuesta
from especiales.MENDOZA_2.apps.paletas_MENDOZA_2 import paletas
from especiales.MENDOZA_2.apps.files_MENDOZA_2 import files_MENDOZA_2
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

    layout_preguntas[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='MENDOZA_2', textos=encuesta.get_textos,
                                           files=files_MENDOZA_2, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=encuesta.preguntas_ocultas,
                                           opciones=tiene_opciones
                                           )

if encuesta.preguntas_imagenes:
    encuesta.actualizar_bloque({'Gestión e imágenes': ['imagen1', 'imagen2', 'imagen3']})
    encuesta.set_bloque_imagen('Gestión e imágenes')

    # Graficos de preguntas de imagen indiviaules para cada candidato
    imagen = plots(files_MENDOZA_2['csv_imagen'][0],files_MENDOZA_2['csv_imagen'][3], files_MENDOZA_2["Sergio Massa"][0], callbackInputTarget= 'selectTargetMENDOZA_2',opcionesDePreguntasInicial = 4,
                                preguntasQueNoVan= encuesta.preguntas_ocultas, name='MENDOZA_2-Comparativo',crucesDict = cruces_dict, files=files_MENDOZA_2, codigo='MENDOZA_2')

    # Layouts imagenes

    #   imagen orden positiva
    layout_preguntas['imagen1'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_MENDOZA_2['csv_imagen'][0], 'selectTargetMENDOZA_2', 'selectOpciones_MENDOZA_2',
                                      opinionColorDict, 'MENDOZA_2-1D1A', opcionesDePreguntasInicial = 4), # Grafico comparado positiva
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen # Imagen
                    ])

    #   imagen orden negativa
    layout_preguntas['imagen2'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_MENDOZA_2['csv_imagen'][1], 'selectTargetMENDOZA_2', 'selectOpciones_MENDOZA_2',
                                      opinionColorDict, 'MENDOZA_2-1D1B', opcionesDePreguntasInicial = 4), # Grafico compardo Negativa
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])

    #   imagen orden ratio
    layout_preguntas['imagen3'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_MENDOZA_2['csv_imagen'][2], 'selectTargetMENDOZA_2', 'selectOpciones_MENDOZA_2',
                                      opinionColorDict, 'MENDOZA_2-1D1C', opcionesDePreguntasInicial = 4), # Grafico comparado Ratio
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])