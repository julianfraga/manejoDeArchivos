from especiales.src.Portada import Portada
from especiales.NEUQUEN_11.apps.encuesta_NEUQUEN_11 import encuesta
from especiales.NEUQUEN_11.apps.estructura_NEUQUEN_11 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


