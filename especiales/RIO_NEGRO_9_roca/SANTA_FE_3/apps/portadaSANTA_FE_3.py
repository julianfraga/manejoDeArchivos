from especiales.src.Portada import Portada
from especiales.SANTA_FE_3.apps.encuesta_SANTA_FE_3 import encuesta
from especiales.SANTA_FE_3.apps.estructura_SANTA_FE_3 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


