from especiales.src.Portada import Portada
from especiales.TRACKING_NACIONAL_B.apps.encuesta_TRACKING_NACIONAL_B import encuesta
from especiales.TRACKING_NACIONAL_B.apps.estructura_TRACKING_NACIONAL_B import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


