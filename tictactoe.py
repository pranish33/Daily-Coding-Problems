# creating tictactoe game using python programming language

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# global variable used later in the following code
game_still_going = True
Winner = None
current_player = "X"

# display board function which will return board of tictactoe


def display_board():
    print(board[0] + " | ", board[1] + " | ", board[2] + " | ")
    print(board[3] + " | ", board[4] + " | ", board[5] + " | ")
    print(board[6] + " | ", board[7] + " | ", board[8] + " | ")


# play game is the main function which will handle whole game
def play_game():
    display_board()
    # looping through function to check if game is still valid for playing or game is out of playing
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if Winner == "X" or Winner == "O":
        print(Winner + " Won. ")
    elif Winner == None:
        print("Game Tie")

    display_board()

# this function handle player's input position


def handle_turn(player):
    print(player, "s' turn")
    position = input("Choose the number between 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(
                "Invalid input please, choose the number between 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there, Try again: ")

    board[position] = player
    display_board()

# check if game is won or tie


def check_if_game_over():
    check_for_winner()
    check_if_game_tie()

# check if player win

# check player won or not


def check_for_winner():
    row_winner = check_rows()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    global Winner

    if row_winner:
        # winner winner
        Winner = row_winner
    elif column_winner:
        # winner winner
        Winner = column_winner
    elif diagonal_winner:
        # winner winner
        Winner = diagonal_winner
    else:
        # there is no win
        Winner = None
        # check row

# check function if game won in row


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return
# check column

# check function if game won in column


def check_column():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return

# check diagonal
# check function if game won in diagonal


def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# check if game tie


def check_if_game_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

# check if current player is "X" or "O"


def flip_player():

    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


# play game function calling
play_game()
