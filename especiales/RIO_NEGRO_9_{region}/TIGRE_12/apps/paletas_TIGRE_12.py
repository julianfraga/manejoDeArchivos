from especiales.TIGRE_12.apps.cuestionario_TIGRE_12 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, qualitative_strong



paletas = {}
# Bloque Intención de voto por espacio político 

paletas["P07"] = {'Al candidato del Frente de Todos': colores["peronismo"],
                  'Al candidato de Juntos por el Cambio': colores["cambiemos"],
                  'Al candidato de los liberales - libertarios': colores["liberales"],
                  'Al candidato de la Izquierda': colores["izquierda"],
                  'A otro candidato': colores["otros"],
                  'No sabe': colores["nosabe"]}

paletas["P08"] = list2dictPalette(['A Malena Galmarini','A Julio Zamora'], qualitative_strong, noSabe=False)

paletas["P09"] = list2dictPalette(['A Segundo Cernadas', 'A Nicolás Massot'], qualitative_strong, noSabe=False)

paletas["P10"] = {'A Malena Galmarini por el Frente de Todos': colores["peronismo"],
                  'A Julio Zamora por el Frente de Todos': colores["peronismo2"],
                  'A Segundo Cernadas por Juntos por el Cambio': colores["cambiemos"],
                  'A Nicolás Massot por Juntos por el Cambio': colores["cambiemos2"],
                  'Al candidato de los liberales libertarios': colores["liberales"],
                  'A Paula Akerfeld por el Frente de Izquierda': colores["izquierda"],
                  'No sabe': colores["nosabe"]}

paletas["P12"] = {'A Julio Zamora por el Frente de Todos': colores["peronismo"],
                  'A Segundo Cernadas por Juntos por el Cambio': colores["cambiemos"], 
                  'Al candidato de los liberales libertarios': colores["liberales"],
                  'A Paula Akerfeld por el Frente de Izquierda': colores["izquierda"], 
                  'No sabe': colores["nosabe"]}

paletas["P14"] = {'A Malena Galmarini por el Frente de Todos': colores["peronismo"],
                  'A Segundo Cernadas por Juntos por el Cambio': colores["cambiemos"],
                  'Al candidato de los liberales libertarios': colores["liberales"],
                  'A Paula Akerfeld por el Frente de Izquierda': colores["izquierda"], 
                  'No sabe': colores["nosabe"]}

paletas["P16"] = {'A Malena Galmarini por el Frente de Todos': colores["peronismo"], 
                  'A Segundo Cernadas por Juntos por el Cambio': colores["cambiemos"], 
                  'A Nicolás Massot por Juntos por el Cambio': colores["cambiemos2"], 
                  'A Julio Zamora por un partido vecinal': colores["otros"], 
                  'Al candidato de los liberales libertarios': colores["liberales"], 
                  'A Paula Akerfeld por el Frente de Izquierda': colores["izquierda"], 
                  'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos municipales en elecciones unificadas
paletas["P18"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                  'Daniel Scioli a presidente, Victoria Tolosa Paz a gobernadora y Julio Zamora a intendente por el Frente de Todos': colores["peronismo"],
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"],
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"],
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"],
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P19"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"],
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"],
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"],
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P20"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                   'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 
                    'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                    'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                    'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P21"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"],
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"],
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P23"] = {'Sergio Massa a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"], 
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P24"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Daniel Scioli a presidente, Victoria Tolosa Paz a gobernadora y Julio Zamora a intendente por el Frente de Todos': colores["peronismo2"],
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"],
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P25"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos2"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"], 
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P26"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"],
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"],
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"], 
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"],
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                   'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                   'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"],
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"],
                  'Javier Milei a presidente, su candidato a gobernador y su candidato a intendente por la Libertad Avanza': colores["liberales"],
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Escenarios políticos municipales en elecciones desdobladas
paletas["P30"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos2"], 
                  'Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"],
                  'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                   'Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                   'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P32"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                   'Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'Julio Zamora a intendente por un partido vecinal': colores["otros"], 
                   'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"],
                   'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                  'Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"],
                  'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"],
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P35"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                  'Victoria Tolosa Paz a gobernadora y Julio Zamora a intendente por el Frente de Todos': colores["peronismo2"],
                  'Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos2"],
                  'Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"],
                  'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"],
                  'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P36"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos2"], 
                  'Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"], 
                  'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P37"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"],
                    'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                    'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P38"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Julio Zamora a intendente por un partido vecinal': colores["otros"],
                    'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                    'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P39"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"],
                   'Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                   'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                   'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P40"] = {'Axel Kicillof a gobernador y Malena Galmarini a intendenta por el Frente de Todos': colores["peronismo"], 
                  'Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"],
                    'Julio Zamora a intendente por un partido vecinal': colores["otros"], 
                    'A los candidatos a gobernador y a intendente de la Libertad Avanza': colores["liberales"], 
                    'A los candidatos a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 
                    'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Imagen de dirigentes locales
paletas["P41"] = opinionColorDict
paletas["P42"] = opinionColorDict
paletas["P43"] = opinionColorDict
paletas["P44"] = opinionColorDict

# Bloque Gestión municipal
paletas["P45"] = opinionColorDict
paletas["P45"] = opinionColorDict
paletas["P46"] = list2dictPalette(['Que continúe el intendente Julio Zamora', 'Que continúe Julio Zamora pero con mejoras', 'Que cambie Julio Zamora pero que se mantengan los avances', 'Que cambie el intendente Julio Zamora'], qualitative_strong, noSabe=False)
paletas["P47"] = list2dictPalette(['Es kirchnerista', 'Forma parte del Frente de Todos', 'Es un hombre de Massa', 'Es un peronista independiente de centro', 'Es un oportunista y está donde le conviene', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P48"] = list2dictPalette(['El tránsito', 'El arreglo de las calles', 'Los parques y espacios públicos', 'El sistema de salud', 'La limpieza de las calles', 'El deporte y la cultura', 'La obra pública', 'La luminaria', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P49"] = list2dictPalette(['El tránsito', 'El arreglo de las calles', 'Los parques y espacios públicos', 'El sistema de salud', 'La limpieza de las calles', 'El deporte y la cultura', 'La obra pública', 'La luminaria', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P50"] = list2dictPalette(['Agua corriente y cloacas', 'Energía eléctrica', 'Red de gas natural', 'Recolección de residuos', 'Ninguno'], qualitative_strong, noSabe=True)
paletas["P51"] = list2dictPalette(['Los robos', 'El narcotráfico', 'La ausencia de patrulleros y personal policial', 'Otro', 'Ninguno'], qualitative_strong, noSabe=True)

# Bloque Imagen de dirigentes nacionales
paletas["P52"] = opinionColorDict
paletas["P53"] = opinionColorDict
paletas["P54"] = opinionColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = opinionColorDict
paletas["P57"] = opinionColorDict
paletas["P58"] = opinionColorDict
paletas["P59"] = opinionColorDict
paletas["P60"] = opinionColorDict
paletas["P61"] = opinionColorDict
paletas["P62"] = opinionColorDict