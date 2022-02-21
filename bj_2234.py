# 성에 있는 방의 개수 
# 가장 넓은 방의 넓이
# 하나의 벽 제거하여 얻을 수 있는 가장 넓은 방의 크기



# # M x N이므로
# N, M 이 주어지고 
# 이진수의 각 비트로 주어짐 = 0001 - 서 / 0010 - 북 / 0100 - 동 / 1000 - 남


N, M = map(int, input().split())

class space:
    west = False
    north = False
    east = False
    south = False

    def __init__(self, west, north, east, south):
        self.west = west
        self.north = north
        self.east = east
        self.south = south


for _ in range(M):
    
