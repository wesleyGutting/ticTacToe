def render (row1, row2, row3):
    print("     |   |     ")
    print(f"  {row1[0]}  | {row1[1]} | {row1[2]} ")
    print("-----|---|-----")
    print(f"  {row2[0]}  | {row2[1]} | {row2[2]} ")
    print("-----|---|-----")
    print(f"  {row3[0]}  | {row3[1]} | {row3[2]} ")
    print("     |   |     ")

def check_input (x):
    y = check_type(x)
    while y > 3:
        y = check_type(input("Please enter a number <= 3: "))
    return y

def check_type(x):
    while not isinstance(x, int):
        try:
            x = int(x)
        except:
            x = input("Please enter a number: ")
    return x

def check_win(board):
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return True
    elif board[1][0] == board[1][1] == board[1][2] != " ":
        return True
    elif board[2][0] == board[2][1] == board[2][2] != " ":
        return True
    elif board[0][0] == board[1][0] == board[2][0] != " ":
        return True
    elif board[0][1] == board[1][1] == board[2][1] != " ":
        return True
    elif board[0][2] == board[1][2] == board[2][2] != " ":
        return True
    elif board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[2][0] == board[1][1] == board[0][2] != " ":
        return True
    else:
        return False

def check_game(answer):
    while answer.upper != "Y" and answer.upper() != "N":
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else:
            answer = input("Please enter Y or N: ")

def game_loop():
    winner = False
    piece = " "
    turn = 1

    top = [" "," "," "]
    mid = [" "," "," "]
    bot = [" "," "," "]
    board = [top, mid, bot]

    while winner == False:
        render(top, mid, bot)
        row = check_input(input("Which row will you play on? (1, 2, or 3 Top to Bottom): "))
        column = check_input(input("Which spot in that row? (1, 2, 3 Left to Right): "))

        if turn % 2 == 1:
            piece = "X"
        else:
            piece = "O"

        if board[row - 1][column - 1] == "X" or board[row - 1][column - 1] == "O":
            print("That spot has been played already")
        else:
            board[row - 1][column - 1] = piece
            winner = check_win(board)
            turn += 1

    render(top, mid, bot)
    print(f"Player {piece} has won!")

while True:
    answer = check_game(input("Would you like to play a game?: "))
    if answer == True:
        game_loop()
    else:
        print("Goodbye.")
        break
