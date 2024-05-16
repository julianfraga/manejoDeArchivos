from especiales.SAN_MARTIN_3.apps.cuestionario_SAN_MARTIN_3 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, internas


paletas = {}
# Bloque Intención de voto por espacio político 

# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por Nuestro País': colores["otros"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P09"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 'Sergio Massa a presidente, Axel Kicillof a gobernador y Leonardo Grosso a intendente por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo3"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Leonardo Grosso a intendente por Unión por la Patria': colores["peronismo4"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora y Hernán Sardella a intendente por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P12"] = votaria
paletas["P13"] = votaria
paletas["P14"] = votaria
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = siNoColorDict