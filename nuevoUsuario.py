#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 00:49:53 2024

@author: julian
"""

import os
os.chdir('/home/julian/trabajo/opinionpublica')
from users_mgt import *

def listarUsuarios():
    lista = []
    select_st = select([User_tbl.c.username])
    
    conn = engine.connect()
    rs = conn.execute(select_st)
    
    for row in rs:
        lista.append(row[0])
    conn.close()
    return lista

def nuevoUsuario(user:str, pw:str):
    if user in listarUsuarios():
        print('el usuario ya existe')
        return
    add_user(user, pw)
    texto = 'opinionpublica.inteligenciaanalitica.com.ar\n'
    texto += f'Usuario: {user}\n'
    texto += f'Contraseña: {pw}\n'
    print(texto)
#%%
nuevoUsuario(user, pw)


