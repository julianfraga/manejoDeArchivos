from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque General
paletas["P06"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"], 'Aun no tengo decidido mi voto': colores["otros"]}

paletas["P08"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P09"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P10"] = votaria
paletas["P11"] = votaria
paletas["P12"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales_contraste"]}

paletas["P14"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"]}