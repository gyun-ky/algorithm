# 좋아하는 초밥 고라 먹는다
# 같은 종류 초밥 있을 수 있음

# 임의의 위치부터 k개의 접시를 연속해서 먹은 경우 -> 할인된 정액 가격
# 초밥 쿠폰 제공 -> 위의 행사에 참가 경우, 추가로 무료 제공 (벨트위에 없을 경우 만들어서 제공)

# 가능한한 다양한 초밥 먹기
from collections import defaultdict
import sys
input = sys.stdin.readline
# 접시수 / 초밥 가짓수 / 연속 먹는 접시수 / 쿠포번호
N, d, k, c = map(int, input().split())

sushi = []
for i in range(N):
    sushi.append(int(input()))

# 7 9 7 30 2 27 9 25


sushi_expand = sushi * 2


answer = -1

start = 0
end = k
dict_s = defaultdict(int)


for i in range(0, k):
    dict_s[sushi_expand[i]] += 1


dict_s[c] += 1

while start < N:

    # 중복 제거
    answer = max(answer, len(dict_s.keys()))
    # 쿠폰번호 c 제거
    # array.pop()
    dict_s[sushi_expand[start]] -= 1
    if dict_s[sushi_expand[start]] == 0:
        del dict_s[sushi_expand[start]]
    start += 1
    
    dict_s[sushi_expand[end]] += 1
    end += 1

print(answer)

