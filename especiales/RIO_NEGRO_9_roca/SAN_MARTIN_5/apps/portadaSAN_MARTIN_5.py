from especiales.src.Portada import Portada
from especiales.SAN_MARTIN_5.apps.encuesta_SAN_MARTIN_5 import encuesta
from especiales.SAN_MARTIN_5.apps.estructura_SAN_MARTIN_5 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


