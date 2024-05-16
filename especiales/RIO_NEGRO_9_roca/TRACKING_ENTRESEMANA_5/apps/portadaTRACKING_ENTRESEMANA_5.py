from especiales.src.Portada import Portada
from especiales.TRACKING_ENTRESEMANA_5.apps.encuesta_TRACKING_ENTRESEMANA_5 import encuesta
from especiales.TRACKING_ENTRESEMANA_5.apps.estructura_TRACKING_ENTRESEMANA_5 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


