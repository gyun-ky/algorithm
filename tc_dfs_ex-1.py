import sys
input = sys.stdin.readline


graph = [
    [],
    [4, 3, 2],
    [2, 4],
    [1, 3, ],
    [3, 5],
    [3, 4],
]

visited = [False]*9

result = []

def dfs(node, graph, visited):
    visited[node] = True

    result.append(node)

    for n in graph[node]:
        if visited[n] == False:
            dfs(n, graph, visited)


dfs(1, graph, visited)
print(result)
        