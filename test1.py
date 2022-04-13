from itertools import permutations
from copy import deepcopy

weak_size = 0


def dfs(fidx, pos, processed, check_list, order):
    
    if fidx == len(order):
        return int(1e9)
    
    


def solution(n, weak, dist):
    global weak_size

    weak_size = len(weak)
    n_weak = deepcopy(weak)
    for w in weak:
        n_weak.append(w+n)
        
    print(n_weak)
    
    answer = int(1e9)
    
    for start in range(0, weak_size):
        
        check_list = [n_weak[i] for i in range(start, start+weak_size)]
        
        for order in permutations(dist, len(dist)):
            
            answer = min(answer, dfs(0, check_list[0], 0, check_list, order))
                
    
    if answer == int(1e9):
        return -1
    else:
        return answer

    
    
        