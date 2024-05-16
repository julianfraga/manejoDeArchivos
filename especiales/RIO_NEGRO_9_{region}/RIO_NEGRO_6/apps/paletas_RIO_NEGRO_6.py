from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong, ingresosColorDict, diverging_mini
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
paletas["P13"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio ': colores["cambiemos"], 'Juntos Somos Río Negro': coloresRN["juntosSomos"], 'Liberales': colores["liberales"], 'Izquierda': colores["izquierda"], 'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P14"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente y Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P14_imputada"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente y Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente y Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente y Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente y Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["P18"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', "Algo seguro", 'Para nada seguro'], diverging, noSabe= False)
paletas["P19"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22"] = list2dictPalette(['Sí', 'No'], diverging_mini, noSabe=False)
paletas["P23"] = {'Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peronismo"], 'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por La Libertad Avanza': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Temas de Coyuntura
paletas["P30"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P31"] = list2dictPalette(['No estaba enterado del tema', 'Un tema de la vida privada de él', 'Un hecho vergonzoso de exclusiva responsabilidad de él', 'Un hecho vergonzoso del cual también es responsable el gobernador Kicillof', 'Un hecho vergonzoso que muestran como son los dirigentes que apoyan a Sergio Massa', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P32"] = siNoColorDict
paletas["P33"] = {'Sergio Massa': colores["peronismo"], 'Patria Bullrich': colores["cambiemos"], 'Javier Milei': colores["liberales"], 'Myriam Bregman': colores["izquierda"], 'Juan Schiaretti': colores["peronismo_nok"]}

paletas["P34"] =  list2dictPalette(['Ha aumentado significativamente', 'Ha aumentado ligeramente', 'Se mantiene igual', 'Ha disminuido ligeramente', 'Ha disminuido significativamente'], diverging, noSabe=False)
paletas["P35"] = list2dictPalette(['No, ninguna dificultad', 'Alguna dificultad ocasional', 'Sí, dificultades frecuentes'], diverging, noSabe=False)
paletas["P36"] = list2dictPalette(['Sí, absolutamente', 'Sí, en cierta medida', 'No, en absoluto'], diverging, noSabe=False)
paletas["P37"] = list2dictPalette(['Reducir la inflación', 'Implementar reformas fiscales', 'Establecer políticas de control de precios', 'Reducir el gasto público', 'Estimular la inversión extranjera', 'Aumentar los subsidios a los servicios públicos'], qualitative_strong, noSabe=False)
paletas["P38"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P39"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P40"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P41"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P42"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)

# Bloque Reach de intención de voto
paletas["P43"] = votaria
paletas["P44"] = votaria
paletas["P45"] = votaria
paletas["P46"] = votaria
paletas["P47"] = votaria

# Bloque Control
paletas["P48"] = siNoColorDict

# Bloque Preferencias políticas
paletas["DIPUTADOS"] = {'Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["DIPUTADOS_imputada"] = {'Martín Soria a Diputado Nacional por Unión por la Patria': colores["peronismo"], 'Sergio Capozzi a Diputado Nacional por Juntos por el Cambio': colores["cambiemos"], 'Luis Di Giacomo a Diputado Nacional por Juntos somos Rio Negro': coloresRN["juntosSomos"], 'Lorena Villaverde a Diputada Nacional por la Libertad Avanza': colores["liberales"], 'Alhue Gavuzzo a Diputada Nacional por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["PRESIDENTE"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresident por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE_imputada"] = {'Sergio Massa a Presidente, Agustín Rossi a Vicepresidente por Unión por la Patria': colores["peronismo"], 'Patricia Bullrich a Presidente, Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a Presidente, Victoria Villarruel a Vicepresident por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a Presidente, Nicolas del Caño a Vicepresidente por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente': colores["peronismo_nok"], 'En blanco': colores["blanco"]}