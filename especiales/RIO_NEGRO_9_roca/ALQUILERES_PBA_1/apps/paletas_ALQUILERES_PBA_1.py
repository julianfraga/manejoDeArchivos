from especiales.ALQUILERES_PBA_1.apps.cuestionario_ALQUILERES_PBA_1 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, diverging_mini, diverging, qualitative_strong

# comando:


paletas = {}

paletas["P04"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Alberto Fernández por el Frente de Todos': colores["peron1"],
 'Sergio Massa por el Frente de Todos': colores["peron2"],
 'Wado de Pedro por el Frente de Todos': colores["peron3"],
 'Daniel Scioli por el Frente de Todos': colores["peron4"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P06"] = list2dictPalette(['Si, es una vivienda alquilada', 'No, no es una vivienda alquilada'],
 diverging_mini, noSabe=False)


paletas["P07"] = list2dictPalette(['Mejor que la ley anterior', 'Igual que la ley anterior', 'Peor que la ley anterior', 'No sabe'],
 diverging, noSabe=True)


paletas["P08"] = list2dictPalette(['Que el estado no hace cumplir la actual ley de alquiler', 'La ley actual no le brinda a los propietarios las garantías e incentivos para poner las viviendas en alquiler', 'Por ambas razones', 'No sabe'],
 qualitative_strong, noSabe=True)


paletas["P09"] = list2dictPalette(['Los inquilinos', 'Los propietarios', 'A ambos, propietarios e inquilinos', 'A ninguno', 'No sabe'],
 qualitative_strong, noSabe=True)


paletas["P10"] = list2dictPalette(['Si, se debería cobrar a las viviendas que no son habitadas por sus dueños o sus familiares y tampoco son puestas en alquiler', 'No, no se debería cobrar nada', 'No sabe'],
 diverging, noSabe=True)
