from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = frecuenciaColorDict

# Bloque Preferencias políticas
paletas["P10"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Pablo Todero a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Francisco Sánchez a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente por la Libertad Avanza y Nadia Marquez a Diputada Nacional por Arriba Neuquén': colores["liberales"], 'Sandro Badilla a diputado nacional por el movimiento popular neuquino':colores["cristianos"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Patricia Jure a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P10_imputada"]  = paletas["P10"] 

paletas["P13"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P17"] = siNoColorDict
paletas["P18"] = {'Pablo Todero a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Francisco Sánchez a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Nadia Márquez a Diputada Nacional por Arriba Neuquén': colores["liberales"], 'Sandro Badilla a diputado nacional por el movimiento popular neuquino': colores["cristianos"], 'Patricia Jure a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P18_imputada"] = paletas["P18"]

paletas['CORTA_DIPUTADOS'] = siNoColorDict
paletas['PRESIDENTE'] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria. ': colores["peronismo"],
'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"],
'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda':colores["izquierda"],
'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"],
 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas['PRESIDENTE_imputada'] = paletas['PRESIDENTE'] 
paletas['DIPUTADOS'] = {'Pablo Todero a Diputado Nacional por Unión por la Patria': colores["peronismo"],
'Francisco Sánchez a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"],
'Nadia Márquez a Diputada Nacional por Arriba Neuquén': colores["liberales"],
'Sandro Badilla a diputado nacional por el movimiento popular neuquino':colores["cristianos"],
'Patricia Jure a Diputada Nacional por el Frente de Izquierda':colores["izquierda"],
 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas['DIPUTADOS_imputada'] =paletas['DIPUTADOS'] 

# Bloque Imaegenes
paletas["P21"] = opinionColorDict
paletas["P22"] = opinionColorDict
paletas["P23"] = opinionColorDict
paletas["P24"] = opinionColorDict
paletas["P25"] = opinionColorDict
paletas["P26"] = opinionColorDict

# Bloque Control
paletas["P27"] = siNoColorDict
