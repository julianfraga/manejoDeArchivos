from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict

# comando:


paletas = {}
# Bloque Uso del transporte público y tiempo de viaje
paletas["P05"] = list2dictPalette(['Todos los días', 'Hasta 5 veces por semana', 'Entre 4 y 1 vez por semana', 'Ocasionalmente/ A veces', 'Nunca'], diverging, noSabe=False)
paletas["P06"] = list2dictPalette(['Colectivo', 'Subte', 'Tren', 'Premetro', 'Taxi', 'Aplicaciones como Uber, Cabify, Didi o similares'], diverging, noSabe=False)
paletas["P07"] = list2dictPalette(['Todos los días', 'Hasta 5 veces por semana', 'Entre 4 y 1 vez por semana', 'Ocasionalmente/ A veces', 'Nunca'], diverging, noSabe=False)
paletas["P08"] = list2dictPalette(['Menos de 30 minutos por día', 'Entre 30 minutos y 1 hora por día', 'Entre 1 y 2 horas por día', 'Más de 2 horas por día'], diverging, noSabe=False)

# Bloque Taxis y aplicaciones de transporte
paletas["P09"] = list2dictPalette(['Todos los días', 'Hasta 5 veces por semana', 'Entre 4 y 1 vez por semana', 'Ocasionalmente/ A veces', 'Nunca'], diverging, noSabe=False)
paletas["P10"] = list2dictPalette(['Todos los días', 'Hasta 5 veces por semana', 'Entre 4 y 1 vez por semana', 'Ocasionalmente/ A veces', 'No existen esos servicios donde vivo', 'Nunca'], diverging, noSabe=False)
paletas["P11"] = list2dictPalette(['Taxis tradicionales', 'Aplicaciones de transporte', 'No tengo preferencia por ninguna', 'No existen servicios de aplicaciones donde vivo'], diverging, noSabe=False)

# Bloque Costos y tarifas
paletas["P12"] = list2dictPalette(['Más de 5000 pesos mensuales', 'Entre 5000 y 2500 pesos mensuales', 'Menos de 2500 pesos mensuales'], diverging, noSabe=False)
paletas["P13"] = list2dictPalette(['Muy caro', 'Caro', 'Ni caro ni barato', 'Barato', 'Muy barato', 'No sabe'], diverging, noSabe=True)
paletas["P14"] = list2dictPalette(['Sí, han aumentado significativamente', 'Sí, han aumentado ligeramente', 'No, se han mantenido iguales', 'No sabe'], diverging, noSabe=True)

# Bloque Infraestructura y comodidades
paletas["P15"] = opinionColorDict
paletas["P16"] = list2dictPalette(['Falta de mantenimiento de estaciones y vehículos', 'Insuficiente cantidad de paradas/estaciones', 'Escasez de señalización', 'Insuficiencia en los horarios', 'Malas conexiones entre medios de transporte', 'Falta de seguridad de estaciones y vehículos', 'Mala accesibilidad para personas con movilidad reducida', 'No sabe'], diverging, noSabe=True)
paletas["P17"] = list2dictPalette(['WiFi gratuito en estaciones y vehículos', 'Cargadores USB en los vehículos', 'Pantallas de información en tiempo real en estaciones y vehículos', 'Buenas instalaciones de espera y descanso en las estaciones'], diverging, noSabe=False)

# Bloque Experiencia de usuario
paletas["P18"] = opinionColorDict
paletas["P19"] = list2dictPalette(['Sí, con frecuencia', 'Sí, ocasionalmente', 'No, rara vez', 'No, nunca he experimentado problemas de congestión o demoras'], diverging, noSabe=False)

# Bloque Seguridad al viajar
paletas["P20"] = list2dictPalette(['Sí, siempre me siento seguro/a', 'Sí, en su mayoría me siento seguro/a', 'A veces me siento seguro/a, a veces no', 'No me siento seguro/a la mayoría de las veces', 'No me siento seguro/a en absoluto'], diverging, noSabe=False)
paletas["P21"] = list2dictPalette([' Sí, en más de una ocasión', 'Sí, en una ocasión', 'No, nunca he presenciado un incidente de seguridad en el trasporte público', 'Prefiero no responder'], diverging, noSabe=False)
paletas["P22"] = list2dictPalette(['a) Sí, en más de una ocasión', 'b) Sí, en una ocasión', 'c) No, nunca he sido víctima de un incidente de seguridad en el trasporte público', 'd) Prefiero no responder'], diverging, noSabe=False)