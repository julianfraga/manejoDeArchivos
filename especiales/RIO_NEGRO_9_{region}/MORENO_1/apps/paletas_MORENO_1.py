from config import colores, votaria, diverging, list2dictPalette, siNoColorDict, muchoPocoColorDict, diverging_mini, frecuenciaColorDict

paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["otros"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Intención de voto intendente
paletas["P11"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Mariel Fernández a intendente por Unión por la Patria': colores["peronismo"], 'Sergio Massa a presidente, Axel Kicillof a gobernador y Damián Contreras a intendente por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Mariel Fernández a intendente por Unión por la Patria': colores["peronismo3"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Damián Contreras a intendente por Unión por la Patria': colores["peronismo4"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Gisele Agosttineli a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Anibal Assef a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Andrea Vera a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P21"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P22"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

paletas["PRESIDENTE"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente y gobernador de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["INTENDENTE"] = {'Mariel Fernández a intendente por Unión por la Patria': colores["peronismo"], 'Damián Contreras a intendente por Unión por la Patria': colores["peronismo2"], 'Giselle Agosttineli a intendente por Juntos por el Cambio': colores["cambiemos"], 'Aníbal Assef a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Andrea Vera a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

# Bloque Reach de intención de voto
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria
paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = votaria

#Control
paletas["P30"] = siNoColorDict
