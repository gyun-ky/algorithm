#bj 14225 - 비트마스크로 다시 풀어보기
import itertools

check = [False]*200000

N = int(input())
data = list(map(int, input().split()))

for i in range(1<<N):
    print(f'{i} 번째')
    for j in range(N):
        if i&(1<<j):
            print(i&(1<<j))



# for cnt in range(N, 0, -1):
#     data_permut = list(itertools.permutations(data, cnt))
#     for l in data_permut:
#         sum = 0
#         for num in l:
#             sum += num
#         check[sum] = True

# for i in range(1, 2000000):
#     if check[i] == False:
#         print(i)
#         break
