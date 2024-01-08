# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:12:37 2024

@author: janna
"""




import random

def start_new_game(players, label, game_btns, next_turn):
    
    player = random.choice(players)

    label.config(text=(player + "turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="grey")
                     
    return player












