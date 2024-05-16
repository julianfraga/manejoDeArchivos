from especiales.PPERON_3.apps.cuestionario_PPERON_3 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, frecuenciaColorDict

coloresRN = {
   'juntosSomos' : '#64e05c', #verde
  'avancemos' : '#e36a27', 
  'unidadPopular' : '#0927bd',
  'unidos' : '#ffa200' #naranja
}
paletas = {}
# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict
paletas["P07"] = {'A Blanca Cantero por el Frente de Todos': colores["peronismo"], 
                  'A Guido Giana por Juntos por el Cambio': colores["cambiemos"], 
                  'A Manuel Toffanelli por Base Ciudadana': colores["peron2"], 
                  'A Malco Muller por Consenso Federal': colores["peronismo_nok"], 
                  'A Marcelo Gomez por el Frente de Izquierda': colores["izquierda"], 
                  'A Victor Rengifo por Compromiso Vecinal': colores["cambiemos"], 
                  'Votó en blanco': colores["blanco"], 'No fue a votar': colores["otros"], 
                  'No sabe': colores["nosabe"]}


# Bloque Intención de voto por espacio político 
paletas["P08"] = {'Al candidato del Frente de Todos': colores["peronismo"], 
                  'Al candidato de Juntos por el Cambio': colores["cambiemos"], 
                  'Al candidato de los liberales - libertarios': colores["liberales"], 
                  'Al candidato de la Izquierda': colores["izquierda"], 
                  'A otro candidato': colores["otros"], 'No sabe': colores["nosabe"]}

paletas["P09"] = {'A Blanca Cantero por el Frente de Todos': colores["peron1"], 
                  'A Federico García por el Frente de Todos': colores["peron2"], 
                  'A Victor Rengifo por Juntos por el Cambio': colores["cambiemos"], 
                  'A Mauro Arranz por Juntos por el Cambio': colores["cambiemos3"], 
                  'A Anibal Regueiro por un partido vecinal': colores["otros"], 
                  'A Eduardo Guardia por La Libertad Avanza': colores["liberales"], 
                  'A Miguel Coria por el Frente de Izquierda': colores["izquierda"], 
                  'No sabe': colores["nosabe"]}
paletas["P09_imputadas"] = paletas["P09"]

paletas["P12"] = {'A Blanca Cantero por el Frente de Todos con el apoyo de Sergio Massa': colores["peron1"], 
                  'A Federico García por el Frente de Todos con el apoyo de La Cámpora': colores["peron2"], 
                  'A Victor Rengifo por Juntos por el Cambio con el apoyo de Patricia Bullrich': colores["cambiemos"], 
                  'A Mauro Arranz por Juntos por el Cambio con el apoyo de Horacio Rodriguez Larreta': colores["cambiemos3"], 
                  'A Anibal Regueiro por un partido vecinal': colores["otros"], 
                  'A Eduardo Guardia por La Libertad Avanza con el apoyo de Javier Milei': colores["liberales"], 
                  'A Miguel Coria por el Frente de Izquierda con el apoyo de Myriam Bregman': colores["izquierda"], 
                  'No sabe': colores["nosabe"]}

paletas["P12_imputadas"] = paletas["P12"]
# Bloque Reach de intención de voto
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
paletas["P19"] = votaria
paletas["P20"] = votaria
paletas["P21"] = votaria

# Bloque control
paletas["P22"] = siNoColorDict