from especiales.ALIMENTACION_2.apps.cuestionario_ALIMENTACION_2 import cuestionario
from config import colores, opinionColorDict, list2dictPalette, qualitative_strong, ingresosColorDict, siNoColorDict, diverging, diverging_mini,acuerdoColorDict

paletas = {}
frecuenciaSemanalColorDict = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)

paletas["P04"] = ingresosColorDict
# Bloque Hábitos alimentarios y consumos regulares

paletas["P05"] =frecuenciaSemanalColorDict
paletas["P06"] =frecuenciaSemanalColorDict
paletas["P07"] =frecuenciaSemanalColorDict
paletas["P08"] =frecuenciaSemanalColorDict
paletas["P09"] =frecuenciaSemanalColorDict
paletas["P10"] =frecuenciaSemanalColorDict
paletas["P11"] =frecuenciaSemanalColorDict
paletas["P12"] =frecuenciaSemanalColorDict
paletas["P13"] =frecuenciaSemanalColorDict
paletas["P14"] =frecuenciaSemanalColorDict
paletas["P15"] = list2dictPalette(['Menos de un vaso al día', 'De 1 a 4 vasos al día', 'Más de 4 vasos al día', 'No consume agua'], "coolwarm", noSabe=True)
paletas["P16"] = list2dictPalette(['Agua embotellada/mineral', 'Agua de la canilla filtrada', 'Agua de la canilla directamente', 'Agua de bidón', 'No consume agua'], qualitative_strong, noSabe=True)
paletas["P17"] =frecuenciaSemanalColorDict
paletas["P18"] = list2dictPalette(['Vino', 'Cerveza', 'Destilados (whisky, vodka, ron, etc.)', 'Espumantes', 'Otros', 'No consume bebidas alcohólicas'], qualitative_strong, noSabe=True)
paletas["P19"] =frecuenciaSemanalColorDict
paletas["P20"] =frecuenciaSemanalColorDict
paletas["P21"] =frecuenciaSemanalColorDict
paletas["P22"] = list2dictPalette(['Asado', 'Pizza', 'Milanesa', 'Pastas', 'Empanadas', 'Hamburguesa', 'Ensaladas (de cualquier tipo)', 'Guiso (de lentejas, de arroz, locro o similares)', 'Polenta o similares (de cualquier tipo)', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P23"] = list2dictPalette(['Asado', 'Pizza', 'Milanesa', 'Pastas', 'Empanadas', 'Hamburguesa', 'Ensaladas (de cualquier tipo)', 'Guiso (de lentejas, de arroz, locro o similares)', 'Polenta o similares (de cualquier tipo)', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P24"] = list2dictPalette(['Helado', 'Tortas, tartas dulces y masas', 'Ensalada de frutas', 'Flan, budín de pan y similares', 'Dulce de batata, membrillo o similares', 'Facturas de todo tipo', 'Postres lácteos caseros o envasados de cualquier tipo', 'Gelatina', 'Panqueques, wafles y similares', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P25"] = list2dictPalette(['Helado', 'Tortas, tartas dulces y masas', 'Ensalada de frutas', 'Flan, budín de pan y similares', 'Dulce de batata, membrillo o similares', 'Facturas de todo tipo', 'Postres lácteos caseros o envasados de cualquier tipo', 'Gelatina', 'Panqueques, wafles y similares', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P26"] = list2dictPalette(['Vegetariano', 'Vegano', 'Dieta baja en carnes rojas', 'Dieta baja en carbohidratos', 'Dieta baja en azúcares', 'Kosher o Alal', 'Ninguna restricción alimentaria'], qualitative_strong, noSabe=True)# Bloque Etiquetado frontal

# Bloque Etiquetado frontal
paletas["P27"] = list2dictPalette(['Si', 'Parcialmente', 'No'], diverging, noSabe=False)
paletas["P28"] = list2dictPalette(['Si', 'Si, pero solo en algunos de ellos', 'No'], diverging, noSabe=False)
paletas["P29"] = siNoColorDict
paletas["P30"] = list2dictPalette(['Muy de acuerdo', 'Parcialmente de acuerdo', 'No'], diverging, noSabe=False)

# Bloque Salud alimentaria
paletas["P31"] = list2dictPalette(['Bajo peso', 'Sobrepeso', 'Obesidad', 'Normal', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P32"] = list2dictPalette(['Diabetes', 'Hipertensión', 'Enfermedades cardiovasculares', 'Celiaquía', 'Ninguna', 'No sabe'], qualitative_strong, noSabe=True)

# Bloque Cotidianidad 
paletas["P33"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'],"coolwarm", noSabe=False)
paletas["P34"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P35"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P36"] = list2dictPalette(['Menos de 1 comida al día', '1 comida', '2 comidas', '3 comidas', '4 comidas', 'Más de 4 comidas'], "coolwarm", noSabe=False)

# Bloque Sobre hábitos de compra y planificación de comidas
paletas["P37"] = list2dictPalette(['Precio', 'Calidad', 'Cantidad de sellos presentes en el producto', 
                                   'Precio y calidad', 'Calidad y cantidad de sellos presentes en el producto',"Precio y cantidad de sellos presentes en el producto",
                                    'Precio, calidad y cantidad de sellos presentes en el producto', 'Compra sin ningún tipo de consideración'], qualitative_strong, noSabe=False)

paletas["P38"] = list2dictPalette(['Menos de 1 vez a la semana', '1 vez a la semana', 'Entre 1 a 4 veces a la semana', 'Más de 4 veces a la semana', 'No sabe'], "coolwarm", noSabe=True)
paletas["P39"] = list2dictPalette(['Hipermercado/Supermercado', 'Almacenes', 'Productores locales/mercados de cercanía/Ferias', 'Vía pública', 'No sabe'], qualitative_strong, noSabe=True)