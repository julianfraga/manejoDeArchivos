from config import colores, ingresosColorDict, opinionColorDict, list2dictPalette, acuerdoBisColorDict, diverging_reverse, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P10"] = ingresosColorDict

# Bloque De rio negro
paletas["P11"] = opinionColorDict
paletas["P12"] = opinionColorDict
paletas["P13"] = opinionColorDict
paletas["P15"] = opinionColorDict
paletas["P16"] = {'Gobierno nacional': colores["liberales_contraste"], 'Gobierno provincial': colores["peronismo_contraste"], 'No sabe': colores["nosabe"]}

paletas["P17"] = {'El anterior gobierno de Arabela Carreras': colores["peronismo1"], 'El actual gobierno de Alberto Weretilneck': colores["peronismo3"], 'No sabe': colores["nosabe"]}

paletas["P18"] = {'El anterior gobierno de Alberto Fernández': colores["peronismo_contraste"], 'El actual gobierno de Javier Milei': colores["liberales_contraste"], 'No sabe': colores["nosabe"]}

paletas["P19"] = opinionColorDict
paletas["P20"] = opinionColorDict
paletas["P21"] = opinionColorDict
paletas["P22"] = acuerdoBisColorDict
paletas["P23"] = {'El estado nacional': colores["liberales_contraste"], 
                  'El estado provincial': colores["peronismo_contraste"], 
                  'Ambos de forma coordinada': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P24"] = list2dictPalette(['Inseguridad y narcotráfico', 'Altos impuestos y tarifas', 'Educación y estado de las escuelas', 'Inflación', 'Estado de la salud', 'Corrupción', 'Pobreza', 'Medio ambiente, incendios y contaminación', 'Falta de trabajo', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P28"] = opinionColorDict
paletas["P29"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P30"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P31"] = {'Javier Milei': colores["liberales_contraste"], 'Los gobernadores': '#e31a1c', 'No sabe': colores["nosabe"]}

paletas["P32"] = opinionColorDict
paletas["P33"] = opinionColorDict
paletas["P34"] = opinionColorDict
paletas["P35"] = opinionColorDict
paletas["P36"] = opinionColorDict
paletas["P37"] = opinionColorDict
paletas["P38"] = opinionColorDict
paletas["P39"] = opinionColorDict
paletas["P40"] = opinionColorDict
paletas["P41"] = opinionColorDict
paletas["P42"] = opinionColorDict
paletas["P43"] = opinionColorDict