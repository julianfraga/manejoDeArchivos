from especiales.src.Portada import Portada
from especiales.LEY_OMNIBUS_2.apps.encuesta_LEY_OMNIBUS_2 import encuesta
from especiales.LEY_OMNIBUS_2.apps.estructura_LEY_OMNIBUS_2 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


