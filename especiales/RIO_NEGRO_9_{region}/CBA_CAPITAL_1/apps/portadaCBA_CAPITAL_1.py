from especiales.src.Portada import Portada
from especiales.CBA_CAPITAL_1.apps.encuesta_CBA_CAPITAL_1 import encuesta
from especiales.CBA_CAPITAL_1.apps.estructura_CBA_CAPITAL_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


