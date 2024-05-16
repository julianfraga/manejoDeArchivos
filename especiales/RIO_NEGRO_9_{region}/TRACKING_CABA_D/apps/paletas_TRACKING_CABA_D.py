from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

## Bloque Intención de voto 
paletas["P10"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P10_imputada"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"]}

paletas["P13"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y vicepresidente de la izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13_imputada"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y vicepresidente de la izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["P16"] = {'Union por la Patria': colores["peronismo"], 'Cambiemos': colores["cambiemos"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P16_imputada"] = {'Union por la Patria': colores["peronismo"], 'Cambiemos': colores["cambiemos"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"]}

paletas["P17"] = {'Leandro Santoro a Jefe de Gobierno por Union por la Patria': colores["peronismo"], 'Jorge Macri a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos"], 'Ramiro Marra a Jefe de Gobierno por la Libertad Avanza': colores["liberales"], 'La candidata a Jefe de Gobierno de la izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P17_imputada"] = {'Leandro Santoro a Jefe de Gobierno por Union por la Patria': colores["peronismo"], 'Jorge Macri a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos"], 'Ramiro Marra a Jefe de Gobierno por la Libertad Avanza': colores["liberales"], 'Los candidatos a Jefe de Gobierno de la izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["P26"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P27"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Escenarios electorales: Segunda vuelta 
paletas["P28"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Político
paletas["P38"] = list2dictPalette(['Inflación', 'Desempleo', 'Corrupción', 'Inseguridad', 'Precio del dólar', 'Pobreza', 'Narcotráfico', 'Tarifas', 'Otro', 'No sabe'], qualitative_strong, noSabe=True)