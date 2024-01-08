# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:11:10 2024

@author: janna
"""

def check_winner(game_btns):
    
    
     # check all 3 horizontal conditions  
    for row in range(3):
        if (game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text']) and game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg="yellow")
            game_btns[row][1].config(bg="yellow")
            game_btns[row][2].config(bg="yellow")
            # Mark the winning buttons with a yellow background

            
            return True  # Return True if a horizontal win is found
        
     # check all 3 vertical conditions 
    for col in range(3):
        if (game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text']) and game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg="yellow")
            game_btns[1][col].config(bg="yellow")
            game_btns[2][col].config(bg="yellow")
             # Mark the winning buttons with a yellow background
            
            return True # Return True if a vertical win is found
        
        
     # check on both diagonals condition
     
     # Main diagonal (top-left to bottom-right)
    if (game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text']) and game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="yellow")
        game_btns[1][1].config(bg="yellow")
        game_btns[2][2].config(bg="yellow")
        
        return True
    # Other diagonal (top-right to bottom-left)
    elif (game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text']) and game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="yellow")
        game_btns[1][1].config(bg="yellow")
        game_btns[2][0].config(bg="yellow")
        return True
     
     # If there is no empty spaces
    if check_empty_spaces(game_btns) == False:
        for row in range (3):
            for col in range(3):
                game_btns[row][col].config(bg = 'red')
                # Mark all buttons with a red background to indicate a tie
                return 'tie'
            # Return 'tie' to indicate a tie
    else:
        return False
          # Return False if there is neither a winner nor a tie          
    
    
    
    

    
    
def check_empty_spaces(game_btns):
    spaces= 9
    # Total number of spaces on the Tic-Tac-Toe board (3x3 grid)
    for row in range(3): 
        for col in range(3): 
            # nested loops iterate over all the rows and columns
            if game_btns[row][col]['text'] != "":
                # Check if the text of the current button is not an empty string
                spaces -= 1
                 # If the button is not empty, decrement the total spaces count
    if spaces == 0:
    # Check if there are no empty spaces left on the board
        return False
    
    else:
        return True
    
    
def next_turn(game_btns, player, players, label, row, col):
    
    if game_btns[row][col]['text'] == "" and check_winner(game_btns) == False:
    # Check if the selected button is empty and there is no winner yet
        
        
        
        if player == players[0]:
         # If it's player 1's turn
            
            game_btns[row][col]['text'] = player
        # Set the text of the clicked button to player 1's symbol ('X' or 'O')
            if check_winner(game_btns) == False:
                # Check if there is still no winner after player 1's move
                player = players[1]
                # Switch to player 2's turn  
                label.config(text=(players[1] + " turn"))
                #update the label
            elif check_winner(game_btns) == True:
                # If there is a winner after player 1's move
                label.config(text=(players[0] + " wins"))
              # Update the label to announce player 1 as the winner
            elif check_winner(game_btns) == 'tie':
                # If the game ends in a tie after player 1's move
                label.config(text=("Tie, no winner"))
                # Update the label to indicate a tie with no winner
                
                
        
        elif player == players[1]:
        # If it's player 2's turn
            game_btns[row][col]['text'] = player
             # Set the text of the clicked button to player 2's symbol ('X' or 'O')

            if check_winner(game_btns) == False:
            # Check if there is still no winner after player 2's move
                player = players[0]
                # Switch to player 1's turn  
                label.config(text=(players[0] + " turn"))
                 #update the label
            elif check_winner(game_btns) == True:
                # If there is a winner after player 2's move
                label.config(text=(players[1] + " wins"))
              # Update the label to announce player 2 as the winner
            elif check_winner(game_btns) == 'tie':
                # If the game ends in a tie after player 2's move
                label.config(text=("Tie, no winner"))
                 # Update the label to indicate a tie with no winner
    
    
    
    
    
    
