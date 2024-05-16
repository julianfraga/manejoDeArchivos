from config import opinionColorDict, list2dictPalette, siNoColorDict, frecuenciaColorDict, diverging_mini,qualitative_strong,acuerdoBisColorDict

# comando:
siNoNoSabe = list2dictPalette(['Si', 'No', 'No sabe'], diverging_mini, noSabe=True)

paletas = {}

# Bloque Control
paletas["P09"] = frecuenciaColorDict

# Bloque De neuquen
paletas["P10"] = opinionColorDict
paletas["P11"] = opinionColorDict
paletas["P12"] = acuerdoBisColorDict
paletas["P13"] = opinionColorDict
paletas["P14"] = opinionColorDict
paletas["P15"] = list2dictPalette(['Mantenerla como en la actualidad aunque tenga que endeudarse la provincia', 'Negociar un nuevo acuerdo salarial qué pueda pagarse con los recursos de la provincia', 'Anularlo, porque es un privilegio que solo tienen los empleados estatales', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P16"] = acuerdoBisColorDict
paletas["P17"] = siNoNoSabe
paletas["P18"] = list2dictPalette(['Proteger sus derechos ancestrales', 'Iniciar un proceso de negociación con la partes del conflicto', 'Exigir el desalojo del predio e iniciar luego un proceso de negociación', 'No negociar con usurpadores y proceder al desalojo de la propiedad', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P19"] = acuerdoBisColorDict
paletas["P20"] = siNoNoSabe
paletas["P21"] = siNoNoSabe
paletas["P22"] = siNoNoSabe
paletas["P23"] = siNoNoSabe
paletas["P24"] = acuerdoBisColorDict
paletas["P25"] = acuerdoBisColorDict

# Bloque Imagen de dirigentes
paletas["P26"] = opinionColorDict
paletas["P27"] = opinionColorDict
paletas["P28"] = opinionColorDict
paletas["P29"] = opinionColorDict
paletas["P30"] = opinionColorDict
paletas["P31"] = opinionColorDict
paletas["P32"] = opinionColorDict
paletas["P33"] = opinionColorDict
paletas["P34"] = opinionColorDict
paletas["P35"] = opinionColorDict
paletas["P36"] = opinionColorDict
paletas["P37"] = opinionColorDict
paletas["P38"] = opinionColorDict
paletas["P39"] = opinionColorDict
paletas["P40"] = opinionColorDict