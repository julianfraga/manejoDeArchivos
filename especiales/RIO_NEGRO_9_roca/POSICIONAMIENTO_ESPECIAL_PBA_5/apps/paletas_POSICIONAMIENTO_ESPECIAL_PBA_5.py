from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, diverging, frecuenciaColorDict,seguridadVotoColorDict

# comando:


paletas = {}

# Bloque Control
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = frecuenciaColorDict

# Bloque Preferencias Políticas
paletas["P08"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Escenarios Electorales
paletas["P11"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P20"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Union por la Patria': colores["peronismo"], 'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P23"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)

paletas["P30"] = {'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Union por la Patria': colores["peronismo"], 'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P32"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["GOBERNADOR"] = {'Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Union por la Patria': colores["peronismo"], 'Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

# Bloque Reach de intención de voto
paletas["P40"] = votaria
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria
paletas["P44"] = votaria
paletas["P47"] = siNoColorDict

paletas["P48"] = {'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"]}

paletas["P49"] = {'Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Union por la Patria': colores["peronismo"], 'Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"]}

paletas["P50"] = {'Al candidato a intendente por la Libertad Avanza': colores["liberales"], 'Al candidato a intendente de Union por la Patria': colores["peronismo"], 'Al candidato a intendente por Juntos por el Cambio': colores["cambiemos"], 'Al candidato a intendente por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"]}

paletas["P51"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)

# Bloque Control
paletas["P52"] = siNoColorDict