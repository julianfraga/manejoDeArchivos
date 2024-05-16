from especiales.src.Portada import Portada
from especiales.ENTRE_RIOS_1.apps.encuesta_ENTRE_RIOS_1 import encuesta
from especiales.ENTRE_RIOS_1.apps.estructura_ENTRE_RIOS_1 import layout_preguntas

portada = Portada(encuesta, layout_preguntas)
layout = portada.layout


