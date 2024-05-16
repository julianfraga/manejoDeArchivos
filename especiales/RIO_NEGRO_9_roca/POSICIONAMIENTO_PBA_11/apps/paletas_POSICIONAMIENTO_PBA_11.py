from especiales.POSICIONAMIENTO_PBA_11.apps.cuestionario_POSICIONAMIENTO_PBA_11 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, frecuenciaColorDict, siNoColorDict, internas
import seaborn as sns
# comando:


paletas = {}

# Bloque Preferencias electorales 
paletas["P06"] = {'Unión por la Patria y el peronismo': colores["peronismo"], 
                  'Juntos por el Cambio ': colores["cambiemos"], 
                  'De los Liberales libertarios': colores["liberales"], 
                  'De la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P07"] = internas

paletas["P08"] = internas

# Bloque Escenarios políticos
paletas["P09"] = {'Sergio Massa presidente y Axel Kicillof gobernador por Unión por la Patria': colores["peron1"], 
                  'Wado de Pedro presidente y  Axel Kicillof gobernador por Unión por la Patria': colores["peron2"], 
                  'Daniel Scioli presidente y Victoria Tolosa Paz gobernadora por Unión por la Patria': colores["peron3"], 
                  'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 
                  'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 
                  'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Sergio Massa presidente y Axel Kicillof gobernador por Unión por la Patria': colores["peron1"], 'Wado de Pedro presidente y  Axel Kicillof gobernador por Unión por la Patria': colores["peron2"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P15"] = {'Sergio Massa presidente y Axel Kicillof gobernador por Unión por la Patria': colores["peron1"], 'Daniel Scioli presidente y Victoria Tolosa Paz gobernadora por Unión por la Patria': colores["peron3"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P18"] = {'Wado de Pedro presidente y  Axel Kicillof gobernador por Unión por la Patria': colores["peron2"], 'Daniel Scioli presidente y Victoria Tolosa Paz gobernadora por Unión por la Patria': colores["peron3"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P21"] = {'Sergio Massa presidente y Axel Kicillof gobernador por Unión por la Patria': colores["peron1"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P24"] = {'Wado de Pedro presidente y  Axel Kicillof gobernador por Unión por la Patria': colores["peron2"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P25"] = {'Axel Kicillof presidente y Sergio Massa gobernador por Unión por la Patria': colores["peron1"], 
                  'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 
                  'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 
                  'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P26"] = {'Sergio Massa presidente y Axel Kicillof gobernador por Unión por la Patria': colores["peron1"], 
                  'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 
                  'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"],
                 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Sergio Massa presidente y Axel Kicillof gobernador por Unión por la Patria': colores["peron1"], 
                  'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Wado de Pedro presidente y  Axel Kicillof gobernador por Unión por la Patria': colores["peron2"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Wado de Pedro presidente y  Axel Kicillof gobernador por Unión por la Patria': colores["peron2"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Axel Kicillof presidente y Sergio Massa gobernador por Unión por la Patria': colores["peron1"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Axel Kicillof presidente y Sergio Massa gobernador por Unión por la Patria': colores["peron1"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P32"] = {'Daniel Scioli presidente y Victoria Tolosa Paz gobernadora por Unión por la Patria': colores["peron3"], 'Patricia Bullrich presidenta y Nestor Grindetti gobernador por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Daniel Scioli presidente y Victoria Tolosa Paz gobernadora por Unión por la Patria': colores["peron3"], 'Horacio Rodriguez Larreta presidente y Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei presidente y  Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Axel Kicillof por Unión por la Patria': colores["peron1"], 'Nestor Grindetti por Juntos por el Cambio': colores["cambiemos"], 'Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P35"] = {'Axel Kicillof por Unión por la Patria': colores["peron1"], 'Diego Santilli por Juntos por el Cambio': colores["cambiemos3"], 'Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P36"] = {'Sergio Massa por Unión por la Patria': colores["peron2"], 'Nestor Grindetti por Juntos por el Cambio': colores["cambiemos"], 'Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P37"] = {'Sergio Massa por Unión por la Patria': colores["peron2"], 'Diego Santilli por Juntos por el Cambio': colores["cambiemos3"], 'Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P38"] = {'Victoria Tolosa Paz por Unión por la Patria': colores["peron3"], 'Nestor Grindetti por Juntos por el Cambio': colores["cambiemos"], 'Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P39"] = {'Victoria Tolosa Paz por Unión por la Patria': colores["peron3"], 'Diego Santilli por Juntos por el Cambio': colores["cambiemos3"], 'Guillermo Britos por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P40"] = votaria
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria
paletas["P44"] = votaria

# Bloque Imagen
paletas["P45"] = opinionColorDict
paletas["P46"] = opinionColorDict
paletas["P47"] = opinionColorDict
paletas["P48"] = opinionColorDict
paletas["P49"] = opinionColorDict

# Control
paletas['P50'] = frecuenciaColorDict
paletas['P51'] = siNoColorDict