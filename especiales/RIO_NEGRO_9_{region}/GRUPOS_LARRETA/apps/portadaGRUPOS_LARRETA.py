from especiales.src.Portada import Portada
from especiales.GRUPOS_LARRETA.apps.encuesta_GRUPOS_LARRETA import encuesta
from especiales.GRUPOS_LARRETA.apps.estructura_GRUPOS_LARRETA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


