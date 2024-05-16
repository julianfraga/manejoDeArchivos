from config import colores, opinionColorDict, list2dictPalette, siNoColorDict,diverging,qualitative_strong, diverging_reverse, acuerdoBisColorDict, siNoNoSabeColorDict

# comando:


paletas = {}

# Bloque Bloque Perfil económico y laboral
paletas["P08"] = list2dictPalette(['Empleado sector publico', 'Empleado sector privado', 'Changas o trabajos eventuales', 'Estudiante', 'Amas de casa', 'Profesional o independiente', 'Comerciante, emprendedor o empresario', 'Trabajador informal', 'No tengo trabajo'], qualitative_strong, noSabe=False)

# Bloque Control
paletas["P09"] = list2dictPalette(['Siempre', 'Casi siempre', 'Casi nunca', 'Nunca, pero esta es una excepción'], diverging, noSabe=False)

# Bloque Bloque Gestión pública provincial y nacional
paletas["P10"] = opinionColorDict
paletas["P11"] = opinionColorDict
paletas["P12"] = opinionColorDict
paletas["P19"] = opinionColorDict
paletas["P21"] = siNoNoSabeColorDict
paletas["P22"] = siNoNoSabeColorDict
paletas["P23"] = {'Gobierno nacional': colores["liberales_contraste"], 'Gobierno provincial': colores["peronismo_contraste"], 'No sabe': colores["nosabe"]}

paletas["P24"] = list2dictPalette(['El gobierno anterior de Omar Gutierrez', 'El actual gobierno de Rolo Figueroa', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P25"] = {'El gobierno anterior de Alberto Fernández': colores["peronismo_contraste"], 'El actual gobierno de Javier Milei': colores["liberales_contraste"], 'No sabe': colores["nosabe"]}


# Bloque Bloque Coyuntura provincial
paletas["P26"] = siNoColorDict
paletas["P27"] = list2dictPalette(['Si', 'No estoy seguro', 'No', 'No sabe'], diverging, noSabe=True)
paletas["P28"] = list2dictPalette(['Espionaje por medio del Monitoreo de telecomunicaciones satelitales', 'Investigaciones científicas no declaradas con fines secretos', 'Prestar servicios de comunicación y posicionamiento global al ejército Chino', 'Otro', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P29"] = list2dictPalette(['Es imposible', 'Es muy difícil', 'Es bastante factible', 'Es posible', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P30"] = list2dictPalette(['Si', 'Es probable', 'No', 'No sabe'], diverging, noSabe=True)
paletas["P31"] = acuerdoBisColorDict
paletas["P32"] = siNoNoSabeColorDict

# Bloque Bloque Coyuntura nacional
paletas["P33"] = acuerdoBisColorDict
paletas["P34"] = siNoColorDict
paletas["P35"] = acuerdoBisColorDict

# Bloque Bloque Gestión pública provincial y nacional
paletas["P36"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P37"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P38"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P39"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)

# Bloque Bloque Coyuntura nacional
paletas["P40"] = list2dictPalette(['Oponerse totalmente y elevar un recurso de amparo ante la corte', 'Oponerse y tratar de negociar con el gobierno nacional a cambio de apoyo legislativo en otros temas', 'Apoyar las iniciativas del gobierno nacional y así no tener problemas con la participación', 'Apoyar totalmente la iniciativa del gobierno nacional porque es lo que votó la mayoría del pueblo argentino', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P41"] = list2dictPalette(['Oponerse totalmente y no concurrir a la convocatoria', 'Oponerse parcialmente y concurrir a la convocatoria', 'Apoyar la iniciativa del gobierno nacional y negociar otros temas en discusión', 'Apoyar totalmente la iniciativa del gobierno nacional', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P42"] = list2dictPalette(['Oponerse totalmente', 'Oponerse parcialmente', 'Apoyar parcialmente', 'Apoyar totalmente', 'No sabe'], diverging_reverse, noSabe=True)

# Bloque Bloque General
paletas["P43"] = list2dictPalette(['Inseguridad y narcotráfico', 'Altos impuestos y tarifas', 'Educación y estado de las escuelas', 'Inflación', 'Estado de la salud', 'Corrupción', 'Pobreza', 'Medio ambiente, incendios y contaminación', 'Falta de trabajo', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P47"] = opinionColorDict
paletas["P48"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P49"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P50"] = {'El gobierno de Javier Milei':colores['liberales_contraste'], 'El gobierno de Alberto Fernández':colores['peronismo_contraste'], 'Ambos':colores['otros'], 'No sabe':colores['nosabe']}
paletas["P51"] = {'Javier Milei': colores["liberales_contraste"], 'Los gobernadores': colores["otros"], 'No sabe': colores["nosabe"]}


# Bloque Imagen de dirigentes provinciales
paletas["P13"] = opinionColorDict
paletas["P14"] = opinionColorDict
paletas["P15"] = opinionColorDict
paletas["P16"] = opinionColorDict
paletas["P20"] = opinionColorDict

# Bloque Imagen de dirigentes nacionales
paletas["P17"] = opinionColorDict
paletas["P18"] = opinionColorDict
paletas["P52"] = opinionColorDict
paletas["P53"] = opinionColorDict
paletas["P54"] = opinionColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = opinionColorDict
paletas["P57"] = opinionColorDict
paletas["P58"] = opinionColorDict
paletas["P59"] = opinionColorDict