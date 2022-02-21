# 막대 A, B, C
# 0 이상 원판 크기 똑같 / 종류 A, B, C
# 한 막대 가장 위 원판 다른 막대의 가장 위로

# 목표 A - A / B - B / C - C
# 최소로 움직여야

# 먼가 각 큐의 element가  AA CBA 이런식으로 리스트를 가지고 있는 건 어떠한가?

from collections import deque

init_data = []
for _ in range(3):
    input_str = input()
    if len(input_str) > 1:
        N, data = map(str, input_str.split()) 
        init_data.append(data)
    else:
        init_data.append('')


# q(1번째 막대 list, 2번째 막대 list, 3번째 막대 list, cnt)
q = deque()
q.append((init_data[0], init_data[1], init_data[2], 0))
visited = set()
visited.add(init_data[0] + '|' + init_data[1] + '|' + init_data[2])
# 만약 꺼냈는데 각각의 막대르르 조사
while q:
    first, second, third, cnt = q.popleft()

    # print("------")
    # print(cnt)
    # print(first_list)
    # print(second_list)
    # print(third_list)
    # print("[-------")
    all_same_flag = True
    for c_idx in range(len(first)):
        if first[c_idx] != 'A':
            all_same_flag = False

    for c_idx in range(len(second)):
        if second[c_idx] != 'B':
            all_same_flag = False

    for c_idx in range(len(third)):
        if third[c_idx] != 'C':
            all_same_flag = False

    if all_same_flag is True:
        print(cnt)
        break
    
    else:
        
        # 첫번째 막대 top 다른 두 막대에
        if len(first) != 0:
            circle = first[-1]

            next_second = second + circle
            next_third = third + circle
            
            next_first = first[0:-1]
            if (next_first + '|' + next_second + '|' + third) not in visited:
                q.append((next_first, next_second, third, cnt+1))
                visited.add(next_first + '|' + next_second + '|' + third)
            
            if (next_first + '|' + second + '|' + next_third) not in visited:
                q.append((next_first, second, next_third, cnt+1))
                visited.add(next_first + '|' + second + '|' + next_third)


        # 두번째 막대 top 다른 두 막대에
        if len(second) != 0 :
            circle = second[-1]

            next_first = first + circle
            next_third = third + circle

            next_second = second[0:-1]
            if (next_first + '|' + next_second + '|' + third) not in visited:
                q.append((next_first, next_second, third, cnt+1))
                visited.add(next_first + '|' + next_second + '|' + third)

            if (first + '|' + next_second + '|' + next_third) not in visited:
                q.append((first, next_second, next_third, cnt+1))
                visited.add(first + '|' + next_second + '|' + next_third)
 
        # 세번째 막대 top 다른 두 막대에
        if len(third) != 0 :
            circle = third[-1]

            next_first = first + circle
            next_second= second + circle

            next_third = third[0:-1]

            if (next_first + '|' + second + '|' + next_third) not in visited:
                q.append((next_first, second, next_third, cnt+1))  
                visited.add(next_first + '|' + second + '|' + next_third)
            
            if (first + '|' + next_second + '|' + next_third) not in visited:
                q.append((first, next_second, next_third, cnt+1))   
                visited.add(first + '|' + next_second + '|' + next_third)
          

# 한개라도 다르다면 -> 해당 top을 다른 두 막대에 옮기고, cnt 올리고 큐에 넣기

# 모두 다 같은 것이라면 cnt 반환 
