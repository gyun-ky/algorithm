# bj_16946.py
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

answer = [[0 for c in range(M)] for r in range(N)]
wall = []
for i in range(N):
    wall.append(list(map(int, input().strip())))
    # 모든 벽이 있는 곳은 벽을 깨고 시작하기 때문에 1로 초기화
    for j in range(M):
        if wall[i][j] == 1:
            answer[i][j] = 1

        

visited = [[False for c in range(M)] for r in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(col, row):
    global answer
    
    q = list()

    q.append((col, row, 0))
    visited[col][row] = True

    total_cnt = 0

    while q:
        cur = q.pop()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]

            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == False:
                
                # bfs 하다가 벽을 만난 경우
                if wall[ny][nx] == 1:
                    # 여태까지 거쳐왔던 빈칸의 개수를 더함 - (ny,nx)와 (col, row) 가 연결된 빈칸의 수
                    answer[ny][nx] += cur[2]
                    print("------")
                    for i in range(N):
                        for j in range(M):
                            print(answer[i][j], end="")
                        print()
                    continue 
                
                cnt = cur[2]+1
                q.append((ny, nx, cnt))
                total_cnt+=1
                visited[ny][nx] = True
    
    return total_cnt


def dfs(col, row):

    visited[col][row] = True

    total_cnt = 0

    for i in range(4):
        # dfs 시작점 - 1인 점의 주변(우하좌상) 좌표들
        ny = col + dy[i]
        nx = row + dx[i]

        stack = []
        dfs_cnt = 0
        wall_detect = []
        if 0<=ny<N and 0<=nx<M and visited[ny][nx] == False:
            stack.append((ny, nx))

        while stack: 
            cur = stack.pop()
            
            # dfs 하다가 벽을 만난 경우
            if wall[cur[0]][cur[1]] == 1:
                # 이 dfs 그래프에 연결된 y,x 저장
                wall_detect.append((cur[0], cur[1]))
                continue 
                
            dfs_cnt += 1
            visited[cur[0]][cur[1]] = True
            for i in range(4):
                nny = cur[0]+dy[i]
                nnx = cur[1]+dx[i]
                if 0<=nny<N and 0<=nnx<M and visited[nny][nnx] == False:
                    stack.append((nny, nnx))
                    
                    
        for detect in wall_detect:
            answer[detect[0]][detect[1]] += dfs_cnt

        total_cnt += dfs_cnt
        
    
    return total_cnt



for i in range(N):
    for j in range(M):
        if wall[i][j] ==1 and visited[i][j] == False:
            answer[i][j] += dfs(i, j)
            visited[i][j] = True

for i in range(N):
    for j in range(M):
        print(answer[i][j]%10, end="")
    print()

        




