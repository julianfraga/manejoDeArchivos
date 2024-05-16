from especiales.src.Portada import Portada
from especiales.TIGRE_15.apps.encuesta_TIGRE_15 import encuesta
from especiales.TIGRE_15.apps.estructura_TIGRE_15 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


