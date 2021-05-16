n = int(input())
# n - node의 개수
c = int(input())
# c - color의 개수


w = [[0 for col in range(0, n+1)] for row in range(0, n+1)]

for i in range(0, n*n):
    a, b = map(int, input().split())
    if(a == 0 and b == 0):
        break
    else:
        w[a][b] = 1
        w[b][a] = 1

vcolor = [0 for i in range(0, n+1)]
print(vcolor)
print(w)


def promising(node, color):
    if node == 1:
        return 1

    i = 1
    while i<node:
        if w[node][i] == 1 and vcolor[i] == color:
            return 0
        i+=1
    return 1


def coloring(node):
    for color in range(1, c+1):
        if promising(node, color) == 1:
            vcolor[node] = color
            if node == n:
                for i in range(1, n+1):
                    print(f'{vcolor[i]} ', end=' ')
                print()
            else:
                coloring(node+1)


coloring(1)
