from especiales.src.Portada import Portada
from especiales.GRUPOS_BLANCOYNULO.apps.encuesta_GRUPOS_BLANCOYNULO import encuesta
from especiales.GRUPOS_BLANCOYNULO.apps.estructura_GRUPOS_BLANCOYNULO import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


