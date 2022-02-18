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

# 만약 꺼냈는데 각각의 막대르르 조사
while q:
    first, second, third, cnt = q.popleft()
    first_list = list(first.strip())
    second_list = list(second.strip())
    third_list = list(third.strip())

    # print("------")
    # print(cnt)
    # print(first_list)
    # print(second_list)
    # print(third_list)
    # print("[-------")
    all_same_flag = True
    for c in first_list:
        if c != 'A':
            all_same_flag = False

    for c in second_list:
        if c != 'B':
            all_same_flag = False

    for c in third_list:
        if c != 'C':
            all_same_flag = False

    if all_same_flag is True:
        print(cnt)
        break

    else:
        # 첫번째 막대 top 다른 두 막대에
        if first_list:
            circle = first_list[-1]

            second_list.append(circle)
            third_list.append(circle)

            next_first = ''.join(first_list[0:len(first_list)-1])
            next_second = ''.join(second_list)
            next_third = ''.join(third_list)
            q.append((next_first, next_second, third, cnt+1))
            q.append((next_first, second, next_third, cnt+1))
            del second_list[-1]
            del third_list[-1]


        # 두번째 막대 top 다른 두 막대에
        if second_list :
            circle = second_list[-1]

            first_list.append(circle)
            third_list.append(circle)

            next_second = ''.join(second_list[0:len(second_list)-1])
            next_first = ''.join(first_list)
            next_third = ''.join(third_list)
            q.append((next_first, next_second, third, cnt+1))
            q.append((first, next_second, next_third, cnt+1))
            del first_list[-1]
            del third_list[-1]
        
        # 세번째 막대 top 다른 두 막대에
        if third_list :
            circle = third_list[-1]

            first_list.append(circle)
            second_list.append(circle)

            next_third = ''.join(third_list[0:len(third_list)-1])
            next_first = ''.join(first_list)
            next_second = ''.join(second_list)
            q.append((next_first, second, next_third, cnt+1))  
            q.append((first, next_second, next_third, cnt+1))   
            del first_list[-1]
            del second_list[-1]
        

# 한개라도 다르다면 -> 해당 top을 다른 두 막대에 옮기고, cnt 올리고 큐에 넣기

# 모두 다 같은 것이라면 cnt 반환 
