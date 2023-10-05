#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:25:39 2023

@author: julian
"""

import configparser
import os
import pandas as pd
rutaUsers = '/home/julian/trabajo/redes/redes/users'
usuario = 'MarceloE'
config = configparser.ConfigParser()
config.read(os.path.join(rutaUsers, usuario))
secciones = config.sections()

permisosRedes = pd.DataFrame(columns = secciones)
listaValores = []
for usuario in os.listdir(rutaUsers):
    if usuario == 'permisos.csv':
        continue
    config.read(os.path.join(rutaUsers, usuario))
    secciones = config.sections()
    valores = {'usuario':usuario}
    for seccion in secciones:
        habilitado = config[seccion]['habilitado']
        valores[seccion] = habilitado
        if seccion not in permisosRedes.columns:
            permisosRedes[seccion] = None
            secciones.append(seccion)
    listaValores.append(valores)

for valores in listaValores:
    nuevaFila = pd.DataFrame.from_dict(valores, orient = 'index').T
    permisosRedes = permisosRedes.append(nuevaFila, ignore_index= True)

columnas = [seccion.lstrip('red') for seccion in secciones]
renombres = dict(zip(secciones, columnas))

permisosRedes.rename(columns = renombres, inplace=True)
permisosRedes = permisosRedes[['usuario']].join(permisosRedes[columnas]) #quiero el usuario primero
permisosRedes.sort_values(by = columnas, ascending = [*[False]*len(columnas)], inplace = True)

mapper = {'T': 1,'F':0}
for columna in columnas:
    permisosRedes[columna] = permisosRedes[columna].replace(mapper)
permisosRedes.to_csv('/home/julian/trabajo/usuarios_redes.csv', index = False)
