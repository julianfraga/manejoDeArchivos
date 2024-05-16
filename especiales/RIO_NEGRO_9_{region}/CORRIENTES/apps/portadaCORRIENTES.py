from especiales.src.Portada import Portada
from especiales.CORRIENTES.apps.encuesta_CORRIENTES import encuesta
from especiales.CORRIENTES.apps.estructura_CORRIENTES import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


