def print_board(board):
    print("-------------")
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("-------------")

def check_winner(board, player):
    for i in range(3):
        # Check rows
        if all(cell == player for cell in board[i]):
            return True

        # Check columns
        if all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}, it's your turn.")
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("Invalid move. That position is already occupied.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

play_game()
