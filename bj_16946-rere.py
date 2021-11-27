# bj_16946.py
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

answer = [[0 for c in range(M)] for r in range(N)]
group_array = [[-1 for c in range(M)] for r in range(N)]
wall_map = []
walls = []
for i in range(N):
    wall_map.append(list(map(int, input().strip())))
    # 모든 벽이 있는 곳은 벽을 깨고 시작하기 때문에 1로 초기화
    


visited = [[False for c in range(M)] for r in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(col, row, cnt, group_num):

    group_array[col][row] = group_num

    for i in range(4):
        ny = col + dy[i]
        nx = row + dx[i]

        if ny<0 or ny>=N or nx<0 or nx>=M:
            continue

        if wall_map[ny][nx] == 0 and visited[ny][nx] == False:
            visited[ny][nx] = True
            cnt = dfs(ny, nx, cnt+1, group_num)
            
    
    return cnt

 
group = []
group_num = 0

for i in range(N):
    for j in range(M):
        if wall_map[i][j] ==0 and visited[i][j] == False:
            visited[i][j] = True
            group.append(dfs(i, j, 1, group_num))
            group_num+=1

# wall_map에서의 1들 좌표 주변 조사 
# for wall in walls:
#     group_check = [False] * len(group)
#     for i in range(4):
#         ny = wall[0] + dy[i]
#         nx = wall[1] + dx[i]
        
#         if 0<=ny<N and 0<=nx<M and wall_map[ny][nx] == 0 and group_check[group_array[ny][nx]] == False:
#             answer[wall[0]][wall[1]] += group[group_array[ny][nx]]
#             group_check[group_array[ny][nx]] == True





for i in range(N):
    for j in range(M):
        if wall_map[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for nd in range(4):
                ny = i+dy[nd]
                nx = j+dx[nd]
            
                if 0<=ny<N and 0<=nx<M and wall_map[ny][nx] == 0 :
                    near.add(group_array[ny][nx])
                
            ans = 1
            for n in near:
                ans += group[n]
                
            print(ans%10, end='')

    print()

        




