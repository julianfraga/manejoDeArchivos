from especiales.src.Portada import Portada
from especiales.LEY_OMNIBUS.apps.encuesta_LEY_OMNIBUS import encuesta
from especiales.LEY_OMNIBUS.apps.estructura_LEY_OMNIBUS import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


