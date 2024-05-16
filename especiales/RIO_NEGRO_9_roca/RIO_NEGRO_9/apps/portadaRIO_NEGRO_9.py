from especiales.src.Portada import Portada
from especiales.RIO_NEGRO_9.apps.encuesta_RIO_NEGRO_9 import encuesta
from especiales.RIO_NEGRO_9.apps.estructura_RIO_NEGRO_9 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


