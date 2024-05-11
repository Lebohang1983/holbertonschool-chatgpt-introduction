#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if row not in range(3) or col not in range(3):
            print("Invalid input! Row and column must be between 0 and 2. Try again.")
            continue
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("Player " + player + " wins!")

def test_game():
    # Test case 1: Player X wins horizontally
    board = [["X", "X", "X"],
             [" ", " ", " "],
             [" ", " ", " "]]
    assert check_winner(board) == True

    # Test case 2: Player O wins vertically
    board = [["O", " ", " "],
             ["O", " ", " "],
             ["O", " ", " "]]
    assert check_winner(board) == True

    # Test case 3: Player X wins diagonally
    board = [["X", " ", " "],
             [" ", "X", " "],
             [" ", " ", "X"]]
    assert check_winner(board) == True

    # Test case 4: Game ends in a draw
    board = [["X", "O", "X"],
             ["X", "O", "O"],
             ["O", "X", "X"]]
    assert check_winner(board) == False

    print("All test cases passed!")

if __name__ == "__main__":
    test_game()

