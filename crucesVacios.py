#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:18:01 2024

@author: julian
"""

import os
import pandas as pd
import csv
path = '/home/julian/trabajo/updates/corte 241/Rio negro/web/viedma'
os.chdir(path)

path_individuales = path+'/individuales/'
# os.mkdir(path_individuales+'datafalsa')
preguntas = [archivo for archivo in os.listdir(path_individuales)  if 'pregunta' in archivo]
for pregunta in preguntas:
    df = pd.read_csv(path_individuales+pregunta)
    df_cruce_vacio = pd.DataFrame(columns = ["var", *list(df.columns)])
    df_cruce_vacio.to_csv(path+'/cruces/cruce_'+pregunta, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
