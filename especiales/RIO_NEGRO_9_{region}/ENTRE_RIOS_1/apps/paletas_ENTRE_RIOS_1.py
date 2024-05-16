from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, list2dictPalette, diverging

# comando:

paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict
paletas["P07"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Preferencias electorales 
paletas["P09"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["otros"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P12"] = {'Sergio Massa a presidente, Agustín Rossi a vicepresidente, Adán Bahl a gobernador y Claudia Monjo a vicegobernadora a  por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Paula Abal Medina a vicepresidenta, Adán Bahl a gobernador y Claudia Monjo a vicegobernadora por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Luis Petri a vicepresidente, Rogelio Frigerio a gobernador y Alicia Aluani a vicegobernadora por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Gerardo Morales a vicepresidente, Rogelio Frigerio a gobernador y Alicia Aluani a vicegobernadora por Juntos por el Cambio': colores["cambiemos2"], 'Pedro Galimberti a gobernador y Ana D´Angelo a vicegobernadora por Juntos por el Cambio': colores["cambiemos3"],'Javier Milei a presidente, Victoria Villarruel a vicepresidenta, Arturo Etchevere a gobernador y Mayda Spizzi a vicegobernadora por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente, vicepresidente, gobernador y vicegobernador  del Frente de Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)

# Bloque Reach de intención de voto
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = siNoColorDict

paletas["P12_imputada"] = {'Sergio Massa a presidente, Agustín Rossi a vicepresidente, Adán Bahl a gobernador y Claudia Monjo a vicegobernadora a  por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Paula Abal Medina a vicepresidenta, Adán Bahl a gobernador y Claudia Monjo a vicegobernadora por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Luis Petri a vicepresidente, Rogelio Frigerio a gobernador y Alicia Aluani a vicegobernadora por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Gerardo Morales a vicepresidente, Rogelio Frigerio a gobernador y Alicia Aluani a vicegobernadora por Juntos por el Cambio': colores["cambiemos2"], 'Pedro Galimberti a gobernador y Ana D´Angelo a vicegobernadora por Juntos por el Cambio': colores["cambiemos3"],'Javier Milei a presidente, Victoria Villarruel a vicepresidenta, Arturo Etchevere a gobernador y Mayda Spizzi a vicegobernadora por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente, vicepresidente, gobernador y vicegobernador  del Frente de Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE"] = {'Sergio Massa a presidente, Agustín Rossi a vicepresidente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Paula Abal Medina a vicepresidenta por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Luis Petri a vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Gerardo Morales a vicepresidente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Victoria Villarruel a vicepresidenta por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente, vicepresidente del Frente de Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE_imputada"] = {'Sergio Massa a presidente, Agustín Rossi a vicepresidente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Paula Abal Medina a vicepresidenta por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Luis Petri a vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Gerardo Morales a vicepresidente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Victoria Villarruel a vicepresidenta por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente, vicepresidente del Frente de Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
