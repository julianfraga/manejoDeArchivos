#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:30:24 2023

@author: julian
"""

def infer_paleta(path, cuestionario, default_paleta="qualitative_strong"):

    import pandas as pd

    path = path[:-1] if path.endswith('/') else path

    df_preguntas = cuestionario


    paleta = {}

    for i, row in df_preguntas.fillna("").iterrows():
        pregunta = row.codigo
        paleta = row.paleta

        if row.paleta == "imagen":
            print(f'paletas["{pregunta}"] = opinionColorDict')


        else:

            df = pd.read_csv(path + "/data/pregunta_" + pregunta + ".csv")
            opciones = df.clase.tolist()

            if "Buena" in opciones:
                # if row.paleta == "imagen":
                print(f'paletas["{pregunta}"] = opinionColorDict')

            if paleta in ["votaria", 'reach']:
                print(f'paletas["{pregunta}"] = votaria')

            elif paleta == "internas":
                print(f'paletas["{pregunta}"] = interna')
            # paleta in ["interna"]:
            #    print(f'paletas["{pregunta}"] = interna')

            elif paleta == "politica":
                p = {opcion:f'colores["{infer_politica(opcion)}"]' for opcion in opciones}
               
                # fix comillas molestas 
                value = repr(p).replace("'colores","colores").replace("]'", "]")
                print(f'paletas["{pregunta}"] = ' + value + '\n' )

                # print(f'paletas["{pregunta}"] = ' + repr(p).replace("'colores[]'","colores[]") + '\n' )


            else:
                opciones = df.clase.astype(str).tolist()
                opciones_lower = df.clase.astype(str).str.lower().tolist()
                nosabe =  ("no sabe" in opciones_lower )  or ( "no se" in opciones_lower)

                print(f'paletas["{pregunta}"] = list2dictPalette({repr(opciones)}, {default_paleta}, noSabe={nosabe})')
