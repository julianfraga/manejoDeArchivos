from especiales.src.Portada import Portada
from especiales.TRACKING_ENTRESEMANA_PROMEDIO.apps.encuesta_TRACKING_ENTRESEMANA_PROMEDIO import encuesta
from especiales.TRACKING_ENTRESEMANA_PROMEDIO.apps.estructura_TRACKING_ENTRESEMANA_PROMEDIO import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


