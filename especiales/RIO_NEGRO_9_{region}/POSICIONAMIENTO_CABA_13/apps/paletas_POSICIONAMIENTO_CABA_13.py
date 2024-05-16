from especiales.POSICIONAMIENTO_CABA_13.apps.cuestionario_POSICIONAMIENTO_CABA_13 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict

# comando:


paletas = {}
# Bloque Sociodemográfico
paletas["P05"] = frecuenciaColorDict
paletas["P06"] = muchoPocoColorDict

# Bloque Preferencias electorales 
paletas["P07"] = {'Del Frente de Todos y el peronismo': colores["peronismo"], 'De Juntos por el Cambio': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}

paletas["P08"] = {'A Leandro Santoro': colores["peron1"], 'A Matias Lammens': colores["peron2"], 'A Mariano Recalde': colores["peron3"]}

paletas["P09"] = {'A Jorge Macri': colores["cambiemos3"], 'A Martín Lousteau': colores["cambiemos_ucr"], 'A Ricardo López Murphy': colores["cambiemos"]}


# Bloque Escenarios políticos
paletas["P10"] = {'Jorge Macri por Juntos por el Cambio': colores["cambiemos3"], 
                  'Martín Lousteau  por Juntos por el Cambio': colores['cambiemos_ucr'], 
                  'Ricardo López Murphy  por Juntos por el Cambio': colores["cambiemos"], 
                  'Leandro Santoro por el Frente de Todos': colores["peron1"], 
                  'Mariano Recalde por el Frente de Todos': colores["peron3"], 
                  'Pedro Rosemblat por el Frente de Todos': colores["peron2"], 
                  'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                  'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13"] = {'Jorge Macri por Juntos por el Cambio': colores["cambiemos3"], 
                  'Martín Lousteau  por Juntos por el Cambio': colores['cambiemos_ucr'], 
                  'Leandro Santoro por el Frente de Todos': colores["peron1"], 
                  'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                  'Al candidato del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P16"] = {'Jorge Macri por Juntos por el Cambio': colores["cambiemos3"],
                   'Martín Lousteau  por Juntos por el Cambio': colores['cambiemos_ucr'], 
                   'Ricardo López Murphy  por Juntos por el Cambio': colores["cambiemos"], 
                   'Leandro Santoro por el Frente de Todos': colores["peron1"], 
                   'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                   'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P19"] = {'Jorge Macri por Juntos por el Cambio': colores["cambiemos3"], 
                  'Leandro Santoro por el Frente de Todos': colores["peron1"], 
                  'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                  'Al candidato del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22"] = {'Martín Lousteau  por Juntos por el Cambio': colores['cambiemos_ucr'],
                   'Leandro Santoro por el Frente de Todos': colores["peron1"], 
                   'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                   'Al candidato del Frente de Izquierda': colores["izquierda"], 
                   'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P25"] = {'Ricardo López Murphy  por Juntos por el Cambio': colores["cambiemos"],
                   'Leandro Santoro por el Frente de Todos': colores["peron1"], 
                   'Ramiro Marra por la Libertad Avanza': colores["liberales"], 
                   'Al candidato del Frente de Izquierda': colores["izquierda"],
                     'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P26"] = {'Jorge Macri por Juntos por el Cambio': colores["cambiemos3"], 
                  'Leandro Santoro por el Frente de Todos': colores["peron1"],
                    'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Martín Lousteau por Juntos por el Cambio': colores["cambiemos"],
                   'Leandro Santoro por el Frente de Todos': colores["peron1"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Ricardo López Murphy por Juntos por el Cambio': colores["cambiemos"], 
                  'Leandro Santoro por el Frente de Todos': colores["peron1"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach de intención de voto
paletas["P29"] = votaria
paletas["P30"] = votaria
paletas["P31"] = votaria
paletas["P32"] = votaria
paletas["P33"] = votaria
paletas["P34"] = votaria
paletas["P35"] = votaria

# Bloque control
paletas["P36"] = siNoColorDict