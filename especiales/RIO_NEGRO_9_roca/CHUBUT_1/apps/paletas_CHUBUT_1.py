from config import colores, votaria, list2dictPalette, siNoColorDict, muchoPocoColorDict, frecuenciaColorDict

# comando:


paletas = {}
# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Arriba Chubut': colores["peronismo"], 'Juntos por el Cambio Chubut': colores["cambiemos"], 'Por la Libertad Independiente Chubutense': colores["liberales"], 'Frente de Izquierda': colores["izquierda"], 'Generación para un Encuentro Nacional': colores["cambiemos_ucr"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos provinciales 
paletas["P14"] = {'A Juan Pablo Luque gobernador y Ricardo Sastre vicegobernador por Arriba Chubut': colores["peronismo"], 'A Ignacio Torres gobernador y Gustavo Menna vicegobernador por Juntos por el Cambio': colores["cambiemos"], 'A César Treffinger gobernador y Laura Mirantes vicegobernadora por La Libertad Independiente Chubutense': colores["liberales"], 'A Emilse Saavedra gobernadora y Julieta Rusconi vicegobernadora por el Frente de Izquierda y de los Trabajadores-Unidad': colores["izquierda"], 'A Oscar Petersen gobernador y Nancy Lobos vicegobernadora por el GEN': colores["cambiemos_ucr"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P17"] = {'A Juan Pablo Luque gobernador por la Alianza Arriba Chubut con el apoyo de Cristina Fernández de Kirchner, Sergio Massa, Alberto Fernández, Mariano Arcioni y el Peronismo': colores["peronismo"], 'A Ignacio Torres gobernador por Juntos por el Cambio con el apoyo de Patricia Bullrich, Horacio Rodríguez Larreta, Mauricio Macri, el PRO y la UCR': colores["cambiemos"], 'A César Treffinger gobernador por La Libertad Independiente Chubutense con el apoyo de Javier Milei': colores["liberales"], 'A Emilse Saavedra gobernadora por el Frente de Izquierda y de los Trabajadores-Unidad con el apoyo de Gabriel Solano y Vilma Ripoll': colores["izquierda"], 'A Oscar Petersen gobernador por el GEN': colores["cambiemos_ucr"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P14_imputada"] = {'A Juan Pablo Luque gobernador y Ricardo Sastre vicegobernador por Arriba Chubut': colores["peronismo"], 'A Ignacio Torres gobernador y Gustavo Menna vicegobernador por Juntos por el Cambio': colores["cambiemos"], 'A César Treffinger gobernador y Laura Mirantes vicegobernadora por La Libertad Independiente Chubutense': colores["liberales"], 'A Emilse Saavedra gobernadora y Julieta Rusconi vicegobernadora por el Frente de Izquierda y de los Trabajadores-Unidad': colores["izquierda"], 'A Oscar Petersen gobernador y Nancy Lobos vicegobernadora por el GEN': colores["cambiemos_ucr"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P17_imputada"] = {'A Juan Pablo Luque gobernador por la Alianza Arriba Chubut con el apoyo de Cristina Fernández de Kirchner, Sergio Massa, Alberto Fernández, Mariano Arcioni y el Peronismo': colores["peronismo"], 'A Ignacio Torres gobernador por Juntos por el Cambio con el apoyo de Patricia Bullrich, Horacio Rodríguez Larreta, Mauricio Macri, el PRO y la UCR': colores["cambiemos"], 'A César Treffinger gobernador por La Libertad Independiente Chubutense con el apoyo de Javier Milei': colores["liberales"], 'A Emilse Saavedra gobernadora por el Frente de Izquierda y de los Trabajadores-Unidad con el apoyo de Gabriel Solano y Vilma Ripoll': colores["izquierda"], 'A Oscar Petersen gobernador por el GEN': colores["cambiemos_ucr"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria

# Bloque Control
paletas["P25"] = siNoColorDict