#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:05:23 2020

@author: rachel.dunne
"""
import random
from threading import Timer
import PySimpleGUI as sg

#### TO DO
# Add a way of telling people which character they all are and letting the spies know who the others are
# Allow to go back if input something wrong - maybe an 'are you sure?' message before properly submit.

def input_player_number():
    layout = [
        [
            sg.Text("Player number:"),
            sg.InputOptionMenu([5, 6, 7, 8, 9, 10], key="player_number"),
        ],
        [sg.Button("Submit")],
    ]
    window = sg.Window("Resistance", layout)
    event, values = window.read()
    if event == "Submit":
        player_number = int(values["player_number"])
        window.close()
    else:
        raise Exception(f"Unknown event {event}")
    return player_number


def input_players(player_number):
    # TODO REMOVE!
    return ['a', 'b', 'c', 'd', 'e']
    
    players = []
    for i in range(player_number):
        layout = [
            [sg.Text("Player name: "), sg.InputText("", key="player")],
            [sg.Button("Submit")],
        ]
        window = sg.Window("Resistance", layout)
        event, values = window.read()
        if event == "Submit":
            player = values["player"]
            players.append(player)
            window.close()
        else:
            raise Exception(f"Unknown event {event}")
            
    return players


def determine_roles_and_rounds(players):
    """ Assigns players as either resistance  or spies """
    number = len(players)
    if number == 5:
        resistance = 3
        spies = 2
        rounds = [2, 3, 2, 3, 3]
    elif number == 6:
        resistance = 4
        spies = 2
        rounds = [2, 3, 4, 3, 4]
    elif number == 7:
        resistance = 4
        spies = 3
        rounds = [2, 3, 3, 4, 4]
    elif number == 8:
        resistance = 5
        spies = 3
        rounds = [3, 4, 4, 5, 5]
    elif number == 9:
        resistance = 6
        spies = 3
        rounds = [3, 4, 4, 5, 5]
    elif number == 10:
        resistance = 6
        spies = 4
        rounds = [3, 4, 4, 5, 5]
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
    players = [
        player for players in [spy_players, resistance_players] for player in players
    ]
    setup = {
        "spies": spy_players,
        "resistance": resistance_players,
        "rounds": rounds,
        "players": players,
    }
    return setup


def reveal_characters(setup):
    players = sorted(setup["players"])
    for player in players:
        if player in setup["spies"]:
            spy = True
            role = "Spy"
        elif player in setup["resistance"]:
            spy = False
            role = "Resistance"
        layout = [
            [sg.Text("We are about to reveal some secret information")],
            [sg.Text(f"Please press show when only {player} is looking at the screen")],
            [sg.Button("Show")],
        ]
        window = sg.Window("Resistance", layout)
        event, _ = window.read()
        
        if event == "Show":
            window.close() # close previous window
            
            base_layout = [
                [sg.Text(f"{player}, your role is {role}")],
                [sg.Button("Done", bind_return_key=True)],
                [sg.Text("This message will self-destruct in 10 seconds or you can press close below")],
            ]
            
            if spy:
                other_spies = ', '.join([spy for spy in setup["spies"] if spy != player])
                layout = [[sg.Text(f"The other {'spy is' if len(other_spies) == 1 else 'spies are'}: {other_spies}")]] + base_layout
            else:
                layout = base_layout
                
            secret_window = sg.Window("Resistance", layout, return_keyboard_events=True)
            
            event, value= secret_window.read()
            if event == "Done":
                secret_window.close()
            """
            def callback():
                
                secret_window.close()
                closed = True
                
            t = Timer(5.0, callback, ())
            t.start()
            while not closed:  
                event, value = secret_window.read()
                print(event)
                if event == "Close":
                    window.close()
            """

    return None


def choose_participants(number, players):
    print("This round requires ", number, " cards")
    participants = []
    print(players)
    print(participants)
    for i in range(number):
        layout = [
            [
                sg.Text(f"Player {i+1}:"),
                sg.Listbox(
                    values=players,
                    default_values=None,
                    size=(10, 10),
                    key="participant",
                ),
            ],
            [sg.Button("Submit")],
            [sg.Button("Close")],
        ]
        window = sg.Window(title="Resistance", layout=layout).read()
        event = window[0]
        values = window[1]
        if event == "Submit":
            participants.append(values["participant"])
        if event == "Close" or event == sg.WIN_CLOSED:
            window.close()
    participants_final = [
        participant for sublist in participants for participant in sublist
    ]

    return participants_final


def get_entries(participants):
    entries = {k: None for k in participants}
    for person in participants:
        layout = [
            [
                sg.Text(f"{person}'s go:"),
                sg.Listbox(
                    values=["Good", "Bad"],
                    default_values=None,
                    size=(10, 10),
                    key="entry",
                ),
            ],
            [sg.Button("Submit")],
            [sg.Button("Close")],
        ]
        window = sg.Window(title="Resistance", layout=layout).read()
        event = window[0]
        values = window[1]
        if event == "Submit":
            entries[person] = values["entry"]
        if event == "Close" or event == sg.WIN_CLOSED:
            window.close()
    return entries


def determine_round(entries, outcomes):
    if ["Bad"] in entries.values():
        print("The spies won the round")
        outcomes.append("spies")
    else:
        print("The resistance won the round")
        outcomes.append("resistance")
    return outcomes


def play_resistance():
    """ Run the game """
    print("Welcome to resistance")
    player_number = input_player_number()
    players = input_players(player_number)
    print(players)
    setup = determine_roles_and_rounds(players)
    print(
        "This game has five rounds. A round fails if there is one bad card in the hand."
    )
    print("The number of cards in each round are: ")
    for i in range(5):
        print("Round", i + 1, "=", setup["rounds"][i], "cards")
    print("Characters will now be revealed")
    reveal_characters(setup)
    outcomes = []
    for i in range(5):
        print("Round", i + 1, ":")
        participants = choose_participants(setup["rounds"][i], setup["players"])
        entries = get_entries(participants)
        outcomes = determine_round(entries, outcomes)
    print(outcomes)
    return


if __name__ == "__main__":
    play_resistance()
