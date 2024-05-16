from config import colores,opinionColorDict, list2dictPalette, siNoColorDict, frecuenciaColorDict, diverging,qualitative_strong,siNoNoSabeColorDict

# comando:
altobajoColorDict = list2dictPalette(['Alto', 'Regular', 'Bajo', 'No sabe'], diverging, noSabe=True)
buenaMalaColorDict = list2dictPalette(['Buena', 'Regular', 'Mala', 'No sabe'], diverging, noSabe=True)

paletas = {}

# Bloque Control
paletas["P08"] = frecuenciaColorDict

# Bloque Bloque General
paletas["P09"] = opinionColorDict
paletas["P10"] = opinionColorDict

# Bloque Bloque Neuquén Capital
paletas["P11"] = opinionColorDict
paletas["P12"] = opinionColorDict

# Bloque Bloque General
paletas["P13"] = siNoNoSabeColorDict
paletas["P14"] = siNoNoSabeColorDict
paletas["P15"] = siNoNoSabeColorDict
paletas["P16"] = siNoNoSabeColorDict
paletas["P17"] = list2dictPalette(['El gobierno nacional', 'El gobierno provincial anterior del MPN', 'El actual gobierno provincial de Rolo Figueroa', 'Todos igual', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P18"] = list2dictPalette(['Es un logro muy importante del Gobierno provincial', 'Está bien, pero es insuficiente para resolver la situación de emergencia', 'No alcanza para nada y son negocios del gobierno Provincial', 'No alcanza para nada porque el gobierno gestionó mal la compra', 'No sabe'], diverging, noSabe=True)
paletas["P19"] = siNoNoSabeColorDict
paletas["P20"] = siNoNoSabeColorDict

# Bloque Bloque Neuquén Capital
paletas["P21"] = siNoNoSabeColorDict
paletas["P22"] = siNoNoSabeColorDict

# Bloque Bloque General
paletas["P23"] = buenaMalaColorDict
paletas["P24"] = buenaMalaColorDict
paletas["P25"] = buenaMalaColorDict
paletas["P26"] = list2dictPalette(['La capacitación para atender a la gente', 'La infraestructura y equipamiento de la fuerza', 'La formación técnica y profesional', 'La cantidad y distribución de los efectivos', 'La velocidad de respuesta ante las denuncias', 'Otros', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P27"] = altobajoColorDict
paletas["P28"] = {'El gobierno de Javier Milei': colores["liberales_contraste"], 'El gobierno de Alberto Fernández': colores["peronismo_contraste"], 'Ambos': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P29"] = list2dictPalette(['Dividirla en partes y transformarlas en varios decretos de necesidad y urgencia', 'Dividirlas en diferentes leyes que se puedan ir votando paulatinamente', 'Realizar un plebiscito sobre la necesidad del tratamiento de la ley ómnibus', 'Retirarla y no presentar nada', 'Volverla a presentar igual', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P30"] = {'Javier Milei': colores["liberales_contraste"], 'Los gobernadores': colores["cambiemos_ucr"], 'No sabe': colores["nosabe"]}


# Bloque Imagen de dirigentes
paletas["P31"] = opinionColorDict
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
paletas["P44"] = opinionColorDict
paletas["P45"] = opinionColorDict