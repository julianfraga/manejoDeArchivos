from especiales.src.Portada import Portada
from especiales.TRACKING_ENTRESEMANA_4.apps.encuesta_TRACKING_ENTRESEMANA_4 import encuesta
from especiales.TRACKING_ENTRESEMANA_4.apps.estructura_TRACKING_ENTRESEMANA_4 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


