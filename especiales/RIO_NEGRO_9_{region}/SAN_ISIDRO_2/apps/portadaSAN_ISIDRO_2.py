from especiales.src.Portada import Portada
from especiales.SAN_ISIDRO_2.apps.encuesta_SAN_ISIDRO_2 import encuesta
from especiales.SAN_ISIDRO_2.apps.estructura_SAN_ISIDRO_2 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


