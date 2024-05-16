from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P09"] = frecuenciaColorDict

# Bloque Bloque Intención de voto
paletas["P10"] = {'Camau Espinola por Unión por la patria': colores["peronismo"], 
                  'German Brailard por Unión por la patria': colores["peronismo2"], 
                  'Juan Pablo Valdes por Juntos por el cambio': colores["cambiemos"], 
                  'Eduardo Tassano por Juntos por el cambio': colores["cambiemos2"], 
                  'Pitin Aragon por Unión por la patria': colores["peronismo3"], 
                  'Tincho Ascua por Unión por la patria': colores["peronismo4"], 
                  'Emiliano Fernandez por Unión por la patria': colores["peronismo5"],
                    'Ricardo Colombi por Juntos por el cambio': colores["cambiemos3"], 
                    'Noelia Bassi por Juntos por el cambio': colores["cambiemos4"], 
                    'No sabe': colores["nosabe"]}

paletas["P14"] = votaria
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria

# Bloque Bloque General
paletas["P23"] = opinionColorDict
paletas["P24"] = opinionColorDict
paletas["P25"] = {'El gobierno nacional':colores['liberales_contraste'], 'El gobierno provincial': colores["cambiemos"], 'No sabe': colores["nosabe"]}
paletas["P26"] = {'El gobierno nacional':colores['liberales_contraste'], 'El gobierno provincial': colores["cambiemos"], 'No sabe': colores["nosabe"]}
# Bloque Imagen de dirigentes
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