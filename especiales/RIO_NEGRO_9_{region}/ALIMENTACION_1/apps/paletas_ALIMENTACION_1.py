from especiales.ALIMENTACION_1.apps.cuestionario_ALIMENTACION_1 import cuestionario
from config import colores, opinionColorDict, list2dictPalette, qualitative_strong, ingresosColorDict

paletas = {}

#paletas["P04"] = list2dictPalette(['AMBA', 'Noroeste', 'Noreste', 'Litoral', 'Centro', 'Patagonia', 'Cuyo'], qualitative_strong, noSabe=False)
paletas["P05"] = ingresosColorDict
# Bloque Hábitos alimentarios y consumos regulares
paletas["P06"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P07"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P08"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P09"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P10"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P11"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P12"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P13"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P14"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P15"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P16"] = list2dictPalette(['Menos de un vaso al día', 'De 1 a 4 vasos al día', 'Más de 4 vasos al día', 'No consume agua'], "coolwarm", noSabe=False)
paletas["P17"] = list2dictPalette(['Agua embotellada/mineral', 'Agua de la canilla filtrada', 'Agua de la canilla directamente', 'Agua de bidón', 'No consume agua'], qualitative_strong, noSabe=True)
paletas["P18"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P19"] = list2dictPalette(['Vino', 'Cerveza', 'Destilados (whisky, vodka, ron, etc.)', 'Espumantes', 'Otros', 'No consume bebidas alcohólicas'], qualitative_strong, noSabe=True)
paletas["P20"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P21"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P22"] = list2dictPalette(['Asado', 'Pizza', 'Milanesa', 'Pastas', 'Empanadas', 'Hamburguesa', 'Ensaladas (de cualquier tipo)', 'Guiso (de lentejas, de arroz, locro o similares)', 'Polenta o similares (de cualquier tipo)', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P23"] = list2dictPalette(['Asado', 'Pizza', 'Milanesa', 'Pastas', 'Empanadas', 'Hamburguesa', 'Ensaladas (de cualquier tipo)', 'Guiso (de lentejas, de arroz, locro o similares)', 'Polenta o similares (de cualquier tipo)', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P24"] = list2dictPalette(['Helado', 'Tortas, tartas dulces y masas', 'Ensalada de frutas', 'Flan, budín de pan y similares', 'Dulce de batata, membrillo o similares', 'Facturas de todo tipo', 'Postres lácteos caseros o envasados de cualquier tipo', 'Gelatina', 'Panqueques, wafles y similares', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P25"] = list2dictPalette(['Helado', 'Tortas, tartas dulces y masas', 'Ensalada de frutas', 'Flan, budín de pan y similares', 'Dulce de batata, membrillo o similares', 'Facturas de todo tipo', 'Postres lácteos caseros o envasados de cualquier tipo', 'Gelatina', 'Panqueques, wafles y similares', 'Ninguno de los anteriores'], qualitative_strong, noSabe=True)
paletas["P26"] = list2dictPalette(['Vegetariano', 'Vegano', 'Dieta baja en carnes rojas', 'Dieta baja en carbohidratos', 'Dieta baja en azúcares', 'Kosher o Alal', 'Ninguna restricción alimentaria'], qualitative_strong, noSabe=True)

# Bloque Salud Alimentaria
paletas["P27"] = list2dictPalette(['Bajo peso', 'Sobrepeso', 'Obesidad', 'Normal', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P28"] = list2dictPalette(['Diabetes', 'Hipertensión', 'Enfermedades cardiovasculares', 'Celiaquía', 'Ninguna', 'No sabe'], qualitative_strong, noSabe=True)

# Bloque Cotidianidad 
paletas["P29"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P30"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P31"] = list2dictPalette(['Todos los días', 'Entre 4 y 6 días a la semana', 'Entre 1 y 3 días a la semana', 'Raramente', 'Nunca'], "coolwarm", noSabe=False)
paletas["P32"] = list2dictPalette(['Menos de 1 comida al día', '1 comida', '2 comidas', '3 comidas', '4 comidas', 'Más de 4 comidas'], "coolwarm", noSabe=False)

# Bloque Hábitos de compra y planificación de comidas
paletas["P33"] = list2dictPalette(['Precio', 'Calidad', 'Ambas', 'Compra sin ningún tipo de consideración'], qualitative_strong, noSabe=False)
paletas["P34"] = list2dictPalette(['Menos de 1 vez a la semana', '1 vez a la semana', 'Entre 1 a 4 veces a la semana', 'Más de 4 veces a la semana', 'No sabe'], "coolwarm", noSabe=True)
paletas["P35"] = list2dictPalette(['Hipermercado/Supermercado', 'Almacenes', 'Productores locales/mercados de cercanía/Ferias', 'Vía pública', 'No sabe'], qualitative_strong, noSabe=True)