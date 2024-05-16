from especiales.src.Portada import Portada
from especiales.TRACKING_PBA_A.apps.encuesta_TRACKING_PBA_A import encuesta
from especiales.TRACKING_PBA_A.apps.estructura_TRACKING_PBA_A import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


