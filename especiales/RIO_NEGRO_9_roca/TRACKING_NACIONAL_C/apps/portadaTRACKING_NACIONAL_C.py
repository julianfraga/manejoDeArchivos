from especiales.src.Portada import Portada
from especiales.TRACKING_NACIONAL_C.apps.encuesta_TRACKING_NACIONAL_C import encuesta
from especiales.TRACKING_NACIONAL_C.apps.estructura_TRACKING_NACIONAL_C import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


