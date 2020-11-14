#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:05:23 2020

@author: rachel.dunne
"""

def assign_players(number, players):
    """ Assigns players as either resistance  or spies """
    if players == 5:
        resistance = 3
        spies = 2
    elif players == 6:
        resistance = 4
        spies = 2
    elif players == 7:
        resistance = 4
        spies = 3
    elif players == 8:
        resistance = 5
        spies = 3
    elif players == 9:
        resistance = 6
        spies = 3
    elif players == 10:
        resistance = 6
        spies = 4
    else:
        print("Invalid player number")
    
    
    