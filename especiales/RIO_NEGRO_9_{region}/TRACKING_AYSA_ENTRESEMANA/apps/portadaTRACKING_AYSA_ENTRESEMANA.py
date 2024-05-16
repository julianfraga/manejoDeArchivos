from especiales.src.Portada import Portada
from especiales.TRACKING_AYSA_ENTRESEMANA.apps.encuesta_TRACKING_AYSA_ENTRESEMANA import encuesta
from especiales.TRACKING_AYSA_ENTRESEMANA.apps.estructura_TRACKING_AYSA_ENTRESEMANA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


