from config import (
    colores, imagenColorDict, qualitative_strong, votaria, opinionColorDict, list2dictPalette,
    siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, comparacionColorDict,
    deudasColorDict, ingresosColorDict, problemaColorDict
)

# comando:


paletas = {}
# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales
paletas["P07"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
                  'De Juntos por el Cambio': colores["cambiemos"],
                  'De los Liberales libertarios': colores["liberales"],
                  'De la Izquierda': colores["izquierda"],
                  'No sabe': colores["nosabe"]}

paletas["P20"] = opinionColorDict
paletas["P22"] = opinionColorDict
paletas["P23"] = opinionColorDict
paletas["P24"] = opinionColorDict
paletas["P12"] = deudasColorDict
paletas["P13"] = ingresosColorDict
paletas["P08"] = problemaColorDict
paletas["P14"] = opinionColorDict
paletas["P15"] = comparacionColorDict
paletas["P16"] = comparacionColorDict
paletas["P17"] = opinionColorDict
paletas["P18"] = comparacionColorDict
paletas["P19"] = comparacionColorDict

paletas["P25"] = {'Frente de Todos y el peronismo': colores["peronismo"],
'Cambiemos': colores["cambiemos"],
'Liberales': colores["otros"],
'Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P28"] = internas

paletas["P30"] = internas

paletas["P31"] = internas

paletas["P39"] = votaria
paletas["P40"] = votaria
paletas["P41"] = votaria
paletas["P42"] = votaria
paletas["P67"] = list2dictPalette(['Radio', 'Televisión', 'Diario', 'Medio digital', 'Redes Sociales', 'Ninguno en particular', 'No sabe'], qualitative_strong, noSabe=True)

paletas["P46"] = imagenColorDict
paletas["P47"] = imagenColorDict
paletas["P48"] = imagenColorDict
paletas["P49"] = imagenColorDict
paletas["P50"] = imagenColorDict
paletas["P51"] = imagenColorDict
paletas["P52"] = imagenColorDict

paletas["P54"] = imagenColorDict

paletas["P56"] = imagenColorDict
paletas["P57"] = imagenColorDict
paletas["P58"] = imagenColorDict
paletas["P59"] = imagenColorDict
paletas["P60"] = imagenColorDict
paletas["P61"] = imagenColorDict
paletas["P62"] = imagenColorDict
paletas["P63"] = imagenColorDict
paletas["P64"] = imagenColorDict
paletas["P65"] = imagenColorDict
paletas["P66"] = imagenColorDict
paletas["P67"] = imagenColorDict



paletas["P68"] = opinionColorDict
paletas["P69"] = opinionColorDict