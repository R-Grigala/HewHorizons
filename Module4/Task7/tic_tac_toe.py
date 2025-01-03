from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|  " + "    |  ".join(str(cell) for cell in row) + "    |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError("Invalid input. Please enter a number between 1 and 9.")
            
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == move:
                        board[i][j] = 'O'
                        return
            print("The selected square is not free. Try again.")
        except ValueError as e:
            print(e)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if isinstance(cell, int):  # Square is free if it contains a number.
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    win_conditions = [
        # Horizontal
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Vertical
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = free_fields[randrange(len(free_fields))]
        board[move[0]][move[1]] = 'X'

def tic_tac_toe():
    board = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
    ]
    
    while True:
        display_board(board)
        
        # User's turn
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("You won!")
            break
        
        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Computer's turn
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("The computer won!")
            break

        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break


# Run the game
tic_tac_toe()