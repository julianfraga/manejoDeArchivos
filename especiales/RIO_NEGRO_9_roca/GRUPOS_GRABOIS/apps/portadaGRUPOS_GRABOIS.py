from especiales.src.Portada import Portada
from especiales.GRUPOS_GRABOIS.apps.encuesta_GRUPOS_GRABOIS import encuesta
from especiales.GRUPOS_GRABOIS.apps.estructura_GRUPOS_GRABOIS import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


