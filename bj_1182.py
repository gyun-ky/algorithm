import sys
input = sys.stdin.readline

N, S = map(int, input().split())

data = list(map(int, input().split()))

answer = 0


def dfs(idx, sum, answer):
    sum += data[idx]
    if sum == S: 
        answer += 1

    if idx == N-1:
        return answer
    
    for i in range(idx+1, N):
        answer = dfs(i, sum, answer)
    return answer
    
        

for i in range(0, N):
    sum = data[i]
    if sum == S :
        answer+=1
    if i != N-1:
        for j in range(i+1, N):
            answer = dfs(j, sum, answer)


print(answer)