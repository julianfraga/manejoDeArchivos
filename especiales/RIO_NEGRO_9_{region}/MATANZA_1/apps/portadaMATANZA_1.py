from especiales.src.Portada import Portada
from especiales.MATANZA_1.apps.encuesta_MATANZA_1 import encuesta
from especiales.MATANZA_1.apps.estructura_MATANZA_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


