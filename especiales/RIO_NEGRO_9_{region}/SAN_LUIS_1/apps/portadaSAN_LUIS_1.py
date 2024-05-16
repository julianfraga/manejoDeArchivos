from especiales.src.Portada import Portada
from especiales.SAN_LUIS_1.apps.encuesta_SAN_LUIS_1 import encuesta
from especiales.SAN_LUIS_1.apps.estructura_SAN_LUIS_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


