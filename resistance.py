#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:05:23 2020

@author: rachel.dunne
"""
import random

players = ["ash", "alex", "maan", "rachel", "christian"]  
    
def input_players():
    number = int(input("How many players are there? "))
    if type(number) is not int:
        print("Invalid entry")
        number = int(input("How many players are there? "))
    players = []
    for i in range(number):
        players.append(input("Player" + str(i) +": "))
    return(players)
    

def assign_players(players):
    """ Assigns players as either resistance  or spies """
    number = len(players)
    if number == 5:
        resistance = 3
        spies = 2
    elif number == 6:
        resistance = 4
        spies = 2
    elif number == 7:
        resistance = 4
        spies = 3
    elif number == 8:
        resistance = 5
        spies = 3
    elif number == 9:
        resistance = 6
        spies = 3
    elif number == 10:
        resistance = 6
        spies = 4
    else:
        print("Invalid player number")
    spy_players = []
    resistance_players = []
    for i in range(spies):
        spy = random.choice(players)
        spy_players.append(spy)
        players.remove(spy)
    for i in range(resistance):
        resistance_person = random.choice(players)
        resistance_players.append(resistance_person)
        players.remove(resistance_person)
    assignment = {"spies" : spy_players, "resistance" : resistance_players}
    return(assignment)
    


def play_resistance(players):
    """ Run the game """
    print("Welcome to resistance")
    players = input_players()
    assignment = assign_players(players)
    return(assignment)
    
    
    
    
    
    