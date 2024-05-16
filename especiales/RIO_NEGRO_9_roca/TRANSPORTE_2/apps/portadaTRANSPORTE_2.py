from especiales.src.Portada import Portada
from especiales.TRANSPORTE_2.apps.encuesta_TRANSPORTE_2 import encuesta
from especiales.TRANSPORTE_2.apps.estructura_TRANSPORTE_2 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


