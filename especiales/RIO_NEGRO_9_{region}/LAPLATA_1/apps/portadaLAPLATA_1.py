from especiales.src.Portada import Portada
from especiales.LAPLATA_1.apps.encuesta_LAPLATA_1 import encuesta
from especiales.LAPLATA_1.apps.estructura_LAPLATA_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


