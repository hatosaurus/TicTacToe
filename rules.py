def display_board(board):
    print("    1    2    3")
    print(f"A {board[0:3]}")
    print(f"B {board[3:6]}")
    print(f"C {board[6:9]}")


def player_turn(player, board, chosen_space):
    player_choosing = True
    while player_choosing:
        if chosen_space == "a1" and board[0] == "_":
            board[0] = player
            player_choosing = False
        elif chosen_space == "a2" and board[1] == "_":
            board[1] = player
            player_choosing = False
        elif chosen_space == "a3" and board[2] == "_":
            board[2] = player
            player_choosing = False
        elif chosen_space == "b1" and board[3] == "_":
            board[3] = player
            player_choosing = False
        elif chosen_space == "b2" and board[4] == "_":
            board[4] = player
            player_choosing = False
        elif chosen_space == "b3" and board[5] == "_":
            board[5] = player
            player_choosing = False
        elif chosen_space == "c1" and board[6] == "_":
            board[6] = player
            player_choosing = False
        elif chosen_space == "c2" and board[7] == "_":
            board[7] = player
            player_choosing = False
        elif chosen_space == "c3" and board[8] == "_":
            board[8] = player
            player_choosing = False
        else:
            print("No space!")
            chosen_space = input("Choose a new space: ")


def check_full_board(board):
    if "_" not in board:
        print("Cat's game! Meow!")
        return True
    else:
        return False


def check_for_winner(board, player):
    if board[0] == board[1] == board[2] == player:
        print(f"{player} is the winner with a horizontal line!")
        return True
    elif board[3] == board[4] == board[5] == player:
        print(f"{player} is the winner with a horizontal line!")
        return True
    elif board[6] == board[7] == board[8] == player:
        print(f"{player} is the winner with a horizontal line!")
        return True
    elif board[0] == board[3] == board[6] == player:
        print(f"{player} is the winner with a vertical line!")
        return True
    elif board[1] == board[4] == board[7] == player:
        print(f"{player} is the winner with a vertical line!")
        return True
    elif board[2] == board[5] == board[8] == player:
        print(f"{player} is the winner with a vertical line!")
        return True
    elif board[0] == board[4] == board[8] == player:
        print(f"{player} is the winner with a diagonal line!")
        return True
    elif board[2] == board[4] == board[6] == player:
        print(f"{player} is the winner with a diagonal line!")
        return True
    else:
        return False
