n = int(input())
# 전체 weight
W = int(input())

# 아이템 총합
total = 0

# 요소를 모두 더해서 W가 되는 부분집합에 포함되는지
include = [False] * n+1

# 오름 차순으로 weight 받는다
w = [0] * (n+1)
for i in range(1, n+1):
    w[i] = int(input)
    total += w[i]



def promising(index):
    return weight + total >= W and (weight == W | weight + w[index+1] <= W)

def sumOfSubset(index, weight, total):
    
    if promising(index):
        if wieght == W:
            for i in range(0, i):
                if include[i] == True:
                    print(f'{i}', end=" ")

        else:
            include[i+1] = True
            sum_of_subset(i+1, weight+w[i+1], total - w[i+1])
            include[i+1] = False
            sum_of_subset(i+1, weight, total-w[i+1])
