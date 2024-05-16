from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging

# comando:


paletas = {}
# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Escenarios Políticos
paletas["P08"] = {'Pablo Javkin a intendente por Unidos para Cambiar Santa Fe': colores["cambiemos"], 'Juan Monteverde a intendente por Juntos Avancemos': colores["peronismo"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P08_imputada"] = paletas["P08"]

paletas["P10"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P11"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

paletas["P12"] = {'Maximiliano Pullaro a gobernador y Gisela Scaglia a vicegobernadora por Unidos para Cambiar Santa Fe': colores["cambiemos"], 'Marcelo Lewandowski a gobernador y Silvina Patricia Frana a vicegobernadora por Juntos Avancemos': colores["peronismo"], 'Edelvino Bodoira a gobernador y Nora Lucia Sanchez por Viva la Libertad': colores["liberales"], 'Carla Deiana a gobernadora y Mauricio Acosta a vicegobernador por el Frente de Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P12_imputada"] =paletas["P12"]

paletas["P14"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P14_imputada"] = paletas["P14"] 

# Bloque Control
paletas["P17"] = siNoColorDict