from especiales.POSICIONAMIENTO_BA_2.apps.cuestionario_POSICIONAMIENTO_BA_2 import cuestionario
from config import colores, votaria, opinionColorDict, list2dictPalette, diverging, diverging_reverse
import seaborn as sns
# comando:


paletas = {}





paletas["P05"] = list2dictPalette(['Tengo trabajo estable',
 'Realizo changas o trabajos de vez en cuando',
 'No tengo trabajo',
 'Soy jubilado o pensionado'], diverging)

paletas["P06"] = list2dictPalette(
    [str(i) for i in range(1,10)], "coolwarm", noSabe=False
)

paletas["P07"] = list2dictPalette(
    [str(i) for i in range(1,10)], diverging_reverse, noSabe=False
)

paletas["P08"] = list2dictPalette(
     [str(i) for i in range(1,10)], reversed(sns.diverging_palette(250, 150, n=10, l=70, s=100)), noSabe=False
)


paletas["P10"] = {'Del Frente de Todos y el peronismo': colores["peronismo"], 'De Cambiemos': colores["cambiemos"], 'De los Liberales libertarios': colores["liberales"], 'De la Izquierda': colores["izquierda"], 'No sabe': colores["nosabe"]}


paletas["P11"] = {
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A algún candidato del kirchnerismo": colores['peron1'],
}


paletas["P12"] ={
    "A Alberto Fernández": colores['peron2'],
    "A Sergio Massa": colores['peron3'],
    "A algún candidato del peronismo": "#7794a3",
    "A Cristina Fernández de Kirchner": colores['peron1'],
}


paletas["P13"] = {
    "A Horacio Rodriguez Larreta": colores['cambiemos2'],
    "A Mauricio Macri": colores['cambiemos1'],
    "A Patricia Bullrich": "#edd464",
    "A Facundo Manes": colores['cambiemos_ucr'],
    "A Gerardo Morales": colores['otros'],
    "Martin Lousteau":" #e0976e"
}

paletas["P14"] = votaria


paletas["P15"] = votaria


paletas["P16"] = votaria


paletas["P17"] = votaria


paletas["P18"] = votaria


paletas["P19"] = votaria


paletas["P20"] = votaria


paletas["P21"] = votaria


paletas["P22"] = votaria


paletas["P23"] = votaria





paletas["P24"] = {'Daniel Scioli presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Wado de Pedro presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo2"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos2"],
'Horacio Rodríguez Larreta presidente - Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos1"],
'María Eugenia Vidal presidenta - Cristian Ritondo gobernador por Juntos por el Cambio': colores["cambiemos3"],
'Facundo Manes presidente - Maximiliano Abad gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
'José Luis Espert presidente y su candidato a gobernador por Juntos por el Cambio': colores["otros"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P25"] = {'Alberto Fernández presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo1"],
'Wado de Pedro presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo2"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos2"],
'Horacio Rodríguez Larreta presidente - Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos1"],
'María Eugenia Vidal presidenta - Cristian Ritondo gobernador por Juntos por el Cambio': colores["cambiemos3"],
'Facundo Manes presidente - Maximiliano Abad gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
'José Luis Espert presidente y su candidato a gobernador por Juntos por el Cambio': colores["otros"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P26"] = {'Sergio Massa presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo1"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos1"],
'Horacio Rodríguez Larreta presidente - Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos2"],
'María Eugenia Vidal presidenta - Cristian Ritondo gobernador por Juntos por el Cambio': colores["cambiemos3"],
'Facundo Manes presidente - Maximiliano Abad gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
'José Luis Espert presidente y su candidato a gobernador por Juntos por el Cambio': colores["otros"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P27"] = {'Daniel Scioli presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo1"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos2"],
'Horacio Rodríguez Larreta presidente - Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos1"],
'Facundo Manes presidente - Maximiliano Abad gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
'José Luis Espert presidente y su candidato a gobernador por Juntos por el Cambio': colores["otros"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P28"] = {'Alberto Fernández presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo1"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos2"],
'Horacio Rodríguez Larreta presidente - Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos1"],
'Facundo Manes presidente - Maximiliano Abad gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
'José Luis Espert presidente y su candidato a gobernador por Juntos por el Cambio': colores["otros"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P29"] = {'Sergio Massa presidente - Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos2"],
'Horacio Rodríguez Larreta presidente - Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos1"],
'Facundo Manes presidente - Maximiliano Abad gobernador por Juntos por el Cambio': colores["cambiemos_ucr"],
'José Luis Espert presidente y su candidato a gobernador por Juntos por el Cambio': colores["otros"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P30"] = {'Daniel Scioli presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Horacio Rodríguez Larreta presidente – Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P31"] = {'Daniel Scioli presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P32"] = {'Alberto Fernández presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Horacio Rodríguez Larreta presidente – Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P33"] = {'Alberto Fernández presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P34"] = {'Sergio Massa presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Horacio Rodríguez Larreta presidente – Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P35"] = {'Sergio Massa presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P36"] = {'Wado de Pedro presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Horacio Rodríguez Larreta presidente – Diego Santilli gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P37"] = {'Wado de Pedro presidente – Axel Kicillof gobernador por el Frente de Todos': colores["peronismo"],
'Patricia Bullrich presidenta - Joaquín De La Torre gobernador por Juntos por el Cambio': colores["cambiemos"],
'Javier Milei presidente y su candidato a gobernador por la Libertad Avanza': colores["liberales"],
'A los candidatos del Frente de Izquierda': colores["izquierda"],
'No sabe': colores["nosabe"]}


paletas["P38"] = opinionColorDict


paletas["P39"] = opinionColorDict


paletas["P40"] = opinionColorDict


paletas["P41"] = opinionColorDict


paletas["P42"] = opinionColorDict


paletas["P43"] = opinionColorDict


paletas["P44"] = opinionColorDict


paletas["P45"] = opinionColorDict


paletas["P46"] = opinionColorDict


paletas["P47"] = opinionColorDict


paletas["P48"] = opinionColorDict


paletas["P49"] = opinionColorDict


paletas["P50"] = opinionColorDict


paletas["P51"] = opinionColorDict


paletas["P52"] = opinionColorDict


paletas["P53"] = opinionColorDict


paletas["P54"] = opinionColorDict


paletas["P55"] = opinionColorDict


paletas["P56"] = opinionColorDict


paletas["P57"] = opinionColorDict


paletas["P58"] = opinionColorDict