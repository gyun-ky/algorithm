# A 출력
# 화면 전체 선택
# 전체 선택 내용 복사
# 버퍼가 비어있찌 않으면 버퍼내용 화면 문자열 뒤에 붙여넣기

# N 번을 눌렀을 때, 출력된 A 개수 최대

N = int(input())

# dp[i] = i번 눌렀을 때, 출력된 A의 개수 최대값
## 3번 이전일 때, 화면 전체 선택 -> 전체 선택내용 복사하고 -> 붙여넣기 = dp[i-3] * 2
## 2번 이전일 때, 버퍼에 있다면 ) dp[i-3] 두번 붙여넣기 / 버퍼에 없다면 AA
## 1번 이전일 때, 버퍼에 있다면 ) 붙여넣기 / 버퍼에 없다면 ) A
# dp[i] = max( 두번 이전 )

# 만약 복붙 했는데 A연속으로 친거랑 같으면 전체선택 해야


dp = [n for n in range(101)]

# dp[i-1] + buffer[i-1] 이 max 인 경우 -> buffer[i] = buffer[i-1]
# dp[i-3] * 2 가 max 인 경우 -> buffer[i] = dp[i-3] * 2
# dp[i-1] + 1이 max 인 경우 -> buffer[i] = 0

for i in range(7, 101):
    j = 3
    max_cnt = dp[i]
    while i-j > 0:
        max_cnt = max(max_cnt, dp[i-j] * (j-1))
        j+=1
    dp[i] = max_cnt

print(dp[N])
