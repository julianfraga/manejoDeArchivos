from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], qualitative_strong, noSabe=False)
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = frecuenciaColorDict

# Bloque Preferencias políticas
paletas["P11"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Pablo Todero a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Francisco Sánchez a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente por la Libertad Avanza y Nadia Marquez a Diputada Nacional por Arriba Neuquén': colores["liberales"], 'Sandro Badilla a diputado nacional por el movimiento popular neuquino': colores["cristianos"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Patricia Jure a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11_imputada"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Pablo Todero a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Francisco Sánchez a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente por la Libertad Avanza y Nadia Marquez a Diputada Nacional por Arriba Neuquén': colores["liberales"], 'Sandro Badilla a diputado nacional por el movimiento popular neuquino': colores["cristianos"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Patricia Jure a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["P14"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], qualitative_strong, noSabe=False)
paletas["P18"] = list2dictPalette(['Si', 'No'], qualitative_strong, noSabe=False)

paletas["CORTA_DIPUTADOS"] = siNoColorDict
paletas["DIPUTADOS"] = {'Pablo Todero a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Francisco Sánchez a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Nadia Márquez a Diputada Nacional por Arriba Neuquén': colores["liberales"], 'Sandro Badilla a diputado nacional por el movimiento popular neuquino': colores["cristianos"], 'Patricia Jure a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["DIPUTADOS_imputada"] = {'Pablo Todero a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Francisco Sánchez a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Nadia Márquez a Diputada Nacional por Arriba Neuquén': colores["liberales"], 'Sandro Badilla a diputado nacional por el movimiento popular neuquino': colores["cristianos"], 'Patricia Jure a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["PRESIDENTE"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria. ': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE_imputada"] = {'Sergio Massa a Presidente y Agustín Rossi a Vicepresidente por Unión por la Patria. ': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente y Nicolás del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"]}


# Bloque Temas de Coyuntura
paletas["P22"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P23"] = list2dictPalette(['No estaba enterado del tema', 'Un tema de la vida privada de él', 'Un hecho vergonzoso de exclusiva responsabilidad de él', 'Un hecho vergonzoso del cual también es responsable el gobernador Kicillof', 'Un hecho vergonzoso que muestran como son los dirigentes que apoyan a Sergio Massa', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P24"] = list2dictPalette(['Ha aumentado significativamente', 'Ha aumentado ligeramente', 'Se mantiene igual', 'Ha disminuido ligeramente', 'Ha disminuido significativamente'], diverging, noSabe=False)
paletas["P25"] = list2dictPalette(['No, ninguna dificultad', 'Alguna dificultad ocasional', 'Sí, dificultades frecuentes'], diverging, noSabe=False)
paletas["P26"] = list2dictPalette(['Sí, absolutamente', 'Sí, en cierta medida', 'No, en absoluto'], diverging, noSabe=False)
paletas["P27"] = list2dictPalette(['Reducir la inflación', 'Implementar reformas fiscales', 'Establecer políticas de control de precios', 'Reducir el gasto público', 'Estimular la inversión extranjera', 'Aumentar los subsidios a los servicios públicos'], qualitative_strong, noSabe=False)
paletas["P28"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P29"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P30"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P31"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P32"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)

# Bloque Imagen de dirigentes
paletas["P33"] = opinionColorDict
paletas["P34"] = opinionColorDict
paletas["P35"] = opinionColorDict
paletas["P36"] = opinionColorDict
paletas["P37"] = opinionColorDict
paletas["P38"] = opinionColorDict

# Bloque Control
paletas["P39"] = siNoColorDict