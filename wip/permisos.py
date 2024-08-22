import os
os.chdir('/home/julian/trabajo/opinionpublica')
from flask_login import current_user
from txt import *
import configparser
import pandas as pd
#%%
config = configparser.ConfigParser()

def getUser():
    if current_user.is_authenticated:
        return(current_user.username)
    else:
        return(False)

def trackingNacionalHabilitado():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        tracking = config['trackingNacional']
        if tracking['habilitado'] == 'T':
            return(True)
        else:
            return(False)
    else:
        return(False)


def trackingPBAHabilitado():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        tracking = config['trackingPBA']
        if tracking['habilitado'] == 'T':
            return(True)
        else:
            return(False)
    else:
        return(False)

def trackingCABAHabilitado():
    usuario = getUser()
    # if usuario and usuario in ['MarceloE','IvanK', 'fertest', 'JMValdez']:
    #     return(True)
    # else:
    #     return (False)
    if usuario:
        config.read('users/' + usuario)
        pba = config['trackingPBA']['habilitado']
        caba = True
        if 'trackingCABA' in config:
            caba = config['trackingCABA']['habilitado'] == 'T'

        if pba and caba:

            return True
        else:
            return(False)
    else:
        return(False)


def trackingCOVIDHabilitado():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        tracking = config['trackingCOVID']
        if tracking['habilitado'] == 'T':
            return(True)
        else:
            return(False)
    else:
        return(False)

def trackingAYSAHabilitado():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        tracking = config['trackingAYSA']
        if tracking['habilitado'] == 'T':
            return(True)
        else:
            return(False)
    else:
        return(False)
    
def controlHabilitado():
    usuario = getUser()
    if usuario and usuario in ['MarceloE', 'Sebas', 'JulianF']:
        return(True)
    else:
        return (False)


def trackingTABACOHabilitado():
    usuario = getUser()
    if usuario and usuario in ['MarceloE','IvanK', 'JorgeBAT', 'FelixBAT']:
        return(True)
    else:
        return (False)


def informesAnterioresHabilitado():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        if 'informesAnteriores' in config:
            informes = config['informesAnteriores']
            if informes['habilitado'] == 'T':
                return(True)
            else:
                return(False)
        else:
            return(False)
    else:
        return(False)

def trackingControlHabilitado():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        if 'trackingControl' in config:
            informes = config['trackingControl']
            if informes['habilitado'] == 'T':
                return(True)
            else:
                return(False)
        else:
            return(False)
    else:
        return(False)

def trackingNacionalPreguntasDeshabilitadas():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        preguntasDeshabilitadas = config['trackingNacional']['preguntasDeshabilitadas']
        if len(preguntasDeshabilitadas) > 0:
            return(preguntasDeshabilitadas.split(","))
        else:
            return([])
    else:
        return([])
    
def trackingNacionalBloquesDeshabilitados():
    usuario = getUser()
    deshabilitados = []
    if usuario:
        config.read('users/' + usuario)
        if 'bloquesDeshabilitados' in config['trackingNacional']:
            bloquesDeshabilitados = config['trackingNacional']['bloquesDeshabilitados']
            if len(bloquesDeshabilitados) > 0:
                deshabilitados = bloquesDeshabilitados.split(",")
    
    return(deshabilitados)    

def trackingPBAPreguntasDeshabilitadas():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        preguntasDeshabilitadas = config['trackingPBA']['preguntasDeshabilitadas']
        if len(preguntasDeshabilitadas) > 0:
            return(preguntasDeshabilitadas.split(","))
        else:
            return([])
    else:
        return([])

def trackingPBABloquesDeshabilitados():
    usuario = getUser()
    deshabilitados = []
    if usuario:
        config.read('users/' + usuario)
        if 'bloquesDeshabilitados' in config['trackingPBA']:
            bloquesDeshabilitados = config['trackingPBA']['bloquesDeshabilitados']
            if len(bloquesDeshabilitados) > 0:
                deshabilitados = bloquesDeshabilitados.split(",")
    
    return(deshabilitados)    

def trackingCOVIDPreguntasDeshabilitadas():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        preguntasDeshabilitadas = config['trackingCOVID']['preguntasDeshabilitadas']
        if len(preguntasDeshabilitadas) > 0:
            return(preguntasDeshabilitadas.split(","))
        else:
            return([])
    else:
        return([])

def trackingAYSAPreguntasDeshabilitadas():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        preguntasDeshabilitadas = config['trackingAYSA']['preguntasDeshabilitadas']
        if len(preguntasDeshabilitadas) > 0:
            return(preguntasDeshabilitadas.split(","))
        else:
            return([])
    else:
        return([])



def trackingCOVIDBloquesDeshabilitados():
    usuario = getUser()
    deshabilitados = []
    if usuario:
        config.read('users/' + usuario)
        if 'bloquesDeshabilitados' in config['trackingCOVID']:
            bloquesDeshabilitados = config['trackingCOVID']['bloquesDeshabilitados']
            if len(bloquesDeshabilitados) > 0:
                deshabilitados = bloquesDeshabilitados.split(",")
    
    return(deshabilitados)

def trackingAYSABloquesDeshabilitados():
    usuario = getUser()
    deshabilitados = []
    if usuario:
        config.read('users/' + usuario)
        if 'bloquesDeshabilitados' in config['trackingAYSA']:
            bloquesDeshabilitados = config['trackingAYSA']['bloquesDeshabilitados']
            if len(bloquesDeshabilitados) > 0:
                deshabilitados = bloquesDeshabilitados.split(",")
    
    return(deshabilitados)    


def informesAnterioresInformesDeshabilitados():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        informesDeshabilitados = config['informesAnteriores']['informesDeshabilitados']
        if len(informesDeshabilitados) > 0:
            return(informesDeshabilitados.split(","))
        else:
            return([])
    else:
        return([])


def trackingSANTIAGOHabilitado():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        tracking = config['trackingSANTIAGO']
        if tracking['habilitado'] == 'T':
            return (True)
        else:
            return (False)
    else:
        return (False)


def trackingSANTIAGOBloquesDeshabilitados():
    usuario = getUser()
    deshabilitados = []
    if usuario:
        config.read('users/' + usuario)
        if 'bloquesDeshabilitados' in config['trackingSANTIAGO']:
            bloquesDeshabilitados = config['trackingSANTIAGO']['bloquesDeshabilitados']
            if len(bloquesDeshabilitados) > 0:
                deshabilitados = bloquesDeshabilitados.split(",")

    return (deshabilitados)


def trackingSANTIAGOPreguntasDeshabilitadas():
    usuario = getUser()
    if usuario:
        config.read('users/' + usuario)
        preguntasDeshabilitadas = config['trackingSANTIAGO']['preguntasDeshabilitadas']
        if len(preguntasDeshabilitadas) > 0:
            return (preguntasDeshabilitadas.split(","))
        else:
            return ([])
    else:
        return ([])


def trackingLEGISLATIVASHabilitado():
    usuario = getUser()

    if usuario:
        permisos = pd.read_csv('./trackingLEGISLATIVAS/apps/permisos.csv', index_col='user').fillna(0).applymap(
            bool).to_dict(orient='index')
        


        if current_user.username in permisos.keys():


            permisos = permisos.get(current_user.username)
            if sum(permisos.values()):
                return (True)
        else:
            return (False)
    else:
        return (False)


def trackingPROVINCIASHabilitado():
    usuario = getUser()

    if usuario:
        permisos = pd.read_csv('./trackingPROVINCIAS/apps/permisos.csv', index_col='user').fillna(0).applymap(
            bool).to_dict(orient='index')

        if current_user.username in permisos.keys():

            permisos = permisos.get(current_user.username)
            if sum(permisos.values()):
                return (True)
        else:
            return (False)
    else:
        return (False)

def trackingPASO_BAHabilitado(encuesta="PASO_BA"):
    usuario = getUser()

    if usuario:
        permisos = pd.read_csv('./tracking' + encuesta + '/apps/permisos.csv', index_col='user').fillna(0).applymap(
            bool).to_dict(orient='index')

        if current_user.username in permisos.keys():

            permisos = permisos.get(current_user.username)
            if sum(permisos.values()):
                return (True)
        else:
            return (False)
    else:
        return (False)





def especiales_check(encuesta):
    usuario = getUser()

    especiales_permisos = (pd.read_csv('./especiales/permisos_especiales.csv', index_col='user')
                           .T
                           .fillna(0)
                           .astype(bool)
                           .to_dict('index')
                           )

    if usuario in especiales_permisos.keys():
        return especiales_permisos[usuario].get(encuesta, False)
    else:
        return False







