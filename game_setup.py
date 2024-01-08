# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:12:37 2024

@author: janna
"""




import random

 
def start_new_game(players, label, game_btns, next_turn):
    
    player = random.choice(players)
      # Randomly choose a player to start the new game
    label.config(text=(player + "turn"))
      # Update the label to indicate the current player's turn
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="grey")
            # Set the text on the button to an empty string and changes the background color to grey.         
    return player # Return the player who will start the new game












