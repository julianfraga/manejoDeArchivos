from especiales.src.Portada import Portada
from especiales.POSICIONAMIENTO_ESPECIAL_NACIONAL.apps.encuesta_POSICIONAMIENTO_ESPECIAL_NACIONAL import encuesta
from especiales.POSICIONAMIENTO_ESPECIAL_NACIONAL.apps.estructura_POSICIONAMIENTO_ESPECIAL_NACIONAL import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


