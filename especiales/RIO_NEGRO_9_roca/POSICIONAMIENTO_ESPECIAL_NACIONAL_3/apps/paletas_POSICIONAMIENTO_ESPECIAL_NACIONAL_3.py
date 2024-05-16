from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, diverging, frecuenciaColorDict,seguridadVotoColorDict

# comando:


paletas = {}
# Bloque Control
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = frecuenciaColorDict
paletas["P08"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Preferencias electorales
paletas["P10"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a Presidente y Paula Abal Medina a Vicepresidente por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P14"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 
                                           'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)

paletas["P23"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a Presidente y Paula Abal Medina a Vicepresidente por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P36"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P37"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P38"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P39"] = {'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P40"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P43"] = votaria
paletas["P44"] = votaria
paletas["P45"] = votaria
paletas["P46"] = votaria
paletas["P47"] = votaria
paletas["P48"] = votaria
paletas["P49"] = votaria

# Bloque Control
paletas["P60"] = siNoColorDict