from especiales.src.Portada import Portada
from especiales.MEDICOS_01.apps.encuesta_MEDICOS_01 import encuesta
from especiales.MEDICOS_01.apps.estructura_MEDICOS_01 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


