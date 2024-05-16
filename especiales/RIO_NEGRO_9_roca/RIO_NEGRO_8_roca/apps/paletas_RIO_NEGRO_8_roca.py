from config import colores, diverging_reverse, opinionColorDict, list2dictPalette, siNoColorDict, acuerdoBisColorDict, internas, ingresosColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P12"] = ingresosColorDict

# Bloque Bloque Política y Gestión
paletas["P13"] = opinionColorDict
paletas["P14"] = opinionColorDict
paletas["P16"] = opinionColorDict
paletas["P19"] = opinionColorDict
paletas["P20"] = {'Gobierno nacional': colores["liberales_contraste"], 'Gobierno provincial': colores["peronismo_contraste"], 'No sabe': colores["nosabe"]}


paletas["P21"] = {'El anterior gobierno de Arabela Carreras': colores["peronismo1"], 'El actual gobierno de Alberto Weretilneck': colores["peronismo3"], 'No sabe': colores["nosabe"]}

paletas["P22"] = {'El anterior gobierno de Alberto Fernández': colores["peronismo_contraste"], 'El actual gobierno de Javier Milei': colores["liberales_contraste"], 'No sabe': colores["nosabe"]}

# Bloque Bloque General
paletas["P23"] = list2dictPalette(['Empleado sector publico', 'Empleado sector privado', 'Changas o trabajos eventuales', 'Estudiante', 'Amas de casa', 'Profesional o independiente', 'Comerciante, emprendedor o empresario', 'Trabajador informal', 'No tengo trabajo'], qualitative_strong, noSabe=False)
paletas["P24"] = acuerdoBisColorDict
paletas["P25"] = acuerdoBisColorDict
paletas["P26"] = siNoColorDict
paletas["P27"] = acuerdoBisColorDict
paletas["P28"] = siNoColorDict
paletas["P29"] = acuerdoBisColorDict 
paletas["P30"] = {'No estaba enterado':"#b15928", 'De acuerdo':'#4bb05c', 'En desacuerdo':'#ea5739', 'No sabe':'#c9bebd'}
paletas["P31"] = {'No tengo cable ni internet':"#b15928", 'Si tuve':'#ea5739', 'No tuve':'#4bb05c'}
paletas["P32"] = list2dictPalette(['Reclamando directamente a la empresa', 'Reclamando en el Enacom porque la empresa nunca lo resolvió', 'Nunca se pudo resolver'], qualitative_strong, noSabe=False)

# Bloque Bloque Gestión Provincial
paletas["P33"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P34"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P35"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P36"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P37"] = list2dictPalette(['Oponerse totalmente y elevar un recurso de amparo ante la corte', 'Oponerse y tratar de negociar con el gobierno nacional a cambio de apoyo legislativo en otros temas', 'Apoyar las iniciativas del gobierno nacional y así no tener problemas con la participación', 'Apoyar totalmente la iniciativa del gobierno nacional porque es lo que votó la mayoría del pueblo argentino', 'No sabe'], diverging, noSabe=True)
paletas["P38"] = list2dictPalette(['Oponerse totalmente y no concurrir a la convocatoria', 'Oponerse parcialmente y concurrir a la convocatoria', 'Apoyar la iniciativa del gobierno nacional y negociar otros temas en discusión', 'Apoyar totalmente la iniciativa del gobierno nacional', 'No sabe'], diverging, noSabe=True)
paletas["P39"] = list2dictPalette(['Oponerse totalmente', 'Oponerse parcialmente', 'Apoyar parcialmente', 'Apoyar totalmente', 'No sabe'], diverging, noSabe=True)

# Bloque Bloque Política y Gestión
paletas["P40"] = list2dictPalette(['Inseguridad y narcotráfico', 'Altos impuestos y tarifas', 'Educación y estado de las escuelas', 'Inflación', 'Estado de la salud', 'Corrupción', 'Pobreza', 'Medio ambiente, incendios y contaminación', 'Falta de trabajo', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P44"] = opinionColorDict
paletas["P45"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P46"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P47"] = {'Javier Milei': colores["liberales_contraste"], 'Los gobernadores': '#e31a1c', 'No sabe': colores["nosabe"]}

# Bloque Imagen de dirigentes
paletas["P48"] = opinionColorDict
paletas["P50"] = opinionColorDict
paletas["P51"] = opinionColorDict
paletas["P54"] = opinionColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = opinionColorDict
paletas["P57"] = opinionColorDict
paletas["P58"] = opinionColorDict
paletas["P59"] = opinionColorDict
paletas["P60"] = opinionColorDict
paletas["P61"] = opinionColorDict