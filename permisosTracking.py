#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:29:44 2023

@author: julian
"""
import configparser
import os
import pandas as pd
rutaUsers = '/home/julian/trabajo/opinionpublica/users'
columnas = ['usuario', 'nacional', 'caba', 'pba']
permisosTracking = pd.DataFrame(columns = columnas)
for usuario in os.listdir(rutaUsers):
    config = configparser.ConfigParser()
    userCfg = config.read(os.path.join(rutaUsers, usuario))
    nacionalHabilitado = config['trackingNacional']['habilitado']
    pbaHabilitado = config['trackingPBA']['habilitado']
    cabaHabilitado = config['trackingCABA']['habilitado']
    permisosTracking = permisosTracking.append(pd.Series([usuario, nacionalHabilitado, cabaHabilitado, pbaHabilitado], index = columnas),
                                               ignore_index=True)
permisosTracking.sort_values(by = ['nacional', 'caba', 'pba', 'usuario'], ascending = [False, False, False, True], inplace = True)


print('    Usuario    nacional       caba        pba')
print('-----------  ---------- ---------- ----------')
for _, row in permisosTracking.iterrows():
    usuario , nacional, caba, pba = row
    print(f'{usuario:>11s} {nacional:>10s} {caba:>10s} {pba:>10s}')

