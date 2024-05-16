from especiales.src.Portada import Portada
from especiales.NEUQUEN_7.apps.encuesta_NEUQUEN_7 import encuesta
from especiales.NEUQUEN_7.apps.estructura_NEUQUEN_7 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


