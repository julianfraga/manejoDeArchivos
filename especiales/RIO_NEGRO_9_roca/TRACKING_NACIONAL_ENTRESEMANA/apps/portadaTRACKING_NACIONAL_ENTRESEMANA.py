from especiales.src.Portada import Portada
from especiales.TRACKING_NACIONAL_ENTRESEMANA.apps.encuesta_TRACKING_NACIONAL_ENTRESEMANA import encuesta
from especiales.TRACKING_NACIONAL_ENTRESEMANA.apps.estructura_TRACKING_NACIONAL_ENTRESEMANA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


