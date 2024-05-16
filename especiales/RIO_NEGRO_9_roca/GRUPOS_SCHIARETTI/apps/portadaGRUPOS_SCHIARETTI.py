from especiales.src.Portada import Portada
from especiales.GRUPOS_SCHIARETTI.apps.encuesta_GRUPOS_SCHIARETTI import encuesta
from especiales.GRUPOS_SCHIARETTI.apps.estructura_GRUPOS_SCHIARETTI import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


