from especiales.src.Portada import Portada
from especiales.TARIFAS.apps.encuesta_TARIFAS import encuesta
from especiales.TARIFAS.apps.estructura_TARIFAS import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


