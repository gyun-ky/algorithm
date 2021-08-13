import sys
import heapq
input = sys.stdin.readline

arry = []

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

for i in range(0, N):
    heapq.heappush(arry, (-data[i], data[i]))

print(arry)

sum = 0
cnt = 0
flag = 1
first = heapq.heappop(arry)[1]
second = heapq.heappop(arry)[1]
while cnt<M:
    
    if flag ==1:
        
        for i in range(0, K):
            if cnt < M:
                sum += first
                cnt += 1
            else:
                break
        flag = 0

    elif flag == 0:
        sum += second
        cnt += 1
        if cnt >= M:
            break
        flag = 1

print(sum)

sum = 0
cir_num = K + 1
sum += (M/cir_num) * (first*K + second)
sum += (M%cir_num) * first

print(sum)