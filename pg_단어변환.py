from collections import deque

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alpha = []
# alpha[0] - 0번째 자리 일 때, 바꿀 수 있는 문자 후보
# alpha[1] - 1번째 자리 일 때, 바꿀 수 있는 문자 후보
word_copy = []
answer = 0

def bfs(begin, target):
    global alpha, answer
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        begin_word, cnt = q.popleft()
        
        for i in range(len(begin_word)):
            
            for al in alpha[i]:
            
                if begin_word[i] == al:
                    continue

                n_begin = begin_word[0: i] + al + begin_word[i+1:]

                if n_begin not in word_copy:
                    continue
                
                if n_begin == target:
                    return cnt+1
                    
                q.append((n_begin, cnt+1))
    return 0
        

def solution(begin, target, words):
    global word_copy, alpha
    # begin -> targer 가장 짧은 변환 과정
    # word에 있는 단어로만 한번에 한개의 알파벳만 가능
    
    if target not in words:
        return 0
    word_copy = words
    
    len_word = len(words[0])
    alpha = [list() for _ in range(len_word)]
    
    for w in words:
        for idx in range(len_word):
            alpha[idx].append(w[idx])
    
    for idx in range(len_word):
        alpha[idx] = set(alpha[idx])
        

    
    return bfs(begin, target)