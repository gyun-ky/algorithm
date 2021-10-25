import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

data = []
max_num = 0

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

visited = [[False] * M for _ in range(N)]

for _ in range(N):
    data.append(list(map(int, input().split())))

max_data = max(map(max, data))

def check(box, sum, i, j):
    global data, N, M, max_num, row, col
        
    if sum + max_data*(4-box) <= max_num:
        return

    if box == 4:
        if max_num < sum:
            max_num = sum
        return
        
    
    if i!=0 and j!=0 and i!=N-1 and j!=M-1:
        q = deque()
        q.append(data[i][j+1])
        q.append(data[i+1][j])
        q.append(data[i][j-1])

        for it in range(3, 7):
            tmp_sum = q[0]+q[1]+q[2] + data[i][j]
            if max_num < tmp_sum:
                max_num = tmp_sum
            q.popleft()
            q.append(data[i+row[it%4]][j+col[it%4]])
    else:
        if i==0 and (j!=0 and j!=M-1):
            tmp_sum = data[i][j] + data[i+row[0]][j+col[0]] + data[i+row[1]][j+col[1]] + data[i+row[2]][j+col[2]]
            max_num = max(tmp_sum, max_num)
        if i==N-1 and (j!=0 and j!=M-1):
            tmp_sum = data[i][j] + data[i+row[0]][j+col[0]] + data[i+row[3]][j+col[3]] + data[i+row[2]][j+col[2]]
            max_num = max(tmp_sum, max_num)
        if j==0 and (i!=0 and i!=N-1):
            tmp_sum = data[i][j] + data[i+row[0]][j+col[0]] + data[i+row[3]][j+col[3]] + data[i+row[1]][j+col[1]]
            max_num = max(tmp_sum, max_num)
        if j==M-1 and (i!=0 and i!=N-1):
            tmp_sum = data[i][j] + data[i+row[1]][j+col[1]] + data[i+row[3]][j+col[3]] + data[i+row[2]][j+col[2]]
            max_num = max(tmp_sum, max_num)

    
    for nIdx in range(0, 4):
        nrow = i + row[nIdx]
        ncol = j + col[nIdx]
        if 0<=nrow<N and 0<=ncol<M and visited[nrow][ncol] == False:
            visited[nrow][ncol] = True
            check(box+1, sum+data[nrow][ncol], nrow, ncol)
            visited[nrow][ncol] = False


for i in range(0, N):
    for j in range(0, M):
        visited[i][j] = True
        check(1, data[i][j], i, j)
        visited[i][j] = False

print(max_num)