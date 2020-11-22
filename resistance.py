#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:05:23 2020

@author: rachel.dunne
"""
import random
import os

    
def input_players():
    number = int(input("How many players are there? "))
    if type(number) is not int:
        print("Invalid entry")
        number = int(input("How many players are there? "))
    players = []
    for i in range(number):
        players.append(input("Player" + str(i+1) +": "))
    return(players)
    

def determine_roles_and_rounds(players):
    """ Assigns players as either resistance  or spies """
    number = len(players)
    if number == 5:
        resistance = 3
        spies = 2
        rounds = [2,3,2,3,3]
    elif number == 6:
        resistance = 4
        spies = 2
        rounds = [2,3,4,3,4]
    elif number == 7:
        resistance = 4
        spies = 3
        rounds = [2,3,3,4,4]
    elif number == 8:
        resistance = 5
        spies = 3
        rounds = [3,4,4,5,5]
    elif number == 9:
        resistance = 6
        spies = 3
        rounds = [3,4,4,5,5]
    elif number == 10:
        resistance = 6
        spies = 4
        rounds = [3,4,4,5,5]
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
    setup = {"spies" : spy_players, "resistance" : resistance_players,
             "rounds": rounds}
    return(setup)
    

def choose_participants(number, players):
    print("This round requires ", number, " cards")
    participants = []
    for i in range(number):
        participants.append(input(f"Who will play this round? (Player {i+1}): "))
    return participants
    

def get_entries(participants):
    entries = {k:None for k in participants}
    for person in participants:
        while entries[person] not in ["bad", "good"]:
            entries[person] = input(f"{person}, what is your choice? (bad/good) ")
            os.system("clear")
    return entries

def determine_round(entries, outcomes):
    if "bad" in entries.values():
        print("The spies won the round")
        outcomes.append("spies")
    else:
        print("The resistance won the round")
        outcomes.append("resistance")
    return outcomes


def play_resistance():
    """ Run the game """
    print("Welcome to resistance")
    players = input_players()
    print(players)
    setup = determine_roles_and_rounds(players)
    print("This game has five rounds. A round fails if there is one bad card in the hand.")
    print("The number of cards in each round are: ")
    for i in range(5):
        print("Round", i+1, "=", setup["rounds"][i], "cards")
    outcomes = []
    for i in range(5):
        print("Round", i+1, ":")
        participants = choose_participants(setup["rounds"][i], players)
        entries = get_entries(participants)
        outcomes = determine_round(entries, outcomes)
    print(outcomes)
    return(participants)
    