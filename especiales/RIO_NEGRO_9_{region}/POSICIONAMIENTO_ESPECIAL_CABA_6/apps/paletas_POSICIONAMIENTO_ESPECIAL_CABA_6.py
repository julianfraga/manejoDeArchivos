from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, ingresosColorDict, frecuenciaColorDict, diverging,qualitative_strong

# comando:
opinionExtendidaColorDict = list2dictPalette(['Muy positiva', 'Positiva', 'Neutral', 'Algo negativa', 'Negativa', 'No sabe'], diverging, noSabe=True)
opinionExtendidaColorDict.update(list2dictPalette(['Muy positivo', 'Positivo', 'Neutral', 'Algo negativo', 'Negativo', 'No sabe'], diverging, noSabe=True))

paletas = {}
# Bloque Control
paletas["P06"] = muchoPocoColorDict
paletas["P07"] = list2dictPalette(['Siempre', 'Casi siempre', 'Casi nunca', 'Nunca, pero esta es una excepción'], diverging, noSabe=False)
paletas["P09"] = ingresosColorDict
paletas["P10"] = list2dictPalette(['Tiene Decidido que va a ir a votar', 'Tiene dudas sobre si va a ir a  votar', 'Tiene Decidido que no va a ir a votar'], diverging, noSabe=False)
## Bloque Coyuntura Política
paletas["P53"] = list2dictPalette(['Sergio Massa y Javier Milei', 'Patricia Bullrich y Javier Milei', 'Sergio Massa y Patricia Bullrich'], qualitative_strong, noSabe=False)
paletas["P54"] = list2dictPalette(['Muy buena', 'Buena', 'Regular', 'Mala', 'Muy mala'], diverging, noSabe=False)
paletas["P55"] = list2dictPalette(['Muy buena', 'Buena', 'Regular', 'Mala', 'Muy mala'], diverging, noSabe=False)
paletas["P56"] = list2dictPalette(['Muy buena', 'Buena', 'Regular', 'Mala', 'Muy mala'], diverging, noSabe=False)
paletas["P57"] = list2dictPalette(['Muy buena', 'Buena', 'Regular', 'Mala', 'Muy mala'], diverging, noSabe=False)
paletas["P58"] = list2dictPalette(['Muy buena', 'Buena', 'Regular', 'Mala', 'Muy mala'], diverging, noSabe=False)
paletas["P59"] = list2dictPalette(['Muy buena', 'Buena', 'Regular', 'Mala', 'Muy mala'], diverging, noSabe=False)
paletas["P60"] = list2dictPalette(['Ha aumentado significativamente', 'Ha aumentado ligeramente', 'Se mantiene igual', 'Ha disminuido ligeramente', 'Ha disminuido significativamente'], diverging, noSabe=False)
paletas["P61"] = list2dictPalette(['Muy baja', 'Baja', 'Moderada', 'Alta', 'Muy alta'], diverging, noSabe=False)
paletas["P62"] = list2dictPalette(['Muy bajas', 'Bajas', 'Adecuadas', 'Altas', 'Muy altas'], diverging, noSabe=False)
paletas["P63"] = list2dictPalette(['No, ninguna dificultad', 'Alguna dificultad ocasional', 'Sí, dificultades frecuentes'], diverging, noSabe=False)
paletas["P64"] = list2dictPalette(['Sí, absolutamente', 'Sí, en cierta medida', 'No, en absoluto'], diverging, noSabe=False)
paletas["P65"] = list2dictPalette(['Reducir la inflación', 'Implementar reformas fiscales', 'Establecer políticas de control de precios', 'Reducir el gasto público', 'Estimular la inversión extranjera', 'Aumentar los subsidios a los servicios públicos'], qualitative_strong, noSabe=False)
paletas["P66"] = list2dictPalette(['Fomentar la competencia entre proveedores', 'Incrementar la inversión en infraestructura', 'Implementar políticas de subsidios focalizados en grupos vulnerables', 'Realizar auditorías periódicas a las empresas de servicios públicos'], qualitative_strong, noSabe=False)

# Bloque Medidas económicas
paletas["P67"] = opinionExtendidaColorDict
paletas["P68"] = opinionExtendidaColorDict
paletas["P69"] = opinionExtendidaColorDict
paletas["P70"] = opinionExtendidaColorDict
paletas["P71"] = opinionExtendidaColorDict
paletas["P72"] = opinionExtendidaColorDict
paletas["P73"] = opinionExtendidaColorDict
paletas["P74"] = opinionExtendidaColorDict
paletas["P75"] = opinionExtendidaColorDict
paletas["P76"] = opinionExtendidaColorDict
paletas["P77"] = opinionExtendidaColorDict
paletas["P78"] = opinionExtendidaColorDict

# Bloque Control
paletas["P79"] = siNoColorDict