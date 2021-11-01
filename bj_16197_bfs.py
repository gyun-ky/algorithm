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

min_num = int(1e9)

def check_boundary(x, y):
    if x<0 or x>=M or y<0 or y>=N:
        return True
    return False

def search(cnt, x1, y1, x2, y2):
    global min_num

    if cnt==11 :
        return 

    if check_boundary(x1, y1) ^ check_boundary(x2, y2):
        min_num = min(cnt, min_num)
        return

    if check_boundary(x1, y1) & check_boundary(x2, y2):
        return

    
    
    for i in range(0, 4):
        nx1 = x1 + col[i]
        ny1 = y1 + row[i]
        nx2 = x2 + col[i]
        ny2 = y2 + row[i]

        if 0<=ny1<N and 0<=nx1<M and board[ny1][nx1] == '#':
            nx1, ny1 = x1, y1

        if 0<=ny2<N and 0<=nx2<M and board[ny2][nx2] == '#':
            nx2, ny2 = x2, y2

        search(cnt + 1, nx1, ny1, nx2, ny2)




search(0, coin[0][1], coin[0][0], coin[1][1], coin[1][0])

if min_num == int(1e9):
    print(-1)
else:
    print(min_num)





