from especiales.INSEGURIDAD.apps.cuestionario_INSEGURIDAD import cuestionario
from config import colores,list2dictPalette, qualitative_strong, ingresosColorDict, siNoColorDict, diverging

paletas = {}


paletas["P04"] = ingresosColorDict

# Bloque Sociodemográfico

# Bloque Delitos a la propiedad
paletas["P05"] = siNoColorDict
paletas["P06"] = list2dictPalette(['Robo en vivienda, en su presencia', 'Robo en vivienda, en su ausencia', 'Robo de auto', 'Robo de moto', 'Robo de bicicleta', 'Vandalismo, como pintura de paredes, rotura de vidrios, o similares', 'Otro tipo de delito a la propiedad'], qualitative_strong, noSabe=True)
paletas["P07"] = list2dictPalette(['Muy seguro', 'Algo seguro', 'Seguro', 'Algo inseguro', 'Inseguro', 'Muy inseguro'], diverging, noSabe=False)
paletas["P08"] = list2dictPalette(['Han aumentado en el último mes', 'Han disminuido en el ultimo mes', 'Se mantienen igual que el mes anterior', 'No sabe'], qualitative_strong, noSabe=True)

# Bloque Delitos en la vía pública
paletas["P09"] = siNoColorDict

paletas["P10"] = list2dictPalette(['Hurto', 'Robo con violencia', 'Agresión física', 'Acoso verbal o intimidación', 'Otros delitos en la vía pública'], qualitative_strong, noSabe=True)
paletas["P11"] = list2dictPalette(['Muy seguro', 'Algo seguro', 'Seguro', 'Algo inseguro', 'Inseguro', 'Muy inseguro'], diverging, noSabe=False)
paletas["P12"] = list2dictPalette(['Han aumentado en el último mes', 'Han disminuido en el último mes', 'Se mantienen igual que el mes anterior', 'No sabe'], diverging, noSabe=True)

# Bloque Políticas públicas de seguridad
paletas["P13"] = list2dictPalette(['Mayor presencia de policía en las calles', 'Presencia de Gendarmería en las calles', 'Cámaras de seguridad en el espacio público como calles, plazas, parques, y similares', 'Más iluminación en espacios públicos', 'Capacitación a las fuerzas de seguridad para la prevención del delito', 'Mayor inversión en equipamiento y tecnología para las fuerzas de seguridad, como mejores patrulleros, armas, uniformes, chalecos, elementos de comunicación, etc', 'Todas las anteriores', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P14"] = list2dictPalette(['Mayor presencia de policía en las calles', 'Presencia de Gendarmería en las calles', 'Cámaras de seguridad en el espacio público como calles, plazas, parques, y similares', 'Más iluminación en espacios públicos', 'Capacitación a las fuerzas de seguridad para la prevención del delito', 'Mayor inversión en equipamiento y tecnología ara las fuerzas de seguridad, como mejores patrulleros, armas, uniformes, chalecos, elementos de comunicación, etc', 'Todas las anteriores', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P15"] = list2dictPalette(['El Gobierno Nacional', 'El Gobierno Provincial', 'El Municipio', 'Todos los niveles de gobierno son igualmente responsables', 'No sabe'], qualitative_strong, noSabe=True)