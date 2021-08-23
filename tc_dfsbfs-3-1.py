
# N - 얼음틀 세로 길이 M - 얼음틀 가로 길이
N, M = map(int, input().split())

graph = []
# visited = [[False]*(M+1) for _ in range(0, N+1)]
# visited 대신 graph의 0을 1로 바꿈으로 visited 처리

direct_row = [-1, 0, 1, 0]
direct_col = [0, 1, 0, -1]

for _ in range(N):
    graph.append(list(map(int, input())))

print(graph)


def dfs(graph, row, col):
    
    
    # 범위를 넘어선 경우
    if row < 0 or row > N-1 or col < 0 or col > M-1 :
        return False

    # 이미 방문했거나 애초부터 1인 경우
    if graph[row][col] == 1:
        return False

    if graph[row][col] == 0:
        graph[row][col] = 1
        for d in range(4):
            new_row = row + direct_row[d]
            new_col = col + direct_col[d]
            
            print(f'{new_row} , {new_col}')
            dfs(graph, new_row, new_col)
        return True



cnt = 0   


for i in range(0, N):
    for j in range(0, M):
        if dfs(graph, i, j) == True:
            cnt+=1
        



print(cnt)



