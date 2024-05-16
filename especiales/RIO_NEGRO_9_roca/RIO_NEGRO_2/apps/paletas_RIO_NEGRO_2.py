from especiales.RIO_NEGRO_2.apps.cuestionario_RIO_NEGRO_2 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, qualitative_strong, diverging

coloresRN = {
   'juntosSomos' : '#64e05c', #verde
  'avancemos' : '#e36a27', 
  'unidadPopular' : '#0927bd',
  'unidos' : '#ffa200' #naranja
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

paletas["P07"] = {'Cambia Bariloche': colores["cambiemos"], 'Juntos Somos Río Negro': coloresRN["juntosSomos"], 
                  'Unidos Bariloche': coloresRN["unidos"], 'Podemos Bariloche': colores["otros"], 
                  'Vamos con Todos': colores["peron3"], 'Nos Une Río Negro': colores["peron1"], 
                  'No sabe': colores["nosabe"]}

# Bloque Escenarios políticos bariloche 2023
paletas["P08"] = {'Gastón Vega por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"],
                   'Agustín Domingo por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                     'Arabella Carreras por Unidos Bariloche': coloresRN["unidos"], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"], 
                     'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"], 
                     'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P09"] = {'Carlos Aristegui por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"], 
                  'Agustín Domingo por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                    'Arabella Carreras por Unidos Bariloche': coloresRN["unidos"], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"], 
                    'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"], 
                    'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P10"] = {'Gastón Vega por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"],
                   'Juan Pablo Muena por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck':coloresRN['juntosSomos'], 
                   'Arabella Carreras por Unidos Bariloche': coloresRN["unidos"], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                     'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"], 
                     'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P11"] = {'Carlos Aristegui por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"],
                  'Juan Pablo Muena por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                    'Arabella Carreras por Unidos Bariloche': coloresRN["unidos"], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                      'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"], 
                      'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P12"] = {'Gastón Vega por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"],
                   'Juan Pablo Ferrari por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                     'Arabella Carreras por Unidos Bariloche': coloresRN["unidos"], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                       'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"],
                         'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P13"] = {'Carlos Aristegui por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"], 
                  'Juan Pablo Ferrari por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                    'Arabella Carreras por Unidos Bariloche': coloresRN["unidos"], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                      'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"],
                        'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P14"] = {'Gastón Vega por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"],
                   'Marcela Gonzalez Abdala por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'], 
                   'Arabella Carreras por Unidos Bariloche': coloresRN['unidos'], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                     'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"],
                       'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P15"] = {'Carlos Aristegui por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"],
                   'Marcela Gonzalez Abdala por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                     'Arabella Carreras por Unidos Bariloche': coloresRN['unidos'], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                       'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"],
                         'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P16"] = {'Gastón Vega por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"], 
                  'Carlos Valeri  por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'],
                    'Arabella Carreras por Unidos Bariloche': coloresRN['unidos'], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                      'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"],
                        'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

paletas["P17"] = {'Carlos Aristegui por Cambia Bariloche con el apoyo de Aníbal Tortoriello': colores["cambiemos"], 
                  'Carlos Valeri por Juntos Somos Río Negro con el apoyo de Alberto Weretilneck': coloresRN['juntosSomos'], 
                  'Arabella Carreras por Unidos Bariloche': coloresRN['unidos'], 'Pablo Chamátropulos por Podemos Bariloche': colores["otros"],
                    'Costa Brutten, Vallazza o Galaverna por Vamos con Todos con el apoyo de los hermanos Soria': colores["peron1"], 
                    'Ramón Chiocconi por Nos Une Río Negro con el apoyo de La Cámpora': colores["peron2"], 'No sabe': colores["nosabe"]}

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
paletas["P31"] = list2dictPalette(['Si', 'No'], qualitative_strong, noSabe=False)