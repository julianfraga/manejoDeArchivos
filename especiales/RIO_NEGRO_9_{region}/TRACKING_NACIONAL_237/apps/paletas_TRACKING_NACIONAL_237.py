from config import (
    colores, acuerdoBisColorDict, qualitative_strong, mediosColorDict, opinionColorDict, list2dictPalette,
    siNoColorDict, siNoNoSabeColorDict, internas, frecuenciaColorDict, comparacionColorDict,
    deudasColorDict, ingresosColorDict, problemaColorDict,diverging
)

# comando:


paletas = {}

# Bloque Control
paletas["P10"] = frecuenciaColorDict

#Bloque Coyuntyra 
paletas["P11"] = list2dictPalette(['El gobierno de Javier Milei','El gobierno de Alberto Fernández', 'Ambos','No sabe'], qualitative_strong, noSabe=True)
paletas["P12"] = list2dictPalette(['Dividirla en partes y transformarlas en varios decretos de necesidad y urgencia',
'Dividirlas en diferentes leyes que se puedan ir votando paulatinamente',
'Realizar un plebiscito sobre la necesidad del tratamiento de la ley ómnibus',
'Retirarla y no presentar nada',
'Volverla a presentar igual',
'No sabe'], qualitative_strong, noSabe=True)

paletas['P13'] = {"Javier Milei":colores['liberales_contraste'], "Los gobernadores": '#e31a1c', "No sabe":colores['nosabe']}

paletas['P14'] = acuerdoBisColorDict

# Bloque Coyuntura
paletas['P15'] = acuerdoBisColorDict
paletas['P16'] = list2dictPalette(['Muy positivo', 'Positivo', 'Ni positivo ni negativo', 'Negativo', 'Muy negativo', 'No sabe'], diverging, noSabe=True)
paletas['P17'] = siNoNoSabeColorDict
paletas['P18'] = list2dictPalette(['Salva muchas vidas',
'Logra disminuir la cantidad de abortos que se producen',
'Representa una reasignación del gasto público en algo más necesario',
'Deja desprotegidas a las mujeres que lo hacen clandestinamente',
'Representa un retroceso en la lucha de los derechos de las mujeres',
'No sabe'], qualitative_strong, noSabe=True)

paletas['P20'] = siNoNoSabeColorDict
paletas['P21'] = list2dictPalette([
'Logra disminuir los cargos militantes presentes en el estado',
'Evita la manipulación de la información por parte del estado',
'Representa una reasignación del gasto público en algo más necesario',
'Constituye una grave violación al derecho de libertad de expresión en Argentina',
'Es parte de la persecución ideológica',
'No sabe'], qualitative_strong, noSabe=True)

paletas['P23'] = siNoNoSabeColorDict 
paletas['P24'] = list2dictPalette([
'Es parte de una persecución ideológica',
'Deja a los argentinos sin una importante oficina de defensa de los derechos de los discapacitados',
'Representa una reasignación del gasto público en algo mas necesario',
'Logra disminuir los cargos militantes presentes en el estado',
'Contribuye a la libertad de pensamiento', 'No sabe'], qualitative_strong, noSabe=True)

# Bloque Político
paletas["P27"] = problemaColorDict

# Bloque Socioeconómico
paletas["P31"] = deudasColorDict
paletas["P32"] = ingresosColorDict
paletas["P33"] = opinionColorDict
paletas["P34"] = comparacionColorDict
paletas["P35"] = comparacionColorDict
paletas["P36"] = opinionColorDict
paletas["P37"] = comparacionColorDict
paletas["P38"] = comparacionColorDict
paletas["P39"] = opinionColorDict
paletas["P40"] = opinionColorDict
# Bloque Políticas públicas
paletas["P41"] = opinionColorDict
paletas["P42"] = opinionColorDict
paletas["P43"] = opinionColorDict

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
paletas["P59"] = opinionColorDict
paletas["P60"] = opinionColorDict
paletas["P61"] = opinionColorDict
paletas["P62"] = opinionColorDict
paletas["P63"] = opinionColorDict
paletas["P64"] = opinionColorDict
# Bloque General
paletas["P65"] = mediosColorDict
paletas["P66"] = opinionColorDict
paletas["P67"] = opinionColorDict
