from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging, qualitative_strong

# comando:


paletas = {}
coloresOtrosChaco =  {
    'renovadora' : "#6A3D67",
    'integrador' : "#B15A28",
    'upg' : "#CAB2D6"}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias Electorales
paletas["P09"] = {'Frente chaqueño': colores["peronismo"], 'Juntos por el cambio': colores["cambiemos"], 'Corriente de expresión renovada': coloresOtrosChaco["renovadora"], 'Partido Integrador': coloresOtrosChaco["integrador"], 'La libertad avanza': colores["liberales"], 'Libertarios en acción': colores["liberales2"], 'Frente unidos por la gente': coloresOtrosChaco["upg"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Jorge Capitanich a gobernador y Analia Rach a vicegobernador por Frente chaqueño': colores["peronismo"], 'Leandro Zdero a gobernador y Silvina Schneider a vicegobernadora por Juntos por el cambio': colores["cambiemos"], 'Gustavo Martinez a gobernador y Lidia Viviam Piolini a vicegobernadora por Corriente de expresión renovada': coloresOtrosChaco["renovadora"], 'Bassileff Ivanoff a gobernador y Picon Cesar a vicegobernador por el Partido Integrador':coloresOtrosChaco["integrador"], 'Alfredo Rodríguez a gobernador y Llena Aguirre a vicegobernadora por la libertad avanza': colores["liberales"], 'Rubén Galassi a gobernador y Marta Kassor a vicegobernador por libertarios en acción': colores["liberales2"], 'Domingo Peppo a gobernador y Nicolas Matta a vicegobernador por el frente unidos por la gente': coloresOtrosChaco["upg"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P11_imputada"] = paletas["P11"]

paletas["P13"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P14"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P15"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P16"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria. ': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P16_imputada"] = paletas["P16"]

# Bloque Control
paletas["P19"] = siNoColorDict