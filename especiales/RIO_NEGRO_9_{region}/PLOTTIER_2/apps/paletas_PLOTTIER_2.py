from especiales.PLOTTIER_2.apps.cuestionario_PLOTTIER_2 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict


paletas = {}
# Bloque Intención de voto por espacio político 

colores["desarrollo"] = '#11c900' #verde
colores['comunidad'] = '#b800eb' #violeta

paletas["P06"] = {'Andres Peressini por Iguales': colores["cambiemos"], 'Sergio Soto por MPN': colores["cristianos"], 'Luis Bertolini por Desarrollo Ciudadano': colores["desarrollo"], 'Karina Ortiz por Unión por Plottier': colores["otros"], 'Norberto Calducci por el Frente de Izquierda': colores["izquierda"], 'Hector Agostino por el Partido Autonomista': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P06_imputada"] = {'Andres Peressini por Iguales': colores["cambiemos"], 'Sergio Soto por MPN': colores["cristianos"], 'Luis Bertolini por Desarrollo Ciudadano': colores["desarrollo"], 'Karina Ortiz por Unión por Plottier': colores["peron1"], 'Norberto Calducci por el Frente de Izquierda': colores["izquierda"], 'Hector Agostino por el Partido Autonomista': colores["otros"], 'No sabe': colores["nosabe"]}


paletas["P10"] = votaria
paletas["P11"] = votaria
paletas["P12"] = votaria
paletas["P13"] = votaria
paletas["P14"] = votaria
paletas["P15"] = votaria
paletas["P16"] = siNoColorDict