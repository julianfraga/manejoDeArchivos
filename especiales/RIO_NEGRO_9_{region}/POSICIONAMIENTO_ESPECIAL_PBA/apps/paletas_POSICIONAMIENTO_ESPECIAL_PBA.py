from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging

# comando:


paletas = {}
# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Posicionamiento Político
paletas["P08"] = {'Unión por la Patria': colores["peron1"], 
                  'Juntos por el Cambio': colores["cambiemos"], 
                  'Liberales': colores["otros"], 'Izquierda': colores["liberales"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios Políticos
paletas["P09"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peron1"], 
                  'Juan Grabois a Presidente y Paula Abal Medina a Vicepresidente por Unión por la Patria': colores["peron2"], 
                  'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos3"], 
                  'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 
                  'Myriam Bregman a Presidente y Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 
                  'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 
                  'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Leandro Santoro a Jefe de Gobierno por Unión por la Patria': colores["peron1"], 
                  'Jorge Macri a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos"], 
                  'Martin Lousteau a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos3"], 
                  'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                  'Vanina Biasi por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peron1"], 
                  'Juan Grabois Presidente, Paula Abal Medina Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peron2"], 
                  'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta Presidente, Gerardo Morales Vicepresidente y Diego Santilli gobernador, Gustavo Posse vicegobernador; por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 
                    'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 
                    'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 
                    'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P18"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peron1"], 
                  'Juan Grabois a Presidente y Paula Abal Medina a Vicepresidente por Unión por la Patria': colores["peron2"], 
                  'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 
                    'Myriam Bregman a Presidente y Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 
                    'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 
                    'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P21"] = {'Leandro Santoro a Jefe de Gobierno por Unión por la Patria': colores["peron1"], 
                  'Jorge Macri a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos"],
                  'Martin Lousteau a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos3"],
                    'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                    'Vanina Biasi por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P24"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peron1"], 
                  'Juan Grabois Presidente, Paula Abal Medina Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peron2"], 
                  'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta Presidente, Gerardo Morales Vicepresidente y Diego Santilli gobernador, Gustavo Posse vicegobernador; por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P25"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)

paletas["P26"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P27"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peron1"], 
                  'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 
                  'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 
                  'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 
                  'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"],
                    'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peron1"],
                   'Horacio Rodríguez Larreta a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos3"],
                     'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 
                     'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 
                     'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Leandro Santoro a Jefe de Gobierno por Unión por la Patria': colores["peron1"], 
                  'Jorge Macri a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos"], 
                  'Ramiro Marra por la Libertad Avanza': colores["liberales"], 'Vanina Biasi por el Frente de Izquierda': colores["izquierda"], 
                  'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Leandro Santoro a Jefe de Gobierno por Unión por la Patria': colores["peron1"], 'Martin Lousteau a Jefe de Gobierno por Juntos por el Cambio': colores["cambiemos3"], 
                  'Ramiro Marra por la Libertad Avanza': colores["liberales"], 'Vanina Biasi por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peron1"], 
                  'Patricia Bullrich Presidenta, Luis Petri Vicepresidente y Nestor Grindetti gobernador, Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"],
                    'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"],
                      'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 
                      'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P32"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente y Axel Kicillof gobernador, Veronica Magario vicegobernadora; por Unión por la Patria': colores["peron1"], 
                  'Horacio Rodríguez Larreta Presidente, Gerardo Morales Vicepresidente y Diego Santilli gobernador, Gustavo Posse vicegobernador; por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei Presidente, Victoria Villarruel Vicepresidenta y Carolina Piparo gobernadora, Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente, Alejandro Bodart a gobernador y Jimena Letieri por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente, Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peron1"],
                   'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 
                  'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P35"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peron1"], 
                  'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos3"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P36"] = {'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos3"], 
                  'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P37"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Unión por la Patria': colores["peron1"], 
                  'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P38"] = votaria
paletas["P39"] = votaria
paletas["P40"] = votaria
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria
paletas["P44"] = votaria
paletas["P45"] = votaria
paletas["P46"] = votaria
paletas["P47"] = votaria
paletas["P48"] = votaria
paletas["P49"] = votaria
paletas["P50"] = votaria
paletas["P51"] = votaria

# Bloque control
paletas["P52"] = siNoColorDict