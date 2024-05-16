from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, diverging, frecuenciaColorDict,seguridadVotoColorDict

# comando:


paletas = {}

# Bloque Control
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = frecuenciaColorDict

# Bloque Preferencias Políticas
paletas["P08"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Escenarios Electorales
paletas["P11"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'Liberales': colores["otros"], 'Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P16"] = {'Leandro Santoro a Jefe de Gobierno por Union por la Patria': colores["peronismo"], 'Jorge Macri a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos"], 'Ramiro Marra por la Libertad Avanza': colores["liberales"], 'Vanina Biasi por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P19"] = seguridadVotoColorDict
paletas["P24"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Leandro Santoro a Jefe de Gobierno por Union por la Patria': colores["peronismo"], 'Jorge Macri a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos"], 'Ramiro Marra por la Libertad Avanza': colores["liberales"], 'Vanina Biasi por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P32"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Leandro Santoro por Union por la Patria': colores["peronismo"], 'Jorge Macri por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P35"] = votaria
paletas["P36"] = votaria
paletas["P37"] = votaria
paletas["P38"] = votaria
paletas["P39"] = votaria
paletas["P45"] = votaria
paletas["P46"] = votaria

# Bloque Control
paletas["P52"] = siNoColorDict