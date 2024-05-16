from especiales.SAN_MARTIN_2.apps.cuestionario_SAN_MARTIN_2 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, internas


paletas = {}
# Bloque Intención de voto por espacio político 

# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P08"] = {'Unión por la Patria y el peronismo': colores["peronismo"], 'Juntos por el Cambio': colores["cambiemos"], 
                  'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P09"] = {'A Sergio Massa': colores["peronismo"], 'A Daniel Scioli': colores["peron2"], 
                  'A algún candidato del peronismo': colores["otros"], 'Wado de Pedro': colores["peron4"]}

paletas["P10"] = {'A Horacio Rodriguez Larreta': colores["cambiemos3"], 'A Patricia Bullrich': colores["cambiemos"],
                   'A Facundo Manes': colores["cambiemos_ucr"], 'A Gerardo Morales': colores["cambiemos2"]}


# Bloque Escenarios políticos 
paletas["P11"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"],
                   'A Leonardo Grosso a intendente por Unión por la Patria': colores["peron2"], 
                   'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"],
                    'No sabe': colores["nosabe"]}

paletas["P13"] = {'Axel Kicillof a presidente, Sergio Massa a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'A Leonardo Grosso a intendente por Unión por la Patria': colores["peron2"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"],
                    'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                      'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                      'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 
                      'No sabe': colores["nosabe"]}

paletas["P15"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'A Leonardo Grosso a intendente por Unión por la Patria': colores["peron2"],
                    'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 
                    'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                      'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                      'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                      'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P17"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"],
                   'Daniel Scioli a presidente, Victoria Tolosa Paz gobernadora y  Leonardo Grosso a intendente por Unión por la Patria': colores["peron2"], 
                   'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos2"],
                     'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                     'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 
                     'No sabe': colores["nosabe"]}

paletas["P19"] = {'Axel Kicillof a presidente, Sergio Massa a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"],
                   'Daniel Scioli a presidente, Victoria Tolosa Paz gobernadora y  Leonardo Grosso a intendente por Unión por la Patria': colores["peron2"], 
                   'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"],
                     'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                       'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P21"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Daniel Scioli a presidente, Victoria Tolosa Paz gobernadora y  Leonardo Grosso a intendente por Unión por la Patria': colores["peron2"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"],
                    'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                      'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                        'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                        'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"],
                    'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"],
                      'No sabe': colores["nosabe"]}

paletas["P23"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"],
                      'No sabe': colores["nosabe"]}

paletas["P24"] = {'Axel Kicillof a presidente, Sergio Massa gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"],
                   'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                     'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P25"] = {'Axel Kicillof a presidente, Sergio Massa gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"],
                      'No sabe': colores["nosabe"]}

paletas["P26"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                    'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                    'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei a presidente, Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"],
                      'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Sergio Massa a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Sergio Massa a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"], 
                  'Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"], 
                  'Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"],
                   'Néstor Grindetti a gobernador y Santiago López Medrano a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                     'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Axel Kicillof a gobernador y Fernando Moreira a intendente por Unión por la Patria': colores["peronismo"],
                   'Diego Santilli a gobernador y Mauricio D’Alessandro a intendente por Juntos por el Cambio': colores["cambiemos3"],
                     'Guillermo Britos a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                       'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

# Bloque Reach de candidatos
paletas["P32"] = votaria
paletas["P33"] = votaria
paletas["P34"] = votaria
paletas["P35"] = votaria
paletas["P36"] = votaria
paletas["P37"] = votaria
paletas["P38"] = votaria
paletas["P39"] = votaria
paletas["P40"] = votaria
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria
paletas["P44"] = votaria
paletas["P45"] = votaria
paletas["P46"] = votaria

paletas["P47"] = siNoColorDict