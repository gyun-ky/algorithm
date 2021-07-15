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

def promising(index):
    switch = True

    while i <index and switch is True:
        if w[index][i] == 1 and vcolor[i] == vcolor[index]:
            switch = False
        i+=1
    
    return switch
    


def coloring(index):
    if promising(index):
        if index == n:
            for i in range(1, n+1):
                print(vcolor[i], end=' ')
        for color in range(1, c+1):
            vcolor[index] = color
            coloring[index+1]
    
            
            