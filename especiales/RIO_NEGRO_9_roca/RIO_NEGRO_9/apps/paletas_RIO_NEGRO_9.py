from config import colores, ingresosColorDict, opinionColorDict, list2dictPalette, siNoColorDict, siNoNoSabeColorDict, internas, diverging_reverse, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Bloque Perfil económico y laboral
paletas["P12"] = ingresosColorDict
paletas["P13"] = list2dictPalette(['Empleado sector publico', 'Empleado sector privado', 'Changas o trabajos eventuales', 'Estudiante', 'Amas de casa', 'Profesional o independiente', 'Comerciante, emprendedor o empresario', 'Trabajador informal', 'No tengo trabajo'], qualitative_strong, noSabe=False)

# Bloque Bloque Gestión pública provincial y nacional
paletas["P14"] = opinionColorDict
paletas["P15"] = opinionColorDict
paletas["P20"] = opinionColorDict
paletas["P21"] = {'Gobierno nacional': colores["otros"], 'Gobierno provincial': colores["cambiemos"], 'No sabe': colores["nosabe"]}

paletas["P22"] = {'El anterior gobierno de Anabela Carreras': colores["otros"], 'El actual gobierno de Alberto Weretilneck': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P23"] = {'El anterior gobierno de Alberto Fernández': colores["otros"], 'El actual gobierno de Javier Milei': colores["liberales"], 'No sabe': colores["nosabe"]}


# Bloque Bloque Coyuntura provincial
paletas["P24"] = siNoNoSabeColorDict
paletas["P25"] = siNoNoSabeColorDict
paletas["P26"] = siNoNoSabeColorDict
paletas["P27"] = list2dictPalette(['Estoy totalmente en desacuerdo, las universidades públicas son garantía de promoción social y contribuyen a igualar las oportunidades de todos los argentinos', 'Estoy en desacuerdo, sin universidades publicas no puede haber crecimiento sostenible ni mejora de la situación económica del país', 'Estoy parcialmente de acuerdo, es necesario una reforma profunda del sistema universitario público, incorporando exámenes de ingreso, arancelamiento para dar becas de estudio y racionalización de la oferta de carreras priorizando aquellas orientadas al desarrollo científico, tecnológico, la salud y el desarrollo económico', 'Estoy de acuerdo, las universidades publicas son muy ineficientes y costosas. La mayor parte de alumnos nunca terminan sus estudios, hay gran cantidad de carreras innecesarias y están muy politizadas', 'Estoy totalmente de acuerdo, las universidades publicas son centros de adoctrinamiento político y sirven a los intereses de los partidos políticos. Sería mejor utilizar esa plata para becar a los alumnos de escasos recursos para que pudieran elegir en que universidad privada estudiar', 'No sabe'], diverging, noSabe=True)

# Bloque Bloque Gestión pública provincial y nacional
paletas["P28"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P29"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P30"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)
paletas["P31"] = list2dictPalette(['1-Excelente', '2', '3', '4', '5', '6', '7', '8', '9-Pésimo', 'No sabe'], diverging, noSabe=True)

# Bloque Bloque Coyuntura nacional
paletas["P32"] = list2dictPalette(['Oponerse totalmente y elevar un recurso de amparo ante la corte', 'Oponerse y tratar de negociar con el gobierno nacional a cambio de apoyo legislativo en otros temas', 'Apoyar las iniciativas del gobierno nacional y así no tener problemas con la participación', 'Apoyar totalmente la iniciativa del gobierno nacional porque es lo que votó la mayoría del pueblo argentino', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P33"] = list2dictPalette(['Oponerse totalmente y no concurrir a la convocatoria', 'Oponerse parcialmente y concurrir a la convocatoria', 'Apoyar la iniciativa del gobierno nacional y negociar otros temas en discusión', 'Apoyar totalmente la iniciativa del gobierno nacional', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P34"] = list2dictPalette(['Oponerse totalmente', 'Oponerse parcialmente', 'Apoyar parcialmente', 'Apoyar totalmente', 'No sabe'], diverging_reverse, noSabe=True)

# Bloque Bloque Principales problemas y situación económica provincial
paletas["P35"] = list2dictPalette(['Inseguridad y narcotráfico', 'Altos impuestos y tarifas', 'Educación y estado de las escuelas', 'Inflación', 'Estado de la salud', 'Corrupción', 'Pobreza', 'Medio ambiente, incendios y contaminación', 'Falta de trabajo', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P39"] = opinionColorDict
paletas["P40"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging, noSabe=True)
paletas["P41"] = list2dictPalette(['Peor', 'Igual', 'Mejor', 'No sabe'], diverging, noSabe=True)

# Bloque Bloque Coyuntura nacional
paletas["P42"] = list2dictPalette(['Javier Milei', 'Los gobernadores', 'No sabe'], diverging, noSabe=True)

# Bloque Imagen de dirigentes
paletas["P43"] = opinionColorDict
paletas["P45"] = opinionColorDict
paletas["P46"] = opinionColorDict
paletas["P49"] = opinionColorDict
paletas["P50"] = opinionColorDict
paletas["P51"] = opinionColorDict
paletas["P52"] = opinionColorDict
paletas["P53"] = opinionColorDict
paletas["P54"] = opinionColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = opinionColorDict