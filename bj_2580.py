import sys
input = sys.stdin.readline


data = []

blank = []

row_memo = [[False]*10 for _ in range(9)]
col_memo = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]

# print(row_memo)
# print(col_memo)

def box_loc(i, j):
    # if i//3 == 0:
    #     return j//3
    
    # elif i//3 == 1:
    #     return 3 + (j//3)

    # else:
    #     return 6 + (j//3)
    return (i//3)*3 + j//3

for i in range(0, 9):
    data.append(list(map(int,  input().split())))
    for j in range(0, 9):
        if data[i][j] == 0:
            blank.append((i, j))
        else:
            box[box_loc(i, j)][data[i][j]] = True
            row_memo[i][data[i][j]] = True
            col_memo[j][data[i][j]] = True

# print("------data----------")
# print(data)
# print("------blank--------")
# print(blank)
# print("------box--------")
# print(box)

# print(blank[1][1])

            

def sudoku(blank_idx):

    if blank_idx == len(blank):
        for i in range(9):
            for j in range(9):
                print(data[i][j], end=' ')
            print()
        sys.exit()

    row = blank[blank_idx][0]
    col = blank[blank_idx][1]

    for n in range(1, 10):
        if row_memo[row][n] == False and col_memo[col][n] == False and box[box_loc(row,col)][n] == False:
            data[row][col] = n
            row_memo[row][n] = True
            col_memo[col][n] = True
            box[box_loc(row,col)][n] = True
            sudoku(blank_idx+1)
            row_memo[row][n] = False
            col_memo[col][n] = False
            box[box_loc(row,col)][n] = False

sudoku(0)

