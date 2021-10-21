import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
check = [False]*2000000

min = int(1e9)

def search(idx, sum):
    global min
    if idx == N:
        check[sum] = True
        if sum != 0 and min > sum:
            min = sum
        return
    
    search(idx+1, sum+S[idx])
    search(idx+1, sum)

    
search(0, 0)


if min == 1 : 
    for i in range(2, 2000000):
        if check[i] is False:
            print(i)
            break

else:
    print(1)