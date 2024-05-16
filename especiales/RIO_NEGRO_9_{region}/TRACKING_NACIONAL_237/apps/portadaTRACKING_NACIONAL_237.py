from especiales.src.Portada import Portada
from especiales.TRACKING_NACIONAL_237.apps.encuesta_TRACKING_NACIONAL_237 import encuesta
from especiales.TRACKING_NACIONAL_237.apps.estructura_TRACKING_NACIONAL_237 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


