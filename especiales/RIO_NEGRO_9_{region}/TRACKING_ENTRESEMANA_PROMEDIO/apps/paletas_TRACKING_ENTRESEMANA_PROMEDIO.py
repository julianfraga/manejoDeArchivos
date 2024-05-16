from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong,diverging_reverse

# comando:


paletas = {}

# Bloque Control
paletas["P10"] = frecuenciaColorDict

# Bloque Intención de voto 
paletas["P11"] = {'Unión por la Patria': colores["peronismo_contraste"], 'La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11_imputada"] = {'Unión por la Patria': colores["peronismo_contraste"], 'La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"]}
paletas["P11_imputada_sinblanco"] = {'Unión por la Patria': colores["peronismo_contraste"], 'La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"]}

paletas["P13"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13_imputada"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"]}

paletas["P13_imputada_sinblanco"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P16"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P17"] = votaria
paletas["P18"] = votaria

# Bloque Coyuntura
paletas["P19"] = opinionColorDict
paletas["P20"] = list2dictPalette(['Totalmente de acuerdo', 'Algo de acuerdo', 'ni de acuerdo ni en desacuerdo', 'En desacuerdo', 'Totalmente en desacuerdo'], diverging, noSabe=False)
paletas["P21"] = list2dictPalette(['Cristiano no practicante', 'Católico apostólico romano', 'Cristiano evangelista o pentecostal', 'Otras confesiones cristianas', 'Musulmán', 'Judío', 'Otras', 'No soy religioso', 'Ateo'], qualitative_strong, noSabe=False)