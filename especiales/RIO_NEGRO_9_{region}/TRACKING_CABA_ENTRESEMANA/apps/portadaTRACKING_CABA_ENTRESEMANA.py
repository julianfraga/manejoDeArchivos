from especiales.src.Portada import Portada
from especiales.TRACKING_CABA_ENTRESEMANA.apps.encuesta_TRACKING_CABA_ENTRESEMANA import encuesta
from especiales.TRACKING_CABA_ENTRESEMANA.apps.estructura_TRACKING_CABA_ENTRESEMANA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


