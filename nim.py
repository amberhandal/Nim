#! /usr/bin/env python3

def board_init():
    default_board = [3, 5, 7]
    board = []
    use_default = input("Use default board [3, 5, 7]? (y/n): ").strip().lower()
    if use_default == 'y':
        return default_board
    else:
        rows = int(input("Enter number of rows: "))
        for row in range(1, rows + 1):
            if row < rows + 1:
                print(f"Enter sticks for row {row}: ")
                sticks = int(input())
                board.append(sticks)
                if sticks < 1:
                    print("You must have at least one stick in each row.")
                    return board_init()
        return board

def update_board(board, row, count):
    if 0 <= row < len(board) and 1 <= count <= board[row]:
        return True
    return False

def player_move(board, player):
    row_turn = True
    stick_turn = True
    print("\n----------------")
    print(f"\n{player}'s turn:")
    while row_turn:
        try:
            row = int(input(f"Choose a row (1-{len(board)}): ")) - 1
            if row < 0 or row >= len(board):
                print("\nHey, pick a real row!")
            elif board[row] == 0:
                print("\nThat row is empty! Pick another.\n")
            else:
                row_turn = False
        except ValueError:
            print("\nHey, pick a real row!")

    while stick_turn:
        try:
            count = int(input("Choose number of sticks to remove: "))
            if 0 <= row < len(board) and 1 <= count <= board[row]:
                board[row] -= count
                if sum(board) == 0:
                    print(f"{player} took the last stick!")
                    break
                stick_turn = False
            elif not count.is_integer() or count < 1:
                print("\nHey, pick a stick!")
            elif count > board[row]:
                print("\nNot that many sticks in that row!")
        except ValueError:
            print("\nHey, pick a stick!")
    update_board(board, row, count)

def nim(board):
    players = ["P1", "P2"]
    turn = 0
    while sum(board) > 0:
        print("\n----------------")
        for i, count in enumerate(board):
            print(f"{i + 1}: {'| ' * count}")
        player_move(board, players[turn])
        if sum(board) == 0:
            break
        turn = 1 - turn 
        
def main():
    print("------NIM------")
    board = board_init()
    nim(board)

if __name__ == "__main__":
    main()