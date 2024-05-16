from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong,diverging_mini

# comando:


paletas = {}

# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict
paletas['P10'] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

# Bloque Escenarios de votación
paletas["P13"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Gustavo Menéndez a intendente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y David Zencich a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Eduardo Varela a intendente por la Libertad Avanza': colores["liberales"], 'Raul Othacehé a intendente por el frente vecinal crecer': colores["otros"], 'Los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13_imputada"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Gustavo Menéndez a intendente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y David Zencich a intendente por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Eduardo Varela a intendente por la Libertad Avanza': colores["liberales"], 'Raul Othacehé a intendente por el frente vecinal crecer': colores["otros"], 'Los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["P16"] = siNoColorDict
paletas["PRESIDENTE"] = {'Sergio Massa a presidente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente de la Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["PRESIDENTE_imputada"] = {'Sergio Massa a presidente por Unión por la Patria.': colores["peronismo"], 'Patricia Bullrich a presidenta por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei a presidente por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente de la Izquierda': colores["izquierda"], 'Juan Schiaretti a presidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 'En blanco': colores["blanco"]}

paletas["GOBERNADOR"] = {'Axel Kicillof a gobernador por Unión por la Patria.': colores["peronismo"], 'Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'El candidato a gobernador de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["GOBERNADOR_imputada"] = {'Axel Kicillof a gobernador por Unión por la Patria.': colores["peronismo"], 'Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"], 'Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 'El candidato a gobernador de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["INTENDENTE"] = {'Gustavo Menéndez a intendente por Unión por la Patria.': colores["peronismo"], 'Zencich a intendente por Juntos por el Cambio': colores["cambiemos"], 'Eduardo Varela a intendente por la Libertad Avanza': colores["liberales"], 'Raul Othacehé a intendente por el frente vecinal crecer': colores["otros"], 'El candidato a intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["INTENDENTE_imputada"] = {'Gustavo Menéndez a intendente por Unión por la Patria.': colores["peronismo"], 'Zencich a intendente por Juntos por el Cambio': colores["cambiemos"], 'Eduardo Varela a intendente por la Libertad Avanza': colores["liberales"], 'Raul Othacehé a intendente por el frente vecinal crecer': colores["otros"], 'El candidato a intendente de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["P26"] = list2dictPalette(['Totalmente seguro.', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P27"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)

# Bloque Temas de Coyuntura
paletas["P28"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones', 'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar', 'Con políticas de desarrollo que permitan el crecimiento con inclusión social', 'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables', 'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P29"] = list2dictPalette(['No estaba enterado del tema', 'Un tema de la vida privada de él', 'Un hecho vergonzoso de exclusiva responsabilidad de él', 'Un hecho vergonzoso del cual también es responsable el gobernador Kicillof', 'Un hecho vergonzoso que muestran como son los dirigentes que apoyan a Sergio Massa', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P30"] = siNoColorDict
paletas["P31"] = {'Sergio Massa': colores["peronismo"], 'Patria Bullrich': colores["cambiemos"], 'Javier Milei': colores["liberales"], 'Myriam Bregman': colores["izquierda"], 'Juan Schiaretti': colores["peronismo_nok"]}

paletas["P32"] = list2dictPalette(['Ha aumentado significativamente', 'Ha aumentado ligeramente', 'Se mantiene igual', 'Ha disminuido ligeramente', 'Ha disminuido significativamente'], diverging, noSabe=False)
paletas["P33"] = list2dictPalette(['No, ninguna dificultad', 'Alguna dificultad ocasional', 'Sí, dificultades frecuentes'], diverging, noSabe=False)
paletas["P34"] = list2dictPalette(['Sí, absolutamente', 'Sí, en cierta medida', 'No, en absoluto'], diverging, noSabe=False)
paletas["P35"] = list2dictPalette(['Reducir la inflación', 'Implementar reformas fiscales', 'Establecer políticas de control de precios', 'Reducir el gasto público', 'Estimular la inversión extranjera', 'Aumentar los subsidios a los servicios públicos'], qualitative_strong, noSabe=False)
paletas["P36"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P37"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P38"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P39"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P40"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)

# Bloque Reach de intención de voto
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria
paletas["P44"] = votaria
paletas["P45"] = siNoColorDict