from especiales.POSICIONAMIENTO_CBA_2.apps.cuestionario_POSICIONAMIENTO_CBA_2 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, frecuenciaColorDict

# comando:


paletas = {}
# Bloque Sociodemográfico
colores['encuentroVecinal'] = '#ff570f'
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Escenarios políticos provinciales
paletas["P08"] = {'A Martín Llaryora gobernador y Myrian Prunotto vicegobernadora por Hacemos Unidos por Córdoba': colores["peron3"],
                'A Luis Juez gobernador y Marcos Carasso vicegobernador por Juntos por el Cambio': colores["cambiemos"], 
                'A Agustín Spaccesi gobernador y Cristina Lagger vicegobernadora por La Libertad Avanza': colores["liberales"],
                'A Federico Alesandri gobernador y Gabriela Estévez vicegobernadora por Creo en Córdoba de Todos': colores["peron1"], 
                'A Aurelio García Elorrio gobernador y María Rosa Marcone vicegobernadora por Encuentro Vecinal Córdoba': colores["encuentroVecinal"],
                'A Rodolfo Eiben gobernador y Gabriel Bornoroni vicegobernador por el Frente Liberal Demócrata Desarrollista': colores["liberales2"],
                'A Liliana Olivero gobernadora y Soledad Díaz vicegobernadora por el Frente de Izquierda y de Trabajadores-Unidad': colores["izquierda"],
                'A los candidatos de otros partidos políticos': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P08_imputadas"] = paletas["P08"]
# Bloque Escenarios políticos locales
paletas["P10"] = {'A Daniel Passerini intendente y Javier Pretto viceintendente por Hacemos Unidos Por Córdoba': colores["peron3"],
                   'A Rodrigo de Loredo intendente y Soher el Sukaria viceintendenta por Juntos por el Cambio': colores["cambiemos"], 
                   'A Verónica Sikora intendenta y Enrique Rigatuso viceintendente por La Libertad Primero': colores["liberales"],
                    'A Juan Pablo Quinteros intendente y Gabriel Ratner viceintendente por Somos Córdoba': colores["peron2"], 
                    'A Jorge Scala intendente y Paola Janett González Cuevas viceintendenta por el Partido Demócrata': colores["liberales2"],
                    'A Humberto Spaccesi intendente y Silvia Peñaloza viceintendenta por Córdoba de Todos': colores["peron1"], 
                    'A César Orgaz intendente y Gonzalo Frontera viceintendente por Encuentro Vecinal Córdoba': colores["encuentroVecinal"],
                    'A Laura Vilches intendenta y Virginia Caldera Marsengo viceintendenta por El Frente De Izquierda y De Trabajadores-Unidad': colores["izquierda"], 
                    'A los candidatos de otros partidos políticos': colores["otros"], 'No sabe': colores["nosabe"]}
paletas["P10_imputadas"] = paletas["P10"]
paletas["P12"] = siNoColorDict