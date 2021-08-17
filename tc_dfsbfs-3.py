
# N - 얼음틀 세로 길이 M - 얼음틀 가로 길이
N, M = map(int, input().split())

graph = []
visited = [[False]*(M+1) for _ in range(0, N+1)]

direct_row = [-1, 0, 1, 0]
direct_col = [0, 1, 0, -1]

for _ in range(N):
    graph.append(list(map(int, input())))

print(graph)


def dfs(graph, visited, row, col, result):
    
    if graph[row][col] == 1 or visited[row][col] == True:
        visited[row][col] = True
        return
    visited[row][col] = True
    result.append((row, col))
    
    

    for d in range(4):
        new_row = row + direct_row[d]
        new_col = col + direct_col[d]
        if new_row < 0 or new_row > N-1 or new_col < 0 or new_col > M-1 or visited[new_row][new_col] == True :
            continue
        print(f'{new_row} , {new_col}')
        if graph[new_row][new_col] == 0:
            dfs(graph, visited, new_row, new_col, result)


cnt = 0   


for i in range(0, N):
    for j in range(0, M):
        result = []
        if visited[i][j] == True:
            continue
        dfs(graph, visited, i, j, result)
        if len(result) != 0:
            print("count 1 추가")
            cnt +=1



print(cnt)



