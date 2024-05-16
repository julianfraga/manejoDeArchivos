from especiales.src.Portada import Portada
from especiales.NEUQUEN_10.apps.encuesta_NEUQUEN_10 import encuesta
from especiales.NEUQUEN_10.apps.estructura_NEUQUEN_10 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


