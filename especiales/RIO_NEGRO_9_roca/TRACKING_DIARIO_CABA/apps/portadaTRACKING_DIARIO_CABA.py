from especiales.src.Portada import Portada
from especiales.TRACKING_DIARIO_CABA.apps.encuesta_TRACKING_DIARIO_CABA import encuesta
from especiales.TRACKING_DIARIO_CABA.apps.estructura_TRACKING_DIARIO_CABA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


