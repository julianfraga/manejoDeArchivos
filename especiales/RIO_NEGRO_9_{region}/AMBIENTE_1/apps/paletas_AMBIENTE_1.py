from especiales.AMBIENTE_1.apps.cuestionario_AMBIENTE_1 import cuestionario
from config import (colores, votaria, opinionColorDict, list2dictPalette,
                    diverging, diverging_reverse, internas, qualitative_strong, deudasColorDict, diverging_mini,
siNoColorDict, siNoNoSabeColorDict
                    )
import seaborn as sns
# comando:


paletas = {}

paletas["P05"] = deudasColorDict

paletas["P06"] = list2dictPalette(['Mucho', 'Algo', 'Poco', 'Nada'], diverging, noSabe=False)
paletas["P07"] = list2dictPalette(['La nación', 'La provincia', 'El municipio', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P08"] = list2dictPalette(['La nación', 'La provincia', 'El municipio', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P09"] = list2dictPalette(['La nación', 'La provincia', 'El municipio', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P10"] = list2dictPalette(['La nación', 'La provincia', 'El municipio', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P11"] = list2dictPalette(['La nación', 'La provincia', 'El municipio', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P12"] = siNoColorDict
paletas["P13"] = siNoNoSabeColorDict
paletas["P14"] = list2dictPalette(['La falta de gestión de los residuos', 'La contaminación del agua', 'Los incendios descontrolados', 'El uso desmedido de fertilizantes y químicos para los cultivos', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P15"] = siNoNoSabeColorDict
paletas["P16"] = list2dictPalette(['Estaría de acuerdo con esta medida', 'No estaría de acuerdo con esta medida', 'No sabe'], diverging_mini, noSabe=True)
paletas["P17"] = siNoNoSabeColorDict
paletas["P18"] = list2dictPalette(['Estaría de acuerdo con la explotación de recursos naturales', 'No estaría de acuerdo con la explotación de recursos naturales', 'No sabe'], diverging_mini, noSabe=True)
paletas["P19"] = list2dictPalette(['Estaría de acuerdo con la explotación de recursos naturales', 'No estaría de acuerdo con la explotación de recursos naturales', 'No sabe'], diverging_mini, noSabe=True)
paletas["P20"] = list2dictPalette(['Las montañas', 'El campo', 'El agua', 'El aire', 'Los bosques', 'Los humedales', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P21"] = list2dictPalette(['El desempleo', 'La corrupción', 'La inseguridad', 'La inflación', 'El precio del dólar', 'La pobreza', 'El narcotráfico', 'Las tarifas', 'Otro', 'No sabe'], qualitative_strong, noSabe=True)
paletas["P24"] = siNoNoSabeColorDict
paletas["P25"] = list2dictPalette(['Mucho', 'Algo', 'Poco', 'Nada'], diverging, noSabe=False)