from especiales.MENDOZA_1.apps.cuestionario_MENDOZA_1 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, qualitative_strong, siNoColorDict

izquierda2 = '#bd0202'

paletas = {}
# Bloque Escenarios políticos
paletas["P08"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
                  'De Juntos por el cambio': colores["cambiemos"],
                  'De los Liberales libertarios': colores["liberales"],
                  'De la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P09"] = list2dictPalette(['A Sergio Massa','A Daniel Scioli','A algún candidato del peronismo','A algún candidato del kirchnerismo'], qualitative_strong, noSabe=False)

paletas["P10"] = list2dictPalette(['A Horacio Rodriguez Larreta','A Patricia Bullrich','A Facundo Manes','A Gerardo Morales'], qualitative_strong, noSabe=False)

paletas["P11"] = {'Alfredo Cornejo por Cambia Mendoza': colores["cambiemos1"],
                  'Luis Petri por Cambia Mendoza': colores["cambiemos2"],
                  'Omar De Marchi por La Unión Mendocina': colores["liberales"],
                  'Omar Parisi por Elegí Mendoza': colores["peronismo1"],
                  'Guillermo Carmona por Elegí Mendoza': colores["peronismo2"],
                  'Nicolás Guillén por Elegí Mendoza': colores["peronismo3"],
                  'Alfredo Guevara por Elegí Mendoza': colores["peronismo4"],
                  'Lautaro Giménez por el Frente de Izquierda': colores["izquierda"],
                  'Victor da Vila por el Frente de Izquierda': izquierda2,
                  'No sabe': colores["nosabe"]}

paletas["P14"] = {'Alfredo Cornejo a gobernador y Hebe Casado a vicegobernadora por Cambia Mendoza': colores["cambiemos1"],
                  'Luis Petri a gobernador y Patricia Giménez a vicegobernadora por Cambia Mendoza': colores["cambiemos2"],
                  'Omar De Marchi a gobernador y Daniel Orozco a vicegobernador por “La Unión Mendocina”': colores["liberales"],
                  'Omar Parisi a gobernador y Lucas Ilardo a vicegobernador por Elegí Mendoza': colores["peronismo1"],
                  'Guillermo Carmona a gobernador y Liliana Paponet a vicegobernadora por Elegí Mendoza': colores["peronismo2"],
                  'Nicolás Guillén a gobernador y Lorena Martin a vicegobernadora por Elegí Mendoza': colores["peronismo3"],
                  'Alfredo Guevara a gobernador y Patricia Galván a vicegobernadora por Elegí Mendoza': colores["peronismo4"],
                  'Lautaro Giménez a gobernador y Noelia Barbeito a vicegobernadora por el Frente de Izquierda': colores["izquierda"],
                  'Victor da Vila a gobernador y Nadya Ortiz Gazzo a vicegobernadora por el Frente de Izquierda': izquierda2,
                  'No sabe': colores["nosabe"]}

paletas["P17"] = {'Alfredo Cornejo por Cambia Mendoza con el apoyo de Patricia Bullrich, Horacio Rodríguez Larreta, Mauricio Macri y una parte de la UCR': colores["cambiemos1"], 
                  'Luis Petri por Cambia Mendoza con el apoyo de Julio Cobos y una parte de la UCR': colores["cambiemos2"],
                  'Omar De Marchi por La Unión Mendocina con el apoyo de una parte del PRO y de Javier Milei': colores["liberales"],
                  'Omar Parisi por Elegí Mendoza con el apoyo de Anabel Fernández Sagasti y una parte del kirchnerismo': colores["peronismo1"],
                  'Guillermo Carmona por Elegí Mendoza con el apoyo de Emir y Omar Félix, y una parte del PJ': colores["peronismo2"],
                  'Nicolás Guillén por Elegí Mendoza con el apoyo de la Corriente Clasista y Combativa, y los movimientos sociales': colores["otros"],
                  'Alfredo Guevara por Elegí Mendoza con el apoyo de una parte del kirchnerismo': colores["peronismo3"],
                  'Lautaro Giménez por el Frente de Izquierda con el apoyo de Nicolás Del Caño, Myriam Bregman, el Partido Socialista de los Trabajadores y el Movimiento Socialista de los Trabajadores': colores["izquierda"],
                  'Victor da Vila por el Frente de Izquierda con el apoyo de Gabriel Solano, Romina Del Plá y el Partido Obrero': izquierda2,
                  'No sabe': colores["nosabe"]}

paletas["P11_imputadas"] = {'Alfredo Cornejo por Cambia Mendoza': colores["cambiemos1"],
                  'Luis Petri por Cambia Mendoza': colores["cambiemos2"],
                  'Omar De Marchi por La Unión Mendocina': colores["liberales"],
                  'Omar Parisi por Elegí Mendoza': colores["peronismo1"],
                  'Guillermo Carmona por Elegí Mendoza': colores["peronismo2"],
                  'Nicolás Guillén por Elegí Mendoza': colores["peronismo3"],
                  'Alfredo Guevara por Elegí Mendoza': colores["peronismo4"],
                  'Lautaro Giménez por el Frente de Izquierda': colores["izquierda"],
                  'Victor da Vila por el Frente de Izquierda': izquierda2}

paletas["P14_imputadas"] = {'Alfredo Cornejo a gobernador y Hebe Casado a vicegobernadora por Cambia Mendoza': colores["cambiemos1"],
                  'Luis Petri a gobernador y Patricia Giménez a vicegobernadora por Cambia Mendoza': colores["cambiemos2"],
                  'Omar De Marchi a gobernador y Daniel Orozco a vicegobernador por “La Unión Mendocina”': colores["liberales"],
                  'Omar Parisi a gobernador y Lucas Ilardo a vicegobernador por Elegí Mendoza': colores["peronismo1"],
                  'Guillermo Carmona a gobernador y Liliana Paponet a vicegobernadora por Elegí Mendoza': colores["peronismo2"],
                  'Nicolás Guillén a gobernador y Lorena Martin a vicegobernadora por Elegí Mendoza': colores["peronismo3"],
                  'Alfredo Guevara a gobernador y Patricia Galván a vicegobernadora por Elegí Mendoza': colores["peronismo4"],
                  'Lautaro Giménez a gobernador y Noelia Barbeito a vicegobernadora por el Frente de Izquierda': colores["izquierda"],
                  'Victor da Vila a gobernador y Nadya Ortiz Gazzo a vicegobernadora por el Frente de Izquierda': izquierda2}

paletas["P17_imputadas"] = {'Alfredo Cornejo por Cambia Mendoza con el apoyo de Patricia Bullrich, Horacio Rodríguez Larreta, Mauricio Macri y una parte de la UCR': colores["cambiemos1"], 
                  'Luis Petri por Cambia Mendoza con el apoyo de Julio Cobos y una parte de la UCR': colores["cambiemos2"],
                  'Omar De Marchi por La Unión Mendocina con el apoyo de una parte del PRO y de Javier Milei': colores["liberales"],
                  'Omar Parisi por Elegí Mendoza con el apoyo de Anabel Fernández Sagasti y una parte del kirchnerismo': colores["peronismo1"],
                  'Guillermo Carmona por Elegí Mendoza con el apoyo de Emir y Omar Félix, y una parte del PJ': colores["peronismo2"],
                  'Nicolás Guillén por Elegí Mendoza con el apoyo de la Corriente Clasista y Combativa, y los movimientos sociales': colores["otros"],
                  'Alfredo Guevara por Elegí Mendoza con el apoyo de una parte del kirchnerismo': colores["peronismo3"],
                  'Lautaro Giménez por el Frente de Izquierda con el apoyo de Nicolás Del Caño, Myriam Bregman, el Partido Socialista de los Trabajadores y el Movimiento Socialista de los Trabajadores': colores["izquierda"],
                  'Victor da Vila por el Frente de Izquierda con el apoyo de Gabriel Solano, Romina Del Plá y el Partido Obrero': izquierda2}

paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria
paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = votaria
paletas["P32"] = votaria
paletas["P33"] = votaria
paletas["P34"] = votaria
paletas["P35"] = votaria
paletas["P36"] = votaria
paletas["P37"] = votaria

# Bloque Imagen de dirigentes
paletas["P38"] = opinionColorDict
paletas["P39"] = opinionColorDict
paletas["P40"] = opinionColorDict
paletas["P41"] = opinionColorDict
paletas["P42"] = opinionColorDict
paletas["P43"] = opinionColorDict
paletas["P44"] = opinionColorDict
paletas["P45"] = opinionColorDict
paletas["P46"] = opinionColorDict
paletas["P47"] = opinionColorDict
paletas["P48"] = opinionColorDict
paletas["P49"] = opinionColorDict
paletas["P50"] = opinionColorDict
paletas["P51"] = opinionColorDict
paletas["P52"] = opinionColorDict
paletas["P53"] = opinionColorDict
paletas["P54"] = opinionColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = siNoColorDict