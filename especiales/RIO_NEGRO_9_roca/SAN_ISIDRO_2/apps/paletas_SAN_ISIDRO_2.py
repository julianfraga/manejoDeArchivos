from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Escenarios Electorales: elecciones PASO
paletas["P09"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio ': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Federico Meca a intendente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Ramón Lanus a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora y Rodolfo Paolucci a intendente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a presidenta, Rubén Sobrero a gobernador y Camila Paiz a intendenta por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P12_imputada"] = paletas["P12"]
paletas["P15"] = siNoColorDict
paletas["P16"] = {'Sergio Massa a presidente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente por la Libertad Avanza': colores["liberales"], 'Myriam Bregman a presidenta por el Frente de Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro País': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["P19"] = {'Axel Kicillof a gobernador por Unión por la Patria.': colores["peronismo"], 'Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'Rubén Sobrero a gobernador por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["P22"] = {'Federico Meca a intendente por Unión por la Patria.': colores["peronismo"], 'Ramón Lanus a intendente por Juntos por el Cambio': colores["cambiemos"], 'Rodolfo Paolucci a intendente por la Libertad Avanza': colores["liberales"], 'Camila Paiz a intendenta por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["P25"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P26"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], qualitative_strong, noSabe=False)
paletas["P27"] = list2dictPalette(['Tiene Decidido que va a ir a votar.', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], qualitative_strong, noSabe=False)

# Bloque Control
paletas["P28"] = siNoColorDict

paletas["PRESIDENTE"] = {"Sergio Massa a presidente por Unión por la Patria.": colores["peronismo"], 
          "Patricia Bullrich a presidenta por Juntos por el Cambio":colores["cambiemos"], 
          "Javier Milei a presidente por la Libertad Avanza": colores["liberales"], 
          "Myriam Bregman a presidenta por el Frente de Izquierda": colores["izquierda"], 
          "Juan Schiaretti a presidente por Hacemos por Nuestro País": colores["peronismo_nok"],'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas['PRESIDENTE_imputada'] = paletas["PRESIDENTE"]
paletas["GOBERNADOR"] = {"Axel Kicillof a gobernador por Unión por la Patria.": colores["peronismo"],
                                 "Néstor Grindetti a gobernador por Juntos por el Cambio": colores["cambiemos"],
                                     "Carolina Piparo a gobernadora por la Libertad Avanza": colores["liberales"],
                                     "Rubén Sobrero a gobernador por el Frente de Izquierda": colores["izquierda"],
                                     "En blanco": colores["blanco"], 'No sabe': colores["nosabe"]}   

paletas["GOBERNADOR_imputada"] = paletas["GOBERNADOR"]
paletas["INTENDENTE"] = {"Federico Meca a intendente por Unión por la Patria.": colores["peronismo"],
                                     "Ramón Lanus a intendente por Juntos por el Cambio": colores["cambiemos"],
                                     "Rodolfo Paolucci a intendente por la Libertad Avanza": colores["liberales"],
                                     "Camila Paiz a intendenta por el Frente de Izquierda": colores["izquierda"],
                                     "En blanco": colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["INTENDENTE_imputada"] =  paletas["INTENDENTE"] 
