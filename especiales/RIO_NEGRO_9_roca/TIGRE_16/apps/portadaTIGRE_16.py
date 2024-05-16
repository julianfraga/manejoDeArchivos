from especiales.src.Portada import Portada
from especiales.TIGRE_16.apps.encuesta_TIGRE_16 import encuesta
from especiales.TIGRE_16.apps.estructura_TIGRE_16 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


