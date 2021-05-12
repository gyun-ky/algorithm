import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미 = 10억

# Node의 개수 및 edge 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for i in range(0, n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 edge 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())
    #a에서 b node로 가는 비용이 c라는 이야기
    graph[a].append((b,c))

# 방문하지 않은 Node들 중에서 가장 최단 거리가 짧은 Node 번호
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if visited[i] is False and distance[i]<min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 Node 기준으로 초기화
    distance[start] = 0
    visited[start] = True
    # 시작 Node에 붙어 있는 node들과의 distance를 업데이트
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 Node와 연결된 모든 Node들을 비교하여 만약에 cost가 더 낮다면 distance에 넣어주기
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])




