from especiales.src.Portada import Portada
from especiales.SANTA_FE_2.apps.encuesta_SANTA_FE_2 import encuesta
from especiales.SANTA_FE_2.apps.estructura_SANTA_FE_2 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


