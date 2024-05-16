from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, diverging,list2dictPalette, diverging_mini

# comando:

paletas = {}
coloresRN = {
   'juntosSomos' : '#64e05c', #verde
  'avancemos' : '#e36a27', 
  'unidadPopular' : '#0927bd',
  'unidos' : '#ffa200' #naranja
}
# Bloque Control

paletas["DIPUTADOS"] = {"Martín Soria a Diputado Nacional por Unión por la Patria" : colores['peronismo'],"Sergio Capozzi a Diputado Nacional por Juntos por el Cambio": colores["cambiemos"],"Roberto Brusa a Diputado Nacional por Juntos por el Cambio": colores["cambiemos2"],"Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro": coloresRN["juntosSomos"],"Lorena Villaverde a Diputada Nacional por la Libertad Avanza": colores["liberales"],"Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda": colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas['PRESIDENTE'] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peron2"], 'Juan Grabois a Presidente, Paula Abal Medina a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peron3"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a Presidente, Gerardo Morales a Vicepresidente y Roberto Brusa a Diputado Nacional por Juntos por el Cambio': colores["cambiemos2"],'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente y Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P06"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 
                                      'Tiene dudas sobre si va a ir a  votar', 
                                      'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P07"] = muchoPocoColorDict
paletas["P08"] = frecuenciaColorDict

# Bloque Preferencias Electorales
paletas["P11"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'Juntos Somos Río Negro': colores["peron2"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Juan Grabois a Presidente, Paula Abal Medina a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a Presidente, Gerardo Morales a Vicepresidente y Roberto Brusa a Diputado Nacional por Juntos por el Cambio': colores["cambiemos2"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente y Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P16"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 
                                           'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)

paletas["P17"] = {'Solo votaría Diputados Nacionales': colores["otros"], 'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Juan Grabois a Presidente, Paula Abal Medina a Vicepresidente y por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a Presidente, Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P20"] = dict(zip(['Sí', 'No'], diverging_mini))

paletas["P21"] = {'Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Roberto Brusa a Diputado Nacional por Juntos por el Cambio': colores["cambiemos2"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P25"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente y Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta a Presidente, Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente y Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"],'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P35"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P36"] = {'Horacio Rodríguez Larreta  a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P37"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P38"] = votaria
paletas["P39"] = votaria
paletas["P40"] = votaria
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria
paletas["P44"] = votaria

# Bloque Control
paletas["P45"] = siNoColorDict