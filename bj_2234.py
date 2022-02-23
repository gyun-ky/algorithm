# 성에 있는 방의 개수 
# 가장 넓은 방의 넓이
# 하나의 벽 제거하여 얻을 수 있는 가장 넓은 방의 크기



# # M x N이므로
# N, M 이 주어지고 
# 이진수의 각 비트로 주어짐 = 0001 - 서 / 0010 - 북 / 0100 - 동 / 1000 - 남

from collections import deque

N, M = map(int, input().split())

class space:
    west = False
    north = False
    east = False
    south = False

    def set_dir(self, west, north, east, south):
        self.west = west
        self.north = north
        self.east = east
        self.south = south


castle = [[space() for j in range(N)] for i in range(M)]
visited_total = [[0] * N for i in range(M)]

def set_space_dir(idx, flag, space):
    if idx == 0 and flag == '1':
        space.south = True

    if idx == 1 and flag == '1':
        space.east = True

    if idx == 2 and flag == '1':
        space.north = True

    if idx == 3 and flag == '1':
        space.west = True


for i in range(M):
    input_data = list(map(int, input().split()))
    for j in range(N):
        if i == 0: 
            castle[i][j].north = True

        if i == M-1:
            castle[i][j].south = True

        if j == 0:
            castle[i][j].west = True
        
        if j == N-1:
            castle[i][j].east = True

        num_bin = format(input_data[j],'b').zfill(4)
        for idx in range(4):
            set_space_dir(idx, num_bin[idx], castle[i][j])


# 방의 개수 room_cnt 
# 방의 크기를 구하기 위해서는 bfs

room_cnt = 0
max_size = 0
integrated_max_size = 0
for i in range(M):
    for j in range(N):
        q = deque()
        room_visitied = [[False]* N for i in range(M)]

        if visited_total[i][j] != 0:
            continue
        size = 0
        q.append((i, j))
        size +=1
        room_cnt += 1
        room_visitied[i][j] = True
        
        while q:
            row, col = q.popleft()

            if castle[row][col].north is False and room_visitied[row-1][col] is False:
                q.append((row-1, col))
                room_visitied[row-1][col] = True
                size +=1
            
            if castle[row][col].south is False and room_visitied[row+1][col] is False:
                q.append((row+1, col))
                room_visitied[row+1][col] = True
                size +=1
            
            if castle[row][col].west is False and room_visitied[row][col-1] is False:
                q.append((row, col-1))
                room_visitied[row][col-1] = True
                size +=1
            
            if castle[row][col].east is False and room_visitied[row][col+1] is False:
                q.append((row, col+1))
                room_visitied[row][col+1] = True
                size +=1

        if max_size < size:
            max_size = size

        for ni in range(M):
            for nj in range(N):
                if room_visitied[ni][nj] is True:
                    visited_total[ni][nj] = size
                    
                    if castle[ni][nj].north is True and ni-1 >= 0 and visited_total[ni-1][nj] != 0 and room_visitied[ni-1][nj] is False:
                        integrated_max_size = max(integrated_max_size, size + visited_total[ni-1][nj])

                    if castle[ni][nj].west is True and nj-1 >= 0 and visited_total[ni][nj-1] != 0 and room_visitied[ni][nj-1] is False:
                        integrated_max_size = max(integrated_max_size, size + visited_total[ni][nj-1])

                    if castle[ni][nj].south is True and ni+1 < M and visited_total[ni+1][nj] != 0 and room_visitied[ni+1][nj] is False:
                        integrated_max_size = max(integrated_max_size, size + visited_total[ni+1][nj])

                    if castle[ni][nj].east is True and nj+1 < N and visited_total[ni][nj+1] != 0 and room_visitied[ni][nj+1] is False:
                        integrated_max_size = max(integrated_max_size, size + visited_total[ni][nj+1])

                    


print(room_cnt)
print(max_size)
if M==1 and N == 1:
    print(visited_total[0][0])
else:
    print(integrated_max_size)