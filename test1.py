import heapq

def solution(jobs):
    
    jobs.sort(key = lambda x : (x[0], x[1]))
    jobs_len = len(jobs)
    
    total_time = 0
    
    start_time = -1 # 중복처리를 피해주기 위해서 heap에 넣어줄 범위 설정
    cur_time = 0
    checked_jobs_cnt = 0
    q = []
    while checked_jobs_cnt < jobs_len:
        
        for j in jobs:
            req_time, need_time = j
            if start_time < req_time <= cur_time :
                heapq.heappush(q, (need_time, req_time))
        
        if not q:
            cur_time += 1
            continue
        need_time, req_time = heapq.heappop(q)
        start_time = cur_time
        cur_time += need_time
        total_time += (cur_time - req_time)
        checked_jobs_cnt += 1
    
    answer = total_time // jobs_len
    return answer

solution([[0, 3], [1, 9], [2, 6]])