graph = {}
total_cnt = 0

def dfs(s, cnt, answer):
    global graph
    
    if cnt == total_cnt:
        return answer
    
    
    # 만약 들어왔는데 graph에 없는 거면?
        # 다시 
    
    # 마지막인데 graph에 없는 거면?
    
    for f in graph[s]:
        # 아직 방문하지 않은 경우
        if f[1] == False:
            # 추가해줄 값이 graph에 없는 것인 경우
            if f[0] not in graph:
                if cnt == total_cnt-1:
                    # answer에 추가 후 dfs 진행
                    f[1] = True
                    answer.append(f[0])
                    return dfs(f[0], cnt+1, answer)
                # 아닌 경우에는 다음 값으로 
            # 추가해줄 값이 graph에 있는 값인 겨우
            else:
                f[1] = True
                answer.append(f[0])
                return dfs(f[0], cnt+1, answer)
        
    return answer
            

def solution(tickets):
    global graph, total_cnt
    
    for d, a in tickets:
        if d in graph:
            graph[d].append([a, False])
        else:
            graph[d] = [[a, False]]
        total_cnt+=1
    
    print(graph)
    for k in graph:
        graph[k].sort(key = lambda x : x[0])
    
    print(graph)
    
    answer = dfs('ICN', 0, ['ICN'])
    
    return answer