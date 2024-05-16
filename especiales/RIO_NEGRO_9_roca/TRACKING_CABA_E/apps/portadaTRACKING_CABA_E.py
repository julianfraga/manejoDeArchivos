from especiales.src.Portada import Portada
from especiales.TRACKING_CABA_E.apps.encuesta_TRACKING_CABA_E import encuesta
from especiales.TRACKING_CABA_E.apps.estructura_TRACKING_CABA_E import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


