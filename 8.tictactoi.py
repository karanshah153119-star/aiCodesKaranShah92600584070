 
# Two Player Tic-Tac-Toe Game
# Using Heuristic Function

def display(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Heuristic function
def heuristic(board):
    win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == "X":
            return 2
        elif board[a] == board[b] == board[c] == "O":
            return 5

    return 10


# Main game
board = [" "] * 9
player = "X"
turns = 0

while turns < 9:
    display(board)
    print("Player", player)

    try:
        position = int(input("Enter position (1-9): ")) - 1
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if position < 0 or position > 8:
        print("Invalid position! Choose from 1 to 9.")
        continue

    if board[position] != " ":
        print("This position is already filled! Try again.")
        continue

    board[position] = player
    turns += 1

    score = heuristic(board)

    if score == 2:
        display(board)
        print("Player X Wins!")
        break

    elif score == 5:
        display(board)
        print("Player O Wins!")
        break

    player = "O" if player == "X" else "X"

else:
    display(board)
    print("Game Draw!")
