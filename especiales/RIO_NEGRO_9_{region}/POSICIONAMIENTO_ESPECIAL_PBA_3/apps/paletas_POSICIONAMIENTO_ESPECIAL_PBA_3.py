from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, diverging, frecuenciaColorDict,seguridadVotoColorDict

# comando:


paletas = {}
# Bloque Control
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = frecuenciaColorDict
paletas["P08"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Preferencias electorales
paletas["P10"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P19"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peronismo"], 'Juan Grabois Presidente, Paula Abal Medina Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta Presidente, Gerardo Morales Vicepresidente y Diego Santilli gobernador, Gustavo Posse vicegobernador; por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 
                                           'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P29"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peronismo"], 'Juan Grabois Presidente, Paula Abal Medina Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta Presidente, Gerardo Morales Vicepresidente y Diego Santilli gobernador, Gustavo Posse vicegobernador; por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P35"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta Presidente, Gerardo Morales Vicepresidente y Diego Santilli gobernador, Gustavo Posse vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P36"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P37"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P38"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P39"] = {'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P40"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P50"] = votaria
paletas["P51"] = votaria
paletas["P52"] = votaria
paletas["P53"] = votaria
paletas["P54"] = votaria
paletas["P55"] = votaria
paletas["P56"] = votaria

# Bloque Control
paletas["P60"] = siNoColorDict