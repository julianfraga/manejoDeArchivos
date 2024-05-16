from especiales.src.Portada import Portada
from especiales.RIOCUARTO.apps.encuesta_RIOCUARTO import encuesta
from especiales.RIOCUARTO.apps.estructura_RIOCUARTO import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


