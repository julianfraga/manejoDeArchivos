from especiales.POSICIONAMIENTO_NACIONAL_10.apps.cuestionario_POSICIONAMIENTO_NACIONAL_10 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, diverging, diverging_reverse, internas
import seaborn as sns
# comando:


paletas = {}
paletas["P06"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
 'De Juntos por el cambio': colores["cambiemos"],
 'De los Liberales libertarios': colores["liberales"],
 'De la Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P07"] = internas
paletas["P08"] = internas
paletas["P09"] = internas

paletas["P06"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
 'De Juntos por el cambio': colores["cambiemos"],
 'De los Liberales libertarios': colores["liberales"],
 'De la Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P10"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos2"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos1"],
 'Sergio Massa  por el Frente de Todos': colores["peronismo"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos3"],
 'Gerardo Morales por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Agustín Rossi  por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos1"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos3"],
 'Gerardo Morales': colores["cambiemos_ucr"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P16"] = {'Daniel Scioli  por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos3"],
 'Gerardo Morales': colores["cambiemos_ucr"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P17"] = {'Axel Kicillof por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos2"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P18"] = {'Sergio Massa  por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P21"] = {'Daniel Scioli  por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P22"] = {'Sergio Massa  por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P25"] = {'Agustín Rossi  por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P26"] = {'Axel Kicillof por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Horacio Rodriguez Larreta por el Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P32"] = {'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Horacio Rodriguez Larreta por el Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Agustín Rossi por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P35"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}

paletas["P36"] = votaria
paletas["P37"] = votaria
paletas["P38"] = votaria
paletas["P39"] = votaria
paletas["P40"] = votaria
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria