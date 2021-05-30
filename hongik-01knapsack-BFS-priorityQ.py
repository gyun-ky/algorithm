from collections import deque
from queue import PriorityQueue

W = int(input())
n = int(input())

price = list(map(int, input().split()))
price.insert(0, 0)
weight = list(map(int, input().split()))
weight.insert(0, 0)

class Status:

    def __init__(self):
        self.level = 0
        self.profit = 0
        self.weight = 0
        self.bound = 0

    def __str__(self):
        return f'{self.level} - {self.profit}'


def bound(level, cur_profit, cur_weight):
    l = level+1
    w = cur_weight
    p = cur_profit
    if cur_weight > W:
        return 0
    while l<=n :
        if w + weight[l] > W:
            p += price[l]/weight[l] * (W-w)
            break
        else:
            w += weight[l]
            p += price[l]
            l+=1
    return p


statusArr = list(Status() for i in range(10000))

print(f'price = {price}')
print(f'weight = {weight}')

max_profit = 0
Q = PriorityQueue()

index = 0
statusArr[index].level = 0
statusArr[index].profit = 0
statusArr[index].weight = 0

Q.put(statusArr[index])
index+=1
print(Q)
while len(Q) != 0:
    prev = Q.popleft()
    is_present = statusArr[index]
    is_present.level = prev.level + 1
    is_present.weight = prev.weight + weight[is_present.level]
    is_present.profit = prev.profit + price[is_present.level]
    print(f'level = {is_present.level} / weight = {is_present.weight} / profit = {is_present.profit}')
    if is_present.weight <= W and is_present.profit > max_profit:
        max_profit = is_present.profit
    if bound(is_present.level, is_present.profit, is_present.weight) > max_profit:
        print(bound(is_present.level, is_present.profit, is_present.weight))
        Q.append(is_present)
    print(Q)
    index+=1
    not_present = statusArr[index]
    not_present.level = prev.level + 1
    not_present.weight = prev.weight
    not_present.profit = prev.profit
    if bound(not_present.level, not_present.profit, not_present.weight) > max_profit:
        Q.append(not_present)
    index+=1
    

print(max_profit)
    



    


    