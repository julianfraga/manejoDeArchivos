from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict, diverging,qualitative_strong

# comando:


paletas = {}

# Bloque Control
paletas["P04"] = list2dictPalette(['Gran excedente habitual', 'Gran excedente excepcional', 'Pequeño excedente habitual', 'Pequeño excedente excepcional', 'Alcanza gastos familia', 'No alcanza gastos familia', 'Solo NBFamiliares', 'No alcanza NBFamiliares', 'No sabe'], diverging, noSabe=True)

# Bloque Percepciones
paletas["P05"] = opinionColorDict
paletas["P06"] = opinionColorDict
paletas["P07"] = opinionColorDict
paletas["P08"] = opinionColorDict
paletas["P09"] = opinionColorDict
paletas["P10"] = opinionColorDict
paletas["P11"] = list2dictPalette(['Ha aumentado significativamente', 'Ha aumentado ligeramente', 'Se mantiene igual', 'Ha disminuido ligeramente', 'Ha disminuido significativamente'], diverging, noSabe=False)
paletas["P12"] = list2dictPalette(['Muy baja', 'Baja', 'Moderada', 'Alta', 'Muy alta'], diverging, noSabe=False)
paletas["P13"] = list2dictPalette(['Muy bajas', 'Bajas', 'Adecuadas', 'Altas', 'Muy altas'], diverging, noSabe=False)
paletas["P14"] = list2dictPalette(['No, ninguna dificultad', 'Alguna dificultad ocasional', 'Sí, dificultades frecuentes'], diverging, noSabe=False)
paletas["P15"] = list2dictPalette(['Sí, absolutamente', 'Sí, en cierta medida', 'No, en absoluto'], diverging, noSabe=False)
paletas["P16"] = list2dictPalette(['Reducir la inflación', 'Implementar reformas fiscales', 'Establecer políticas de control de precios', 'Reducir el gasto público', 'Estimular la inversión extranjera', 'Aumentar los subsidios a los servicios públicos'], qualitative_strong, noSabe=False)
paletas["P17"] = list2dictPalette(['Fomentar la competencia entre proveedores', 'Incrementar la inversión en infraestructura', 'Implementar políticas de subsidios focalizados en grupos vulnerable', 'Realizar auditorías periódicas a las empresas de servicios públicos'], qualitative_strong, noSabe=False)

# Bloque Medidas económicas
paletas["P18"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P19"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)
paletas["P20"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)
paletas["P21"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P22"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)
paletas["P23"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)
paletas["P24"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P25"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)
paletas["P26"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)
paletas["P27"] = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
paletas["P28"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)
paletas["P29"] = list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True)