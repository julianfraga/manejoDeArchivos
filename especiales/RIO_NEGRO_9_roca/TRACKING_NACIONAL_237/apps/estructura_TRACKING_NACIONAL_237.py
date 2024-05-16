import pandas as pd
import aux
from config import *
from especiales.TRACKING_NACIONAL_237.apps.encuesta_TRACKING_NACIONAL_237 import encuesta
from especiales.TRACKING_NACIONAL_237.apps.paletas_TRACKING_NACIONAL_237 import paletas
from especiales.TRACKING_NACIONAL_237.apps.files_TRACKING_NACIONAL_237 import files_TRACKING_NACIONAL_237
import dash_html_components as html
from txt import textos as textos_base

from graph_imagen import *
from especiales.src.plots import plots as especiales_plots
from bloques import tracking_bloques, orden_cruces

tracking_bloques['TRACKING_NACIONAL_237'] = encuesta.bloques      
orden_cruces['TRACKING_NACIONAL_237'] = [elemento for lista in encuesta.bloques.values() for elemento in lista]

# En cruces_dict se almacenan paletas y etiquetas de cada pregunta, cuando grafican los cruces para una pregunta,
# paleta y label de la pregunta con la que se quiere cruzar sale de cruces_dict
cruces_dict = {}
for pregunta, paleta in paletas.items():
    if pregunta not in encuesta.preguntas_ocultas:
        cruces_dict[pregunta] = [encuesta.get_textos['label' + pregunta], paleta]

## Estructura del layout

layout_preguntas = {}  # Aca va el layout de cada pregunta, que luego va a usar portada.py para mostrarlo segun correponda
# for _,row in encuesta.cuestionario[~encuesta.cuestionario.codigo.isin(encuesta.preguntas_imagenes)].iterrows(): # Si no quiero preguntas de imagenes
for _, row in encuesta.cuestionario.iterrows(): # Si quiero preguntas imaganes
    pregunta = row.codigo
    tiene_opciones = encuesta.preguntas_con_opciones.get(pregunta, True) #corregir, problema con las de imagen
    tiene_series = pregunta in encuesta.preguntas_con_series

    layout_preguntas[pregunta] = aux.get_pregunta_layout(pregunta, encuesta='TRACKING_NACIONAL_237', textos=encuesta.get_textos,
                                           files=files_TRACKING_NACIONAL_237, paletas=paletas, cruces_dict=cruces_dict, preguntas_ocultas=encuesta.preguntas_ocultas,
                                           opciones=tiene_opciones, series= tiene_series
                                           )

if encuesta.preguntas_imagenes:
    encuesta.actualizar_bloque({'Imagen Comparada de dirigentes': ['imagen1', 'imagen2', 'imagen3']})
    encuesta.set_bloque_imagen('Imagen Comparada de dirigentes')

    serie_sinGalmarini = None
    if 'serie_imagen_4opc.csv' in os.listdir(f"{encuesta.path}/data"):
        serie_sinGalmarini = plot_candidates_ts(f"{encuesta.path}/data/serie_imagen_4opc.csv", 
                                            name = 'TRACKING_NACIONAL_237-Series',
                                            callback_target= 'selectTargetTRACKING_NACIONAL_237',
                                            callback_opciones=f'selectOpciones_{encuesta.codigo}',
                                            select_opciones=f'selectOpciones_{encuesta.codigo}')
   

    # Graficos de preguntas de imagen indiviaules para cada candidato

    imagen_individual = plots(files_TRACKING_NACIONAL_237['csv_imagen'][0],files_TRACKING_NACIONAL_237['csv_imagen'][3], files_TRACKING_NACIONAL_237["Sergio Massa"][0], 
                              callbackInputTarget= 'selectTargetTRACKING_NACIONAL_237',crucesDict=cruces_dict, callbackOpciones = f'selectOpciones_{encuesta.codigo}',
                              preguntasQueNoVan= encuesta.preguntas_ocultas, name='TRACKING_NACIONAL_237-Comparativo',
                              files=files_TRACKING_NACIONAL_237,)
    
    #   imagen orden positiva
    layout_preguntas['imagen1'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_TRACKING_NACIONAL_237['csv_imagen'][0], 'selectTargetTRACKING_NACIONAL_237', f'selectOpciones_{encuesta.codigo}',
                                        opinionColorDict, 'TRACKING_NACIONAL_237-1D1A', opcionesDePreguntasInicial = 4), # Grafico comparado positiva
                                        ])
    #   imagen orden negativa
    layout_preguntas['imagen2'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_TRACKING_NACIONAL_237['csv_imagen'][1], 'selectTargetTRACKING_NACIONAL_237', f'selectOpciones_{encuesta.codigo}',
                                        opinionColorDict, 'TRACKING_NACIONAL_237-1D1B', opcionesDePreguntasInicial = 4), # Grafico compardo Negativa
                                        ])


    #   imagen orden ratio
    layout_preguntas['imagen3'] = html.Div([
                    html.H3(textos_base['pregunta_imagen'], className='subtituloBloque'),
                    html.H5(textos_base['seleccioneFigura']),
                    getStackedBarplot(files_TRACKING_NACIONAL_237['csv_imagen'][2], 'selectTargetTRACKING_NACIONAL_237', f'selectOpciones_{encuesta.codigo}',
                                        opinionColorDict, 'TRACKING_NACIONAL_237-1D1C', opcionesDePreguntasInicial = 4), # Grafico comparado Ratio
                                         ])
    
                                                    
    if serie_sinGalmarini:
        div_serie = html.Div([html.H3('Serie Temporal'),serie_sinGalmarini])
        layout_preguntas['imagen1'].children.append(div_serie) #serie imagen
        layout_preguntas['imagen2'].children.append(div_serie)
        layout_preguntas['imagen3'].children.append(div_serie)

    div_individual = html.Div([html.H3('Seleccione un dirigente o funcionario político'),imagen_individual])
    layout_preguntas['imagen1'].children.append(div_individual) #serie imagen
    layout_preguntas['imagen2'].children.append(div_individual)
    layout_preguntas['imagen3'].children.append(div_individual)   