from especiales.TIGRE_14.apps.cuestionario_TIGRE_14 import cuestionario
from config import colores, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, votaria


paletas = {}

# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Intención de voto intendente
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["otros"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P09"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendente por Unión por la Patria': colores["peronismo"], 'Sergio Massa a presidente, Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendente por Unión por la Patria': colores["peronismo3"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria': colores["peronismo4"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendente por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria': colores["peronismo3"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P15"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendente por Unión por la Patria': colores["peronismo2"], 'Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria': colores["peronismo3"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto fórmulas
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria

paletas["P26"] = siNoColorDict