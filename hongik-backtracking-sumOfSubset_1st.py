
n = int(input())
G = int(input())
sum_total = 0

w = list()
answer = list()


def promising(total):
    if total == G:
        return 2
    elif total < G:
        return 1
    else :
        return 0


def sum_of_subset(index, total):
    
    if promising(total) == 2:
        for i in answer:
            print(w[i], end=', ')
        print()
        return
    if promising(total) == 1:
        if index+1 > n:
            return
        answer.append(index+1)
        sum_of_subset(index+1, total+w[index+1])
        answer.pop(-1)
        sum_of_subset(index+1, total)
    if promising(total) == 0:
        return


w.append(0)
for i in range(0, n):
    tmp = int(input())
    w.append(tmp)

print(f'w = {w}')

sum_of_subset(0, 0)
