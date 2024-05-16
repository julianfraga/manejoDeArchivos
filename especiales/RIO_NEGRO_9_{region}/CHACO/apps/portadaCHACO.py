from especiales.src.Portada import Portada
from especiales.CHACO.apps.encuesta_CHACO import encuesta
from especiales.CHACO.apps.estructura_CHACO import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


