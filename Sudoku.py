def Copy(sud):
    global board_initial
    board_initial= [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if sud[i][j] != 0:
                board_initial[i][j] = sud[i][j]
def validCube(i, j, board):
    list = []
    if 0 <= i < 3 and 0 <= j < 3:
        for i in range(3):
            for j in range(3):
                list.append(board[i][j])
        return list
    if 3 <= i < 6 and 0 <= j < 3:
        for i in range(3, 6):
            for j in range(3):
                list.append(board[i][j])
        return list
    if 6 <= i < 9 and 0 <= j < 3:
        for i in range(6, 9):
            for j in range(3):
                list.append(board[i][j])
        return list
    if 0 <= i < 3 and 3 <= j < 6:
        for i in range(3):
            for j in range(3, 6):
                list.append(board[i][j])
        return list
    if 0 <= i < 3 and 6 <= j < 9:
        for i in range(3):
            for j in range(6, 9):
                list.append(board[i][j])
        return list
    if 3 <= i < 6 and 3 <= j < 6:
        for i in range(3, 6):
            for j in range(3, 6):
                list.append(board[i][j])
        return list
    if 3 <= i < 6 and 6 <= j < 9:
        for i in range(3, 6):
            for j in range(6, 9):
                list.append(board[i][j])
        return list
    if 6 <= i < 9 and 3 <= j < 6:
        for i in range(6, 9):
            for j in range(3, 6):
                list.append(board[i][j])
        return list
    if 6 <= i < 9 and 6 <= j < 9:
        for i in range(6, 9):
            for j in range(6, 9):
                list.append(board[i][j])
        return list
def acceptable(value, board, i, j):
    if value not in board[i]:
        row = []
        for a in range(9):
            row.append(board[a][j])
        if value not in row:
            if value not in validCube(i, j, board):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def next():
    print('--- Going Forward ---')
    global i, j,v
    if j == 8 and i != 8:
        i += 1
        j = 0
        v+=1
    elif i == 8 and j == 8:
        print('last move')
    else:
        j += 1
        v+=1
def previous():
    print('--- Going Back ---')
    global i, j,v
    if j == 0 and i != 0:
        i -= 1
        j = 8
        v-=1
    elif i == 0 and j == 0:
        print('first pixel')
    else:
        j -= 1
        v-=1
def Done(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return True
    return False
def Solve(i, j, board):
    if board[i][j] == 0 :
        for value in range(9,0,-1):
            if value not in values[v]:
                if acceptable(value, board, i, j):
                    board[i][j] = value
                    values[v].append(value)
                    print(values)
                    print(value,'Added to Sudoku')
                    for k in range(9):
                        print(board[k][0:9])
                    print('\n')
                    break
def back():
    for t in range(v, 81):
        values[t] = []
    while True:
        previous()
        if board_initial[i][j]==0:
            board[i][j]=0
            break

values = [[] for p in range(81)]

board = [[8, 0, 0, 0, 0, 0, 0, 0, 7],
         [0, 0, 2, 7, 0, 8, 3, 0, 0],
         [0, 7, 0, 0, 9, 0, 0, 4, 0],
         [0, 4, 0, 0, 7, 0, 0, 9, 0],
         [0, 0, 8, 6, 0, 5, 1, 0, 0],
         [0, 1, 0, 0, 3, 0, 0, 5, 0],
         [0, 8, 0, 0, 4, 0, 0, 2, 0],
         [0, 0, 3, 5, 0, 9, 4, 0, 0],
         [5, 0, 0, 0, 0, 0, 0, 0, 1]]


for o in range(9):
    print(board[o][0:9])
print('\n')

Copy(board)

i = 0
j = 0
v = 0
while Done(board):
    Solve(i, j, board)
    if board[i][j]==0:
        back()
    else :
        next()
print('DONE')