from especiales.src.Portada import Portada
from especiales.TRACKING_ENTRESEMANA_1.apps.encuesta_TRACKING_ENTRESEMANA_1 import encuesta
from especiales.TRACKING_ENTRESEMANA_1.apps.estructura_TRACKING_ENTRESEMANA_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


