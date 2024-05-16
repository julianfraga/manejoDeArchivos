from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = list2dictPalette(['Siempre', 'Casi siempre', 'Casi nunca', 'Nunca, pero esta es una excepción'], diverging, noSabe=False)

# Bloque Bloque electoral
paletas["P10"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a presidenta, Rubén Sobrero a gobernador y Paula Akerfeld a intendenta por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13_imputada"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a presidenta, Rubén Sobrero a gobernador y Paula Akerfeld a intendenta por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["P16"] = siNoColorDict
paletas["PRESIDENTE"] = {'Sergio Massa a presidente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a presidenta por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE_imputada"] = {'Sergio Massa a presidente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a presidenta por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["GOBERNADOR"] = {'Axel Kicillof a gobernador por Unión por la Patria.': colores["peronismo"], 'Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'El candidato a gobernador de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["GOBERNADOR_imputada"] = {'Axel Kicillof a gobernador por Unión por la Patria.': colores["peronismo"], 'Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'El candidato a gobernador de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["INTENDENTE"] = {'Julio Zamora a intendente por Unión por la Patria.': colores["peronismo"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Paula Akerfeld a intendenta por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["INTENDENTE_imputada"] = {'Julio Zamora a intendente por Unión por la Patria.': colores["peronismo"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Paula Akerfeld a intendenta por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["P26"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P27"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Control
paletas["P28"] = siNoColorDict