import pandas as pd
import aux
from config import *
from especiales.TRACKING_AYSA_ENTRESEMANA.apps.encuesta_TRACKING_AYSA_ENTRESEMANA import encuesta
from especiales.TRACKING_AYSA_ENTRESEMANA.apps.paletas_TRACKING_AYSA_ENTRESEMANA import paletas
from especiales.TRACKING_AYSA_ENTRESEMANA.apps.files_TRACKING_AYSA_ENTRESEMANA import files_TRACKING_AYSA_ENTRESEMANA
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
    tiene_series = pregunta in encuesta.preguntas_con_series

    layout_preguntas[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='TRACKING_AYSA_ENTRESEMANA', textos=encuesta.get_textos,
                                           files=files_TRACKING_AYSA_ENTRESEMANA, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=encuesta.preguntas_ocultas,
                                           opciones=tiene_opciones, series=tiene_series
                                           )

if encuesta.preguntas_imagenes:
    encuesta.actualizar_bloque({'Imagen de dirigentes': ['imagen1', 'imagen2', 'imagen3']})
    encuesta.set_bloque_imagen('Imagen de dirigentes')

    # Graficos de preguntas de imagen indiviaules para cada candidato
    imagen = plots(files_TRACKING_AYSA_ENTRESEMANA['csv_imagen'][0],files_TRACKING_AYSA_ENTRESEMANA['csv_imagen'][3], files_TRACKING_AYSA_ENTRESEMANA["Alberto Fernandez"][0], callbackInputTarget= 'selectTargetTRACKING_AYSA_ENTRESEMANA',opcionesDePreguntasInicial = 4,
                                preguntasQueNoVan= encuesta.preguntas_ocultas, name='TRACKING_AYSA_ENTRESEMANA-Comparativo',crucesDict = cruces_dict, files=files_TRACKING_AYSA_ENTRESEMANA, codigo='TRACKING_AYSA_ENTRESEMANA')
    
    serie_conGalmarini = plot_candidates_ts(f"{encuesta.path}/data/serie_imagen_4opc.csv", 
                                            name = 'TRACKING_AYSA_ENTRESEMANA-Series',
                                            callback_target= 'selectTargetTRACKING_AYSA_ENTRESEMANA',
                                            callback_opciones='selectOpciones_TRACKING_AYSA_ENTRESEMANA',
                                            suf='conGalmarini')
    # Layouts imagenes

    #   imagen orden positiva
    layout_preguntas['imagen1'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_TRACKING_AYSA_ENTRESEMANA['csv_imagen'][0], 'selectTargetTRACKING_AYSA_ENTRESEMANA', 'selectOpciones_TRACKING_AYSA_ENTRESEMANA',
                                      opinionColorDict, 'TRACKING_AYSA_ENTRESEMANA-1D1A', opcionesDePreguntasInicial = 4), # Grafico comparado positiva
                    html.H3('Serie Temporal'),
                    serie_conGalmarini, #serie imagen
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen # Imagen
                    ])

    #   imagen orden negativa
    layout_preguntas['imagen2'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_TRACKING_AYSA_ENTRESEMANA['csv_imagen'][1], 'selectTargetTRACKING_AYSA_ENTRESEMANA', 'selectOpciones_TRACKING_AYSA_ENTRESEMANA',
                                      opinionColorDict, 'TRACKING_AYSA_ENTRESEMANA-1D1B', opcionesDePreguntasInicial = 4), # Grafico compardo Negativa
                    html.H3('Serie Temporal'),
                    serie_conGalmarini, #serie imagen
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])

    #   imagen orden ratio
    layout_preguntas['imagen3'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_TRACKING_AYSA_ENTRESEMANA['csv_imagen'][2], 'selectTargetTRACKING_AYSA_ENTRESEMANA', 'selectOpciones_TRACKING_AYSA_ENTRESEMANA',
                                      opinionColorDict, 'TRACKING_AYSA_ENTRESEMANA-1D1C', opcionesDePreguntasInicial = 4), # Grafico comparado Ratio
                    html.H3('Serie Temporal'),
                    serie_conGalmarini, #serie imagen
                    html.H3('Seleccione un dirigente o funcionario político'),
                    imagen])