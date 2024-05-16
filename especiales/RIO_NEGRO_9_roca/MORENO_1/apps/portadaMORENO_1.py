from especiales.src.Portada import Portada
from especiales.MORENO_1.apps.encuesta_MORENO_1 import encuesta
from especiales.MORENO_1.apps.estructura_MORENO_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


