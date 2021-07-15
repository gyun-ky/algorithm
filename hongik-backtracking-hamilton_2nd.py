# node의 개수
n = int(input())
# 시작 노드
start = 1

vIndex = [0] * n+1

w = [[0 for col in range(0, n+1)] for row in range(0, n+1)]

for i in range(0, n*n):
    a, b = map(int, input().split())
    if(a == 0 and b == 0):
        break
    else:
        w[a][b] = 1
        w[b][a] = 1

def promising(index):
    switch = True
    if index == n and w[n][start] == 0 :
        switch = False
    elif index > 1 and w[vIndex[index-1]][vIndex[index]] == 0:
        switch = False
    else:
        for i in range(2, index):
            if vIndex[i] == vIndex[index]:
                switch = False
        
    return switch



def hamilton(index):
    if promising(index):
        if index == n:
            for i in range(1, n+1):
                print(vIndex[i], end=" ")
        for i in range(2, n+1):
            vIndex[index+1] = i
            hamiltonian(i+1)


        