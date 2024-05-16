from especiales.src.Portada import Portada
from especiales.NEUQUEN_14.apps.encuesta_NEUQUEN_14 import encuesta
from especiales.NEUQUEN_14.apps.estructura_NEUQUEN_14 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


