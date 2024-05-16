from especiales.src.Portada import Portada
from especiales.TRACKING_DIARIO_PBA.apps.encuesta_TRACKING_DIARIO_PBA import encuesta
from especiales.TRACKING_DIARIO_PBA.apps.estructura_TRACKING_DIARIO_PBA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


