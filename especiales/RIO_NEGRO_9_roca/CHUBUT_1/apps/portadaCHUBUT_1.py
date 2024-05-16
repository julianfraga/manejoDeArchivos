from especiales.src.Portada import Portada
from especiales.CHUBUT_1.apps.encuesta_CHUBUT_1 import encuesta
from especiales.CHUBUT_1.apps.estructura_CHUBUT_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


