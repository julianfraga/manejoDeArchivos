from especiales.src.Portada import Portada
from especiales.POSICIONAMIENTO_ESPECIAL_CABA_5.apps.encuesta_POSICIONAMIENTO_ESPECIAL_CABA_5 import encuesta
from especiales.POSICIONAMIENTO_ESPECIAL_CABA_5.apps.estructura_POSICIONAMIENTO_ESPECIAL_CABA_5 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


