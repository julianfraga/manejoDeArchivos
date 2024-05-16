from especiales.src.Portada import Portada
from especiales.TRACKING_PBA_ENTRESEMANA.apps.encuesta_TRACKING_PBA_ENTRESEMANA import encuesta
from especiales.TRACKING_PBA_ENTRESEMANA.apps.estructura_TRACKING_PBA_ENTRESEMANA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


