def infer_politica(opcion):
    dic = {
        'peronismo': ['massa', 'kicillof', 'juntos avancemos', 'por la patria', 'nos une', 'peronismo', 'fdt', 'evita', 'kirchnerismo', 'cfk'],
        'cambiemos': ['bullrich', 'juntos por el cambio', 'pro', 'macrismo', 'jxc'],
        'liberales': ['milei', 'libertad', 'villarruel'],
        'izquierda': ['izquierda', 'socialismo', 'bregman'],
        'blanco': ['en blanco'],
        'nosabe': ['no sabe', 'no se']
    }

    for color, palabras in dic.items():
        for palabra in palabras:
            if palabra in opcion.lower():
                return color
    return 'otros'

def infer_paleta_else(paleta):
    if paleta == 'sino':
        return 'paletas["{pregunta}"] = siNoColorDict'
    elif paleta == 'sinonosabe':
        return 'paletas["{pregunta}"] = siNoNoSabeColorDict'
    elif paleta in ['frecuencia', 'freq', 'frec']:
        return 'paletas["{pregunta}"] = frecuenciaColorDict'
    elif paleta == 'mucho':
        return 'paletas["{pregunta}"] = muchoPocoColorDict'
    elif paleta in ['problema', 'deuda', 'ingresos', 'opinion', 'comparacion', 'medios']:
        return f'paletas["{pregunta}"] = {paleta}ColorDict'
    return False

def infer_paleta(opciones_todas, cuestionario):
    bloque = ''
    for _, row in cuestionario.iterrows():
        pregunta = row['codigo']
        paleta = row['paleta']
        if bloque != row['bloque']:
            bloque = row['bloque']
            print(f'\n# Bloque {bloque}')
        
        if paleta == "imagen":
            print(f'paletas["{pregunta}"] = opinionColorDict')
        elif paleta == "politica":
            apariciones = {'peronismo': 0, 'cambiemos': 0, 'liberales': 0, 'izquierda': 0}
            p = {}
            for opcion in opciones_todas[pregunta]:
                politica = infer_politica(opcion)
                apariciones[politica] += 1
                p[opcion] = f'colores["{politica}{apariciones[politica] if apariciones[politica] > 1 else ""}"]'
            print(f'paletas["{pregunta}"] = {repr(p).replace("colores","colores").replace("]", "]")}')
        else:
            string_salida = infer_paleta_else(paleta.lower())
            if string_salida:
                print(string_salida.format(pregunta=pregunta))
            else:
                opciones_lower = [opcion.lower() for opcion in opciones_todas[pregunta]]
                nosabe = "no sabe" in opciones_lower or "no se" in opciones_lower
                default_paleta = 'qualitative_strong' if 'quali' in paleta else 'diverging'
                print(f'paletas["{pregunta}"] = list2dictPalette({repr(opciones_todas[pregunta])}, {default_paleta}, noSabe={nosabe})')
