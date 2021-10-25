import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

each_operator_cnt = list(map(int, input().split()))

# 0 - + / 1 - - / 2 - * / 3 - /
operator = []
operator_cnt = 0

for i in range(4):
    for _ in range(each_operator_cnt[i]):
        operator.append(i)
        operator_cnt+=1

print(operator_cnt)

print(operator)



max = -1000000001
min = int(1e9)

operator_check = []



def search(idx, op, sum):
    global max, min, operator_check
    operator_check[op] = True
    if operator[op] == 0:
        print('+', end='')
        sum += data[idx]
        print(f"[{sum}]", end = ' ')
    elif operator[op] == 1:
        print('-', end = '')
        sum -= data[idx]
        print(f"[{sum}]", end = ' ')
    elif operator[op] == 2:
        print('*', end = '')
        sum *= data[idx]
        print(f"[{sum}]", end = ' ')
    else:
        print('/', end = '')
        if sum//data[idx] <0 : 
            sum = -(-sum // data[idx])
        else:
            sum = sum // data[idx]
        print(f"[{sum}]", end = ' ')

    # 끝
    if idx == N-1:
        print()
        if min>sum:
            min = sum
        if max<sum:
            max = sum
        operator_check[op] = False
        return 

    for i in range(operator_cnt):
        if operator_check[i] == False:
            search(idx+1, i, sum)


for op in range(operator_cnt):
    print("new")
    sum = data[0]
    operator_check = [False]*operator_cnt
    search(1, op, sum)    


print(max)
print(min)