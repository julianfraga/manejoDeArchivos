from especiales.NEUQUEN_5.apps.cuestionario_NEUQUEN_5 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict


paletas = {}

# Bloque Escenarios políticos 
paletas["P06"] = {'José Rioseco': colores["peronismo"], 'Rubén Ojito García': colores["cristianos"], 'Otros candidatos': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P08"] = {'José Rioseco con el apoyo de Ramón Rioseco': colores["peronismo"], 'Rubén Ojito García con el apoyo de Rolo Figueroa': colores["cristianos"], 'Otros candidatos': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P10"] = votaria
paletas["P11"] = votaria

# Bloque Control
paletas["P12"] = siNoColorDict
