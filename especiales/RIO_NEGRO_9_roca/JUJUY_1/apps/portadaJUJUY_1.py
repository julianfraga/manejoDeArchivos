from especiales.src.Portada import Portada
from especiales.JUJUY_1.apps.encuesta_JUJUY_1 import encuesta
from especiales.JUJUY_1.apps.estructura_JUJUY_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


