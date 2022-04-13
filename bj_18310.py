
# 안테나로부터 모든 집까지의 거리의 총합이 최소

# 동일 위치에 여러개 집 존재 가능

N = int(input())

house = list(map(int, input().split()))

house.sort()


print(house[(N-1)//2])