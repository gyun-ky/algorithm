n = int(input())
INF = int(1e9) #무한을 의미 = 10억

# DP는 s에서 d까지 가는데에 걸리는 최소 거리
DP = [[INF for i in range(0, n+1)] for j in range(0, n+1)]

# s->d로 가는 경로에 있는 node number 중 가장 큰것
P = [[0 for i in range(0, n+1)] for j in range(0, n+1)]

for same in range(1, n+1):
    DP[same][same] = 0

while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0 and inputs[1] == 0:
        break
    # 아무것도 중간에서 경유해가지 않을 때의 걸리는 최소 거리
    # 각 노드의 edge들의 가중치로 초기화
    DP[inputs[0]][inputs[1]] = inputs[2]

# 각각의 노드에서 노드를 (s->d)로 갈 때, 각 node를 경유하도록 하나씩 추가하면서 그떄의 최소 거리를 구한다
# {node1, node2, node3} 포함하여 계산한 경로의 최소거리를 가지고 {node1, node2, node3, node4}를 포함하여 개선한 경로의 최소 거리 구하면 됨
for k in range(1, n+1):
    for s in range(1, n+1):
        for d in range(1, n+1):
            # 이번 k번째 node 추가시, 더 작은 최소 거리가 되는지 파악
            if (DP[s][k]+DP[k][d]) < DP[s][d]:
                P[s][d] = k
                DP[s][d] = DP[s][k]+DP[k][d]

print(DP)
print(P)

start = int(input())
destination = int(input())


# s->d 까지의 최단 경로 node들 순서
pathList = [start, ]
# def path(s, d):
#     if P[s][d] == 0:
#         pathList.append(d)
#         return
    
#     path(s, P[s][d])
#     pathList.append(d)

def path(s, d):
    if P[s][d] == 0:
        # 해당 d로의 경로 존재하지 않으면 탈출하면서 각 P[s][d]들을 저장하게 한다
        return 
    # 각 P는 s 와 d 일 때, 최단 경로 중 가장 큰 node number를 가지고 있으므로 재귀를 통해 하나씩 밑으로 알아간다
    path(s, P[s][d])
    pathList.append(P[s][d])

pathList.append(destination)

path(start, destination)

print(pathList)


