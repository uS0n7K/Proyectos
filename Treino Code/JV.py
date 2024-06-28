import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def bot_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    return None

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            while True:
                move = input("Enter your move (row and column): ")
                try:
                    row, col = map(int, move.split())
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        break
                    else:
                        print("Cell is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter row and column as two numbers separated by space.")
        else:
            row, col = bot_move(board)
            board[row][col] = "O"
            print(f"Bot chose: {row} {col}")

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()