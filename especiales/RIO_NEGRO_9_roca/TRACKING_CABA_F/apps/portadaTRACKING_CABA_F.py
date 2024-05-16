from especiales.src.Portada import Portada
from especiales.TRACKING_CABA_F.apps.encuesta_TRACKING_CABA_F import encuesta
from especiales.TRACKING_CABA_F.apps.estructura_TRACKING_CABA_F import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


