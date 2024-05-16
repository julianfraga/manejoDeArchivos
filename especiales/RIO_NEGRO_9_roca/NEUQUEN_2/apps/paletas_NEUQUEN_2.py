from especiales.NEUQUEN_2.apps.cuestionario_NEUQUEN_2 import cuestionario
from config import colores, votaria, opinionColorDict
paletas = {}




paletas["P05"] = {'Marcos Koopmann a gobernador y Ana Pechén a vicegobernadora': colores["cristianos"],
                  '“Rolo” Figueroa a gobernador y Gloria Ruiz a vicegobernadora': colores["otros"],
                  'Ramón Rioseco a gobernador y Ayelén Gutiérrez a vicegobernadora': colores["peronismo"],
                  'Pablo Cervi a gobernador y Jorge Taylor a vicegobernador': colores["cambiemos"],
                  'Carlos Eguía a gobernador y Catalina Uleri a vicegobernadora': colores["cambiemos_ucr"],
                  'Patricia Jure a gobernadora y Raúl Godoy a vicegobernador': colores["izquierda"],
                  'En blanco':colores['blanco'],
                  'No sabe': colores["nosabe"]}
paletas['P05_imputada'] = paletas['P05']
paletas["P07"] = votaria
paletas["P08"] = votaria
paletas["P09"] = votaria
paletas["P10"] = votaria
paletas["P11"] = votaria


