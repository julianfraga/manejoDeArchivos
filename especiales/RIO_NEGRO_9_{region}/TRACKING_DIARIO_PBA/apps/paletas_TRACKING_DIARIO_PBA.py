from config import colores, votaria, problemaColorDict, list2dictPalette, siNoColorDict, irAVotarColorDict, seguridadVotoColorDict, frecuenciaColorDict

# comando:


paletas = {}
paletas['P09'] = {
"Unión por la Patria": colores['peron1'],
"Juntos por el Cambio": colores['cambiemos1'],
"De los liberales libertarios": colores['liberales'],
"De la Izquierda": colores['izquierda'],
"Hacemos por nuestro país": colores['peronismo_nok'],
"Otro" : colores['otros'],
"En blanco" : colores['blanco'],
'No sabe': colores['nose']}

paletas['P09_imputada'] =paletas['P09']
paletas['P09_imputada_votan'] =paletas['P09']
paletas['P12'] = {'Sergio Massa a Presidente y Agustin Rossi a Vicepresidente por Union por la Patria': colores["peron1"], 
'Juan Grabois a Presidente y Paula Abal Medina a Vicepresidente por Union por la Patria': colores["peron2"], 
'Patricia Bullrich a Presidente y Luis Petri a Vicepresidente por Juntos por el Cambio': colores["cambiemos"], 
'Horacio Rodríguez Larreta a Presidente y Gerardo Morales a Vicepresidente por Juntos por el Cambio': colores["cambiemos3"], 
'Javier Milei a Presidente y Victoria Villarruel a Vicepresidente por la Libertad Avanza': colores["liberales"], 
'Los candidatos a presidente y vicepresidente de las diferentes opciones de izquierda': colores["izquierda"], 
'Juan Schiaretti a presidente y Florencio Randazzo a vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 
'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas['P12_imputada'] = paletas['P12']
paletas['P12_imputada_votan'] = paletas['P12']

paletas['P19'] = {'Sergio Massa Presidente, Agustin Rossi Vicepresidente , Axel Kicillof gobernador y Veronica Magario vicegobernadora; por Union por la Patria': colores["peron1"], 
                  'Juan Grabois Presidente, Paula Abal Medina Vicepresidente, Axel Kicillof gobernador y Veronica Magario vicegobernadora; por Union por la Patria': colores["peron2"], 
                  'Patricia Bullrich Presidenta, Luis Petri Vicepresidente, Nestor Grindetti gobernador y Miguel Fernandez vicegobernador; por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta Presidente, Gerardo Morales Vicepresidente, Diego Santilli gobernador y Gustavo Posse vicegobernador; por Juntos por el Cambio': colores["cambiemos3"],
                    'Javier Milei Presidente, Victoria Villarruel Vicepresidenta, Carolina Piparo gobernadora y Francisco Oneto vicegobernador; por la Libertad Avanza': colores["liberales"], 
                    'Los candidatos a presidente, vicepresidente, gobernador y vicegobernador de las diferentes opciones de izquierda': colores["izquierda"], 
                    'Juan Schiaretti a presidente y Florencio Randazzo vicepresidente por Hacemos por Nuestro Pais': colores["peronismo_nok"], 
                    'Otros': colores["otros"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}
paletas['P19_imputada'] = paletas['P19']

paletas['P22'] = seguridadVotoColorDict
paletas['P22_votan'] = paletas['P22']

paletas['P23'] = irAVotarColorDict
paletas['P23_votan'] = paletas['P23'] 
paletas['P34'] = problemaColorDict