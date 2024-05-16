from config import frecuenciaColorDict, colores, deudasColorDict,list2dictPalette,diverging_mini, problemaColorDict,diverging, votaria, ingresosColorDict, opinionColorDict, comparacionColorDict, mediosColorDict, siNoColorDict,qualitative_strong, problemaColorDict

# comando:
paletas = {}

# Bloque Control
paletas["P10"] = frecuenciaColorDict

# Bloque Intención de voto 
paletas["P11"] = {'Unión por la Patria': colores["peronismo_contraste"], 'La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11_imputada"] = {'Unión por la Patria': colores["peronismo_contraste"], 'La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"]}
paletas["P11_imputada_sinblanco"] = {'Unión por la Patria': colores["peronismo_contraste"], 'La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"]}

paletas["P13"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales_contraste"],'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13_imputada"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"]}
paletas["P13_imputada_sinblanco"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales_contraste"],  'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales_contraste"],'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P16"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
# Bloque Reach de dirigentes nacionales
paletas["P17"] = votaria
paletas["P18"] = votaria


# Bloque Coyuntura
paletas["P19"] = list2dictPalette(['Si', 'No'], diverging_mini, noSabe=False)
paletas["P20"] = {'Sergio Massa':colores["peronismo_contraste"], 'Javier Milei': colores["liberales_contraste"]}
paletas["P21"] ={'Sergio Massa':colores["peronismo_contraste"], 'Javier Milei': colores["liberales_contraste"]}
paletas["P22"] ={'Sergio Massa':colores["peronismo_contraste"], 'Javier Milei': colores["liberales_contraste"]}
paletas["P23"] ={'Sergio Massa':colores["peronismo_contraste"], 'Javier Milei': colores["liberales_contraste"]}
paletas["P24"] = list2dictPalette(['Si', 'No'], diverging_mini, noSabe=False)
paletas["P25"] = list2dictPalette(['Si', 'No'], diverging_mini, noSabe=False)

# Bloque Político
paletas["P28"] = problemaColorDict

# Bloque Socioeconómico
paletas["P32"] = deudasColorDict
paletas["P33"] = ingresosColorDict
paletas["P34"] = opinionColorDict
paletas["P35"] = comparacionColorDict
paletas["P36"] = comparacionColorDict
paletas["P37"] = opinionColorDict
paletas["P38"] = comparacionColorDict
paletas["P39"] = comparacionColorDict
paletas["P40"] = opinionColorDict
paletas["P41"] = opinionColorDict
# Bloque Políticas públicas
paletas["P42"] = opinionColorDict
paletas["P43"] = opinionColorDict
paletas["P44"] = opinionColorDict

# Bloque Imagen de dirigentes
paletas["P45"] = opinionColorDict
paletas["P46"] = opinionColorDict
paletas["P47"] = opinionColorDict
paletas["P48"] = opinionColorDict
paletas["P49"] = opinionColorDict
paletas["P50"] = opinionColorDict
paletas["P51"] = opinionColorDict
paletas["P52"] = opinionColorDict
paletas["P53"] = opinionColorDict
paletas["P54"] = opinionColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = opinionColorDict
paletas["P57"] = opinionColorDict
paletas["P58"] = opinionColorDict
# Bloque General
paletas["P59"] = mediosColorDict
paletas["P60"] = opinionColorDict
paletas["P61"] = opinionColorDict