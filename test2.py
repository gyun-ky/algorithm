from collections import deque


def full_music(minfo):
    st, et, t, music_part = minfo.split(',')
    
    music_part = parse_music(music_part)
    
    sh, sm = map(int, st.split(':'))
    eh, em = map(int, et.split(':'))
    
    play_time = (eh*60 + em) - (sh*60 + sm)
    
    if play_time < len(music_part):
        full_music = music_part[0:play_time]
    else:
        iter_time = play_time // (len(music_part))
        last_time = play_time % (len(music_part))
        print(iter_time)
        print(last_time)
        full_music = music_part*iter_time + music_part[0:last_time]
    print(full_music)
    return (t, play_time, music_part)


def parse_music(m_str):
    m_str = list(m_str.strip())
    
    result = []
    
    for i in range(len(m_str)):
        
        if m_str[i] == '#':
            n_str = m_str[i-1] + m_str[i]
            result.pop()
            result.append(n_str)
        else:
            result.append(m_str[i])
            
    return result
    
def is_same(m, music, play_time, title, answer_list):

    # dp[i][j] music의 i까지보고 m의 j까지 봤을 때의 일치하는지?
    dp = [[0] * len(music) for _ in range(len(m))]

    for i in range(len(m)):
            for j in range(len(music)):
                if m[i] == music[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] == len(m):
                        answer_list.append((play_time, title))
                        return
                        
                else:
                    dp[i][j] = 0

def solution(m, musicinfos):
    

    m = parse_music(m)
    print(m)
    
    answer_list = []
    answer_list_idx = 0
    for minfo in musicinfos:
        title, play_time, music = full_music(minfo)
        
        is_same(m, music, play_time, title, answer_list)
    
        
                    
    if len(answer_list) == 0:
        answer = '(None)'
    else:
        answer_list.sort(key = lambda x: -x[0])
        answer = answer_list[0][1]
    
    return answer