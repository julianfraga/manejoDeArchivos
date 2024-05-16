from especiales.src.Portada import Portada
from especiales.MISIONES_1.apps.encuesta_MISIONES_1 import encuesta
from especiales.MISIONES_1.apps.estructura_MISIONES_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


