def solution(n, times):
    progress = []
    times.sort()
    
    # 초기에 모든 심사대에 사람 배정
    for i in range(len(times)):
        if i == n-1:
            # 인원 배정이 다 끝난 경우 가장 긴 심사대 소요 시간을 answer로 return 
            return times[i]
        else:
            n -= 1
            progress.append((i, 0, times[i], times[i]))
            

    answer = 0
    while True:
        if n==0 :
            progress.sort(key = lambda x : -x[2])
            answer = progress[0][2]
            break
            
        progress.sort(key = lambda x : (x[2], x[3]))
        a_end = progress[0][2] + progress[0][3]
        b_end = progress[1][2] + progress[1][3]
        if a_end < b_end:
            progress.append((progress[0][0], progress[0][2], progress[0][2]+progress[0][3], progress[0][3]))
            del progress[0]
            n-=1
            
        else:
            
            progress.append((progress[1][0], progress[1][2], progress[1][2]+progress[1][3], progress[1][3]))
            del progress[1]
            n-=1
        
    return answer