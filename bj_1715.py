# 정렬된 두 묶음의 카드 A, B 
# 합치려면 비교해야

# N개의 숫자 카드 묶음 -> 최소한 몇번의 비교?

# 항상 작은 묶음과 합치면 된다

import heapq

# 10 + 20 + 30 + 30 + 60 + 40

N = int(input())

card_group = []
for i in range(N):
    num = int(input())
    heapq.heappush(card_group, num)

if N == 1:
    print(0)
    exit(0)

answer = 0
while True:
    if len(card_group) == 1:
        break
    a = heapq.heappop(card_group)
    b = heapq.heappop(card_group)

    answer += (a+b)
    heapq.heappush(card_group, a+b)

print(answer)

# 10 11 12 21

# 21 + (21+ 12) + 
