from especiales.src.Portada import Portada
from especiales.GRUPOS_BLANCOPASO.apps.encuesta_GRUPOS_BLANCOPASO import encuesta
from especiales.GRUPOS_BLANCOPASO.apps.estructura_GRUPOS_BLANCOPASO import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


