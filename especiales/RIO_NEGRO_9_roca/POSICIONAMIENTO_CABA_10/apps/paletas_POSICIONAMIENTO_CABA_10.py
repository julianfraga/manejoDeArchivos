from especiales.POSICIONAMIENTO_CABA_10.apps.cuestionario_POSICIONAMIENTO_CABA_10 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, diverging, diverging_reverse, internas
import seaborn as sns
# comando:


paletas = {}

paletas["P06"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
 'De Cambiemos': colores["cambiemos"],
 'De los Liberales libertarios': colores["liberales"],
 'De la Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}

paletas["P07"] = internas
paletas["P08"] = internas
paletas["P09"] = internas

paletas["P10"] = {'Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'Jorge Macri por Juntos por el Cambio': colores["cambiemos1"],
 'Martín Lousteau por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P11"] = {'María Eugenia Vidal por Juntos por el Cambio': colores["cambiemos1"],
 'Martín Lousteau por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P12"] = {'A Jorge Macri por Juntos por el Cambio': colores["cambiemos1"],
 'A Martín Lousteau por Juntos por el Cambio': colores["cambiemos_ucr"],
 'A Ricardo López Murphy por Juntos por el Cambio': colores["cambiemos2"],
 'A Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'A Matías Lammens por el Frente de Todos': colores["peronismo2"],
 'A Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["otros"],
 'No sabe': colores["nosabe"]}
paletas["P13"] = {'A Martín Lousteau por Juntos por el Cambio': colores["cambiemos_ucr"],
 'A Jorge Macri por Juntos por el Cambio': colores["cambiemos1"],
 'A Ricardo López Murphy por Juntos por el Cambio': colores["cambiemos2"],
 'A Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'A Pedro Rosemblat por el Frente de Todos': colores["peronismo2"],
 'A Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P14"] = {'A Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'A Pedro Rosemblat por el Frente de Todos': colores["peronismo2"],
 'A María Eugenia Vidal por Juntos por el Cambio': colores["cambiemos"],
 'A Martín Lousteau por Juntos por el Cambio': colores["cambiemos_ucr"],
 'A Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P15"] = {'A Leandro Santoro por el Frente de Todos con el apoyo de Cristina Fernández de Kirchner, Sergio Massa y Alberto Fernández': colores["peronismo"],
 'A Jorge Macri por Juntos por el Cambio con el apoyo de Mauricio Macri, Patricia Bullrich y Horacio Rodríguez Larreta': colores["cambiemos"],
 'A Martín Lousteau por Juntos por el Cambio el apoyo de la UCR y de Horacio Rodríguez Larreta': colores["cambiemos_ucr"],
 'A Ramiro Marra por La Libertad Avanza con el apoyo de Javier Milei': colores["liberales"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P16"] = {'A Leandro Santoro por el Frente de Todos con el apoyo de Cristina Fernández de Kirchner, Sergio Massa y Alberto Fernández': colores["peronismo"],
 'A María Eugenia Vidal por Juntos por el Cambio con el apoyo de Mauricio Macri, Patricia Bullrich y Horacio Rodríguez Larreta': colores["cambiemos"],
 'A Martín Lousteau por Juntos por el Cambio el apoyo de la UCR y de Horacio Rodríguez Larreta': colores["cambiemos_ucr"],
 'A Ramiro Marra por La Libertad Avanza con el apoyo de Javier Milei': colores["liberales"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P17"] = {'A Jorge Macri por Juntos por el Cambio con el apoyo de Mauricio Macri y Horacio Rodríguez Larreta': colores["cambiemos"],
 'A Martín Lousteau por Juntos por el Cambio con el apoyo de la UCR y Horacio Rodríguez Larreta': colores["cambiemos_ucr"],
 'A Ricardo López Murphy por Juntos por el Cambio con el apoyo de Patricia Bullrich': colores["cambiemos2"],
 'A Leandro Santoro por el Frente de Todos con el apoyo de Sergio Massa y Alberto Fernández': colores["peronismo"],
 'A Pedro Rosemblat por el Frente de Todos con el apoyo de La Cámpora y Juan Grabois': colores["peronismo2"],
 'A Ramiro Marra por La Libertad Avanza con el apoyo de Javier Milei': colores["liberales"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P18"] = {'A Leandro Santoro por el Frente de Todos con el apoyo de Sergio Massa y Alberto Fernández': colores["peronismo"],
 'A Pedro Rosemblat por el Frente de Todos con el apoyo de La Cámpora y Juan Grabois': colores["peronismo2"],
 'A María Eugenia Vidal por Juntos por el Cambio con el apoyo de Mauricio Macri, Patricia Bullrich y Horacio Rodríguez Larreta': colores["cambiemos"],
 'A Martín Lousteau por Juntos por el Cambio con el apoyo de la UCR y Horacio Rodríguez Larreta': colores["cambiemos_ucr"],
 'A Ramiro Marra por La Libertad Avanza con el apoyo de Javier Milei': colores["liberales"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P19"] = {'A Martín Lousteau por Juntos por el Cambio': colores["cambiemos"],
 'A Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'A Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P22"] = {'A Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'A Jorge Macri por Juntos por el Cambio': colores["cambiemos"],
 'A Ramiro Marra por La Libertad Avanza': colores["otros"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P25"] = {'A Leandro Santoro por el Frente de Todos': colores["peronismo"],
 'A María Eugenia Vidal por Juntos por el Cambio': colores["cambiemos"],
 'A Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P28"] = {'A Pedro Rosemblat por el Frente de Todos': colores["peronismo"],
 'A María Eugenia Vidal por Juntos por el Cambio': colores["cambiemos"],
 'A Ramiro Marra por La Libertad Avanza': colores["liberales"],
 'Al candidato del Frente de Izquierda con el apoyo de Nicolás Del Caño, Romina Del Plá y Myriam Bregman': colores["izquierda"],
 'A Luis Zamora por Autodeterminación y Libertad': colores["otros"],
 'En blanco': colores["blanco"],
 'No sabe': colores["nosabe"]}
paletas["P31"] = votaria
paletas["P32"] = votaria
paletas["P33"] = votaria
paletas["P34"] = votaria
paletas["P35"] = votaria
paletas["P36"] = votaria
paletas["P37"] = votaria
paletas["P38"] = votaria