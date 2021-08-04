import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for i in range(0, n+1)]

via = [[0]*(n+1) for i in range(0, n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0
            via[i][j] = i

for _ in range(0, m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    via[b][a] = a
    via[a][b] = b

# k = 중간 방문 소개팅녀 회사 / x = 최종 계약 회사 / 판매원은 1번 회사
x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k]+graph[k][j]<graph[i][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
                via[i][j] = k
            

path = list()

def split(s, e):
    
    if(via[s][e]==e):
        path.append(s)
        path.append(e)
    else:
        split(s, via[s][e])
        path.pop()
        split(via[s][e], e)


print(graph[1][k] + graph[k][x])

print(via)
print(1, end=" ")
split(1, k)
print()
split(k, x)

print(path)