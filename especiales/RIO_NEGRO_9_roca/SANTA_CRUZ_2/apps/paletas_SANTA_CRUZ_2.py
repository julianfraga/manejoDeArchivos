from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, internas

# comando:

paletas = {}
# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P09"] = {'Sergio Massa a presidente y Agustín Rossi a vicepresidente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente y Paula Abal Medina a vicepresidenta por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta y Luis Petri a vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente y Gerardo Morales a vicepresidente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente y Victoria Villarruel a vicepresidenta por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Pablo Grasso a gobernador y Javier Castro a vicegobernador dentro del lema de Unión por la Patria': colores["peronismo"], 'Javier Belloni a gobernador y Fernando Cotillo a vicegobernador dentro del lema de Unión por la Patria': colores["peronismo2"], 'Guillermo Polke  a gobernador y Miriam Glorgia a vicegobernadora dentro del lema de Unión por la Patria': colores["peronismo3"], 'Claudio Vidal a gobernador y Fabián Leguizamón a vicegobernador dentro del lema de por Santa Cruz': colores["cambiemos"], 'Jose Carambia a gobernador y Maria Guerra a vicegobernadora dentro del lema de por Santa Cruz': colores["cambiemos2"], 'A alguno de los otros candidatos a gobernador del lema Por Santa Cruz: Sergio Acevedo, Daniel Gardonio, Mario Markic o Ruben Ferrara': colores["cambiemos3"], 'Roxana Reyes a gobernadora y Luis Vera a vicegobernador dentro del lema de Cambia Santa Cruz': colores["cambiemos4"], 'Mirey Zeidan a gobernador y Carlos Fernández a vicegobernador dentro del lema de Cambia Santa Cruz': colores["cambiemos5"], 'Alguno de los candidatos de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}


# Bloque Reach de candidatos
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria
paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria

# Bloque Control
paletas["P31"] = siNoColorDict