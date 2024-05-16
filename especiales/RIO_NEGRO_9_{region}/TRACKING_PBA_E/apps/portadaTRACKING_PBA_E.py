from especiales.src.Portada import Portada
from especiales.TRACKING_PBA_E.apps.encuesta_TRACKING_PBA_E import encuesta
from especiales.TRACKING_PBA_E.apps.estructura_TRACKING_PBA_E import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


