# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:10:02 2024

@author: janna
"""

# main.py
from tkinter import Tk
from game_setup import start_new_game
from ui_functions import create_label, create_restart_button, create_game_buttons
from game_logic import next_turn, check_winner, check_empty_spaces
import random
from tkinter import Label, Button, Frame




window = Tk()
window.title("Tic-Tac-Toe")
# Create the main window for the Tic-Tac-Toe game

players = ["x", "o"]
player = random.choice(players) 
# Define the players as "x" and "o", and randomly choose a starting player

label = create_label(window, player)
# Create and display the label indicating the current player's turn


btns_frame = Frame(window)
btns_frame.pack()
# Create a frame for the game buttons and pack it into the main window

game_btns = create_game_buttons(btns_frame, label, players, next_turn)
# Create and display the game buttons, linking them to the game logic functions


restart_btn = create_restart_button(window, lambda: start_new_game(players, label, game_btns, next_turn))
# Create and display the restart button, linking it to the start_new_game function


window.mainloop()