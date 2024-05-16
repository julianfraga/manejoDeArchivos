from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging, qualitative_strong

# comando:


paletas = {}
# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias políticas
paletas["P09"] = {'Alfredo Cornejo a gobernador y Hebe Casado a vicegobernador por Cambia Mendoza': colores["cambiemos"], 'Omar De Marchi a gobernador y Daniel Orozco a vicegobernador por La Unión Mendocina': colores["liberales"], 'Omar Parisi a gobernador y Lucas Ilardo a vicegobernador por Elegí Mendoza': colores["peronismo"], 'Mario Vadillo a gobernador y Emanuel Fugazzotto a vicegobernador por el Partido Verde': colores["otros"], 'Lautaro Giménez a gobernador y Noelia Barbeito a vicegobernadora por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P09_imputada"] = paletas["P09"]

paletas["P12"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P13"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P14"] = paletas["P26"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P15"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15_imputada"] = paletas["P15"] 
# Bloque Reach de intención de voto
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria

# Bloque control
paletas["P23"] = siNoColorDict