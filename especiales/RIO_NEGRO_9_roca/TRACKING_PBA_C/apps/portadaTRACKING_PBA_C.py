from especiales.src.Portada import Portada
from especiales.TRACKING_PBA_C.apps.encuesta_TRACKING_PBA_C import encuesta
from especiales.TRACKING_PBA_C.apps.estructura_TRACKING_PBA_C import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


