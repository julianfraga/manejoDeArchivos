from especiales.FORMULAS_PRESIDENCIALES_1.apps.cuestionario_FORMULAS_PRESIDENCIALES_1 import cuestionario
from config import colores, list2dictPalette, qualitative_strong, diverging
import seaborn as sns
# comando:


paletas = {}

paletas["P05"] = {'A Sergio Massa a presidente y a Juan Manzur a vicepresidente por el Frente de Todos': colores["peronismo"],
                   'A Horacio Rodríguez Larreta a presidente y a Gerardo Morales a vicepresidente por Juntos por el Cambio': colores["cambiemos"],
                     'A Patricia Bullrich a presidenta y a Rodrigo De Loredo a vicepresidente por Juntos por el Cambio': colores["cambiemos3"],
                       'A Javier Milei a presidente y a Victoria Villarruel a vicepresidenta por La Libertad Avanza': colores["liberales"],
                         'A los candidatos a presidente y vicepresidente del Frente de Izquierda': colores["izquierda"],
                           'En blanco': colores["blanco"], 
                           'No sabe': colores["nosabe"]}

paletas["P06"] = {'A Sergio Massa a presidente y a Victoria Tolosa Paz a vicepresidenta por el Frente de Todos': colores["peronismo"],
                   'A Horacio Rodríguez Larreta a presidente y a Martín Lousteau a vicepresidente por Juntos por el Cambio': colores["cambiemos"],
                   'A Patricia Bullrich a presidenta y a Maximiliano Abad a vicepresidente por Juntos por el Cambio': colores["cambiemos3"],
                     'A Javier Milei a presidente y a Victoria Villarruel a vicepresidenta por La Libertad Avanza': colores["liberales"], 
                     'A los candidatos a presidente y vicepresidente del Frente de Izquierda': colores["izquierda"], 
                     'En blanco': colores["blanco"], 
                     'No sabe': colores["nosabe"]}

paletas["P07"] = {'A Sergio Massa a presidente y a Wado De Pedro a vicepresidente por el Frente de Todos': colores["peronismo"], 
                  'A Horacio Rodríguez Larreta a presidente y a Soledad Acuña a vicepresidenta por Juntos por el Cambio': colores["cambiemos"],
                    'A Patricia Bullrich a presidenta y a Ricardo López Murphy a vicepresidente por Juntos por el Cambio': colores["cambiemos3"],
                      'A Javier Milei a presidente y a Victoria Villarruel a vicepresidenta por La Libertad Avanza': colores["liberales"],
                        'A los candidatos a presidente y vicepresidente del Frente de Izquierda': colores["izquierda"],
                          'En blanco': colores["blanco"],
                            'No sabe': colores["nosabe"]}

votariaFormula = list2dictPalette(['Los votaría', 'Puede que los vote', 'Nunca los votaría', "No sabe"], diverging, noSabe = True)
paletas["P08"] = votariaFormula
paletas["P09"] = votariaFormula
paletas["P10"] = votariaFormula
paletas["P11"] = votariaFormula
paletas["P12"] = votariaFormula
paletas["P13"] = votariaFormula
paletas["P14"] = votariaFormula
paletas["P15"] = votariaFormula
paletas["P16"] = votariaFormula
paletas["P17"] = votariaFormula
paletas["P18"] = votariaFormula
paletas["P19"] = votariaFormula
paletas["P20"] = votariaFormula

paletas["P21"] = list2dictPalette(['Ricardo López Murphy',
 'Rodolfo Suárez',
 'Rodrigo de Loredo',
 'Maximiliano Abad',
 'Luis Naidenoff',
 'Martín Tetaz',
 'José Luis Espert',
 'No sabe'], palette = qualitative_strong, noSabe=True)


paletas["P22"] = list2dictPalette(['Gustavo Valdés',
 'Gerardo Morales',
 'María Eugenia Vidal',
 'Cristian Ritondo',
 'Emilio Monzó',
 'Martín Lousteau',
 'Juan Schiaretti',
 'Soledad Acuña',
 'No sabe'], palette = qualitative_strong, noSabe=True)

paletas["P23"] = list2dictPalette(['Wado De Pedro',
 'Victoria Tolosa Paz',
 'Sergio Uñac',
 'Fernanda Raverta',
 'Anabel Fernández Sagasti',
 'Gustavo Bordet',
 'Juan Manzur',
 'No sabe'], palette = qualitative_strong, noSabe=True)