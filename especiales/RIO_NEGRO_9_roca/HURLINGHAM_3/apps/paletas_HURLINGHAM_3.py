from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, list2dictPalette,diverging

# comando:

paletas = {}
# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P09"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro pais': colores["otros"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P10"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo2"], 'Sergio Massa a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peronismo3"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peronismo4"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P16"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P19"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Damian Selci a intendente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P25"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P26"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Control
paletas["P27"] = siNoColorDict


# Imputadas
# Bloque Escenarios políticos 
paletas["P10_imputadas"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo2"], 'Sergio Massa a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peronismo3"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peronismo4"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13_imputadas"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P16_imputadas"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P19_imputadas"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Damian Selci a intendente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22_imputadas"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
