#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:15:00 2024

@author: julian
"""

import dash
from dash.testing.application_runners import import_app
from dash.testing.browser import Browser

def test_dropdowns(app_path, section_path):
    # Importa la aplicación Dash
    app = import_app(app_path)

    # Crea una instancia del navegador
    browser = Browser(app)

    # Navega a la sección especificada
    browser.visit(section_path)

    # Encuentra todos los dropdowns en la página
    dropdowns = browser.find_all("select")

    # Prueba cada dropdown
    for dropdown in dropdowns:
        # Selecciona la primera opción del dropdown
        dropdown.select_by_index(0)

        # Verifica si se muestra algún error en el navegador
        if browser.is_element_present(".dash-error"):
            print("Se encontró un error en el dropdown:", dropdown.get_attribute("name"))

    # Cierra el navegador
    browser.quit()

# Ruta de la aplicación Dash
app_path = "/ruta/de/tu/aplicacion.py"

# Ruta de la sección que deseas probar
section_path = "/ruta/de/la/seccion"

# Ejecuta la función de prueba
test_dropdowns(app_path, section_path)