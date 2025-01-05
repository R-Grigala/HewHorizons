def is_valid_sudoku(board):
    for row in board:
        if sorted(row) != list("123456789"):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if sorted(column) != list("123456789"):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            sub_square = [
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if sorted(sub_square) != list("123456789"):
                return False

    return True


# Read 9 rows of Sudoku input
sudoku = []
print("Enter the Sudoku board row by row (9 rows, 9 digits each):")
for _ in range(9):
    row = input().strip()
    if len(row) != 9 or not row.isdigit():
        print("Invalid input. Each row must be exactly 9 digits.")
        exit()
    sudoku.append(row)

if is_valid_sudoku(sudoku):
    print("Yes")
else:
    print("No")