from config import colores, votaria, opinionColorDict, list2dictPalette,diverging_reverse, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P07"] = frecuenciaColorDict

# Bloque General
paletas["P08"] = opinionColorDict
paletas["P09"] = list2dictPalette(['Muy negativa', 'Negativa', 'Indiferente', 'Positiva', 'Muy positiva'], diverging_reverse, noSabe=False)
paletas["P11"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo_contraste"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales_contraste"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13"] = votaria
paletas["P14"] = votaria