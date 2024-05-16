#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:25:34 2024

@author: julian
"""
from aux import get_series
from trackingCABA.apps.preguntasCABA import filesCABA, preguntasQueNoVanCABA, dataFolderCABA
aux.get_series(f'{self.path}/data/')
#%%
codigos_imagen = [f'P{i}' for i in range(44, 62) if i not in (57, 62, 63)] # excluyo Macri, Santoro y Santilli
