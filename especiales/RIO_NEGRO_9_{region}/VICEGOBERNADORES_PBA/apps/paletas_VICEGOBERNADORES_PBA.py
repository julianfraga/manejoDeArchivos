from especiales.VICEGOBERNADORES_PBA.apps.cuestionario_VICEGOBERNADORES_PBA import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict


paletas = {}
# Bloque Intención de voto por espacio político 

# Bloque Vicegobernadores
paletas["P04"] = frecuenciaColorDict

paletas["P05"] = muchoPocoColorDict

paletas["P07"] = {'Néstor Grindetti a gobernador y Maximiliano Abad a vicegobernador por Juntos por el Cambio.': colores["cambiemos"], 
                  'Diego Santilli a gobernador y su candidato a vicegobernador por Juntos por el Cambio.': colores["cambiemos2"], 
                  'Axel Kicillof a gobernador y Verónica Magario a vicegobernadora por el Frente de Todos.': colores["peronismo"],
                    'A Guillermo Britos a gobernador y su candidato a vicegobernador por La Libertad Avanza.': colores["liberales"],
                      'A los candidatos a gobernador y vicegobernador por el Frente de Izquierda.': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P10"] = {'Néstor Grindetti a gobernador y Joaquín De La Torre a vicegobernador por Juntos por el Cambio.': colores["cambiemos"],
                   'Diego Santilli a gobernador y su candidato a vicegobernador por Juntos por el Cambio.': colores["cambiemos2"],
                     'Axel Kicillof a gobernador y Verónica Magario a vicegobernadora por el Frente de Todos.': colores["peronismo"], 
                     'A Guillermo Britos a gobernador y su candidato a vicegobernador por La Libertad Avanza.': colores["liberales"],
                       'A los candidatos a gobernador y vicegobernador por el Frente de Izquierda.': colores["izquierda"], 
                       'No sabe': colores["nosabe"]}

paletas["P13"] = {'Néstor Grindetti a gobernador y Fernando Burlando a vicegobernador por Juntos por el Cambio.': colores["cambiemos"],
                   'Diego Santilli a gobernador y su candidato a vicegobernador por Juntos por el Cambio.': colores["cambiemos2"],
                     'Axel Kicillof a gobernador y Verónica Magario a vicegobernadora por el Frente de Todos.': colores["peronismo"], 
                     'A Guillermo Britos a gobernador y su candidato a vicegobernador por La Libertad Avanza.': colores["liberales"],
                       'A los candidatos a gobernador y vicegobernador por el Frente de Izquierda.': colores["izquierda"], 
                       'No sabe': colores["nosabe"]}

paletas["P16"] = {'Néstor Grindetti a gobernador y Maximiliano Abad a vicegobernador por Juntos por el Cambio.': colores["cambiemos"],
                   'Diego Santilli a gobernador y su candidato a vicegobernador por Juntos por el Cambio.': colores["cambiemos2"],
                     'Axel Kicillof a gobernador y Malena Galmarini a vicegobernadora por el Frente de Todos.': colores["peronismo"], 
                     'A Guillermo Britos a gobernador y su candidato a vicegobernador por La Libertad Avanza.': colores["liberales"], 
                     'A los candidatos a gobernador y vicegobernador por el Frente de Izquierda.': colores["izquierda"],
                       'No sabe': colores["nosabe"]}

paletas["P19"] = {'Néstor Grindetti a gobernador y Joaquín De La Torre a vicegobernador por Juntos por el Cambio.': colores["cambiemos"], 
                  'Diego Santilli a gobernador y su candidato a vicegobernador por Juntos por el Cambio.': colores["cambiemos2"], 
                  'Axel Kicillof a gobernador y Malena Galmarini a vicegobernadora por el Frente de Todos.': colores["peronismo"],
                    'A Guillermo Britos a gobernador y su candidato a vicegobernador por La Libertad Avanza.': colores["liberales"], 
                    'A los candidatos a gobernador y vicegobernador por el Frente de Izquierda.': colores["izquierda"], 
                    'No sabe': colores["nosabe"]}


# Bloque Reach candidatos a gobernador y vicegobernador
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria
paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = siNoColorDict