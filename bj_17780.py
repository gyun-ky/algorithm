# N*N 체스판, 사용하는 말 개수 K, 하나의 말 위에 다른 말 가능
# 턴 1 : 1 ~ K 번말 순서대로 
# 이동 방향 정해져있음

# 이동시, 위의 말도 같이 이동 / 가장 아래 말만 이동 가능
# 말이 네개 이상 쌓이면 -> 게임 종료

# 이동 규칙
## 이동 칸이 흰색 -> 이동 / 모두 위로 올린다
## 이동 칸이 빨간색 ->  이동 / 모두 거꾸로 reverse 해서 올린다
## 이동 칸이 파란색 -> A번말 이동 방향 반대로 하고 한칸 이동 / 반대한 후에도 파란색이면 방향만 반대로
## 체스판 벗어나는 경우 -> 파란색과 같음



dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

reverse_dir = [1, 0, 3, 2]

N, K = map(int, input().split())

chess = []
for _ in range(N):
    chess.append(list(map(int, input().split())))

# 0 - 흰 / 1- 빨 / 2- 파

horse = []
for i in range(K):
    horse.append(list(map(int, input().split())))
    horse[i][0] = horse[i][0]-1
    horse[i][1] = horse[i][1]-1
    horse[i][2] = horse[i][2]-1
    horse[i].append(True)
    # 값 idx에 맞게 보정


# [row, col, dir, base]
# dir 0 - 오 / dir 1 - 왼 / dir - 2 위 / dir - 3 아

chess_status = [[list() for j in range(N)] for _ in range(N)]


for i in range(len(horse)):
    row, col, dir, base = horse[i]
    chess_status[row][col].append(i)


turn = 0
while turn <= 1000:

    turn += 1

    for h in horse:
    
        crow, ccol, dir, base = h
        nrow = crow + dx[dir]
        ncol = ccol + dy[dir]

        if base is False:
            continue

        # 벗어나거나 파란색인 경우
        if nrow >= N or nrow < 0 or ncol >= N or ncol < 0 or chess[nrow][ncol] == 2:
            h[2] = reverse_dir[dir]
            
            
            nnrow = crow + dx[h[2]]
            nncol = ccol + dy[h[2]]
            # 방향 바꾸고 한번 갔는데 파란색이 아닌 경우
            if 0<= nnrow < N and 0<= nncol < N and chess[nnrow][nncol] != 2:
                nrow = nnrow
                ncol = nncol
            # 방향 바꾸고 한번 갔는데 파란색인 경우
            else:
                continue


        # 이동 칸이 흰색인 경우
        if chess[nrow][ncol] == 0:
            # 원래칸에 있던 horse들의 위치 모두 바꾼다
            for hIdx in chess_status[crow][ccol]:
                horse[hIdx][0] = nrow
                horse[hIdx][1] = ncol
                horse[hIdx][3] = False
            
            # 옮기는 칸에 아무것도 없다면
            if len(chess_status[nrow][ncol]) == 0:
                h_last_idx = chess_status[crow][ccol][0]
                horse[h_last_idx][3] = True
            
            # 모두 새로운 칸으로 옮긴다 
            chess_status[nrow][ncol] += chess_status[crow][ccol]
            # 원래칸 빈 list로 초기화
            chess_status[crow][ccol] = list()
            # 만약 새로운 칸으로 옮긴게 4개 이상? -> 종료
    
            if len(chess_status[nrow][ncol]) >= 4:
                print(turn)
                exit(0)
        else: 
            # 원래 칸에 있던 horse들의 위치 모두 바꾼다
            for hIdx in chess_status[crow][ccol]:
                    horse[hIdx][0] = nrow
                    horse[hIdx][1] = ncol
                    horse[hIdx][3] = False

            # 옮기는 칸에 아무것도 없다면
            if len(chess_status[nrow][ncol]) == 0:
                h_last_idx = chess_status[crow][ccol][-1]
                horse[h_last_idx][3] = True

            # 모두 새로운칸으로 reverse 된 후에 옮긴다
            chess_status[nrow][ncol] += list(reversed(chess_status[crow][ccol]))
            # 원래칸 빈 list로 초기화
            chess_status[crow][ccol] = list()
            # 만약 새로운 칸으로 옮긴게 4개 이상? -> 종료
        
            if len(chess_status[nrow][ncol]) >= 4:
                print(turn)
                exit(0)
        
    

print(-1)




