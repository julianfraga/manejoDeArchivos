from especiales.src.Portada import Portada
from especiales.MERLO_12.apps.encuesta_MERLO_12 import encuesta
from especiales.MERLO_12.apps.estructura_MERLO_12 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


