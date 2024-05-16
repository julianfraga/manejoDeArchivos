from especiales.src.Portada import Portada
from especiales.LEY_OMNIBUS_2_convoto.apps.encuesta_LEY_OMNIBUS_2_convoto import encuesta
from especiales.LEY_OMNIBUS_2_convoto.apps.estructura_LEY_OMNIBUS_2_convoto import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


