from especiales.src.Portada import Portada
from especiales.HURLINGHAM_3.apps.encuesta_HURLINGHAM_3 import encuesta
from especiales.HURLINGHAM_3.apps.estructura_HURLINGHAM_3 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


