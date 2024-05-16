from especiales.src.Portada import Portada
from especiales.BASE_1.apps.encuesta_BASE_1 import encuesta
from especiales.BASE_1.apps.estructura_BASE_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


