from especiales.src.Portada import Portada
from especiales.NEUQUEN_12.apps.encuesta_NEUQUEN_12 import encuesta
from especiales.NEUQUEN_12.apps.estructura_NEUQUEN_12 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


