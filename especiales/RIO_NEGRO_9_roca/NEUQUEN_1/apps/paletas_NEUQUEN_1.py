from especiales.NEUQUEN_1.apps.cuestionario_NEUQUEN_1 import cuestionario
from config import colores, votaria, opinionColorDict
paletas = {}



paletas["P05"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
                  'De Juntos por el cambio': colores["cambiemos"],
                  'De los Liberales libertarios': colores["liberales"],
                  'De la Izquierda': colores["izquierda"],
                  'No sabe': colores["nosabe"]}

paletas["P06"] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}

paletas["P07"] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
}
paletas["P08"] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros'],
    "Martin Lousteau":" #e0976e"
}




paletas["P09"] = {'Marcos Koopmann a gobernador y Ana Pechén a vicegobernadora por el Movimiento Nacional Neuquino': colores["cristianos"],
                  '“Rolo” Figueroa a gobernador y Gloria Ruiz a vicegobernadora por el Comunidad y el Frente Neuquinizate': colores["otros"],
                  'Ramón Rioseco a gobernador y Ayelén Gutiérrez a vicegobernadora por el Frente de Todos Neuquino': colores["peronismo"],
                  'Pablo Cervi a gobernador y Jorge Taylor a vicegobernador por Juntos por el Cambio Neuquén': colores["cambiemos"],
                  'Carlos Eguía a gobernador y Catalina Uleri a vicegobernadora por Cumplir': colores["cambiemos_ucr"],
                  'Patricia Jure a gobernadora y Raúl Godoy a vicegobernador por el Frente de Izquierda Unidad': colores["izquierda"],
                  'No sabe': colores["nosabe"]}

paletas["P10"] = {'A Marcos Koopmann por el Movimiento Popular Neuquino con el apoyo de Jorge Sapag': colores["cristianos"],
                  'A “Rolo” Figueroa por Comunidad y el Frente Neuquinizate con el apoyo del PRO, parte de la UCR, el Frente Grande y sectores del PJ': colores["otros"],
                  'A Ramón Rioseco por el Frente de Todos Neuquino con el apoyo del PJ, Cristina Fernández de Kirchner y Libres del Sur': colores["peronismo"],
                  'A Pablo Cervi por Juntos por el Cambio Neuquén con el apoyo de Martín Lousteau y parte de la UCR': colores["cambiemos"],
                  'A Carlos Eguía por Cumplir con el apoyo de Javier Milei': colores["liberales"],
                  'A Patricia Jure del Frente de Izquierda Unidad con apoyo de Nicolás del Caño':
                      colores["izquierda"],
                  'No sabe': colores["nosabe"]
                  }

paletas['P09_imputada'] = paletas['P09']
paletas['P10_imputada'] = paletas['P10']

paletas["P11"] = votaria
paletas["P12"] = votaria
paletas["P13"] = votaria
paletas["P14"] = votaria
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = opinionColorDict
paletas["P18"] = opinionColorDict
paletas["P19"] = opinionColorDict
paletas["P20"] = opinionColorDict
paletas["P21"] = opinionColorDict
paletas["P22"] = opinionColorDict
paletas["P23"] = opinionColorDict
paletas["P24"] = opinionColorDict
paletas["P25"] = opinionColorDict
paletas["P26"] = opinionColorDict
paletas["P27"] = opinionColorDict
paletas["P28"] = opinionColorDict
