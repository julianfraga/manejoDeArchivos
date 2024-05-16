from especiales.SANTA_FE1_1.apps.cuestionario_SANTA_FE1_1 import cuestionario
from config import colores, votaria, muchoPocoColorDict, frecuenciaColorDict, siNoColorDict


paletas = {}
# Bloque Intención de voto por espacio político 

# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Escenarios políticos santa fe 2023
paletas["P09"] = {'De Unión por la Patria': colores["peronismo"], 'De Juntos por el Cambio': colores["cambiemos"], 
                  'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 
                  'Hacemos por Nuestro País': colores["otros"], 'otro': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P10"] = {'Unidos para Cambiar Santa Fe': colores["cambiemos"], 'Juntos Avancemos': colores["peronismo"],
                   'De los liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Marcelo Lewandowski a gobernador y Silvina Patricia Frana a vicegobernadora por Juntos Avancemos': colores["peron1"], 
                     'Marcos Cleri a gobernador y Alejandra del Huerto Obeid a vicegobernadora por Juntos Avancemos': colores["peron2"], 
                     'Leandro Busatto a gobernador y Alejandra Gómez Sáenz a vicegobernadora por Juntos Avancemos': colores["peron3"], 
                     'Eduardo Toniolli a gobernador y Leticia Quagliaro a vicegobernadora por Juntos Avancemos': colores["peron4"],
                     'Carolina Losada a gobernadora y Federico Angelini a vicegobernador por Unidos para Cambiar Santa Fe': colores["cambiemos"],
                   'Maximiliano Pullaro a gobernador y Gisela Scaglia a vicegobernadora por Unidos para Cambiar Santa Fe': colores["cambiemos2"],
                     'Mónica Fein a gobernadora y Eugenio Fernández a vicegobernador por Unidos para Cambiar Santa Fe': colores["cambiemos3"], 
                    'Alguno de los candidatos a gobernador y vicegobernador de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas["P11_imputada"] = {'Marcelo Lewandowski a gobernador y Silvina Patricia Frana a vicegobernadora por Juntos Avancemos': colores["peron1"], 
                     'Marcos Cleri a gobernador y Alejandra del Huerto Obeid a vicegobernadora por Juntos Avancemos': colores["peron2"], 
                     'Leandro Busatto a gobernador y Alejandra Gómez Sáenz a vicegobernadora por Juntos Avancemos': colores["peron3"], 
                     'Eduardo Toniolli a gobernador y Leticia Quagliaro a vicegobernadora por Juntos Avancemos': colores["peron4"],
                     'Carolina Losada a gobernadora y Federico Angelini a vicegobernador por Unidos para Cambiar Santa Fe': colores["cambiemos"],
                   'Maximiliano Pullaro a gobernador y Gisela Scaglia a vicegobernadora por Unidos para Cambiar Santa Fe': colores["cambiemos2"],
                     'Mónica Fein a gobernadora y Eugenio Fernández a vicegobernador por Unidos para Cambiar Santa Fe': colores["cambiemos3"], 
                    'Alguno de los candidatos a gobernador y vicegobernador de la Izquierda': colores["izquierda"], 'En blanco': colores["blanco"]}

paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria
paletas["P22"] = votaria
paletas["P23"] = votaria
paletas["P24"] = votaria
paletas["P25"] = votaria
paletas["P26"] = votaria
paletas["P27"] = votaria
paletas["P28"] = votaria
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = votaria
paletas["P32"] = votaria
paletas["P33"] = votaria
paletas["P34"] = votaria
#control
paletas["P35"] = siNoColorDict