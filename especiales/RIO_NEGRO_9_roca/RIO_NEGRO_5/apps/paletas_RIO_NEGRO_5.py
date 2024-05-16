from config import colores, votaria, seguridadVotoColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict,diverging, diverging_mini

# comando:
coloresRN = {
   'juntosSomos' : '#64e05c', #verde
  'avancemos' : '#e36a27', #naranja oscuro
  'unidadPopular' : '#0927bd', #azul
  'unidos' : '#ffa200' #naranja
}

paletas = {}

# Bloque Control
paletas["P06"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P07"] = muchoPocoColorDict
paletas["P08"] = frecuenciaColorDict

# Bloque Preferencias políticas
paletas["P12"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'Juntos Somos Río Negro': colores["otros"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P13"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente y Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13_imputada"] = paletas["P13"]
paletas["P17"] = seguridadVotoColorDict
paletas["P18"] = {'Solo votaría Diputados Nacionales': colores["otros"], 'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"],
                   'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 
                   'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente el Frente de Izquierda': colores["izquierda"],
                   'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P21"] = dict(zip(['Sí', 'No'], diverging_mini))
paletas["P22"] = {'Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios Electorales: Segunda Vuelta
paletas["P26"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = votaria
paletas["P32"] = votaria
paletas["P33"] = votaria

# Bloque Control
paletas["P34"] = siNoColorDict

paletas["DIPUTADOS"] = {"Martín Soria a Diputado Nacional por Unión por la Patria" : colores['peronismo'],"Sergio Capozzi a Diputado Nacional por Juntos por el Cambio": colores["cambiemos"],"Roberto Brusa a Diputado Nacional por Juntos por el Cambio": colores["cambiemos2"],"Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro": coloresRN["juntosSomos"],"Lorena Villaverde a Diputada Nacional por la Libertad Avanza": colores["liberales"],"Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda": colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["DIPUTADOS_imputada"] = paletas["DIPUTADOS"] 

paletas['PRESIDENTE'] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peron1"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresident por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores['peronismo_nok'], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas['PRESIDENTE_imputada'] = paletas['PRESIDENTE'] 