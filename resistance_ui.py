#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:06:09 2020

@author: rachel.dunne
"""

import PySimpleGUI as sg

layout = [[sg.Text("Welcome to Resistance")], [sg.Text("Player 1: "), sg.InputText("")]]

# Create the window
window = sg.Window("Demo", layout).read()

