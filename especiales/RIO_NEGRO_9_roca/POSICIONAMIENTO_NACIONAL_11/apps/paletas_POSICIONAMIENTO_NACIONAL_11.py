from especiales.POSICIONAMIENTO_NACIONAL_11.apps.cuestionario_POSICIONAMIENTO_NACIONAL_11 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, siNoColorDict, muchoPocoColorDict, internas, frecuenciaColorDict

# comando:


paletas = {}
# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = frecuenciaColorDict

# Bloque Preferencias electorales 
paletas["P07"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
                  'De Juntos por el Cambio': colores["cambiemos"],
                  'De los Liberales libertarios': colores["liberales"], 
                  'De la Izquierda': colores["izquierda"], 
                  'No sabe': colores["nosabe"]}

paletas["P08"] = {
    "A Sergio Massa": colores['peron3'],
    "A Daniel Scioli": colores['peron2'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],}

paletas["P09"] = {
    "A Horacio Rodríguez Larreta": colores['cambiemos3'],
    "A Patricia Bullrich": colores['cambiemos1'],
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros']}
# Bloque Escenarios políticos
paletas["P10"] = {'Sergio Massa por el Frente de Todos': colores["peronismo2"], 
                  'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 
                  'Juan Schiaretti por Juntos por el Cambio': colores["cambiemos2"], 
                  'Jose Luis Espert por Juntos por el Cambio': colores["cambiemos4"], 
                  'Javier Milei por la Libertad Avanza': colores["liberales"], 
                  'Al candidato del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P13"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"], 
                  'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 
                  'Juan Schiaretti por Juntos por el Cambio': colores["cambiemos2"], 
                  'Jose Luis Espert por Juntos por el Cambio': colores["cambiemos4"], 
                  'Javier Milei por la Libertad Avanza': colores["liberales"], 
                  'Al candidato del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P16"] = {'Sergio Massa por el Frente de Todos': colores["peronismo2"], 
                  'Wado de Pedro por el Frente de Todos': colores["peronismo"], 
                  'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 
                  'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 
                  'Javier Milei por la Libertad Avanza': colores["liberales"], 
                  'Al candidato del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P19"] = {'Sergio Massa por el Frente de Todos': colores["peronismo2"], 
                  'Wado de Pedro por el Frente de Todos': colores["peronismo"], 
                  'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 
                  'Javier Milei por la Libertad Avanza': colores["liberales"], 
                  'Al candidato del Frente de Izquierda': colores["izquierda"], 
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P22"] = {'Sergio Massa a presidente y Wado de Pedro a vicepresidente por el Frente de Todos con el apoyo de Cristina Kirchner y Alberto Fernandez': colores["peronismo"], 
                  'Patricia Bullrich a presidente y Ricardo Lopez Murphy a vicepresidente  por Juntos por el Cambio con el apoyo de Mauricio Macri y Alfredo Cornejo': colores["cambiemos"], 
                  'Horacio Rodríguez Larreta a presidente y Juan Schiaretti a vicepresidente  por Juntos por el Cambio, con el apoyo de Gerardo Morales y Martin Lousteau': colores["cambiemos3"],
                  'Jose Luis Espert a presidente y a su candidato a vicepresidente por Juntos por el Cambio': colores["cambiemos2"], 
                  'Javier Milei a presidente y Victoria Villarruel como vicepresidenta  por la Libertad Avanza': colores["liberales"],
                  'Al candidato a presidente y al candidato a vicepresidente del Frente de Izquierda': colores["izquierda"],
                  'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P25"] = {'Sergio Massa por el Frente de Todos': colores["peronismo2"], 'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P26"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"], 'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P27"] = {'Sergio Massa por el Frente de Todos': colores["peronismo2"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P28"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P29"] = {'Axel Kicillof por el Frente de Todos': colores["peronismo4"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P30"] = {'Sergio Massa  por el Frente de Todos': colores["peronismo"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P31"] = {'Sergio Massa  por el Frente de Todos': colores["peronismo"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P32"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P33"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P34"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P35"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P36"] = {'Axel Kicillof por el Frente de Todos': colores["peronismo4"], 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P37"] = {'Axel Kicillof por el Frente de Todos': colores["peronismo4"], 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei por la Libertad Avanza': colores["liberales"], 'Al candidato del Frente de Izquierda': colores["izquierda"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P38"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Sergio Massa por el Frente de Todos': colores["peronismo2"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P39"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Wado de Pedro por el Frente de Todos': colores["peronismo"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P40"] = {'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Sergio Massa por el Frente de Todos': colores["peronismo2"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P41"] = {'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Wado de Pedro  por el Frente de Todos': colores["peronismo"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P42"] = {'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P43"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P44"] = {'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Axel Kicillof por el Frente de Todos': colores["peronismo4"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P45"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Axel Kicillof por el Frente de Todos': colores["peronismo4"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P46"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos3"], 'Javier Milei por los liberales libertarios': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P47"] = {'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"], 'Javier Milei por los liberales libertarios': colores["liberales"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P48"] = {'Javier Milei por los liberales libertarios': colores["liberales"], 'Sergio Massa por el Frente de Todos': colores["peronismo2"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P49"] = {'Javier Milei por los liberales libertarios': colores["liberales"], 'Wado de Pedro  por el Frente de Todos': colores["peronismo"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P50"] = {'Javier Milei por los liberales libertarios': colores["liberales"], 'Daniel Scioli por el Frente de Todos': colores["peronismo3"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}

paletas["P51"] = {'Javier Milei por los liberales libertarios': colores["liberales"], 'Axel Kicillof por el Frente de Todos': colores["peronismo4"], 'En blanco': colores["blanco"], 'No sabe': colores["nosabe"]}


# Bloque Reach candidatos a presidente
paletas["P52"] = votaria
paletas["P53"] = votaria
paletas["P54"] = votaria
paletas["P55"] = votaria
paletas["P56"] = votaria
paletas["P57"] = votaria
paletas["P58"] = votaria
paletas["P59"] = votaria
paletas["P60"] = votaria

# Bloque Gestión e imágenes
paletas["P61"] = opinionColorDict
paletas["P62"] = opinionColorDict
paletas["P63"] = opinionColorDict
paletas["P64"] = opinionColorDict
paletas["P65"] = opinionColorDict
paletas["P66"] = opinionColorDict
paletas["P67"] = opinionColorDict
paletas["P68"] = opinionColorDict
paletas["P69"] = opinionColorDict
paletas["P70"] = siNoColorDict