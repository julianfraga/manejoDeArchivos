from especiales.src.Portada import Portada
from especiales.TRACKING_PBA_D.apps.encuesta_TRACKING_PBA_D import encuesta
from especiales.TRACKING_PBA_D.apps.estructura_TRACKING_PBA_D import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


