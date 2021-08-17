import sys
input = sys.stdin.readline

stack = []
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
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
        