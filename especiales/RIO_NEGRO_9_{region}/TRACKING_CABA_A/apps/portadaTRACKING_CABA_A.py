from especiales.src.Portada import Portada
from especiales.TRACKING_CABA_A.apps.encuesta_TRACKING_CABA_A import encuesta
from especiales.TRACKING_CABA_A.apps.estructura_TRACKING_CABA_A import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


