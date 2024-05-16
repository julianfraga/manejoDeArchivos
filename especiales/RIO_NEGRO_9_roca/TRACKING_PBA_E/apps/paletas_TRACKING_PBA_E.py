from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:
corteBoleta = {'No cortaría boleta a gobernador' : colores["cambiemos_ucr"],
               'Axel Kicillof a gobernador y Verónica Magario a vicegobernadora por unión por la patria' : colores["peronismo"],
                  'Néstor Grindetti a gobernador y Miguel Fernández a vicegobernador por juntos por el cambio' : colores["cambiemos"], 
                  'Carolina Piparo a Gobernadora y Francisco Oneto a Vicegobernador por la Libertad Avanza' : colores["liberales"],
                  'Axel Kicillof gobernador y Veronica Magario vicegobernadora; por Union por la Patria' : colores["peronismo"],
                  'Nestor Grindetti gobernador y Miguel Fernandez vicegobernador; por Juntos por el Cambio' : colores["cambiemos"], 
                  'Carolina Piparo gobernadora y Francisco Oneto vicegobernador; por la Libertad Avanza' : colores["liberales"],
                 'Carolina Piparo a gobernadora y Francisco Oneto a vicegobernador por la libertad avanza' : colores["liberales"],
                  'Gobernador y vicegobernador de la izquierda' : colores["izquierda"],'Otro' : colores["otros"], 'En blanco' : colores["blanco"], 'No sabe' : colores["nosabe"]}


paletas = {}

# Bloque Intención de voto 
paletas["P10"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P10_imputada"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"]}

paletas["P20"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente, Axel Kicillof gobernador y Veronica Magario vicegobernadora; por Union por la Patria': colores["peronismo"], 'Patricia Bullrich Presidenta, Luis Petri Vicepresidente, Nestor Grindetti gobernador y Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei Presidente, Victoria Villarruel Vicepresidenta, Carolina Piparo gobernadora y Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente, vicepresidente, gobernador y vicegobernador de la izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P20_imputada"] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente, Axel Kicillof gobernador y Veronica Magario vicegobernadora; por Union por la Patria': colores["peronismo"], 'Patricia Bullrich Presidenta, Luis Petri Vicepresidente, Nestor Grindetti gobernador y Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei Presidente, Victoria Villarruel Vicepresidenta, Carolina Piparo gobernadora y Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente, vicepresidente, gobernador y vicegobernador de la izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P26"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P27"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Escenarios electorales: Segunda vuelta 
paletas["P28"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Político
paletas["P38"] = list2dictPalette(['Inflación', 'Desempleo', 'Corrupción', 'Inseguridad', 'Precio del dólar', 'Pobreza', 'Narcotráfico', 'Tarifas', 'Otro', 'No sabe'], qualitative_strong, noSabe=True)

paletas['CORTA_GOBERNADOR'] = siNoColorDict

paletas['GOBERNADOR'] = corteBoleta

paletas['GOBERNADOR_imputada'] = corteBoleta