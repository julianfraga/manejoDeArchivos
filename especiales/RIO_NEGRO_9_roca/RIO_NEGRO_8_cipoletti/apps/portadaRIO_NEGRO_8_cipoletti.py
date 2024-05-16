from especiales.src.Portada import Portada
from especiales.RIO_NEGRO_8_cipoletti.apps.encuesta_RIO_NEGRO_8_cipoletti import encuesta
from especiales.RIO_NEGRO_8_cipoletti.apps.estructura_RIO_NEGRO_8_cipoletti import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


