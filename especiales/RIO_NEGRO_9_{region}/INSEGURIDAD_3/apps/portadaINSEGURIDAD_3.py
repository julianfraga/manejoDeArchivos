from especiales.src.Portada import Portada
from especiales.INSEGURIDAD_3.apps.encuesta_INSEGURIDAD_3 import encuesta
from especiales.INSEGURIDAD_3.apps.estructura_INSEGURIDAD_3 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


