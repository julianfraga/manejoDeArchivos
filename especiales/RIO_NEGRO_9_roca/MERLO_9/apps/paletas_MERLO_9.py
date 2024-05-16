from especiales.MERLO_9.apps.cuestionario_MERLO_9 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, qualitative_strong

paletas = {}
paletas["P05"] = {'A Gustavo Menéndez por el Frente de Todos': colores["peronismo"],
                  'A David Zencich por Juntos por el Cambio': colores["cambiemos"],
                  'A Osvaldo Martino por Consenso Federal': colores["otros"],
                  'A Cristian Franco por el Frente de Izquierda': colores["izquierda"],
                  'A otro candidato': colores["otros"]}

paletas["P06"] = {'Al candidato del Frente de Todos': colores["peronismo"],
                  'Al candidato de Juntos por el Cambio': colores["cambiemos"],
                  'Al candidato de la Izquierda': colores["izquierda"],
                  'A otro candidato': colores["otros"],
                  'No sabe': colores["nosabe"]}

paletas["P07"] = {'A Gustavo Menéndez': colores["peronismo1"],
                  'A Karina Menéndez': colores["peronismo2"],
                  'A Florencia Lizaraso': colores["otros"],
                  'No sabe': colores["nosabe"]}

paletas["P08"] = {'A Gustavo Menéndez por el Frente de Todos': colores["peronismo1"],
                'A Raúl Othacehé por el Frente de Todos': colores["peronismo2"], 
                'A David Zencich por Juntos por el Cambio': colores["cambiemos1"],
                'A Pablo Cocuzza por Juntos por el Cambio': colores["cambiemos2"],
                'Al candidato de Javier Milei por La Libertad Avanza': colores["liberales"],
                'Al candidato del Frente de Izquierda': colores["izquierda"],
                'En blanco': colores["blanco"],
                'No sabe': colores["nosabe"]}

paletas["P10"] = {'A Gustavo Menéndez por el Frente de Todos': colores["peronismo1"],
                'A Raúl Othacehé por un partido vecinal': colores["otros"],
                'A David Zencich por Juntos por el Cambio': colores["cambiemos1"],
                'A Pablo Cocuzza por Juntos por el Cambio': colores["cambiemos2"],
                'Al candidato de Javier Milei por La Libertad Avanza': colores["liberales"],
                'Al candidato del Frente de Izquierda': colores["izquierda"],
                'En blanco': colores["blanco"],
                'No sabe': colores["nosabe"]}

paletas["P12"] = votaria
paletas["P13"] = votaria
paletas["P14"] = votaria
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria

paletas["P20"] = list2dictPalette(['La seguridad', 'El tránsito', 'El arreglo de las calles', 'El estado de las escuelas y la educación', 'El sistema de salud', 'El deporte y la cultura', 'La obra pública', 'La luminaria', 'No sabe'], 
                                  qualitative_strong, noSabe=True)

paletas["P21"] = list2dictPalette(['La seguridad', 'El tránsito', 'El arreglo de las calles', 'El estado de las escuelas y la educación', 'El sistema de salud', 'El deporte y la cultura', 'La obra pública', 'La luminaria', 'No sabe'],
                                   qualitative_strong, noSabe=True)

paletas["P22"] = list2dictPalette(['Agua corriente y cloacas', 'Energía eléctrica', 'Red de gas natural', 'Recolección de residuos', 'Ninguno'], 
                                  qualitative_strong, noSabe=False)

paletas["P23"] = list2dictPalette(['Los robos', 'El narcotráfico', 'La ausencia de patrulleros y personal policial', 'Otro', 'Ninguno'], 
                                  qualitative_strong, noSabe=False)



paletas["P24"] = opinionColorDict


paletas["P25"] = opinionColorDict

paletas["P26"] = opinionColorDict
paletas["P27"] = opinionColorDict
paletas["P28"] = opinionColorDict
paletas["P29"] = opinionColorDict
paletas["P30"] = opinionColorDict
paletas["P31"] = opinionColorDict
paletas["P32"] = opinionColorDict
paletas["P33"] = opinionColorDict
paletas["P34"] = opinionColorDict
paletas["P35"] = opinionColorDict
paletas["P36"] = opinionColorDict
paletas["P37"] = opinionColorDict
paletas["P38"] = opinionColorDict
paletas["P39"] = opinionColorDict
paletas["P40"] = opinionColorDict
