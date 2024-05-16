from especiales.src.Portada import Portada
from especiales.INSEGURIDAD_2.apps.encuesta_INSEGURIDAD_2 import encuesta
from especiales.INSEGURIDAD_2.apps.estructura_INSEGURIDAD_2 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


