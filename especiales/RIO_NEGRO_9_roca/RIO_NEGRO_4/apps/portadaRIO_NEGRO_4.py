from especiales.src.Portada import Portada
from especiales.RIO_NEGRO_4.apps.encuesta_RIO_NEGRO_4 import encuesta
from especiales.RIO_NEGRO_4.apps.estructura_RIO_NEGRO_4 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


