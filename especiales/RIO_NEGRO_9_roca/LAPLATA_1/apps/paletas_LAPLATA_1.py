from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, internas

# comando:

paletas = {}
# Bloque Control
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 
                  'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 
                  'Hacemos por nuestro país': colores["peronismo_nok"], 'Otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos 
paletas["P09"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Julio Alak a intendente por Unión por la Patria': colores["peronismo"], 
                  'Sergio Massa a presidente, Axel Kicillof a gobernador y Guillermo Escudero a intendente por Unión por la Patria': colores["peronismo2"], 
                  'Sergio Massa a presidente, Axel Kicillof a gobernador y Gaston Castagneto a intendente por Unión por la Patria': colores["peronismo3"], 
                  'Juan Grabois a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo4"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Juan Pablo Allan a intendente por Juntos por el Cambio': colores["cambiemos"],
                'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Julio Garro a intendente por Juntos por el Cambio': colores["cambiemos2"], 
                'Javier Milei a presidente, Carolina Piparo a gobernadora y Luciano Guma a intendente por la Libertad Avanza': colores["liberales"], 
                'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                'Otro': colores["otros"],'No sabe': colores["nosabe"]}

paletas["P12"] = siNoColorDict
paletas["P13"] = {'Julio Alak a intendente por Unión por la Patria': colores["peronismo"], 
                  'Guillermo Escudero a intendente por Unión por la Patria': colores["peronismo2"], 
                  'Gaston Castagneto a intendente por Unión por la Patria': colores["peronismo3"], 
                  'Juan Pablo Allan a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Garro a intendente por Juntos por el Cambio': colores["cambiemos2"], 
                  'Luciano Guma a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a intendente del Frente de Izquierda': colores["izquierda"], 'Otro': colores["otros"],
                  'No sabe': colores["nosabe"]}

paletas["P16"] = {'Ninguno': '#f05d93', 'Julio Alak a intendente por Unión por la Patria': colores["peronismo"], 
                  'Guillermo Escudero a intendente por Unión por la Patria': colores["peronismo2"], 
                  'Gaston Castagneto a intendente por Unión por la Patria': colores["peronismo3"], 
                  'Juan Pablo Allan a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Garro a intendente por Juntos por el Cambio': colores["cambiemos2"], 
                  'Luciano Guma a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a intendente del Frente de Izquierda': colores["izquierda"], 
                  'Otro': colores["otros"],'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach candidatos
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria

# Bloque Control
paletas["P26"] = siNoColorDict

paletas["INTENDENTE"] = {'Julio Alak a intendente por Unión por la Patria': colores["peronismo"], 
                  'Guillermo Escudero a intendente por Unión por la Patria': colores["peronismo2"], 
                  'Gaston Castagneto a intendente por Unión por la Patria': colores["peronismo3"], 
                  'Juan Pablo Allan a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Garro a intendente por Juntos por el Cambio': colores["cambiemos2"], 
                  'Luciano Guma a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a intendente del Frente de Izquierda': colores["izquierda"],
                   'En blanco': colores["blanco"],'Otro': colores["otros"], 'No sabe': colores["nosabe"]}


paletas["PRESIDENTE"] ={'Sergio Massa a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo"], 
                  'Juan Grabois a presidente, Axel Kicillof a gobernador por Unión por la Patria': colores["peronismo2"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador por Juntos por el Cambio': colores["cambiemos"],
                'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"], 
                'Javier Milei a presidente, Carolina Piparo a gobernadora por la Libertad Avanza': colores["liberales"], 
                'A los candidatos a presidente, a gobernador del Frente de Izquierda': colores["izquierda"], 
                'En blanco': colores["blanco"],'Otro': colores["otros"],'No sabe': colores["nosabe"]}