from config import colores, votaria, diverging, list2dictPalette, siNoColorDict, muchoPocoColorDict, diverging_mini, frecuenciaColorDict

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict
paletas["P07"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 
                                      'Tiene dudas sobre si va a ir a  votar', 
                                      'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Preferencias electorales
paletas["P09"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["otros"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria': colores["peronismo3"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P15"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P16"] = list2dictPalette(['Sí', 'No'], diverging_mini, noSabe=False)
paletas["P17"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente y gobernador de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P20"] = {'Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P23"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False) #oculta

paletas["P24"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = votaria
paletas["P32"] = votaria
paletas["P33"] = votaria
paletas["P34"] = siNoColorDict


paletas["PRESIDENTE"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente y gobernador de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE_imputada"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo2"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente y gobernador de la Izquierda': colores["izquierda"], 'Otros': colores["otros"]}

paletas["P12_imputada"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Julio Zamora a intendente por Unión por la Patria': colores["peronismo3"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["INTENDENTE"] = {'Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["INTENDENTE_imputada"] = {'Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"]}

paletas["INTENDENTE_CORTA_1"] = {'Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}
paletas["INTENDENTE_CORTA_2"] = {'Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["INTENDENTE_CORTA_1_imputada"] = {'Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"]}
paletas["INTENDENTE_CORTA_2_imputada"] = {'Malena Galmarini a intendenta por Unión por la Patria': colores["peronismo"], 'Julio Zamora a intendente por Unión por la Patria': colores["peronismo2"], 'Claudio Cufré a intendente por Juntos por el Cambio': colores["cambiemos"], 'Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Claudio Baumgarten a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"]}
