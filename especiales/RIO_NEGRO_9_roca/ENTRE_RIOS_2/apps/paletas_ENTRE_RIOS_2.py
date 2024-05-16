from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, seguridadVotoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = list2dictPalette(['Mucho', 'Bastante', 'Poco', 'Nada', 'No sabe'], diverging, noSabe=True)
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P10"] = {'Unidos para Cambiar misiones': colores["cambiemos"], 'Juntos Avancemos': colores["peronismo"], 'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P13"] = {'Sergio Massa a presidente, Agustín Rossi a vicepresidente, Adán Bahl a gobernador y Claudia Monjo a vicegobernadora a  por Unión por la Patria': 
colores["peronismo"], 'Patricia Bullrich a presidenta, Luis Petri a vicepresidente, Rogelio Frigerio a gobernador y Alicia Aluani a vicegobernadora por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Victoria Villarruel a vicepresidenta, Arturo Etchevere a gobernador y Mayda Spizzi a vicegobernadora por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a presidenta y Nicolas del Caño a vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"],'No sabe': colores["nosabe"]}
paletas["P13_imputada"] = paletas["P13"]

paletas["P16"] = siNoColorDict
paletas["P17"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P20"] = {'Adán Bahl a gobernador y Claudia Monjo a vicegobernadora a  por Unión por la Patria': colores["peronismo"], 'Rogelio Frigerio a gobernador y Alicia Aluani a vicegobernadora por Juntos por el Cambio': colores["cambiemos"], 'Arturo Etchevere a gobernador y Mayda Spizzi a vicegobernadora por la Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P23"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P24"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 
                                           'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P25"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Reach de intención de voto
paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = siNoColorDict


paletas["PRESIDENTE"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE_imputada"] = paletas["PRESIDENTE"]

paletas["GOBERNADOR"] = {'Adán Bahl a gobernador y Claudia Monjo a vicegobernadora a  por Unión por la Patria':colores["peronismo"], 'Rogelio Frigerio a gobernador y Alicia Aluani a vicegobernadora por Juntos por el Cambio':colores['cambiemos'],'Arturo Etchevere a gobernador y Mayda Spizzi a vicegobernadora por la Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["GOBERNADOR_imputada"] = paletas["GOBERNADOR"] 