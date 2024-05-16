from especiales.src.Portada import Portada
from especiales.APOYO_LULA.apps.encuesta_APOYO_LULA import encuesta
from especiales.APOYO_LULA.apps.estructura_APOYO_LULA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


