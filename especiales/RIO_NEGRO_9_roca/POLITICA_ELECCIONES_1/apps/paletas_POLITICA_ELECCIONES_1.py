from especiales.POLITICA_ELECCIONES_1.apps.cuestionario_POLITICA_ELECCIONES_1 import cuestionario
from config import colores, list2dictPalette, diverging, siNoColorDict, qualitative_strong
import seaborn as sns
# comando:


paletas = {}

paletas["P05"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
                  'Horacio Rodriguez Larreta por Juntos por el Cambio': colores["cambiemos2"],
                  'Patricia Bulrich por Juntos por el Cambio': colores["cambiemos1"],
                  'Javier Milei por La Libertad Avanza': colores["liberales"],
                  'Al candidato del Frente de Izquierda': colores["izquierda"],
                  'No sabe': colores["nosabe"]}

paletas["P09"] = list2dictPalette(['Si, habitualmente', 'Algunas veces', 'Nunca, pero esta es una excepción'], diverging, noSabe=False)

paletas["P10"] = siNoColorDict

paletas["P11"] = list2dictPalette(['La política no sirve para nada',
                                    'La política no me interesa',
                                    'La política me interesa poco',
                                    'La política me interesa',
                                    'La política es muy importante',
                                    'No sabe'], qualitative_strong, noSabe=True)

paletas["P12"] = list2dictPalette(['Siempre', 'A veces', 'Nunca', 'No sabe'], diverging, noSabe=True)

paletas["P13"] = list2dictPalette(['Los políticos son todos ladrones y corruptos', 
                                  'Los políticos sólo piensan en ellos y no en los problemas de la gente',
                                  'Algunos políticos son corruptos, ladrones y no piensan en la gente, pero otros no',
                                  'Los políticos tratan de solucionar los problemas de la gente, pero necesitan pelearse menos y que los controlen',
                                  'Los políticos representan distintos intereses y por eso deben obtener siempre el mayor apoyo posible para lograr sus objetivos',
                                  'No sabe'], qualitative_strong, noSabe=True)

paletas["P14"] = list2dictPalette(['Con fuerza, determinación y coraje para lograr sus objetivos',
                                   'Usando los mejores recursos disponibles para defender los intereses que representan',
                                   'Defendiendo los intereses que representan pero sin dejar de dialogar con los adversarios',
                                   'Buscando los acuerdos necesarios para obtener el mayor consenso posible para sus políticas',
                                   'Negociando entre las diferentes perspectivas para reducir el enfrentamiento y el conflicto social',
                                   'No sabe'], qualitative_strong, noSabe=True)

paletas["P15"] = list2dictPalette(['Con políticas de shock, mano dura y castigando a los corruptos y ladrones',
                                   'Con políticas muy estudiadas y progresivas  para que las transformaciones de fondo necesarias se puedan realizar',
                                   'Con políticas de desarrollo que permitan el crecimiento con inclusión social',
                                   'Con políticas que limiten los privilegios de los que más tienen y favorezcan a los sectores más vulnerables',
                                   'Con políticas revolucionarias que permitan la transformación igualitaria de la sociedad apoyándose en las mayorías populares',
                                   'No sabe'], qualitative_strong, noSabe=True)



derechaIzquierda = ['Muy de derecha', 'De derecha', 'De centro', 'De centro izquierda', 'Muy de izquierda']
paletaDerechaIzquierda = list2dictPalette( derechaIzquierda, "coolwarm", noSabe=False)

paletas["P16"] = paletaDerechaIzquierda

paletas["P17"] = paletaDerechaIzquierda

paletas["P18"] = paletaDerechaIzquierda

paletas["P19"] = paletaDerechaIzquierda