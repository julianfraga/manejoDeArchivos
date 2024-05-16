from especiales.src.Portada import Portada
from especiales.POSICIONAMIENTO_ESPECIAL_PBA.apps.encuesta_POSICIONAMIENTO_ESPECIAL_PBA import encuesta
from especiales.POSICIONAMIENTO_ESPECIAL_PBA.apps.estructura_POSICIONAMIENTO_ESPECIAL_PBA import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


