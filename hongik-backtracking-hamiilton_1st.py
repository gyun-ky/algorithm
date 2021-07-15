# node의 개수
n = int(input())
# 시작 노드
start = int(input())

way = [0 for i in range(0, n+1)]

way[1] = start

w = [[0 for col in range(0, n+1)] for row in range(0, n+1)]

for i in range(0, n*n):
    a, b = map(int, input().split())
    if(a == 0 and b == 0):
        break
    else:
        w[a][b] = 1
        w[b][a] = 1

def promising(node, num):
    i = 1
    while i<=num:
        if way[i] == node:
            return 0
        i+=1
    return 1

def hamiltonian(node, num):
    if num == n:
        if w[node][start] == 1:
            for k in range(1, n+1):
                print(way[k], end=" ")
            print()
        return
    i = 1
    while i<= n:
        if i==node:
            i+=1
            continue
        if w[node][i] == 1:
            if promising(i, num) == 1:
                way[num+1] = i
                hamiltonian(i, num+1)
        i+=1

hamiltonian(1, 1)