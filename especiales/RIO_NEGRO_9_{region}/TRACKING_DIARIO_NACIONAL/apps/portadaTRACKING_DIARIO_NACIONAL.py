from especiales.src.Portada import Portada
from especiales.TRACKING_DIARIO_NACIONAL.apps.encuesta_TRACKING_DIARIO_NACIONAL import encuesta
from especiales.TRACKING_DIARIO_NACIONAL.apps.estructura_TRACKING_DIARIO_NACIONAL import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


