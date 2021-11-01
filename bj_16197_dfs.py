import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

coin = []

for i in range(N):
    board.append(list(input().strip()))
    for j in range(M):
        if board[i][j] == 'o':
            coin.append([i, j])


# 오 아 왼 위
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

# visited_1 = [[False]*M for _ in range(N)]
# visited_2 = [[False]*M for _ in range(N)]

min_num = int(1e9)

def check_drop(x, y):
    if x<0 or x>=M or y<0 or y>=N:
        return True

    return False

def search(move, y1, x1, y2, x2):
    global min_num

    
    if move>=10:
        return
    else:
        move = move+1
        for i in range(0, 4):

            ny1 = y1 + row[i]
            nx1 = x1 + col[i]

            ny2 = y2 + row[i]
            nx2 = x2 + col[i]

            check_drop_1 = check_drop(nx1, ny1)
            check_drop_2 = check_drop(nx2, ny2)

            if check_drop_1 ^ check_drop_2:
                min_num = min(move, min_num)
                return
            elif check_drop_2 & check_drop_2:
                continue
            else:
                if board[ny1][nx1] == '#':
                    ny1, nx1 = y1, x1
                if board[ny2][nx2] == '#':
                    ny2, nx2 = y2, x2
                search(move, ny1, nx1, ny2, nx2)

search(0, coin[0][0], coin[0][1], coin[1][0], coin[1][1])


if min_num == int(1e9):
    print(-1)
else:
    print(min_num)



