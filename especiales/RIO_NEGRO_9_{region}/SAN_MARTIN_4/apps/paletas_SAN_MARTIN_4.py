from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P09"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P12"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora y Hernán Sardella a intendente por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P12_imputada"] = paletas["P12"]

paletas["P15"] = siNoColorDict
paletas["P16"] = {'Sergio Massa a presidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a presidenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente de la Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P16_imputada"] = paletas["P16"]

paletas["P19"] = {'Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo"], 'Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'El candidato a gobernador de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P19_imputada"] = paletas["P19"]

paletas["P22"] = {'Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 'Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos"], 'Hernán Sardella a intendente por la Libertad Avanza': colores["liberales"], 'El candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P22_imputada"] = paletas["P22"] 

paletas["P25"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], diverging, noSabe=True)
paletas["P26"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P27"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Reach de intención de voto
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria

# Bloque control
paletas["P31"] = siNoColorDict

paletas['PRESIDENTE']={"Sergio Massa a presidente por Unión por la Patria": colores["peronismo"],
"Patricia Bullrich a presidenta por Juntos por el Cambio": colores["cambiemos"],
"Javier Milei a presidente por la Libertad Avanza": colores["liberales"],
"Los candidatos a presidente de la Izquierda": colores["izquierda"],
"Juan Schiaretti a presidente por Hacemos por Nuestro Pais": colores["peronismo_nok"],'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas['PRESIDENTE_imputada']=paletas['PRESIDENTE']

paletas['GOBERNADOR']={'Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo"], 'Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'El candidato a gobernador de la Izquierda': colores["izquierda"],'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas['GOBERNADOR_imputada']=paletas['GOBERNADOR']

paletas['INTENDENTE']={'Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"],"Mauricio D’Alessandro a intendente por Juntos por el Cambio": colores["cambiemos"],"Hernán Sardella a intendente por la Libertad Avanza": colores["liberales"],"El candidato del Frente de Izquierda": colores["izquierda"],'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas['INTENDENTE_imputada']=paletas['INTENDENTE']

