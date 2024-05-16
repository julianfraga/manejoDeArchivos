from config import colores, votaria, diverging, list2dictPalette, siNoColorDict, muchoPocoColorDict, frecuenciaColorDict

# comando:


paletas = {}

# Bloque Control
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = frecuenciaColorDict

# Bloque Intención de voto intendente
paletas["P08"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Espinoza a intendente por Unión por la Patria': colores["peronismo"], 'Sergio Massa a presidente, Axel Kicillof a gobernador y Patricia Cubria a intendente por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Fernando Espinoza a intendente por Unión por la Patria': colores["peronismo3"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Patricia Cubria a intendente por Unión por la Patria': colores["peronismo4"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Eduardo “Lalo” Creus a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Josefina Mendoza a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Adrián "El Dipy" Martínez a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}
paletas["P08_imputadas"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Espinoza a intendente por Unión por la Patria': colores["peronismo"], 'Sergio Massa a presidente, Axel Kicillof a gobernador y Patricia Cubria a intendente por Unión por la Patria': colores["peronismo2"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Fernando Espinoza a intendente por Unión por la Patria': colores["peronismo3"], 'Juan Grabois a presidente, Axel Kicillof a gobernador y Patricia Cubria a intendente por Unión por la Patria': colores["peronismo4"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Eduardo “Lalo” Creus a intendente por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Josefina Mendoza a intendente por Juntos por el Cambio': colores["cambiemos2"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Adrián "El Dipy" Martínez a intendente por la Libertad Avanza': colores["liberales"], 'Alguno de los candidatos a presidente, gobernador e intendente de la Izquierda': colores["izquierda"], 'Otros': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P11"] = list2dictPalette(['Totalmente seguro', 'Bastante seguro', 'Algo seguro', 'Para nada seguro'], diverging, noSabe=False)
paletas["P12"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
paletas["P13"] = {'Fernando Espinoza a intendente por Unión por la Patria': colores["peronismo"], 'Patricia Cubria a intendente por Unión por la Patria': colores["peronismo2"], 'María Laura Ramírez a intendente por Unión por la Patria': colores["peronismo3"], 'Eduardo “Lalo” Creus por Juntos por el Cambio': colores["cambiemos"], 'Josefina Mendoza por Juntos por el Cambio': colores["cambiemos2"], 'Héctor “Toty” Flores a intendente por Juntos por el Cambio': colores["cambiemos3"], 'Adrián "El Dipy" Martínez a intendente por la Libertad Avanza': colores["liberales"], 'Alberto Samid a intendente por Principios y Valores': colores["otros"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}
paletas["P13_imputadas"] = {'Fernando Espinoza a intendente por Unión por la Patria': colores["peronismo"], 'Patricia Cubria a intendente por Unión por la Patria': colores["peronismo2"], 'María Laura Ramírez a intendente por Unión por la Patria': colores["peronismo3"], 'Eduardo “Lalo” Creus por Juntos por el Cambio': colores["cambiemos"], 'Josefina Mendoza por Juntos por el Cambio': colores["cambiemos2"], 'Héctor “Toty” Flores a intendente por Juntos por el Cambio': colores["cambiemos3"], 'Adrián "El Dipy" Martínez a intendente por la Libertad Avanza': colores["liberales"], 'Alberto Samid a intendente por Principios y Valores': colores["otros"], 'Alguno de los candidatos a intendente de la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria
paletas["P23"] = votaria

# Bloque Control
paletas["P24"] = siNoColorDict