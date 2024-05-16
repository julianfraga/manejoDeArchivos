from especiales.POSICIONAMIENTO_PBA_10.apps.cuestionario_POSICIONAMIENTO_PBA_10 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, diverging, diverging_reverse, internas
import seaborn as sns
# comando:


paletas = {}

paletas["P06"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
 'De Juntos por el cambio': colores["cambiemos"],
 'De los Liberales libertarios': colores["liberales"],
 'De la Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]
}

paletas["P07"] = internas

paletas["P08"] = internas

paletas["P09"] = internas

paletas["P10"] = {'Sergio Massa a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Diego Santilli a Gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P11"] = {'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'Sergio Massa a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Joaquín De La Torre a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes a presidente y Maximiliano Abad a gobernador por Juntos por el Cambio': colores["cambiemos3"],
 'Gerardo Morales a presidente y su candidato a gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P12"] = {'Agustín Rossi  a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Joaquín De La Torre a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes a presidente y Maximiliano Abad a gobernador por Juntos por el Cambio': colores["cambiemos3"],
 'Gerardo Morales a presidente y su candidato a gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P16"] = {'Daniel Scioli a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Joaquín De La Torre a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes a presidente y Maximiliano Abad a gobernador por Juntos por el Cambio': colores["cambiemos3"],
 'Gerardo Morales a presidente y su candidato a gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P17"] = {'Axel Kicillof a presidente y Sergio Massa a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P18"] = {'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'Axel Kicillof a presidente y Sergio Massa a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y José Luis Espert a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P19"] = {'Sergio Massa a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y José Luis Espert a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos2"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P20"] = {'Sergio Massa a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P23"] = {'Daniel Scioli a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P24"] = {'Sergio Massa a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P27"] = {'Daniel Scioli a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P28"] = {'Agustín Rossi a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P29"] = {'Agustín Rossi a presidente y Axel Kicillof a gobernador por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P30"] = {'Axel Kicillof a presidente y Sergio Massa a gobernador por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich a presidenta y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P33"] = {'Axel Kicillof a presidente y Sergio Massa a gobernador por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta a presidente y Diego Santilli a gobernador por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei a presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
 'A los candidatos a presidente y a gobernador del Frente de Izquierda': colores["izquierda"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P34"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P35"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P36"] = {'Horacio Rodriguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por la Libertad Avanza': colores["liberales"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P37"] = {'Javier Milei por la Libertad Avanza': colores["liberales"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P38"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Horacio Rodriguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P39"] = {'Agustín Rossi por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P40"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]
}

paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P43"] = votaria
paletas["P44"] = votaria
paletas["P45"] = votaria
paletas["P46"] = votaria
paletas["P47"] = votaria
paletas["P48"] = votaria
