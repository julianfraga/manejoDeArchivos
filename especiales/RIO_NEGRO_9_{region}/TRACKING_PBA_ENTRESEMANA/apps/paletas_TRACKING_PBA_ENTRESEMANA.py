from config import frecuenciaColorDict, colores, deudasColorDict,list2dictPalette,diverging_mini, problemaColorDict,diverging, votaria, ingresosColorDict, opinionColorDict, comparacionColorDict, mediosColorDict, siNoColorDict,qualitative_strong, problemaColorDict, siNoNoSabeColorDict

# comando:
paletas = {}


# Bloque Control
paletas["P10"] = frecuenciaColorDict

# Bloque Coyuntura
paletas["P11"] = siNoNoSabeColorDict
paletas["P12"] = {'Javier Milei': colores["liberales_contraste"], 'Mauricio Macri': colores["cambiemos"], 'Ambos': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P13"] = siNoNoSabeColorDict
paletas["P14"] = {'Florencio Randazzo': colores["peronismo_nok"], 'Cristian Ritondo': colores["cambiemos"], 'Algun diputado del bloque de Milei': colores["liberales_contraste"], 'No sabe': colores["nosabe"]}

paletas["P15"] = siNoNoSabeColorDict
paletas["P16"] = siNoNoSabeColorDict
paletas["P17"] = siNoNoSabeColorDict
paletas["P18"] = list2dictPalette(['Los cargos públicos', 'El empleo público', 'Los planes sociales', 'Las tarifas de los servicios públicos', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P19"] = siNoNoSabeColorDict
paletas["P20"] = siNoNoSabeColorDict

# Bloque Político
paletas["P21"] = problemaColorDict

# Bloque Socioeconómico
paletas["P25"] = deudasColorDict
paletas["P26"] = ingresosColorDict
paletas["P27"] = opinionColorDict
paletas["P28"] = comparacionColorDict
paletas["P29"] = comparacionColorDict
paletas["P30"] = opinionColorDict
paletas["P31"] = comparacionColorDict
paletas["P32"] = comparacionColorDict
paletas["P33"] = opinionColorDict
paletas["P34"] = opinionColorDict
# Bloque Políticas públicas
paletas["P35"] = opinionColorDict
paletas["P36"] = opinionColorDict
paletas["P37"] = opinionColorDict

# Bloque Imagen de dirigentes
paletas["P38"] = opinionColorDict
paletas["P39"] = opinionColorDict
paletas["P40"] = opinionColorDict
paletas["P41"] = opinionColorDict
paletas["P42"] = opinionColorDict
paletas["P43"] = opinionColorDict
paletas["P44"] = opinionColorDict
paletas["P45"] = opinionColorDict
paletas["P46"] = opinionColorDict
paletas["P47"] = opinionColorDict
paletas["P48"] = opinionColorDict
paletas["P49"] = opinionColorDict
paletas["P50"] = opinionColorDict
paletas["P52"] = opinionColorDict
paletas["P53"] = opinionColorDict

# Bloque General
paletas["P54"] = mediosColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = opinionColorDict