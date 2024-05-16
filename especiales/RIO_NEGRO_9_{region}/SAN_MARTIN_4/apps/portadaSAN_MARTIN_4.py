from especiales.src.Portada import Portada
from especiales.SAN_MARTIN_4.apps.encuesta_SAN_MARTIN_4 import encuesta
from especiales.SAN_MARTIN_4.apps.estructura_SAN_MARTIN_4 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


