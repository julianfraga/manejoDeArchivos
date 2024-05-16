from especiales.src.Portada import Portada
from especiales.GRUPOS_BULLRICH.apps.encuesta_GRUPOS_BULLRICH import encuesta
from especiales.GRUPOS_BULLRICH.apps.estructura_GRUPOS_BULLRICH import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


