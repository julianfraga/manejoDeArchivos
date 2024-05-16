from especiales.src.Portada import Portada
from especiales.RIO_NEGRO_7_roca.apps.encuesta_RIO_NEGRO_7_roca import encuesta
from especiales.RIO_NEGRO_7_roca.apps.estructura_RIO_NEGRO_7_roca import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


