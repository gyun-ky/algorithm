W = int(input())
n = int(input())

price = list(map(int, input().split()))
price.insert(0, 0)
weight = list(map(int, input().split()))
weight.insert(0, 0)
print(price)
print(weight)


p = [[0 for col in range(0, W+1)] for row in range(0, n+1)]

print(p)

for i in range(1, n+1):
    for w in range(1, W+1):
        if weight[i] > w:
            p[i][w] = p[i-1][w]
        else:
            p[i][w] = max(p[i-1][w], price[i]+p[i-1][w-weight[i]])
        
            

print(p)

print(p[n][W])






