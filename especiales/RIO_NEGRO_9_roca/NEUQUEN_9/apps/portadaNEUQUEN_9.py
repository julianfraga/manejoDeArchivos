from especiales.src.Portada import Portada
from especiales.NEUQUEN_9.apps.encuesta_NEUQUEN_9 import encuesta
from especiales.NEUQUEN_9.apps.estructura_NEUQUEN_9 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


