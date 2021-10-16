
def dfs(indic, plus, minus, idx, total_cnt, target, op_sum, answer):
    
    if idx > total_cnt-1:
        return answer
    
    if indic == "plus":
        array = plus   
    else :
        array = minus
    
    op_sum += array[idx]
    print(op_sum)
    
    if idx == total_cnt-1: 
        if op_sum == target:
            answer += 1
            print("answer 증가 + "+ (str)(answer))
            return answer
        else:
            return answer
    else:
        if op_sum >= target:
            return answer
        else:
            answer = dfs("plus", plus, minus, idx+1, total_cnt, target, op_sum, answer)
            answer = dfs("minus", plus, minus, idx+1, total_cnt, target, op_sum, answer)

def solution(numbers, target):
    numbers.insert(0, 0)
    plus = numbers
    minus = [(-i) for i in numbers]
    print(plus)
    print(minus)
    
    total_cnt = len(plus)
    op_sum = 0 
    answer = 0
    
    answer = dfs("plus", plus, minus, 0, total_cnt, target, op_sum, answer)
    print(answer)

    return answer


solution([1, 1, 1, 1, 1], 3)
