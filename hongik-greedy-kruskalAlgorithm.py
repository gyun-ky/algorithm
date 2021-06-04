# 크루스칼 알고리즘으로 최소비용 신장트리 만들기

n = int(input())
INF = int(1e9)


class Vertex:
    def __init__(self, p):
        self.depth = 0
        self.parent = p

# V - 크루스칼 알고리즘을 위한 vertex
# init - 각 vertex 서로소 집합 만들기
# v[]
V = [Vertex(i) for i in range(0, n+1)]
print(V)

# vertex i가 속해있는 집합을 찾기 
# 속한 집합 최상단 vertex index return
def find(i):
    while V[i].parent != i:
        i = V[i].parent
    
    return i

# 두 집합 합치기
# 인자 값은 각 집합의 최상단 index
def merge(p, q):
    if V[p].depth == V[q].depth:
        V[p].parent = q
        V[q].depth += 1

    elif V[p].depth > V[q].depth:
        V[q].parent = p
    else:
        V[p].parent = q

# vertex p와 q가 속한 집합이 같은 집합인 경우 True
def equal(p, q):
    if find(p) == find(q):
        return True
    else:
        return False
        


# W - vertex 두개, 두개 사이의 가중치가 반영된 비방향 그래프
# 각 row[0]=vertex1 / row[1]=vertex2 / row[2]=vertex3
W =[]

# 최종 edge 보관 list
F = []

# 가중치 기준으로 작은 것부터 정렬된 순서로 넣기 
while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break
    W.append(inputs)

print(W)

while len(W) != 0:
    # 이음선 연결하는 두 vertex가 같은 집합이 아닌 경우에만 집합으로 묶어주기
    if equal(W[0][0], W[0][1]) is False:
        merge(find(W[0][0]), find(W[0][1]))
        F.append((W[0][0], W[0][1])) 
    
    W.pop(0)


print(F)