from rules import *

menu = True
while menu:
    print("New game!")
    set_board = [
        "_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"
    ]
    game_on = True
    display_board(set_board)

    while game_on:
        x_player_choice = input("It is the X player's turn. Select a space using the grid (eg. B3): ").lower()
        player_turn("X", set_board, x_player_choice)
        display_board(set_board)
        if check_for_winner(set_board, "X"):
            game_on = False
            break
        if check_full_board(set_board):
            game_on = False
            break
        o_player_choice = input("It is the O player's turn. Select a space using the grid (eg. B3): ").lower()
        player_turn("O", set_board, o_player_choice)
        display_board(set_board)
        if check_for_winner(set_board, "O"):
            game_on = False
            break
        if check_full_board(set_board):
            game_on = False
            break
