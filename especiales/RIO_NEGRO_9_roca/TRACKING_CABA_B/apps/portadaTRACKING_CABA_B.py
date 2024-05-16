from especiales.src.Portada import Portada
from especiales.TRACKING_CABA_B.apps.encuesta_TRACKING_CABA_B import encuesta
from especiales.TRACKING_CABA_B.apps.estructura_TRACKING_CABA_B import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


