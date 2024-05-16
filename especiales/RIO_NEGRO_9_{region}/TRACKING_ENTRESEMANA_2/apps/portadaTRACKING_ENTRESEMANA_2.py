from especiales.src.Portada import Portada
from especiales.TRACKING_ENTRESEMANA_2.apps.encuesta_TRACKING_ENTRESEMANA_2 import encuesta
from especiales.TRACKING_ENTRESEMANA_2.apps.estructura_TRACKING_ENTRESEMANA_2 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


