from especiales.src.Portada import Portada
from especiales.RIO_NEGRO_8_viedma.apps.encuesta_RIO_NEGRO_8_viedma import encuesta
from especiales.RIO_NEGRO_8_viedma.apps.estructura_RIO_NEGRO_8_viedma import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


