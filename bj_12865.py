import sys
input = sys.stdin.readline()

N, K = map(int, input().split())

product = []
visited = [False for _ in range(N)]

for i in range(N):
    product.append(list(map(int, input().split())))


max_value = 0

def dfs(p_idx, value, remain):
    global max_value

    if p_idx == N-1:
        max_value = max(max_value, value)
        return

    if remain < product[p_idx+1][0]:
        max_value = max(max_value, value)
        return
    
    next_p_idx = p_idx+1

    dfs(next_p_idx, value+product[next_p_idx][1], remain-product[next_p_idx][0])

    dfs(next_p_idx, value, remain)


product.sort(key=lambda x : x[0])

dfs(0, product[0][1], K-product[0][0])

dfs(0, 0, K)

print(max_value)