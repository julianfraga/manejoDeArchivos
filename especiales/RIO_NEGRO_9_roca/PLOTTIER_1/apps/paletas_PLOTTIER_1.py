from especiales.PLOTTIER_1.apps.cuestionario_PLOTTIER_1 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict


paletas = {}
# Bloque Intención de voto por espacio político 

colores["desarrollo"] = '#11c900' #verde
colores['comunidad'] = '#b800eb' #violeta

paletas["P05"] = muchoPocoColorDict

paletas["P06"] = {'Comunidad': colores["comunidad"],
                  'MPN': colores["cristianos"], 
                  'Desarrollo Ciudadano': colores["desarrollo"],
                  'Partido Justicialista': colores["peron1"],
                  'Iguales': colores["cambiemos"],
                  'Otro': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P07"] = {'Julieta Corroza por Comunidad': colores["comunidad"],
                  'Sergio Soto por el MPN': colores["cristianos"],
                  'Luis Bertolini por Desarrollo Ciudadano': colores["desarrollo"],
                  'Andrés Peressini por Iguales': colores["cambiemos"], 
                  'Karina Ortiz por el PJ': colores["peron1"], 
                  'No sabe': colores["nosabe"]}
paletas["P07_imputadas"] = paletas["P07"] 

paletas["P11"] = {'Julieta Corroza por Comunidad': colores["comunidad"],
                  'Sergio Soto por el MPN': colores["cristianos"],
                  'Luis Bertolini por Desarrollo Ciudadano': colores["desarrollo"],
                  'Andrés Peressini por Iguales': colores["cambiemos"],
                  'Karina Ortiz por el PJ': colores["peron1"], 
                  'No sabe': colores["nosabe"]}

paletas["P11_imputadas"] = paletas["P11"]
#Reach de intención de voto
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria

#control
paletas["P20"] = siNoColorDict