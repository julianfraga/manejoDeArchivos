from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging, qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias Electorales
paletas["P09"] = {'Unidos para Cambiar Santa Fe': colores["cambiemos"], 'Juntos Avancemos': colores["peronismo"], 'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Maximiliano Pullaro a gobernador y Gisela Scaglia a vicegobernadora por Unidos para Cambiar Santa Fe': colores["cambiemos"], 'Marcelo Lewandowski a gobernador y Silvina Patricia Frana a vicegobernadora por Juntos Avancemos': colores["peronismo"], 'Edelvino Bodoira a gobernador y Nora Lucia Sanchez por Viva la Libertad': colores["liberales"], 'Carla Deiana a gobernadora y Mauricio Acosta a vicegobernador por el Frente de Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P11_imputada"] = paletas["P11"]
paletas["P13"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P14"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P15"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P16"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria. ': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P16_imputada"] = paletas["P16"]

# Bloque Control
paletas["P19"] = siNoColorDict