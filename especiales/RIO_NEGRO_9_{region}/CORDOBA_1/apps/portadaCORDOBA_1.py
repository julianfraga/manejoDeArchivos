from especiales.src.Portada import Portada
from especiales.CORDOBA_1.apps.encuesta_CORDOBA_1 import encuesta
from especiales.CORDOBA_1.apps.estructura_CORDOBA_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


