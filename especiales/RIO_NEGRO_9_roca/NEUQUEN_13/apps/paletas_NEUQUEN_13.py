from config import colores, diverging_mini, opinionColorDict, list2dictPalette, diverging_reverse, siNoNoSabeColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P08"] = list2dictPalette(['Siempre', 'Casi siempre', 'Casi nunca', 'Nunca, pero esta es una excepción'], diverging, noSabe=False)

# Bloque Bloque General
paletas["P09"] = opinionColorDict
paletas["P10"] = opinionColorDict
paletas["P11"] = opinionColorDict
paletas["P12"] = opinionColorDict
paletas["P13"] = siNoNoSabeColorDict
paletas["P14"] = siNoNoSabeColorDict
paletas["P15"] = list2dictPalette(['Gobierno nacional', 'Gobierno provincial', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P16"] = list2dictPalette(['El gobierno anterior de Omar Gutierrez', 'El actual gobierno de Rolo Figueroa', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P17"] = list2dictPalette(['El gobierno anterior de Alberto Fernández', 'El actual gobierno de Javier Milei', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P18"] = opinionColorDict
paletas["P19"] = opinionColorDict
paletas["P20"] = opinionColorDict
paletas["P21"] = list2dictPalette(['Muy de acuerdo', 'De acuerdo', 'Ni de acuerdo ni en desacuerdo', 'En desacuerdo', 'Muy en desacuerdo', 'No sabe'], diverging, noSabe=True)
paletas["P22"] = list2dictPalette(['El estado nacional', 'El estado provincial', 'Ambos de forma coordinada', 'No sabe'], qualitative_strong, noSabe=True)

# Bloque Bloque Gremio Docente
paletas["P23"] = siNoNoSabeColorDict
paletas["P24"] = list2dictPalette(['Excesiva', 'Adecuada', 'Insuficiente', 'Inaceptable', 'No sabe'], diverging, noSabe=True)
paletas["P26"] = siNoNoSabeColorDict
paletas["P27"] = list2dictPalette(['Correcta', 'Incorrecta', 'No sabe'], diverging_mini, noSabe=True)
paletas["P28"] = siNoNoSabeColorDict
paletas["P29"] = list2dictPalette(['Correcta', 'Incorrecta', 'No sabe'], diverging_mini, noSabe=True)
paletas["P30"] = siNoNoSabeColorDict
paletas["P31"] = list2dictPalette(['Excesiva', 'Adecuada', 'Insuficiente', 'Inaceptable', 'No sabe'], diverging, noSabe=True)
paletas["P33"] = siNoNoSabeColorDict
paletas["P34"] = siNoNoSabeColorDict

# Bloque Bloque General
paletas["P35"] = list2dictPalette(['Inseguridad y narcotráfico', 'Altos impuestos y tarifas', 'Educación y estado de las escuelas', 'Inflación', 'Estado de la salud', 'Corrupción', 'Pobreza', 'Medio ambiente, incendios y contaminación', 'Falta de trabajo', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P39"] = opinionColorDict
paletas["P40"] = list2dictPalette(["Peor","Igual","Mejor","No sabe"], diverging_reverse, noSabe=True)
paletas["P41"] = list2dictPalette(["Peor","Igual","Mejor","No sabe"], diverging_reverse, noSabe=True)
paletas["P42"] = {'El gobierno de Javier Milei':colores['liberales_contraste'], 'El gobierno de Alberto Fernández':colores['peronismo_contraste'], 'Ambos':colores['otros'], 'No sabe':colores['nosabe']}
paletas["P43"] = {'Javier Milei': colores["liberales_contraste"], 'Los gobernadores': colores["otros"], 'No sabe': colores["nosabe"]}


# Bloque Imagen de dirigentes
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
paletas["P56"] = opinionColorDict
paletas["P57"] = opinionColorDict
paletas["P58"] = opinionColorDict