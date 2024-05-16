from especiales.HURLINGHAM_1.apps.cuestionario_HURLINGHAM_1 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, internas


paletas = {}
# Bloque Intención de voto por espacio político 

# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict


# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria y el peronismo': colores["peronismo"], 
                  'Juntos por el Cambio': colores["cambiemos"], 
                  'De los Liberales libertarios': colores["liberales"],
                    'De la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P09"] = {'A Sergio Massa': colores["peronismo"], 'A Daniel Scioli': colores["peron2"], 
                  'A algún candidato del peronismo': colores["otros"], 'Wado de Pedro': colores["peron4"]}

paletas["P10"] = {'A Horacio Rodriguez Larreta': colores["cambiemos3"], 'A Patricia Bullrich': colores["cambiemos"],
                   'A Facundo Manes': colores["cambiemos_ucr"], 'A Gerardo Morales': colores["cambiemos2"]}

# Bloque Escenarios políticos 
paletas["P11"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peron1"],
                   'Wado de Pedro a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peron2"], 
                   'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 
                   'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos3"], 
                   'Javier Milei a presidente, Carolina Piparo a gobernadora y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 
                   'Al candidato a presidente, a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"],
                     'No sabe': colores["nosabe"]}

paletas["P13"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Damián Selci a intendente por Unión por la Patria': colores["peron2"], 
                  'Wado de Pedro a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peron1"],
                    'Daniel Scioli a presidente, Victoria Tolosa Paz gobernadora y su candidato a intendente por Unión por la Patria': colores["peron3"], 'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Al candidato a presidente, a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P14"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peron1"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"],
                    'Javier Milei a presidente, Carolina Piparo a gobernadora y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 
                    'Al candidato a presidente, a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peron1"],
                   'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos3"], 
                   'Javier Milei a presidente, Carolina Piparo a gobernadora y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Al candidato a presidente, a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], ' En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P16"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Damian Selci a intendente por Unión por la Patria': colores["peron2"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 
                  'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 
                  'Al candidato a presidente, a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P17"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Damian Selci a intendente por Unión por la Patria': colores["peron2"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei a presidente, Carolina Piparo a gobernadora  y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Al candidato a presidente, a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P18"] = {'Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peron1"], 
                  'Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 
                  'Carolina Piparo a gobernadora y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 
                  'Al candidato a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P19"] = {'Axel Kicillof a gobernador y Juan Zabaleta a intendente por Unión por la Patria': colores["peron1"], 
                  'Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos3"], 
                  'Carolina Piparo a gobernadora y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 
                  'Al candidato a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P20"] = {'Axel Kicillof a gobernador y Damian Selci a intendente por Unión por la Patria': colores["peron2"], 
                  'Néstor Grindetti a gobernador y Andrea Giorgini a intendenta por Juntos por el Cambio': colores["cambiemos"], 
                  'Carolina Piparo a gobernadora y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Al candidato a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P21"] = {'Axel Kicillof a gobernador y Damian Selci a intendente por Unión por la Patria': colores["peron2"], 
                  'Diego Santilli a gobernador y Lucas Delfino a intendente por Juntos por el Cambio': colores["cambiemos3"],
                    'Carolina Piparo a gobernadora y Rafael De Francesco a intendente por la Libertad Avanza': colores["liberales"], 'Al candidato a gobernador y Alejandro Chayán a intendente por el Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

# Bloque Reach candidatos
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria
paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = votaria
paletas["P32"] = votaria
paletas["P33"] = votaria
paletas["P34"] = votaria
paletas["P35"] = votaria
paletas["P36"] = votaria
paletas["P37"] = votaria
paletas["P38"] = votaria

# Bloque Control
paletas["P39"] = siNoColorDict