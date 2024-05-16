from especiales.src.Portada import Portada
from especiales.RIO_NEGRO_7_bariloche.apps.encuesta_RIO_NEGRO_7_bariloche import encuesta
from especiales.RIO_NEGRO_7_bariloche.apps.estructura_RIO_NEGRO_7_bariloche import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


