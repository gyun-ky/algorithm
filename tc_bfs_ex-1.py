import sys
from collections import deque
input = sys.stdin.readline

visited = [False]*9


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

result = []

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        result.append(node)
        for i in graph[node]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True

bfs(graph, 1, visited)

print(result)

