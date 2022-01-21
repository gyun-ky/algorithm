from collections import deque
import copy

def check_number(num):
    i = 2
    while i * i <= num:
        if num%i == 0:
            return False

        i+=1

    return True


T =int(input())

for _ in range(T):
    a, b = map(int, input().split())

    visited = [int(1e9)] * 10000
    visited[a] = 0

    q = deque()
    q.append((a, 0)) # 현재 숫자, 변환 횟수

    while q:
        num, cnt = q.popleft()
        num_str = list(str(num)) # t 각 자리 분리 위한 str list 변환

        if num == b :
            print(cnt)
            break
    
        for i in range(4): # 앞에서부터 한자리씩 탐색하며 바꾸기
            for s_num in range(10): # 0 ~ 9까지 변환한 (to) 숫자
                
                if i==0 and s_num == 0: # 1000의 자리수가 0인 경우
                    continue

                if int(num_str[i]) == s_num : # 변경하지 않는 경우
                    continue

                r_num = copy.deepcopy(num_str)
                r_num[i] = str(s_num) # 변환
                r_num = ''.join(r_num)

                if check_number(int(r_num)) and visited[int(r_num)] >= cnt+1:
                    q.append((int(r_num), cnt+1))
                    visited[int(r_num)] = cnt+1

    if visited[b] == int(1e9):
        print(0)

