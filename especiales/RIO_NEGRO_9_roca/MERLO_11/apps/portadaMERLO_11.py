from especiales.src.Portada import Portada
from especiales.MERLO_11.apps.encuesta_MERLO_11 import encuesta
from especiales.MERLO_11.apps.estructura_MERLO_11 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


