from especiales.MORON_1.apps.cuestionario_MORON_1 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, qualitative_strong
paletas = {}



paletas["P07"] =  {'Del Frente de Todos y el peronismo': colores["peronismo"],
                  'De Cambiemos': colores["cambiemos"],
                  'De los Liberales libertarios': colores["liberales"],
                  'De la Izquierda': colores["izquierda"],
                  'No sabe': colores["nosabe"]}


paletas["P09"] =  {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
    "A Cristina Fernández de Kirchner": colores['peron1'],
}

paletas["P10"] =  {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
    "A Cristina Fernández de Kirchner": colores['peron1'],
}


paletas["P11"] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Patricia Bullrich": colores['cambiemos1'],
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros'],
    "Martin Lousteau":" #e0976e"
}

paletas["P12"] = votaria


paletas["P13"] = votaria


paletas["P14"] = votaria


paletas["P15"] = votaria


paletas["P16"] = votaria


paletas["P17"] = votaria

paletas["P18"] = {'Lucas Ghi con el  apoyo de Axel Kicillof y Cristina Fernández de Kirchner por el Frente de Todos': colores["peronismo"],
 'A Martin Marinucci con el apoyo de Axel Kicillof y Sergio Massa  por el Frente de Todos': colores["peronismo2"],
 'A Ramiro Tagliaferro con el  apoyo de Horacio Rodríguez Larreta y Mauricio Macri por Juntos por el Cambio': colores["cambiemos1"],
 'A Analía Zapulla con el apoyo  de Patricia Bullrich y Mauricio Macri por Juntos por el Cambio': colores["cambiemos2"],
 'Al candidato de José Luis Espert por Juntos por el Cambio': colores["cambiemos3"],
 'A Roly Moretto con el apoyo de Facundo Manes por Juntos por el Cambio': colores["cambiemos_ucr"],
 'A Ariel Diguan con el apoyo de Javier Milei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P19"] = {'A Scioli Presidente, Kiciloff Gobernador y Lucas Ghi Intendente por el Frente de Todos': colores["peronismo1"],
 'A Scioli Presidente, Kiciloff Gobernador y  Martin Marinucci Intendente por el Frente de Todos': colores["peronismo2"],
 'A Horacio Rodríguez Larreta Presidente, Santilli Gobernador y Ramiro Tagliaferro Intendente por Juntos por el Cambio': colores["cambiemos1"],
 'A Patricia Presidenta, Joaquín De la Torre Gobernador y Analia Zapulla Intendenta por Juntos por el Cambio': colores["cambiemos2"],
 'A Javier Millei Presidente, su candidato a Gobernador y Ariel Diguan Intendente por la Libertad Avanza': colores["liberales"],
 'A los candidatos a Presidente, Gobernador e Intendente del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P20"] = {'A Lucas Ghi con el  apoyo de Axel Kicilof, Cristina Fernández de Kirchner, Sergio Massa y Alberto Fernández por el Frente de Todos': colores["peronismo"],
 'A Ramiro Tagliaferro con el  apoyo de Horacio Rodríguez Larreta, Mauricio Macri y Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'A Ariel Diguan con el apoyo de Javier Millei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P21"] = {'A Lucas Ghi con el  apoyo de Axel Kicilof, Cristina Fernández de Kirchner, Sergio Massa y Alberto Fernández por el Frente de Todos': colores["peronismo"],
 'A Analía Zapulla con el apoyo  de Patricia Bullrich y Mauricio Macri por Juntos por el Cambio': colores["cambiemos"],
 'A Ariel Diguan con el apoyo de Javier Millei por la Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P22"] = {'A Daniel Scioli Presidente, Axel Kiciloff Gobernador y Lucas Ghi Intendente por el Frente de Todos': colores["peronismo"],
 'A Horacio Rodríguez Larreta Presidente, Diego Santilli Gobernador y Ramiro Tagliaferro Intendente por Juntos por el Cambio': colores["cambiemos"],
 'A Javier Millei Presidente, su candidato a Gobernador y Ariel Diguan Intendente por la Libertad Avanza': colores["liberales"],
 'A los candidatos a Presidente, Gobernador e Intendente del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P23"] = {'A Daniel Scioli Presidente, Axel Kiciloff Gobernador y Lucas Ghi Intendente por el Frente de Todos': colores["peronismo"],
 'A Patricia Bullrich Presidenta, Joaquín De la Torre Gobernador y Analia Zapulla Intendenta': colores["cambiemos"],
 'A Javier Milei Presidente, su candidato a Gobernador y Ariel Diguan Intendente por la Libertad Avanza': colores["liberales"],
 'Al los candidatos a Presidente, Gobernador e Intendente del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P24"] = opinionColorDict


paletas["P25"] = opinionColorDict


paletas["P26"] = opinionColorDict


paletas["P27"] = opinionColorDict


paletas["P28"] = opinionColorDict


paletas["P29"] = opinionColorDict


paletas["P30"] = opinionColorDict


paletas["P31"] = list2dictPalette(['Que continúe el intendente Lucas Gui', 'Que continúe Lucas Gui pero con mejoras', 'Que cambie Lucas Gui pero que se mantengan los avances', 'Que cambie el intendente Lucas Gui'], qualitative_strong, noSabe=False)


paletas["P32"] = list2dictPalette(['La seguridad', 'El tránsito', 'El arreglo de las calles', 'Los parques y espacios públicos', 'El sistema de salud', 'La limpieza de las calles', 'El deporte y la cultura', 'La luminaria', 'No sabe'], qualitative_strong, noSabe=True)


paletas["P33"] = list2dictPalette(['La seguridad', 'El tránsito', 'El arreglo de las calles', 'Los parques y espacios públicos', 'El sistema de salud', 'La limpieza de las calles', 'El deporte y la cultura', 'La luminaria', 'No sabe'], qualitative_strong, noSabe=True)


paletas["P34"] = list2dictPalette(['Agua corriente y cloacas', 'Energía eléctrica', 'Red de gas natural', 'Recolección de residuos', 'Ninguno'], qualitative_strong, noSabe=False)


paletas["P35"] = list2dictPalette(['Los robos', 'El narcotráfico', 'La ausencia de patrulleros y personal policial', 'Otro', 'Ninguno'], qualitative_strong, noSabe=False)


paletas["P36"] = opinionColorDict


paletas["P37"] = votaria


paletas["P38"] = votaria


paletas["P39"] = votaria


paletas["P40"] = votaria


paletas["P41"] = votaria


paletas["P42"] = votaria


paletas["P43"] = votaria


paletas["P44"] = votaria


paletas["P45"] = votaria


paletas["P46"] = opinionColorDict


paletas["P47"] = opinionColorDict


paletas["P48"] = opinionColorDict


paletas["P49"] = opinionColorDict


paletas["P50"] = opinionColorDict


paletas["P51"] = opinionColorDict


paletas["P52"] = opinionColorDict

