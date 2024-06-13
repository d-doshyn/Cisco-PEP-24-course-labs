sudoku_grid = [
    [2, 9, 5, 7, 4, 3, 8, 6, 1],
    [4, 3, 1, 8, 6, 5, 9, 2, 7],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [1, 5, 4, 9, 3, 8, 6, 7, 2]
]

def sudoku_checking():
    for row in sudoku_grid:
        if len(row) != len(set(row)):
            print("No")
            return False

    for i in range(9):
        col_checking = []
        for row in sudoku_grid:
            col_checking.append(row[i])
        if len(col_checking) != len(set(col_checking)):
            print("No")
            return False
        
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            cube_checking = []
            for x in range(3):
                for y in range(3):
                    cube_checking.append(sudoku_grid[row + x][col + y])
            if len(cube_checking) != len(set(cube_checking)):
                print("No")
                return False
        
    print("Yes")
    return True
        
sudoku_checking()