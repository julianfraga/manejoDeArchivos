from config import colores, votaria, muchoPocoColorDict, siNoColorDict,opinionColorDict


paletas = {}

# Bloque Sociodemográfico
paletas["P05"] = muchoPocoColorDict
paletas["P06"] = {'Norma Sepulveda por el MPN':colores["cristianos"], 'Walter Erdozain por el Frente Provincial ':colores["otros"], 'No sabe':colores["nosabe"]}
paletas["P06_imputadas"] = {'Norma Sepulveda por el MPN':colores["cristianos"], 'Walter Erdozain por el Frente Provincia':colores["otros"], 'No sabe':colores["nosabe"]}

# Bloque Reach candidatos a intendente
paletas["P08"] = votaria
paletas["P09"] = votaria

# Bloque Gestión e imágenes
paletas["P10"] = opinionColorDict
paletas["P11"] = opinionColorDict
paletas["P12"] = opinionColorDict
paletas["P13"] = siNoColorDict