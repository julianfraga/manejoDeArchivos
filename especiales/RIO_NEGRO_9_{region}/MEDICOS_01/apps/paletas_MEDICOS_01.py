from config import list2dictPalette, siNoColorDict, siNoNoSabeColorDict, diverging,qualitative_strong, diverging_reverse,diverging_mini

# comando:


paletas = {}

# Bloque General
paletas["P04"] = list2dictPalette(['Gran excedente habitual', 'Gran excedente excepcional', 'Pequeño excedente habitual', 'Pequeño excedente excepcional', 'Alcanza gastos familia', 'No alcanza gastos familia', 'Solo NBFamiliares', 'No alcanza NBFamiliares', 'No sabe'], diverging, noSabe=True)
paletas["P06"] = list2dictPalette(['Menos de 5 años ', 'Entre 6 y 10 años', 'Entre 11 y 20 años', 'Mas de 20 años'], diverging_reverse, noSabe=False)
paletas["P07"] = list2dictPalette(['Medico clínico', 'Pediatra', 'Cardiólogo', 'Neumólogos', 'Otra especialidad'], qualitative_strong, noSabe=False)
paletas["P08"] = list2dictPalette(['En una institución pública', 'En una institución privada', 'Ambas', 'Solo consultorio', 'Institución publica o privada y consultorio'], qualitative_strong, noSabe=False)
paletas["P09"] = siNoColorDict
paletas["P10"] = list2dictPalette(['1 dosis', '2 dosis.', '3 dosis o más'], diverging_reverse, noSabe=False)
paletas["P11"] = siNoColorDict
paletas["P12"] = list2dictPalette(['Para protegerse de la enfermedad', 'Porque soy personal de riesgo', 'Porque colegas se vacunaron', 'Me lo recomendó la institución donde trabajo', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P13"] = siNoColorDict
paletas["P14"] = siNoColorDict
paletas["P15"] = list2dictPalette(['Si, a todos sus pacientes', 'Depende el caso del paciente', 'No la recomiendo'], diverging, noSabe=False)
paletas["P16"] = list2dictPalette(['Dos dosis', 'Tres dosis', 'Cuatros o mas dosis'], diverging_reverse, noSabe=False)
paletas["P17"] = list2dictPalette(['Porque ya no hay casos de COVID', 'Porque ha disminuido de forma significativa el contagio', 'Por los efectos secundarios', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P18"] = siNoNoSabeColorDict
paletas["P19"] = siNoNoSabeColorDict
paletas["P20"] = siNoNoSabeColorDict
paletas["P21"] = siNoNoSabeColorDict
paletas["P22"] = list2dictPalette(['Sinopharm', 'Sputnik', 'Aztra-Zeneca', 'Moderna', 'Pfizer', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P23"] = list2dictPalette(['Si', 'No', 'A veces'], diverging_mini, noSabe=True)
paletas["P24"] = siNoNoSabeColorDict
paletas["P25"] = siNoNoSabeColorDict
paletas["P26"] = siNoNoSabeColorDict
paletas["P27"] = siNoNoSabeColorDict
paletas["P28"] = siNoNoSabeColorDict
paletas["P29"] = siNoNoSabeColorDict
paletas["P30"] = list2dictPalette(['No tengo información suficiente', 'No tengo tiempo en la consulta', 'No es un tema importante en la consulta médica', 'El COVID no es una enfermedad prevalente o importante actualmente en Argentina', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P31"] = list2dictPalette(['Nunca', 'Pocas veces', 'Muchas veces', 'Siempre', 'No sabe'], diverging_reverse, noSabe=True)
paletas["P32"] = list2dictPalette(['adultos mayores sanos', 'Adultos jóvenes sanos', 'Madres de niños pequeños', 'No sabe'], qualitative_strong, noSabe=True)