# 프림의 알고리즘

n = int(input())
INF = int(1e9)

# E - 이어진 edge들 가짐
E = []
# V - 이어진 vetex들이 순서대로 있는 list
V = [1, ]

W = [[INF for i in range(0, n+1)] for j in range(0, n+1)]

for i in range(1, n+1):
    W[i][i] = 0

# W - 가중치가 반영된 비방향 그래프
while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break
    W[inputs[0]][inputs[1]] = inputs[2]
    W[inputs[1]][inputs[0]] = inputs[2]

# distance - V에 포함된 vertex와 distance가 가리키는 index를 가진 vertex와의 거리가 얼마인지 표현
# 거리가 더 짧은 vertex를 발견하면 해당 vertex를 index로 가지는 nearest에 메모
distance = [0 for i in range(0, n+1)]
for i in range(2, n+1):
    distance[i] = W[1][i]

# nearest - index i vertex와 가장 가까운 V의 vertex의 index
# 가장 가까운 distance값을 가진 vertex가 (nearest[i])가 V중의 누구와 제일 가까운지를 표시
# v1은 V에 넣고 시작할 것이기 때문에 모든 배열에 1을 미리 넣어둠
nearest = [1 for i in range(0, n+1)]
print(nearest)

# V에 포함된 첫 시작 vertex
vertex = 1

# V에 1을 미리 넣었으니 n-1회 반복
for loop in range(0, n-1):
    min = INF
    # V 외부에 있는 vertex 간의 거리 중에서 가장 최소 거리인 vertex를 뽑기 
    for i in range(2, n+1):
        if distance[i]<min and distance[i]>=0:
            min = distance[i]
            vertex = i
    
    # V에 vertex 추가
    V.append(vertex)

    # E에 edge 쌍을 추가
    # 처음 돌리는 경우 1이 들어가 있다. 즉 V에 1밖에 없으니 연결될 외부 vertex는 1뿐이라는 거다
    # ex) 외부 vertex 2에 가장 가까운 nearest V 속하는 vertex
    E.append((vertex, nearest[vertex]))

    # 이제 vertex 값을 V에 넣어줬으니 더이상 해당 vertex는 검사 안해도 된다 
    # -1로 초기화해서 아예 검사를 안하도록 해주자
    distance[vertex] = -1

    print(f'nearest : {nearest}')
    print(f'distance : {distance}')
    # 이제 새롭게 선정된 vertex 기준으로 distance를 다시 만들어준다
    # 그럼 이전 것들이랑 어케 구별하냐? 가장 최소 값을 찾아주는 것이라서 누적되면서 비교가 된다 또한 distance값이 바뀌면 nearest에 등록이 된다!
    for i in range(2, n+1):
        # 새롭게 선택된 V 소속 vertex가 이전 선배의 data위에 새 정보 쌓는다! 더 작은 경우 찾았을 때만!
        if W[vertex][i] < distance[i]:
            # V 집합과 해당 index와의 거리를 더 짧은 거리로 업데이트!
            distance[i] = W[vertex][i]
            # 외부 vertex가 V에 등록될 것을 대비해서 nearest도 바꿔주어야 한다 !!! nearest[외부 vertex] = V안의 vertex !!!
            nearest[i] = vertex



print(V)
print(E)
