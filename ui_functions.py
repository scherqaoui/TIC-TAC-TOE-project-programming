# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:13:24 2024

@author: janna
"""
#ui_fonctions.py

from tkinter import Label, Button, Frame

def create_label(window, player):
    
    label = Label(window, text=(player + " turn"), font=('consolas', 40))
    # Create a label displaying the current player's turn with a specified font
    label.pack(side="top")
    # Pack the label to place it in the window's layout, on the top side
    return label
# this function creates and returns a label displaying the current player's turn


def create_restart_button(window, start_new_game):
    restart_btn = Button(window, text="restart", font=('consolas', 20), command=start_new_game)
    # Create a restart button with specified text, font, and command
    restart_btn.pack(side="top")
    # Pack the restart button to place it in the window's layout, on the top side
    return restart_btn
# this function create and returns a restart button with a specified command



def create_game_buttons(btns_frame, label, players, next_turn):
    game_btns = []
    #the game_btns list
    for row in range(3):
        row_buttons = []
        for col in range(3):
            button = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                            command=lambda label=label, players=players, row=row, col=col: 
                                next_turn(game_btns, label.cget("text")[0], players, label, row, col))
                # Create a button with a specific command linked to the next_turn function
                # label.cget("text")[0] donne "x" or "o"
            button.grid(row=row, column=col)
            # Place the button in the grid
            row_buttons.append(button)
            # add the button to the current row's list of buttons
        game_btns.append(row_buttons)
        # Add the row of buttons to the game_btns list
    return game_btns

# this function creates and returns a 3x3 grid of buttons for the Tic-Tac-Toe game




