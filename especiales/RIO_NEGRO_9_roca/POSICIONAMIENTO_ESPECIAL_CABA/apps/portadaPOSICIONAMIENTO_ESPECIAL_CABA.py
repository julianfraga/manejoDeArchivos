from especiales.src.Portada import Portada
from especiales.POSICIONAMIENTO_ESPECIAL_CABA.apps.encuesta_POSICIONAMIENTO_ESPECIAL_CABA import encuesta
from especiales.POSICIONAMIENTO_ESPECIAL_CABA.apps.estructura_POSICIONAMIENTO_ESPECIAL_CABA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


