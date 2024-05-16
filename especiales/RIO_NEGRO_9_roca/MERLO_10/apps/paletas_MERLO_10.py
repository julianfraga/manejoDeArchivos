from especiales.MERLO_10.apps.cuestionario_MERLO_10 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict,list2dictPalette, siNoColorDict

paletas = {}
# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Intención de voto
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P09"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Gustavo Menéndez a intendente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Gustavo Menéndez a intendente por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Pablo Cocuzza a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y David Zencich a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Eduardo Varela a intendente por la Libertad Avanza': colores["liberales"], 'Raul Othaceché a intendente por el frente vecinal crecer': colores["otros"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Guillermo Moreno a presidente, Luis D´elia a gobernador y Alberto Viscoti a intendente por Principios y valores': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P12"] = votaria
paletas["P13"] = votaria
paletas["P14"] = votaria
paletas["P15"] = votaria
paletas["P16"] = votaria

# Bloque Control
paletas["P17"] = siNoColorDict
