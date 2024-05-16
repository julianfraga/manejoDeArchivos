from especiales.POSICIONAMIENTO_NACIONAL_9.apps.cuestionario_POSICIONAMIENTO_NACIONAL_9 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, diverging, diverging_reverse
import seaborn as sns
# comando:


paletas = {}





paletas["P04"] = list2dictPalette(['Tengo trabajo estable',
 'Realizo changas o trabajos de vez en cuando',
 'No tengo trabajo',
 'Soy jubilado o pensionado'], diverging)

paletas["P05"] = list2dictPalette(
    [str(i) for i in range(1,10)], "coolwarm", noSabe=False
)

paletas["P06"] = list2dictPalette(
    [str(i) for i in range(1,10)], diverging_reverse, noSabe=False
)

paletas["P07"] = list2dictPalette(
     [str(i) for i in range(1,10)], reversed(sns.diverging_palette(250, 150, n=10, l=70, s=100)), noSabe=False
)






paletas["P09"] = {'Del Frente de Todos y el peronismo': colores["peronismo"],
 'De Juntos por el cambio': colores["cambiemos"],
 'De los Liberales libertarios': colores["liberales"],
 'De la Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P10"] =  {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}


paletas["P11"] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
    }

paletas["P12"] ={
    "A Horacio Rodriguez Larreta": colores['cambiemos'],
    "A Patricia Bullrich":colores['cambiemos2'],
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros']
}
paletas["P13"] = votaria


paletas["P14"] = votaria


paletas["P15"] = votaria


paletas["P16"] = votaria


paletas["P17"] = votaria


paletas["P18"] = votaria


paletas["P19"] = votaria


paletas["P20"] = votaria


paletas["P21"] = votaria


paletas["P22"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Alberto Fernández por el Frente de Todos': colores["peronismo1"],
 'Sergio Massa por el Frente de Todos': colores["peronismo2"],
 'Wado de Pedro por el Frente de Todos': colores["peronismo3"],
 'Daniel Scioli por el Frente de Todos': colores["peronismo4"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P23"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos2"],
 'María Eugenia Vidal por Juntos por el Cambio': colores["cambiemos3"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Sergio Massa por el Frente de Todos': colores["peronismo2"],
 'Wado de Pedro por el Frente de Todos': colores["peronismo1"],
 'Daniel Scioli por el Frente de Todos': colores["peronismo3"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P24"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos2"],
 'María Eugenia Vidal por Juntos por el Cambio': colores["cambiemos3"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Sergio Massa por el Frente de Todos': colores["peronismo2"],
 'Wado de Pedro por el Frente de Todos': colores["peronismo3"],
 'Alberto Fernández por el Frente de Todos': colores["peronismo1"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P25"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos2"],
 'Facundo Manes por Juntos por el Cambio': colores["cambiemos_ucr"],
 'Sergio Massa por el Frente de Todos': colores["peronismo2"],
 'Wado de Pedro por el Frente de Todos': colores["peronismo1"],
 'Daniel Scioli por el Frente de Todos': colores["peronismo3"],
 'Javier Milei por los liberales libertario': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P26"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bulrich por Juntos por el Cambio': colores["cambiemos2"],
 'Alberto Fernández por el Frente de Todos': colores["peronismo1"],
 'Sergio Massa por el Frente de Todos': colores["peronismo2"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P27"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos2"],
 'Wado de Pedro por el Frente de Todos': colores["peronismo1"],
 'Sergio Massa por el Frente de Todos': colores["peronismo2"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P28"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos2"],
 'Wado de Pedro por el Frente de Todos': colores["peronismo1"],
 'Daniel Scioli por el Frente de Todos': colores["peronismo2"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P29"] = {'Horacio Rodríguez Larreta presidente – Gerardo Morales vice por Juntos por el Cambio': colores["cambiemos1"],
 'Patricia Bullrich presidenta – Gustavo Valdes vice por Juntos por el Cambio': colores["cambiemos2"],
 'Sergio Massa presidente – Ricardo Alfonsín vice por el Frente de Todos': colores["peronismo1"],
 'Wado de Pedro presidente – Jorge Capitanich vice por el Frente de Todos': colores["peronismo2"],
 'Javier Milei presidente y su candidato a vice': colores["liberales"],
 'A los candidatos de la izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P30"] = {'Alberto Fernández por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P31"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P32"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P33"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P34"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P35"] = {'Alberto Fernández por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P36"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P37"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'Al candidato del Frente de Izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P38"] = {'Horacio Rodríguez Larreta presidente – Gerardo Morales vice por Juntos por el Cambio': colores["cambiemos"],
 'Sergio Massa presidente – Ricardo Alfonsín vice por el Frente de Todos': colores["peronismo"],
 'Javier Milei presidente y su candidato a vice': colores["liberales"],
 'A los candidatos de la izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P39"] = {'Patricia Bullrich presidenta – Gustavo Valdés vice por Juntos por el Cambio': colores["cambiemos"],
 'Sergio Massa presidente – Ricardo Alfonsín vice por el Frente de Todos': colores["peronismo"],
 'Javier Milei presidente y su candidato a vice': colores["liberales"],
 'A los candidatos de la izquierda': colores["izquierda"],
 'No sabe': colores["nosabe"]}


paletas["P40"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P41"] = {'Alberto Fernández por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P42"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P43"] = {'Alberto Fernández por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P44"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P45"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo"],
 'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P46"] = {'Wado de Pedro por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P47"] = {'Daniel Scioli por el Frente de Todos': colores["peronismo"],
 'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'No sabe': colores["nosabe"]}


paletas["P48"] = {'Horacio Rodríguez Larreta por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'No sabe': colores["nosabe"]}


paletas["P49"] = {'Patricia Bullrich por Juntos por el Cambio': colores["cambiemos"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'No sabe': colores["nosabe"]}


paletas["P50"] = {'Alberto Fernández por el Frente de Todos': colores["peronismo"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'No sabe': colores["nosabe"]}


paletas["P51"] = {'Sergio Massa por el Frente de Todos': colores["peronismo"],
 'Javier Milei por los liberales libertarios': colores["liberales"],
 'No sabe': colores["nosabe"]}

paletas["P52"] = opinionColorDict
paletas["P53"] = opinionColorDict
paletas["P54"] = opinionColorDict
paletas["P55"] = opinionColorDict
paletas["P56"] = opinionColorDict
paletas["P57"] = opinionColorDict
paletas["P58"] = opinionColorDict
paletas["P59"] = opinionColorDict
paletas["P60"] = opinionColorDict
paletas["P61"] = opinionColorDict
paletas["P62"] = opinionColorDict