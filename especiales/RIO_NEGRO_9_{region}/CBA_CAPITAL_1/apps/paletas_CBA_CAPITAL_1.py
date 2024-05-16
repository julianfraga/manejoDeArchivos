from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, list2dictPalette,diverging

# comando:

paletas = {}

colores['vecinal'] = '#b800eb' 
# Bloque Control
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos locales
paletas["P10"] = {'A Daniel Passerini intendente y Javier Pretto viceintendente por Hacemos Unidos Por Córdoba': colores["peronismo1"], 'A Rodrigo de Loredo intendente y Soher el Sukaria viceintendenta por Juntos por el Cambio': colores["cambiemos"], 'A Verónica Sikora intendenta y Enrique Rigatuso viceintendente por La Libertad Primero': colores["liberales"], 'A Juan Pablo Quinteros intendente y Gabriel Ratner viceintendente por Somos Córdoba': colores["cambiemos2"], 'A Jorge Scala intendente y Paola Janett González Cuevas viceintendenta por el Partido Demócrata': colores["cristianos"], 'A Humberto Spaccesi intendente y Silvia Peñaloza viceintendenta por Córdoba de Todos': colores["peronismo2"], 'A César Orgaz intendente y Gonzalo Frontera viceintendente por Encuentro Vecinal Córdoba': colores["vecinal"], 'A Laura Vilches intendenta y Virginia Caldera Marsengo viceintendenta por El Frente De Izquierda y De Trabajadores-Unidad': colores["izquierda"], 'A los candidatos de otros partidos políticos': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P10_imputadas"] = {'A Daniel Passerini intendente y Javier Pretto viceintendente por Hacemos Unidos Por Córdoba': colores["peronismo1"], 'A Rodrigo de Loredo intendente y Soher el Sukaria viceintendenta por Juntos por el Cambio': colores["cambiemos"], 'A Verónica Sikora intendenta y Enrique Rigatuso viceintendente por La Libertad Primero': colores["liberales"], 'A Juan Pablo Quinteros intendente y Gabriel Ratner viceintendente por Somos Córdoba': colores["cambiemos2"], 'A Jorge Scala intendente y Paola Janett González Cuevas viceintendenta por el Partido Demócrata': colores["cristianos"], 'A Humberto Spaccesi intendente y Silvia Peñaloza viceintendenta por Córdoba de Todos': colores["peronismo2"], 'A César Orgaz intendente y Gonzalo Frontera viceintendente por Encuentro Vecinal Córdoba': colores["vecinal"], 'A Laura Vilches intendenta y Virginia Caldera Marsengo viceintendenta por El Frente De Izquierda y De Trabajadores-Unidad': colores["izquierda"], 'A los candidatos de otros partidos políticos': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P12"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P13"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Control
paletas["P14"] = siNoColorDict