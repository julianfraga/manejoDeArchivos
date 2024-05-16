from especiales.RIO_NEGRO_1.apps.cuestionario_RIO_NEGRO_1 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, qualitative_strong, diverging

coloresRN = {
   'juntosSomos' : '#64e05c',
  'avancemos' : '#e36a27', 
  'unidadPopular' : '#0927bd'
}
intendentes_rn_9 = {'Liliana Alvarado por Nos Une Río Negro': colores["peronismo"], 
                  'Hernán Cáceres por Cambia Cinco Saltos': colores["cambiemos3"],
                    'Quique Rossi por Avancemos Cinco Saltos': coloresRN['avancemos'], 
                    'María Elena Vogel por Juntos Somos Río Negro': coloresRN['juntosSomos'], 
                    'Silvina Gastiazoro por Nueva Generación': colores["otros"],
                      'Miguel Vidal por el Partido Socialista': colores["izquierda"], 
                      'Martín Palumbo por Vamos Con Todos': colores["peron3"], 
                      'Norberto Soto por la UCR': colores["cambiemos_ucr"], 
                      'No sabe': colores["nosabe"]}
intendentes_rn_10 = {'A Liliana Alvarado por Nos Une Río Negro con el apoyo del kirchnerismo, Martín Doñate y La Cámpora': colores["peronismo"],
                  'A Hernán Cáceres por Cambia Cinco Saltos con el apoyo de una parte del PRO': colores["cambiemos3"],
                  'A Quique Rossi  por Avancemos Cinco Saltos': coloresRN['avancemos'],
                  'A María Elena Vogel por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                  'A Silvina Gastiazoro por Nueva Generación': colores["otros"], 
                  'A Miguel Vidal por el Partido Socialista con el apoyo de una parte del PRO y de Anibal Tortoriello': colores["izquierda"], 
                  'A Martín Palumbo por Vamos Con Todos con el apoyo del Movimiento Evita y de Silvia Horne': colores["peron3"], 
                  'A Norberto Soto por la UCR con el apoyo del radicalismo': colores["cambiemos_ucr"], 
                  'No sabe': colores["nosabe"]}

paletas = {}
paletas["P05"] = list2dictPalette(['Siempre', 'Casi siempre', 'Casi nunca', 'Nunca, pero esta es una excepción'], "coolwarm", noSabe=False)

paletas["P06"] = {'Alberto Weretilneck y Pedro Pesatti': coloresRN['juntosSomos'],
                   'Aníbal Tortoriello y Juan Pablo Álvarez Guerrero': colores["cambiemos3"],
                   'Silvia Horne y Leandro Costa Brutten': colores["peron3"],
                  'Sergio Ariel Rivero y Sylvia Margarita Astuena': colores["liberales"], 
                   'Gustavo Casas y Luisa Villarroel': colores["peron1"], 
                   'Aníbal Zamaro y Marcela Roca': coloresRN['unidadPopular'], 
                   'A otros candidatos': colores["otros"],
                   'Votó en blanco': colores["blanco"], 
                   'No sabe': colores["nosabe"]}

paletas["P07"] = list2dictPalette(['Muy de acuerdo', 'De acuerdo', 'Ni a favor ni en contra', 'En desacuerdo', 'Muy en desacuerdo', 'No sabe'], diverging, noSabe=True)
paletas["P08"] = opinionColorDict
paletas["P09"] = intendentes_rn_9 
paletas["P09_convoto"] = intendentes_rn_9 
paletas["P09_domiciliarias"] = intendentes_rn_9 
paletas["P09_imputadas"] = intendentes_rn_9 
paletas["P09_telefonicas"] = intendentes_rn_9 

paletas["P10"] = intendentes_rn_10
paletas["P10_convoto"] = intendentes_rn_10 
paletas["P10_domiciliarias"] = intendentes_rn_10 
paletas["P10_imputadas"] = intendentes_rn_10 
paletas["P10_telefonicas"] = intendentes_rn_10 

#paletas["P13"] = {'A Liliana Alvarado por Nos Une Río Negro con el apoyo del kirchnerismo, Martín Doñate y La Cámpora': colores["peronismo"],
#                  'A Hernán Cáceres por Cambia Cinco Saltos con el apoyo de una parte del PRO': colores["cambiemos"],
#                  'A Quique Rossi  por Avancemos Cinco Saltos': coloresRN['avancemos'],
#                  'A María Elena Vogel por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
#                  'A Silvina Gastiazoro por Nueva Generación': colores["otros"], 
#                  'A Miguel Vidal por el Partido Socialista con el apoyo de una parte del PRO y de Anibal Tortoriello': colores["izquierda"], 
#                  'A Martín Palumbo por Vamos Con Todos con el apoyo del Movimiento Evita y de Silvia Horne': colores["peron3"], 
#                  'A Norberto Soto por la UCR con el apoyo del radicalismo': colores["cambiemos_ucr"], 
#                  'No sabe': colores["nosabe"]}
paletas["P11"] = votaria
paletas["P12"] = votaria
paletas["P13"] = votaria
paletas["P14"] = votaria
paletas["P15"] = votaria
paletas["P16"] = votaria
paletas["P17"] = votaria
paletas["P18"] = votaria
