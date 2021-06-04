# 1. i까지 가는 데에 걸리는 최소 비용 담은 D[i]를 만들고 시작점에서 연결되어 있는 노드들로 가는 비용으로 일단 초기화한다
# 2. 시작 지점에서 작은 비용이 있는 곳으로 일단 간 후 D 배열 업데이트 비용은 누적하여 메무한다

# Y - 최단 경로를 구하려고 하는 vertex가 포함된 집합 즉, visited
# F - 가까운 vertex 선택 후 이음선 저장 집합

INF = int(1e9)
n = int(input())

# 이어진 edge들 메모
E = []

W = [[INF for i in range(0, n+1)] for j in range(0, n+1)]

for i in range(1, n+1):
    W[i][i] = 0


# W - 가중치가 반영된 방향 그래프
while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break
    W[inputs[0]][inputs[1]] = inputs[2]


# 시작점은 1

# length[i] - 시작점에서 vertex i 까지의 최단 거리
length = [0] * n+1
# touch - vertex i가 E 집합 중에서 어디와 제일 가까운지
touch = [0] * n+1
for i in range(2, n+1):
    touch[i] = 1
    length[i] = W[1][i]

for loop in range(0, n-1):
    min = INF
    for i in range(2, n+1):
        if min > length[i] and length[i] >=0:
            min = length[i]
            vertex = i
    
    E.append((touch[vertex], vertex))

    for i in range(2, n+1):
        if length[i] + W[vertex][i] < length[i]:
            touch[i] = vertex
            length[i] = length[i] + W[vertex][i]
    
    length[vertex] = -1





