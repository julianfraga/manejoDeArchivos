from especiales.src.Portada import Portada
from especiales.TRACKING_PBA_F.apps.encuesta_TRACKING_PBA_F import encuesta
from especiales.TRACKING_PBA_F.apps.estructura_TRACKING_PBA_F import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


