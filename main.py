from helpers import draw_board, check_turn
import os

spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

playing = True
turn = 0

while playing:
    os.system('cls' if os.name == "nt" else "clear")
    draw_board(spots)
    print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your corresponding number for your choice or press q to quit ")
    
    choice = input()
    if choice =="q":
        playing = False 
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = check_turn(turn)