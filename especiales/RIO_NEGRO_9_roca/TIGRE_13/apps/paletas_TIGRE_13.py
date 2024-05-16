from especiales.TIGRE_13.apps.cuestionario_TIGRE_13 import cuestionario
from config import colores, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict, internas


paletas = {}


# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict


# Bloque Intención de voto por espacio político 

paletas["P08"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peron1"],
                  'Daniel Scioli a presidente, Victoria Tolosa Paz a gobernadora y Julio Zamora a intendente por Unión por la Patria': colores["peron2"],
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"],
                  'Horacio Rodríguez Larreta a presidente, Diego Santilli a gobernador y Segundo Cernadas a intendente por Juntos por el Cambio': colores["cambiemos3"],
                  'Javier Milei a presidente, Carolina Piparo a gobernadora y Martín Urionagüena a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Wado de Pedro a presidente, Axel Kicillof a gobernador y Malena Galmarini a intendenta por Unión por la Patria': colores["peron1"], 
                  'Patricia Bullrich a presidenta, Néstor Grindetti a gobernador y Nicolás Massot a intendente por Juntos por el Cambio': colores["cambiemos"], 
                  'Javier Milei a presidente, Carolina Piparo a gobernadora y Martín Urionagüena a intendente por la Libertad Avanza': colores["liberales"], 
                  'A los candidatos a presidente, a gobernador y a intendente del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 
                  'No sabe': colores["nosabe"]}

paletas["P14"] = siNoColorDict