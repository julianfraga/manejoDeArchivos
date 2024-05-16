from config import colores, acuerdoBisColorDict, siNoNoSabeColorDict, list2dictPalette, siNoColorDict, diverging_mini, frecuenciaColorDict, diverging,qualitative_strong

# comando:

acuerdoMiniColorDict = list2dictPalette(['De acuerdo', 'Ni de acuerdo ni en desacuerdo', 'En desacuerdo', 'No sabe'], diverging, noSabe=True)

paletas = {}

## Bloque Control
paletas["P08"] = list2dictPalette([
    'Siempre',
    'Casi siempre',
    'Casi nunca',
    'Nunca, pero esta es una excepción'],
    diverging, noSabe=False)

# Bloque Bloque General
paletas["P09"] = acuerdoBisColorDict
paletas["P10"] = acuerdoMiniColorDict
paletas["P11"] = acuerdoMiniColorDict
paletas["P12"] = acuerdoMiniColorDict
paletas["P13"] = acuerdoMiniColorDict
paletas["P14"] = acuerdoMiniColorDict
paletas["P15"] = acuerdoMiniColorDict
paletas["P16"] = acuerdoMiniColorDict
paletas["P17"] = acuerdoMiniColorDict
paletas["P18"] = acuerdoMiniColorDict
paletas["P19"] = acuerdoMiniColorDict
paletas["P20"] = acuerdoMiniColorDict
paletas["P21"] = acuerdoMiniColorDict
paletas["P22"] = siNoNoSabeColorDict
paletas["P23"] = siNoNoSabeColorDict
paletas["P24"] = siNoNoSabeColorDict
paletas["P25"] = siNoNoSabeColorDict
paletas["P26"] = list2dictPalette(['A favor', 'En contra', 'No sabe'], diverging_mini, noSabe=True)