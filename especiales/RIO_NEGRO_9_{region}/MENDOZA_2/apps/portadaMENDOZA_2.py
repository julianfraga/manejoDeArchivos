from especiales.src.Portada import Portada
from especiales.MENDOZA_2.apps.encuesta_MENDOZA_2 import encuesta
from especiales.MENDOZA_2.apps.estructura_MENDOZA_2 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


