from random import randrange

field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    print( f'''
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+''')
display_board(field)

def enter_move(board):
    move = int(input("Enter your move (1-9): "))
    field_row = (move - 1) // 3
    field_col = (move - 1) % 3
    
    if board[field_row][field_col] not in ["X", "O"]:
        board[field_row][field_col] = "X"
        display_board(board)
    else:
        print("This place i occupied. Try again.")
        enter_move(field)

def computer_move(board):
    while True:
        move = randrange(9)
        field_row = move // 3
        field_col = move % 3
        
        if board[field_row][field_col] not in ["X", "O"]:
            board[field_row][field_col] = "O"
            print("Computer's move: ", move + 1)
            display_board(board)
            break
        else:
            continue

def victory_for(board, sign):
    victory_combinations = [[1, 4, 7], [1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for combination in victory_combinations:
        if all(board[(i - 1) // 3][(i - 1) % 3] == sign for i in combination):
            print(sign, "won!")
            return True
    return False

def draw_move(board):
    for row in board:
        for cell in row:
            if cell not in ["X", "O"]:
                return False
    print("It's a draw!")
    return True
    
while True:
    enter_move(field)
    if victory_for(field, "O"):
        break
    if draw_move(field):
        break
    computer_move(field)
    if victory_for(field, "X"):
        break
    if draw_move(field):
        break