# 3*3 배열 -> idx 1부터 시작
# R : 배열 A의 모든 행에 대해서 정렬을 수행 - 행의 개수 >= 열의 개수인 경우 적용
# C : 배열 A의 모든 열에 대해서 정렬 수행 - 행의 개수 < 열의 개수

# 정렬 : 각 배열의 수의 개수에 따라 정렬 1 - 1 / 2 - 1 / 3 - 2  -> 이런식으로 커지는 숫자 순서대로, 개수가 ASC 순서대로
# 가장 큰 행과 열을 기준을 모든 행의 크기가 변함 - 빈 곳에는 0
# 100 이 넘어가는 경우 -> 처음 100 개 제외 나머지는 버림

# r, c, k가 있을 때
# A[r][c] 의 값이 k가 되기 위한 최소 시간

r, c, k = map(int, input().split())
# idx 0에서 시작하는 것으로 보정
r = r-1
c = c-1

A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

row_cnt, col_cnt = 3, 3

# 시간 복잡도
# 0.5 초 -> 10000
# 100 * 100 = 10000 

# sort_rc
# A[r][c]가 k인지 점검
# 행의 개수 >= 열의 개수
## 모든 row list에 대해
## 각 수의 개수 카운팅 하면서 dict에 추가 - O(N)
## dict를 sort (1 idx 우선, 2 idx 다음)
## sort된 튜플을 풀어서 새로운 A로 생성 -> c 값 갱신

# 행의 개수 < 열의 개수
## A배열의 col에 대해서 dict로 생성 - O(N)
## dict를 sort
## A 를 빈 list로 row수에 맞춰 만들어 놓은 후에 
## sort된 튜플을 풀어서 각 row에 추가 -> r 값 갱신

def sort_R():
    global col_cnt
    new_A = []
    new_col_cnt = 0
    for row_list in A:
        dict = {}
        for elem in row_list:
            # 0인 경우 카운팅 하지 않으므로 skip
            if elem == 0:
                continue

            if elem in dict:
                dict[elem] += 1
            else:
                dict[elem] = 1
        
        sorted_tuple = sorted(dict.items(), key=lambda x:(x[1], x[0]))

        # col_cnt 갱신을 위한 가장 큰 col_cnt 측정
        # 100개로 valid
        sorted_tuple_len = len(sorted_tuple)
        if sorted_tuple_len > 50:
            sorted_tuple = sorted_tuple[0:50]
            new_col_cnt = max(new_col_cnt, 100)
        else:
            new_col_cnt = max(new_col_cnt, len(sorted_tuple)*2)
        # col_cnt 갤신
        col_cnt = new_col_cnt
        tmp = []
        for t in sorted_tuple:
            tmp.append(t[0])
            tmp.append(t[1])
        new_A.append(tmp)

    for row in new_A:
        rest_cnt = col_cnt - len(row)
        for _ in range(rest_cnt):
            row.append(0)

    return new_A


def sort_C():
    global row_cnt, col_cnt
    new_A = [[0]*100 for _ in range(100)]

    new_row_cnt = 0
    for cIdx in range(col_cnt):
        dict = {}
        for rIdx in range(row_cnt):
            # 0인 경우 카운팅 하지 않으므로 skip
            if A[rIdx][cIdx] == 0:
                continue
            
            if A[rIdx][cIdx] in dict:
                dict[A[rIdx][cIdx]] += 1
            else:
                dict[A[rIdx][cIdx]] = 1
        
        sorted_tuple = sorted(dict.items(), key=lambda x:(x[1], x[0]))
        # col_cnt 갱신을 위한 가장 큰 col_cnt 측정
        # 100개로 valid
        sorted_tuple_len = len(sorted_tuple)
        if sorted_tuple_len > 50:
            sorted_tuple = sorted_tuple[0:50]
            new_row_cnt = max(new_row_cnt, 100)
        else:
            new_row_cnt = max(new_row_cnt, len(sorted_tuple)*2)
     
        

        for tIdx in range(len(sorted_tuple)):
            new_A[tIdx*2][cIdx] = sorted_tuple[tIdx][0]
            new_A[tIdx*2+1][cIdx] = sorted_tuple[tIdx][1]

    # row cnt를 모든게 끝난 후 갱신 해주어야 함!!!
    row_cnt = new_row_cnt
    
    return new_A



time = 0
while True:

    if 0<=r<row_cnt and 0<=c<col_cnt and A[r][c] == k:
        print(time)
        break

    if time > 100:
        print(-1)
        break
    if row_cnt >= col_cnt:
        A = sort_R()

    else:
        A = sort_C()

    time+=1


    

    
