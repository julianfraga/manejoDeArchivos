from especiales.src.Portada import Portada
from especiales.NEUQUEN_8.apps.encuesta_NEUQUEN_8 import encuesta
from especiales.NEUQUEN_8.apps.estructura_NEUQUEN_8 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


